# Project managers, account managers, and embedded consultants — interview guide

## Embedded consultant note

Mindy Bomonti and Sallie St. Laurent are RDC consultants embedded at Microsoft. If someone identifies as an embedded consultant, use this same reference file but adjust your framing throughout: their work happens inside a large enterprise client environment, not at RDC directly. Their friction points likely involve navigating large org processes, working across many internal Microsoft stakeholders, managing deliverables that go through extensive client review cycles, and producing communications that have to work within Microsoft's style and process norms. The AI opportunities are similar in shape — document generation, communication drafting, research synthesis, meeting notes — but the examples and first-step prompts should reflect a Microsoft enterprise context rather than a small agency context. Ask one early clarifying question if needed to understand what kinds of work they primarily do before drilling into friction.

---

## Role context

PMs and AMs at RDC (currently Naj/Najwa and Silas) sit at the intersection of client communication and internal coordination. They receive briefs and direction from clients, translate that into actionable work for the creative team, track project status across multiple active deliverables, manage review rounds and feedback, and handle a high volume of back-and-forth communication in both directions.

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
- **Brief-to-internal-direction translation**: Turning a client email or call into a clear brief for the creative team — getting the right level of detail, the right format, the right tone
- **Status update writing**: Composing regular status updates and client-facing summaries that feel professional and are fast to produce
- **Meeting notes**: Turning a meeting transcript or rough notes into a clean, structured summary with action items
- **Client communication drafting**: Writing clear, appropriately toned responses to client questions or concerns — especially when the answer is complicated or the situation is sensitive
- **Tracking what's outstanding**: Keeping mental track of what's been requested, what's been delivered, what's still outstanding across multiple projects
- **Onboarding new projects**: Getting up to speed on a new project quickly — what are the deliverables, who are the stakeholders, what's the timeline

## Question sequence

After role is confirmed, continue:

**Q2: Volume and mix**
> "On a typical week, where does most of your time go?"

Options:
- Client communication (email, Teams, calls)
- Building and maintaining project documents
- Coordinating between clients and the creative team
- Tracking project status and chasing things
- Something else

**Q3: Document generation**
> "When you need to build a project document — a kickoff deck, brief, workback schedule — how do you usually start?"

Options:
- I find a past example and adapt it
- I start from a blank template
- I build it from scratch each time
- It depends on the document type

**Q4: Where time gets lost**
> "What kind of writing or document task takes longer than it should?"

Options:
- Writing status updates or client summaries
- Turning meeting notes into something structured
- Drafting responses to tricky client questions
- Building kickoff or scoping documents from a brief
- Something else

**Q5: Drill-down on top friction**

If they said "status updates or client summaries":
> "What makes status updates take longer than you'd like?"

Options:
- Finding the right tone — professional but not stiff
- Figuring out what level of detail the client actually wants
- Gathering all the relevant info before I can write anything
- Writing basically the same update slightly differently every time
- Something else

If they said "meeting notes":
> "What's the hardest part of turning a meeting into a useful summary?"

Options:
- Capturing everything accurately in the moment
- Organizing what was discussed into a clear structure after
- Pulling out the actual action items from a long conversation
- Getting it done while it's still fresh — it always falls to the end of the day
- Something else

If they said "tricky client questions":
> "When a client asks something complicated, what's the hardest part of responding?"

Options:
- Figuring out the right level of detail — not too much, not too little
- Finding the right tone so it doesn't sound defensive or over-technical
- Structuring the answer clearly when the situation is complicated
- Getting the response out quickly enough
- Something else

If they said "kickoff or scoping documents":
> "What's the most repetitive part of building a kickoff or scoping doc?"

Options:
- Setting up the basic structure and boilerplate sections
- Pulling in the right info from the brief or email thread
- Adapting past examples to fit the new project without it feeling like a copy-paste
- Getting the timeline and deliverable list to look right
- Something else

**Q6: Communication volume**
> "How much of your day is writing — emails, Teams messages, project notes?"

Options:
- It's most of my day
- A significant chunk — maybe half
- It comes and goes depending on the project phase
- Less than you'd think — it's more coordination

**Q7: AI experience**
> "Have you used Claude or any AI tools for work tasks before?"

Options:
- Yes, fairly regularly
- A few times, with mixed results
- Once or twice but it didn't really stick
- Not really

**Q8: Barrier check**
> "What would make an AI solution feel too complicated to bother with?"

Options:
- If it takes more time to set up than it saves
- If I have to paste in a lot of context every time
- If the output still needs major editing
- If it only works sometimes
- Something else

## Output guidance for project managers

Strong recommendation candidates for this role:
- A meeting-to-summary workflow: paste raw notes or a transcript, get a structured summary with decisions and action items pulled out clearly
- A brief-to-kickoff-deck workflow: paste a client brief or email thread, get a kickoff deck outline or first-pass draft in the right structure
- A client-question-response workflow: describe the situation and what the client asked, get a draft response at the right tone and detail level
- A status update generator: paste the current project state (what's done, what's in review, what's next), get a client-ready status update in one pass
- A workback schedule generator: paste deliverables, timeline, and team info, get a draft workback schedule to refine

For the "first step" in each recommendation, give them an actual prompt they could use. For example:

> "Here's a starting point: 'I need to write a status update for [client]. Here's what's done: [list]. Here's what's in review: [list]. Here's what's next: [list]. Write a professional, concise status update I can send. Keep it short and avoid sounding like a form letter.'"

Keep recommendations grounded in things they can do right now without any setup. Do not suggest building templates, projects, or anything requiring configuration.
