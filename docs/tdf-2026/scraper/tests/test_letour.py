"""Parser tests for sources/letour.py against fixtures mirroring the real
letour.fr rankings page and its /subtab AJAX fragments (verified live,
2026-07-04 — see scraper/README.md for how the tab/hash/AJAX mechanism
was reverse-engineered).

Run from the scraper/ directory:
    python3 -m unittest discover -s tests -p 'test_*.py'
"""

import pathlib
import unittest
from unittest import mock

from sources import letour

FIXTURES = pathlib.Path(__file__).parent / "fixtures"


class TestExtractTabConfig(unittest.TestCase):
    def test_parses_types_and_ajax_hashes(self):
        html = (FIXTURES / "letour_stage1_rankings.html").read_text(encoding="utf-8")
        types, ajax = letour._extract_tab_config(html)
        self.assertEqual(types["general"], ["itg", "ipg", "img", "ijg", "etg"])
        # A team time trial's "stage" type only exposes team ("ete") — no
        # separate individual stage ranking distinct from the day's GC.
        self.assertEqual(types["stage"], ["ete"])
        self.assertIn("itg", ajax)
        self.assertTrue(ajax["itg"].startswith("/en/ajax/ranking/1/itg/"))

    def test_general_codes_found_even_when_stage_tab_is_default_active(self):
        # Regression test: stage 2 (the first road stage) defaulted to the
        # "Stage ranking" tab active, unlike stage 1's TTT which defaulted
        # to "General ranking". Only the active tab's sub-tabs render
        # individual data-tabs-ajax attributes; the general/GC codes
        # (itg/ipg/img/ijg) must still be found via that tab's
        # data-ajax-stack blob, which is present regardless of which tab
        # is active. Missing this caused jersey_wearers_after to come back
        # empty and standings to silently fall back to a stale stage.
        html = (FIXTURES / "letour_stage2_rankings.html").read_text(encoding="utf-8")
        types, ajax = letour._extract_tab_config(html)
        self.assertEqual(set(types["general"]), {"itg", "ipg", "img", "ijg", "etg"})
        for code in ("itg", "ipg", "img", "ijg"):
            self.assertIn(code, ajax, f"{code} missing — general codes not found when Stage tab is active")


class TestParseRankingFragment(unittest.TestCase):
    def test_time_based_fragment(self):
        html = (FIXTURES / "letour_ranking_fragment.html").read_text(encoding="utf-8")
        rows = letour._parse_ranking_fragment(html, "time")
        self.assertEqual(len(rows), 3)
        # Full name from the profile-link slug, not the abbreviated "J.
        # VINGEGAARD" — trimmed to press-common form via RIDER_NAME_OVERRIDES
        # (the raw slug gives "Jonas Vingegaard").
        self.assertEqual(rows[0]["rider"], "Jonas Vingegaard")
        self.assertEqual(rows[0]["time"], "21:47")
        self.assertEqual(rows[0]["gap"], "—")
        self.assertEqual(rows[1]["rider"], "Filippo Ganna")
        self.assertEqual(rows[1]["gap"], "+0:08")
        # Team names re-cased from ALL CAPS, short acronyms preserved.
        self.assertEqual(rows[2]["team"], "UAE Team Emirates XRG")

    def test_points_based_fragment(self):
        html = (FIXTURES / "letour_points_fragment.html").read_text(encoding="utf-8")
        rows = letour._parse_ranking_fragment(html, "points")
        # Trimmed via RIDER_NAME_OVERRIDES (raw slug gives "Egan Bernal Gomez").
        self.assertEqual(rows[0]["rider"], "Egan Bernal")
        self.assertEqual(rows[0]["points"], 0)
        self.assertNotIn("time", rows[0])

    def test_missing_table_returns_empty_list(self):
        self.assertEqual(letour._parse_ranking_fragment("<div>no table here</div>", "time"), [])


class TestFormatTeam(unittest.TestCase):
    def test_preserves_short_acronyms(self):
        self.assertEqual(letour._format_team("UAE TEAM EMIRATES XRG"), "UAE Team Emirates XRG")

    def test_titlecases_long_words(self):
        self.assertEqual(letour._format_team("NETCOMPANY INEOS CYCLING TEAM"), "Netcompany Ineos Cycling Team")

    def test_handles_hyphenated_names(self):
        self.assertEqual(letour._format_team("LIDL-TREK"), "Lidl-Trek")

    def test_denylist_excludes_common_short_words(self):
        # "RED" is 3 letters and all-caps but is not an acronym.
        self.assertEqual(letour._format_team("RED BULL - BORA - HANSGROHE"), "Red Bull - Bora - Hansgrohe")


class TestRiderNameOverrides(unittest.TestCase):
    def test_override_applied_wherever_a_rider_name_is_derived(self):
        # Vingegaard's registration slug carries a second surname press
        # coverage doesn't use ("jonas-vingegaard-hansen"); this must come
        # back trimmed everywhere a rider name is derived from that slug —
        # GC row, stage result, and jersey_wearers_after alike.
        self.assertIn("Jonas Vingegaard Hansen", letour.RIDER_NAME_OVERRIDES)
        self.assertEqual(letour.RIDER_NAME_OVERRIDES["Jonas Vingegaard Hansen"], "Jonas Vingegaard")

    def test_curated_overrides_cover_known_double_surname_riders(self):
        # Same class of fix as Vingegaard: the slug carries a second
        # official surname (Spanish maternal surname, or — for Foss — a
        # middle name) that press coverage drops. Note the positions
        # differ per rider (drop the LAST word for the Spanish-convention
        # names, but the MIDDLE word for "Tobias Svendsen Foss"), which is
        # exactly why this is a curated map rather than a positional rule.
        expected = {
            "Juan Ayuso Pesquera": "Juan Ayuso",
            "Egan Bernal Gomez": "Egan Bernal",
            "Isaac Del Toro Romero": "Isaac Del Toro",
            "Tobias Svendsen Foss": "Tobias Foss",
        }
        for full_name, trimmed in expected.items():
            self.assertEqual(letour.RIDER_NAME_OVERRIDES.get(full_name), trimmed)


class TestFetchClassifications(unittest.TestCase):
    def _fake_fetch(self, url_to_fixture):
        def fetch(session, url, cache_dir=None, cache_key=None):
            for fragment, fixture in url_to_fixture.items():
                if fragment in url:
                    return (FIXTURES / fixture).read_text(encoding="utf-8")
            raise AssertionError(f"unexpected URL in test: {url}")
        return fetch

    def test_returns_all_four_classifications(self):
        fetch = self._fake_fetch({
            "rankings/stage-1": "letour_stage1_rankings.html",
            "/itg/": "letour_ranking_fragment.html",
            "/ipg/": "letour_points_fragment.html",
            "/img/": "letour_points_fragment.html",
            "/ijg/": "letour_ranking_fragment.html",
        })
        with mock.patch("sources.letour.fetch_html", side_effect=fetch):
            result = letour.fetch_classifications(session=None, stage_number=1)
        self.assertEqual(result["gc"][0]["rider"], "Jonas Vingegaard")
        self.assertEqual(result["points"][0]["rider"], "Egan Bernal")
        self.assertEqual(result["youth"][0]["rider"], "Jonas Vingegaard")

    def test_future_stage_with_no_tables_returns_none(self):
        with mock.patch("sources.letour.fetch_html", return_value="<html><body>no ranking data yet</body></html>"):
            self.assertIsNone(letour.fetch_classifications(session=None, stage_number=5))


class TestFetchStageResult(unittest.TestCase):
    def test_ttt_falls_back_to_general_when_no_stage_only_ranking(self):
        # Fixture's "stage" type list is ["ete"] only (team) — no "ite" —
        # so fetch_stage_result must fall back to itg (general/GC).
        fetch = lambda session, url, cache_dir=None, cache_key=None: (  # noqa: E731
            (FIXTURES / "letour_stage1_rankings.html").read_text(encoding="utf-8")
            if "rankings/stage-1" in url
            else (FIXTURES / "letour_ranking_fragment.html").read_text(encoding="utf-8")
        )
        with mock.patch("sources.letour.fetch_html", side_effect=fetch):
            result = letour.fetch_stage_result(session=None, stage_number=1)
        self.assertEqual(result["top10"][0]["rider"], "Jonas Vingegaard")
        self.assertIn("gc", result["jersey_wearers_after"])

    def test_road_stage_populates_jersey_wearers_when_stage_tab_is_active(self):
        # Regression test for the stage-2 bug: jersey_wearers_after must
        # populate even though the page's default-active tab is "Stage",
        # not "General" (see test_general_codes_found_even_when_stage_tab_is_default_active).
        fetch = lambda session, url, cache_dir=None, cache_key=None: (  # noqa: E731
            (FIXTURES / "letour_stage2_rankings.html").read_text(encoding="utf-8")
            if "rankings/stage-2" in url
            else (FIXTURES / "letour_ranking_fragment.html").read_text(encoding="utf-8")
        )
        with mock.patch("sources.letour.fetch_html", side_effect=fetch):
            result = letour.fetch_stage_result(session=None, stage_number=2)
        self.assertTrue(result["jersey_wearers_after"], "jersey_wearers_after came back empty")
        self.assertIn("gc", result["jersey_wearers_after"])
        self.assertIn("points", result["jersey_wearers_after"])
        self.assertIn("kom", result["jersey_wearers_after"])
        self.assertIn("youth", result["jersey_wearers_after"])


if __name__ == "__main__":
    unittest.main()
