---
name: task-triage
description: "Triage tasks from the inbox section of Joe's tasks.md Obsidian note. Use this skill whenever Joe says \"triage my inbox\", \"let's triage\", \"sort my inbox tasks\", \"process the inbox\", or any variation indicating he wants to sort and prioritize captured tasks. Also trigger if Joe opens tasks.md and asks what to do with the inbox items, or asks Claude to help him process or organize his task inbox."
---

# Task triage skill

This skill triages tasks from the inbox section of Joe's tasks.md Obsidian note. The goal is to move items out of the inbox and into the right section of the file with an appropriate priority flag — with Joe's approval before any changes are made.

## The vault and file

Joe's task list lives at `tasks.md` in his Obsidian vault. The inbox is the `## 📥 Inbox` section at the top of the file.

## Triage workflow

### Step 1: Read the file

Use the Obsidian tool to read `tasks.md`. Extract all unchecked items from the `## 📥 Inbox` section. Ignore any checked (`[x]`) items.

### Step 2: Prepare a batch proposal

For each unchecked inbox item, produce:

1. **Refined task** — a cleaned-up version of the original, following these rules:
   - Start with a verb
   - Remove inline context, rationale, or parenthetical notes that belong in a note body — extract only the core action
   - Expand vague shorthand where intent is clear
   - If the intent is genuinely ambiguous, do not guess — flag it with a note like "(unclear — did you mean X or Y?)"
   - The rewrite should be intent-preserving; do not change what the task is, only how it's expressed
   - If the rewrite is minimal or identical to the original, just show the refined version with no annotation
   - If something meaningfully changed, show the original below the refined version in italics: *was: "[original text]"*

2. **Category** — which section of tasks.md it belongs in. The current sections are:
   - 🏠 Personal → Immediate, Home, Errands & purchases, Health & fitness, Someday / low priority
   - 💼 Red Door → Active projects & tasks, AI workflows & skills, Claude Cowork, Misc
   - 🌿 Red Cedar / Recovery Dharma → Active, Misc
   - 🌀 Ideas & future projects → Claude / AI projects, Personal projects, Trips & experiences

3. **Priority flag** — one of:
   - ⏫ high priority
   - 🔼 medium priority
   - No flag (low priority / someday)

Use judgment based on the item's content, time-sensitivity, and which section of Joe's life it belongs to. When genuinely unsure about a category or priority, say so — flag it with a note like "(not sure — could also go under X)" so Joe can weigh in.

### Step 3: Present the proposal

Present all items as a clean table with three columns: refined task, proposed category, proposed priority. Where the original wording meaningfully differed, show it in italics below the refined task in the same cell.

Example format:

| Refined task | Proposed category | Priority |
|---|---|---|
| Schedule dentist appointment | 🏠 Personal → Immediate | 🔼 medium |
| Research Whisper transcription options | 💼 Red Door → AI workflows & skills | no flag |
| Draft outline for next AES episode *was: "AES script stuff"* | 💼 Red Door → Active projects & tasks | 🔼 medium |
| (unclear — did you mean review the slide deck or update it?) | 💼 Red Door → Active projects & tasks | ⏫ high |

End with: "Does this look right? Let me know any changes before I move them."

### Step 4: Wait for input

Do not make any changes to tasks.md until Joe confirms or redirects. He may:
- Approve the whole batch ("looks good")
- Adjust individual items ("move that one to Someday instead")
- Change a priority ("make that one high")
- Clarify an ambiguous item

Incorporate any feedback, confirm the final version if changes were significant, then proceed to step 5.

### Step 5: Make the changes

For each item:
1. Remove it from the inbox section in tasks.md
2. Add the **refined task text** (not the original) to the correct section with the agreed priority flag

Use `obsidian:patch_note` for each move. Work carefully — do not disturb surrounding items or formatting.

Once all items are moved, confirm to Joe: "Done — X items triaged. Your inbox is clear."

## Notes

- Never move or modify checked (`[x]`) items in the inbox — leave them in place
- If the inbox is empty (no unchecked items), say so and stop
- Do not invent new sections or subsections — place items into existing ones only; if nothing fits well, default to the relevant section's Misc or Someday / low priority
- Always file the refined task text, never the raw original
