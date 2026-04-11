# Friction points

Known edge cases and fallbacks for vault gardening sessions.

- **Ambiguous tag fit** — if two tags both apply, propose both. Joe will decide.
- **Long notes with many potential links** — limit proposed related notes to 3–5 per note to
  avoid overwhelming the section. The most thematically proximate notes first.
- **Notes in Inbox** — treat these the same as any other note. Many inbox notes have no
  frontmatter at all.
- **Notes that are just stubs or very short** — use judgment. A 2-line stub may not need tags.
  Flag it and ask Joe if he wants to tag it or leave it.
- **`obsidian:patch_note` failure** — if the patch fails (likely due to curly quotes or em
  dashes in the anchor string), fall back to `obsidian:write_note` with the full note content.
  Always read the current note content fresh before attempting a full write.
- **Notes that already have a `## Related notes` section** — read the existing links before
  proposing additions. Don't suggest links that are already there.
