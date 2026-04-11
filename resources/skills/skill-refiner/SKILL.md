---
name: skill-refiner
description: >
  Audit and restructure an existing Claude skill from a flat SKILL.md into a properly organized
  folder with separate references, templates, and examples files. Use this skill whenever someone
  wants to improve a skill that has grown too large or complex, says things like "refine this
  skill", "restructure this skill", "this skill is getting too long", "audit this skill",
  "clean up this skill file", "split this skill into files", or "organize this skill properly".
  Also trigger when a skill file is approaching or over 200 lines, contains embedded data tables
  or keyword lists, or mixes workflow instructions with rules and templates. This skill is
  complementary to the skill-creator skill — use skill-creator to build skills from scratch,
  and this skill to improve ones that already exist.
---

# Skill Refiner

Audits an existing skill and restructures it from a flat SKILL.md into a properly organized
folder using the orchestrator pattern: SKILL.md handles only workflow and pointers; rules, data,
templates, and examples live in separate files.

## When restructuring is warranted

A flat SKILL.md is fine for simple skills. Restructure when any of these are true:

- The file is approaching 200+ lines
- You find yourself scrolling past data tables or keyword lists to reach the workflow
- The same content would need updating in multiple places if the workflow changed
- There are embedded templates, examples, or rules that would be useful to read in isolation
- A future editor would have trouble knowing what to change vs. what to leave alone

If the skill doesn't meet any of these criteria, say so and ask the user if they want to
proceed anyway or just make targeted edits instead.

## Content-type taxonomy

Every piece of content in a skill falls into one of these categories:

| Type | Description | Goes in |
|---|---|---|
| **Procedure** | The ordered workflow — what to do, in what sequence | `SKILL.md` (orchestrator) |
| **Rules** | Behavioral constraints — always/never, decision logic | `references/` |
| **Data** | Lists, tables, keyword sets, label tiers, configuration | `references/` |
| **Templates** | Structural skeletons for output documents | `templates/` |
| **Examples** | Completed real outputs that demonstrate correct behavior | `examples/` |
| **Friction points** | Known failure modes and fallbacks | `references/` |
| **Writing guidance** | Style rules, tone constraints, anti-patterns | `templates/` (attached to the template they govern) or `references/` |

## The orchestrator principle

After restructuring, SKILL.md should contain *only* procedure — the step-by-step workflow
with pointers to other files. No rules, no data, no templates, no examples inline. Every
step that requires detailed guidance should say "read [file]" rather than containing that
guidance directly.

A well-structured SKILL.md reads like a table of contents and a checklist combined. Someone
following it should never need to re-read it to understand *what* to do — only to remember
*where* to look.

## Step-by-step workflow

### Step 1: Read the skill

Ask the user to provide the skill — either paste the SKILL.md content directly, or if vault
or filesystem access is available, read it from the path they specify.

Read the full skill from top to bottom before doing anything else.

### Step 2: Run the content audit

Tag each section with its content type from the taxonomy above. Then identify:

- What is pure procedure and belongs in SKILL.md
- What is rules, data, or friction points and belongs in `references/`
- What describes an output format and could become a `templates/` file
- What examples exist in the conversation history or skill itself that could become
  `examples/` files (real outputs only — never fabricate examples)

Present the audit to the user as a table before changing anything:

| Content | Currently in | Proposed location | Rationale |
|---|---|---|---|

Wait for the user to review and confirm the proposed structure. They may want to adjust
where things go — that's expected.

### Step 3: Propose the folder structure

Based on the confirmed audit, show the user the proposed folder layout:

```
skill-name/
├── SKILL.md                    — orchestrator only: workflow + pointers
├── references/
│   └── [topic].md              — one file per concern
├── templates/
│   └── [output-type].md        — skeleton + writing rules for that output
└── examples/
    └── [descriptive-name].md   — real completed output with annotation
```

Name files by concern, not by type. Good names: `filter-criteria.md`, `sources.md`,
`friction-points.md`. Bad names: `rules.md`, `misc.md`, `notes.md`.

Get confirmation before writing any files.

### Step 4: Write the restructured files

Work through the files one at a time, in this order:

1. Reference files first (they contain the extracted content)
2. Template files next
3. Example files (if any)
4. SKILL.md last (the orchestrator, now pointing to everything else)

For each file:
- Show the user what you're about to write
- Write it
- Confirm before moving to the next

### Step 5: Verify the orchestrator

After all files are written, re-read the new SKILL.md and verify:

- It contains only procedure and pointers
- Every pointer resolves to an actual file that was written
- No rules, data tables, or templates remain inline
- The workflow is still complete and followable

If anything is missing or a pointer is broken, fix it before closing out.

### Step 6: Deliver

If working in Claude chat with a filesystem, package the folder and present it for download.
If working in Claude Code, confirm the files are written to the correct location.

Give a brief summary: how many files were created, what was extracted where, and what the
new SKILL.md structure looks like.

## File content guidelines

### References

Each file in `references/` should cover one concern. Don't consolidate unrelated things into
a single file just to reduce file count. Include in each file:
- The actual content (lists, tables, decision rules)
- Any context needed to interpret it correctly
- No procedure — that stays in SKILL.md

### Templates

Templates contain:
- The structural skeleton (headers, placeholders)
- Writing rules specific to that output type (style constraints, anti-patterns)
- Everything a writer needs to fill it in correctly

Writing rules belong *with the template they govern*, not in a separate file.

### Examples

Examples must be real outputs from actual skill runs, not fabricated illustrations. Each
example file should include a brief annotation at the top:
- What this example demonstrates
- Notable decisions made (why something was included or excluded)
- Edge cases it illustrates

Examples are the most valuable documentation a skill can have. A future Claude instance
reading a well-annotated real example understands correct output in a way that abstract
instructions cannot convey.

## Edge cases

- **Skill is already well-structured** — say so. Don't restructure for its own sake.
- **Skill is short and simple** — a 50-line skill probably doesn't need references files.
  Targeted edits may be more appropriate than a full restructure.
- **No examples exist** — skip the `examples/` folder entirely. Don't fabricate examples.
- **User wants to keep it flat** — respect that. The orchestrator pattern is a recommendation,
  not a requirement. Offer targeted improvements instead.
- **Skill is a pre-installed/read-only skill** — note that the restructured version will need
  to be installed as a new skill rather than replacing the original.
