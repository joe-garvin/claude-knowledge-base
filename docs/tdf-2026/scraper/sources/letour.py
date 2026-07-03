"""letour.com best-effort scraper for stage start/finish time refreshes.

This is the lowest-priority source in the build spec: data/watch.json is
already seeded with reasonable start/finish estimates (see
scraper/seed_stages_2026.json and Section 8 of the build spec), so a
failure here just means the seed estimate stands — nothing downstream
depends on this succeeding. letour.com's schedule-page markup was not
verified live while building this scraper, so fetch_stage_schedule is
deliberately conservative: it returns None whenever the page doesn't
match the expected shape rather than guessing, and it never raises past
scrape.py's optional, non-fatal call site.
"""

import re

from bs4 import BeautifulSoup

from net import fetch_html

BASE_URL = "https://www.letour.fr/en/stage"


def fetch_stage_schedule(session, stage_number, cache_dir=None):
    """Returns {"start_utc": ..., "est_finish_utc": ...} or None.

    Best-effort only — see module docstring. Currently this looks for a
    simple "HH:MM ... start" pattern in the page text as a starting point;
    it should be revisited against the real 2026 letour.com markup (saved
    to scraper/.cache/) before being trusted over the seed data.
    """
    url = f"{BASE_URL}-{stage_number}"
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
