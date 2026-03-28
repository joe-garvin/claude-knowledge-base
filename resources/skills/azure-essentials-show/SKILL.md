---
name: azure-essentials-show
description: Write outlines and bullet-point scripts for episodes of The Azure Essentials Show, following the show's editorial standards, dialogue conventions, and a strict two-stage workflow. Use this skill whenever the user is working on an Azure Essentials Show episode, mentions a script or outline for the show, references Thomas Maurer or the Azure Essentials Show project, or says things like "new episode" or "let's do the outline" in an Azure context. Trigger even for partial signals — any mention of the show's name or scriptwriting workflow should invoke this skill.
---

# Azure Essentials Show — skill orchestrator

This file contains no rules. It tells you which files to read and when.

---

## On any Azure Essentials Show task

Always read first:
- `show-reference.md` — show format, tone, audience, business purpose
- `workflow-and-gates.md` — the staged process, gate rules, and behavior guardrails

---

## Stage 1: Outline phase (starting a new episode)

Read:
- `episode-structure.md` — standard episode arc and section-by-section guidance
- `title-conventions.md` — title rules; produce title options alongside the outline
- `visual-aids.md` — visual aid callout conventions and demo placeholder rules
- `source-material-handling.md` — how to approach and prioritize source materials
- `length-and-pacing.md` — outline length expectations and section sizing targets

If this is a series episode, also read:
- `series-handling.md` — callbacks, naming patterns, series context

Use **Prompt A** from `prompt-library.md` to structure the kickoff.

Deliver: comprehensive outline + 2–3 title options. Then stop and wait for SME feedback.

---

## Stage 2: Script phase (after SME approval)

Read:
- `style-guide.md` — language rules, constructions to avoid, preferred patterns
- `length-and-pacing.md` — word count and pacing targets per section and per speaker
- `visual-aids.md` — inline placement rules for visual callouts

Consult reference examples for formatting and rhythm:
- `examples/` — see index below

Use **Prompt B** from `prompt-library.md` to structure the script request.

---

## Stage 3: Revisions

Use **Prompt C** (single revision) or **Prompt E** (batch revisions) from `prompt-library.md`.

Read `workflow-and-gates.md` if the scope of the revision is unclear.

---

## Title refinement only

Read `title-conventions.md` and use **Prompt D** from `prompt-library.md`.

---

## Reference examples

Three complete episode packages live in `examples/`. Each contains an intake form, outline, and full script.

| File | Format | Best for studying |
|---|---|---|
| `examples/cloud-accelerate-factory.md` | Service overview, single guest, no series context | Cleanest standalone example; four-step process format; slide-heavy visual aids |
| `examples/azure-cost-estimation-pricing-calculator.md` | Tool demo, series episode 1 | OVERLAY/LOWER THIRD callouts; 3UP staging; demo walkthrough structure |
| `examples/azure-cost-estimation-strategic-guide.md` | Framework episode, series episode 2 | Callbacks to prior episode; electricity bill analogy; multi-tool CTA section |

Study these for: exact outline and script formatting, dialogue rhythm, visual aid integration, how analogies work, and series continuity.
