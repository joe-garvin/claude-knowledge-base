# Friction points

Known failure modes in the music digest workflow and how to handle them. Skim before starting each run.

---

## Gmail / Boomkat

**Boomkat email not yet arrived**
The weekly digest drops Friday mornings UK time. If you're running the workflow before it lands, check Gmail first. If it's not there, proceed with other sources and add a note at the top of the digest: *"Boomkat W[N] newsletter had not arrived at time of writing — picks may be incomplete. Revisit to append."*

**Boomkat email search returns no results**
Try alternate queries: `from:mailboy@boomkat.com`, `from:boomkat`, or just `boomkat` with a date filter. The sender address has historically been `mailboy@boomkat.com`.

**Boomkat surfaces back-catalog items as new**
Common — Boomkat frequently highlights back-in-stock vinyl or catalog discoveries alongside new releases. Always check release dates. Filter out anything not released within the past 2–3 weeks unless it's a significant reissue with a clear editorial hook.

---

## RA / web sources

**RA reviews page returns empty or navigation-only**
The RA reviews pages (`ra.co/reviews/albums`, `ra.co/reviews/singles`) sometimes return minimal content when fetched. Fallback options in order:
1. Search `site:ra.co reviews [artist or label] 2026`
2. Check `ra.co/music` homepage — RA Recommends is often visible there
3. Search `Resident Advisor new reviews [month] [year]` and fetch individual review URLs

**Pitchfork returns mainstream results**
Apply the aesthetic filter aggressively. If a Pitchfork pick doesn't have at least two positive aesthetic signals from the filter-criteria list, skip it.

---

## Obsidian / file writing

**obsidian:write_note tool not available**
This happens in long conversations when tools get pruned from context. Options:
1. Start a fresh conversation and run the digest from the top — tools will be available
2. Produce the digest content in chat and ask Joe to paste it manually into the vault

**Note already exists for current week**
Ask Joe before overwriting: *"A digest note for W[N] already exists. Overwrite, append, or skip?"*

---

## HTML output / GitHub

**GitHub push fails or tools unavailable**
If `github:push_files` isn't in context, start a fresh Desktop session. As a fallback, write the HTML content to chat and note what files need pushing. Never silently skip the push.

**Index not updated**
Always update `index.html` in the same commit as the new digest file. A digest that exists but isn't in the index is effectively invisible.

**Live template fetch fails**
If the raw GitHub URL for the most recent digest returns an error, fall back to the layout spec in `templates/digest-html-structure.md` as the baseline. Note in the session that the live template was unavailable.

**Art not found on Bandcamp**
Check `templates/digest-html-structure.md` → "Known Bandcamp slugs" before giving up. If still not found, use the SVG placeholder — do not leave an empty `<img>` tag. Reference the W13/W14/W16 files in the repo for placeholder examples.

**Obsidian markdown note is secondary**
If the GitHub push succeeds but the Obsidian write fails, that's acceptable — the HTML is the primary record.

---

## Scoring / filtering

**Too many candidates, hard to choose**
Apply the scoring rubric strictly. Anything below 3.0 goes to "also noted" at most. If still too many, prioritize Boomkat editorial picks over web research picks — Boomkat has the strongest aesthetic alignment.

**No strong candidates in a given week**
Thin weeks happen. Lower the also-noted threshold and be honest about it in the digest header: *"Light week for in-profile releases — a few near-misses in also noted."* Don't inflate picks to hit a target count.

**Unknown artist with no label information**
Skip unless Boomkat or RA editorial copy provides enough aesthetic context to score it confidently. Don't surface artists based on name alone.
