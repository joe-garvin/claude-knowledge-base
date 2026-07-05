"""letour.fr scraper — the official rankings site, and our primary source
for both standings and stage results, plus a best-effort watch-time refresh.

Empirically verified 2026-07-04, on race day: ProCyclingStats returns
HTTP 403 to every automated fetch (see sources/pcs.py), and Wikipedia's
article only carries thin summary tables that are easy to mis-parse (see
sources/wikipedia.py's history). letour.fr's `/en/rankings/stage-N` pages
serve full, structured, official ranking tables via a plain GET — no
cookies, no session, no browser-only bot check observed — once you know
that page's per-classification AJAX hash tokens. Those tokens are baked
into the page's HTML and are deterministic (stable across repeat fetches;
not tied to a session), so no login dance is needed.

How the site is wired (reverse-engineered from the rendered HTML):

  1. GET /en/rankings/stage-{n} — the page embeds, per ranking-type tab, a
     `data-types` JSON telling you which classification codes exist for
     "general" (cumulative through this stage) vs "stage" (this stage
     only), e.g. `{"general": ["itg","ipg","img","ijg","etg"],
     "stage": ["ite"]}`. Codes: it=individual, ip=points, im=mountains
     (KOM), ij=young rider, et=team; suffix g=general, e=stage-only.
     Each code also has a `data-tabs-ajax` URL carrying its hash token.

  2. GET each needed `/en/ajax/ranking/{n}/{code}/{hash}/subtab` — returns
     an HTML fragment containing one <table> (Rank/Rider/Team/Time-or-
     Points/Gap/Bonus/Penalty columns) for that classification.

A team time trial's "stage" type only exposes "ete" (team) — there is no
separate individual stage ranking distinct from the cumulative GC that
day — so fetch_stage_result falls back to the general/GC table (itg) when
a stage-only individual ranking ("ite") isn't offered.

A future stage's page returns 200 but has no ranking tables at all (the
race hasn't reached it yet) — that reads as "no data", not an error.
"""

import json
import re

from bs4 import BeautifulSoup

from net import fetch_html
from sources.table_parse import cell_text, column_index, find_table_by_header

BASE_URL = "https://www.letour.fr"

CLASSIFICATION_CODES = {"gc": "it", "points": "ip", "kom": "im", "youth": "ij"}
VALUE_KIND = {"gc": "time", "points": "points", "kom": "points", "youth": "time"}

# The rider profile slug carries the full name on official registration
# (which can include a second surname press coverage doesn't use day to
# day, e.g. a Danish patronymic or a Spanish maternal surname). Curated on
# request rather than guessed algorithmically — the "keep everything before
# the last name" heuristic doesn't hold across naming conventions (compare
# "Isaac Del Toro" dropping the *last* word vs "Tobias Foss" dropping a
# *middle* one). Add an entry here if another rider's display name needs
# trimming; this is the single place the fix applies everywhere a rider
# name is derived (standings, stage results, jersey wearers, history).
RIDER_NAME_OVERRIDES = {
    "Jonas Vingegaard Hansen": "Jonas Vingegaard",
    "Juan Ayuso Pesquera": "Juan Ayuso",
    "Egan Bernal Gomez": "Egan Bernal",
    "Isaac Del Toro Romero": "Isaac Del Toro",
    "Tobias Svendsen Foss": "Tobias Foss",
}


def _rankings_url(stage_number):
    return f"{BASE_URL}/en/rankings/stage-{stage_number}"


def _extract_tab_config(html):
    """Returns (types: {"general": [codes], "stage": [codes]}, ajax: {code: url})."""
    types = {}
    types_match = re.search(r'data-types="([^"]*)"', html)
    if types_match:
        try:
            types = json.loads(types_match.group(1).replace("&quot;", '"'))
        except json.JSONDecodeError:
            types = {}
    ajax = {}
    for m in re.finditer(r'data-tabs-ajax="(/en/ajax/ranking/\d+/([a-z]+)/[a-f0-9]+/subtab)"', html):
        url, code = m.group(1), m.group(2)
        ajax[code] = url
    return types, ajax


def _rider_name(cells, rider_index):
    """The visible cell text is an abbreviated "J. VINGEGAARD". The
    profile link's URL slug carries the full name and is always present,
    even on rows where the abbreviated text or photo alt text is not."""
    if rider_index is None or rider_index >= len(cells):
        return None
    link = cells[rider_index].find("a", class_="rankingTables__row__profile--name")
    if link is None:
        return cell_text(cells, rider_index)
    slug = link.get("href", "").rstrip("/").split("/")[-1]
    if not slug:
        return cell_text(cells, rider_index)
    name = " ".join(w.capitalize() for w in slug.split("-"))
    return RIDER_NAME_OVERRIDES.get(name, name)


def _format_time(raw):
    m = re.match(r"(\d+)h\s*(\d+)'\s*(\d+)", raw or "")
    if not m:
        return raw
    h, mi, s = (int(x) for x in m.groups())
    return f"{h}:{mi:02d}:{s:02d}" if h else f"{mi}:{s:02d}"


def _format_gap(raw):
    raw = (raw or "").strip()
    if raw in ("-", "", "–"):
        return "—"
    m = re.match(r"\+?\s*(\d+)h\s*(\d+)'\s*(\d+)", raw)
    if not m:
        return raw
    h, mi, s = (int(x) for x in m.groups())
    return f"+{h}:{mi:02d}:{s:02d}" if h else f"+{mi}:{s:02d}"


# Short words that happen to be all-caps in the source markup but are NOT
# an acronym like "UAE" or "XRG" — kept lowercase-cased rather than
# preserved as-is.
_NOT_ACRONYM = {"RED", "OLD", "NEW", "THE", "AND", "FOR", "ONE", "ALL", "ANY"}


def _capitalize_token(tok):
    if not tok or not any(ch.isalpha() for ch in tok):
        return tok
    if "-" in tok and len(tok) > 1:
        return "-".join(_capitalize_token(p) for p in tok.split("-"))
    alpha = re.sub(r"[^A-Za-z]", "", tok)
    if alpha.isupper() and len(alpha) <= 3 and alpha not in _NOT_ACRONYM:
        return tok  # preserve short acronyms: UAE, XRG, CMA, CGM…
    return tok.capitalize()


def _format_team(raw):
    """Team names come back ALL CAPS ("TEAM VISMA | LEASE A BIKE"); title-case
    them for the site's editorial tone while preserving short acronyms."""
    return " ".join(_capitalize_token(w) for w in (raw or "").split(" ") if w)


def _parse_ranking_fragment(html, value_kind):
    """Parses one /subtab AJAX fragment into a list of contract-shaped rows."""
    soup = BeautifulSoup(html, "lxml")
    table, headers = find_table_by_header(soup, "rider")
    if table is None:
        return []

    rider_i = column_index(headers, "rider")
    team_i = column_index(headers, "team")
    value_i = column_index(headers, "times" if value_kind == "time" else "points")
    gap_i = column_index(headers, "gap")

    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = tr.find_all("td")
        if len(cells) < 4:
            continue
        rider = _rider_name(cells, rider_i)
        if not rider:
            continue
        entry = {"rank": len(rows) + 1, "rider": rider, "team": _format_team(cell_text(cells, team_i))}
        if value_kind == "points":
            raw = cell_text(cells, value_i) or ""
            digits = "".join(ch for ch in raw if ch.isdigit())
            entry["points"] = int(digits) if digits else 0
        else:
            entry["time"] = _format_time(cell_text(cells, value_i) or "")
            entry["gap"] = _format_gap(cell_text(cells, gap_i) or "")
        rows.append(entry)
    return rows


def fetch_classifications(session, stage_number, cache_dir=None):
    """Returns {"gc": [...], "points": [...], "kom": [...], "youth": [...]}
    (cumulative through `stage_number`), or None if the stage page itself
    couldn't be fetched or carries no ranking tables yet (future stage)."""
    html = fetch_html(session, _rankings_url(stage_number), cache_dir, f"letour_stage_{stage_number:02d}_rankings")
    types, ajax = _extract_tab_config(html)
    if not types.get("general"):
        return None

    classifications = {}
    for key, prefix in CLASSIFICATION_CODES.items():
        code = f"{prefix}g"
        url = ajax.get(code)
        if not url:
            classifications[key] = []
            continue
        fragment = fetch_html(session, f"{BASE_URL}{url}", cache_dir, f"letour_stage_{stage_number:02d}_{code}")
        classifications[key] = _parse_ranking_fragment(fragment, VALUE_KIND[key])
    return classifications


def fetch_stage_result(session, stage_number, cache_dir=None):
    """Returns {"top10": [...], "jersey_wearers_after": {...}} for this
    stage, or None if the page has no ranking data yet. Uses the
    stage-only individual ranking ("ite") when the site offers one;
    team time trials only expose a team stage-ranking, so this falls back
    to the cumulative GC (itg) — the individual times ARE the GC that day."""
    html = fetch_html(session, _rankings_url(stage_number), cache_dir, f"letour_stage_{stage_number:02d}_rankings")
    types, ajax = _extract_tab_config(html)
    if not types.get("general") and not types.get("stage"):
        return None

    stage_codes = types.get("stage", [])
    code = "ite" if "ite" in stage_codes else "itg"
    url = ajax.get(code)
    if not url:
        return None
    fragment = fetch_html(session, f"{BASE_URL}{url}", cache_dir, f"letour_stage_{stage_number:02d}_{code}_result")
    rows = _parse_ranking_fragment(fragment, "time")
    if not rows:
        return None

    jersey_wearers_after = {}
    for key, prefix in CLASSIFICATION_CODES.items():
        leader_code = f"{prefix}g"
        leader_url = ajax.get(leader_code)
        if not leader_url:
            continue
        leader_fragment = fetch_html(
            session, f"{BASE_URL}{leader_url}", cache_dir,
            f"letour_stage_{stage_number:02d}_{leader_code}_leader",
        )
        leader_rows = _parse_ranking_fragment(leader_fragment, VALUE_KIND[key])
        if leader_rows:
            jersey_wearers_after[key] = leader_rows[0]["rider"]

    return {"top10": rows[:10], "jersey_wearers_after": jersey_wearers_after}


def fetch_stage_schedule(session, stage_number, cache_dir=None):
    """Best-effort start/finish time refresh — see data/watch.json, which
    is already seeded with reasonable estimates (Section 8 of the build
    spec), so a failure here just means the seed estimate stands. Not
    verified against real markup; deliberately conservative."""
    url = f"{BASE_URL}/en/stage-{stage_number}"
    try:
        html = fetch_html(session, url, cache_dir, f"letour_stage_{stage_number:02d}_schedule")
    except RuntimeError:
        return None

    soup = BeautifulSoup(html, "lxml")
    text = soup.get_text(" ", strip=True)
    if not re.search(r"\d{1,2}:\d{2}", text):
        return None

    # Deliberately not parsed further: without a verified live page to
    # confirm the real markup/wording, guessing a precise start/finish
    # time here risks silently replacing a good seed estimate with a
    # wrong one. Returning None keeps the seed value in place.
    return None
