---
name: music-discovery-digest
description: "Run Joe's weekly music discovery digest. Use this skill whenever Joe says 'run my music digest', 'let's do the music digest', 'it's digest time', 'music discovery', 'run the digest', or any variation indicating he wants to generate a weekly music discovery note. Also trigger for short prompts like 'digest?', 'music this week?', 'what's new in music?', or 'let's do the weekly digest'. This skill pulls from Boomkat, Resident Advisor, Pitchfork, and other sources, filters releases against Joe's taste profile and known collection, and produces a curated HTML file pushed to the joe-garvin/claude-knowledge-base repo."
---

# Music discovery digest skill

Generates Joe's weekly music discovery digest as an **HTML file** pushed to `docs/listening-notes/` in `joe-garvin/claude-knowledge-base`. A secondary markdown note to the Obsidian vault is optional.

**Timing:** Run on Fridays after the Boomkat weekly newsletter arrives (typically Friday morning UK time, mid-morning PST). If triggered earlier in the week, check whether the current week's Boomkat email has landed in Gmail before proceeding.

**Primary output:** `docs/listening-notes/2026-W{NN}-listening-notes.html` pushed to `main` branch, plus an updated `docs/listening-notes/index.html`.

**Secondary output (optional):** Markdown note at `Resources/Music Discovery/YYYY-WNN — weekly digest.md` in the Obsidian vault.

---

## Step 0: Load context and fetch live template

Read all of the following before doing anything else:

1. **Taste profile** (Obsidian vault): `Resources/Music Discovery/Music taste profile.md`
2. **Filter criteria**: `references/filter-criteria.md`
3. **Friction points**: `references/friction-points.md` — skim for known failure modes
4. **Live template**: Fetch the most recent digest from the repo to use as the HTML baseline:
   ```
   https://raw.githubusercontent.com/joe-garvin/claude-knowledge-base/main/docs/listening-notes/index.html
   ```
   Identify the most recent digest filename from the index, then fetch:
   ```
   https://raw.githubusercontent.com/joe-garvin/claude-knowledge-base/main/docs/listening-notes/[most-recent-filename].html
   ```
   This is the canonical template. Any design changes made to prior digests automatically propagate forward this way.

---

## Step 1: Pull sources

Read `references/sources.md` for the full source list with access methods, URLs, and editorial notes.

**Boomkat emails — correct Gmail search:**
- Weekly Digest: `from:mailboy@boomkat.com subject:"Weekly Digest"` → use `Gmail:search_threads` then `Gmail:get_thread` with `messageFormat: FULL_CONTENT`. Pass the **thread ID**, not the message ID.
- Download Now: `from:mailboy@boomkat.com subject:"Download Now"` — pull alongside the weekly digest.

Pull from all sources in sequence. If a source fails, note it in the digest header and continue.

---

## Step 2: Filter each release

For every release found, apply the three-check filter in `references/filter-criteria.md`:
1. Known collection check
2. Label and aesthetic match
3. Deduplication across sources

---

## Step 3: Score and select

Using the scoring rubric in `references/filter-criteria.md`, rank candidates and assign each to the correct output section.

Target: 2–4 new discoveries · 1–3 known-artist picks · 1 wildcard · 3–6 also-noted items.

**Exact section names (use these strings verbatim, no subtext appended):**
1. `New Discoveries`
2. `New Releases from Artists You Know`
3. `Wildcard`
4. `Also Noted`

---

## Step 4: Fetch album art

For each pick, retrieve album art from Bandcamp CDN. Full workflow in `templates/digest-html-structure.md` → "Album art workflow" section.

Short version:
```bash
curl -s --max-time 12 -L \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36" \
  -H "Accept: text/html" \
  "https://[artist].bandcamp.com/album/[slug]" \
  | grep -o 'og:image.*content="[^"]*"' | head -1 | grep -oP 'https://f[^"]+'
```

- Swap `_5` suffix to `_0` for full resolution (1400×1400).
- If artist Bandcamp slug fails, try the label's Bandcamp page instead.
- Do not attempt to fetch art from Boomkat — it blocks og:image scraping.
- For releases not on Bandcamp, use the SVG placeholder defined in `templates/digest-html-structure.md`.

Known tricky Bandcamp slugs are documented in `templates/digest-html-structure.md` → "Known Bandcamp slugs."

---

## Step 5: Build links

For each pick, construct:
- Boomkat product URL (from email or web)
- Bandcamp album URL (from Step 4 research)
- YouTube search URL: `https://www.youtube.com/results?search_query=[Artist]+[Release+Title]+[Label]`

---

## Step 6: Write the HTML digest

Using the live template fetched in Step 0, build the HTML file for the current week.

Full layout spec, CSS tokens, and component markup are in `templates/digest-html-structure.md`. Follow it exactly — do not invent new design patterns or deviate from the established CSS variables.

Key rules:
- The `№XX` issue number in the hero title: `color: var(--text-primary)` — black, no accent color.
- The week label in the sticky header: `color: var(--text-secondary)` — same as the left-side label, no accent.
- Links always cobalt `#003B8E` with `border-bottom: 1px solid rgba(0,59,142,0.28)`.
- Art tags: `.art-tag.new` (black bg), `.art-tag.known` (cobalt bg), `.art-tag.wild` (amber `#a07010` bg).

File to generate: `2026-W{NN}-listening-notes.html`

---

## Step 7: Update the index

Fetch the current index:
```
https://raw.githubusercontent.com/joe-garvin/claude-knowledge-base/main/docs/listening-notes/index.html
```

Add the new entry at the **top** of the digest list:
```html
<div class="digest-item">
  <span class="digest-week">W{NN}</span>
  <a href="2026-W{NN}-listening-notes.html" class="digest-link">
    Listening Notes \u2116{NN} — [Artist 1], [Artist 2], [Artist 3], [Artist 4]
  </a>
  <span class="digest-meta">{DD Month YYYY}</span>
</div>
```

---

## Step 8: Push to GitHub

Use `github:push_files` to push both files in a single commit to `joe-garvin/claude-knowledge-base`, `main` branch:
- `docs/listening-notes/2026-W{NN}-listening-notes.html`
- `docs/listening-notes/index.html`

Commit message format: `Add W{NN} listening notes digest`

Always specify `owner: joe-garvin` explicitly in the push call.

---

## Step 9: Optional vault note

If Joe wants a secondary markdown note, write it to `Resources/Music Discovery/YYYY-WNN — weekly digest.md` using the template at `templates/digest-note.md`. This is a lightweight summary, not a duplicate of the full HTML. Ask before writing if not explicitly requested.
