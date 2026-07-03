"""ProCyclingStats scraper — primary source for standings and stage results.

PCS's exact markup could not be verified live while building this scraper:
the site returned HTTP 403 to automated fetches during development, which
is exactly the kind of source fragility this build spec warns about.
Parsing is header-driven (see sources/table_parse.py) rather than tied to
specific CSS class names, which tends to survive minor markup changes
better than hard-coded column positions — but it is unverified against a
real page.

Before relying on this in production, spot-check the cached HTML this
writes to scraper/.cache/ against the selectors below and adjust if PCS's
real markup doesn't match. Until then, a parse failure here is not
silent: every function returns None on anything unexpected, which
scrape.py treats as a failed source and falls through to Wikipedia —
it never crashes the run or clobbers a good snapshot.
"""

from bs4 import BeautifulSoup

from net import fetch_html
from sources.table_parse import cell_text, column_index, find_table_by_header, parse_rank

BASE_URL = "https://www.procyclingstats.com"
CLASSIFICATION_SLUGS = {"gc": "gc", "points": "points", "kom": "kom", "youth": "youth"}


def _parse_results_rows(table, headers, is_points_classification=False):
    rank_i = column_index(headers, "rnk", "rank", "pos")
    rider_i = column_index(headers, "rider")
    team_i = column_index(headers, "team")
    time_i = column_index(headers, "time")
    gap_i = column_index(headers, "gap", "b.i.t")
    points_i = column_index(headers, "points", "pnt")

    rows = []
    for tr in table.find_all("tr"):
        cells = tr.find_all("td")
        if not cells or rider_i is None or rider_i >= len(cells):
            continue
        rider = cell_text(cells, rider_i)
        if not rider:
            continue
        entry = {
            "rank": parse_rank(cell_text(cells, rank_i), len(rows) + 1),
            "rider": rider,
            "team": cell_text(cells, team_i) or "",
        }
        if is_points_classification:
            points_text = cell_text(cells, points_i)
            entry["points"] = int(points_text) if points_text and points_text.isdigit() else 0
        else:
            entry["time"] = cell_text(cells, time_i) or ""
            entry["gap"] = cell_text(cells, gap_i) or "—"
        rows.append(entry)
    return rows


def fetch_stage_result(session, year, stage_number, cache_dir=None):
    """Returns {"top10": [...]} or None if the page couldn't be fetched
    or parsed into a plausible results table."""
    url = f"{BASE_URL}/race/tour-de-france/{year}/stage-{stage_number}"
    html = fetch_html(session, url, cache_dir, f"pcs_stage_{stage_number:02d}_result")
    soup = BeautifulSoup(html, "lxml")
    table, headers = find_table_by_header(soup, "rider")
    if table is None:
        return None
    rows = _parse_results_rows(table, headers)
    if not rows:
        return None
    return {"top10": rows[:10]}


def fetch_standings(session, year, cache_dir=None):
    """Returns {"classifications": {...}} or None if the GC table (the
    only classification treated as required) couldn't be found."""
    classifications = {}
    for key, slug in CLASSIFICATION_SLUGS.items():
        url = f"{BASE_URL}/race/tour-de-france/{year}/{slug}"
        try:
            html = fetch_html(session, url, cache_dir, f"pcs_standings_{key}")
        except RuntimeError:
            continue
        soup = BeautifulSoup(html, "lxml")
        table, headers = find_table_by_header(soup, "rider")
        if table is None:
            continue
        rows = _parse_results_rows(table, headers, is_points_classification=(key in ("points", "kom")))
        if rows:
            classifications[key] = rows

    if not classifications.get("gc"):
        return None
    return {"classifications": classifications}
