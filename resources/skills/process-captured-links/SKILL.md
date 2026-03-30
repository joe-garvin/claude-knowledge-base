---
name: process-captured-links
description: Process raw captured links from Joe's Obsidian inbox note into labeled, categorized, described entries filed into the right section of his vault. Use this skill whenever Joe says "process my links", "let's process captured links", "triage my links", "file my saved links", "categorize my links", or any variation indicating he wants to work through the raw links in his Obsidian capture note. Also trigger when Joe mentions his "Captured links" note and wants to do something with it.
---

# Process captured links skill

This skill processes raw URLs from Joe's `Inbox/Captured links.md` Obsidian note. For each link, it fetches the page to get a title and description, presents a proposed entry to Joe for confirmation or override, then moves the processed link to the right destination note in his vault based on PARA category.

## The vault structure

Joe's vault is called "Still point" and uses a PARA-inspired structure:

- `Projects/Red Door/Saved links.md`
- `Projects/Recovery Dharma/Saved links.md`
- `Projects/Red Cedar/Saved links.md`
- `Projects/Mart coordination/Saved links.md`
- `Areas/Dharma practice/Saved links.md`
- `Areas/Books and literature/Saved links.md`
- `Areas/Life in Bellingham/Saved links.md`
- `Areas/Relationship/Saved links.md`
- `Resources/Saved links.md` (catch-all for broadly useful reference material)

If a destination `Saved links.md` note doesn't exist yet, create it before appending.

## Entry format

Each processed link should be stored in this format:

```
- [YYYY-MM-DD] [Title](URL)
  [One or two sentence description of what it is and why it was saved]

```

Always include a blank line after the description — this keeps entries visually separated in Obsidian.

Example:
```
- 2026-03-15 [The Attention Merchants — Nieman Lab](https://niemanlab.org/...)
  Overview of how digital platforms commodify user attention. Saved for relevance to AI roundtable discussion on friction and workflow design.

```

## Processing workflow

### Step 1: Read the capture note

Use the Obsidian tool to read `Inbox/Captured links.md`. Extract all raw unprocessed URLs — these are lines that contain a URL but no title, description, or category metadata yet. Ignore any lines that are already in the processed entry format above.

### Step 2: For each URL, fetch and propose

For each raw URL:

1. Use `web_fetch` to retrieve the page and extract: the page title, a brief description of the content (from meta description, opening paragraph, or your own summary), and any signals about what category it belongs to
2. Propose a complete entry in the format above, including:
   - **Title**: from the page, cleaned up if needed
   - **Description**: one or two sentences — what it is and why Joe likely saved it (infer from content and context)
   - **Destination**: which Saved links note it should go to, with brief reasoning

Present the proposed entry in the conversation like this:

---
**Link 1 of [n]:** `[raw URL]`

**Proposed entry:**
- 2026-03-15 [Title](URL)
  Description here.

**Destination:** Projects/Red Door/Saved links.md
*Reasoning: AI workflow content, relevant to RDC work*

---

Then immediately use the `AskUserQuestion` tool to present action choices as buttons:

```
Question: "What would you like to do with this entry?"
Header: "Action"
Options:
  ✅ Confirm       — "File as proposed to [destination]"
  ✏️ Edit description — "Change the description text"
  ✏️ Change destination — "File it somewhere else in the vault"
  ⏭️ Skip          — "Leave it in the inbox and move on"
```

Wait for Joe's response before moving to the next link. He may also type a free-form response to edit a field inline ("change description to...", "move it to Dharma practice instead") or quit the session ("stop here", "that's enough for now") — if he quits, stop processing and summarize what was done.

### Step 3: Write processed entries

Once Joe confirms an entry:
1. Append it to the correct destination `Saved links.md` note using the Obsidian write tool (append mode)
2. Remove the raw URL line from `Inbox/Captured links.md`
3. Move to the next link

### Step 4: Wrap up

When all links have been processed (or Joe stops the session), give a brief summary:
- How many links processed
- Where they were filed
- How many remain in the inbox (if any were skipped)

## Notes and edge cases

- **Twitter/X links**: These can't be fetched reliably with `web_fetch` since Twitter blocks unauthenticated requests. Instead:
  1. Check whether `mcp__Claude_in_Chrome__navigate` is available in your current tool set
  2. If **yes**: use Claude in Chrome to navigate to the tweet URL and call `get_page_text` to extract the content. This works when Joe is logged into X in Chrome. Process the link inline, same as any other
  3. If **no**: add the link to a deferred list and continue processing the rest. At wrap-up, note how many Twitter links were deferred and suggest re-running the skill in a Cowork session with Claude in Chrome connected
- **Paywalled articles**: Fetch what's available (title, meta description) and note that full content wasn't accessible
- **Dead links**: If a URL returns an error, flag it and ask Joe whether to skip or file it anyway with a manual description
- **Ambiguous category**: If a link could plausibly go in two places, flag both options and let Joe decide
- **YouTube videos**: Use the page title and any available description; note it's a video in the description
- Process links one at a time — never batch-confirm multiple links without Joe reviewing each one
