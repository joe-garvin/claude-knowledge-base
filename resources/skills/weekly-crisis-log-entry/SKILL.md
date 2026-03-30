---
name: weekly-crisis-log-entry
description: Generate a new weekly entry for the Mart family crisis response log. Use this skill whenever Joe says things like "let's do the log entry", "write up this week's log entry", "add to the crisis response log", "log entry for this week", or provides a batch of family communications (emails, texts, call notes) and asks to document them. Also trigger when Joe pastes family group chat content, email threads, or meeting summaries and says anything about capturing, recording, or logging the week. The output is a formatted entry ready to prepend to the top of Family_coordination_log.md.
---

# Weekly crisis response log entry skill

## Purpose

Generate a new weekly crisis response log entry covering the period from the most recent Friday family meeting through the following Thursday (or Friday morning if needed). The entry is prepended to the top of the family's crisis response log — a shared family document, not a personal journal. Tone and content should reflect that: the log is a record for all family members, not Joe's internal notes.

## Input sources

Joe will provide some combination of the following. Accept whatever subset he brings:

- **Family email thread** — pasted or (if Gmail MCP is connected) fetched by date range
- **Family group chat** — pasted text or uploaded PDF exported from iMessage
- **Individual texts** — pasted directly
- **Call notes** — high-level takeaways from calls Joe had with Mart that were shared with the family (not private notes; only what's family-relevant)
- **Meeting summary** — the separate Friday family meeting summary document, or Joe's notes from it
- **Context from project documents** — the project corpus files are available for background; do not re-summarize them, but use them to correctly characterize significance of new developments

If Gmail MCP is available and connected, offer to fetch the family email thread for the date range before asking Joe to paste it. Ask: "Do you want me to pull the family emails from [date range] via Gmail, or will you paste them in?"

## Entry structure

Every entry follows this structure. Adapt section names to what actually happened that week — not every section appears every week, and new sections can be added for significant new developments.

---

### Header

```
## **[Time span] — [topic summary]**
```

**Time span format:** Use natural language that matches the log's existing style — "Early March 2026", "Week of March 17", "Mid-March 2026", etc. Avoid single dates for weekly entries.

**Topic summary:** 2–4 plain-language descriptors of the week's defining themes, separated by commas. Written for someone scanning the log who already knows the situation and just needs a quick landmark. Example: "Post-discharge return home, AR Intervention next steps"

Propose a title to Joe before finalizing — he may want to adjust it.

---

### Body sections

Use `###` subheadings. Each subhead captures a distinct thread. Common threads include:

- **Mart's condition** — behavioral indicators, sobriety status, psychiatric appointments, social media activity, communications with family
- **[Specific service or resource track]** — AR Intervention, SSDI, foreclosure/housing, conservatorship, AOT — one subhead per active track if there were meaningful developments
- **Family meeting — [date]** — always present; see format below
- **Action items** — always present at end of entry
- **Risk assessment** — include when risk level has changed or warrants documentation

Add or omit subheads based on what actually happened. Don't generate placeholder content for inactive tracks.

---

### Family meeting subhead format

Keep this condensed — it is not a full summary, just a log entry marker. The full meeting summary lives in a separate document.

```
### **Family meeting — [day, date]**

**Participants:** [names]

**Key topics:** [brief list]

**Alignment or notable outcome:** [1–3 bullets on where the family landed or what shifted]
```

---

### Action items format

```
### **Action items**

* [Owner]: [task]
* [Owner]: [task]
* Outstanding: [unresolved items without a clear owner]
```

---

### Risk assessment format

Include when the risk picture has meaningfully changed or when specific elevated risks should be documented for the record.

```
### **Risk assessment**

[2–5 sentences or bullets characterizing current risk level and the key factors driving it. What's elevated, what's the most acute concern, what the family is watching for.]
```

---

## Formatting rules

- **Bullets dominate.** Use short paragraphs only for synthesis or assessment — not for reporting facts or events.
- **No single dates as entry-level headers.** Weekly entries use time-span headers. Daily events within an entry can be labeled with dates inline (e.g., "Dad's call with Mart (Tuesday, March 18):").
- **Direct quotes are acceptable** when they carry specific evidential weight — Mart saying something revealing, a clinician's assessment, a family member's framing of a decision. Keep them brief and purposeful. Do not quote routine conversation.
- **Sentence case** for all headings and subheadings.
- **Bold** for subheading labels, key names, and inline labels (e.g., **Sobriety status:**, **Josh (AR Intervention):**).
- **No line dividers within a weekly entry.** The `---` divider appears only between entries (i.e., after the full entry is complete).
- **Level of detail:** High-level and purposeful throughout. This is a family record, not a transcript. Capture what happened, what it means, and what comes next — not every exchange.
- **Significance framing:** When a development is particularly notable, include a brief interpretive sentence or labeled observation (e.g., "This marks the first time Mart has expressed willingness to consider residential treatment"). Don't editorialize constantly, but do flag genuine turning points.
- **Avoid AI-isms.** No contrastive negation constructions ("it's not X, it's Y"). No em-dash-heavy sentence structures. Write in direct, plain prose that sounds like a careful human record-keeper.

---

## Workflow

1. **Receive inputs** — accept whatever Joe provides; note what's missing if anything material
2. **Propose title** — draft a time span + topic summary header and confirm with Joe before writing the full entry
3. **Draft entry** — generate the full entry in chat (not as a file, unless Joe asks for a .docx)
4. **Joe reviews** — he'll request adjustments inline; iterate until it's right
5. **Placement reminder** — remind Joe that the entry goes at the top of the log, above the previous most-recent entry, followed by a `---` divider

---

## What not to include

- Private or personal observations Joe hasn't shared with the family
- Speculation about family members' internal states beyond what they've expressed
- Content from the project corpus documents that is historical background rather than new this week — the log captures developments, not re-summarizes the situation
- Excessive detail on routine check-ins or calls that didn't produce new information
- Anything that would embarrass a family member if they read the log

---

## Notes on Gmail automation

If the Gmail MCP tool is connected, use it to search for emails in the relevant date range before asking Joe to paste. Suggested search: the family email thread by subject line or participant, filtered to the week being documented. Confirm with Joe what you found before drafting.

If Gmail is not connected, proceed with whatever Joe pastes. Do not block on this.

## Notes on iMessage content

iMessage content is provided manually — either as a pasted excerpt or an uploaded PDF from the macOS Messages print export. Accept either format. If the content is a PDF, read it before drafting. If Joe mentions friction with iMessage capture, note that Cowork desktop automation may be worth exploring as a future workflow for this step.
