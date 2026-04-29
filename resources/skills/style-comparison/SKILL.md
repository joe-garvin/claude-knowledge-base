---
name: style-comparison
description: Compare a Claude-generated first draft against a finished working draft to extract personal writing principles. Use this skill whenever Joe says "compare drafts", "run the style comparison", "extract principles from this", "log this revision", or provides a first draft and finished draft and asks what changed. Also trigger when Joe says things like "I revised this — can you extract principles from what I changed?" or any variation indicating he wants to learn from the diff between a generated draft and his manual revision. This skill scrapes the originating conversation for in-session edit requests, compares both drafts, extracts principles from both signals, appends a dated entry to the style principles log in GitHub, and rebuilds the synthesized principles file.
---

# Style comparison — writing principles extractor

Compares a Claude-generated first draft against a finished working draft to extract personal writing style principles. Logs findings to `resources/voice-dna/style-principles-log.md` and rebuilds `resources/voice-dna/style-principles-synthesized.md` in Joe's GitHub knowledge base (`joe-garvin/claude-knowledge-base`).

## Inputs

Joe provides:
1. **First draft** — the Claude-generated version, pasted into chat
2. **Finished working draft** — Joe's final manually-revised version, pasted into chat

Claude retrieves:
3. **In-session edit requests** — scraped from the originating conversation via past-chats search

## Step-by-step workflow

### Step 1 — Infer context and confirm

Before doing anything else, read both drafts and infer:
- **Project type** — what kind of writing is this? (personal email, client blog post, eulogy, newsletter, etc.)
- **Register** — what's the tone and formality level?
- **Audience** — who is this for, and what's the relationship?

State your inferences briefly and ask Joe to confirm or correct before proceeding. Example:

> "This looks like a personal email to Joe's Zen teacher — conversational, warm, deferential. Does that match how you'd describe it?"

Don't proceed until confirmed.

### Step 2 — Scrape in-session edit requests

Search past conversations to find the session where the first draft was generated. Look for:
- Explicit revision requests ("can you make X more...", "cut this", "add more detail about...")
- Feedback on specific passages ("this feels too formal", "this sounds off")
- Directional corrections mid-conversation

Use `conversation_search` with keywords drawn from the first draft content — specific phrases, names, or subject matter. If the session isn't findable (too recent to be indexed, or ambiguous), note that and proceed with the two drafts only.

Distill the in-session edit requests into a clean bulleted list. Don't transcribe verbatim — extract the signal (what was being corrected and why).

### Step 3 — Compare drafts

Diff the first draft against the finished working draft. For each meaningful change, note:
- What changed
- What it suggests about Joe's writing instincts or preferences

Group changes into categories as they emerge (specificity, voice, register, structure, closings, etc.). Don't force categories — let the diff dictate them.

### Step 4 — Extract principles

Synthesize both signals into a set of writing principles:

- **From in-session edits:** What did Claude get wrong early enough that Joe caught it in conversation?
- **From the manual diff:** What survived Claude's revisions but still needed Joe's hand?
- **Cross-cutting:** Any observation that spans both signals?

Label each principle by source: `[in-session]`, `[manual]`, or `[both]`.

Write principles as actionable directives, not observations. Bad: "Joe added more detail." Good: "Restore concrete specifics — numbers, names, sensory details — before polishing rhythm. These are load-bearing, not decorative."

Aim for 4–8 principles per session. Don't manufacture principles if the diff is small.

### Step 5 — Append to log

Read the current `resources/voice-dna/style-principles-log.md` from GitHub. Append a new dated entry at the bottom using this format:

```
## YYYY-MM-DD — [Project type and brief description]

**Context:** [Register, audience, relationship — one sentence]

**In-session edits (from conversation scrape):**
- [distilled edit request]
- [distilled edit request]

(If conversation not found: "Conversation not retrievable — in-session edits omitted.")

**Principles extracted:**

- [source tag] **[Short principle title].** [1–2 sentence explanation with specific example from this session's drafts.]
```

Push the updated file to GitHub.

### Step 6 — Rebuild synthesized file

Read the full log. Rebuild `resources/voice-dna/style-principles-synthesized.md` from scratch, incorporating all sessions:

- Consolidate duplicate or overlapping principles across sessions into single entries
- Note when a principle has appeared across multiple sessions (it's more reliable)
- Group by category (specificity, voice, register, closings, etc.)
- Update the "Last updated" and "Sessions included" header

Push the rebuilt file to GitHub.

### Step 7 — Confirm

Tell Joe:
- How many principles were extracted this session
- Whether the conversation scrape succeeded or not
- That both files were updated, with file paths

Keep it brief.

## File locations

- Log: `resources/voice-dna/style-principles-log.md`
- Synthesized: `resources/voice-dna/style-principles-synthesized.md`
- Repo: `joe-garvin/claude-knowledge-base`, branch `main`

## Notes

- If Joe provides a label or description for the context upfront, use it and skip the confirmation step.
- If the diff between drafts is very small (minor wording tweaks only), say so and ask if he still wants a log entry or wants to wait for a more substantive revision.
- Principles should sound like something Joe would say to a future version of Claude before a drafting session — concrete, direct, specific to his instincts.
