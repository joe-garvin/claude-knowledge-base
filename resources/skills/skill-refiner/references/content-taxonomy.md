# Content taxonomy

Every piece of content in a skill falls into one of these types. The type determines where
it lives after restructuring.

## Type definitions and destinations

| Type | Description | Goes in |
|---|---|---|
| **Procedure** | The ordered workflow — what to do, in what sequence | `SKILL.md` (orchestrator only) |
| **Rules** | Behavioral constraints — always/never, decision logic | `references/` |
| **Data** | Lists, tables, keyword sets, label tiers, configuration values | `references/` |
| **Templates** | Structural skeletons for output documents | `templates/` |
| **Examples** | Completed real outputs that demonstrate correct behavior | `examples/` |
| **Friction points** | Known failure modes and fallbacks | `references/` |
| **Writing guidance** | Style rules, tone constraints, anti-patterns | `templates/` (with the template they govern) or `references/` |

## Naming conventions

### references/
Name files after the concern they cover, not generic labels.

Good: `filter-criteria.md`, `sources.md`, `friction-points.md`, `tag-vocabulary.md`
Bad: `rules.md`, `misc.md`, `notes.md`, `reference.md`

One file per concern. Don't consolidate unrelated things just to reduce file count.

### templates/
Name files after the output type they produce.

Good: `digest-entry.md`, `weekly-note.md`, `episode-outline.md`
Bad: `template.md`, `output.md`

Writing rules belong *with the template* rather than in a separate file — the person filling
in the template is the one who needs them.

### examples/
Name files descriptively so a future reader knows what the example demonstrates without
opening it.

Good: `dense-electronic-release-short-entry.md`, `ambient-album-with-caveats.md`
Bad: `example1.md`, `sample.md`

## What always stays in SKILL.md

- The frontmatter (name, description)
- A one-sentence summary of what the skill does
- The step-by-step workflow, each step pointing to relevant files
- Pointers to where edge cases are documented

If you find yourself writing a rule, a list, a table, or a template inline in SKILL.md,
stop and ask whether it belongs in a reference file instead.

## Tagging cheat sheet for the audit step

- "Always do X" / "Never do Y" → **Rules** → `references/`
- A list of items (labels, tags, sources, keywords) → **Data** → `references/`
- "Here's what the output should look like" + structure → **Template** → `templates/`
- "Here's a real example of a completed output" → **Example** → `examples/`
- "If X fails, do Y instead" → **Friction point** → `references/`
- "Write in this tone / avoid these phrases" → **Writing guidance** → with template or `references/`
- "Do step 1, then step 2, then step 3" → **Procedure** → stays in `SKILL.md`
