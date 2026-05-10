# Claude Code context — workflows, tools, and environment

This document covers Joe's development environment, connected tools, and recurring workflow patterns.

## Environment

- **Primary interface:** Claude Desktop (macOS) with MCP servers active
- **Claude Code:** Used for code-level work on this machine; does NOT share memory or context with Claude Desktop sessions
- **OS:** macOS
- **DAW:** Ableton Live (music production)

## Connected MCP servers (Claude Desktop)

| Service | Notes |
|---------|-------|
| Obsidian | "Still Point" vault; always active in Claude Desktop |
| M365 | Outlook, Teams, SharePoint (RDC tenant) |
| monday.com | reddoorcollaborative.monday.com |
| GitHub | RDC org: reddoorcollaborative; personal: joe-garvin/claude-knowledge-base |
| Box | RDC internal + Portfolio folders |
| Gmail | Personal |
| Google Drive | Personal |

**Note:** These MCP connections exist in Claude Desktop. Claude Code does not have these connections unless explicitly configured.

## GitHub accounts and orgs

| Repo/Org | Purpose |
|----------|---------|
| `joe-garvin/claude-knowledge-base` | Personal knowledge base, skills library, Voice DNA, design system |
| `reddoorcollaborative` (org) | RDC client and team work |

## Skills library

Joe uses a structured skills system — SKILL.md files that define recurring workflows. Skills live in `resources/skills/` in the knowledge base repo and are also mounted at `/mnt/skills/user/` in Claude Desktop.

Skills are not code — they're instruction documents for Claude. When working in Claude Code, reference them directly from the repo if needed.

**High-frequency skills:**
- `meeting-debrief` — `/debrief` trigger; analyzes Teams transcripts
- `music-discovery-digest` — Weekly music digest workflow
- `databricks-blog` — Databricks blog post production
- `azure-essentials-show` — Show script workflow
- `github-push` — Pushes Claude session outputs to the knowledge base repo
- `vault-gardening` — Obsidian vault maintenance
- `task-triage` — Obsidian task inbox processing

## Box file references

Joe's RDC Box account contains:
- RDC brand assets (fonts, logos)
- Suisse Int'l font files (used in RDC design system)
- Portfolio folder with client work

Box folder IDs and font file IDs are documented in the design system files in the knowledge base repo.

## monday.com

Joe's primary project management is through `reddoorcollaborative.monday.com`. Board structure tracks active RDC workstreams. When referencing project status, monday.com is the source of truth for task tracking.

## OpenGov procurement

Joe has run procurement scrapers against `procurement.opengov.com` using the opengov-scraper skill (vendor ID: 377089 for RDC). Results are saved as CSV to outputs.

## Design system

**Published:** GitHub Pages at the `joe-garvin/claude-knowledge-base` repo (`docs/rdc-design-system.html`)
**Source:** `design-system/` folder in the same repo
**Purpose:** RDC brand design system for use with Claude Design generation

## Workflow preferences

- **Batch operations:** Align on approach fully before executing. Joe prefers to review the plan before any bulk writes, pushes, or deletions.
- **Iterative refinement:** Precise accountability at each step. Flag ambiguities before proceeding.
- **File output:** Default to plain markdown or text in chat. Only generate .docx when explicitly requested.
- **Headings:** Sentence case always.
- **No line dividers** in documents or responses.

## Key file paths (Claude Desktop environment)

These paths are relevant in the Claude Desktop/container environment, not in this local Claude Code session:

| Path | Contents |
|------|----------|
| `/mnt/skills/user/` | Joe's user skills library |
| `/mnt/skills/public/` | Shared public skills |
| `/mnt/skills/organization/` | RDC org-level skills |
| `/mnt/user-data/uploads/` | Files uploaded in the current Claude Desktop session |
| `/mnt/user-data/outputs/` | Output files created during Claude Desktop sessions |
