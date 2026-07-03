"""Wikipedia fallback scraper for GC standings and stage winners.

Wikipedia's race-article tables are hand-maintained wikitext rendered to
standard `wikitable` HTML, which tends to be more stable than a source
site's own markup — the reason the build spec lists it as the fallback
rather than the primary. Confirmed against the live "2025 Tour de France"
article's structure while building this (see scraper/README.md); the 2026
article should follow the same shape once the race is underway.

Wikipedia's race-summary "Route and stages" table only lists the stage
winner, not a full top 10 — so fetch_stage_result here can only ever
produce a single-entry (rank 1) result. That's a real, validated result
(not a parse failure), just a thinner one than PCS would give.
"""

from bs4 import BeautifulSoup

from net import fetch_html
from sources.table_parse import cell_text, column_index, find_table_by_header, parse_rank

BASE_URL = "https://en.wikipedia.org/wiki"


def _article_url(year):
    return f"{BASE_URL}/{year}_Tour_de_France"


def fetch_standings(session, year, cache_dir=None):
    """Returns {"classifications": {...}} with gc populated and
    points/kom/youth as empty lists (Wikipedia's race-summary article
    doesn't carry live secondary classifications), or None if no GC
    table could be found."""
    html = fetch_html(session, _article_url(year), cache_dir, "wikipedia_standings")
    soup = BeautifulSoup(html, "lxml")

    gc_table, gc_headers = find_table_by_header(soup, "rider")
    if gc_table is None:
        return None

    rank_i = column_index(gc_headers, "rank", "pos")
    rider_i = column_index(gc_headers, "rider")
    team_i = column_index(gc_headers, "team")
    time_i = column_index(gc_headers, "time")

    gc_rows = []
    for tr in gc_table.find_all("tr"):
        cells = tr.find_all("td")
        if not cells or rider_i is None or rider_i >= len(cells):
            continue
        rider = cell_text(cells, rider_i)
        if not rider:
            continue
        gc_rows.append({
            "rank": parse_rank(cell_text(cells, rank_i), len(gc_rows) + 1),
            "rider": rider,
            "team": cell_text(cells, team_i) or "",
            "gap": cell_text(cells, time_i) or "—",
        })

    if not gc_rows:
        return None

    return {"classifications": {"gc": gc_rows, "points": [], "kom": [], "youth": []}}


def fetch_stage_result(session, year, stage_number, cache_dir=None):
    """Returns {"top10": [<winner only>]} or None."""
    html = fetch_html(session, _article_url(year), cache_dir, f"wikipedia_stage_{stage_number:02d}_result")
    soup = BeautifulSoup(html, "lxml")

    for table in soup.find_all("table", class_="wikitable"):
        headers = [th.get_text(strip=True).lower() for th in table.find_all("th")]
        if not any("winner" in h or "rider" in h for h in headers):
            continue
        stage_i = column_index(headers, "stage")
        rider_i = column_index(headers, "winner", "rider")
        team_i = column_index(headers, "team")
        if stage_i is None or rider_i is None:
            continue
        for tr in table.find_all("tr"):
            cells = tr.find_all("td")
            if not cells or stage_i >= len(cells):
                continue
            if parse_rank(cell_text(cells, stage_i), -1) != stage_number:
                continue
            rider = cell_text(cells, rider_i)
            if not rider:
                continue
            return {"top10": [{
                "rank": 1,
                "rider": rider,
                "team": cell_text(cells, team_i) or "",
                "time": "",
                "gap": "—",
            }]}
    return None
