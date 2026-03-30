---
name: github-push
description: Push a summary or key outputs from the current conversation to Joe's GitHub knowledge base repo (joe-garvin/claude-knowledge-base). Use this skill whenever Joe says things like "push this to my repo", "save this to GitHub", "push this to my knowledge base", "save this conversation", "archive this to GitHub", or any variation indicating he wants to preserve the current conversation or its outputs. Also trigger if Joe asks to "back this up" or "add this to my knowledge base". Always use this skill rather than attempting a raw GitHub push without it.
---

# GitHub Push — Claude Knowledge Base

This skill saves a summary of the current conversation (and any key outputs) to Joe's GitHub knowledge base at `joe-garvin/claude-knowledge-base`.

## Repo structure

The repo uses a PARA-inspired folder structure. Place files in the most appropriate folder:

- `projects/` — Active work with a defined outcome (client deliverables, RDC workflows, specific builds)
- `areas/` — Ongoing responsibilities without a fixed end (dharma practice, personal systems, team operations)
- `resources/` — Reference material, research, how-tos, tool notes, coffee guides, etc.
- `archive/` — Completed or inactive things worth keeping

## Step-by-step instructions

### 1. Decide where the file goes
Read the conversation and pick the best PARA folder. When in doubt:
- Client work or a specific deliverable → `projects/`
- Recurring practice or responsibility → `areas/`
- Reference, research, or tool knowledge → `resources/`
- Something finished or no longer active → `archive/`

### 2. Generate a descriptive filename
- Lowercase, words separated by hyphens
- Include the date in `YYYY-MM-DD` format at the start
- Be specific enough that the filename is meaningful on its own later
- Format: `YYYY-MM-DD-descriptive-title.md`
- Examples:
  - `2026-03-15-azure-smb-infographic-brief.md`
  - `2026-03-15-obsidian-mobile-capture-workflow.md`
  - `2026-03-15-baratza-virtuoso-grind-settings.md`

### 3. Write the file content

Open with a standard header block:

```
# [Descriptive Title]

**Date:** YYYY-MM-DD
**Source:** Claude conversation
**Folder:** [projects / areas / resources / archive]
```

Then include:

**Summary** (always): 2–4 sentences capturing what this conversation was about and what was accomplished or decided.

**Key outputs** (when relevant): Include artifacts, files created, decisions made, prompts developed, reference info, or anything else with lasting value. Use judgment — not every conversation has outputs worth preserving beyond the summary.

**Next steps or open threads** (optional): If there were clear follow-ups or unresolved questions, note them briefly.

### 4. Push to GitHub

Use the GitHub tool to create or update the file at the correct path:
- Owner: `joe-garvin`
- Repo: `claude-knowledge-base`
- Branch: `main`
- Path: `[folder]/[filename].md`

### 5. Confirm
Tell Joe the file was saved, including the folder and filename so he knows where to find it.

---

## Notes

- If Joe specifies what he wants captured ("just save the prompt" or "summarize this whole thing"), follow his direction rather than using defaults.
- If Joe doesn't specify, default to: summary + any significant outputs or reference material.
- Keep the file readable and useful as a standalone document — someone (Joe) should be able to open it six months from now and understand what it contains without any other context.
