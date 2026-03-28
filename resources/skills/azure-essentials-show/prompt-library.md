# Prompt library

Five prompt templates for the standard phases of episode production.

---

## Prompt A: Outline phase (starting a new episode)

Use when beginning work on a new episode from source materials and kickoff notes.

```
I'm starting a new Azure Essentials Show episode. I need a comprehensive outline — not a script.

EPISODE INFORMATION
Topic: [Topic name]
Working title: [Working title from kickoff materials]
Host: Thomas Maurer
Guest(s): [SME name(s) and title]
Part of a series? [Yes/No — if yes: series name, episode position, and what prior episodes covered]

SOURCE MATERIALS
Uploaded files:
- [File 1: description]
- [File 2: description]
Additional links:
- [Link: description]

KICKOFF NOTES
[Paste notes from kickoff call or SME emails]
Key emphasis points: [anything to prioritize or avoid]

DEMO SCOPE
[What the demo will cover, or "TBD — SME to define"]

TARGET CTAs
[Specific resources/links if known, or "TBD"]

Please produce a comprehensive outline following the show's standard structure. Include speaker assignments, full talking points, visual aid placeholders, and CTAs where known. Outline only — do not produce a script.
```

---

## Prompt B: Script phase (after SME approval)

Use when the outline has been reviewed and approved.

```
The outline for [Episode Topic] has been reviewed and approved. Ready to develop the bullet-point script.

SME FEEDBACK SUMMARY
[Paste or summarize SME feedback — additions, cuts, clarifications, restructuring]

UPDATED OUTLINE
[Paste revised outline, or: "Outline unchanged — proceeding with original version"]

DEMO DETAILS (if updated)
[Any new information about demo scope or depth]

ADDITIONAL NOTES
[Any clarifications on tone, emphasis, or technical depth]

Please produce a bullet-point script based on the approved outline. Format as natural conversation between Thomas and [Guest Name]. Use bullet points under each speaker (not numbered lists). Follow the standard exchange rhythm: Thomas asks (1–2 bullets) → Guest answers (3–5 bullets) → Thomas bridges. Include all visual aid callouts inline. Target: 6–8 pages for a 5–6 minute episode.
```

---

## Prompt C: Single revision

Use for individual revision requests during the SME review cycle.

```
I have a revision request for the [Episode Topic] [outline/script].

REVISION REQUEST
Section: [Which section]
Type: [Technical accuracy / Emphasis / Language / Structure / Demo scope]
Request: [Describe the change]

Please make this specific change while preserving the rest of the [outline/script] unchanged. If this change affects other sections, flag it before proceeding.
```

---

## Prompt D: Title refinement

Use when the episode title needs work separately from the outline.

```
I need to refine the title for an Azure Essentials Show episode.

Topic: [Brief description]
Working title: [Current working title]
Key viewer benefit: [What viewers will gain]
Part of a series? [Yes/No — if yes, series name]

Please provide 2–3 title options following the show's title rules: 4–6 words, action verb first, customer-focused. For series episodes, use the "Series Name: Specific Episode Focus" pattern.
```

---

## Prompt E: Batch revisions

Use when multiple changes have accumulated and need to be applied together.

```
I have multiple revision requests for the [Episode Topic] [outline/script].

CURRENT VERSION
[Paste the complete current outline or script]

REVISION REQUESTS
1. Section: [which section] | Type: [type] | Request: [description]
2. Section: [which section] | Type: [type] | Request: [description]
[Continue as needed]

Please revise the [outline/script] incorporating all requested changes. Maintain consistent formatting, conversational tone, and technical depth throughout. Note any conflicts between requested changes before proceeding.
```
