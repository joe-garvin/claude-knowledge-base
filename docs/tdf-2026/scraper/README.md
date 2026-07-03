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

| Data | Primary | Fallback |
|---|---|---|
| GC + jersey standings | `sources/pcs.py` (ProCyclingStats) | `sources/wikipedia.py` |
| Stage top 10 | `sources/pcs.py` | `sources/wikipedia.py` (winner only) |
| Start/finish times | seed data in `data/watch.json` | `sources/letour.py` (best-effort) |

**A note on verification:** ProCyclingStats returned HTTP 403 to automated
fetches (both this scraper's and a plain `WebFetch`) while this scraper
was being built, ahead of the 2026 race. `sources/pcs.py`'s parser is
therefore header-driven (matches columns by header text like "Rider" or
"Gap" rather than hard-coded positions) and documented as unverified
against a live page — see the module docstring. `sources/wikipedia.py`
was checked against the live "2025 Tour de France" article's table
structure and should carry over to the 2026 article once it exists.

Before trusting a live run: check `scraper/.cache/*.html` (written per
run, gitignored) against the fixtures in `scraper/tests/fixtures/`. If
PCS's real markup doesn't match, update `sources/pcs.py`'s column-header
names and refresh the fixture — the parser tests will catch drift going
forward.

We evaluated the `procyclingstats` PyPI wrapper before building this;
given the inability to verify it against a live, current PCS page during
this build, we went with a direct `requests` + `BeautifulSoup` scraper
instead, so the parsing logic and its failure modes are fully visible and
testable here. Revisit that package if PCS's markup proves more volatile
than expected.

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
