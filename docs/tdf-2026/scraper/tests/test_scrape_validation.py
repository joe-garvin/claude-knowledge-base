"""Tests for scrape.py's contract validation and idempotent history upsert
— the part of the scraper that matters most, since sources will change out
from under it but this logic is what keeps a bad scrape from ever
clobbering a good snapshot.

Run from the scraper/ directory:
    python3 -m unittest discover -s tests -p 'test_*.py'
"""

import unittest

import scrape


class TestValidateGcRows(unittest.TestCase):
    def test_valid_sequential_ranks(self):
        rows = [
            {"rank": 1, "rider": "A", "team": "T1"},
            {"rank": 2, "rider": "B", "team": "T2"},
        ]
        self.assertTrue(scrape.validate_gc_rows(rows))

    def test_empty_is_invalid(self):
        self.assertFalse(scrape.validate_gc_rows([]))
        self.assertFalse(scrape.validate_gc_rows(None))

    def test_non_sequential_ranks_invalid(self):
        rows = [{"rank": 1, "rider": "A", "team": "T1"}, {"rank": 3, "rider": "B", "team": "T2"}]
        self.assertFalse(scrape.validate_gc_rows(rows))

    def test_missing_field_invalid(self):
        rows = [{"rank": 1, "rider": "A", "team": ""}]
        self.assertFalse(scrape.validate_gc_rows(rows))


class TestValidateTop10(unittest.TestCase):
    def test_single_winner_is_valid(self):
        self.assertTrue(scrape.validate_top10([{"rank": 1, "rider": "A"}]))

    def test_missing_rider_invalid(self):
        self.assertFalse(scrape.validate_top10([{"rank": 1, "rider": ""}]))


class TestUpsertGcHistory(unittest.TestCase):
    def test_appends_new_stage(self):
        history = [{"stage": 1, "rider": "A"}]
        result = scrape.upsert_gc_history(history, 2, "A")
        self.assertEqual(result, [{"stage": 1, "rider": "A"}, {"stage": 2, "rider": "A"}])

    def test_replaces_existing_stage_idempotently(self):
        history = [{"stage": 1, "rider": "A"}, {"stage": 2, "rider": "A"}]
        result = scrape.upsert_gc_history(history, 2, "B")
        self.assertEqual(result, [{"stage": 1, "rider": "A"}, {"stage": 2, "rider": "B"}])

    def test_rerun_same_day_stays_single_entry(self):
        history = []
        history = scrape.upsert_gc_history(history, 1, "A")
        history = scrape.upsert_gc_history(history, 1, "A")
        history = scrape.upsert_gc_history(history, 1, "A")
        self.assertEqual(history, [{"stage": 1, "rider": "A"}])


class TestDueStageNumbers(unittest.TestCase):
    def test_only_stages_on_or_before_today(self):
        race = {"stages": [
            {"number": 1, "date": "2026-07-04"},
            {"number": 2, "date": "2026-07-05"},
            {"number": 3, "date": "2026-07-06"},
        ]}
        self.assertEqual(scrape.due_stage_numbers(race, "2026-07-05"), [1, 2])
        self.assertEqual(scrape.due_stage_numbers(race, "2026-07-01"), [])
        self.assertEqual(scrape.due_stage_numbers(race, "2026-07-06"), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
