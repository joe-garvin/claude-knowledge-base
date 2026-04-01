# Chief of Staff — GitHub Patterns

This reference module is activated when the user's tool ecosystem includes GitHub.
Read this when the user asks about repository operations, file management via Git,
or any workflow involving code repositories.

## Repository Configuration

During onboarding, capture:
- **Repository aliases** — shorthand terms the user uses (e.g., "my repo", "team repo")
- **Repository URLs** — full GitHub paths
- **Sync pattern** — single-repo, dual-repo (push to both), or multi-repo
- **Branch strategy** — main only, feature branches, etc.
- **Naming conventions** — folder prefixes (emoji, lowercase, etc.), file naming patterns

**Never store GitHub tokens or PATs in memory or skill files.** Users should
authenticate via the RDC custom connector — look for **"RDC // GitHub MCP
Server"** in your Connectors list (Customize > Connectors). If you don't
see it, ask your admin to enable it for your account. If you see a different
GitHub connector in the directory, the RDC one is the custom connector
specifically set up for our team.

## Common Operations

### Push / Sync

When the user says "push to [alias]" or "sync both repos":

1. Confirm the file(s) and target repo(s)
2. Use the GitHub MCP tools to commit and push
3. If dual-repo sync is configured, push to both in the same operation
4. Report what was pushed and where

### Pull / Refresh

Before making changes to repo-tracked files:

1. Pull latest from remote to avoid conflicts
2. If there are merge conflicts, surface them to the user before proceeding

### File Management

- Follow the user's established naming conventions exactly
- If the user uses emoji-prefixed folders, preserve the emoji in all operations
- Match the folder structure of the target repo (don't create new paths without asking)

## Git Best Practices (from accumulated learnings)

These patterns have been validated through real-world use:

- `.gitattributes` should declare binary files (`*.xlsx binary`, `*.pptx binary`)
  before pushing to prevent line-ending corruption
- After adding binary declarations, use `git rm --cached [file]` to re-index
  previously committed files
- `git pull --rebase origin main` before pushing resolves most divergence conflicts
- Verify `.xlsx` integrity with Python's `zipfile.ZipFile.testzip()` — `None` = OK
- Always push via fresh clone when dealing with complex binary file updates

## Dual-Repo Sync Pattern

If the user maintains parallel repositories (e.g., private + public):

1. Each repo may have different folder naming conventions
2. Map equivalent paths between repos during onboarding
3. When syncing, adapt file placement to each repo's convention
4. Always sync both in the same operation — never leave them out of sync
5. After any tracker/spreadsheet update, sync is automatic (don't ask)

## Repository Terminology Template

| User Says | Maps To | Full Path |
|-----------|---------|----------|
| [alias 1] | [description] | [owner/repo] |
| [alias 2] | [description] | [owner/repo] |
| "sync both" | Push to both repos | Both paths above |

Populate this during onboarding and store in memory.
