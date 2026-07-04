#!/usr/bin/env python3
"""Build assets/img/route-map.svg — a stylized map of the whole 2026 route.

Reads data/race.json for each stage's start/finish/type (so labels and
marker colors stay in sync with the route data) and combines it with the
approximate town coordinates and mountain-massif shapes defined below.

The map is an original illustration, not a copy of any official race map:
- Land outlines are public-domain Natural Earth country borders (France +
  northern Spain), baked in as simplified paths.
- Soft "relief" shading marks the main massifs (Pyrenees, Massif Central,
  Alps, Jura, Vosges) — a stylized elevation cue, clipped to the land.
- Each stage is a marker linked to its stage page, colored by stage type.

Run from anywhere:
    python3 scraper/build_route_map.py
"""

import json
import math
import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
RACE_JSON = REPO_ROOT / "data" / "race.json"
OUT_SVG = REPO_ROOT / "assets" / "img" / "route-map.svg"
# Country outlines live next to this script's build inputs; fetched once from
# github.com/johan/world.geo.json (Natural Earth, public domain).
GEO_DIR = pathlib.Path(__file__).resolve().parent / "geo"

# Approximate [lon, lat] of each stage's finish town (stage 1 = Barcelona).
STAGE_COORDS = {
    1: (2.17, 41.39), 2: (2.17, 41.39), 3: (2.07, 42.57), 4: (1.61, 42.96),
    5: (-0.37, 43.30), 6: (0.00, 42.74), 7: (-0.58, 44.84), 8: (0.48, 44.85),
    9: (2.31, 45.55), 10: (2.74, 45.08), 11: (3.16, 46.99), 12: (4.85, 46.78),
    13: (6.86, 47.64), 14: (7.02, 47.92), 15: (6.40, 46.10), 16: (6.48, 46.37),
    17: (5.59, 45.36), 18: (6.33, 44.70), 19: (6.07, 45.09), 20: (6.07, 45.09),
    21: (2.35, 48.86),
}
# Small pixel nudges so co-located markers (Barcelona 1/2, Alpe d'Huez 19/20)
# stay individually clickable.
MARKER_NUDGE = {2: (-8, 7), 20: (-9, -8)}

# Mountain massifs: center [lon, lat] + half-widths in degrees [dlon, dlat]
# and a relative strength for the shading.
MASSIFS = [
    ("Pyrenees",       0.5, 42.65, 2.4, 0.55, 1.0),
    ("Massif Central", 2.9, 45.05, 1.5, 1.25, 0.85),
    ("Alps",           6.4, 45.25, 1.1, 1.45, 1.0),
    ("Alps-north",     6.5, 46.2,  0.7, 0.7,  0.7),
    ("Jura",           6.0, 46.6,  0.5, 0.85, 0.7),
    ("Vosges",         6.9, 48.0,  0.5, 0.7,  0.7),
]

TYPE_COLOR = {
    "flat": "#1aae39", "hilly": "#dd5b00", "mountain": "#c8443a",
    "individual_time_trial": "#2a9d99", "team_time_trial": "#2a9d99",
}

# Projection window (equirectangular with a cos(lat) correction).
LON0, LON1, LAT0, LAT1 = -5.5, 8.6, 40.2, 51.4
K = math.cos(math.radians((LAT0 + LAT1) / 2))
PAD = 26
SCALE = 62.0


def project(lon, lat):
    return ((lon - LON0) * K * SCALE + PAD, (LAT1 - lat) * SCALE + PAD)


def load_land():
    bbox = (-10, 10, 36, 52)
    rings = []
    for name in ("ESP", "FRA"):
        data = json.loads((GEO_DIR / f"{name}.geo.json").read_text())
        for feat in data["features"]:
            g = feat["geometry"]
            polys = g["coordinates"] if g["type"] == "Polygon" else [r for p in g["coordinates"] for r in p]
            for ring in polys:
                cx = sum(p[0] for p in ring) / len(ring)
                cy = sum(p[1] for p in ring) / len(ring)
                if bbox[0] <= cx <= bbox[1] and bbox[2] <= cy <= bbox[3]:
                    rings.append(ring)
    return rings


def ring_to_path(ring):
    pts = [project(lon, lat) for lon, lat in ring]
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z"


def build():
    race = json.loads(RACE_JSON.read_text())
    stages = {s["number"]: s for s in race["stages"]}
    land_rings = load_land()

    land_paths = "".join(
        f'<path d="{ring_to_path(r)}" fill="#efece4" stroke="#d7d0c0" stroke-width="1"/>'
        for r in land_rings
    )
    clip_paths = "".join(f'<path d="{ring_to_path(r)}"/>' for r in land_rings)

    # Relief ellipses (clipped to land)
    relief = []
    for _name, lon, lat, dlon, dlat, strength in MASSIFS:
        cx, cy = project(lon, lat)
        rx = dlon * K * SCALE
        ry = dlat * SCALE
        relief.append(
            f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" '
            f'fill="url(#relief)" opacity="{strength:.2f}"/>'
        )

    # Route line through the finishes in order
    seq = [project(*STAGE_COORDS[n]) for n in range(1, 22)]
    route = ("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in seq))

    # Markers as links
    markers = []
    for n in range(1, 22):
        s = stages.get(n, {})
        x, y = project(*STAGE_COORDS[n])
        dx, dy = MARKER_NUDGE.get(n, (0, 0))
        x += dx
        y += dy
        color = TYPE_COLOR.get(s.get("type"), "#928c7d")
        route_txt = f'{s.get("start", "")} → {s.get("finish", "")}'.strip(" →")
        title = f'Stage {n} — {route_txt}' if route_txt else f'Stage {n}'
        markers.append(
            f'<a href="stages/stage-{n:02d}.html" class="rm-marker">'
            f'<title>{title}</title>'
            f'<circle class="rm-hit" cx="{x:.1f}" cy="{y:.1f}" r="10" fill="transparent"/>'
            f'<circle class="rm-dot" cx="{x:.1f}" cy="{y:.1f}" r="3.6" fill="{color}" stroke="#fff" stroke-width="1.3"/>'
            f'</a>'
        )
    # Start / finish rings
    rings_svg = ""
    for n in (1, 21):
        x, y = project(*STAGE_COORDS[n])
        rings_svg += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="none" stroke="#213183" stroke-width="2" pointer-events="none"/>'

    font = 'font-family="Inter, system-ui, -apple-system, sans-serif"'

    def label(lon, lat, text, dx, dy, anchor="start", weight=600, size=13, color="#1a1a1a"):
        x, y = project(lon, lat)
        return (f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" {font} font-size="{size}" '
                f'font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{text}</text>')

    labels = "".join([
        label(2.17, 41.39, "Barcelona", 11, 5, "start", 700, 14),
        label(2.35, 48.86, "Paris", 11, -8, "start", 700, 14),
        label(-0.58, 44.84, "Bordeaux", -9, 4, "end", 600, 12, "#615d59"),
        label(6.07, 45.09, "Alpe d'Huez", 12, 3, "start", 600, 12, "#615d59"),
        label(0.0, 42.74, "Pyrenees", 0, 26, "middle", 600, 11, "#8a6d3b"),
        label(6.5, 45.0, "Alps", 12, 2, "start", 600, 11, "#8a6d3b"),
    ])

    width = (LON1 - LON0) * K * SCALE + 2 * PAD
    height = (LAT1 - LAT0) * SCALE + 2 * PAD

    svg = f'''<svg viewBox="0 0 {width:.0f} {height:.0f}" xmlns="http://www.w3.org/2000/svg" aria-label="Clickable map of the 2026 Tour de France route from Barcelona to Paris">
<defs>
<radialGradient id="relief" cx="50%" cy="50%" r="50%">
<stop offset="0%" stop-color="#9c7b48" stop-opacity="0.5"/>
<stop offset="55%" stop-color="#b89a6a" stop-opacity="0.26"/>
<stop offset="100%" stop-color="#b89a6a" stop-opacity="0"/>
</radialGradient>
<clipPath id="landclip">{clip_paths}</clipPath>
</defs>
<g>{land_paths}</g>
<g clip-path="url(#landclip)">{''.join(relief)}</g>
<path d="{route}" fill="none" stroke="#213183" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round" opacity="0.9" pointer-events="none"/>
<g class="rm-markers">{''.join(markers)}</g>
{rings_svg}
<g class="rm-labels" pointer-events="none">{labels}</g>
</svg>'''

    OUT_SVG.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT_SVG.relative_to(REPO_ROOT)} ({len(svg)} bytes, {len(land_rings)} land rings)")


if __name__ == "__main__":
    build()
