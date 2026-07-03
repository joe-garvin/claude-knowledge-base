#!/usr/bin/env python3
"""One-time build: turn scraper/seed_stages_2026.json into data/race.json
and data/watch.json.

The seed file holds the 2026 route facts gathered from letour.com,
ProCyclingStats, and Wikipedia (see Section 8 of the build spec). This
script shapes that into the data contract and derives:

  - race.json's profile.points: a coarse elevation profile per stage,
    built from start/finish elevation and each climb's length + average
    gradient. It is not survey-accurate, but it is a truthful sketch of
    where the road goes up — every stage is marked profile_quality:
    "coarse" so a future pass with real GPX data can replace it.
  - watch.json's UTC timestamps: seed start/finish times are published
    in CEST (UTC+2 during July); converted here so the front end never
    has to reason about the source timezone.

Run once (and again if the seed file is corrected):

    python3 scraper/build_race_json.py
"""

import json
import pathlib
from datetime import datetime, timedelta

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SEED_PATH = pathlib.Path(__file__).resolve().parent / "seed_stages_2026.json"
DATA_DIR = REPO_ROOT / "data"

CLASSIFICATIONS = [
    {"id": "gc", "name": "General classification", "jersey": "yellow"},
    {"id": "points", "name": "Points classification", "jersey": "green"},
    {"id": "kom", "name": "Mountains classification", "jersey": "polka"},
    {"id": "youth", "name": "Young rider classification", "jersey": "white"},
]

BASELINE_ELEVATION_M = 200.0
DEFAULT_CLIMB_LENGTH_KM = 4.0
DEFAULT_CLIMB_GRADIENT_PCT = 5.0
DESCENT_RETRACE_FRACTION = 0.55
MIN_VALLEY_ELEVATION_M = 180.0
FINISH_CLIMB_THRESHOLD_KM = 2.0


def cest_to_utc_iso(date_str, time_str):
    """Convert a CEST (UTC+2) wall-clock time to a UTC ISO 8601 string."""
    dt = datetime.strptime(f"{date_str}T{time_str}", "%Y-%m-%dT%H:%M")
    dt_utc = dt - timedelta(hours=2)
    return dt_utc.strftime("%Y-%m-%dT%H:%M:00Z")


def build_profile_points(stage):
    """Sketch a coarse elevation profile: start, each climb's base and
    summit, and the finish, with a partial descent between climbs so the
    chart reads as a real profile rather than a staircase."""
    distance = stage["distance_km"]
    climbs = stage.get("climbs") or []
    points = [{"km": 0.0, "elevation_m": round(BASELINE_ELEVATION_M)}]
    elevation = BASELINE_ELEVATION_M
    prev_km = 0.0

    for i, climb in enumerate(climbs):
        km_mark = float(climb["km_mark"])
        length = climb.get("length_km") or DEFAULT_CLIMB_LENGTH_KM
        gradient = climb.get("avg_gradient") or DEFAULT_CLIMB_GRADIENT_PCT

        climb_start_km = max(prev_km, round(km_mark - length, 1))
        if climb_start_km > prev_km:
            points.append({"km": climb_start_km, "elevation_m": round(elevation)})

        rise_m = length * 1000 * (gradient / 100.0)
        elevation += rise_m
        points.append({"km": round(km_mark, 1), "elevation_m": round(elevation)})

        is_finish_climb = (i == len(climbs) - 1) and (distance - km_mark < FINISH_CLIMB_THRESHOLD_KM)
        prev_km = km_mark
        if not is_finish_climb:
            elevation = max(MIN_VALLEY_ELEVATION_M, elevation - rise_m * DESCENT_RETRACE_FRACTION)

    if prev_km < distance:
        points.append({"km": distance, "elevation_m": round(elevation)})

    return points


def build_climbs(stage):
    return [
        {
            "name": c["name"],
            "category": c["category"],
            "km_mark": c["km_mark"],
            "length_km": c.get("length_km"),
            "avg_gradient": c.get("avg_gradient"),
        }
        for c in (stage.get("climbs") or [])
    ]


def build_race_json(seed_stages):
    stages = []
    for s in seed_stages:
        stages.append({
            "number": s["number"],
            "date": s["date"],
            "start": s["start"],
            "finish": s["finish"],
            "distance_km": s["distance_km"],
            "type": s["type"],
            "elevation_gain_m": s["elevation_gain_m"],
            "summit_finish": s["summit_finish"],
            "profile_quality": s.get("profile_quality", "coarse"),
            "preview": s["preview"],
            "profile": {
                "points": build_profile_points(s),
                "climbs": build_climbs(s),
            },
        })

    total_distance = round(sum(s["distance_km"] for s in stages), 1)
    total_elevation = sum(s["elevation_gain_m"] for s in stages)

    return {
        "edition": "113th",
        "year": 2026,
        "start_date": "2026-07-04",
        "end_date": "2026-07-26",
        "grand_depart": "Barcelona, Spain",
        "finish": "Paris (Champs-Élysées, via Montmartre)",
        "totals": {
            "distance_km": total_distance,
            "elevation_gain_m": total_elevation,
            "stages": len(stages),
        },
        "rest_days": ["2026-07-13", "2026-07-20"],
        "classifications": CLASSIFICATIONS,
        "stages": stages,
    }


def build_watch_json(seed_stages):
    stages = []
    for s in seed_stages:
        stages.append({
            "number": s["number"],
            "date": s["date"],
            "start_utc": cest_to_utc_iso(s["date"], s["start_time_cest"]),
            "est_finish_utc": cest_to_utc_iso(s["date"], s["est_finish_time_cest"]),
        })
    return {"stages": stages}


def main():
    seed_stages = json.loads(SEED_PATH.read_text(encoding="utf-8"))
    if len(seed_stages) != 21:
        raise SystemExit(f"expected 21 seed stages, found {len(seed_stages)}")

    race = build_race_json(seed_stages)
    watch = build_watch_json(seed_stages)

    DATA_DIR.mkdir(exist_ok=True)
    (DATA_DIR / "race.json").write_text(json.dumps(race, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (DATA_DIR / "watch.json").write_text(json.dumps(watch, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"wrote data/race.json ({race['totals']['distance_km']} km, {race['totals']['elevation_gain_m']} m over {race['totals']['stages']} stages)")
    print("wrote data/watch.json")


if __name__ == "__main__":
    main()
