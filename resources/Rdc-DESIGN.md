# Red Door Collaborative — design system

Version 1.0 · 2025

---

## Contents

- [Brand colors](#brand-colors)
- [Typography](#typography)
- [Logos and marks](#logos-and-marks)
- [Spacing and layout](#spacing-and-layout)
- [Components](#components)
- [Usage rules](#usage-rules)
- [Asset library](#asset-library)

---

## Brand colors

### Primary palette

| Name | Hex | RGB | CMYK | Role |
|---|---|---|---|---|
| RDC Coral | `#FF4F58` | 255 · 79 · 88 | 0 · 84 · 58 · 0 | Primary action, accent |
| Squid | `#0D1724` | 13 · 23 · 36 | 87 · 75 · 56 · 71 | Dark surfaces, type |
| Wine | `#7F0046` | 127 · 0 · 70 | 35 · 100 · 48 · 25 | Secondary brand color |

### Secondary palette

| Name | Hex | RGB | CMYK | Role |
|---|---|---|---|---|
| Mist | `#ABDCE0` | 171 · 220 · 224 | 36 · 0 · 13 · 0 | Accent, tonal contrast |
| White | `#FFFFFF` | 255 · 255 · 255 | 0 · 0 · 0 · 0 | Backgrounds, reversed type |
| Gray | `#F3F3F3` | 243 · 243 · 243 | 3 · 2 · 2 · 0 | Light surface backgrounds |

### Gradient

A vertical Wine-to-Coral gradient (`#7F0046` → `#FF4F58`, 180°) is approved for decorative use only — not as a primary background treatment.

### Color pairing

- **Dark anchored:** Squid (dominant) + Wine + Coral
- **Coral on Squid:** Squid background, Coral CTA
- **Light with accent:** Gray background, Wine + Coral accent
- **High contrast tonal:** Wine + Mist

### Print references

| Color | Pantone (approx) | Notes |
|---|---|---|
| RDC Coral | 186 C | — |
| Squid | Black 6 C | — |
| Wine | 228 C | Spot: PANTONE 343 C (premium print) |
| Mist | 290 C | — |

For production print, use the `.ase` swatch file or Pantone references above.

---

## Typography

### Brand typeface

**Suisse Int'l** (Swiss Typefaces) is the primary typeface across all print and digital platforms. It's a functional, neutral grotesque with a wide weight range and excellent legibility at all sizes.

**Proxima Nova** is an approved secondary digital typeface (Adobe Fonts). Available weights: Light, Regular, Medium, Semibold, Bold, Extrabold.

### Weights in use

| Weight | Value | Use |
|---|---|---|
| Light | 300 | Large display, elegant subheadings |
| Regular | 400 | Body copy |
| Medium | 500 | UI labels, subheadings |
| Semibold | 600 | Section headings |
| Bold | 700 | Display headings, high-emphasis text |

### Type scale

| Level | Size | Weight | Tracking | Line height | Use |
|---|---|---|---|---|---|
| Display | 48px | 700 | −0.03em | 1.05 | Hero headlines |
| H1 | 36px | 600 | −0.02em | 1.1 | Page titles |
| H2 | 24px | 600 | −0.01em | 1.2 | Section headings |
| H3 | 18px | 600 | 0 | 1.3 | Component headings |
| Body | 16px | 400 | 0 | 1.7 | Paragraph copy |
| Small | 14px | 400 | 0 | 1.6 | Supporting copy, captions |
| Label | 11px | 600 | +0.1em | — | Uppercase tags, eyebrows |

### Rules

- Always sentence case for headings — never title case or all caps (labels excepted)
- Use no more than 3 weights on a single page
- Do not italicize headings as an emphasis style
- Do not set body copy in condensed or decorative variants

---

## Logos and marks

### Primary lockup

The full logo — circular Wine/Coral mark + "red door collaborative" lowercase wordmark — is the primary brand identifier. Use it first and foremost in all marketing materials.

### Color variants

| Variant | Background | Mark | Wordmark |
|---|---|---|---|
| Full color | White / light | Wine circle, Coral "rd" | Squid |
| Full color reversed | Squid / dark | Wine circle, Coral "rd" | White |
| Reversed coral | Coral | White circle, Coral "rd" | White |
| Black | Any light | Black | Black |
| White | Dark / photo | White | White |

### Mark only

Use the mark alone only when the full lockup is too wide for the context (e.g., app icons, social avatars, favicon). Available as: Wine/Coral (primary), Squid/Coral, Coral/White, Squid outline.

### Clear space

Maintain clear space equal to the height of the "r" letterform on all four sides of the logo. No type, graphics, or other elements may enter this zone.

### Minimum sizes

| Format | Minimum |
|---|---|
| Mark only | 24px |
| Full lockup | 120px wide |
| Print (mark) | 0.35 in |
| Print (lockup) | 1.5 in wide |

### Rules

- Always use approved logo files from Box — do not recreate
- Do not alter proportions, colors, or spacing
- Do not add drop shadows, outlines, or effects
- Do not place the full-color logo on complex photographic backgrounds without a protective field

---

## Spacing and layout

### Spacing scale (8pt grid)

| Token | Value | Common use |
|---|---|---|
| `space-1` | 4px | Icon gaps, tight inline elements |
| `space-2` | 8px | Between label and input, badge gaps |
| `space-3` | 12px | Between sibling elements |
| `space-4` | 16px | Card padding, base section gap |
| `space-6` | 24px | Section dividers, grid gaps |
| `space-8` | 32px | Major section padding |
| `space-12` | 48px | Page section breathing room |
| `space-16` | 64px | Hero and section-level spacing |

All spacing values should fall on 4px increments.

### Border radius

| Token | Value | Use |
|---|---|---|
| `radius-sm` | 2px | Subtle corners, rule accents |
| `radius-md` | 6px | Inputs, form elements |
| `radius-lg` | 10px | Cards, panels |
| `radius-xl` | 16px | Modals, large containers |
| `radius-pill` | 999px | Buttons (CTAs), badges |

### Layout grid

| Breakpoint | Width | Columns | Gutter | Margin |
|---|---|---|---|---|
| Mobile | < 768px | 4 | 16px | 16px |
| Tablet | 768–1024px | 8 | 24px | 32px |
| Desktop | 1024–1440px | 12 | 32px | 64px |
| Wide | > 1440px | 12 | 32px | auto |

Max content width: 1280px. Page sections use 80–100px top/bottom padding on desktop.

---

## Components

### Buttons

Three filled styles, two outlined styles, one ghost.

| Variant | Background | Text | Border | Use |
|---|---|---|---|---|
| Primary | `#FF4F58` Coral | White | — | Main CTA |
| Dark | `#0D1724` Squid | White | — | Secondary action on light surfaces |
| Wine | `#7F0046` Wine | White | — | Tertiary / branded accent |
| Outline coral | Transparent | Coral | 1.5px Coral | Secondary on white |
| Outline dark | Transparent | Squid | 1.5px Squid | Secondary on light |
| Ghost | Transparent | Muted | 0.5px border | Low-priority action |

All buttons use `border-radius: 999px` (pill shape). Sizes: Small (11px / 6px 14px padding), Default (13px / 9px 20px), Large (15px / 12px 28px).

### Badges and tags

Inline labels for categories, clients, and statuses. Always pill-shaped. Use tinted backgrounds derived from the brand palette — never solid fills for tags.

| Variant | Background | Text |
|---|---|---|
| Coral | `#FF4F58` at 12% | Dark coral |
| Squid | `#0D1724` at 8% | Primary text |
| Wine | `#7F0046` at 12% | Wine |
| Mist | `#ABDCE0` at 20% | Teal-dark |

### Cards

**Content cards** — white background, 0.5px border, 10px radius. A 5px top accent bar in Coral or Wine signals category. Internal structure: eyebrow (Coral, uppercase 10px) → title (16px/600) → body copy (13px) → optional CTA.

**Metric cards** — light gray background (`#F3F3F3`), no border. Label (11px uppercase, tertiary) above value (28px/700). Optional delta line below in success or muted color.

### Form elements

- Inputs: 14px Suisse Int'l, 9px 14px padding, 0.5px border, 8px radius. Focus state: Coral border + `#FF4F58` at 15% shadow.
- Select: same treatment as inputs, custom arrow.
- Labels: 12px/600, slightly tracked, secondary color, above the input.

### Alerts

Three semantic levels, each using a colored background tint + colored dot + title + body structure.

| Level | Background | Text color | Use |
|---|---|---|---|
| Brand / Coral | Coral at 7% | Dark coral | Brand notices, warnings |
| Info | System info tint | Info | Informational updates |
| Success | System success tint | Success | Confirmations, approvals |

---

## Usage rules

### Logo

**Do:** Use approved Box files. Maintain clear space. Match variant to background.

**Don't:** Recreate the logo. Alter proportions or colors. Add effects. Place full-color logo on complex imagery without a field.

### Color

**Do:** Lead with Coral for CTAs and primary actions. Use Squid to anchor dark surfaces. Use the Wine-to-Coral gradient for decorative accents only.

**Don't:** Use Mist as a primary page background — it's an accent color. Set Coral text on Wine backgrounds (insufficient contrast). Introduce off-brand colors without approval from the design lead.

### Typography

**Do:** Use Suisse Int'l for all branded communications. Use sentence case for headings. Create hierarchy through weight variation.

**Don't:** Use more than 3 weights per page. Use condensed or decorative variants for body copy. Italicize headings as emphasis.

### Photography and illustration

RDC uses a combination of custom illustrations (on file in Box under Custom RDC illustrations) and editorial photography. Photography should feel candid, human, and professional — not stock-photo staged. Illustrations use the brand palette and geometric line style.

---

## Asset library

All assets live in Box under: **Red Door File Database > Red Door Guidelines and Assets > RDC 2025 Branding**

| Asset | Format | Location |
|---|---|---|
| Primary logo (all variants) | SVG, PNG, AI, JPG | Logos/ |
| Horizontal lockup | SVG, PNG, AI | Logos/2-Primary Horizontal (RDC)/ |
| Tertiary logo | SVG, PNG, AI | Logos/3-Tertiary Logo (RDC)/ |
| Primary icon | SVG, PNG, AI | Logos/4-Primary Icon/ |
| Secondary icon | SVG, PNG, AI | Logos/5-Secondary Icon/ |
| Social mark | SVG, PNG | Logos/7-Social/ |
| Hex color swatches | .ase | RDC hex colors.ase |
| Brand guide | PDF | RDC_Brand-GUIDE-V1.0.pdf |
| PowerPoint template | .potx | 2025 RedDoor_Template.potx |
| Suisse Int'l font files | OTF (zipped) | swisstypefaces-[...].zip |
| Custom illustrations | — | Custom RDC illustrations/ |
| Icons | — | Icons/ |
| Social media assets | — | RDC social media/ |
| Website graphics | — | Website Graphics/ |

For questions about brand usage or asset requests, contact the RDC creative team.
