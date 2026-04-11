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

Before starting, read `references/constraints.md` — all rules and the tag vocabulary filter
apply for the full session.

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
3. Propose changes using the format in `templates/proposal-format.md`
4. Wait for Joe's response before proceeding
5. On **y**: apply changes per `references/write-mechanics.md`, then move to next note
6. On **e**: show the proposal again and let Joe dictate the corrected version, then apply
7. On **s**: skip and move to next note
8. On **q**: stop, give a session summary, and offer to resume next time

See `references/friction-points.md` for edge cases.

### Step 4: Session summary

When all candidates are processed (or Joe quits), report:
- Notes tagged this session
- Notes linked this session
- Notes skipped
- Notes remaining (if session ended early)

Offer to save a brief "last gardened" note or update an existing vault log if Joe wants a
record.
