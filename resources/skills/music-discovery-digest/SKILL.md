---
name: music-discovery-digest
description: "Run Joe's weekly music discovery digest. Use this skill whenever Joe says 'run my music digest', 'let's do the music digest', 'it's digest time', 'music discovery', 'run the digest', or any variation indicating he wants to generate a weekly music discovery note. Also trigger for short prompts like 'digest?', 'music this week?', 'what's new in music?', or 'let's do the weekly digest'. This skill pulls from Boomkat, Resident Advisor, Pitchfork, and other sources, filters releases against Joe's taste profile and known collection, and writes a curated note to his Obsidian vault."
---

# Music discovery digest skill

Generates Joe's weekly music discovery digest — a **single unified Obsidian note** pulling from all sources, filtered against his taste profile and known collection, with YouTube preview links for each pick.

**Timing:** Run on Fridays after the Boomkat weekly newsletter arrives (typically Friday morning UK time, mid-morning PST). If triggered earlier in the week, check whether the current week's Boomkat email has landed in Gmail before proceeding. If it hasn't arrived yet, note it in the digest and flag that picks may be incomplete pending that source.

**Output:** One note per week, organized by pick type (not by source). Never create separate per-source digest notes.

## Step 0: Load context

Read both of the following before doing anything else:

1. **Taste profile** (Obsidian vault): `Resources/Music Discovery/Music taste profile.md`
   Contains Joe's known artist lists, label priorities, genre/aesthetic fingerprint, and filter criteria. Everything downstream depends on it.

2. **Filter criteria**: `references/filter-criteria.md`
   The keyword lists, label tiers, and scoring rubric used in Steps 2 and 3.

## Step 1: Pull sources

Read `references/sources.md` for the full source list with access methods, URLs, and editorial notes.

Pull from all sources in sequence. If a source fails, note it and continue with the rest.

## Step 2: Filter each release

For every release found across all sources, apply the three-check filter described in `references/filter-criteria.md`:

1. Known collection check
2. Label and aesthetic match
3. Deduplication across sources

## Step 3: Score and select

Using the scoring rubric in `references/filter-criteria.md`, rank surviving candidates and assign each to the correct output section.

Target: 2–4 new discoveries · 1–3 known-artist picks · 1 wildcard · handful of also-noted items.

## Step 4: Build YouTube preview links

For each pick, construct a YouTube search URL per the format in `references/filter-criteria.md`.

## Step 5: Write the digest note

Use the template at `templates/digest-note.md` to structure the output.

Write to: `Resources/Music Discovery/YYYY-WNN — weekly digest.md`

Use ISO week number (e.g. W14 for week 14 of the year). If a note already exists for the current week, ask Joe whether to overwrite or append before writing.

For a completed example of correct output, see `examples/w13-digest.md`.

## Edge cases

Before starting, skim `references/friction-points.md` to load known failure modes and fallbacks. Consult it whenever something unexpected happens mid-run.
