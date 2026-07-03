# Meta

System notes, conventions, and a running changelog for this repo.

## File naming conventions

- Lowercase, hyphen-separated (e.g. `azure-smb-messaging-framework.md`)
- Each file should open with a comment block noting creation date and source session/project

## Folder conventions

- `projects/` — one file or subfolder per active project
- `areas/` — ongoing responsibilities, grouped by domain
- `resources/` — reusable reference material
- `archive/` — completed or inactive material; preserve but don't actively maintain
- `meta/` — this folder; system-level documentation

## Changelog

| Date | Change |
|------|--------|
| 2026-03-12 | Initial repo created and scaffolded via Claude GitHub MCP integration |
| 2026-07-03 | Added `docs/tdf-2026/` — a self-updating Tour de France 2026 tracker — plus `.github/workflows/tdf-2026-scrape.yml` (repo root) and `.gitignore` (new file). The scrape workflow commits directly to `main` as a deliberate exception to the "no direct pushes to main" convention, since GitHub Pages only publishes from `main`/`docs`; see the workflow file and `docs/tdf-2026/README.md` for details. |
