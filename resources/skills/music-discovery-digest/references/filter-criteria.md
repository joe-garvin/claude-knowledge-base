# Filter criteria

Reference for the music discovery digest workflow. Used in Steps 2 and 3 of SKILL.md.

## Step 1: Known collection check

Before surfacing any release, cross-reference against the known artists in `Music taste profile.md`.

Rules:
- **Owned (local library):** Omit entirely unless it's a significant new release or reissue with a strong reason to flag.
- **Known (Spotify, 3+ tracks):** Flag as "new from an artist you know" if the release is new work. Omit if it's back-catalog or back-in-stock with no new angle.
- **Known alias / side project:** Treat as potentially unknown — surface it but note the connection.
- **2-track Spotify artists:** Treat as borderline known. Surface new releases but keep the bar higher.

## Step 2: Label and aesthetic match

**Include** releases on or adjacent to these label tiers (from taste profile):

Tier 1 (highest priority): Perlon, Future Times, Ilian Tape, DDS, Comatonse, Wild Oats / FTC, Apron, Mood Hut, Tartelet, Workshop, Warp, Rush Hour, Hessle Audio, Numbers, Shall Not Fade

Tier 2 (strong): Jiaolong, Ghostly, Ostgut Ton, R&S, Spectral Sound, Houndstooth, Tresor, Stones Throw, 100% Silk, Delsin, Rekids, Studio Barnhus, Acid Test, Wisdom Teeth, Stroom, Dekmantel, LuckyMe, Antinote, Still Music, Incienso

Tier 3 (monitor): L.I.E.S., Emotional Especial, Running Back, Crème Organization, New Kanada, Styles Upon Styles, Entropy, ESP Institute

**Positive aesthetic signals** (from reviews): minimal, deep, dub, textural, micro-house, lo-fi, Detroit, Chicago, IDM, abstract, rhythmic, introspective, conceptual, electroacoustic, long-form, austere, modular, dub techno, ambient, experimental

**Negative signals — deprioritize or omit:** functional, peak-time, banging, crossover, anthemic, commercial, tech house, progressive, trance, EDM-adjacent, vocal pop crossover

## Step 3: Deduplication

If the same release appears across multiple sources, merge into a single entry. Note which sources covered it (adds to confidence score).

## Scoring rubric

Score each surviving candidate 1–5. Pick the highest scorers for each output section.

| Signal | Points |
|---|---|
| Tier 1 label | +2 |
| Tier 2 label | +1 |
| Tier 3 / adjacent label | +0.5 |
| Known artist (new release) | +1 |
| Unknown artist, strong aesthetic match | +1 |
| Covered by Boomkat editorial | +2 |
| Covered by RA review | +1.5 |
| Multiple sources | +0.5 |
| Negative aesthetic signals | −2 |
| Back-catalog / back-in-stock only | −1 |

Target scores by section:
- **New discoveries:** 3.5+ from unknown artists
- **Known-artist picks:** 3+ from known artists with new releases
- **Wildcard:** 2.5+, deliberately outside the established profile
- **Also noted:** 2–3, near-misses worth tracking

## YouTube search URL format

`https://www.youtube.com/results?search_query=[Artist]+[Release Title]+[Label]`

Replace spaces with `+`. Include label name to disambiguate. Example:
`https://www.youtube.com/results?search_query=Passarani+Analog+Fingerprints+Vol+0+Numbers`
