---
name: databricks-blog
description: Write Databricks blog posts following editorial standards, voice, and a structured multi-stage workflow. Use this skill whenever the user is working on a Databricks blog post, mentions a Databricks blog brief or outline, asks to draft or revise a Databricks article, or references the Databricks blog workflow. Trigger even if the user just says "I have a Databricks brief" or "let's do the next Databricks post" — any signal that Databricks blog writing work is happening should invoke this skill.
---

# Databricks blog post workflow

This skill governs the full process of drafting Databricks blog posts from a creative brief, following editorial standards, voice guidelines, and a structured multi-stage workflow with explicit approval gates.

Two workflow variants exist depending on what the brief contains:
- **Variant A** — Brief includes source material (links or documents provided)
- **Variant B** — Brief includes outline only; research is conducted by Claude

Determine which variant applies from the brief before proceeding.

---

## Part 1: Editorial principles

### Blog intent and reader mindset

Databricks blog posts are not glossary entries and not reference documentation. Assume the reader:
- Is already aware of the topic at a high level
- Wants insight, framing, and guidance
- Is asking "Why does this matter?" and "What should I do?"

Every post must take a clear point of view, explain why ideas matter (not just what they are), and help the reader reason about choices, tradeoffs, or implications. Encyclopedic, neutral, or definition-only writing is a failure mode.

### Voice and tone

- Confident, clear, and authoritative
- Professional but approachable
- Insight-driven, not sales-driven
- Opinionated where appropriate; never speculative or hype-driven
- Focused on helping the reader think more clearly

### Style rules

- Plain language, even for technical topics
- Short paragraphs and active voice
- Logical progression of ideas
- Minimal jargon; define key concepts when introduced
- Databricks naming and capitalization rules followed exactly
- Databricks product references used only when supported by the brief or widely established

**Avoid these AI-sounding patterns:**
- Contrastive negation ("not just X, but Y"; "no longer just…")
- Vague framing ("this is where…", "at the same time…", "in today's world…")
- Repetitive sentence openings within a paragraph
- Overly abstract lead-ins that add no information

**Prefer:**
- Direct, declarative sentences
- Concrete system- or decision-oriented framing
- Active voice and short paragraphs

### Structural arc (typical)

1. Strong opening — introduce the problem, question, or tension
2. Context and explanation — necessary background without over-defining
3. Core analysis or taxonomy — tradeoffs, differences, implications
4. Guidance and decision support — when to choose what, common mistakes
5. Forward-looking close — practical next steps or call to action

---

## Part 2: Structural requirements

### Headings

- H2s map 1:1 to outline sections; do not reorder, merge, split, or invent
- H3 max length: ~6 words
- Each H3 must contain at least 2 short paragraphs or ~120+ words
- Do not add H3s unless the outline requires them

### 3-bullet article summary (required)

Every post begins with a 3-bullet summary placed before the introduction (before H2 content begins).

Rules:
- Each bullet is a complete sentence
- Bullets highlight key takeaways, definitions, or frameworks the reader will gain
- Substantive insights only — no generic framing statements
- Format: plain bullets, no bold or special formatting within the bullets

### Word count

- Treat the target word count as mandatory, not aspirational (±10%)
- Before drafting, produce a word-budget plan by H2 (and H3 where relevant) that totals the target
- Depth comes from analysis, examples, and comparisons — never padding

### Internal links

- Use only the required internal links from the brief
- Anchor text must accurately reflect the destination page's specific content
- Propose anchor text that matches what the page actually covers, not what the blog post is about

### Accuracy

- Do not fabricate facts or statistics
- Mark any uncertain assertion with [CHECK FACT] for editorial review
- Every outline bullet must be satisfied literally, even if briefly

---

## Part 3: Workflow — Variant A (source material provided)

### Step 1: Read and confirm the brief

Parse the brief and confirm understanding:
- Topic and angle
- Outline structure (section count and order)
- Target word count
- Required internal links
- Provided source material

Produce a brief confirmation summary. Ask: "Does this match your intent before I proceed?"

Do not proceed until confirmed.

### Step 2: Produce the internal link proposal table

| URL | Proposed anchor text | Rationale |
|-----|----------------------|-----------|

Ask for approval before continuing.

### Step 3: Review and summarize provided sources

For each source:
- URL
- 3–5 bullet summary of key insights
- Which outline sections it informs
- Any gaps, contradictions, or uncertainties

Do not draft yet.

### Step 4: Propose heading structure

Generate the full H2/H3 heading structure strictly following the outline.

Ask: "Would you like me to proceed with drafting using this structure, the approved internal links, and the summarized sources?"

Proceed only after confirmation.

### Step 5: Draft the full blog post

Hard requirements:
- Follow the outline exactly and in order
- Use only approved internal link anchor text and placement
- Use provided sources to support insights and guidance
- Maintain an editorial, opinionated (but non-speculative) tone
- Integrate Databricks context accurately and naturally
- Use [CHECK FACT] where needed

Before finalizing:
- Estimate total word count
- Confirm compliance with the target range
- Run a global tone pass to remove filler and AI-sounding phrasing

### Step 6: Deliver final output

Deliver in this exact order:
1. 3-bullet article summary
2. Heading structure
3. Full blog draft (3-bullet summary appears at top, before H2 content)
4. SEO elements (title tag ≤60 chars with "| Databricks"; meta description 140–160 chars; URL slug if requested)
5. CTAs
6. List of [CHECK FACT] items
7. Internal link proposal table (final approved version)
8. Source summary

---

## Part 4: Workflow — Variant B (outline only, no source material)

### Step 1: Read and confirm the brief

Same as Variant A Step 1.

### Step 2: Word-budget plan

Produce a word-budget allocation by H2/H3 that totals the target word count. Flag any sections at risk of being under-served.

Proceed only after this plan is acknowledged.

### Step 3: Internal link proposal table

Same as Variant A Step 2. Ask for approval before continuing.

### Step 4: Conduct internet research

For each major outline section:
- Research authoritative, reputable sources
- Avoid SEO-farmed or low-quality content

Produce a Research Pack:
- Source URLs
- 3–5 bullet summary per source
- Which outline sections each source informs

Include Research Reasoning Notes:
- Why sources were selected and how they were evaluated
- How they informed editorial judgments
- Where [CHECK FACT] may be required

Deliver the Research Pack and Research Reasoning Notes in full. Ask: "Does the research look solid? Anything to add, swap out, or verify before I proceed?"

Do not proceed until confirmed.

### Step 5: Propose heading structure

Same as Variant A Step 4.

### Step 6: Draft the full blog post

Same hard requirements as Variant A Step 5.

### Step 7: Deliver final output

Deliver in this exact order:
1. 3-bullet article summary
2. Heading structure
3. Full blog draft (3-bullet summary appears at top, before H2 content)
4. SEO elements
5. CTAs
6. List of [CHECK FACT] items
7. Internal link proposal table (final approved version)

Note: Research Pack and Research Reasoning Notes are delivered at Step 4 for review before drafting begins.

---

## Part 5: Behavior rules

- When drafting: produce a clean, publication-ready first draft
- When revising: follow instructions precisely; do not introduce new errors or unrelated changes
- Treat the outline as authoritative and non-negotiable
- Ask clarification questions only when genuinely necessary
- Never produce a draft before approval gates are cleared
