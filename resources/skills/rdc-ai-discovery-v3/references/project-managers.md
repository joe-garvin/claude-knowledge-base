# Project managers and account managers — interview guide

Note: if the person identified as an embedded consultant, use this same file but apply the embedded consultant framing from `references/rdc-context.md`.

---

## Role context

PMs and AMs at RDC (currently Naj/Najwa, Silas, Karin, and Amy Metzler) sit at the intersection of client communication and internal coordination. They receive briefs and direction from clients, translate that into actionable work for the creative team, track project status across multiple active deliverables, manage review rounds and feedback, and handle a high volume of back-and-forth communication in both directions.

Common work patterns:
- Receiving a client brief or email and turning it into internal direction for the creative team
- Writing up status updates, answering client questions, and relaying feedback
- Tracking multiple active projects simultaneously, each at different stages
- Building project documents from past examples (kickoff decks, workback schedules, SOWs, creative briefs)
- Coordinating review rounds and chasing approvals
- Writing notes that capture what was decided in a meeting or call

This role involves significant document generation that follows predictable templates — the content changes project to project, but the structure is largely the same every time.

## Likely friction areas to probe

- **Document generation from templates**: Creating kickoff decks, workback schedules, creative briefs, status updates, and SOWs from scratch each time even though the structure is almost always the same
- **Brief-to-internal-direction translation**: Turning a client email or call into a clear brief for the creative team
- **Status update writing**: Composing regular status updates and client-facing summaries fast
- **Meeting notes**: Turning a transcript or rough notes into a clean summary with action items
- **Client communication drafting**: Writing clear, appropriately toned responses to client questions
- **Onboarding new projects**: Getting up to speed on a new project quickly

## Question sequence

**Q3 — Volume and mix** (buttons):
> "On a typical week, where does most of your time go?"

Options: Client communication (email, Teams, calls) / Building and maintaining project documents / Coordinating between clients and the creative team / Tracking project status and chasing things / Something else

**Q4 — Document generation** (buttons):
> "When you need to build a project document — a kickoff deck, brief, workback schedule — how do you usually start?"

Options: I find a past example and adapt it / I start from a blank template / I build it from scratch each time / It depends on the document type

**Q5 — Where time gets lost** (buttons):
> "What kind of writing or document task takes longer than it should?"

Options: Writing status updates or client summaries / Turning meeting notes into something structured / Drafting responses to tricky client questions / Building kickoff or scoping documents from a brief / Something else

**Q6 — Drill-down** (buttons, branch on Q5 answer):

If "status updates or client summaries":
> "What makes status updates take longer than you'd like?"
Options: Finding the right tone — professional but not stiff / Figuring out what level of detail the client actually wants / Gathering all the relevant info before I can write anything / Writing basically the same update slightly differently every time / Something else

If "meeting notes":
> "What's the hardest part of turning a meeting into a useful summary?"
Options: Capturing everything accurately in the moment / Organizing what was discussed into a clear structure after / Pulling out the actual action items from a long conversation / Getting it done while it's still fresh — it always falls to the end of the day / Something else

If "tricky client questions":
> "When a client asks something complicated, what's the hardest part of responding?"
Options: Figuring out the right level of detail / Finding the right tone so it doesn't sound defensive or over-technical / Structuring the answer clearly when the situation is complicated / Getting the response out quickly enough / Something else

If "kickoff or scoping documents":
> "What's the most repetitive part of building a kickoff or scoping doc?"
Options: Setting up the basic structure and boilerplate sections / Pulling in the right info from the brief or email thread / Adapting past examples without it feeling like a copy-paste / Getting the timeline and deliverable list to look right / Something else

**Q7 — Open-text moment** (see Step 4 in SKILL.md)

**Q8 — AI experience** (buttons):
> "Have you used Claude or any AI tools for work tasks before?"

Options: Yes, fairly regularly / A few times, with mixed results / Once or twice but it didn't really stick / Not really

**Q9 — Barrier check** (buttons):
> "What would make an AI solution feel too complicated to bother with?"

Options: If it takes more time to set up than it saves / If I have to paste in a lot of context every time / If the output still needs major editing / If it only works sometimes / Something else

## Output guidance

Strong recommendation candidates for this role:
- A meeting-to-summary workflow: paste raw notes or a transcript, get a structured summary with decisions and action items
- A brief-to-kickoff-deck workflow: paste a client brief or email thread, get a kickoff deck outline or first-pass draft
- A client-question-response workflow: describe the situation, get a draft response at the right tone and detail level
- A status update generator: paste what's done, in review, and next — get a client-ready status update in one pass
- A workback schedule generator: paste deliverables, timeline, and team info, get a draft workback schedule

Example "Where to start" prompt for the output document:
> "I need to write a status update for [client]. Here's what's done: [list]. Here's what's in review: [list]. Here's what's next: [list]. Write a professional, concise status update I can send. Keep it short and avoid sounding like a form letter."
