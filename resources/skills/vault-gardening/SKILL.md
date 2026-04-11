---
name: vault-gardening
description: >
  Maintain Joe's Obsidian vault ("Still Point") by scanning all notes for missing or incomplete
  tags and missing inter-note links, then proposing improvements one note at a time for approval.
  Use this skill whenever Joe says "run vault maintenance", "let's do vault gardening", "tag my
  notes", "check for missing tags", "link my notes", "run the gardening skill", "let's maintain
  the vault", or any variation indicating he wants to audit and improve tags and wikilinks across
  the vault. Also trigger when Joe says things like "any notes without tags?" or "what notes
  aren't linked to anything?" This is a repeatable, periodic workflow — not a one-time task.
---

# Vault Gardening Skill

A repeatable vault maintenance workflow for the Still Point Obsidian vault. Scans all notes,
identifies gaps in tagging and inter-note linking, and proposes improvements note by note with
Joe's approval before writing anything.

## Overview

This skill does two things:
1. **Tagging** — finds notes with no tags or obviously incomplete tags and proposes additions
   drawn only from the vault's existing tag vocabulary (never inventing new tags)
2. **Linking** — finds notes that have no `## Related notes` section or have a sparse one, and
   proposes wikilinks to thematically related notes elsewhere in the vault

Joe reviews each proposal and confirms, edits, skips, or stops the session.

## Constraints

- **Never invent new tags.** Only use tags that already exist in the vault, discovered by
  `obsidian:list_all_tags` at the start of each session.
- **Tag vocabulary filter.** The vault has a long tail of one-off tags (count = 1) that are
  noise. Prefer tags with count ≥ 2 unless a one-off tag is an exceptionally precise fit.
  Core vocabulary as of initial skill creation:
  `personal`, `dharma`, `family-crisis`, `work`, `ai-tools`, `reference`, `meta`,
  `claude-context`, `digest`, `music-discovery`, `agents`, `ai`, `claude`, `mental-health`,
  `mesh`, `voice`. This list will be refreshed live from the vault each session.
- **Related notes format.** Always use `## Related notes` as the section heading, with each
  link on its own line as `- [[note-title]]`. If a note already has this section, append to it
  rather than replacing it.
- **Never touch system/config notes.** Skip `.obsidian/`, `Attachments/`, `Clippings/`, and
  any non-markdown files. Skip `Tasks.md` and `Daily view.md` as these are operational notes
  that don't benefit from gardening.
- **Ask before writing.** Every proposed change is shown to Joe first. Write only after explicit
  confirmation.

## Step-by-step workflow

### Step 1: Inventory the vault

Run these in parallel at session start:

1. `obsidian:list_all_tags` — get the live tag vocabulary with counts
2. Walk the full vault directory tree using `obsidian:list_directory` recursively across all
   top-level folders: `Archive`, `Areas`, `Inbox`, `Projects`, `Resources`
3. Collect every `.md` file path into a working list

Announce the totals: how many notes found, how many unique tags discovered.

### Step 2: Read frontmatter for all notes

Use `obsidian:get_frontmatter` in batches to check which notes have tags and which don't.
Notes with no `tags` field in frontmatter, or an empty `tags: []`, are tagging candidates.

Also flag notes that have no `## Related notes` section (check via content scan) as linking
candidates. Use `obsidian:read_multiple_notes` in batches of up to 10 for this content check.

Triage the full list into:
- **Needs tagging** — no tags or clearly sparse tags
- **Needs linking** — no `## Related notes` section, or section is empty
- **Needs both**
- **OK** — has tags and has a related notes section (skip unless Joe asks otherwise)

Report the triage counts before proceeding. Ask Joe if he wants to handle tagging first, linking
first, or interleave them (default: tagging first, then linking).

### Step 3: Propose changes, one note at a time

For each candidate note:

1. Read the full note content with `obsidian:read_note`
2. Analyze content and existing frontmatter
3. Propose changes in this format:

---
**Note:** `Projects/Red Door/AI roundtable prep.md`

**Proposed tags:** `work`, `ai-tools`
*(Current tags: none)*

**Proposed related notes:**
- [[Claude build queue]]
- [[Tasks]]

Type **y** to apply, **e** to edit before applying, **s** to skip, or **q** to quit the session.

---

4. Wait for Joe's response before proceeding
5. On **y**: write the changes using `obsidian:manage_tags` for tags and `obsidian:patch_note`
   or `obsidian:write_note` for the related notes section, then move to next note
6. On **e**: show the proposal again and let Joe dictate the corrected version, then apply
7. On **s**: skip and move to next note
8. On **q**: stop, give a session summary, and offer to resume next time

### Step 4: Session summary

When all candidates are processed (or Joe quits), report:
- Notes tagged this session
- Notes linked this session
- Notes skipped
- Notes remaining (if session ended early)

Offer to save a brief "last gardened" note or update an existing vault log if Joe wants a
record.

## Edge cases

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

## Tag application mechanics

Use `obsidian:manage_tags` with `operation: "add"` to add tags. This tool handles frontmatter
correctly without requiring a full note rewrite.

## Related notes section mechanics

To add or append a `## Related notes` section:
1. Read the current note content
2. If no section exists: append the section to the end of the note using `obsidian:patch_note`
   with a unique anchor string near the end, or `obsidian:write_note` with full content
3. If section exists but is empty or sparse: append new links below the existing ones

Always confirm the note content after writing to verify the change landed correctly.
