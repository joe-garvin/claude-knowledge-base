---
name: meeting-debrief
description: Analyze a pasted meeting transcript and produce a structured debrief. Use this skill whenever Joe says "debrief this meeting", "analyze this transcript", "run the meeting debrief", "/debrief", or pastes a Teams transcript and asks for a summary, breakdown, or analysis. Also trigger when Joe pastes timestamped speaker turns and asks what happened, what's important, or what he needs to know. Apply to any meeting type — internal recurring meetings, one-off internal meetings, client kickoffs, project check-ins, or any other meeting where a transcript is available.
---

# Meeting Debrief

Analyze a raw Teams transcript (timestamped speaker turns) and produce a structured debrief output in the chat. Output is always the same format — Joe decides what to do with it afterward.

## Input

Joe will paste a raw transcript with timestamped speaker turns. Read the full transcript before producing any output.

## Context awareness

Before generating the debrief, identify:
- **Meeting type** — recurring internal (Creative Sync, Script Scrum, AI Roundtable, 1:1 with Justine, Open Door Sync), one-off internal, or client-facing/project meeting
- **Attendees** — note who was present and their roles (RDC team vs. client contacts)
- **Primary subject** — what workstream(s) or topic(s) drove the meeting

Use this to calibrate depth and relevance filtering throughout the output.

## Output format

Produce the following sections in clean markdown. Use sentence case for all headings. Omit any section that has nothing substantive to report — don't pad with "nothing to note here."

---

### Meeting overview
One short paragraph. Meeting type, date/time if inferable, attendees, and the main thing the meeting was about. Written as a quick orient — not a recap.

### Key discussion points
The substance of the meeting. What was actually talked about, decided, debated, or surfaced. Group by topic if multiple threads were covered. Use bullet points within each topic grouping. Include enough detail that someone who wasn't in the meeting would understand what happened and why it matters.

### Decisions made
Explicit decisions or directions that were locked in during the meeting. If none were made, omit this section.

### Open questions and unresolved items
Things raised but not resolved — questions left hanging, items deferred, things flagged for follow-up without a clear owner or timeline.

### What Joe needs to know
This is the most important section. Focus specifically on Joe's role as Marketing Content Specialist at Red Door Collaborative.

Flag as a bulleted list:
- Action items assigned to Joe (explicitly or implicitly)
- Content direction decisions that affect Joe's current or upcoming work
- Feedback on Joe's work that was discussed
- Deadlines, timelines, or scheduling items that affect Joe's workload
- Strategic or creative decisions Joe needs to be aware of to do his job well
- Anything Joe should follow up on, ask about, or keep an eye on

If the meeting was purely informational with no direct implications for Joe's work, say so plainly in one sentence rather than forcing items into this section.

### Broader context worth noting
Anything from the meeting that's useful company or client context for Joe to have — even if it doesn't require action. This could include: shifts in client priorities, team dynamics, project health signals, things that may affect Joe's work down the road. Keep it concise.

---

## Tone and style guidelines

- Write in clear, direct prose and tight bullets — no filler, no over-explanation
- Sentence case throughout
- Don't editorialize or speculate beyond what the transcript supports
- If something is ambiguous in the transcript, note the ambiguity rather than resolving it
- Vary sentence rhythm; avoid formulaic phrasing
