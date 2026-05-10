# Claude Code context — knowledge base repo

This document describes Joe's personal GitHub knowledge base repo and its structure.

## Repo

**Repo:** `joe-garvin/claude-knowledge-base`
**Purpose:** Personal knowledge base and skills library, structured as a PARA-based folder system. Backed up and synced from Claude Desktop sessions.

## Folder structure (PARA)

```
joe-garvin/claude-knowledge-base/
├── resources/
│   ├── claude-code/             # Claude Code context bundle (CLAUDE.md + supporting files)
│   └── skills/                  # All Claude skill files (SKILL.md + supporting files)
│       ├── meeting-debrief/
│       ├── music-discovery-digest/
│       ├── prompt-optimizer/
│       ├── vault-gardening/
│       ├── style-comparison/
│       ├── databricks-blog/
│       ├── azure-essentials-show/
│       ├── conversation-handoff/
│       ├── github-push/
│       ├── task-triage/
│       ├── process-captured-links/
│       ├── client-writing-outline/
│       ├── avoid-ai-writing/
│       └── skill-refiner/
├── voice-dna/
│   └── personal-register.md     # Joe's writing voice reference doc
├── docs/
│   └── rdc-design-system.html   # RDC design system published via GitHub Pages
└── design-system/               # RDC design system source files
    ├── SKILL.md
    ├── DESIGN.md
    └── [CSS token architecture + font references]
```

## Skills library

Each skill lives in `resources/skills/<skill-name>/` and contains at minimum a `SKILL.md`. Some skills have additional supporting files (references, templates, examples).

**Key skills:**
- `meeting-debrief` — Analyzes raw Teams transcripts; triggered by `/debrief`
- `music-discovery-digest` — Weekly music digest from Boomkat + RA + Pitchfork; writes to Obsidian vault
- `databricks-blog` — Multi-stage workflow for Databricks blog posts
- `azure-essentials-show` — Script outlines + bullet-point scripts for the show
- `vault-gardening` — Obsidian vault maintenance (tags, links)
- `style-comparison` — Compares Claude draft vs. Joe's revised draft to extract style principles
- `prompt-optimizer` — Compresses brain-dump prompts into concise actionable prompts
- `avoid-ai-writing` — Audits and rewrites content to remove AI-isms
- `github-push` — Pushes conversation outputs to this repo
- `task-triage` — Processes inbox tasks from Obsidian tasks.md
- `conversation-handoff` — Generates a handoff note for continuing work in a new session

## Voice DNA

**File:** `voice-dna/personal-register.md`

Joe's personal writing voice reference, used to calibrate tone and style in drafts. Reference this whenever generating writing that should sound like Joe, or when doing style-comparison work.

## Design system

**Published URL:** GitHub Pages at `docs/rdc-design-system.html`

The `design-system/` folder contains:
- CSS token architecture
- Font references (Suisse Int'l, sourced via Box)
- A `SKILL.md` for Claude Design generation
- `DESIGN.md` — full RDC design system documentation

## Workflow notes

- Joe audited and synced 14 personal skills between Claude and this repo
- Skills are the authoritative source for recurring workflow behavior in Claude Desktop
- When pushing new content, use the `github-push` skill workflow or the RDC GitHub MCP connector
- Joe uses the `reddoorcollaborative` GitHub org separately for RDC client/team work
