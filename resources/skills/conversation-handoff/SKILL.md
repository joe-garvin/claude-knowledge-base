---
name: conversation-handoff
description: >
  Generate a handoff note summarizing the current conversation for use in a new chat or as a project file. Use this skill whenever the conversation has reached a natural stopping point and work needs to continue in a new session. Trigger phrases include: "generate a handoff note", "summarize for new chat", "create a handoff", "handoff note", "context summary", "summarize this conversation". Also trigger when the user says things like "I want to start a new chat" or "let's continue this in a new session" — any signal that the current session is wrapping up and continuity is needed. Note: works best on task-focused conversations with clear outputs and next steps. For exploratory or strategy conversations, the output will be less structured — expect a looser current-state summary and a "possible directions" section in place of a defined next step.
---

# Conversation handoff

Produce a handoff note as a markdown file that gives a new Claude instance enough context to continue the work without re-litigating decisions already made.

## Instructions

Review the full conversation and extract the operative context — what the next instance needs to act, not a record of how you got there. This is a briefing document, not a transcript or compressed summary of the discussion.

Use this structure:

```
## Project / task
One or two sentences: what this conversation was about and what it was trying to accomplish.

## Current state
What exists, what's been decided, what's been produced. Be specific — reference actual outputs, filenames, decisions, or draft content where relevant.

## Active task or next step
What's in flight or queued. If there are multiple tasks, list them in priority order. For exploratory conversations, replace this section with "## Possible directions" and summarize the options in play.

## Constraints and preferences
Any voice, style, format, or client-specific rules established in this conversation. Only include what was explicitly stated or confirmed here — do not pull from general knowledge or training.

## Open questions or blockers
Anything unresolved that the next session needs to address. Omit this section if none.
```

Target length: 300–500 words. Omit any section that isn't applicable. Do not include background discussion, abandoned approaches, or anything already executed and closed.

## Output

Save the file as `handoff-[brief-slug].md` where the slug is a 2–4 word description of the conversation topic (e.g., `handoff-databricks-blog-draft.md`). Present it to the user as a downloadable file.
