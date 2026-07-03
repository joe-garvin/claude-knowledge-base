"""Shared HTTP fetch helper: descriptive User-Agent, retries with backoff,
a polite delay between requests, and optional raw-HTML caching per run so
a scrape can be debugged after the fact without re-hitting the source."""

import time

import requests

USER_AGENT = (
    "tdf-2026-tracker-bot/1.0 "
    "(+https://github.com/; daily data refresh for a personal Tour de France "
    "tracker; contact via repo issues)"
)
REQUEST_DELAY_SECONDS = 1.5
MAX_ATTEMPTS = 3
BACKOFF_BASE_SECONDS = 2
TIMEOUT_SECONDS = 15


def fetch_html(session, url, cache_dir=None, cache_key=None):
    """GET a URL with retries/backoff. Raises RuntimeError after exhausting
    attempts. Caches the raw response body if cache_dir/cache_key given."""
    last_error = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            resp = session.get(url, headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT_SECONDS)
            resp.raise_for_status()
            html = resp.text
            if cache_dir and cache_key:
                cache_dir.mkdir(parents=True, exist_ok=True)
                (cache_dir / f"{cache_key}.html").write_text(html, encoding="utf-8")
            time.sleep(REQUEST_DELAY_SECONDS)
            return html
        except requests.RequestException as e:
            last_error = e
            if attempt < MAX_ATTEMPTS:
                time.sleep(BACKOFF_BASE_SECONDS * attempt)
    raise RuntimeError(f"failed to fetch {url} after {MAX_ATTEMPTS} attempts: {last_error}")
