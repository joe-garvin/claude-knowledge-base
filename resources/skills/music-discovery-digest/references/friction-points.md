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

## Scoring / filtering

**Too many candidates, hard to choose**
Apply the scoring rubric strictly. Anything below 3.0 goes to "also noted" at most. If still too many, prioritize Boomkat editorial picks over web research picks — Boomkat has the strongest aesthetic alignment.

**No strong candidates in a given week**
Thin weeks happen. Lower the also-noted threshold and be honest about it in the digest header: *"Light week for in-profile releases — a few near-misses in also noted."* Don't inflate picks to hit a target count.

**Unknown artist with no label information**
Skip unless Boomkat or RA editorial copy provides enough aesthetic context to score it confidently. Don't surface artists based on name alone.
