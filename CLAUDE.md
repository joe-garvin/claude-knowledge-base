# CLAUDE.md — Instructions for Claude Code sessions

This file provides persistent context and instructions for Claude when working in this repository. Read it at the start of every session.

## What this repo is

A personal knowledge base for Joe Garvin. It stores outputs, context, and reference material from Claude sessions, organized using a PARA-inspired structure. Files are created during or after working sessions and pushed via the GitHub MCP integration.

## Folder routing

When creating or placing a file, use this logic:

- `projects/` — Active client or work projects with a defined scope (e.g., Microsoft SMB infographic, Databricks content, RDC workflows). One file or subfolder per project.
- `areas/` — Ongoing responsibilities without a defined end date (e.g., dharma group, RDC team AI workflows, personal systems).
- `resources/` — Reusable reference material: frameworks, prompt libraries, research, voice/style guides.
- `archive/` — Completed or inactive projects. Preserve but don't actively update.
- `meta/` — System-level documentation: conventions, changelog, repo instructions. This is one of those files.

When in doubt: if it has a client and a deliverable, it's `projects/`. If it's a recurring responsibility, it's `areas/`. If it's reusable reference material, it's `resources/`.

## File naming conventions

- Lowercase, hyphen-separated: `azure-smb-messaging-framework.md`
- For session notes tied to a specific date, prefix with the date: `2026-03-16-microsoft-smb-ai-infographic-session.md`
- For evergreen documents, omit the date prefix: `red-door-ai-experimentation.md`

## File header conventions

Every file should open with a metadata block identifying when it was created and where it came from. Use this format:

```
**Date:** YYYY-MM-DD
**Source:** [Claude conversation | working session | meeting debrief | etc.]
**Folder:** [projects | areas | resources | archive | meta]
```

## Git and push workflow

- Work on branches prefixed with `claude/` (e.g., `claude/create-claude-md-TpVYs`)
- Commit with clear, descriptive messages
- Push with: `git push -u origin <branch-name>`
- Do NOT push directly to `main`
- Do NOT create a pull request unless explicitly asked

## Changelog

Update `meta/README.md` changelog when making structural changes to the repo (new folders, convention changes, etc.). Routine file additions do not need a changelog entry.

## What not to do

- Don't create duplicate files for the same project — check existing files first
- Don't overwrite an existing file without reading it first
- Don't add files to the root directory — everything goes in a subfolder
- Don't create `README.md` files in new folders unless asked
