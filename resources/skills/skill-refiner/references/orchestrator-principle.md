# The orchestrator principle

After restructuring, SKILL.md should contain *only* procedure — the step-by-step workflow
with pointers to other files. No rules, no data, no templates, no examples inline.

## What a good orchestrator reads like

A well-structured SKILL.md reads like a table of contents and a checklist combined. Someone
following it should never need to re-read it to understand *what* to do — only to remember
*where to look* for the details of how.

**Before** — flat SKILL.md with everything inline:

```
## Step 2: Filter each release

Check release dates. If a release is more than 3 months old, exclude it.
Does the label appear in the core label list? Core labels: Perlon, Ilian Tape,
DDS, Comatonse, Wild Oats, Apron, Mood Hut, Tartelet, Workshop...
Flag anything described as "peak-time," "banging," "anthemic"...
```

**After** — orchestrator SKILL.md with pointer:

```
## Step 2: Filter each release

Apply the three-check filter described in `references/filter-criteria.md`.
```

And `references/filter-criteria.md` contains the label lists, keyword tables, and decision
logic — readable on its own, updatable without touching the procedure.

## The test

After restructuring, read the new SKILL.md and ask:

1. Does every step tell you *what* to do without requiring you to absorb *how* inline?
2. Could you update the label list without touching the procedure?
3. Could you swap out a template without changing the workflow?
4. Would a future Claude instance reading only SKILL.md know where to find everything?

If the answer to all four is yes, the orchestrator is clean.

## Common violations to watch for

- A step that says "check the following criteria: [long inline list]" — the list belongs in
  a reference file
- A step that says "output should look like this: [inline template]" — the template belongs
  in `templates/`
- A section labeled "edge cases" or "notes" at the bottom of SKILL.md — these are friction
  points or rules and belong in `references/`
- Writing guidance embedded in a workflow step — belongs with the template or in `references/`
