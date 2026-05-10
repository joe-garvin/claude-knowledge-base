# Implementing an LLM knowledge base at Red Door Collaborative: a practical guide

*Research document for Red Door Collaborative | April 2026*

## Overview

This document translates the LLM knowledge base concept into a concrete implementation plan for Red Door Collaborative. It covers the folder structure, schema design, workflows for contributing and querying, the multi-user access model, role-based access controls, and the tooling stack.

The goal is a shared, compounding knowledge base that serves the full RDC team — in-house creative, embedded Azure and VSS teams, operations, and leadership — while respecting appropriate access boundaries between those groups.

## What the RDC knowledge base would contain

Before designing the system, it helps to be specific about what knowledge RDC actually needs to accumulate and share.

**Client knowledge:** Brand voice guides, messaging frameworks, past deliverable examples, client preferences and feedback patterns, SME knowledge, competitive landscape notes, and project post-mortems for each major account (Microsoft Azure, Databricks, City of Seattle, etc.).

**Craft and process knowledge:** What kinds of blog posts, ebooks, infographics, and scripts have worked and why. Prompts and workflows that have been effective in Claude. Writing and design guidelines by client and deliverable type. Lessons from production cycles — what caused delays, what made reviews smooth.

**Operational knowledge:** How work flows through the creative team. Who to contact for what. How decisions get made. Active project context for PMs and leads.

**AI and tooling knowledge:** What the team has tried with Claude, what worked, what didn't. Effective prompts by use case. Skill and workflow documentation.

**New business knowledge:** Past proposals, capabilities statements, pitch materials, and what has resonated with different types of prospects.

## Recommended folder structure

The RDC knowledge base follows the three-layer architecture: raw sources, wiki, and schema. A fourth layer — access tiers — addresses the RBAC requirements.

```
rdc-knowledge-base/
│
├── CLAUDE.md                    ← The schema: rules, conventions, workflow instructions
├── index.md                     ← Master index of all wiki pages (LLM-maintained)
├── log.md                       ← Append-only log of all operations (LLM-maintained)
│
├── raw/                         ← Immutable source material
│   ├── clients/
│   │   ├── microsoft-azure/     ← Briefs, transcripts, brand guides, past deliverables
│   │   ├── databricks/
│   │   ├── city-of-seattle/
│   │   └── [other clients]/
│   ├── craft/                   ← Articles, guides, reference material about writing/design
│   ├── ai-workflows/            ← Captured prompts, workflow notes, session outputs
│   ├── operations/              ← Process documents, onboarding materials, handbook excerpts
│   └── new-business/           ← Proposals, capabilities statements, pitch materials
│
├── wiki/                        ← LLM-generated and LLM-maintained knowledge pages
│   ├── clients/
│   │   ├── microsoft-azure/
│   │   │   ├── index.md         ← Azure client wiki index
│   │   │   ├── brand-voice.md
│   │   │   ├── deliverable-types.md
│   │   │   ├── key-contacts.md
│   │   │   ├── past-projects.md
│   │   │   └── lessons-learned.md
│   │   ├── databricks/
│   │   └── [other clients]/
│   ├── craft/
│   │   ├── blog-posts.md
│   │   ├── ebooks.md
│   │   ├── infographics.md
│   │   ├── scripts.md
│   │   └── writing-principles.md
│   ├── ai-workflows/
│   │   ├── effective-prompts.md
│   │   ├── skills-and-tools.md
│   │   └── workflow-templates.md
│   ├── operations/
│   │   ├── team-structure.md
│   │   ├── workflow-overview.md
│   │   └── tools-and-platforms.md
│   └── new-business/
│       ├── capabilities.md
│       ├── past-proposals.md
│       └── positioning.md
│
└── outputs/                     ← Generated reports, analyses, one-pagers, research
    ├── [date]-[topic].md
    └── ...
```

## The schema file (CLAUDE.md)

The CLAUDE.md is the most important file in the system. A starting template for RDC:

```markdown
# RDC Knowledge Base Schema

## What this is
Red Door Collaborative's shared institutional knowledge base.
Maintained by AI (Claude), fed by the RDC team.
The wiki is the organized layer. Raw/ is the source material. You write the wiki; humans read it.

## Who uses it
- Creative team (content, design, motion, video, PMs)
- Embedded teams (Azure, VSS)
- Operations and leadership (admin, finance, HR)
- Leadership (Chris, Jenny)

## How it's organized
- raw/ contains immutable source documents. Never modify these.
- wiki/ contains synthesized, interlinked knowledge pages. You own and maintain this.
- outputs/ contains generated analyses and one-pagers. These may be filed back into wiki/.
- index.md is a master catalog of all wiki pages, updated on every ingest.
- log.md is an append-only operation log. Format: ## [YYYY-MM-DD] action | description

## Wiki conventions
- Every page starts with a one-paragraph summary.
- Use [[page-name]] for internal links.
- Add YAML frontmatter: tags, last_updated, source_count.
- Maintain an index.md within each sub-folder for that section.
- When ingesting a source, update: the summary page, the section index, the master index, the log.
- When a new source contradicts an existing page, flag the contradiction prominently.

## Access tiers (see RBAC section below)
- Tier 1: Company-wide — general operations, craft knowledge, AI workflows, public-facing materials
- Tier 2: Client-specific — client wiki pages, deliverable examples, project history
- Tier 3: Sensitive — financial data, HR, new business pipeline, strategic planning

## Ingest workflow
1. Source is placed in raw/ by a team member
2. Notify Claude: "New source in raw/clients/microsoft-azure/[filename]. Please ingest."
3. Claude reads source, writes/updates wiki pages, updates index, appends to log
4. Review the changes in Obsidian or the file viewer

## Query workflow
1. Ask your question in Claude
2. Claude reads index.md, identifies relevant pages, reads them, synthesizes an answer
3. If the answer is valuable, ask Claude to file it as a new page in outputs/ or wiki/

## Lint (run monthly)
Ask Claude: "Run a health check on wiki/. Find contradictions, orphan pages,
unsupported claims, stale content, and gaps. Write a report to wiki/lint-report.md."
```

## Multi-user access: how the whole team contributes and queries

The LLM wiki was designed for individual use. Adapting it for a team of 30+ across multiple contexts requires deliberate choices about how people contribute, how the wiki stays coherent, and how queries work.

### Option A: Shared Git repository (recommended for RDC)

Host the knowledge base as a Git repository — either on GitHub (already used by RDC) or on an internal server. All team members clone the repo. They contribute by adding files to raw/ and committing them. The "wiki compiler" (Claude, run by a designated maintainer or via automation) processes new raw files and updates the wiki. The wiki is the shared, authoritative output.

**Advantages:** Version history on every change. Branch-and-merge for experimental ingests. Existing RDC GitHub infrastructure can be used. Transparent — you can see who added what and when. The log.md provides an additional audit layer.

**Challenges:** Requires team members to use Git, which adds friction for non-technical contributors. Merge conflicts in wiki files are possible if multiple people trigger ingest passes simultaneously.

**Mitigation:** A shared intake form or Slack channel where people post sources they want ingested (rather than directly committing to raw/) keeps the workflow accessible. A designated "wiki steward" runs the actual ingest passes.

### Option B: Shared folder (SharePoint or Box)

The raw/ folder lives in a shared SharePoint document library or Box folder. Team members add documents to the appropriate subfolder. The wiki is generated and stored in a separate SharePoint folder or Box folder. A designated maintainer (or automated task) runs ingest passes when new content arrives.

**Advantages:** No Git required. Uses tools the team already has. Familiar file-browser interface for contribution.

**Challenges:** No native version control (though SharePoint has version history). Multiple people triggering Claude to ingest simultaneously could create conflicts. Less traceability than Git.

**Recommendation:** For RDC's current tooling setup, SharePoint is the path of least resistance for broad team participation, with Git as the stronger option for the creative and tech-savvy subset. A hybrid works too: Git for the wiki itself (version-controlled, authoritative), SharePoint for the intake pipeline (where people drop new sources), with a maintainer bridging the two.

### Querying for all team members

Each team member queries the knowledge base through Claude, with the wiki folder accessible in their Claude session. No shared server required. Team members just need to have the wiki files available to their Claude session — either via the shared folder (Cowork/file access), a mounted drive, or a copy they keep current.

This means queries are private by default — each person's Claude conversation is their own. The shared knowledge is in the files; the conversations are individual.

## Role-based access control (RBAC)

This is the hardest problem in adapting the LLM wiki for a team context. The pattern doesn't have built-in access controls — it's files on a filesystem. RBAC has to be implemented at the file system and schema level.

### Three-tier access model for RDC

**Tier 1 — Company-wide (all staff):** General operations knowledge, craft and writing principles, AI workflow documentation, RDC brand materials, team structure, public-facing capabilities. All team members can read and contribute to Tier 1 sections.

**Tier 2 — Client-specific (by workstream):** Each client's wiki section is accessible only to the team members working on that account. Azure team members have access to the Azure wiki. Databricks writers have access to the Databricks wiki. Creative team leads have access to all client wikis. This is enforced at the folder level.

**Tier 3 — Leadership/sensitive (Chris, Jenny, Amy, select leads):** Financial data, HR documents, new business pipeline, strategic planning, and competitive intelligence. Stored in a separate, restricted folder not visible to general staff.

### Implementation approach

**Folder-level access on the shared drive.** SharePoint and Box both support folder-level permission settings. The Tier 3 folder is restricted by SharePoint/Box permissions to leadership only. Tier 2 client folders are restricted to the relevant account teams plus leads. Tier 1 is open to all.

**Separate CLAUDE.md files by tier.** The Tier 3 folder has its own schema that governs the sensitive wiki. The Tier 1/2 CLAUDE.md does not reference Tier 3 content.

**Query scoping.** When a team member queries Claude, their Claude session only has access to the wiki folders they're permitted to see. This is enforced by what folder they've pointed Claude at — not by a system-level filter. This means the access control lives in the folder permissions, not in Claude itself.

**Important caveat:** This approach relies on folder-level permissions enforced by the file system or shared drive platform. It does not provide the same rigorous enforcement as platform-level RBAC in an enterprise RAG system. For genuinely sensitive data (HR, financials), additional safeguards should be considered — or that data should remain in purpose-built systems rather than the wiki.

### Practical tiering for RDC roles

| Role | Tier 1 access | Tier 2 access | Tier 3 access |
|---|---|---|---|
| All creative team | Yes | Client-specific | No |
| Embedded Azure team | Yes | Azure wiki only | No |
| VSS team | Yes | VSS wiki only | No |
| Creative leads (Naj, Justine, Joy, Nathan) | Yes | All client wikis | No |
| PMs (Karin, Silas) | Yes | All client wikis | No |
| Account managers (Amy, Erin) | Yes | Their accounts | Partial |
| Operations (Ashley, Brandon) | Yes | No | Partial |
| Leadership (Chris, Jenny) | Yes | All | Yes |

## Step-by-step implementation plan

### Phase 1: Foundation (week 1–2)

1. Designate a wiki steward — the person responsible for running ingest passes, maintaining the schema, and doing monthly lint checks. In the short term, this is likely Joe or another Claude-fluent team member.

2. Set up the folder structure on SharePoint (or GitHub, depending on access model decision). Create the raw/, wiki/, and outputs/ directories with the appropriate sub-structure.

3. Write the initial CLAUDE.md schema. Start with the template above and refine it with input from Justine (content standards), Naj (workflow), and Chris (priorities).

4. Set folder permissions. Configure Tier 1 (all staff), Tier 2 (by account), and Tier 3 (leadership) access in SharePoint or Box.

5. Seed the raw/ folder with 10–20 existing documents that represent the most valuable institutional knowledge RDC already has: a client brand voice guide, a few past project post-mortems, the RDC overview and org documents, the most useful AI prompts and workflows.

### Phase 2: Initial wiki build (week 2–3)

6. Run the first ingest pass. Point Claude at the raw/ folder and run: *"Read all sources in raw/. Build the wiki following the conventions in CLAUDE.md. Start with index.md, then create pages for each major section. Link related topics."*

7. Review the wiki with Naj, Justine, and at least one PM. Identify gaps, errors, and priorities for the next round of ingestion.

8. Refine the CLAUDE.md schema based on what the initial build revealed about your domain structure.

### Phase 3: Team onboarding (week 3–4)

9. Write a one-page "how to use the wiki" guide for the team. Keep it simple: how to add a source, how to ask a question, who to notify when you want something ingested.

10. Introduce the wiki to the creative team in a short team meeting. Have the wiki steward demonstrate a live query session.

11. Open the intake pipeline: a Teams channel, a SharePoint form, or a simple email alias where team members can submit sources for ingestion.

### Phase 4: Steady state (ongoing)

12. Weekly ingest passes: the wiki steward processes new submissions from the intake pipeline.

13. Monthly lint passes: Claude health-checks the wiki for contradictions, orphan pages, and gaps.

14. Quarterly schema review: is the CLAUDE.md still reflecting how the team uses the wiki? Update it as the system evolves.

15. Log review: periodically review log.md to see what's been ingested, what questions have been asked, and where the wiki is most actively used.

## Tooling stack for RDC

**Storage:** SharePoint (primary, for team access) or GitHub (for version control). Either works; the choice depends on how technical the steward and contributors are comfortable being.

**Frontend for reading:** Obsidian (free, local-first) for the wiki steward and power users. For general staff, reading wiki pages in SharePoint's document viewer is sufficient. Obsidian's graph view is useful for the steward to see the shape of the knowledge base.

**LLM agent for all operations:** Claude (via Cowork on Desktop, Claude Code, or the Claude API). All ingest, query, and lint operations run through Claude.

**Intake pipeline:** A dedicated Teams channel (#wiki-submissions) or SharePoint intake folder where team members drop sources they want ingested.

**Search (optional, later):** If the wiki grows to a scale where index-based navigation isn't sufficient, qmd (a local hybrid BM25/vector search tool for markdown files) can be added. This is not needed at RDC's current scale.

**Browser extension:** The Obsidian Web Clipper converts any web page into a markdown file ready for the raw/ folder. Useful for the steward and any team member who wants to contribute web-sourced content.

## What the wiki looks like in use

A few concrete examples of how RDC team members would use the knowledge base day-to-day:

**Joe is starting a new Databricks blog post.** He asks Claude: *"What do we know about Databricks' brand voice and the types of content they've approved in the past?"* Claude reads the Databricks wiki section and returns a synthesis of brand voice guidelines, past deliverable examples, and lessons from previous review cycles — all in one response, grounded in the wiki.

**Karin is onboarding a new designer to the Azure account.** She asks Claude: *"Give me an overview of how Azure account work flows, who the key contacts are, and what the most common deliverable types look like."* Claude synthesizes the Azure wiki's team structure, workflow, and deliverable type pages.

**Justine wants to capture a lesson from a difficult client review.** She writes a brief note about what went wrong and what fixed it, drops it in the Teams intake channel. The steward ingests it, and Claude adds it to the relevant client wiki's lessons-learned page.

**Chris is prepping for a new business pitch.** He asks Claude: *"What have our most successful proposals for tech companies had in common?"* Claude reads the new-business wiki section and synthesizes patterns from past proposals — what language landed, what differentiated RDC, what fell flat.

## Sources

- [Karpathy's llm-wiki GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- ["Claude + Obsidian should be illegal"](https://x.com/defileo/status/2042241063612502162) (@defileo, April 9, 2026)
- [MindStudio: What Is Andrej Karpathy's LLM Wiki?](https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code)
- [Atlan: LLM Knowledge Base — Definition, Components, and Enterprise Use](https://atlan.com/know/what-is-an-llm-knowledge-base/)
- [Collaborative Memory RBAC research](https://arxiv.org/html/2505.18279v1) (arXiv 2505.18279)
- [AnythingLLM](https://anythingllm.com/)
- RDC operations and pain points context document (internal)
