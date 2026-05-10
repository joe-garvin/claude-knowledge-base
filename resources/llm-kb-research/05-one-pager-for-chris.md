# LLM knowledge bases: a brief for Chris Telfer

*April 2026*

## Context for this note

You've already spoken with Sean Champ Smith at CYSTEMS and received their proposal. They diagnosed three priorities — SOW automation, RFP/proposal acceleration, and BI/reporting — and proposed a RAG platform built on Claude/Anthropic as the foundation. The discovery session is the next step.

This note isn't an argument against that conversation. It's context that will help you walk in with clearer questions and a sharper sense of what you're evaluating.

## The underlying problem (as CYSTEMS correctly named it)

RDC's institutional knowledge is scattered — across SharePoint sites, Box, Google Drive, individual hard drives, and people's heads. When proposals get written, the team re-creates things that already exist. When someone joins, they learn by trial and error rather than from what the team already knows. When someone leaves, their knowledge goes with them.

CYSTEMS's framing of this as an operational bottleneck costing time and margin every month is accurate.

## What CYSTEMS is proposing

A purpose-built RAG platform — a centralized system that ingests RDC's SharePoint/OneDrive content, templates, rate cards, past SOWs, and client data, and makes it queryable through a natural language interface. You upload a brief; you get a draft SOW. You ask a question; you get an answer grounded in RDC's own data.

Their security framing is meaningful for RDC specifically: closed-loop, no client data touching public AI models, managed IT oversight. For a firm doing NDA-sensitive Microsoft and government work, that matters.

Their timeline is approximately two months from kickoff to full delivery, with pricing to be scoped at the discovery session. (Their public packages run €12K–€25K for setup and €750–€1,250/month for maintenance, though RDC's custom build would be separately scoped.)

## What this note introduces: a different approach

In April 2026, Andrej Karpathy — former head of AI at Tesla, one of the most credible practitioners in the field — published a widely-discussed description of an alternative to RAG. The idea: instead of building retrieval infrastructure, use Claude to build and maintain a structured knowledge base directly — a wiki of interlinked markdown files that compounds over time.

You don't retrieve raw documents on demand. Claude compiles the knowledge once, keeps it current, and answers from that synthesis. No database. No retrieval pipeline. Just well-organized files and Claude.

The pattern has attracted significant attention in the past month — tools, companies, and implementations are emerging rapidly around it.

## How the two approaches map to RDC's three priorities

This is the most important thing to understand going into the discovery session.

**RFP & Proposal Acceleration** — this is where the LLM wiki approach is directly competitive with RAG. A knowledge base containing past proposals, client research, and RDC's Messaging Positioning Framework would power faster, grounded first drafts. You already use Claude for this; the wiki gives Claude better organized context to work from. This could be built and tested in weeks, for near-zero cost beyond Claude API usage.

**SOW & Contract Automation** — partially overlapping. An LLM wiki with templates, rate cards, and past SOW examples would help, and Claude can generate 80–85% complete SOW drafts today with good prompts and examples. But the SOW automation CYSTEMS is describing — a system that generates structured documents from defined parameters — is more of a document workflow than a knowledge retrieval problem. Claude with the right setup can address this without a full RAG build.

**Business Intelligence & Reporting** — this is not what either approach addresses natively. Automated BI requires live connection to operational data — your Excel files, financial records, workstream breakdowns. Neither a knowledge wiki nor a RAG retrieval layer solves this on its own; it requires data pipeline and dashboard tooling. This is a separate problem from knowledge synthesis, and worth asking CYSTEMS specifically how they address it.

## What the LLM wiki approach offers

**For RFP/proposal work specifically:**

- Deployable in days, not months
- Costs what we already spend on Claude — no new vendor, no new contract
- Transparent: the wiki is just readable files, not a black box
- Every proposal written, every client brief ingested, every lesson captured makes the next one better
- No lock-in: if it stops serving us, we've lost nothing but the time to set it up

**What it doesn't offer:**

- The enterprise security infrastructure CYSTEMS is describing (closed-loop, managed IT oversight, air-gapped from public models) — for genuinely NDA-sensitive work, this is a real gap
- Automated BI/reporting — that problem requires different tooling regardless
- A branded dashboard or purpose-built UI — it's Claude sessions against organized files, not a polished product

## The question worth sitting with before the discovery session

CYSTEMS is proposing a platform that addresses three distinct problems: knowledge retrieval, document automation, and business intelligence. Each of those is a legitimate problem. But they're different problems, and it's worth knowing which one is urgent enough to pay for — and which ones could be addressed with what we already have.

Specifically: the RFP and proposal acceleration use case may be 80% solvable with Claude and a lightweight knowledge base we build ourselves, in the next few weeks, for free. If that's true, the discovery session question shifts from "should we buy this system" to "what is the system solving that we couldn't solve ourselves — and is that worth the cost and the dependency?"

That's not an argument against CYSTEMS. Their proposal has real strengths, particularly on security and the foundation architecture framing. It's an argument for walking into the session knowing exactly which problems you're trying to buy your way out of.

## The short version

CYSTEMS is proposing a well-scoped solution to real problems. Before the discovery session, it's worth knowing that one of those three problems — RFP and proposal acceleration — has a low-cost, low-risk alternative that could be tested immediately. The other two (SOW automation and BI/reporting) are more complex and may genuinely benefit from what CYSTEMS is building.

Going in informed doesn't mean going in skeptical. It means knowing which questions to ask.

*Prepared by Joe Garvin, April 2026.*

## Sources

- [Karpathy's original tweet](https://x.com/karpathy/status/2039805659525644595) (April 2, 2026)
- [Karpathy's llm-wiki GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [VentureBeat: Karpathy's LLM Knowledge Base architecture](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an)
- CYSTEMS x Red Door Collaborative proposal document (March 2026, confidential)
