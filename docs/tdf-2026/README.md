# Tour de France 2026 tracker

A static, self-updating dashboard for following the 2026 Tour de France (Barcelona Grand Départ, July 4 → Paris finale, July 26), published via GitHub Pages at:

**https://joe-garvin.github.io/claude-knowledge-base/tdf-2026/**

This lives under this repo's `docs/` folder (Pages source), alongside the rest of the knowledge base's published content.

## How it works

- Plain HTML/CSS/JS, no build step, no framework. Pages fetch shared JSON snapshots in `data/` at load time.
- A Python scraper (`scraper/`) runs on a GitHub Actions cron three times a day during the race (`.github/workflows/tdf-2026-scrape.yml`, repo root), writing fresh JSON into `data/` and committing it back to `main`.
- The front end never goes blank: a failed or partial scrape leaves the last good snapshot in place, and `assets/js/common.js` shows a stale-data banner client-side if `data/meta.json` is more than 26 hours old.

## Local development

This is a static site — any static file server works, run from this folder:

```
cd docs/tdf-2026
python3 -m http.server 8000
```

Then open `http://localhost:8000/`.

## Repository layout

See `data/` for the JSON data contract, `scraper/` for the scraper and its README, and `../../.github/workflows/tdf-2026-scrape.yml` (repo root) for the automation.

## Data refresh

The scraper runs automatically on a cron schedule (see `.github/workflows/tdf-2026-scrape.yml` at the repo root — cron paths in GitHub Actions are always relative to the repo root, not this folder) and can also be triggered manually from the Actions tab (`workflow_dispatch`). As an exception to this repo's usual "no direct pushes to main" convention, that workflow commits straight to `main` since GitHub Pages only publishes from `main` — see the workflow file for the full reasoning.
