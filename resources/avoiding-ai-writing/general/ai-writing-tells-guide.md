# AI writing tells: a comprehensive guide

A research reference on what makes writing sound AI-generated, how detection works, and the best-known techniques for remediation. Compiled April 2026.

---

## What we mean by "sounds like AI"

Recognition is typically immediate. A reader encounters a paragraph and something tells them — "AI wrote this" — before they can articulate why. That instinct is responding to a cluster of overlapping signals: vocabulary, rhythm, structure, and a certain epistemic cowardice that passes as thoroughness.

The core problem is statistical. Language models are trained on the patterns of human writing and optimized to produce what is most expected next. That optimization produces text that is grammatically flawless, structurally tidy, and stylistically dead — the average of a billion documents rather than any individual's voice. It reads like the platonic corporate memo: complete, correct, and forgettable.

Tom Orbach (Director of Growth Marketing at Google, Forbes 30 Under 30) frames the problem precisely: "The problem is that AI writes in very specific patterns that are invisible to the writer but obvious to everyone reading." Most people trying to fix this ask AI to "add a personal touch." That misses the point. The problem is more related to pattern than tone.

---

## The taxonomy of AI tells

### 1. Vocabulary tells

**Mode collapse vocabulary.** AI gravitates toward a small rotation of words that feel authoritative but add nothing. These fall into clusters:

- *Elevation verbs*: delve, harness, leverage, navigate, streamline, foster, cultivate, empower, spearhead, galvanize
- *Approval adjectives*: robust, seamless, comprehensive, cutting-edge, pivotal, holistic, multifaceted, nuanced, groundbreaking, transformative, innovative, dynamic
- *Metaphor nouns*: landscape, tapestry, realm, ecosystem, beacon, symphony, cornerstone, paradigm
- *Filler verbs*: serves as, features (verb), boasts, presents, encompasses, underpins, underscores

These words are massively overrepresented in AI text relative to human text. Research from the Max Planck Institute found that "words like these have spiked in usage by over 50% in published writing since ChatGPT launched" — including in human writing, as people unconsciously absorb AI's vocabulary.

**"Delve" as the canonical example.** The word "delve" became the public symbol of AI writing in 2023–2024 because ChatGPT used it at extraordinary frequency. It's an academic-register word that sounds sophisticated while saying nothing specific: "let's delve into this topic." By 2025, it had become so flagged that models started suppressing it, but the underlying impulse — reaching for the fanciest thesaurus synonym — persists.

**Aidiolects.** Research achieving 97.1% accuracy in identifying which AI wrote a given piece found that each model has a distinct vocabulary signature — what researchers call "aidiolects." ChatGPT favors "certainly," "such as," "overall," and "below is." Claude leans on "according to the text," "based on," "both," "the text." DeepSeek overuses "crucial," "essentially," "here's a breakdown." These per-model signatures persist even after rewriting, translation, or summarization by another LLM. The patterns are encoded at the word-distribution level and don't wash out easily.

**Copula avoidance.** AI avoids "is" and "has" by substituting fancier verbs: "serves as," "features," "boasts," "represents," "presents." This sounds like a press release. The fix is defaulting to "is" or "has" unless a more specific verb genuinely adds meaning.

**Synonym cycling.** To avoid repeating a word, AI rotates through synonyms: "developers… engineers… practitioners… builders" in the same paragraph. Human writers repeat the clearest word. Forced variation reads like thesaurus abuse.

---

### 2. Phrase-level tells

**Formulaic openers.** AI defaults to scene-setting preambles that contextualize the topic grandly before saying anything. The canonical forms:

- "In today's rapidly evolving digital landscape…"
- "In an era where [X]…"
- "In the realm of…"
- "In today's digital age…"

These are the most flagged location for AI phrases — introductions far outpace conclusions. They're how AI eases into a topic instead of starting with the point.

**Significance inflation.** AI marks routine events as historical: "marking a pivotal moment in the evolution of," "a watershed moment for the industry," "a testament to human ingenuity." If the inflation clause can be deleted and the sentence still works, delete it.

**Filler transitions.** "Moreover," "Furthermore," "Additionally," "In conclusion," "In summary," "It's worth noting that," "Notably" — these are AI's essay-structure scaffolding, not connective tissue. They signal a paragraph is done rather than connecting it to the next.

**Confidence calibration phrases.** "Interestingly," "Surprisingly," "Importantly," "Significantly," "Certainly," "Undoubtedly" — AI uses these to tell the reader how to feel about a fact rather than letting the fact speak. Density is the signal: one "notably" in 2,000 words is fine; three in 500 is AI-style emphasis stacking.

**The false contrast structure.** "It's not just X — it's Y." "This isn't about X, it's about Y." "No X. No Y. Just Z." These mimic the shape of insight without containing any. Will Francis, in his guide to prompting Claude, calls them out specifically: "These constructions mimic insight without providing any."

**False ranges.** AI creates apparent breadth by pairing unrelated extremes: "from the Big Bang to dark matter," "from ancient civilizations to modern startups." These sound sweeping but say nothing.

**Template slot-fill phrases.** "Whether you're [X] or [Y]" (false breadth — just say "everyone"), "a [adjective] step forward for [noun]," "I recently had the pleasure of [verb]-ing" (LinkedIn review pattern).

---

### 3. Structural tells

**The intro-list-conclusion architecture.** AI defaults to a predictable scaffold: broad contextual opening → enumerated points or bulleted list → summary conclusion that restates what was just said. This structure "tells you what it's about to do, does it, then tells you what it just did," as one analysis puts it.

**Inline-header lists.** The single most recognizable AI formatting pattern, per Will Francis: bullet lists where each item begins with a bold term followed by an explanation. "**Performance:** Performance improved by…" Strip the bold headers; write the point directly.

**Formulaic challenges.** A "Challenges" section that begins "Despite [positive word], [subject] faces challenges…" and ends with vague optimism. Name the actual challenge and the actual response, or cut it.

**Paragraph length uniformity.** AI produces paragraphs of nearly identical size. Human writing has natural variation: some paragraphs are one sentence; some run longer. If every paragraph is 3–5 sentences, it's a structural tell.

**Sentence length uniformity.** The metronomic rhythm — most sentences 15–25 words — is a strong detector signal. Human writing mixes short punchy sentences (3–8 words) with longer flowing ones. Fragments work. Questions break the pattern.

**Excessive structure.** More than 3 headings in under 300 words is almost always AI trying to look organized. "Overview," "Key Points," "Summary," "Conclusion," "Introduction" are default AI scaffolding — use headers that tell the reader something specific.

**Numbered list inflation.** "Three key takeaways," "Five things to know," "Here are the top seven" — AI defaults to numbered lists because they're structurally safe. Only use them when the content genuinely has that many discrete, parallel items.

---

### 4. Cognitive and epistemic tells

**Epistemic cowardice.** AI presents multiple perspectives even when one is clearly stronger, creating text that is perpetually balanced to the point of meaninglessness. It hedges with "perhaps," "could potentially," "it's important to note that," "to be clear," and "generally speaking." This is a form of self-protection: the model avoids commitment to avoid being wrong.

**Absence of genuine opinion.** Humans have preferences, reactions, and stakes. AI is relentlessly neutral. The absence of "I think," stated preferences, or any position that might be disagreed with is itself a tell, especially in pieces that are supposed to have a voice.

**Lack of specificity.** AI speaks in broad claims and sweeping generalities. It says "experts believe" without naming the expert. It cites "studies show" without naming the study. It calls things "significant" without quantifying the significance. Human writers know specific things — names, numbers, dates, contexts. AI approximates.

**No personal experience.** AI cannot have been somewhere, tried something, or changed its mind. The absence of first-person experience ("when I ran this campaign," "the time we tried X") is a tell in contexts where that experience would be natural.

**Novelty inflation.** AI treats established concepts as if the writer invented or discovered them: "She introduced a term I hadn't heard before," "a failure mode nobody's naming," "the insight everyone's missing." This is both credibility risk (the concept probably has a Wikipedia page) and AI's simulation of discovery.

**Vague attributions.** "Experts believe," "Studies show," "Research suggests," "Industry leaders agree" — without naming the expert, study, or leader. Either cite a specific source or drop the attribution and state the claim directly.

**Emotional flatline.** AI claims emotions structurally without conveying them through writing: "What surprised me most," "I was fascinated to discover," "What struck me was." If the thing is genuinely surprising, the reader should feel that from the content, not from the writer announcing it.

**Reasoning chain artifacts.** AI's chain-of-thought process leaking into prose: "Let me think step by step," "Breaking this down," "Step 1:," "Working through this logically." The reader doesn't need the scaffolding. State the conclusion, then the evidence.

**Chatbot artifacts.** "I hope this helps!", "Certainly!", "Absolutely!", "Great question!", "Feel free to reach out." Remove entirely. Also: "In this article, we will explore…" and "Let's dive in!" — AI-generated meta-narration.

**Sycophantic tone.** "Great question!", "Excellent point!", "You're absolutely right!", "That's a really insightful observation." These are conversational rewards from chat interfaces, not writing.

**Acknowledgment loops.** "You're asking about," "The question of whether," "To answer your question" — AI restating the prompt before answering. Just answer.

---

## The detection science: perplexity and burstiness

AI detectors operate on two primary metrics:

**Perplexity** measures how predictable the text is — how well an AI can predict what word comes next. Low perplexity means the text used high-probability words in expected positions. AI writes to minimize perplexity by construction. Human writers choose words for reasons a language model doesn't optimize for: memory, rhythm, specificity, humor, context only the writer has. Those choices register as perplexity spikes.

By GPTZero's public methodology: human writing averages ~80–100 perplexity units; GPT-4 output averages ~20–30.

**Burstiness** measures variation in sentence structure and length. Human writing has high burstiness — a mix of short, staccato sentences and long flowing ones. AI text is metronomic: it clusters around uniform sentence lengths and consistent rhythmic patterns, producing low burstiness scores.

GPTZero's burstiness scores: humans spread 0.6–1.2; GPT output clusters around 0.2–0.4.

**The detection limit.** These metrics are increasingly circumventable by humanizer tools. Pangram Labs, which trains a classifier on 28 million human documents, argues that structural regularity is a more robust signal than vocabulary. Fixing the flagged words while leaving the rhythm untouched still reads as AI-generated. Detection tools' claimed accuracy rates (often 99%+) are disputed; independent testing typically shows 76–90% real-world accuracy, with false positive rates that vary significantly.

**The fingerprint persistence problem.** Per the arxiv study (February 2025): AI writing patterns persist even when texts are rewritten, translated, or summarized by another LLM. Patterns are encoded at the word-distribution level. The remediation has to involve genuine human intervention — not AI paraphrasing AI.

---

## Manual editorial techniques: the gold standard

### Philosophy first

The goal is not to fool a detector. It's to write text that sounds like a specific person wrote it — text with individual vocabulary, genuine opinion, earned emotion, and imperfect rhythm. Detection evasion is a byproduct; the actual target is authentic voice.

### The editorial workflow (professional standard)

**Step 1: Never use AI's opener.** Write the first 2–3 sentences yourself, in your own voice. This establishes authority and voice immediately, and the opening is the highest-density location for AI tells.

**Step 2: Vocabulary pass.** Work through the Tier 1 flagged words and cut or replace on sight. Then check for Tier 2 clustering (two or more elevation words in the same paragraph). This is mechanical and fast.

**Step 3: Structural break.** Identify AI's default architecture (intro-list-conclusion) and break it. Lead with the point instead of building to it. Merge uniform paragraphs or split them. Convert bullet lists into prose where the content is actually sequential thinking, not a genuine list.

**Step 4: Specificity injection.** Find every vague attribution ("experts say"), every sweeping generality ("this is crucial for success"), every round number ("thousands of customers"), and replace with specifics — names, dates, numbers, examples, quotes from actual sources.

**Step 5: Voice injection.** Add what only a human with skin in the game can add: opinion, experience, reaction, preference, stakes. Where the piece is supposed to have a point of view, take one. If the draft is neutral on a question that should have an answer, answer it.

**Step 6: Rhythm break.** Read the draft aloud. Count sentence lengths. If you hear a metronome, break it — add a fragment, a one-sentence paragraph, a question, a longer sentence with a natural comma-and-then structure. Any sentence that sounds like it could be delivered by text-to-speech without sounding weird is probably too uniform.

**Step 7: Expert quotes.** Weave in real expert quotes or sourced data — from HARO (relaunched 2025), LinkedIn, professional communities. "Experts believe" becomes "Dr. Sarah Chen, in a 2024 interview with Nature, argued that..."

**Step 8: Fact-check everything.** Click through every source AI cited. Verify numbers against the primary study, not the AI summary. AI hallucinates citations with confidence.

**Step 9: Second pass.** Run the Contently checklist: cut filler ("in order to," "as well as," "in terms of"), cut padded verbs ("helps with," "is aimed at," "can be used to"), check for "lists of three" appearing in every section, check for forced rhythmic patterns like "While X is true, Y is also important."

### The read-aloud test

If the text sounds like it could be read by text-to-speech without sounding weird, it's too uniform. Human writing has rhythm that resists robotic delivery — uneven sentence length, natural disfluency, idiosyncratic word choices, pacing that speeds up and slows down.

### The Orbach standard

Tom Orbach's personal editorial standard: "I personally run every single thing I write through these rules before I publish. I refuse to let anything out the door that could make someone think 'AI wrote this.'" The framing is credibility: every AI-sounding piece erodes a small amount of the audience's trust in whether the writer is actually talking to them.

### The Contently editorial additions

From Contently's professional editorial guide:
- Cut "padded language and limp verbs": "helps with," "is aimed at," "can be used to," "serves as"
- Cut filler: "in order to," "as well as," "in terms of"
- Seek out generalisms and personalize with names, proper pronouns, specific examples
- "AI text loves to speak in broad claims" — the fastest fix is to get concrete
- If a bullet list appears in every section, editorial judgment should determine whether the content actually warrants lists or just defaulted to them

---

## The over-polishing trap

Applying every rule at maximum strictness can push human writing toward AI statistical profiles. Natural disfluency, idiosyncratic word choices, and uneven pacing are what keep text out of the "AI-generated" classification. Deliberately sanding away all irregularity in pursuit of clean prose creates the very uniformity you're trying to avoid.

The avoid-ai-writing SKILL.md captures this precisely: "Don't sand away all personality in pursuit of clean prose. This skill should make writing sound more human, not less."

---

## The rewrite-vs-patch threshold

If a draft has:
- 5+ flagged vocabulary hits across multiple Tier 1 categories
- 3+ distinct structural pattern categories triggered
- Uniform sentence/paragraph length throughout

...patching individual phrases won't fix it. The structure itself is AI-generated. Advise a full rewrite: state the core point in one sentence, then rebuild from there.

---

## Sources

- [AI Writing Fingerprints: Identify (& Fix) AI-Generated Content — Search Engine Journal](https://www.searchenginejournal.com/ai-writing-fingerprints-how-to-spot-fix-ai-generated-content/541613/)
- [avoid-ai-writing GitHub repo (conorbronsdon)](https://github.com/conorbronsdon/avoid-ai-writing)
- [The 50 Most Common AI Phrases — AI Phrase Finder](https://aiphrasefinder.com/common-ai-phrases/)
- [How to Edit the AI-isms Out of Your Content (No Detectors Needed) — Contently](http://contently.com/2025/10/14/how-to-edit-the-ai-isms-out-of-your-content-no-detectors-needed/)
- [How to Stop Claude Writing Like an AI — Will Francis](https://willfrancis.com/how-to-stop-claude-writing-like-an-ai/)
- [The "Anti-AI" Writing Cheat Sheet — Tom Orbach, Marketing Ideas](https://www.marketingideas.com/p/the-anti-ai-writing-cheat-sheet)
- [Perplexity and Burstiness in Writing — Originality.AI](https://originality.ai/blog/perplexity-and-burstiness-in-writing)
- [The Ten Telltale Signs of AI-Generated Text — The Augmented Educator](https://www.theaugmentededucator.com/p/the-ten-telltale-signs-of-ai-generated)
