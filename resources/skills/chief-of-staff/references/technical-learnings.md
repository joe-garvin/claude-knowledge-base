# Chief of Staff — Technical Learnings Repository

This reference contains accumulated technical patterns and fixes that apply
across CoS users. These are tool-specific gotchas and best practices that
have been validated through real-world use.

The CoS should also maintain **user-specific** learnings in memory. When a
user encounters and resolves a technical issue, commit the fix to memory
so it's never repeated.

---

## Document Generation (PPTX / DOCX)

### PowerPoint (pptx)

- Internal slide hyperlinks require relationship type `.../slide` (not
  `hyperlink`) in `.rels` files; no `TargetMode` attribute; `hlinkClick`
  must include `action="ppaction://hlinksldjump"`
- Font declarations must be explicit `<a:latin typeface="..."/>` tags in
  each `<a:rPr>` — theme inheritance only works with theme placeholders
- In pptxgenjs, never stack a rectangle shape + separate text box for
  table cells — creates a double-box rendering bug. Use a single
  `addText()` with fill and line properties set directly.
- Placeholder text in response cells must use a readable color (e.g.,
  steel blue `#5A7FA8`), never a faint tint
- Readability is the top priority: use the largest font size that fits,
  with 9pt as the absolute minimum floor. Prefer 11-12pt for body text.
  Split content across slides rather than shrinking fonts.

### Word Documents (docx)

- Use the `/mnt/skills/public/docx/` skill for generation
- Validate output with the office validation script when available

### Excel (xlsx)

- `merge_cells()` in openpyxl causes Excel corruption — use matching
  fills on individual cells instead
- `insert_cols()` creates unstyled cells that must be explicitly filled
- Data validation `sqref` references don't auto-update after structural
  column changes
- Ampersands in XML content must be encoded as `&amp;`
- Verify ZIP integrity with `zipfile.ZipFile.testzip()` — `None` = OK
- Checkbox cells in shared strings must be `t="s"`, headers stay `inlineStr`

---

## Git / GitHub

- `.gitattributes` must declare binary files before pushing (`*.xlsx binary`,
  `*.pptx binary`, etc.) to prevent line-ending corruption
- After adding binary declarations, `git rm --cached [file]` re-indexes
  previously committed files
- `git pull --rebase origin main` before pushing resolves divergence conflicts
- Emoji-prefixed folder names must be preserved exactly in all file operations
- Always push complex binary file updates via fresh clone

---

## General Patterns

- When generating conditional formatting rules for Excel, use `CODE()`
  for checkbox comparison rather than string comparison
- Date formatting in filenames should follow the user's stated convention
  (capture during onboarding — common formats: MMDDYYYY, YYYY-MM-DD, DDMMYYYY)
- Color-coded status systems should be consistent across all deliverables
  for a given user — capture their color mapping during onboarding

---

## Adding New Learnings

When a user encounters and resolves a technical issue:

1. Identify the root cause and fix
2. Generalize: does this apply to a specific tool, or is it broader?
3. Commit to the user's memory as a CoS Learning entry
4. If it's broadly applicable, flag it as a candidate for this reference doc

Memory format:
```
CoS Learning: [Tool/Context] — [Description of issue and fix]
```
