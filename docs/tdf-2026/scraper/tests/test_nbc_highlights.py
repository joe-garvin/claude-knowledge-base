"""Parser tests for sources/nbc_highlights.py against a fixture
approximating the NBC Tour de France hub page's embedded video metadata
(see the fixture file and the module docstring for provenance).

Run from the scraper/ directory:
    python3 -m unittest discover -s tests -p 'test_*.py'
"""

import pathlib
import unittest
from unittest import mock

from sources import nbc_highlights

FIXTURES = pathlib.Path(__file__).parent / "fixtures"


class TestFetchHighlightLinks(unittest.TestCase):
    def setUp(self):
        self.html = (FIXTURES / "nbc_tdf_hub.html").read_text(encoding="utf-8")

    def _fetch_returns_fixture(self, *args, **kwargs):
        return self.html

    def test_finds_highlights_reel_per_stage(self):
        with mock.patch("sources.nbc_highlights.fetch_html", side_effect=self._fetch_returns_fixture):
            found = nbc_highlights.fetch_highlight_links(session=None)
        self.assertEqual(set(found.keys()), {4, 5})

    def test_extracts_url_and_title(self):
        with mock.patch("sources.nbc_highlights.fetch_html", side_effect=self._fetch_returns_fixture):
            found = nbc_highlights.fetch_highlight_links(session=None)
        self.assertEqual(
            found[5]["url"],
            "https://www.nbcsports.com/watch/tour-de-france-2026-highlights-olav-kooij-wins-stage-5-sprint",
        )
        self.assertEqual(found[5]["title"], "Highlights: 2026 Tour de France, Stage 5")

    def test_ignores_non_highlights_category_for_same_stage(self):
        # The stage-5 "finish only" decoy clip shares stage 5's guid prefix
        # but a different category; the real highlights reel must win, not
        # the finish clip's videoPageUrl.
        with mock.patch("sources.nbc_highlights.fetch_html", side_effect=self._fetch_returns_fixture):
            found = nbc_highlights.fetch_highlight_links(session=None)
        self.assertNotIn("finish", found[5]["url"])

    def test_fetch_failure_returns_empty_dict_not_raise(self):
        with mock.patch("sources.nbc_highlights.fetch_html", side_effect=RuntimeError("boom")):
            found = nbc_highlights.fetch_highlight_links(session=None)
        self.assertEqual(found, {})


if __name__ == "__main__":
    unittest.main()
