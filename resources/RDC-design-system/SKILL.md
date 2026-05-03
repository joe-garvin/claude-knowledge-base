# Red Door Collaborative — Design System SKILL

Use this skill whenever generating any visual asset, layout, component, or design output for Red Door Collaborative. This is the authoritative instruction set for producing on-brand work.

## Identity

**Agency:** Red Door Collaborative (RDC)
**Location:** Bellevue, WA
**Positioning:** Boutique creative agency specializing in marketing for enterprise tech clients (Microsoft, Databricks, Salesforce, Meta).
**Voice:** Professional, sharp, human. No jargon. Benefits before features. Direct without being blunt.

## File structure

```
design-system/
├── colors_and_type.css     ← Token stylesheet — always import this
├── fonts/
│   ├── fonts.css           ← @font-face declarations
│   └── SuisseIntl-*.ttf   ← Full Suisse Int'l family (download from Box)
├── assets/
│   ├── logos/              ← SVG/PNG logo variants
│   └── icons/              ← Brand icon set (Icon 1–9)
├── ui_kits/
│   ├── buttons.html        ← Button component reference
│   ├── cards.html          ← Card components
│   ├── badges.html         ← Badges and tags
│   ├── forms.html          ← Form elements
│   └── typography.html     ← Type specimens
├── preview/                ← Rendered preview images
├── uploads/                ← Working files
├── SKILL.md                ← This file
└── README.md               ← Human-readable overview
```

## Token usage

Always import `colors_and_type.css` and reference **semantic tokens** in all output. Never hardcode raw hex values in components — use the token layer.

```css
/* ✓ Correct — semantic token */
.cta { background: var(--color-action-primary); }

/* ✗ Wrong — hardcoded primitive */
.cta { background: #FF4F58; }
```

## Color

### Palette

| Token | Value | Role |
|---|---|---|
| `--color-brand-primary` | `#FF4F58` | CTAs, links, active states, accents |
| `--color-brand-secondary` | `#7F0046` | Secondary brand, icon circles, gradient base |
| `--color-brand-dark` | `#0D1724` | Dark backgrounds, type on light |
| `--color-brand-accent` | `#ABDCE0` | Tonal accent, supporting color only |
| `--color-brand-gradient` | Wine→Coral 180° | Decorative only — never for backgrounds |

### Color rules

- **Coral** leads all CTAs and primary interactive elements
- **Squid** anchors dark surfaces — headers, footers, sidebar nav
- **Wine** is used for icon marks, secondary brand moments, and gradient base
- **Mist** is an accent only — never use as a page or section background
- **Gradient** (Wine→Coral, 180°) is decorative — use sparingly for visual interest, not as a primary surface
- Never place Coral text on Wine backgrounds — contrast is insufficient
- Do not introduce off-brand colors without approval

### Color pairing patterns

```
Dark anchored:    Squid (dominant) + Wine + Coral accents
Coral on Squid:   Squid background + Coral CTAs + White text
Light with accent: Gray-50 background + Wine/Coral accents
High contrast:    Wine + Mist (complementary tonal pair)
```

## Typography

### Typeface

**Primary:** Suisse Int'l (all weights, all contexts)
**Condensed:** Suisse Intl Condensed (display/headline use only)
**Mono:** Suisse Intl Mono Bold (code, tokens, technical labels)
**Digital fallback:** Proxima Nova (Adobe Fonts) when Suisse Int'l is unavailable

### Weight usage

| Weight | Value | When to use |
|---|---|---|
| Light | 300 | Large display, elegant subheadings |
| Regular | 400 | All body copy |
| Book | 450 | Mid-weight body, refined labels |
| Medium | 500 | UI labels, nav items, metadata |
| Semibold | 600 | Headings (H2–H4), card titles |
| Bold | 700 | Display, H1, high-emphasis CTAs |
| Black | 900 | Rare — oversized display only |

**Maximum 3 weights per page or layout.** Hierarchy through weight, not color.

### Type scale

| Role | Size | Weight | Tracking | Leading |
|---|---|---|---|---|
| Display | 48px | 700 | −0.03em | 1.05 |
| H1 | 36px | 600–700 | −0.02em | 1.1 |
| H2 | 24px | 600 | −0.01em | 1.2 |
| H3 | 18px | 600 | 0 | 1.3 |
| H4 | 16px | 600 | 0 | 1.4 |
| Body | 16px | 400 | 0 | 1.7 |
| Body SM | 14px | 400 | 0 | 1.6 |
| Label | 11px | 600 | +0.10em | — |
| Eyebrow | 11px | 600 | +0.14em | — |

### Typography rules

- **Always sentence case** for headings — never title case, never all caps (eyebrows/labels excepted)
- Eyebrows and labels are always uppercase with tracked spacing
- Do not italicize headings as emphasis — use weight instead
- Do not set body copy in Condensed variant

## Logo

### Primary lockup

Circle mark (Wine background, Coral "rd" letterform) + lowercase "red door collaborative" wordmark in Suisse Intl Semibold.

### Logo variants and when to use them

| Variant | Background | Mark | Wordmark |
|---|---|---|---|
| Full color | White / light gray | Wine circle, Coral rd | Squid |
| Full color reversed | Squid / dark | Wine circle, Coral rd | White |
| Coral reversed | Coral | White circle, Coral rd | White |
| Black | Any light | Black | Black |
| White (outline) | Dark / photo | White outline | White |

### Logo rules

- Always source from Box — never recreate
- Never alter proportions, colors, or letterforms
- No drop shadows, outlines, glows, or effects
- Maintain clear space equal to the height of the "r" letterform on all sides
- Minimum: 24px (mark alone), 120px wide (full lockup)
- Full-color logo on photography requires a protective field

### Box logo asset paths

```
Logos/1-Primary Logo (RDC)/Primary Logo/1-Full Color/Web/
  → red-door-collaborative-primary-logo-full-color-rgb.svg  (ID: 1757641069668)
  → red-door-collaborative-primary-logo-full-color-rgb.png  (ID: 1757641183064)

Logos/2-Primary Horizontal (RDC)/
Logos/3-Tertiary Logo (RDC)/
Logos/4-Primary Icon/
Logos/5-Secondary Icon/
Logos/7-Social/
```

## Spacing

Built on an 8pt grid. All values are multiples of 4px.

```
--space-xs:   4px   Icon gaps, tight inline
--space-sm:   8px   Between label and input
--space-md:  16px   Card padding (base unit)
--space-lg:  24px   Grid gaps, section dividers
--space-xl:  32px   Major section padding
--space-2xl: 48px   Section breathing room
--space-3xl: 64px   Hero spacing
--space-4xl: 80px   Page section top/bottom padding
```

## Components

### Buttons

All buttons use `border-radius: var(--radius-button)` (pill shape, 999px).

```
Primary:       Coral fill + white text     → main CTA
Dark:          Squid fill + white text     → secondary on light
Wine:          Wine fill + white text      → tertiary / branded
Outline coral: Transparent + coral border  → secondary on white
Outline dark:  Transparent + squid border  → secondary on light
Ghost:         Transparent + gray border   → low-priority
```

### Cards

Two types:

**Content card:** White bg, 1px `--color-border-default` border, `--radius-card` (12px). Structure: 4px accent bar (Coral or Wine) → eyebrow label (Coral, uppercase, 10px) → title (16px/Semibold) → body (13px) → optional CTA.

**Metric card:** `--color-surface-subtle` bg, no border, 8px radius. Label (10px uppercase) → value (28–30px/Bold) → optional delta.

### Badges

Always pill-shaped. Use tinted backgrounds — never solid fills for status tags.

```
Coral:   rgba(255,79,88,0.12)  + dark coral text
Squid:   rgba(13,23,36,0.08)   + squid text
Wine:    rgba(127,0,70,0.12)   + wine text
Mist:    rgba(171,220,224,0.30) + teal-dark text
```

### Forms

- Inputs: 14px Suisse Intl, `--input-padding-y` / `--input-padding-x`, `--input-border`, `--radius-input` (8px)
- Focus state: `--input-border-focus` (Coral) + `--input-shadow-focus` (Coral at 25%)
- Labels: 12px / Semibold / slightly tracked / `--color-text-secondary` / always above input

## Usage rules summary

| Element | Do | Don't |
|---|---|---|
| Logo | Use Box files, match variant to bg, maintain clear space | Recreate, alter, add effects |
| Color | Coral for CTAs, Squid for dark surfaces, gradient decoratively | Mist as bg, Coral on Wine, off-brand colors |
| Type | Suisse Intl, sentence case, weight for hierarchy | 3+ weights, condensed for body, italic headings |
| Spacing | 4px increments, 8pt grid | Arbitrary values |
| Photography | Candid, human, editorial | Stock-photo staged, heavy filters |

## Tone of voice

When writing copy alongside visuals:

- Lead with benefits, not features
- Use "business" not "organization" (SMB contexts)
- Vary sentence rhythm — avoid formulaic cadence
- No contrastive negation ("not X, it's Y") — it reads as AI-generated
- No filler phrases or soundbite structures
- Sentence case everywhere, including headlines
