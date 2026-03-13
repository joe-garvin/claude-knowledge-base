# Red Door AI experimentation project

**Date:** March 13, 2026
**Source context:** Internal meeting with Chris Telfer and Najwa Yosof (Red Door Collaborative), followed by post-meeting working session in Claude. Covers meeting debrief, action items, document creation, monday.com board updates, and follow-up email drafting.

---

## Project background

Joe has been leading internal AI experimentation efforts at Red Door Collaborative, a boutique creative agency in Bellevue, WA that produces marketing content for clients including Microsoft, Databricks, and Salesforce. The central worked example is an AI-assisted SOW (statement of work) generator, built first as a standalone Python/Flask app and then rebuilt as a Claude Project. The broader goal is identifying and building AI automation for repetitive internal processes across the agency.

A discovery call with an external AI vendor (CYSTEMS, contact: Sean Champ Smith) is scheduled for **March 26, 2026** (rescheduled from the 23rd to accommodate Joe). Attendees: Joe, Chris, Naj, Tom, Brian.

---

## March 13 internal meeting — key takeaways

### What went well
- Meeting had a natural, conversational flow rather than feeling like a formal presentation
- Joe walked through the outline document, the SOW Claude Project demo, and the tools section
- Chris was visibly engaged and added substantial new context throughout
- Strong alignment on goals, realistic expectations about AI limitations, and enthusiasm for next steps

### New information surfaced in the meeting

- **SOW templates come from the client, not Red Door.** Microsoft, Databricks, and Salesforce each have their own templates that they provide to Red Door to fill in. This changes the architecture of the Claude Project approach: one project per client makes more sense, each referencing that client's specific template.
- **Microsoft SOWs are the most complex** due to the rate card, volume discounts, and year-over-year discount structure. Databricks and Salesforce are simpler — no discount tables, no hours/rates breakdown, just flat deliverable costs. Priority order for building out client-specific projects: Databricks or Salesforce first, Microsoft second.
- **Microsoft staff augmentation SOWs** sometimes include a PII/compliance table that would likely need to be dropped in manually. Worth flagging as a known exception when building that Claude Project.
- **Sean (CYSTEMS) primarily uses Claude**, which creates potential for synergy with what Joe has already built.
- **Sean's planned approach** includes setting up a RAG system with a closed loop (sensitive/pricing data) and an open system, plus a SOUL.md file — a governing document capturing Red Door's identity, values, and operating philosophy as context for AI tools.
- **Chris and Brian are already doing data cleanup work** with an Excel consultant as a precursor to AI — cleaning up the rate card spreadsheet so data is ready to be pulled programmatically.
- **Internal HR/policy chatbot** — Chris wants to feed the Red Door employee handbook into a closed-loop agent so staff can self-serve on HR questions (PTO, insurance, policies) without going to Brian every time.

### Chris's overarching vision
80% of the lift on processes like SOW generation done by AI, with humans spending 20% of their time on vetting and adjustments. Wants to give everyone at Red Door back 20% of their time. Sees this as a constant discovery process — tackle one thing, then identify the next.

---

## SOW Claude Project — current state and pivot

### What's built (current Microsoft-focused version)
- Project-level instructions defining how Claude handles SOW requests
- Real example SOWs as reference models
- A starter prompt for Naj to kick off new SOW chats
- A SOW template file with `{{PLACEHOLDER}}` tokens
- A placeholder reference document mapping each token to plain-English descriptions
- Step-by-step user guide and test scenarios with generated outputs

### Pivot: one Claude Project per client
Based on the meeting revelation that each enterprise client provides their own SOW template, the architecture should be:
- One Claude Project per client (Microsoft, Databricks, Salesforce, etc.)
- Each project references that client's specific template
- If a client updates their template, only that project needs to be updated
- Over time, each project accumulates a repository of past SOWs from that client as additional reference models
- Microsoft project may need separate handling for staff augmentation vs. creative/project-based work due to the PII compliance table

---

## Monday.com AI automations board

Board: **Red Door AI Automations** (ID: 18403856642)
Groups: References | Ongoing AI Projects | Wishlist Projects

### Items added to Wishlist Projects in this session
All items below were added with status "Not Started":

| Item | Description | Priority | Complexity (1–10) |
|---|---|---|---|
| RFP drafting | Feed in a client brief or RFP document, get a structured Red Door response draft | High | 6 |
| RFP discovery | AI actively searches for relevant RFPs to support biz dev; no one currently dedicated to prospecting | Medium | 8 |
| Workback schedule generation | Generate a draft based on project details and team availability; standard templates already exist | High | 4 |
| Kickoff deck generation | Adapt content from a brief or email chain into a branded RDC kickoff deck using the existing PowerPoint template | High | 3 |
| Internal HR / policy chatbot | Closed-loop agent fed with the Red Door handbook; staff self-serve on HR questions without going to Brian | Medium | 7 |
| Client onboarding materials | Welcome docs, project overview one-pagers, intro emails; high repetition project to project | Medium | 3 |
| Creative briefs | Translate a client call or email thread into a structured brief for the creative team | Medium | 4 |
| Change order drafts | When scope changes, generate a formatted change order from a description of what shifted | Medium | 4 |
| Job descriptions and contractor briefs | Generate JDs and project briefs for freelancers; Red Door hires regularly and these follow a consistent pattern | Low | 3 |
| LinkedIn and newsletter content | Repurpose existing client work into LinkedIn posts or newsletter copy for Red Door's own channels | Low | 4 |
| Cost proposals | Generate quick cost proposals for clients who need fast pricing before a full SOW | High | 5 |

Note: The first five items (RFP drafting through Internal HR/policy chatbot) were accidentally added to the References group and need to be manually dragged into Wishlist Projects. The last six were added to Wishlist Projects correctly.

### SOW Generation item — suggested description
> Generate a structured SOW draft from a scoping conversation or email thread. Input is whatever the client has communicated so far — deliverable details, specs, timelines. Output is a properly formatted Word document following the client's SOW template, with the right sections, boilerplate language, and detail level filled in. Pricing and final review stay with Chris. Currently built as a Claude Project with a Microsoft template; next step is expanding to one project per client (Databricks, Salesforce, etc.), each referencing that client's own template.

---

## Follow-up email to Chris and Naj

Drafted and sent (March 13, 2026). Subject: "Follow-up from this morning + outline doc for Sean"

### Attachments / items referenced:
- Meeting outline doc (`Exploring AI for Red Door internal processes`) — Chris specifically requested this for Sean's prep package
- Zip file containing the SOW Claude Project materials: Claude Project guide, two generated output examples, SOW template file, placeholder reference doc
- Red Door Prompt Library — currently a Google Doc; offered to export as Word file for inclusion in Sean's package

### Key framing in the email:
The outline doc description was written so Chris could lift it verbatim when forwarding to Sean: it walks through Red Door's framework for identifying AI automation opportunities, uses the SOW generator as a worked example, and includes a running list of identified opportunities (RFP drafting, RFP discovery, workback schedule generation, kickoff deck generation, and more).

---

## Pending action items

- [ ] Manually move misplaced monday.com items from References into Wishlist Projects (five items)
- [ ] Add complexity scores to the six new Wishlist Projects items added in this session (pending approval)
- [ ] Write up the one-project-per-client plan for the SOW Claude Project and share with Chris/Naj separately
- [ ] Export Red Door Prompt Library from Google Docs to Word and send to Chris for Sean's package
- [ ] Chris to compile and send prep materials to Sean (deadline: before March 26)
- [ ] CYSTEMS discovery call — March 26, 2026, 12:30 PM, 1.5 hours. Attendees: Joe, Chris, Naj, Tom, Brian

---

## Reference: complexity scores (1–10) for all wishlist items

| Item | Score | Notes |
|---|---|---|
| Kickoff deck generation | 3 | Existing branded template, predictable inputs, nearly fully automatable |
| Client onboarding materials | 3 | Known structure, repetitive assembly, similar to kickoff decks |
| Job descriptions / contractor briefs | 3 | Highly repetitive, consistent structure, past examples available |
| Workback schedule generation | 4 | Slightly complex due to resourcing data; template logic is straightforward |
| Creative briefs | 4 | More judgment involved but still well-defined structure |
| Change order drafts | 4 | Same template-based pattern as SOW generation, narrower scope |
| LinkedIn and newsletter content | 4 | Voice consistency adds complexity beyond pure document assembly |
| SOW generation | 5 | Partially built; complexity from one-project-per-client expansion and Microsoft discount math |
| Cost proposals | 5 | Similar ceiling to SOW generation; still requires pricing book logic |
| Internal HR / policy chatbot | 7 | Access controls, data accuracy, and trust bar make it harder than it appears |
| RFP drafting | 6 | More varied than SOWs; more judgment required in structuring a response |
| RFP discovery | 8 | Outbound/autonomous; requires external sources, reliable ongoing operation |
