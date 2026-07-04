"""Parser tests against a fixture mirroring the live "2026 Tour de France"
article structure (verified 2026-07-04 — see scraper/tests/fixtures/).

These lock in the two bugs found on race day: the rank row-header <th> that
shifted every column by one, and the route table being mistaken for the
leaders-summary table (which returned the stage type as the "winner").

Run from the scraper/ directory:
    python3 -m unittest discover -s tests -p 'test_*.py'
"""

import pathlib
import unittest
from unittest import mock

from sources import wikipedia

FIXTURES = pathlib.Path(__file__).parent / "fixtures"


class TestWikipediaParsing(unittest.TestCase):
    def setUp(self):
        self.html = (FIXTURES / "wikipedia_2026.html").read_text(encoding="utf-8")

    def _patched(self):
        return mock.patch("sources.wikipedia.fetch_html", return_value=self.html)

    def test_gc_parsed_with_correct_columns(self):
        with self._patched():
            result = wikipedia.fetch_standings(session=None, year=2026)
        gc = result["classifications"]["gc"]
        self.assertEqual(len(gc), 6)
        # The row-header <th> rank must not shift rider into the team slot.
        self.assertEqual(gc[0]["rider"], "Jonas Vingegaard")
        self.assertEqual(gc[0]["team"], "Visma–Lease a Bike")
        self.assertEqual(gc[0]["gap"], "—")
        self.assertEqual(gc[1]["rider"], "Filippo Ganna")
        self.assertEqual(gc[1]["gap"], '+ 8"')

    def test_all_four_classifications_assigned_in_order(self):
        with self._patched():
            c = wikipedia.fetch_standings(session=None, year=2026)["classifications"]
        self.assertEqual(c["points"][0]["rider"], "Egan Bernal")
        self.assertEqual(c["kom"][0]["rider"], "Tadej Pogačar")
        self.assertEqual(c["youth"][0]["rider"], "Juan Ayuso")
        # secondary classifications carry teams and integer points
        self.assertEqual(c["points"][0]["team"], "Netcompany INEOS")
        self.assertEqual(c["kom"][0]["points"], 0)

    def test_stage_result_uses_leaders_table_not_route_table(self):
        with self._patched():
            result = wikipedia.fetch_stage_result(session=None, year=2026, stage_number=1)
        # Must be the winner from the leaders table, never the route table's
        # "Team time trial" stage-type cell.
        self.assertEqual(result["top10"][0]["rider"], "Visma–Lease a Bike")
        self.assertEqual(result["jersey_wearers_after"]["gc"], "Jonas Vingegaard")
        self.assertEqual(result["jersey_wearers_after"]["youth"], "Juan Ayuso")

    def test_missing_stage_returns_none(self):
        with self._patched():
            self.assertIsNone(wikipedia.fetch_stage_result(session=None, year=2026, stage_number=9))


if __name__ == "__main__":
    unittest.main()
