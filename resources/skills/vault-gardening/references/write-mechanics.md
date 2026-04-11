# Write mechanics

How to apply tags and related notes sections using Obsidian tools.

## Tag application

Use `obsidian:manage_tags` with `operation: "add"` to add tags. This tool handles frontmatter
correctly without requiring a full note rewrite.

## Related notes section

To add or append a `## Related notes` section:

1. Read the current note content
2. If no section exists: append the section to the end of the note using `obsidian:patch_note`
   with a unique anchor string near the end, or `obsidian:write_note` with full content
3. If section exists but is empty or sparse: append new links below the existing ones

Always confirm the note content after writing to verify the change landed correctly.
