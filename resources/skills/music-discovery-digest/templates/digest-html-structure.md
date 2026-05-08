# HTML digest structure

Full layout specification for the weekly listening notes HTML file. Used in Step 6 of SKILL.md.

The live template fetched from the repo in Step 0 takes precedence over anything here if they conflict — this file documents the stable baseline.

---

## Design tokens

```css
:root {
  --stone-50:  #f9f8f6;   /* page background */
  --stone-100: #f0eeea;   /* section strip background, art placeholders */
  --stone-200: #e4e1db;   /* borders, art placeholder fill */

  --cobalt:    #003B8E;   /* ALL links and link underlines */

  --text-primary:   #111010;  /* headlines, artist names, strong text */
  --text-secondary: #2e2a27;  /* body copy, album titles */
  --text-tertiary:  #6a6259;  /* metadata, mono labels, footer */

  --rule:        rgba(15,13,12,0.10);
  --rule-strong: rgba(15,13,12,0.24);

  --font-sans: "IBM Plex Sans", system-ui, sans-serif;
  --font-mono: "IBM Plex Mono", monospace;

  --art-size: 200px;
  --col-gap:  48px;
}
```

**Color rules (do not deviate):**
- `--accent` exists in the CSS but is never used visibly. No green, no red anywhere.
- `\u2116XX` in hero title: `color: var(--text-primary)` — black, same as the rest of the title.
- Week label in sticky header: `color: var(--text-secondary)` — not an accent color.
- All links: `color: var(--cobalt)` with `border-bottom: 1px solid rgba(0,59,142,0.28)`.

---

## Sticky header

```html
<header class="site-header">
  <div class="inner">
    <span class="header-title">Still Point — Listening Notes</span>
    <span class="header-week">W{NN} · {DD Month YYYY}</span>
  </div>
</header>
```

Both `.header-title` and `.header-week` use `color: var(--text-secondary)`. No accent.

---

## Hero

```html
<div class="hero">
  <p class="hero-eyebrow">Weekly digest · {Month D, YYYY}</p>
  <div class="hero-lockup">
    <h1 class="hero-title">Listening<br>Notes <em>\u2116{NN}</em></h1>
    <div class="hero-stats">
      <div class="hero-stat"><strong>Sources</strong> — {list sources used this week}</div>
      <div class="hero-stat"><strong>Picks</strong> — {N} new discoveries · {N} known artists · {N} wildcard</div>
      <div class="hero-stat"><strong>RA</strong> — {status, e.g. "page unavailable this week"}</div>
    </div>
  </div>
  <hr class="hero-rule">
</div>
```

`.hero-title em`: `font-style: normal; color: var(--text-primary)` — black, not styled differently.

---

## Section strips

```html
<div class="section-head">
  <span class="section-index">01</span>
  <span class="section-label">New Discoveries <span>\u00d7{N}</span></span>
</div>
```

CSS: `margin: 0 -48px 52px; border-top: 2px solid var(--text-primary); background: var(--stone-100); padding: 11px 48px;`

The negative margin creates a full-bleed strip breaking out of the `.page` container padding. The count badge uses `color: var(--text-tertiary)`.

Section order and exact names:
1. `New Discoveries`
2. `New Releases from Artists You Know`
3. `Wildcard`
4. `Also Noted`

---

## Entry layout

2-column CSS grid: `200px` art + `1fr` body, `48px` gap.

```html
<div class="entry">
  <div class="art-wrap">
    <a href="[BOOMKAT_URL]" target="_blank">
      <img src="https://f4.bcbits.com/img/[IMAGE_ID]_0.jpg" alt="[ARTIST] — [ALBUM]" loading="lazy">
    </a>
    <div class="art-tag new">New</div>
  </div>
  <div class="entry-body">
    <div class="entry-artist">[Artist]</div>
    <div class="entry-album">[Album title]</div>
    <div class="entry-meta">
      <span>[Label]</span>
      <span>[Genre · Genre]</span>
      <span>[Month Year]</span>
    </div>
    <p class="entry-copy">[2–4 sentence write-up]</p>
    <div class="entry-links">
      <a href="[BOOMKAT_URL]" class="link primary" target="_blank">Boomkat ↗</a>
      <a href="[BANDCAMP_URL]" class="link" target="_blank">Bandcamp ↗</a>
      <a href="[YOUTUBE_SEARCH_URL]" class="link" target="_blank">Preview on YouTube</a>
    </div>
  </div>
</div>
```

Art tag classes:
- `.art-tag.new` — black background
- `.art-tag.known` — cobalt `#003B8E` background
- `.art-tag.wild` — amber `#a07010` background

---

## Also Noted section

Left column is an empty spacer (same width as art column), right column is the list with a left border.

```html
<div class="also-grid">
  <div></div>
  <div class="also-items">
    <div class="also-item">
      <span class="also-n">01</span>
      <span class="also-text"><strong>Artist — Title</strong> (Label) — one sentence note.</span>
    </div>
  </div>
</div>
```

---

## Footer

```html
<div class="site-footer">
  <p class="footer-note">[Italicised editorial note about the week]</p>
  <span class="footer-stamp">Still Point · 2026-W{NN}</span>
</div>
```

---

## Album art workflow

All art comes from Bandcamp CDN. Pattern:

```bash
curl -s --max-time 12 -L \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36" \
  -H "Accept: text/html" \
  "https://[artist].bandcamp.com/album/[slug]" \
  | grep -o 'og:image.*content="[^"]*"' | head -1 | grep -oP 'https://f[^"]+'
```

- `og:image` returns `_5` suffix (700px) — swap to `_0` for full resolution (1400×1400).
- If the artist Bandcamp slug fails, search for the label's Bandcamp page instead.
- Do not attempt to scrape art from Boomkat pages — they block og:image.
- For releases not on Bandcamp, use an SVG placeholder (see existing W13/W14/W16 files in the repo for examples).

### Known Bandcamp slugs

| Artist / Release | Bandcamp URL |
|---|---|
| Fabiano/Landmarks | mammoworks.bandcamp.com |
| Passarani | marcopassarani.bandcamp.com |
| Loidis/One Day | huercosplonk.bandcamp.com |
| MM/KM/Velours | kimochi.bandcamp.com |
| Millia/Sprawll | futuretimes.bandcamp.com/album/sprawll-ep |
| Rabit/Stranger | gangstalkers.bandcamp.com |
| Borderland/Transport | tresorberlin.bandcamp.com/album/transport |
| Inrain/Rise | music-from-memory.bandcamp.com/album/rise |
| Buttechno | buttechno.bandcamp.com |
| Irmin Schmidt | irminschmidt.bandcamp.com |
| Carla Dal Forno | carladalforno.bandcamp.com |
| Genioh Yamashirogumi | image: a0684238834_0.jpg (provided directly — not found via scraping) |
| Spivak & Prins Emanuel (Fasaan) | fasaan-recordings.bandcamp.com |

---

## Index entry format

New entries go at the **top** of the digest list in `index.html`:

```html
<div class="digest-item">
  <span class="digest-week">W{NN}</span>
  <a href="2026-W{NN}-listening-notes.html" class="digest-link">
    Listening Notes \u2116{NN} — [Artist 1], [Artist 2], [Artist 3], [Artist 4]
  </a>
  <span class="digest-meta">{DD Month YYYY}</span>
</div>
```

The index page title uses `.hero-title em` with `color: var(--text-primary)` — "Archive" in black.

---

## File naming

`2026-W{NN}-listening-notes.html`

Pushed to `docs/listening-notes/` on `main` branch of `joe-garvin/claude-knowledge-base`.
