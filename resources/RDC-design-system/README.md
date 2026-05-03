# Red Door Collaborative — Design System

Version 1.0 · 2025

An operational design system for generating on-brand assets and layouts. Built for use with Claude Design and any tool that can consume CSS custom properties and HTML component references.

## Folder structure

```
design-system/
├── colors_and_type.css          ← Token stylesheet — always import this first
├── fonts/
│   ├── fonts.css                ← @font-face declarations
│   ├── SuisseIntl-Thin.ttf
│   ├── SuisseIntl-Light.ttf
│   ├── SuisseIntl-LightIt.ttf
│   ├── SuisseIntl-Regular.ttf
│   ├── SuisseIntl-Book.ttf
│   ├── SuisseIntl-Medium.ttf
│   ├── SuisseIntl-Semibold.ttf
│   ├── SuisseIntl-Bold.ttf
│   ├── SuisseIntl-Black.ttf
│   ├── SuisseIntlCondensed-Regular.ttf
│   └── SuisseIntlMono-Bold.ttf
├── assets/
│   ├── logos/                   ← Download SVG/PNG from Box (see below)
│   └── icons/                   ← Download from Box: Icons/ folder
├── ui_kits/
│   └── components.html          ← Buttons, cards, badges, forms, type specimens
├── preview/                     ← Rendered preview images (add as generated)
├── uploads/                     ← Working files
├── SKILL.md                     ← Generation instructions for Claude
└── README.md                    ← This file
```

## Quick start

```html
<!-- In any HTML file within the design system -->
<link rel="stylesheet" href="fonts/fonts.css">
<link rel="stylesheet" href="colors_and_type.css">
```

Then reference semantic tokens in all styles:

```css
/* Always use semantic tokens, never raw hex values */
.cta-button {
  background: var(--color-action-primary);   /* #FF4F58 coral */
  color: var(--color-text-inverted);         /* #ffffff */
  border-radius: var(--radius-button);       /* 999px pill */
  font-family: var(--font-primary);          /* Suisse Intl */
  font-weight: var(--font-weight-display);   /* 700 */
}
```

## Token layers

`colors_and_type.css` organizes tokens into three layers:

**1. Primitive tokens** — raw brand values (`--rdc-coral-500: #FF4F58`). Never use these directly in components.

**2. Semantic tokens** — purpose-named aliases (`--color-action-primary`, `--font-size-h1`, `--space-lg`). Use these everywhere.

**3. Component tokens** — per-component variables (`--btn-primary-bg`, `--card-radius`, `--input-border`). Override at component scope only.

## Brand colors

| Token | Hex | Role |
|---|---|---|
| `--color-brand-primary` | `#FF4F58` | CTAs, links, active states |
| `--color-brand-secondary` | `#7F0046` | Secondary brand, icon marks |
| `--color-brand-dark` | `#0D1724` | Dark surfaces, high-authority type |
| `--color-brand-accent` | `#ABDCE0` | Tonal accent only |
| `--color-brand-gradient` | Wine→Coral 180° | Decorative use only |

## Typography

**Primary typeface:** Suisse Int'l (all weights loaded via `fonts/fonts.css`)
**Fallback:** Proxima Nova (Adobe Fonts), then `system-ui`

Weights available: Thin (100) · Light (300) · Regular (400) · Book (450) · Medium (500) · Semibold (600) · Bold (700) · Black (900)

## Font files

Font TTF/OTF files are not committed to this repo (binary files). Download them from Box:

**Box path:** Red Door File Database → Red Door Guidelines and Assets → RDC 2025 Branding → RDC_Brand-GUIDE-FINAL_Folder → Fonts

Place downloaded files in `design-system/fonts/` alongside `fonts.css`.

| File | Box ID |
|---|---|
| SuisseIntl-Thin.ttf | 1793776497294 |
| SuisseIntl-Light.ttf | 1793776228062 |
| SuisseIntl-LightIt.ttf | 1793778597034 |
| SuisseIntl-Regular.ttf | 1793776039090 |
| SuisseIntl-Book.ttf | 1793775220259 |
| SuisseIntl-Medium.ttf | 1793776307651 |
| SuisseIntl-Semibold.ttf | 1793778442820 |
| SuisseIntl-Bold.ttf | 1793766700385 |
| SuisseIntl-Black.ttf | 1793775726001 |
| SuisseIntlCondensed-Regular.ttf | 1793778618634 |
| SuisseIntlMono-Bold.ttf | 1793778644963 |

## Logo assets

Logo SVG/PNG files are stored in Box and should be placed in `design-system/assets/logos/` locally.

**Box path:** Red Door File Database → Red Door Guidelines and Assets → RDC 2025 Branding → Logos

| Variant | Box folder |
|---|---|
| Primary logo (full color) | 1-Primary Logo (RDC)/Primary Logo/1-Full Color/ |
| Primary horizontal | 2-Primary Horizontal (RDC)/ |
| Tertiary logo | 3-Tertiary Logo (RDC)/ |
| Primary icon | 4-Primary Icon/ |
| Secondary icon | 5-Secondary Icon/ |
| Social mark | 7-Social/ |

Primary logo SVG (full color, web): Box file ID `1757641069668`

## Component reference

Open `ui_kits/components.html` in a browser to see all components rendered with actual Suisse Int'l type and brand tokens. Includes: buttons (all variants and sizes), badges, content cards, metric cards, form elements, type scale, and alerts.

## Generation instructions

See `SKILL.md` for the full instruction set Claude uses when generating new assets against this design system. It covers color rules, typography rules, logo usage, spacing, component patterns, and tone of voice.

## Updating the system

When brand guidelines change:
1. Update primitive tokens in `colors_and_type.css` — semantic tokens cascade automatically
2. Update `SKILL.md` rules to reflect any new constraints
3. Re-render any preview images in `preview/`
4. Bump the version number in this README and in `colors_and_type.css`

---

**Source of truth:** RDC Brand Guide PDF — Box file ID `1788584828402`
