# When to restructure a skill

A flat SKILL.md is fine for simple skills. Restructuring adds overhead — only worth doing
when the skill genuinely benefits from it.

## Clear signals to restructure

- **File length** — SKILL.md is approaching 200+ lines
- **Scrolling past data** — you scroll past tables or keyword lists to reach the workflow
- **Update risk** — the same content would need changing in multiple places if the workflow evolved
- **Isolated utility** — embedded templates, examples, or rules that would be useful to read
  or update independently
- **Editability** — a future editor would struggle to know what to change vs. leave alone
- **Embedded output formats** — the skill describes what output looks like inline rather than
  pointing to a template

## Signs a flat file is fine

Leave it flat if:
- The skill is a short, linear workflow (under ~100 lines)
- There's no embedded data that changes independently of the procedure
- There are no output templates or examples worth preserving separately
- The whole thing reads clearly top to bottom without restructuring

## The restructuring payoff

After restructuring, each file has a single job:
- **SKILL.md** — procedure only; a reader follows it like a checklist
- **references/** — rules, data, and friction points; readable and updatable independently
- **templates/** — output skeletons + writing rules for that output type
- **examples/** — real completed outputs with annotation; the most valuable documentation
  a skill can have

The main benefit: you can update a label list, a template, or filter rules without ever
touching the procedure. And a future Claude instance reading an annotated example immediately
understands what correct output looks like in a way abstract instructions cannot convey.
