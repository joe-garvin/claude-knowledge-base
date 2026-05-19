# Building an autonomous knowledge base agent with Claude Code and Obsidian

A general-purpose guide derived from building the LLM Impacts research agent — documenting the full process from concept through implementation, including refinements discovered during actual use. Intended as a replicable template for knowledge bases on other subjects.

---

## What this system is

A Claude Code agent that autonomously researches a defined topic, evaluates sources against a calibrated taste profile, ingests keepers into a structured Obsidian vault, synthesizes findings across a compounding wiki, and reports to you on a defined cadence. The key property is that it compounds — each new source doesn't just add a page, it updates existing concept pages, adds cross-references, and strengthens the connective tissue of the knowledge base over time.

This is not a feed reader or a clipping tool. The difference is synthesis. A feed reader gives you more things to read. This system builds a body of knowledge you can query.

---

## Phase 1: scoping the agent

Before writing any configuration, you need to define three things clearly. Rushing this step produces a CLAUDE.md that's either too vague to be useful or too narrow to catch what matters.

### Define the topic and its edges

Write a plain-language statement of what the agent should track. Then list the sub-strands explicitly — every angle or dimension of the topic you care about. Be honest about whether you want a wide or narrow net at this stage. Wide nets are better for early-stage research where you're still learning the shape of a field; narrow nets are better when you already know exactly what you're looking for.

For the LLM Impacts agent, the decision was to keep the net intentionally wide across five distinct strands (cognitive effects, labor displacement, aesthetic changes, epistemological effects, organizational dynamics) and let scope refinement happen through supervised runs rather than pre-filtering.

Useful questions to ask yourself:
- What would I definitely want to know about?
- What would I definitely not care about?
- Is there a particular tension or question driving my interest, or is this more general accumulation?
- Am I building toward a specific output (a report, a writing project, a position) or building ongoing situational awareness?

### Define your source quality bar

Think in terms of: what makes a source worth reading vs. worth skipping? This is your taste profile. It should be specific enough that the agent could explain why it included or excluded a given piece.

Useful dimensions to define:
- **Originality** — original argument/findings vs. summary/explainer
- **Influence** — does it start conversations or add a new layer to existing ones?
- **Credibility** — outlet standards, author credentials, institutional backing
- **Specificity** — concrete data and named experience vs. abstract speculation

Also define explicit reject criteria. Naming what you don't want is as useful as naming what you do.

### Define source types and outlets

Build a tiered list: what types of sources take priority, and within each type, which specific outlets or databases. Be specific. "Good journalism" is not actionable; "New Yorker, Atlantic, 404 Media, Nieman Lab" is.

Tiers typically look like:
1. Academic preprints and peer-reviewed papers (arXiv, SSRN, PsyArXiv, ACM, etc.)
2. Longform journalism and cultural criticism (named outlets)
3. Newsletters and Substack essays with documented reach (named authors/publications)
4. Institutional reports with original data (named organizations)

The outlet list will grow through use. Start with what you know and expand as the agent surfaces new sources worth adding to the rotation.

---

## Phase 2: calibrating scope through examples

If you already have sources you've found relevant, share them before writing the CLAUDE.md. This is the fastest way to calibrate the agent's taste profile — more precise than describing preferences in the abstract.

For the LLM Impacts agent, this meant reading a folder of existing clippings (academic preprints, New Yorker criticism, longform reportage, cultural commentary) and extracting the pattern: empirically grounded, takes a clear position, adds something to the conversation, valued at both the macro level (population-level language change) and the granular/experiential level (what it feels like from inside a disrupted creative practice).

If you don't have example sources yet, you can skip this step and rely on the written taste profile — but expect to spend more time in supervised mode correcting scope.

Existing sources you share for calibration should go into a pre-seeded exclusion list in the CLAUDE.md. The agent can ingest them as founding wiki content, but should never re-surface them as "new finds" in future digests.

---

## Phase 3: designing the vault structure

The Karpathy pattern is the right foundation for most knowledge bases of this type:

```
[vault name]\
  raw\              ← immutable source clippings; never modified after ingest
  wiki\
    index.md        ← catalog of all wiki pages with one-line summaries
    log.md          ← append-only chronological record of all operations
    concepts\       ← thematic articles, one per major concept or strand
    sources\        ← one summary page per ingested source
    entities\       ← people, outlets, institutions, orgs worth tracking
    synthesis\      ← evolving cross-strand analysis and thesis notes
  weekly\           ← digest notes at whatever cadence you've chosen
  CLAUDE.md         ← agent configuration; the agent reads this on every run
```

Key principles behind this structure:

**`raw\` is immutable.** Everything the agent clips goes here and is never modified. This is your source of truth if something gets corrupted or misrepresented downstream.

**`wiki\` is the agent's domain.** The human rarely edits wiki files directly. The agent owns them, maintains them, and keeps them consistent.

**`index.md` and `log.md` are the backbone.** Index is how both you and the agent navigate the wiki. Log is the audit trail — greppable, append-only, never edited. If something went wrong, the log tells you when and what.

**Concepts compound.** The most important structural property: when a new source touches an existing concept, the concept page gets updated. Don't let concept pages go stale. This is what makes the wiki a knowledge base rather than a pile of summaries.

**Adapt the structure to your use case.** A knowledge base for a specific writing project might not need an entities folder. One tracking a fast-moving regulatory landscape might need a `timeline\` folder instead of `synthesis\`. The folder structure should reflect how you'll actually use the material.

---

## Phase 4: writing the CLAUDE.md

This is the agent's single source of truth. Every time it runs, it reads this file. It should contain everything the agent needs to operate independently — research mandate, taste profile, vault structure, all workflows, conventions, and operating principles.

### Essential sections

**Identity and scope** — what the agent is, what it's not, what it tracks, and where everything lives (project directory and vault path). Be explicit that it is not a general assistant.

**Research mandate** — the topic and all sub-strands. If you want a wide net, say so explicitly.

**Taste profile** — quality signals, source tiers with named outlets, reject criteria.

**Vault structure** — the folder map with annotations explaining each folder's purpose.

**Core workflows** — step-by-step instructions for every operation the agent performs. Don't assume the agent will infer what you mean. Spell out each step. Ambiguous instructions produce inconsistent behavior.

**Index and log conventions** — exact format examples for both files. The agent needs to know what these files should look like so it maintains them consistently across runs.

**Pre-seeded exclusion list** — sources already known to you that shouldn't appear as new finds.

**Operating principles** — high-level rules that apply across all workflows (cross-link aggressively, prefer depth over breadth, flag contradictions, etc.).

**Human context** — why this research matters, what it's for, what tensions or stakes are involved. This is optional but useful: it gives the agent enough grounding to make better judgment calls about borderline sources.

### Workflows to include (adapt as needed)

**Primary research workflow** — the main recurring operation: search, evaluate, ingest, write digest, notify. Break each step into explicit sub-steps.

**Scope confirmation mode** — a supervised phase for the first N runs where the agent presents candidates for review instead of ingesting autonomously. Always include this for new knowledge bases. It costs little and prevents the agent from building on a miscalibrated foundation.

**Manual ingest workflow** — handling files you drop into `raw\` yourself. The agent should scan for unprocessed files at the start of every run and ingest them before doing new research. Without this, manually added files pile up unprocessed indefinitely.

**Query workflow** — how the agent responds when you ask it questions against the wiki. Should include: reading index first, drilling into relevant pages, synthesizing with citations, offering to file substantive answers as synthesis pages.

**Lint workflow** — periodic maintenance: orphan pages, concept pages that need splitting, contradictions, data gaps, missing cross-references. Run monthly or on demand.

### PDF handling

If your knowledge base will include PDFs in `raw\`, document the reading method explicitly in the CLAUDE.md. Don't assume the agent will figure it out.

In the LLM Impacts implementation, the native file-reading approach failed because `pdftoppm` (from poppler) wasn't installed. The PDF MCP tool (`mcp__PDF_Tools_-_View__Fill__Merge__Split__Manage_Pages__Extract__read_pdf_content`) was already configured and worked reliably. The lesson: test your PDF reading method early and document the working approach in CLAUDE.md before you have a backlog of unread PDFs.

---

## Phase 5: implementation

### Directory and vault setup

1. Create the Claude Code project directory (e.g. `C:\Claude\[project-name]\`)
2. Place CLAUDE.md in the project root
3. Create a new Obsidian vault at your chosen path (e.g. `C:\Obsidian\[Vault Name]\`)
4. Manually create the folder structure inside the vault
5. Create stub `wiki\index.md` and `wiki\log.md` with minimal placeholder content — the agent needs these files to exist before it can update them

Stub `index.md`:
```markdown
# Wiki index

Last updated: —

## Concepts

## Sources

## Entities

## Synthesis
```

Stub `log.md`:
```markdown
# Log

## [setup] Vault initialized
```

### First session

Open Claude Code (desktop app or terminal) with the project directory as the working directory. The agent will find CLAUDE.md automatically.

First message to send:
> Please read your CLAUDE.md and confirm you understand your research mandate, the vault structure, and the difference between scope confirmation mode and full autonomous mode. Don't start any research yet — just confirm your understanding and tell me if anything is unclear.

Read the response. Clarify anything that looks wrong before proceeding.

### Seeding with existing sources

If you have relevant sources already collected, ask the agent to ingest them as founding wiki content in the first session:
> Before running any new research, I want to seed the wiki with sources I've already collected. They live at [path]. Please read all the notes in that folder, ingest each one as a seed source, create initial concept pages based on what you find, and update index.md and log.md as you go. These should not appear as new finds in future digests — treat them as the wiki's founding collection.

This gives the wiki a real foundation from day one and calibrates the agent's sense of what's already known before it starts searching.

### Supervised mode (first 2–3 runs)

Trigger the first scope check run:
> Run your first scope check as defined in CLAUDE.md. Search for new sources, evaluate them against the taste profile, and write a scope-check file to weekly\scope-check-W01.md. Do not ingest anything yet. When done, show me what you found and ask for my feedback before proceeding.

Review the scope check file in Obsidian. Redirect as needed. Repeat for 2–3 runs until you're confident the agent is finding the right things, then tell it to proceed to full autonomous mode.

### Automation (after supervised mode)

For recurring autonomous runs, use Windows Task Scheduler (Windows) or cron (Mac/Linux).

Create a batch file (Windows example):
```batch
@echo off
cd C:\Claude\[project-name]
claude --print "Run your weekly research workflow as defined in CLAUDE.md. We are past scope confirmation — proceed to full ingest, write the weekly digest, and fire the completion notification." --max-turns 50
```

For notifications without Telegram: a Windows toast notification via PowerShell is the simplest option. The agent fires it at the end of each run, prompting you to open Claude Code and review the digest. No back-and-forth required — the digest is already written in Obsidian when you arrive.

---

## Phase 6: refinements discovered in practice

These are issues that emerged during actual use of the LLM Impacts agent and required CLAUDE.md updates. Worth anticipating for new knowledge bases.

### Filename date precision

The CLAUDE.md specified `YYYY-MM-DD` as the filename format for raw clippings. During a standardization pass, several sources had only month or year-level date precision — no exact day available. The instruction as written would have required fabricating a date.

**Fix:** specify fallback formats explicitly. Use `YYYY-MM` when only the month is known, `YYYY` when only the year is known. Never fabricate a date.

### Entity page creation threshold

The original entity page instruction used the word "notable" without defining it. After 73+ sources ingested, only 4 entity pages existed — the undefined threshold meant entity pages were being skipped systematically.

**Fix:** replace vague language with explicit trigger criteria. Create an entity page when: (a) the outlet is in the mandatory rotation list; (b) the researcher's work is primary to a concept page, not just cited in passing; (c) the institution has significant ongoing research or policy weight; (d) the entity has 2 or more sources in the wiki. Also specify: if a page already exists, add the new source to its Works list; do not create pages for one-off sources from non-rotation outlets.

**General lesson:** any instruction that relies on an undefined threshold ("notable," "significant," "important") will be applied inconsistently. Replace with concrete, binary criteria wherever possible.

### Source rotation table expansion

The initial CLAUDE.md named specific outlets in prose. Through use, the outlet list grew and required better organization. Replacing prose outlet lists with structured tables (outlet, URL, why it's in the rotation) makes the list easier to scan, easier to update, and gives the agent better context for why each source is trusted.

The LLM Impacts rotation expanded from ~8 outlets to ~17 across journalism, newsletters, academic databases, and institutional reports — with different check frequencies (weekly vs. quarterly) for different tiers.

**General lesson:** start with what you know, then grow the rotation as the agent surfaces new sources worth adding. Build the table structure early so expansion is easy.

### Manual ingest gap

The initial CLAUDE.md had no instruction for handling files manually dropped into `raw\`. Without this, files the human added between runs would sit unprocessed indefinitely.

**Fix:** add a manual ingest workflow that runs at the start of every weekly run, before new research begins. The agent scans `raw\` for files without a corresponding `wiki\sources\` page and ingests them first. Also add on-demand triggering: if the human says "check raw for unprocessed files," run immediately.

---

## Adaptations for different knowledge base types

The LLM Impacts agent runs weekly, autonomously, with broad scope and recurring research. Other knowledge bases may need different configurations:

**Manually triggered, no recurring schedule** — remove Task Scheduler setup entirely. Remove scope confirmation mode timing language. The human triggers runs by opening Claude Code and saying "run a research pass." Useful for slower-moving topics or when you want full control over when research happens.

**Narrow scope, high precision** — tighten the taste profile, reduce the number of outlets in the rotation, add more explicit reject criteria. Consider adding a "this is not in scope" section to the mandate alongside the "in scope" list.

**Output-oriented** (building toward a specific deliverable) — add a `drafts\` folder to the vault structure. Add a synthesis workflow that periodically generates draft sections of the target deliverable based on accumulated wiki content. The lint workflow should also check for coverage gaps relative to the deliverable's outline.

**Multiple agents, one vault** — possible but requires careful coordination. Each agent should have a clearly delineated domain within the vault (separate concept folders, separate digest locations) and explicit instructions not to modify the other agent's files. Shared `index.md` and `log.md` work fine as long as both agents append rather than overwrite.

**No Obsidian** — the vault structure works as a plain folder of markdown files in any location. Obsidian is optional; it just provides graph view, backlinks, and search on top of the same files.

---

## The interview process

One of the most useful parts of building the LLM Impacts agent was the structured interview before writing any configuration. Rather than starting from the CLAUDE.md directly, a series of questions established: topic scope, source quality bar, outlet list, research cadence, knowledge base structure, supervision preferences, and system architecture. Only after all of these were settled was the CLAUDE.md written.

This produced a cleaner first draft than writing the CLAUDE.md speculatively and refining from there. For new knowledge bases, the same interview process is worth running — either with Claude or with yourself in writing — before touching the configuration file.

Core questions to answer before writing CLAUDE.md:
- What is the topic, and what are its sub-strands?
- Wide net or narrow net at this stage?
- What makes a source worth reading? What makes it worth skipping?
- Which specific outlets and databases should the agent monitor?
- How often should the agent run, and how should it report?
- What's the primary organizing logic for the knowledge base (thematic, chronological, by source type)?
- How many supervised runs before going autonomous?
- How will you receive notifications?
- Where will the project directory and vault live?
- Do you have existing sources to seed the wiki?

---

## Files to create

For any new knowledge base agent, the minimum set of files:

| File | Location | Purpose |
|------|----------|---------|
| `CLAUDE.md` | Project root | Agent configuration; read on every run |
| `wiki\index.md` | Vault | Navigation catalog; updated on every ingest |
| `wiki\log.md` | Vault | Append-only audit trail |
| `weekly-run.bat` | Project root | Batch file for Task Scheduler (if automating) |

Everything else — concept pages, source pages, entity pages, synthesis notes, weekly digests — is written and maintained by the agent.
