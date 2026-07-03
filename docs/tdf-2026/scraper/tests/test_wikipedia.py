"""Parser tests against a fixture approximating the live "2025 Tour de
France" Wikipedia article structure (confirmed via WebFetch while building
this scraper — see scraper/README.md). The 2026 article should follow the
same shape once the race is underway.

Run from the scraper/ directory:
    python3 -m unittest discover -s tests -p 'test_*.py'
"""

import pathlib
import unittest
from unittest import mock

from bs4 import BeautifulSoup

from sources import wikipedia

FIXTURES = pathlib.Path(__file__).parent / "fixtures"


class TestWikipediaParsing(unittest.TestCase):
    def setUp(self):
        self.html = (FIXTURES / "wikipedia_article.html").read_text(encoding="utf-8")

    def _fetch_returns_fixture(self, *args, **kwargs):
        return self.html

    def test_fetch_standings_parses_gc(self):
        with mock.patch("sources.wikipedia.fetch_html", side_effect=self._fetch_returns_fixture):
            result = wikipedia.fetch_standings(session=None, year=2026)
        self.assertIsNotNone(result)
        gc = result["classifications"]["gc"]
        self.assertEqual(len(gc), 2)
        self.assertEqual(gc[0]["rider"], "Tadej Pogačar")
        self.assertEqual(gc[0]["team"], "UAE Team Emirates-XRG")
        self.assertEqual(gc[1]["gap"], "+ 4' 24\"")
        # Wikipedia's race-summary article doesn't carry secondary
        # classifications, so these must come back as legitimate empty lists.
        self.assertEqual(result["classifications"]["points"], [])
        self.assertEqual(result["classifications"]["kom"], [])

    def test_fetch_stage_result_returns_winner_only(self):
        with mock.patch("sources.wikipedia.fetch_html", side_effect=self._fetch_returns_fixture):
            result = wikipedia.fetch_stage_result(session=None, year=2026, stage_number=2)
        self.assertIsNotNone(result)
        self.assertEqual(len(result["top10"]), 1)
        self.assertEqual(result["top10"][0]["rank"], 1)
        self.assertEqual(result["top10"][0]["rider"], "Jasper Philipsen")

    def test_fetch_stage_result_missing_stage_returns_none(self):
        with mock.patch("sources.wikipedia.fetch_html", side_effect=self._fetch_returns_fixture):
            result = wikipedia.fetch_stage_result(session=None, year=2026, stage_number=99)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
