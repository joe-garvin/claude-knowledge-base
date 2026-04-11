# Constraints

Behavioral rules and data that govern every vault gardening session.

## Rules

- **Never invent new tags.** Only use tags that already exist in the vault, discovered by
  `obsidian:list_all_tags` at the start of each session.
- **Related notes format.** Always use `## Related notes` as the section heading, with each
  link on its own line as `- [[note-title]]`. If a note already has this section, append to it
  rather than replacing it.
- **Never touch system/config notes.** Skip `.obsidian/`, `Attachments/`, `Clippings/`, and
  any non-markdown files. Skip `Tasks.md` and `Daily view.md` as these are operational notes
  that don't benefit from gardening.
- **Ask before writing.** Every proposed change is shown to Joe first. Write only after explicit
  confirmation.

## Tag vocabulary filter

The vault has a long tail of one-off tags (count = 1) that are noise. Prefer tags with
count ≥ 2 unless a one-off tag is an exceptionally precise fit.

Core vocabulary as of initial skill creation:
`personal`, `dharma`, `family-crisis`, `work`, `ai-tools`, `reference`, `meta`,
`claude-context`, `digest`, `music-discovery`, `agents`, `ai`, `claude`, `mental-health`,
`mesh`, `voice`

This list is a starting point only — always refresh from `obsidian:list_all_tags` at session
start and use the live vocabulary.
