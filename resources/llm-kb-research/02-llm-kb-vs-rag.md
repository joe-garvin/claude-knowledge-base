# LLM knowledge bases vs. RAG: a clear-eyed comparison

*Research document for Red Door Collaborative | April 2026*

## What each approach actually is

Before comparing them, it's worth being precise about what each approach does — because "RAG" is often used loosely to mean anything that connects an LLM to external documents.

**Retrieval-augmented generation (RAG)** is an architectural pattern in which an LLM retrieves relevant information from an external knowledge store at query time, then uses that retrieved information to generate a response. The typical implementation: documents are chunked into segments, each chunk is converted into a numerical vector (embedding) that captures its semantic meaning, and those vectors are stored in a vector database. When a user asks a question, the question is also converted into a vector, the database finds the nearest-neighbor chunks, and those chunks are injected into the LLM's context alongside the query. The LLM answers from whatever the retrieval pipeline surfaced.

**LLM knowledge base (LLM wiki)** is a pattern in which the LLM itself builds and maintains a structured, persistent wiki — a collection of interlinked markdown files — rather than querying raw documents at answer time. When you add a new source, the LLM reads it and integrates it into the wiki: updating topic pages, noting contradictions, maintaining cross-references. Queries are answered from the pre-synthesized wiki, not from raw documents retrieved on the fly.

The key difference: RAG re-derives answers from raw material every time. The LLM wiki compiles knowledge once, keeps it current, and answers from that compiled synthesis.

## How they differ architecturally

| Dimension | RAG | LLM knowledge base |
|---|---|---|
| Knowledge representation | Raw document chunks in a vector DB | Structured, synthesized markdown files |
| Query mechanism | Semantic similarity retrieval at query time | Index-based navigation + direct file reading |
| Infrastructure required | Embedding model, vector database, retrieval pipeline, orchestration layer | LLM agent + file system (markdown files) |
| Knowledge synthesis | Happens at query time (per-question) | Happens at ingest time (once, then updated) |
| Accumulation | None — each query starts fresh | Compounding — every addition enriches the whole |
| Human readability | Low — stored as vectors | High — stored as readable markdown |
| Setup complexity | High — multiple services to configure, tune, and maintain | Low — folder structure and a schema file |
| Cost to build | High ($10k–$100k+ for custom builds) | Low to moderate (primarily LLM API costs) |
| Cost to maintain | Ongoing engineering support typically required | Ongoing LLM API costs for ingest/lint passes |
| Scale ceiling | Very high (millions of documents) | Moderate (~100–500 sources before needing search tooling) |
| Error traceability | Low — hard to see why the wrong chunk was retrieved | High — you can read every wiki page directly |
| Multi-user support | Available via platform (Pinecone, Weaviate, etc.) | Requires additional tooling (Git, shared drive, or platform) |
| Role-based access | Mature (platform-level controls) | Requires custom implementation |

## Where RAG excels

RAG was designed for enterprise-scale knowledge retrieval and it does that well. When you have thousands to millions of documents — a legal firm's entire case library, an enterprise's complete technical documentation, a support system spanning 50,000 articles — RAG is the right tool. Its retrieval is fast (sub-200ms in production systems), it scales horizontally, and the infrastructure is mature.

RAG is also well-suited to situations where you need precise, citation-accurate retrieval from specific source documents. Legal, compliance, and regulated industries particularly benefit from RAG's ability to point to exact source locations.

Enterprise adoption of RAG has accelerated sharply: 85% of enterprises now use some form of RAG-based retrieval, up from 40% in 2024. It has become the default architecture for large-scale internal knowledge management. As of 2026, 60% of new RAG deployments include systematic evaluation from day one — a sign the field has matured past experimentation.

A custom RAG build from a vendor like CYSTEMS (cystems.io) typically involves: document ingestion pipelines, embedding infrastructure, a vector database, a retrieval orchestration layer, a front-end query interface, and ongoing engineering support. This is appropriate when the problem genuinely requires it.

## Where the LLM knowledge base excels

The LLM knowledge base pattern outperforms RAG on several dimensions that are highly relevant to creative agencies and small-to-mid-sized teams.

**Synthesis over retrieval.** RAG surfaces chunks. The LLM wiki surfaces synthesis. Ask a complex question requiring context from 10 different sources, and RAG has to find and reassemble the right fragments on the fly — and may miss the connections. The wiki already has the cross-references and the synthesis built in.

**Accumulation.** Every source added to the wiki doesn't just sit in a database — it actively updates existing pages, strengthens or challenges claims, and surfaces new connections. Over time, the wiki becomes richer than the sum of its sources. RAG doesn't accumulate anything; it just retrieves from what's there.

**Transparency.** You can read every page in the wiki. You know exactly what the LLM knows and why. When an answer is wrong or incomplete, you can go find the relevant wiki page and fix it. With RAG, when retrieval fails — when the wrong chunks are surfaced or the right chunks aren't found — the failure is often invisible and hard to diagnose.

**Zero infrastructure.** The LLM wiki requires a file system, an LLM agent, and a CLAUDE.md schema file. That's it. No embedding model to configure, no vector database to provision, no retrieval pipeline to orchestrate and maintain. For a team already using Claude, the marginal cost of standing up a wiki is the time to design the schema and the ongoing API costs for ingest and maintenance passes.

**Cost.** MindStudio's analysis found that for knowledge bases under roughly 200,000 tokens, full-context prompting with prompt caching can be faster and cheaper than building retrieval infrastructure. For a small agency's use case, the LLM wiki is a significant cost advantage over a custom RAG build.

**Human involvement.** The wiki is not a black box. Team members can read it, contribute to it, edit it, and understand it. This matters for a creative team that needs to trust and audit its own knowledge sources.

## The honest limitations of each

**RAG limitations:**
- Infrastructure complexity is real. Chunking strategy, embedding model choice, retrieval tuning — each requires engineering judgment and ongoing attention.
- Retrieval can fail silently. The wrong chunks get surfaced, or the right chunks aren't found, and the LLM generates a plausible-sounding but poorly-grounded answer. These failures are hard to catch.
- Each query re-derives from scratch. There's no learning, no synthesis, no compounding. The system is the same after 1,000 questions as it was after 10.
- Maintenance requires engineering support. When your document collection changes, the pipeline needs to re-index. Chunking strategies may need to be revisited. Vector databases need to be managed.

**LLM knowledge base limitations:**
- Scale ceiling. The index-based navigation approach works well up to roughly 100–500 sources. Beyond that, you need a search layer. At very large scale (thousands of documents), RAG has a structural advantage.
- Error compounding. If the LLM writes something subtly wrong into the wiki and it gets filed back, subsequent answers can build on that error. Periodic linting helps but doesn't eliminate this risk.
- Multi-user contribution is not native. The pattern was designed for a single researcher or a small team. Shared write access, governance, and role-based permissions require additional tooling.
- Discipline required. The system doesn't maintain itself without prompting. Someone has to run ingest passes, lint passes, and ensure the schema stays relevant. In a busy team, this can slip.
- No formal audit trail for RAG-style citation. The wiki can cite sources, but it doesn't preserve the precise document-chunk-to-answer traceability that compliance-heavy RAG implementations provide.

## Which is right for RDC?

The question isn't which is better in the abstract — it's which is better for RDC's actual situation.

RDC's knowledge landscape looks like this: a creative agency with roughly 30 people, several distinct client workstreams, significant institutional knowledge about clients and deliverable types, and a clear problem of fragmented files and siloed learning. The total document corpus is large but not enterprise-scale. The primary need is synthesis and institutional memory — making existing knowledge findable, shareable, and compounding — rather than precise retrieval from a specific document at a specific line.

This profile fits the LLM knowledge base pattern well — but the picture is more nuanced given what CYSTEMS has specifically proposed.

**What CYSTEMS's proposal actually covers.** In their March 2026 proposal to Chris Telfer, CYSTEMS identified three distinct use cases: RFP and proposal acceleration, SOW and contract automation, and business intelligence/reporting. These are not the same problem. Only the first maps directly to what either RAG or an LLM wiki primarily addresses. SOW automation is partly a knowledge retrieval problem and partly a structured document generation workflow. BI/reporting automation is a data pipeline and dashboard problem that neither architecture solves on its own.

Additionally, CYSTEMS builds specifically on Claude/Anthropic — not a generic RAG platform — and their closed-loop security model (no client data touching public AI models) is a genuine differentiator for RDC's NDA-sensitive Microsoft and government work. That security posture is not easily replicated with a self-managed file-based wiki.

The case for exploring the LLM wiki alongside the CYSTEMS evaluation:

1. The RFP and proposal use case — which is where the knowledge synthesis problem is most acute — can be prototyped with the LLM wiki in days, at negligible cost, using Claude you're already paying for. If it works, that's one of the three CYSTEMS use cases potentially solved before the discovery session.
2. The LLM wiki answer to "what has worked before for this client" or "what's our voice guide for Databricks" is better than what even a well-built RAG system returns, because synthesis has already happened rather than being re-derived on every query.
3. Transparency matters for a content team. Writers and designers need to be able to trust, read, and edit the knowledge they're working from — not query a black box.

The case for CYSTEMS specifically:

1. Their closed-loop security architecture directly addresses RDC's NDA and client confidentiality obligations in a way a self-managed wiki cannot without significant additional investment.
2. SOW automation and BI/reporting — if they can genuinely deliver on both — represent operational leverage well beyond what an LLM wiki provides.
3. They build on Claude, so there's no platform switching cost, and the team's existing Claude fluency transfers directly.
4. A completed system RDC owns, with training and defined handoff, is a different value proposition than a wiki the team maintains itself.

The practical recommendation: test the LLM wiki against the RFP/proposal use case before the discovery session. Run a real proposal through it. See how much of the knowledge synthesis problem it solves. Then walk into the CYSTEMS discovery session with a clear sense of what you're buying beyond what you can already do — which will sharpen the conversation and improve whatever decision comes out of it.

## Sources

- [Karpathy's llm-wiki GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [MindStudio: LLM Wiki vs RAG comparison](https://www.mindstudio.ai/blog/llm-wiki-vs-rag-markdown-knowledge-base-comparison)
- [Atlan: LLM Knowledge Base vs RAG: How They Differ](https://atlan.com/know/llm-knowledge-base-vs-rag/)
- [VentureBeat: Karpathy's LLM Knowledge Base architecture](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an)
- [RAGFlow: From RAG to Context — 2025 year-end review](https://ragflow.io/blog/rag-review-2025-from-rag-to-context)
- [NStarX 2026 enterprise RAG adoption analysis](https://blog.starmorph.com/blog/rag-techniques-compared-best-practices-guide)
- CYSTEMS x Red Door Collaborative proposal document (March 2026, confidential)
