# RDC AI discovery skill — build conversation

**Date:** 2026-03-17
**Source:** Claude conversation
**Folder:** projects

## Summary

Full design and build session for a new Claude skill called `rdc-ai-discovery` — a structured, low-friction AI workflow discovery interviewer for Red Door Collaborative team members. The session moved through concept development, thought partnership on goals and deliverables, connector-based research (Monday.com Active Projects, Creative Roster, AI Automations board), and complete skill authoring. The skill and all reference files were pushed to the repo at `projects/2026-03-16-rdc-ai-discovery-skill/`.

## Key decisions made

**Concept and goals**
- The skill is an interviewer persona that takes the cognitive burden off the interviewee by asking structured questions rather than asking them to self-diagnose AI opportunities
- Target audience: non-technical RDC colleagues with mixed feelings about AI and low confidence using it
- Trigger: slash command (`/discover` or `/ai-discovery`) or natural-language phrases like "how can AI help me" or "I don't know where to start with AI"
- The `ask_user_input` tool (button-based multiple choice) should be used throughout to minimize typing burden

**Output format**
- Tiered personal recommendation — not a report, not something to present to leadership, just a gift for the individual
- Structure: 2–3 sentence summary of what Claude heard → headline recommendation (highest-value, most immediately actionable) → 2–3 secondary opportunities
- Each recommendation includes a concrete first step: an actual prompt the person could paste into Claude right now
- The framework table from Joe's notes (friction → ideal → realistic → solution) informs the interview logic invisibly but does not appear in the output
- Execution is explicitly out of scope for this skill — it surfaces and hands off, it doesn't build

**Role branching**
- Opening question identifies role; Claude then reads the appropriate reference file silently and tailors subsequent questions
- Seven role options: writer/content, visual designer, motion graphics/animator, video editor, project manager/account manager, embedded consultant, ops/HR/leadership
- Embedded consultants (Mindy Bomonti, Sallie St. Laurent) route to the PM reference file, which opens with a dedicated note reorienting for a Microsoft enterprise context

**Connector research findings (Monday.com)**
- Active Projects board surfaced the full deliverable taxonomy: blogs, glossary pages, L200/battlecard/executive decks, customer stories, newsletters, videos, social cards, infographics, ebooks, courses, flyers, graphic design assets
- Creative Roster confirmed role taxonomy: visual design, motion graphics, video editor, writer/editor, storyboard/animation, production/QC, web dev
- AI Automations board captured existing org-level AI opportunities — intentionally not pre-filtered from skill output; the skill should surface these organically through the interview

**Team roster corrections applied**
- Added: Nina Stackhouse (Visual Designer), Karin Hokanson (Creative PM, started 2026-03-17), Mindy Bomonti and Sallie St. Laurent (embedded consultants at Microsoft)
- Corrected: Amy Metzler is Client Success & Strategy (Sr. Account Manager, Azure), not Creative Team
- Jeffrey Griffith confirmed as Motion Graphics & Video Editor

## Skill structure

```
rdc-ai-discovery/
├── SKILL.md
└── references/
    ├── writers.md
    ├── designers.md
    ├── animators.md
    ├── video-editors.md
    ├── project-managers.md   ← also handles embedded consultants
    └── ops-leadership.md
```

Skill files: `projects/2026-03-16-rdc-ai-discovery-skill/`

## Next steps / open threads

- Skill needs to be installed in the shared RDC Claude skill directory (Brian to action)
- No formal evals run yet — qualitative review and real-world testing with a colleague would be the natural next step
- The skill explicitly does not recommend building skills or complex setups — it recommends things people can do in Claude today. That boundary should be preserved in any future iterations.
- Consider a follow-up session after first few real interviews to tune question branches based on what actually surfaces
