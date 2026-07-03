"""Parser tests against saved fixtures (scraper/tests/fixtures/).

The fixtures are representative markup, not captures of a live page — PCS
returned HTTP 403 to automated fetches while this scraper was being built,
so the real markup couldn't be verified (see scraper/README.md). These
tests lock in the parsing *logic* against the documented shape; if PCS's
real markup differs, update the fixture to match a real saved page and
these tests will catch any regression in the parser going forward.

Run from the scraper/ directory:
    python3 -m unittest discover -s tests -p 'test_*.py'
"""

import pathlib
import unittest

from bs4 import BeautifulSoup

from sources import pcs
from sources.table_parse import find_table_by_header

FIXTURES = pathlib.Path(__file__).parent / "fixtures"


class TestPcsStageResult(unittest.TestCase):
    def setUp(self):
        html = (FIXTURES / "pcs_stage_result.html").read_text(encoding="utf-8")
        self.soup = BeautifulSoup(html, "lxml")

    def test_finds_results_table_by_header(self):
        table, headers = find_table_by_header(self.soup, "rider")
        self.assertIsNotNone(table)
        self.assertIn("rider", headers)

    def test_parses_rows_in_rank_order(self):
        table, headers = find_table_by_header(self.soup, "rider")
        rows = pcs._parse_results_rows(table, headers)
        self.assertEqual(len(rows), 3)
        self.assertEqual([r["rank"] for r in rows], [1, 2, 3])

    def test_extracts_rider_team_time_gap(self):
        table, headers = find_table_by_header(self.soup, "rider")
        rows = pcs._parse_results_rows(table, headers)
        winner = rows[0]
        self.assertEqual(winner["rider"], "POGAČAR Tadej")
        self.assertEqual(winner["team"], "UAE Team Emirates-XRG")
        self.assertEqual(winner["time"], "4:32:18")
        self.assertEqual(winner["gap"], "—")

        second = rows[1]
        self.assertEqual(second["rider"], "VINGEGAARD Jonas")
        self.assertEqual(second["gap"], "+ 0:04")


class TestPcsGc(unittest.TestCase):
    def setUp(self):
        html = (FIXTURES / "pcs_gc.html").read_text(encoding="utf-8")
        self.soup = BeautifulSoup(html, "lxml")

    def test_parses_gc_rows(self):
        table, headers = find_table_by_header(self.soup, "rider")
        rows = pcs._parse_results_rows(table, headers)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["rider"], "POGAČAR Tadej")
        self.assertEqual(rows[1]["gap"], "+ 1:22")


if __name__ == "__main__":
    unittest.main()
