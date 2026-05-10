# LLM knowledge base research and proposal

A collection of research and strategy documents around building an LLM-native knowledge base at Red Door Collaborative, produced in April 2026 in the context of an ongoing evaluation of an AI platform proposal from CYSTEMS.

## Context

In March 2026, CYSTEMS (cystems.io) submitted a confidential proposal to Chris Telfer for an AI strategy and integration partnership. Their proposed solution: a RAG-based platform built on Claude/Anthropic to centralize RDC's fragmented institutional knowledge and address three operational priorities — RFP/proposal acceleration, SOW automation, and BI/reporting.

These documents were produced to:
1. Research the underlying LLM knowledge base concept, prompted by Andrej Karpathy's widely-circulated April 2026 post on the topic
2. Compare the LLM wiki approach against the RAG architecture CYSTEMS proposed
3. Develop a concrete RDC-specific implementation plan for the LLM wiki pattern
4. Surface the real challenges and honest limitations of that approach
5. Prepare a brief for Chris to sharpen the CYSTEMS discovery session

## Documents (in reading order)

| File | Contents |
|------|----------|
| [00-cystems-proposal-context.md](00-cystems-proposal-context.md) | Background on CYSTEMS, their March 2026 proposal, RDC's three identified pain points, and how the LLM KB maps to each |
| [01-concept-overview.md](01-concept-overview.md) | What LLM knowledge bases are, the Karpathy LLM Wiki pattern, three-layer architecture, and the ecosystem landscape as of April 2026 |
| [02-llm-kb-vs-rag.md](02-llm-kb-vs-rag.md) | Side-by-side architectural comparison of LLM wiki and RAG, with honest limitations of both and an RDC-specific recommendation |
| [03-rdc-implementation-guide.md](03-rdc-implementation-guide.md) | Concrete implementation plan for RDC: folder structure, schema file, multi-user access model, RBAC tiers, tooling stack, and phased rollout |
| [04-challenges-and-pitfalls.md](04-challenges-and-pitfalls.md) | Honest assessment of eight specific challenges: multi-user friction, error compounding, RBAC gaps, embedded team access, scale ceiling, governance burden, compliance, and adoption |
| [05-one-pager-for-chris.md](05-one-pager-for-chris.md) | Executive brief for Chris Telfer: framing for the CYSTEMS discovery session, mapping of each approach to RDC's three priorities, and key questions to bring |

## Currency

Produced April 2026. The CYSTEMS discovery session was the immediate context; this research remains relevant as a foundation for any internal LLM knowledge base initiative at RDC.
