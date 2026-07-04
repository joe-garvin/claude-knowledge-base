"""Wikipedia scraper for GC + jersey standings and stage winners.

Primary source in practice: ProCyclingStats blocks automated fetches with
HTTP 403, so the daily scrape relies on this. Verified against the live
"2026 Tour de France" article once the race was underway (a saved copy is
in scraper/tests/fixtures/).

The article carries, in this order:
  - a summary table ("Stage | Winner | General classification | Points… |
    Mountains… | Young rider… | Team… | Combativity") — the current jersey
    wearers and each stage's winner; and
  - four full classification tables (GC, points, mountains, youth) whose
    first column (rank) is a row-header <th>. Body cells must therefore be
    read as th+td, not td alone, or every column shifts left by one — the
    bug that once wrote a team name into the rider field.
"""

from bs4 import BeautifulSoup

from net import fetch_html

BASE_URL = "https://en.wikipedia.org/wiki"

# The four classification tables always appear in this order on the article.
CLASSIFICATION_ORDER = ["gc", "points", "kom", "youth"]
VALUE_FIELD = {"gc": "time", "points": "points", "kom": "points", "youth": "time"}


def _article_url(year):
    return f"{BASE_URL}/{year}_Tour_de_France"


def _header_cells(table):
    row = table.find("tr")
    if not row:
        return []
    return [c.get_text(strip=True).lower() for c in row.find_all(["th", "td"])]


def _cell_text(cells, i):
    if i is None or i >= len(cells):
        return ""
    link = cells[i].find("a")
    return (link or cells[i]).get_text(strip=True)


def _col_index(headers, *names):
    for name in names:
        for i, h in enumerate(headers):
            if h == name or name in h:
                return i
    return None


def _classification_tables(soup):
    """Classification tables (rank + rider + team + time/points), in the
    document order that maps to GC, points, mountains, youth."""
    found = []
    for table in soup.find_all("table"):
        headers = _header_cells(table)
        has_rider = any("rider" in h for h in headers)
        has_team = any("team" in h for h in headers)
        has_value = any(("time" in h or "points" in h) for h in headers)
        has_rank = any(h in ("rank", "pos") for h in headers)
        if has_rider and has_team and has_value and has_rank:
            found.append((table, headers))
    return found


def _parse_classification(table, headers, value_field):
    rider_i = _col_index(headers, "rider")
    team_i = _col_index(headers, "team")
    value_i = _col_index(headers, value_field)

    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = tr.find_all(["th", "td"])
        rider = _cell_text(cells, rider_i)
        if not rider:
            continue
        entry = {"rank": len(rows) + 1, "rider": rider, "team": _cell_text(cells, team_i)}
        value = _cell_text(cells, value_i)
        if value_field == "time":
            entry["time"] = value
            entry["gap"] = value if value.startswith("+") else "—"
        else:
            digits = "".join(ch for ch in value if ch.isdigit())
            entry["points"] = int(digits) if digits else 0
        rows.append(entry)
    return rows


def fetch_standings(session, year, cache_dir=None):
    """Returns {"classifications": {gc, points, kom, youth}} or None if the
    GC table can't be found. Each classification carries teams; missing
    ones come back as empty lists."""
    html = fetch_html(session, _article_url(year), cache_dir, "wikipedia_standings")
    soup = BeautifulSoup(html, "lxml")

    tables = _classification_tables(soup)
    classifications = {"gc": [], "points": [], "kom": [], "youth": []}
    for label, (table, headers) in zip(CLASSIFICATION_ORDER, tables):
        classifications[label] = _parse_classification(table, headers, VALUE_FIELD[label])

    if not classifications["gc"]:
        return None
    return {"classifications": classifications}


def _summary_table(soup):
    """The stage-by-stage leaders table (Stage | Winner | General
    classification | …). Requiring a 'general classification' column
    disambiguates it from the plain route table, which also has
    Stage/Winner columns but would hand back the stage type as the winner."""
    for table in soup.find_all("table"):
        headers = _header_cells(table)
        if (any(h == "stage" for h in headers)
                and any("winner" in h for h in headers)
                and any("general" in h for h in headers)):
            return table, headers
    return None, None


def fetch_stage_result(session, year, stage_number, cache_dir=None):
    """Returns {"top10": [<winner only>], "jersey_wearers_after": {...}} for
    the given stage, or None. Wikipedia's summary table lists only the stage
    winner (a team on a team time trial), not a full top 10."""
    html = fetch_html(session, _article_url(year), cache_dir, f"wikipedia_stage_{stage_number:02d}_result")
    soup = BeautifulSoup(html, "lxml")

    table, headers = _summary_table(soup)
    if table is None:
        return None

    winner_i = _col_index(headers, "winner")
    gc_i = _col_index(headers, "general")
    points_i = _col_index(headers, "points")
    kom_i = _col_index(headers, "mountains")
    youth_i = _col_index(headers, "young")

    for tr in table.find_all("tr")[1:]:
        cells = tr.find_all(["th", "td"])
        if not cells:
            continue
        stage_digits = "".join(ch for ch in _cell_text(cells, 0) if ch.isdigit())
        if stage_digits != str(stage_number):
            continue
        winner = _cell_text(cells, winner_i)
        if not winner:
            return None
        jerseys = {
            "gc": _cell_text(cells, gc_i),
            "points": _cell_text(cells, points_i),
            "kom": _cell_text(cells, kom_i),
            "youth": _cell_text(cells, youth_i),
        }
        return {
            "top10": [{"rank": 1, "rider": winner, "team": "", "time": "", "gap": "—"}],
            "jersey_wearers_after": {k: v for k, v in jerseys.items() if v},
        }
    return None
