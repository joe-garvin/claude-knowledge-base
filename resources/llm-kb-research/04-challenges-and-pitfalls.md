# Challenges and pitfalls: the LLM knowledge base at RDC

*Research document for Red Door Collaborative | April 2026*

## Overview

The LLM knowledge base pattern is genuinely promising for a creative agency like RDC. But it's an emerging idea, and the honest assessment includes real limitations — especially when adapted from its original single-user context to a team of 30+ people across multiple workstreams. This document catalogs the challenges you should expect, why they're hard, and what can be done about each.

## 1. Multi-user contribution is not a solved problem

**The issue.** The LLM wiki was designed and optimized for a single researcher — one person, one agent, one coherent point of view on the knowledge base. Karpathy describes a solo setup: he adds sources, he runs ingests, he asks questions. The system has no concept of multiple people contributing simultaneously with different perspectives on what the wiki should contain.

At RDC, you have 30+ team members, multiple account teams, and at least two distinct operational contexts (in-house creative vs. embedded at Microsoft). Getting all of them to contribute to a shared wiki in a coherent way is a genuine coordination challenge.

**What goes wrong.** If multiple people add conflicting sources — say, two writers with different takes on Databricks' brand voice — the wiki may develop internally contradictory pages that the lint process can flag but can't resolve. If contribution is ad hoc, the wiki fills unevenly: well-populated in areas where engaged contributors work, sparse everywhere else. If the intake pipeline isn't clear and easy, most people won't use it.

**Mitigation.** Designate a wiki steward with clear ownership of the wiki's coherence. Use a structured intake pipeline (Teams channel, SharePoint form) rather than letting people write directly to the wiki. Set clear guidelines in the CLAUDE.md about how contradictions are handled. Accept that the wiki will reflect the team's actual knowledge, not a perfect synthesis, and that linting is how you keep it from drifting.

**Residual risk.** Even with a steward, the contribution workflow adds friction. In a busy agency where everyone is billable, maintaining a knowledge base as a non-billable activity is genuinely hard to sustain. This is not a technical problem — it's a cultural and operational one.

## 2. Error compounding

**The issue.** This is one of the most frequently cited risks of the LLM wiki pattern. As one practitioner put it: "When outputs get filed back, errors compound too." If the LLM writes something subtly wrong into a wiki page — a mischaracterized client preference, a flawed synthesis of brand voice guidelines — and that page then becomes a source for future queries and ingests, subsequent content builds on the error. Over time, a small initial mistake can contaminate a significant portion of the wiki.

**What goes wrong.** A writer asks Claude to summarize RDC's tone guidelines for Microsoft. Claude writes a summary that's slightly off — it conflates the formal Azure docs tone with the conversational SMB tone. That summary gets filed into the wiki. Future queries about Azure tone pull from that page. The error propagates.

**Mitigation.** Several practices reduce this risk. First, never file an output back into the wiki without human review. The answer is valuable and worth preserving, but someone should read it before it becomes canonical. Second, run monthly lint passes that actively look for contradictions and unsupported claims. Third, keep raw sources immutable — the LLM can recompile wiki pages from raw sources if an error is discovered. Fourth, treat high-stakes wiki pages (brand voice guides, client personas) as requiring explicit human sign-off before they go into the wiki.

**Residual risk.** Error compounding is harder to catch the older and more embedded the error is. A mistake in a page from six months ago may be cited dozens of times before a lint pass surfaces it. This is a meaningful limitation compared to RAG, where the source documents are immutable and errors in the synthesis are at least traceable to the retrieval step.

## 3. Role-based access control is complex and imperfect

**The issue.** The wiki pattern has no built-in RBAC. Access controls live at the file system level — which folders a person can see on SharePoint or Box. This works for coarse-grained separation (Tier 1 / Tier 2 / Tier 3) but has real limitations for fine-grained control.

**What goes wrong.** A writer on the Azure account has SharePoint access to the Azure wiki folder. When they query Claude, Claude can only see what's in their Claude session — which is what they've pointed Claude at. If they've pointed Claude at only the Azure wiki folder, they can't accidentally see Databricks content. But if they've pointed Claude at the full wiki directory (which is the more convenient setup for broad queries), they potentially see all client wikis. The access control depends on how they've configured their Claude session, not on a system-level filter Claude enforces.

Additionally, the embedded Azure and VSS teams operate inside Microsoft's environment, with different tool access. Getting those team members onto a shared RDC knowledge base requires a clear path for how they access the files — which may conflict with Microsoft's security policies.

**Mitigation.** Structure the folder hierarchy so that sensitive tiers are clearly separated and require deliberate action to include in a Claude session. Document the expected Claude session configuration for each role in the "how to use the wiki" guide. For the most sensitive materials (financials, HR, new business pipeline), keep them in purpose-built systems rather than the wiki. Reserve the wiki for knowledge that, if seen by the wrong person, causes embarrassment rather than serious harm.

**Residual risk.** This approach is not comparable to enterprise-grade RBAC in a properly architected RAG system. A well-built RAG system with metadata-level access filtering can enforce strict document-level permissions that the LLM wiki simply cannot replicate without significant additional tooling. If RDC's RBAC requirements are strict — for example, if client contracts prohibit certain staff from seeing certain project materials — the wiki pattern may not be sufficient as-is.

## 4. The embedded teams are hard to integrate

**The issue.** The Azure account team (9 people) and the VSS team (5 people) work inside Microsoft's environment. Their day-to-day tools are Microsoft's — Teams, SharePoint internal to Microsoft, Microsoft-managed endpoints. They can't easily access an RDC-hosted SharePoint site or a GitHub repo in the same way the in-house creative team can.

Integrating their knowledge into the wiki means finding a pathway from Microsoft's environment to RDC's. That pathway may be constrained by Microsoft's security policies, NDA provisions, or the practical reality that embedded staff are primarily focused on client deliverables and have limited bandwidth for RDC internal operations.

**What goes wrong.** The embedded teams end up with a separate, disconnected knowledge base (or no knowledge base at all). The institutional knowledge from the Azure and VSS workstreams — which is substantial — doesn't flow into the shared RDC wiki. The in-house creative team doesn't benefit from what the embedded teams have learned, and vice versa.

**Mitigation.** Designate a liaison from each embedded team (the account manager, or a senior team member) whose role includes periodically distilling key insights from the embedded context into a format that can be shared with RDC. This doesn't require Microsoft-hosted files; it means a human writes a summary note and adds it to the RDC intake pipeline. The wiki doesn't need to hold everything — it needs to hold the synthesized institutional knowledge, not the raw Microsoft-internal materials.

**Residual risk.** Some knowledge from the embedded context is inherently not shareable — it's inside Microsoft's systems, governed by Microsoft's confidentiality policies. The wiki can only hold what's appropriate to hold. This is a real constraint on the completeness of the knowledge base.

## 5. Scale ceiling and context window limits

**The issue.** The LLM wiki's index-based navigation approach works well up to roughly 100–500 sources, or a few hundred wiki pages. Beyond that, the index gets unwieldy, and navigating to relevant pages becomes less reliable. At some scale, the approach requires a lightweight search layer (like qmd) to remain effective.

Additionally, even with large context windows, there are limits to how much of the wiki Claude can hold in context for a single query. Queries that require synthesizing information from many disparate wiki sections may hit these limits, leading to answers that miss relevant context.

**RDC's likely trajectory.** RDC is not currently near the scale ceiling. A focused first implementation — covering the top 3–4 clients and the key craft and operations topics — would involve perhaps 50–100 raw sources and 50–100 wiki pages. That's well within the comfortable operating range.

Over 12–24 months of active use, the wiki could grow to 300–500 wiki pages if ingestion is consistent. At that point, a search tool like qmd would be worth adding. This is not a blocker — it's a natural evolution point.

**Mitigation.** Design the wiki to stay focused rather than comprehensive. Not every document needs to be ingested. The steward's judgment about what belongs in raw/ is the primary quality control. Keep the index well-organized and enforce consistent YAML frontmatter so the index remains navigable as the wiki grows.

## 6. Governance and maintenance burden

**The issue.** The LLM handles the bookkeeping of wiki maintenance — updating cross-references, keeping summaries current, running lint passes. But someone has to ask it to do these things. The wiki doesn't maintain itself autonomously; it requires a human to initiate ingest passes, review outputs, and run the periodic lint.

In a busy agency where everyone is at or near capacity on billable work, the non-billable overhead of wiki stewardship can become a significant friction point. It's easy to let a week of ingestion pass slip. Then two weeks. Then the wiki is three months out of date and team members have stopped trusting it.

**What goes wrong.** The wiki becomes a snapshot of RDC's institutional knowledge as of the day it was last actively maintained. New projects add new learnings; those learnings never make it into the wiki. Team members stop querying it because they know it's stale. The system atrophies.

**Mitigation.** Treat wiki maintenance as a recurring operational commitment, not a project task. Build it into the wiki steward's role definition with time budgeted. Make the intake pipeline as frictionless as possible so contribution doesn't depend on a single person. Automate what you can: if a task can be triggered by a scheduled Claude job (e.g., a weekly prompt that asks Claude to check for new items in the intake folder and process them), schedule it.

**Residual risk.** This is ultimately a cultural challenge, not a technical one. No system survives organizational indifference. The wiki needs a champion who is genuinely invested in its health and whose role explicitly includes maintaining it.

## 7. No formal compliance or audit trail

**The issue.** In regulated industries or for clients with strict data handling requirements, a RAG system built by a vendor like CYSTEMS (cystems.io) can offer SOC2 compliance, HIPAA compliance, audit logs, and data residency controls. The LLM wiki stored in SharePoint or Git has the access controls and version history of those platforms — which is meaningful but not the same as a purpose-built compliant system.

**RDC's exposure.** For most of RDC's use cases, this is not a significant concern. Brand voice guides, writing samples, and operational knowledge are not regulated data. However, if the wiki were to hold financial data, HR information, or materials covered by specific client NDAs, the compliance posture of a flat file system would need to be more carefully evaluated.

**Mitigation.** Keep regulated and NDA-covered materials out of the wiki. Use the wiki for knowledge that, if inappropriately accessed, is embarrassing rather than legally significant. Maintain those data categories in the existing systems that are already governed appropriately.

## 8. The "not invented here" adoption problem

**The issue.** No knowledge system is useful if the team doesn't use it. RDC has a mixed AI maturity profile — some team members are confident Claude users, others have barely touched it. Asking the whole team to adopt a new workflow, even a simple one, requires deliberate change management.

The most common failure mode for internal knowledge bases is not technical failure — it's adoption failure. People contribute to the wiki for a month during the initial excitement, then revert to the way they've always worked.

**Mitigation.** Start with the people who are already converted — the Claude-fluent team members who can see the value immediately and become internal advocates. Demonstrate the wiki's value with concrete, specific examples that resonate with people's actual pain points (e.g., "Joe used the wiki to get Databricks brand context in 30 seconds instead of digging through three SharePoint sites"). Keep the contribution mechanism simple enough that it doesn't require anyone to learn a new tool.

## Summary: the honest bottom line

The LLM knowledge base is a legitimate, workable approach for RDC — but it is not a turnkey system. It requires a steward, a clear intake process, discipline around human review of outputs before they become canonical, and ongoing cultural investment.

The challenges above are real but manageable for an agency that commits to the approach seriously. They are also instructive about what a RAG system from CYSTEMS would or wouldn't solve. A custom RAG build would resolve the RBAC and compliance concerns more robustly. It would not solve the adoption, governance, or error-quality problems — those are organizational, not technical.

The decision between the two approaches should be made with a clear-eyed view of which problems are organizational (and would persist regardless of the system chosen) and which are technical (and would be better addressed by one architecture than the other).

## Sources

- [Karpathy's llm-wiki GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- ["I Went Through Every AI Memory Tool I Could Find"](https://x.com/witcheer/status/2044456778843238689) (@witcheer, April 15, 2026)
- ["How to Build Your Second Brain"](https://x.com/nickspisak_/status/2040448463540830705) (@nickspisak_, April 4, 2026)
- ["Claude + Obsidian should be illegal"](https://x.com/defileo/status/2042241063612502162) (@defileo, April 9, 2026)
- [Atlan: LLM Knowledge Base — Definition, Components, and Enterprise Use](https://atlan.com/know/what-is-an-llm-knowledge-base/)
- [Collaborative Memory RBAC research](https://arxiv.org/html/2505.18279v1) (arXiv 2505.18279)
- RDC operations and pain points context document (internal)
