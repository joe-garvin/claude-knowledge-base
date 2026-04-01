# Sources

All active sources for the weekly music discovery digest. Pull in sequence. If a source fails or is unavailable, note it in the digest header and continue.

---

## 1. Boomkat weekly digest (primary)

**Access:** Gmail — search `from:boomkat subject:"Weekly Digest"`
**Cadence:** Arrives Friday mornings UK time (typically 10am GMT / mid-morning PST)
**Read method:** Pull the most recent message. Read full body — Boomkat's editorial descriptions are the highest-signal input in the workflow.
**What to extract:** Artist, release title, label, genre tags, Boomkat's editorial language, Boomkat product URL
**Weight:** Highest. Boomkat editorial is the most reliable aesthetic filter for this collection.
**Notes:** Occasionally surfaces back-catalog or back-in-stock items alongside new releases. Check release dates — filter out anything that isn't new this week unless it's a significant reissue.

## 2. Boomkat "Download Now" email (secondary)

**Access:** Gmail — search `from:boomkat subject:"Download Now"`
**Cadence:** Arrives same day as the weekly digest, usually a few hours earlier
**Read method:** Pull alongside the weekly digest. Shorter format, less editorial copy.
**What to extract:** Same as above. Cross-reference with weekly digest to catch duplicates.
**Weight:** Medium. Good for catching digital-only or download-focused releases the digest may skip.

## 3. Resident Advisor — new reviews

**Access:** Web fetch `https://ra.co/reviews/albums` and `https://ra.co/reviews/singles`
**Cadence:** Updated continuously; check for reviews published in the current week
**Read method:** Fetch the page, extract review titles, artists, labels, scores, and any editorial snippets visible
**What to extract:** Artist, release, label, RA score (if shown), genre description
**Weight:** High for albums with strong scores. RA's taste skews more mainstream than Boomkat for club music — apply the aesthetic filter carefully.
**Notes:** RA's album reviews page may not render full content via fetch. If the fetch returns only navigation, fall back to searching `site:ra.co/reviews [artist or label]` or checking RA Recommends.

## 4. Pitchfork — electronic/experimental

**Access:** Web search `pitchfork new reviews electronic experimental [current month year]`
**Cadence:** Check for reviews from the current week
**What to extract:** Artist, release, label, Pitchfork score, genre tags
**Weight:** Lower than Boomkat/RA for this collection. Pitchfork skews toward accessible crossover. Only surface picks that score 7.5+ and pass the aesthetic filter.
**Notes:** Best used as a cross-reference or wildcard source, not a primary discovery channel.

## 5. The Wire — new releases

**Access:** Web search `the wire magazine new releases [current month year]`
**Cadence:** Monthly magazine, but online coverage is continuous
**What to extract:** Artist, release, label, Wire editorial language
**Weight:** Medium-high for experimental, electroacoustic, and leftfield picks. Strong signal for wildcard slot candidates.

## 6. Bandcamp New & Notable / Weekly

**Access:** Web fetch `https://daily.bandcamp.com/` or search `bandcamp new notable electronic [current week]`
**Cadence:** Updated weekly (Bandcamp Weekly drops Thursdays)
**What to extract:** Artist, release, label, Bandcamp editorial description
**Weight:** Medium. Good for independent and self-released material that Boomkat/RA may not cover.

---

## Source priority summary

| Source | Weight | Best for |
|---|---|---|
| Boomkat Weekly Digest | ★★★★★ | Primary picks, editorial framing |
| Boomkat Download Now | ★★★★ | Digital releases, cross-reference |
| Resident Advisor | ★★★★ | Club music, albums |
| The Wire | ★★★ | Experimental, wildcard slot |
| Bandcamp | ★★★ | Independent releases |
| Pitchfork | ★★ | Cross-reference, sanity check |
