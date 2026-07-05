# Scraper

Refreshes `data/standings.json`, `data/results/stage-N.json`, and
`data/meta.json` once a day (three times during the race — see
`../../../.github/workflows/tdf-2026-scrape.yml` at the repo root). Never
destructive: a section only gets overwritten if the new scrape validates
against the contract; otherwise the prior good file stays in place and
`meta.json` records the failure.

## Running it

This scraper lives at `docs/tdf-2026/scraper/` inside the
`claude-knowledge-base` repo. `scrape.py` resolves its own paths relative
to its own file location (not the current working directory), so it can
be run either from this folder or from the repo root:

```
pip install -r requirements.txt
python3 scrape.py
```

`net.py` and `sources/` resolve as plain imports because `scrape.py` adds
its own directory to `sys.path`.

## Sources

| Data | Primary | Fallback 1 | Fallback 2 |
|---|---|---|---|
| GC + jersey standings | `sources/letour.py` (official rankings) | `sources/pcs.py` (ProCyclingStats) | `sources/wikipedia.py` |
| Stage top 10 | `sources/letour.py` | `sources/pcs.py` | `sources/wikipedia.py` (winner only) |
| Start/finish times | seed data in `data/watch.json` | `sources/letour.py` (best-effort) | — |

**Why letour.fr is primary (verified live, 2026-07-04, race day):**
ProCyclingStats returns HTTP 403 to every automated fetch attempted
against it (this scraper's, and a plain `WebFetch`) — it has never
succeeded once against the live 2026 race. Wikipedia's article only
carries thin summary tables (whole-field GC, but only the stage *winner*
for individual stage results, not a top 10), and its rank column being a
row-header `<th>` once caused a real bug (see git history: a mismatched
column shifted a team name into the rider field, undetected until a
too-weak validator let a 1-row garbage table overwrite good standings —
that's also why `MIN_GC_ROWS` exists in `scrape.py`).

letour.fr's `/en/rankings/stage-N` pages, by contrast, serve the full,
official, structured ranking tables (184+ rows, every classification)
via a plain cookie-less GET, once you know that page's per-classification
AJAX hash tokens — which are baked into the page HTML and are
deterministic (stable across repeat fetches, not tied to a session). See
`sources/letour.py`'s module docstring for exactly how the tab/hash/AJAX
mechanism was reverse-engineered from the rendered HTML, and why a team
time trial's stage-only ranking falls back to the cumulative GC table.

ProCyclingStats and Wikipedia stay wired as fallbacks in case letour.fr's
markup or hash scheme ever changes; `sources/pcs.py`'s parser remains
unverified against a live page (still 403-blocked) and is documented as
such in its module docstring.

Before trusting a live run: check `scraper/.cache/*.html` (written per
run, gitignored) against the fixtures in `scraper/tests/fixtures/`. If a
source's real markup doesn't match, update that source's parser and
refresh the fixture — the parser tests will catch drift going forward.

We evaluated the `procyclingstats` PyPI wrapper before building the PCS
source; given the inability to verify it against a live, current PCS page
during this build, we went with a direct `requests` + `BeautifulSoup`
scraper instead, so the parsing logic and its failure modes are fully
visible and testable here.

## Tests

Fixture-based parser tests, no network required:

```
cd scraper
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Design notes

- `net.py` centralizes retries (3 attempts, backoff), a descriptive
  User-Agent, a polite delay between requests, and raw-HTML caching to
  `scraper/.cache/` for post-run debugging.
- `scrape.py` validates every section before writing it (ranks sequential
  from 1, required fields present) and only touches `data/*.json` files
  whose new scrape validated.
- `standings.json`'s `history.gc_leader_by_stage` is upserted by stage
  number (never blind-appended), so reruns on the same day — a second
  cron, a manual `workflow_dispatch`, a retry — stay idempotent.
- `scrape.py` exits non-zero only when a source fails outright; the
  GitHub Actions workflow is structured to commit whatever good state
  exists regardless of this script's exit code, then surface the failure
  separately (Section 7 of the build spec).
