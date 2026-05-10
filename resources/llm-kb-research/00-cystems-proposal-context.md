# CYSTEMS proposal context

*Reference document for Red Door Collaborative | April 2026*

## Background

In March 2026, Red Door Collaborative had an initial exploratory call with Sean Champ Smith of CYSTEMS (cystems.io). Sean followed up with a confidential proposal document — "CYSTEMS x Red Door Collaborative: AI Strategy & Integration Partnership" — prepared for Chris Telfer and dated March 2026. The upcoming session is a formal Discovery Session, not a first contact.

## What CYSTEMS does

CYSTEMS is an AI strategy and integration firm. Their public service offerings include AI strategy consulting, social media automation, custom AI customer service agents, and workflow automation. They position themselves as "One ECOCYSTEM Multiple Solutions" — a suite of AI capabilities rather than a single-purpose tool.

Importantly for RDC: CYSTEMS builds specifically on Anthropic's architecture and Claude as the underlying model. This means they're not proposing a generic enterprise AI platform — they're proposing a purpose-built system using the same model RDC already uses and trusts.

**Public pricing (from cystems.io, as of April 2026):**
- Social Media Automation Machine: €12K setup or €750/month maintenance
- AI Agent Buildout (most popular): €20K setup or €1,250/month maintenance
- Echo – Intelligent Feedback Agent: €25K setup or €1,350/month maintenance

RDC's custom scope has not yet been priced — that will be determined at the Discovery Session.

## What they heard from RDC

CYSTEMS summarized three priority pain points from their initial call with Chris:

**1. SOW & Contract Automation.** RDC writes Statements of Work constantly, with May–June being particularly high-pressure due to Microsoft's fiscal year reset in July. CYSTEMS proposes a system that can generate 80–85% complete SOWs from existing templates, rate cards, and project parameters — requiring only minor human refinement before delivery.

**2. RFP & Proposal Acceleration.** Government contracts (e.g., City of Seattle) require 275+ page documentation packages with two-week turnarounds. RDC is already using Claude with its Messaging Positioning Framework for this, but needs a purpose-built system that draws from the full knowledge base to generate comprehensive first drafts at speed.

**3. Business Intelligence & Reporting.** Client performance analysis is currently run manually in Excel — year-over-year comparisons, workstream breakdowns (Visual Studio vs. Azure vs. SMB), percentage allocations. RDC is running roughly a month behind on insights. CYSTEMS proposes making this live, automated, and available on demand.

## What CYSTEMS is proposing

A single, secure, centralized RAG platform built on top of RDC's existing data infrastructure — described as "the operational brain for Red Door's internal processes."

The platform would include:

- **Data aggregation:** SharePoint/OneDrive content, rate cards, templates, past SOWs, proposals, and client data ingested into a unified knowledge base.
- **Custom AI interface:** A branded dashboard for natural-language interaction. Upload a brief, get a draft SOW. Ask a question, get an answer grounded in RDC's own data.
- **Multi-modal input:** Text prompts, document uploads, spreadsheet analysis.
- **Closed-loop security:** Designed for NDA-sensitive client work. No client information touches public AI models. RDC's managed IT provider maintains full oversight.
- **Foundation architecture:** The RAG platform as a base layer for future automation — SOWs first, proposals, BI reporting, and eventually content production.

**Projected timeline:** Approximately 2 months from kickoff to full delivery (April–May 2026 target). Discovery Session → SOW & pricing → contract & kickoff → build & deploy → handoff.

## What they said about adoption

CYSTEMS acknowledged RDC's mixed AI maturity directly. Their framing: AI champions on the team become internal evangelists whose experiments scale into company-wide systems; more cautious team members' concerns are addressed by human review built into every output, and a system trained on RDC's own standards, voice, and quality bar. Their stated goal: "A team that's aligned, confident, and equipped — not divided."

## What they said about themselves

Five differentiators from their proposal:

- Understanding of creative teams (not purely tech-oriented)
- Closed-loop security by design
- Claude/Anthropic-native (builds on what RDC already uses)
- Partnership model, not vendor relationship
- Clear milestones and defined deliverables; "a completed system you own"

## What to bring to the Discovery Session (per CYSTEMS)

- Examples of current SOW templates and rate cards
- A recent RFP or proposal
- Current Claude-based SOW experiments (live demo welcome)
- Any reporting spreadsheets or dashboards in use today
- Questions, concerns, and wish lists

**Contact:** Sean Champ Smith | sean@cystems.io | cal.com/cystems/1hr

## How this maps to the LLM knowledge base question

Not all three of CYSTEMS's identified use cases are equivalently addressed by the LLM knowledge base approach:

**RFP & Proposal Acceleration** is the strongest overlap. An LLM wiki containing past proposals, client knowledge, and RDC's Messaging Positioning Framework would directly power faster, grounded first drafts. This is squarely what the knowledge base approach does well.

**SOW & Contract Automation** is partially addressable. An LLM wiki with rate cards, templates, and past SOW examples would help, but the core of what's being proposed — a system that generates structured legal/financial documents from defined parameters — is more of a document automation workflow than a knowledge retrieval problem. Claude can do significant heavy lifting here with or without a purpose-built RAG system; the question is whether a knowledge base makes it materially better.

**Business Intelligence & Reporting** is least addressable by an LLM knowledge base. BI/reporting automation requires live connection to operational data (Excel files, financial records, workstream data) — not a knowledge synthesis layer. Neither RAG nor an LLM wiki solves this on its own; it requires data pipeline and dashboard tooling. This is the piece most clearly outside the knowledge base conversation.

This mapping is worth keeping in mind when evaluating the approaches: the LLM wiki may resolve one of the three priorities well, partially address a second, and not address the third at all.
