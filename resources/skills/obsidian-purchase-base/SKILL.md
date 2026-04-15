---
name: obsidian-purchase-base
description: "Convert a CSV export from Joe's purchase wishlist Google Sheet into an Obsidian Base file and write it to the vault. Use this skill when Joe says things like 'let's build the purchase tracker base', 'convert my spreadsheet to a base', 'create the purchase wishlist base', or uploads a CSV and asks to create an Obsidian Base from it."
---

# Obsidian purchase base skill

This skill converts a CSV export of Joe's purchase wishlist Google Sheet into a valid Obsidian `.base` file and writes it directly to the vault via MCP.

## Background

Joe has an existing purchase wishlist note at `Resources/To move to purchase tracker note (TBD).md`. The goal is to replace that ad-hoc note with a proper Obsidian Base — a structured, filterable database view — built from a CSV export of his Google Sheet.

## What Obsidian Bases are

Bases are YAML-based `.base` files that define dynamic views of notes in an Obsidian vault. They are not databases themselves — they are *views* over notes whose data lives in frontmatter properties. Each item in the wishlist becomes its own note with frontmatter fields; the `.base` file defines how those notes are displayed and filtered.

## Step-by-step workflow

### Step 1: Receive the CSV

Joe will upload or paste a CSV export from his Google Sheet. Before proceeding, read the CSV and:

1. List all column headers
2. Identify the likely frontmatter property names (lowercase, hyphenated) each column should map to
3. Note any columns that are ambiguous or may need clarification

Show Joe the proposed column-to-property mapping in a simple two-column list and confirm before proceeding. Example:

```
Item name     → name (will become the note title)
Category      → category
Price         → price
Priority      → priority
Status        → status
URL/Link      → url
Notes         → notes
```

If a column doesn't have an obvious mapping, ask. Don't guess at intent.

### Step 2: Create the notes folder

All purchase wishlist notes should live in a dedicated folder. Propose this path unless Joe specifies otherwise:

```
Resources/Purchase wishlist/
```

If the folder doesn't exist, create it using the MCP tool before writing notes.

### Step 3: Create one note per item

For each row in the CSV, create a note at:

```
Resources/Purchase wishlist/<item-name>.md
```

Use the item name (slugified — lowercase, spaces replaced with hyphens) as the filename. Each note should have:

- A frontmatter block with all mapped properties
- A minimal body — just the item name as an H1 heading, plus the URL as a link if present

Example note for a keyboard entry:

```markdown
---
category: peripherals
price: 149
priority: medium
status: wishlist
url: https://www.lofree.co/products/lofree-flow100
notes: Ultra-slim aluminum mechanical keyboard, gasket mount
---

# Lofree Flow100

[Product page](https://www.lofree.co/products/lofree-flow100)
```

Write all notes in a batch. Confirm the count to Joe before writing: "Ready to create X notes in Resources/Purchase wishlist/ — proceed?"

### Step 4: Create the Base file

After notes are written, create the `.base` file at:

```
Resources/Purchase wishlist.base
```

#### Base file structure

The Base should include:

**Global filter** — scope the base to the wishlist folder only:
```yaml
filters:
  and:
    - file.inFolder("Resources/Purchase wishlist")
```

**Formulas** — include only what's useful given the actual columns present. Common useful ones:

```yaml
formulas:
  formatted_price: 'if(price, "$" + price.toFixed(2), "")'
  is_purchased: 'if(status == "purchased", "✅", "⏳")'
```

Only include formulas for columns that actually exist in the data.

**Properties** — configure display names for any properties that benefit from a cleaner label:
```yaml
properties:
  formula.formatted_price:
    displayName: "Price"
  formula.is_purchased:
    displayName: ""
  url:
    displayName: "Link"
```

**Views** — create at minimum two views:

1. **Wishlist** — shows all unpurchased items, grouped by category if that column exists:
```yaml
- type: table
  name: "Wishlist"
  filters:
    and:
      - 'status != "purchased"'
  order:
    - file.name
    - category
    - formula.formatted_price
    - priority
    - formula.is_purchased
  groupBy:
    property: category
    direction: ASC
```

2. **All items** — unfiltered, full list:
```yaml
- type: table
  name: "All items"
  order:
    - file.name
    - category
    - formula.formatted_price
    - priority
    - status
```

Optionally add a **Cards** view if an image or cover property exists in the data:
```yaml
- type: cards
  name: "Gallery"
  order:
    - file.name
    - category
    - formula.formatted_price
```

Adapt the `order` arrays to reflect the actual columns present — don't include columns that don't exist in the data.

### Step 5: Write the Base file

Write the completed `.base` file to `Resources/Purchase wishlist.base` using the MCP write tool.

Confirm to Joe: "Done — X notes created in Resources/Purchase wishlist/ and the Base file is at Resources/Purchase wishlist.base. Open it in Obsidian to verify the view renders correctly. If you see a YAML error, let me know and I'll fix the quoting."

## YAML rules for Base files

These are the most common failure points:

- Use single quotes for formulas that contain double quotes: `'if(status == "done", "✅", "⏳")'`
- Use double quotes for simple strings like view names: `"Wishlist"`
- Never leave special characters like `!`, `@`, `#`, `>`, `:` unquoted in filter expressions
- Formula references in `order` and `summaries` must be prefixed with `formula.`: `formula.formatted_price`
- All property names in frontmatter must be lowercase — no spaces, use hyphens

## Notes and edge cases

- If Joe's CSV has a column called something like "Purchased?" or "Bought" (boolean-ish), map it to a `status` field with values `wishlist` / `purchased` rather than using a raw boolean
- If price data has currency symbols (e.g. `$149.00`), strip the symbol and store as a plain number so formulas can do math on it
- If there's no category column, omit the `groupBy` directive from the Wishlist view
- If a URL column exists, include it in the note body as a clickable link, not just in frontmatter
- Do not include columns that are entirely empty across all rows
- The existing note at `Resources/To move to purchase tracker note (TBD).md` may have items not in the spreadsheet — flag this to Joe after the base is created so he can decide whether to fold them in manually
