#!/usr/bin/env python3
"""Generate the 21 stage HTML files from a single shared template.

Run once (and any time the template changes):

    python3 scraper/build_pages.py

All 21 files are near-identical shells — the only per-stage difference is
the stage number baked into the page. Everything else (route, profile,
results) is loaded at runtime by assets/js/stage.js from data/race.json,
data/results/stage-N.json, and data/watch.json.
"""

import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
STAGES_DIR = REPO_ROOT / "stages"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Stage {n} — Tour de France 2026 tracker</title>
<meta name="description" content="Route, elevation profile, climbs, and results for stage {n} of the 2026 Tour de France.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/site.css">
<link rel="icon" href="../assets/img/favicon.svg" type="image/svg+xml">
</head>
<body data-stage="{n}">
<header class="site-header" id="site-header"></header>

<main class="site-main">
  <div class="stale-banner" id="stale-banner" role="status"></div>

  <div class="stage-header" id="stage-header">
    <p class="stage-header__eyebrow">Loading stage {n}…</p>
  </div>

  <section aria-labelledby="preview-title">
    <h2 id="preview-title" class="section-title">Preview</h2>
    <p id="stage-preview" class="muted">Loading…</p>
  </section>

  <section aria-labelledby="profile-title">
    <h2 id="profile-title" class="section-title">Elevation profile</h2>
    <div class="card">
      <div class="chart-wrap chart-wrap--tall">
        <canvas id="profile-chart"></canvas>
      </div>
    </div>
  </section>

  <section aria-labelledby="climbs-title">
    <h2 id="climbs-title" class="section-title">Categorized climbs</h2>
    <div class="card table-wrap">
      <table id="climbs-table">
        <thead>
          <tr>
            <th>Climb</th>
            <th>Category</th>
            <th class="num">Km mark</th>
            <th class="num">Length</th>
            <th class="num">Avg gradient</th>
          </tr>
        </thead>
        <tbody></tbody>
      </table>
      <p class="muted faint" id="climbs-empty" style="display:none;">No categorized climbs on this stage.</p>
    </div>
  </section>

  <section aria-labelledby="result-title">
    <h2 id="result-title" class="section-title">Result</h2>
    <div class="card" id="result-card">
      <p class="muted">Loading…</p>
    </div>
  </section>

  <nav class="stage-nav" aria-label="Stage navigation" id="stage-nav"></nav>

  <p class="updated-line" data-updated-line></p>
</main>

<footer class="site-footer">
  <p>Data from ProCyclingStats and Wikipedia, refreshed automatically. Not an official Tour de France product.</p>
</footer>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation@3"></script>
<script type="module" src="../assets/js/stage.js"></script>
</body>
</html>
"""


def main():
    STAGES_DIR.mkdir(exist_ok=True)
    for n in range(1, 22):
        html = TEMPLATE.format(n=n)
        out_path = STAGES_DIR / f"stage-{n:02d}.html"
        out_path.write_text(html, encoding="utf-8")
        print(f"wrote {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
