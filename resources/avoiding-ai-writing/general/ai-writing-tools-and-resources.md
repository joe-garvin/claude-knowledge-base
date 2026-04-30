# AI writing: tools, skills, prompts, and resources

A catalog of everything built or published on detecting, auditing, and removing AI writing patterns. Compiled April 2026.

---

## Agentic skills and Claude-compatible tools

### avoid-ai-writing (conorbronsdon) ⭐ gold standard
**GitHub:** https://github.com/conorbronsdon/avoid-ai-writing  
**Type:** Portable SKILL.md / Claude Code skill  
**Version:** 3.3.1 (MIT license)  
**Author:** Conor Bronsdon (@ConorBronsdon, Chain of Thought podcast)

The most comprehensive open-source Claude skill for this purpose. A 109-entry tiered word replacement table, 36 pattern categories with before/after examples, two operating modes (rewrite and detect), P0/P1/P2 severity tiers, a second-pass audit, context profiles (linkedin, blog, technical-blog, investor-email, docs, casual), and a tolerance matrix adjusting rule strictness by content type.

What makes it different from a "make this sound human" prompt: structured audit, tiered detection (not vibes-based), automatic second pass to catch surviving tells, and a rewrite-vs-patch threshold (when to stop patching and advise a full rewrite).

**Integration options:**

Option 1 (clone into Claude Code skills):
```
git clone https://github.com/conorbronsdon/avoid-ai-writing ~/.claude/skills/avoid-ai-writing
```

Option 2 (reference in CLAUDE.md):
```
- Editing for AI patterns → read `path/to/avoid-ai-writing/SKILL.md`
```

Option 3 (slash command) — create `~/.claude/commands/clean-ai-writing.md`:
```
---
description: Audit and rewrite content to remove AI writing patterns
---
$ARGUMENTS
Read and follow the instructions in ~/.claude/skills/avoid-ai-writing/SKILL.md
```
Invoke with `/clean-ai-writing <your text>`.

**Trigger phrases:** "Remove AI-isms from this post," "Audit this draft for AI tells," "Make this sound less like AI," "Clean up AI writing in this paragraph."  
**Detect mode:** "detect," "flag only," "audit only," "just flag," "scan."

**Web app:** avoid-ai-writing-app.vercel.app — paste text, get full audit + rewrite (token-gated, community-built on Solana).

---

### anti-ai-slop-writing (jalaalrd)
**GitHub:** https://github.com/jalaalrd/anti-ai-slop-writing  
**Type:** Writing skill compatible with Claude Code, Codex, Cursor, Gemini CLI, and 8+ other agents  
**Description:** An alternative approach to eliminating detectable AI patterns. Works across multiple agent ecosystems.

---

### anti-ai-writing-patterns (Lobehub ecosystem)
**URL:** https://lobehub.com/skills/acaprino-figtree-plugins-anti-ai-writing-patterns  
**Type:** Skill in the Lobehub marketplace  
**Description:** Anti-AI writing patterns skill for the Lobehub/LobeChat ecosystem.

---

### anti-ai-writing (SkillsLLM listing)
**URL:** https://skillsllm.com/skill/avoid-ai-writing  
**Type:** Listed on the agentskills.io marketplace  
**Description:** The conorbronsdon avoid-ai-writing skill as listed in the agentskills.io registry.

---

## Custom prompts and instruction sets

### Will Francis's Claude custom instruction prompt ⭐
**URL:** https://willfrancis.com/how-to-stop-claude-writing-like-an-ai/  
**Type:** Claude custom instructions block (paste into Settings → Profile → Custom Instructions)

This is a production-tested system prompt for suppressing AI patterns at the generation stage. The author tested it against hundreds of pieces of content over a year. Verbatim:

```
## Voice

Be direct. Have opinions. Use specific examples and names, not vague claims. State your point first, then support it. Trust the reader to recognise what matters without labelling it as "significant" or "important."

## Banned words

Never use these — they are the most flagged AI-writing markers:

delve, dive into, navigate (figurative), underscore, bolster, foster, harness, leverage, unpack, shed light on, pave the way, pivotal, groundbreaking, cutting-edge, transformative, game-changing, innovative, robust, comprehensive, seamless, intricate, nuanced (as empty praise), vibrant, multifaceted, holistic, testament, landscape (figurative), realm

Never use these phrases:

- "In today's [fast-paced/rapidly evolving/digital] world..."
- "It's important/worth noting that..."
- "One of the most [important/significant/crucial]..."
- "When it comes to..." / "At its core..." / "At the end of the day..."
- "This is where X comes in" / "Let's break it down"
- "Plays a crucial role in..." / "It cannot be overstated..."
- "...underscoring the importance of..." / "...highlighting the need for..."
- "...reflecting a broader trend toward..." / "...marking a significant shift in..."

Never use these structures:

- "It's not just X — it's Y"
- "Not only X, but Y"
- "This isn't about X. It's about Y."
- "No X. No Y. Just Z."

These mimic insight without providing any.

## Structure

- Vary paragraph and sentence length. Don't write uniform blocks.
- Never use the "Bold term: explanation sentence" list format. It's the single most recognisable AI pattern.
- Don't signpost ("Let's explore," "Now let's turn to"). Just make your point.
- Don't open with a sweeping contextual statement. Don't close with a summary or inspirational wrap-up. Start and end on substance.
- Don't restate the question back before answering it.

## Style

- Use contractions. "It's," "don't," "won't."
- Maximum one em dash per response. Use commas or parentheses instead.
- Don't over-format. Plain prose is often clearer than headers and bullet points.
- Drop preamble ("Great question!"), performative enthusiasm ("exciting," "incredible," "powerful"), and unsolicited caveats.
- Match tone to context. Casual question, casual answer.

## Before finishing, check:

1. Read it out loud. Does any sentence sound like a press release? Rewrite it.
2. Are you repeating the same point in different words? Say it once.
3. Does your opening sentence set the scene with a grand statement about the state of the world? Delete it, start with the second sentence.
```

Add a personal voice note: "I write in a [warm/direct/dry] tone. I'm [knowledgeable/casual/conversational]. I use [British/American] English. I prefer [short sentences/plain language/jargon-free prose]." Even 2–3 sentences makes a measurable difference.

---

### Ruben Hassid's anti-AI-voice editor prompt
**URL:** https://substack.com/@ruben/note/c-181376166  
**Type:** Paste-and-go rewrite prompt for ChatGPT/Claude

The prompt instructs the model to act as an "Anti-AI-Voice Editor" that rewrites pasted text "so it reads like a clear, specific human. Not like ChatGPT, Claude, or a generic 'AI thought leader'." Published on Substack; high engagement as a social post.

---

### Nate B. Jones's 20-prompt anti-slop system
**URL:** https://natesnewsletter.substack.com/p/i-built-a-20-prompt-set-to-kill-ai  
**Type:** Substack newsletter / prompt library  
**Published:** October 10, 2025

A set of 20 prompts designed to catch and kill "AI slop" — shallow, directionless content. Structured around the idea that every decision must have a name, every action item an owner, every open question a next step. If any requirement fails, the AI revises before sending. Frames AI as a first-pass evaluator running against explicit quality checks before human review. His diagnosis: "The problem isn't the model. The problem is your standards."

---

### Voice profile interview method
**URL:** https://aiforcontentmarketing.ai/how-to-make-claude-write-like-you-the-interview-method/  
**Type:** Workflow / methodology

Rather than describing your voice to the AI, paste 5–10 of your best pieces (diverse contexts — a proposal and a blog post teach more than five proposals) and ask the AI to extract patterns and cite specific evidence. You're too close to your own voice to describe it accurately. The AI pattern-matches better from examples than from abstract rules.

**Key principle from the research:** "Most of a good voice profile is about what you reject, not what you prefer. Specificity comes from describing rejections like 'I'd never use semicolons because they make my writing sound like a college essay.'"

---

## Detection tools (AI detectors)

Understanding detectors matters for two reasons: knowing what signals trigger them, and knowing whether your editing has actually moved the needle.

### GPTZero
**URL:** https://gptzero.me  
**Method:** Five-layer detection model measuring perplexity, burstiness, and structural patterns. Has additional shields against paraphrasing bypass. Industry standard for educational contexts.  
**Reported accuracy:** 99.3% overall, 0.24% false positive rate (company claim). Independent testing: ~90%.

### Originality.AI
**URL:** https://originality.ai  
**Method:** Supervised learning with modified BERT and Roberta models. Strong on blog and web content.  
**Reported accuracy:** 99% (company claim). Independent testing: ~76% overall.

### Winston AI
**URL:** https://gowinston.ai  
**Reported accuracy:** 99.98% (company claim). Real-world ~90%.

### Copyleaks
**URL:** https://copyleaks.com  
**Strength:** Multilingual support (30+ languages). Trained on scholarly papers; strong on academic content, potentially less accurate on blog posts and creative writing.

### Turnitin
**Strength:** Academic standard. Trains on scholarly papers. High accuracy for essays and research papers; less calibrated to marketing/creative content.

### Sapling AI
**URL:** https://sapling.ai  
**Notes:** Strong performance in independent tests; matched or outperformed top competitors in several comparison studies.

### ZeroGPT
**URL:** https://zerogpt.com  
**Notes:** Free, widely used. Accuracy varies significantly in independent tests.

---

## Humanizer tools (AI-to-human conversion)

These tools rewrite AI text to score higher on human detection. Most are content farms with marketing claims far exceeding independent validation. Useful as a first pass; human editorial is still required for authentic voice.

**The limits of humanizer tools:** They can improve perplexity and burstiness scores, but the SEJ/arxiv research finding stands — patterns are encoded at the word-distribution level and persist even through LLM-to-LLM rewriting. A humanizer tool is a good first step, not a solution.

| Tool | URL | Notes |
|---|---|---|
| WriteHuman | writehuman.ai | Claims bypass of most major detectors |
| QuillBot AI Humanizer | quillbot.com/ai-humanizer | Trained on human texts; evolves with AI detectors |
| Grammarly AI Humanizer | grammarly.com/ai-humanizer | Integrated into the Grammarly ecosystem |
| Phrasly | phrasly.ai | All-in-one: detector + humanizer, proprietary models, claimed 2M+ users |
| Undetectable AI | undetectableai.pro | Multi-detector testing |
| StealthWriter | stealthwriter.ai | Focuses on structural rebuilding, not just synonym swapping |
| BypassGPT | bypassgpt.ai | Multiple detector cross-check |
| WalterWrites | walterwrites.ai | Sentence length randomization + humanization |
| Rewritify | rewritify.ai | Cross-checks with GPTZero, ZeroGPT, Sapling, Winston, Copyleaks |
| GPTHuman | gpthuman.ai | Continuously retrained against evolving detectors |
| GPTinf | gptinf.com | Combined detector + humanizer |
| Humanize.io | humanize.io | Claims 99% bypass success (company claim) |
| Humanize AI | humanizeai.pro | Free, no signup |

---

## Written resources and reference guides

### The avoid-ai-writing SKILL.md (primary reference)
**URL:** https://github.com/conorbronsdon/avoid-ai-writing/blob/main/SKILL.md  
The most comprehensive open-source structured reference on AI patterns. 36 pattern categories with before/after examples, 109-entry tiered word table, severity system, context profiles, tolerance matrix. This is the document to read if you read one.

### Wikipedia: Signs of AI Writing
**URL:** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing  
Built by Wikipedia editors dealing with AI-generated article submissions. Grounded in thousands of real examples. Frequently cited by other researchers as the canonical taxonomy.

### Search Engine Journal: AI Writing Fingerprints
**URL:** https://www.searchenginejournal.com/ai-writing-fingerprints-how-to-spot-fix-ai-generated-content/541613/  
Reports on the arxiv.org classifier study achieving 97.1% accuracy in attributing text to specific LLMs. Documents per-model vocabulary signatures (aidiolects) and five specific remediation techniques. Key finding: patterns persist through LLM-to-LLM rewriting.

### Contently: How to Edit the AI-isms Out of Your Content
**URL:** http://contently.com/2025/10/14/how-to-edit-the-ai-isms-out-of-your-content-no-detectors-needed/  
Professional editorial perspective from a major content agency. Practical workflow: cut padded language and limp verbs, inject specific names and data, fact-check every source, add expert quotes (via HARO, LinkedIn). Stanford study cited: edited AI content scored 47% higher on originality metrics than raw outputs.

### Tom Orbach: The "Anti-AI" Writing Cheat Sheet
**URL:** https://www.marketingideas.com/p/the-anti-ai-writing-cheat-sheet  
Paywalled (paid Substack). The accessible preview establishes: 13 fixable AI patterns (with before/after fixes), a 100+ banned words/phrases list, instructions for adding voice back after AI strips it out, and a copy-paste auto-fix prompt. Orbach's framing is useful: the problem is pattern-based, not tone-based. "AI writes in very specific patterns that are invisible to the writer but obvious to everyone reading."

### Will Francis: How to Stop Claude Writing Like an AI
**URL:** https://willfrancis.com/how-to-stop-claude-writing-like-an-ai/  
Practical guide to using Claude's custom instructions to suppress AI patterns at generation. Includes the full verbatim prompt (reproduced above). References Max Planck Institute research finding AI vocabulary words spiked 50%+ in published human writing post-ChatGPT.

### The Augmented Educator: Ten Telltale Signs of AI-Generated Text
**URL:** https://www.theaugmentededucator.com/p/the-ten-telltale-signs-of-ai-generated  
Accessible 10-sign taxonomy, educational framing. Useful for quick orientation.

### Originality.AI: Perplexity and Burstiness in Writing
**URL:** https://originality.ai/blog/perplexity-and-burstiness-in-writing  
Explains the two primary metrics AI detectors use. Essential for understanding why structural uniformity is harder to mask than vocabulary.

### Pangram Labs: Walking Through AI's Most Overused Phrases
**URL:** https://www.pangram.com/blog/walking-through-ai-phrases  
From the team that trains classifiers on 28 million human documents. Their key finding: structural regularity outweighs vocabulary as a detection signal. Fixing words while leaving rhythm untouched doesn't fool structural classifiers.

### Pangram Labs: Why Perplexity and Burstiness Fail to Detect AI
**URL:** https://www.pangram.com/blog/why-perplexity-and-burstiness-fail-to-detect-ai  
The counterargument to the perplexity/burstiness framing. Worth reading alongside the Originality.AI piece for a complete picture of detection methodology debates.

### Nate B. Jones Substack (natesnewsletter.substack.com)
Multiple posts on prompt engineering for quality over "AI slop." The "20 prompts" post (October 2025) and the "Goldilocks prompting" methodology are both relevant. His framing: quality standards matter more than model choice.

### AI Phrase Finder: The 50 Most Common AI Phrases
**URL:** https://aiphrasefinder.com/common-ai-phrases/  
Full annotated list with explanations for why each phrase signals AI authorship. Companion pieces: "The 100 Most Common AI Words" and "100 Common ChatGPT Adjectives."

### Walter Writes: Most Common ChatGPT Words to Avoid
**URL:** https://walterwrites.ai/most-common-chatgpt-words-to-avoid/  
Extended word list with 150+ flagged words.

### Blake Stockton: Red Flag Words
**URL:** https://www.blakestockton.com/red-flag-words/  
Additional curated list with commentary.

---

## Academic and research sources

### arxiv: Identifying which LLM wrote a given text (February 2025)
**URL:** https://arxiv.org/pdf/2502.12150  
The study reported by SEJ. 97.1% accuracy in attributing text to specific LLMs. Key findings: per-model vocabulary signatures persist through rewriting/translation/summarization; patterns are encoded at word-distribution level, not just surface vocabulary.

### ScienceDirect: Humanizing AI-Generated Text: Techniques and Future Directions
**URL:** https://www.academia.edu/123664396/Humanizing_AI_Generated_Text_Techniques_and_Future_Directions  
Academic survey of humanization techniques: lexical substitution, sentence restructuring, sentiment adjustment, idiomatic expression insertion.

### ScienceDirect: Linguistic fingerprints in human and AI-generated texts (NLP approach)
**URL:** https://www.sciencedirect.com/science/article/pii/S2215039026000056  
NLP-based study comparing linguistic features of human vs. AI text in second language writing contexts.

### Copyleaks research: AI has unique stylistic fingerprints
**URL:** https://copyleaks.com/blog/copyleaks-research-reveals-which-ai-wrote-what  
Research demonstrating model-specific stylistic fingerprints; basis for Copyleaks' attribution methodology.

### Inside Higher Ed: Distinguishing AI-composed from human-composed essays (opinion)
**URL:** https://www.insidehighered.com/opinion/career-advice/teaching/2024/07/02/ways-distinguish-ai-composed-essays-human-composed-ones  
Academic context; useful for the educational/writing program perspective on what distinguishes AI composition.

---

## The detection-evasion ecosystem (context, not recommendation)

For background awareness: an entire industry has built tools specifically to bypass AI detectors — marketed to students, content creators, and professionals under the banner of "humanization." These tools typically work by adjusting burstiness (sentence length variation) and perplexity scores, and cross-checking against multiple detectors before delivery.

The ethical issues in educational contexts are real and not addressed here. From a craft perspective, the relevant finding is that these tools can improve detection scores without actually producing good writing — they optimize for the metric, not the result. A piece can pass GPTZero and still read as obviously machine-generated to a human reader with good editorial instincts.

---

## Sources

- [avoid-ai-writing (conorbronsdon)](https://github.com/conorbronsdon/avoid-ai-writing)
- [anti-ai-slop-writing (jalaalrd)](https://github.com/jalaalrd/anti-ai-slop-writing)
- [How to Stop Claude Writing Like an AI — Will Francis](https://willfrancis.com/how-to-stop-claude-writing-like-an-ai/)
- [I Got Tired of AI Slop so I Built 20 Prompts to Fix It — Nate B. Jones](https://natesnewsletter.substack.com/p/i-built-a-20-prompt-set-to-kill-ai)
- [How to Edit the AI-isms Out of Your Content — Contently](http://contently.com/2025/10/14/how-to-edit-the-ai-isms-out-of-your-content-no-detectors-needed/)
- [The "Anti-AI" Writing Cheat Sheet — Tom Orbach](https://www.marketingideas.com/p/the-anti-ai-writing-cheat-sheet)
- [GPTZero vs Copyleaks vs Originality — GPTZero](https://gptzero.me/news/gptzero-vs-copyleaks-vs-originality/)
- [Most Accurate AI Detectors — GPTZero](https://gptzero.me/news/best-ai-detectors/)
- [Perplexity and Burstiness — Originality.AI](https://originality.ai/blog/perplexity-and-burstiness-in-writing)
- [Walking Through AI's Most Overused Phrases — Pangram Labs](https://www.pangram.com/blog/walking-through-ai-phrases)
- [AI Writing Fingerprints — Search Engine Journal](https://www.searchenginejournal.com/ai-writing-fingerprints-how-to-spot-fix-ai-generated-content/541613/)
- [The 50 Most Common AI Phrases — AI Phrase Finder](https://aiphrasefinder.com/common-ai-phrases/)
- [AI Writing vs Human Writing — Programming Insider](https://programminginsider.com/ai-writing-vs-human-writing-where-humanizer-tools-bridge-the-gap/)
- [How to Humanize AI Content Like a Pro — Medium / Illumination](https://medium.com/illumination/how-to-humanize-ai-content-like-a-pro-in-2025-what-actually-works-bc51eab02edc)
