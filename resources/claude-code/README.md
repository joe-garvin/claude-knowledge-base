# Claude Code context bundle — readme

This folder contains context documents for Joe Garvin to use with Claude Code. Drop any or all of these into a Claude Code session as context files.

## Files in this bundle

| File | Contents |
|------|----------|
| `CLAUDE.md` | Core identity, work context, team, clients, writing preferences |
| `CLAUDE-github.md` | knowledge base repo structure, skills library, design system |
| `CLAUDE-obsidian.md` | Obsidian vault structure, key notes, workflow notes |
| `CLAUDE-workflows.md` | Environment, MCP servers, tools, workflow preferences |

## How to use

**Option 1 — Global auto-load (already set up)**
All four context files are copied to `~/.claude/` on this machine. `~/.claude/CLAUDE.md` imports the others automatically, so context loads in every Claude Code session without any extra steps.

**Option 2 — Drop into project root**
Copy the relevant files into your project root. Claude Code reads `CLAUDE.md` automatically from the project root.

**Option 3 — Reference as context files**
Paste contents into the Claude Code context window at session start using the context file interface.

## What Claude Code will know

After reading these files, Claude Code will have context for:
- Who Joe is, his role, his team, his clients
- Active workstreams and recurring meeting rhythms
- The knowledge base repo structure and skills library
- The Obsidian vault structure and key files
- Writing/editing preferences and style rules
- Connected tools and accounts (for reference — not directly accessible from Claude Code without explicit config)
- Workflow preferences (batch ops, file output defaults, etc.)

## What's missing

Claude Code cannot directly access:
- Joe's Obsidian vault (requires Claude Desktop + Obsidian MCP)
- MCP-connected services (M365, Box, monday.com, etc.) unless separately configured
- Files from previous Claude Desktop sessions

For those, continue using Claude Desktop.
