"""NBC Sports stage-highlights video discovery.

The published highlights video's URL embeds a freeform editorial phrase
(e.g. "mads-pedersens-exciting-stage-4-win") that can't be constructed
from the stage number alone, so this can't work like the numbered-URL
scrapers in pcs.py / letour.py. Instead it scrapes NBC's Tour de France
hub page for the structured video metadata NBC embeds there for its
featured "The Feed" highlights reel: a stable guid
("nbc_cyc_tdfst{N}_{date}") that DOES encode the stage number, sitting
in the same embedded block as the real videoPageUrl.

Confirmed against the live hub page while building this (2026-07-07,
stage 4): the guid, its "Tour de France highlights (The Feed)" category,
and videoPageUrl all appear in one flat metadata block per video, mixed
in with unrelated clips (stage-finish-only clips, "beyond the podium"
analysis, post-race interviews) that share the page. The category string
is what distinguishes the real highlights reel from those.

Best-effort only, in the same spirit as letour.py's fetch_stage_schedule:
never raises past its caller, and a parse failure just means no new
highlight link is discovered this run. data/highlights.json is otherwise
hand-curated — the caller must only ever use this to fill in a *missing*
stage, never to overwrite an existing entry.
"""

import re

from net import fetch_html

HUB_URL = "https://www.nbcsports.com/cycling/tour-de-france"

# The one category string NBC applies to its official full-stage
# highlights reel on this page, distinct from finish-only clips and
# analysis/interview clips that share the same embedded metadata shape.
HIGHLIGHTS_CATEGORY = "Tour de France highlights (The Feed)"

GUID_RE = re.compile(r'"guid":"nbc_cyc_tdfst(\d+)_\d+"')

# The guid, category, and videoPageUrl fields aren't in a fixed order or
# distance in the embedded metadata (observed field order varies), so a
# generous window in both directions around each guid match is searched
# rather than a strict forward-only regex.
WINDOW_BEFORE = 1200
WINDOW_AFTER = 900


def fetch_highlight_links(session, cache_dir=None):
    """Returns {stage_number: {"url": ..., "title": ...}} for every
    official highlights reel currently linked from the hub page (in
    practice usually just the latest stage — older ones roll off).
    Returns {} on any fetch or parse problem; never raises."""
    try:
        html = fetch_html(session, HUB_URL, cache_dir, "nbc_tdf_hub")
    except RuntimeError:
        return {}

    found = {}
    for m in GUID_RE.finditer(html):
        stage_n = int(m.group(1))
        window = html[max(0, m.start() - WINDOW_BEFORE): m.start() + WINDOW_AFTER]
        if HIGHLIGHTS_CATEGORY not in window:
            continue
        url_m = re.search(r'"videoPageUrl":\s*"([^"]+)"', window)
        if not url_m:
            continue
        title_m = re.search(r'"title":\s*"([^"]+)"', window)
        found[stage_n] = {
            "url": url_m.group(1),
            "title": title_m.group(1) if title_m else None,
        }
    return found
