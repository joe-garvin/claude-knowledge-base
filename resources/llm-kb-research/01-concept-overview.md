# LLM knowledge bases: concept overview

*Research document for Red Door Collaborative | April 2026*

## Origin and context

On April 2, 2026, Andrej Karpathy — former director of AI at Tesla, co-founder of OpenAI, and one of the most widely followed voices in AI — posted a [thread on X](https://x.com/karpathy/status/2039805659525644595) describing how he was building personal knowledge bases using LLMs. The post went immediately viral, accumulating hundreds of thousands of engagements within days. He followed it with [a GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) formalizing the idea as a pattern he called "LLM Wiki."

Several converging conditions made Karpathy's idea land the way it did. Context windows on frontier models had grown large enough to hold hundreds of pages at once. LLMs had become good enough at structured reading and writing tasks. And a growing number of people were frustrated with the complexity and cost of retrieval-augmented generation (RAG) systems — the dominant approach for connecting LLMs to large bodies of knowledge.

Karpathy's insight was that for many use cases, RAG is the wrong solution to the right problem. His alternative: have the LLM itself build and maintain a structured, interlinked knowledge base — a wiki — rather than having it rediscover knowledge from raw documents every time someone asks a question.

## The core idea

Most people's experience with LLMs and documents follows the RAG pattern: you upload files, the system retrieves relevant chunks at query time, and the LLM generates an answer from those chunks. Every question starts from scratch. Nothing accumulates. If you ask a question that requires synthesizing five documents, the system has to locate and piece together the relevant fragments each time.

The LLM knowledge base pattern works differently. Instead of retrieving from raw documents at query time, an LLM incrementally builds and maintains a persistent, structured wiki — a collection of interlinked markdown files that sits between you and your raw sources. When you add a new source, the LLM reads it, integrates the key information into the existing wiki, updates relevant pages, flags where new data conflicts with old claims, and cross-references related concepts. The knowledge is compiled once and kept current — not re-derived on every query.

As Karpathy put it in his gist: "The wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read. The wiki keeps getting richer with every source you add and every question you ask."

This is the fundamental shift: from retrieval to accumulation.

## Three-layer architecture

The LLM wiki pattern has three distinct layers:

**Raw sources.** The original documents, articles, papers, transcripts, images, and data files you collect. These are immutable — the LLM reads from them but never modifies them. This is the source of truth.

**The wiki.** A directory of LLM-generated markdown files: summaries, entity pages, concept pages, comparisons, an index, and a log. The LLM owns this layer entirely. It creates pages, updates them as new sources arrive, maintains cross-references, and keeps everything consistent. You read it; the LLM writes it.

**The schema.** A configuration document — typically called CLAUDE.md (for Claude Code) or AGENTS.md (for other agents) — that tells the LLM how the wiki is structured, what conventions to follow, and what workflows to use when ingesting sources, answering questions, or doing maintenance. This file is co-evolved between you and the LLM as you figure out what works for your domain. It's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot.

## The three operations

**Ingest.** You drop a new source into the raw collection and tell the LLM to process it. A typical flow: the LLM reads the source, discusses key takeaways, writes a summary page in the wiki, updates the index, updates relevant entity and concept pages, and appends an entry to the log. A single source often touches 10–15 wiki pages. The LLM surfaces unexpected connections and flags contradictions you might not have noticed.

**Query.** You ask questions against the wiki. The LLM reads the index first to identify relevant pages, then drills into them and synthesizes an answer with citations. Importantly, good answers can be filed back into the wiki as new pages — so your explorations compound in the knowledge base just like ingested sources do. Insights don't disappear into chat history.

**Lint.** Periodically, you ask the LLM to health-check the wiki: find contradictions between pages, locate orphan pages with no inbound links, identify concepts mentioned but lacking their own page, flag claims that newer sources have superseded, and suggest new articles or sources to investigate. This keeps the wiki healthy as it grows.

## Two special files

**index.md** is content-oriented. It's a catalog of everything in the wiki — each page listed with a link and a one-line summary, organized by category. The LLM reads the index first on every query to find relevant pages, then drills in. This works well at moderate scale (roughly 100 sources, hundreds of pages) without requiring embedding-based retrieval infrastructure.

**log.md** is chronological. It's an append-only record of all ingests, queries, and lint passes. Structured entries make the log parseable with simple tools. The log gives the LLM a timeline of the wiki's evolution and helps it understand what's been done recently.

## The two camps: where this fits in the AI memory landscape

Karpathy's tweet accelerated a conversation that was already underway. In April 2026, a widely-circulated analysis identified 450+ GitHub repos tagged "agent-memory" and 460+ tagged "context-management" — and characterized them as belonging to two fundamentally different paradigms.

**Camp 1: Memory backends.** These tools — [Mem0](https://github.com/mem0ai/mem0) (53k stars), [MemPalace](https://github.com/MemPalace/mempalace) (46k stars), [Supermemory](https://github.com/supermemoryai/supermemory) (22k stars) — extract facts from conversations, store them in vector databases, and retrieve relevant facts at query time. They optimize for recall: can the system find the right fact? The loop is: conversation happens → facts extracted → stored in DB → retrieved at next query. Nothing gets directly edited. Memories sit as flat entries with no synthesis.

**Camp 2: Context substrates.** These tools — [OpenClaw](https://github.com/openclaw/openclaw), [Zep](https://www.getzep.com/), [MemSearch](https://github.com/zilliztech/memsearch) (by Zilliz), [TrustGraph](https://github.com/trustgraph-ai/trustgraph) — maintain structured, human-readable context that accumulates across sessions. Nothing gets "extracted." The context is the files. The agent reads them, works within them, writes back to them, and the whole thing compounds over time. They optimize for compounding: does the system get better over time?

LLM knowledge bases as Karpathy describes them are firmly in Camp 2. The intelligence is in accumulation, not retrieval.

A telling signal from the market: [Zep](https://www.getzep.com/), a funded company with 4.4k stars, recently rebranded from "memory" to "context engineering." A company that built retrieval infrastructure decided the right word for what they were building was not "memory" — it was "context." That conceptual shift is propagating across the ecosystem.

## The ecosystem in April 2026

Since Karpathy's tweet, the space has expanded rapidly across several categories:

**Tooling for individuals:** The simplest implementations are just folders, markdown files, and a CLAUDE.md schema. Karpathy himself keeps his schema "super simple and flat." The [Obsidian Web Clipper](https://obsidian.md/clipper) browser extension converts any web page into a markdown file for the raw/ folder. The [qmd](https://github.com/tobi/qmd) search tool adds hybrid BM25/vector search over markdown files for larger wikis. [Claude Code](https://claude.ai/code) (or any LLM agent with file access) handles all wiki maintenance.

**Companies building on the pattern:**

- [Hyperspell](https://www.hyperspell.com/) bills itself as "a brain for your company" — a context graph built from connected tools (documents, emails, calendars, transcripts) exposed as a filesystem any agent can read.
- [Membase](https://membase.so/) positions as a personal memory layer for AI agents, MCP-compatible, connecting context across sessions and apps.
- [ALIVE](https://alivecontext.com/) builds a structured context substrate with "walnuts" as portable context containers — file-native, agent-agnostic, zero infrastructure dependencies.
- [TrustGraph](https://github.com/trustgraph-ai/trustgraph) introduces "Context Cores" — portable, versioned bundles treating context like code: version it, test it, promote it, roll it back.

**GitHub projects:**

- [LLM Wiki v2](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2) (rohitg00) extends Karpathy's pattern with lessons from building agentmemory
- [OpenClaw](https://github.com/openclaw/openclaw)'s dreaming system — background consolidation of context through light sleep, REM, and deep sleep phases
- [Thoth](https://github.com/siddsachar/Thoth) — a knowledge graph with 10 entity types, 67 typed relations, and a nightly dream cycle for duplicate merging, enrichment, and relationship inference

**Platforms:**

- [Obsidian](https://obsidian.md/) (free, local-first markdown IDE with graph view) has become the de facto "frontend" for personal LLM wikis
- [Claude Code](https://claude.ai/code) is the dominant "agent" pairing for file-based wiki maintenance
- [AnythingLLM](https://anythingllm.com/) supports multi-user shared workspace access with RBAC for teams
- [Tolaria](https://tolaria.md/) — a purpose-built markdown knowledge base editor designed around the LLM wiki workflow

## Why this works

The tedious part of maintaining a knowledge base has never been the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the perceived value.

LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in a single pass. The wiki stays maintained because the cost of maintenance is near zero.

The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else.

This connects to a vision Vannevar Bush articulated in 1945 — a personal, curated knowledge store called the Memex, where the connections between documents would be as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. That's now solved.

## Scale and limits

The LLM wiki pattern works well at what Karpathy calls "small scale" — roughly 100 sources and hundreds of pages, or around 400,000 words of wiki content. At this scale, reading the index and drilling into relevant pages is enough. No embedding infrastructure needed.

As the wiki grows toward thousands of documents, the index-based approach begins to strain. This is where the pattern either graduates to a lightweight search layer (like [qmd](https://github.com/tobi/qmd)) or where true RAG starts to make sense. The crossover point depends on the use case, but most practitioners identify it in the range of a few hundred to a few thousand documents.

For a company like RDC — a 30-person agency managing several distinct client workstreams — the scale is comfortably within the range where this pattern works without additional infrastructure.

## Sources

- [Karpathy's original tweet](https://x.com/karpathy/status/2039805659525644595) (x.com/karpathy, April 2, 2026)
- [Karpathy's llm-wiki GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [VentureBeat: Karpathy's LLM Knowledge Base architecture](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an)
- [MindStudio: LLM Wiki vs RAG comparison](https://www.mindstudio.ai/blog/llm-wiki-vs-rag-markdown-knowledge-base-comparison)
- [Atlan: LLM Knowledge Base vs RAG](https://atlan.com/know/llm-knowledge-base-vs-rag/)
- [DAIR.AI Academy: LLM Knowledge Bases](https://academy.dair.ai/blog/llm-knowledge-bases-karpathy)
- ["I Went Through Every AI Memory Tool I Could Find"](https://x.com/witcheer/status/2044456778843238689) (@witcheer, April 15, 2026)
- [Collaborative Memory RBAC research](https://arxiv.org/html/2505.18279v1) (arXiv 2505.18279)
- [Hyperspell](https://www.hyperspell.com/)
- [Membase](https://membase.so/)
