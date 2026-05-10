# Claude Code context — Obsidian vault

This document describes Joe's Obsidian vault and how to work with it.

## Vault

**Name:** Still Point
**Sync:** Obsidian Sync (not iCloud)
**Access from Claude Desktop:** Via Obsidian MCP server (always active in Claude Desktop)
**Mobile access:** GitHub mirror via obsidian-git (most practical path for mobile read access)

The vault is NOT accessible via Claude web or mobile interfaces — only Claude Desktop with the MCP server active.

## Folder structure (PARA)

```
Still Point/
├── Projects/          # Active projects with clear outcomes
├── Areas/             # Ongoing responsibilities without end dates
├── Resources/         # Reference material, organized by topic
│   ├── Music Discovery/
│   │   └── [year]-W[week] — weekly digest.md    # Music digest notes
│   ├── Voice DNA - personal register.md          # Writing voice reference
│   ├── Will/                                      # Estate planning documents
│   └── [other reference folders]
├── Archive/           # Completed or inactive items
└── [root-level notes] # tasks.md, inbox, etc.
```

## Key notes and files

| Path | Purpose |
|------|--------|
| `tasks.md` | Main task list; inbox section is triaged with the task-triage skill |
| `Resources/Voice DNA - personal register.md` | Joe's writing voice DNA — reference for any writing that should sound like Joe |
| `Resources/Music Discovery/` | Weekly music digest notes written by music-discovery-digest skill |
| `Resources/Will/` | Estate planning documents (personal/sensitive) |
| `Family_coordination_log.md` | Crisis response log (family coordination related to Mart's illness/passing) |

## Tagging taxonomy

Joe has an established tagging taxonomy. When writing notes or gardening the vault, follow existing tag patterns — don't introduce new top-level tags without checking what exists.

## Wikilinks

Notes use wikilinks (`[[note name]]`) for inter-note linking. The vault-gardening skill audits for missing or incomplete links and tags.

## Music discovery digests

**Location:** `Resources/Music Discovery/[year]-W[week] — weekly digest.md`
**Source:** Boomkat email newsletter (primary), Resident Advisor, Pitchfork
**Written by:** music-discovery-digest skill (run from Claude Desktop)

## Voice DNA

**File:** `Resources/Voice DNA - personal register.md`
**Mirror:** `voice-dna/personal-register.md` in joe-garvin/claude-knowledge-base repo

Contains Joe's personal writing register — tone, vocabulary, sentence rhythm, patterns to avoid. Reference when generating any writing that should sound like Joe.

## Workflow notes

- Vault is only accessible via Claude Desktop + Obsidian MCP
- Writes to the vault happen through MCP tool calls, not direct file access
- The vault-gardening skill is the tool for periodic maintenance (tags, links)
- task-triage skill processes the inbox section of tasks.md
- process-captured-links skill handles raw captured links in the inbox note

## Mac Mini (headless node)

Joe runs a Late 2014 Mac Mini (A1347, Intel i5, 8GB, Monterey 12.7.6) as a headless node for Plex and planned Claude agentic workflows that feed into Obsidian via Obsidian Sync.
