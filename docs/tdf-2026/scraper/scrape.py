#!/usr/bin/env python3
"""Daily scrape entry point. Run from the repo root:

    python3 scraper/scrape.py

Order of operations (Section 6 of the build spec):

  1. Load the existing data/ snapshot (the current good state).
  2. Determine which stages should be complete based on today's date vs.
     data/race.json's stage dates.
  3. Scrape standings (PCS, falling back to Wikipedia) and any
     newly-due stage results.
  4. Validate every scraped section against the contract.
  5. Only overwrite a section if its scrape validated — a failed section
     keeps the prior file and is marked "failed"/"partial" in meta.json.
  6. Write meta.json last, with a fresh last_updated and per-section
     status. No "stale" flag: staleness is computed client-side.
  7. Exit non-zero only on total failure; the GitHub Actions workflow
     commits whatever good state exists regardless of this script's
     exit code (see .github/workflows/scrape.yml).

Never destructive: a run that finds nothing new, or fails outright,
leaves data/ exactly as it was except for meta.json's status/timestamp.
"""

import datetime
import json
import pathlib
import sys
import time

import requests

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from sources import pcs, wikipedia, letour  # noqa: E402

DATA_DIR = REPO_ROOT / "data"
RESULTS_DIR = DATA_DIR / "results"
CACHE_DIR = pathlib.Path(__file__).resolve().parent / ".cache"

RACE_YEAR = 2026
STAGE_RESULT_DELAY_SECONDS = 1.5


def load_json(path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return default


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def utc_now_iso():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def validate_gc_rows(rows):
    if not rows:
        return False
    for i, r in enumerate(rows, start=1):
        if r.get("rank") != i or not r.get("rider") or not r.get("team"):
            return False
    return True


def validate_top10(rows):
    if not rows:
        return False
    for i, r in enumerate(rows, start=1):
        if r.get("rank") != i or not r.get("rider"):
            return False
    return True


def validate_standings(standings):
    classifications = (standings or {}).get("classifications", {})
    return validate_gc_rows(classifications.get("gc"))


def upsert_gc_history(history, stage_number, rider):
    kept = [h for h in history if h.get("stage") != stage_number]
    kept.append({"stage": stage_number, "rider": rider})
    kept.sort(key=lambda h: h["stage"])
    return kept


def due_stage_numbers(race, today_iso):
    return [s["number"] for s in race["stages"] if s["date"] <= today_iso]


def scrape_standings(session, existing_standings, prior_section_meta):
    for source_name, fetcher in (("procyclingstats", pcs.fetch_standings), ("wikipedia", wikipedia.fetch_standings)):
        try:
            result = fetcher(session, RACE_YEAR, cache_dir=CACHE_DIR)
        except Exception as e:
            print(f"[standings] {source_name} fetch failed: {e}", file=sys.stderr)
            continue
        if result and validate_standings(result):
            return result["classifications"], source_name

    print("[standings] all sources failed validation; keeping prior snapshot", file=sys.stderr)
    return None, prior_section_meta.get("source", "unknown")


def scrape_due_results(session, due_numbers):
    """Returns (results_written: list[int], any_attempted: bool, all_ok: bool)."""
    written = []
    attempted = False
    all_ok = True

    for n in due_numbers:
        existing = load_json(RESULTS_DIR / f"stage-{n:02d}.json", {"stage": n, "completed": False})
        if existing.get("completed"):
            continue

        attempted = True
        result, source_name = None, None
        for name, fetcher in (("procyclingstats", pcs.fetch_stage_result), ("wikipedia", wikipedia.fetch_stage_result)):
            try:
                candidate = fetcher(session, RACE_YEAR, n, cache_dir=CACHE_DIR)
            except Exception as e:
                print(f"[stage {n}] {name} fetch failed: {e}", file=sys.stderr)
                continue
            if candidate and validate_top10(candidate.get("top10")):
                result, source_name = candidate, name
                break

        if result:
            result["stage"] = n
            result["completed"] = True
            result.setdefault("date", None)
            write_json(RESULTS_DIR / f"stage-{n:02d}.json", result)
            written.append(n)
            print(f"[stage {n}] wrote result from {source_name}")
        else:
            all_ok = False
            print(f"[stage {n}] no source produced a valid result; leaving as awaiting", file=sys.stderr)

        time.sleep(STAGE_RESULT_DELAY_SECONDS)

    return written, attempted, all_ok


def refresh_watch_times(session, due_numbers):
    """Best-effort only; never affects scrape_status. See sources/letour.py."""
    watch = load_json(DATA_DIR / "watch.json", {"stages": []})
    changed = False
    for n in due_numbers:
        try:
            schedule = letour.fetch_stage_schedule(session, n, cache_dir=CACHE_DIR)
        except Exception as e:
            print(f"[watch {n}] letour.com fetch failed (non-fatal): {e}", file=sys.stderr)
            continue
        if not schedule:
            continue
        for entry in watch["stages"]:
            if entry["number"] == n:
                entry.update(schedule)
                changed = True
    if changed:
        write_json(DATA_DIR / "watch.json", watch)


def main():
    race = load_json(DATA_DIR / "race.json", None)
    if race is None:
        print("data/race.json is missing — cannot determine the stage schedule, aborting", file=sys.stderr)
        sys.exit(1)

    standings = load_json(DATA_DIR / "standings.json", {
        "as_of_stage": 0,
        "classifications": {"gc": [], "points": [], "kom": [], "youth": []},
        "history": {"gc_leader_by_stage": []},
    })
    meta = load_json(DATA_DIR / "meta.json", {"sections": {}})
    prior_sections = meta.get("sections", {})

    today_iso = datetime.date.today().isoformat()
    due = due_stage_numbers(race, today_iso)

    session = requests.Session()
    section_status = {}
    overall_ok = True

    written_results, attempted, results_ok = scrape_due_results(session, due)

    new_classifications, standings_source = scrape_standings(session, standings, prior_sections.get("standings", {}))
    if new_classifications:
        as_of_stage = standings.get("as_of_stage", 0)
        gc_leader = new_classifications["gc"][0]["rider"] if new_classifications.get("gc") else None
        history = standings["history"]["gc_leader_by_stage"]

        if written_results:
            as_of_stage = max(as_of_stage, max(written_results))
        if gc_leader and as_of_stage > 0:
            history = upsert_gc_history(history, as_of_stage, gc_leader)

        standings = {
            "as_of_stage": as_of_stage,
            "classifications": new_classifications,
            "history": {"gc_leader_by_stage": history},
        }
        write_json(DATA_DIR / "standings.json", standings)
        section_status["standings"] = {"status": "ok", "source": standings_source, "scraped_at": utc_now_iso()}
    else:
        section_status["standings"] = {
            **prior_sections.get("standings", {"source": "unknown", "scraped_at": None}),
            "status": "failed",
        }
        overall_ok = False

    if attempted:
        section_status["results"] = {
            "status": "ok" if results_ok else "partial",
            "source": "procyclingstats",
            "scraped_at": utc_now_iso(),
        }
        if not results_ok:
            overall_ok = False
    else:
        section_status["results"] = prior_sections.get("results", {"status": "ok", "source": "seed", "scraped_at": utc_now_iso()})

    refresh_watch_times(session, due)

    meta_out = {
        "last_updated": utc_now_iso(),
        "scrape_status": "ok" if overall_ok else ("partial" if section_status["standings"]["status"] == "ok" else "failed"),
        "sections": section_status,
        "notes": meta.get("notes", ""),
    }
    write_json(DATA_DIR / "meta.json", meta_out)

    print(f"scrape complete: scrape_status={meta_out['scrape_status']}")
    if not overall_ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
