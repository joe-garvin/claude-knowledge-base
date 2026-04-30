# AI writing tools and resources for RDC writers

A practical catalog of tools, prompts, and references for writers using Claude, ChatGPT, or Gemini to assist with client content. Organized from most to least immediately usable, with plain-language explanations for anything technical. This document is for writers who use AI chatbots as part of their workflow — not engineers or developers. Everything here is accessible through a browser. Where more advanced tools are mentioned, they're flagged clearly.

---

## The most important thing to set up: custom instructions

Every major AI chatbot lets you give it standing instructions that apply to every conversation. This is the single highest-leverage thing you can do to reduce AI-isms at the generation stage — before you have to edit them out.

Think of it as a style brief that the AI reads before every project. You set it once; it applies automatically.

---

### Custom instructions for Claude (claude.ai)

**Where to set it:** Settings → Profile → Custom instructions → paste → Save

This set of instructions — adapted from Will Francis's widely-used guide — suppresses the most common AI patterns before they appear in the draft. Copy and paste it as-is, then add a note at the end describing your own voice.

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
- Never use the "Bold term: explanation sentence" list format.
- Don't signpost ("Let's explore," "Now let's turn to"). Just make your point.
- Don't open with a sweeping contextual statement. Don't close with a summary or inspirational wrap-up.
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

**Add your own voice note at the end.** Even two or three sentences makes a measurable difference. For example:

> "I write in a direct, conversational tone. I'm knowledgeable without being showy. I use American English. I prefer short sentences and plain language over jargon."

---

### Custom instructions for ChatGPT (chatgpt.com)

**Where to set it:** Click your name (bottom left) → Customize ChatGPT → paste into "What would you like ChatGPT to know about you?" or "How would you like ChatGPT to respond?"

Use the same instruction set above. ChatGPT's custom instructions work identically in practice — same suppression effect on vocabulary and structure.

---

### Custom instructions for Gemini (gemini.google.com)

Gemini's custom instruction support is less robust than Claude's or ChatGPT's as of early 2026. The most reliable approach is to paste the instruction set at the top of each conversation as a system prompt: "Before we start, follow these writing guidelines throughout our conversation: [paste instructions]."

Alternatively, save the instruction set as a text file and paste it at the start of each Gemini session.

---

## Paste-and-go rewrite prompts

For when you already have an AI draft and need to clean it up in the same chatbot session. Paste the prompt, then paste your draft below it.

### General AI-isms cleanup
```
Act as an editor who specializes in removing AI writing patterns. Rewrite the following text so it sounds like a specific, knowledgeable person wrote it — not a language model. Make these changes:

1. Replace any AI-vocabulary words (delve, leverage, robust, seamless, pivotal, tapestry, landscape, realm, holistic, transformative, groundbreaking, showcase, foster, harness, etc.) with simpler, more specific alternatives.
2. Remove any opener that begins with a grand contextual statement ("In today's rapidly evolving...") and start with the actual point.
3. Break the Bold term: explanation bullet format — rewrite as prose.
4. Remove filler transitions (Moreover, Furthermore, In conclusion, It's worth noting that).
5. Remove any chatbot residue (Certainly!, Great question!, I hope this helps!).
6. Vary sentence and paragraph length — mix short and long.
7. Replace vague attributions ("experts believe," "studies show") with specific sources or reframe as general claims.
8. Remove the false contrast structure ("It's not just X — it's Y").
9. If the closing is generic (The future looks bright / Only time will tell), replace with something specific to the piece's argument.

Return the rewritten version only. No commentary.
```

### Microsoft-specific editorial pass
```
You are editing marketing content for a Microsoft audience — primarily IT professionals, developers, and business decision-makers. Rewrite the following draft to:

1. Replace elevated AI vocabulary with plain, precise language (use "use" not "leverage," "strong" not "robust," "smooth" not "seamless").
2. Verify that any technical claims are specific and accurate — if a claim is vague ("significantly improves performance"), make it concrete or flag it for fact-checking with [VERIFY].
3. Remove promotional language ("groundbreaking," "revolutionary," "unprecedented") unless the specific claim backs it up.
4. Start with the actual point, not a contextual scene-setter.
5. Vary sentence length — avoid the metronomic 15–20-word average that AI defaults to.

Return the rewritten version. Flag anything that needs a human fact-check with [VERIFY].
```

### Databricks-specific editorial pass
```
You are editing technical marketing content for a Databricks audience — data engineers, ML practitioners, and data platform architects. Rewrite the following draft to:

1. Replace all AI-ism vocabulary with plain, precise alternatives.
2. Flag any technical claims that need verification against Databricks documentation with [VERIFY: check against docs.databricks.com].
3. Make integration and feature names specific — "leverages a robust ecosystem" should name the actual integrations.
4. Remove thought-leadership inflation ("paradigm shift," "transformative approach") — this audience responds to specifics, not superlatives.
5. Use active voice throughout.

Return the rewritten version with [VERIFY] flags where relevant.
```

### City of Seattle / public sector pass
```
You are editing content for a public sector audience — City of Seattle employees and residents. Rewrite the following draft to:

1. Replace elevated or jargon-heavy language with plain alternatives (city staff and residents vary widely in technical background).
2. Replace "utilize" with "use," "facilitate" with "help," "leverage" with "use."
3. Remove all AI-ism vocabulary from the Tier 1 list.
4. Keep sentences short and declarative where possible.
5. Remove any promotional register — public sector content should be informational, not sales-oriented.

Return the rewritten version only.
```

---

## Ruben Hassid's anti-AI-voice prompt

A widely-shared single-prompt approach for quick cleanups. Paste this, then paste the text.

```
Act as my Anti-AI-Voice Editor. Rewrite the text I paste so it reads like a clear, specific human wrote it. Not like ChatGPT, Claude, or a generic "AI thought leader." Rules: no em dashes, no "delve," no "tapestry," no "in the realm of," no "it's not just X — it's Y" constructions, no bold-term bullet lists, no opener that sets global context before getting to the point. Make it direct and specific. Return the rewrite only.
```

---

## The voice profile method

For ongoing projects with a specific client or content series, the most effective approach is building a voice profile from existing content rather than writing instructions from scratch. Here's how:

1. Gather 5–10 pieces of content from the client (or RDC's best work for that client) that represent the voice you're trying to match.
2. Paste them into Claude or ChatGPT with this prompt: "Read these samples and extract the voice patterns. What vocabulary does this writer avoid? What sentence rhythms do they use? What's their relationship to technical jargon? Cite specific examples from the text."
3. Take the AI's analysis and refine it — you know things it doesn't about what was intentional vs. accidental.
4. Use the resulting profile as a prefix to any content brief for that client.

The key insight: describing your rejections is more useful than describing your preferences. "We would never use 'leverage' or write a sentence like 'It's not just a platform, it's a paradigm shift'" teaches the model more than "we write in a clear, direct voice."

---

## The avoid-ai-writing skill

**What it is:** A detailed set of instructions — 36 pattern categories, a 109-word replacement table, and a severity system — that tells Claude how to audit and rewrite content to remove AI tells.

**Who it's for:** This is a more advanced tool. If you're using Claude through a regular browser chat window (claude.ai), you can still use it — you just need to paste the instructions into your conversation.

**The easy version (no technical setup required):** Go to github.com/conorbronsdon/avoid-ai-writing. Click the file called SKILL.md. Copy the entire contents. At the start of a Claude conversation, paste it in and say "Follow these instructions. Here's the text I want you to audit: [paste your text]." Claude will run a full structured audit and rewrite.

**The more advanced version (requires technical setup):** If you or someone at RDC uses Claude Code — a command-line developer tool, separate from the regular Claude chatbot — the skill can be installed as a slash command that works automatically. This is worth exploring if RDC wants to build a more systematic workflow, but it requires someone comfortable with developer tools to set it up. More at github.com/conorbronsdon/avoid-ai-writing.

**What it does:** Returns your text with every AI-ism flagged by category and severity (P0 credibility-killers, P1 obvious AI smell, P2 stylistic polish), a clean rewrite, and a second pass to catch anything the first edit missed.

---

## Written references

### The word and phrase list (this folder)
The working replacement table. Use during your editorial pass.

### The conceptual guide (this folder)
The fuller explanation of AI tells — what they are, why they happen, and the complete editorial workflow. Reference when onboarding new writers or explaining the problem to a client.

### Wikipedia: Signs of AI Writing
**URL:** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing  
Built by Wikipedia editors dealing with AI-generated article submissions. The canonical public reference — grounded in thousands of real examples, not theory. Useful when you need to explain the problem to someone who's skeptical.

### Contently: How to Edit the AI-isms Out of Your Content
**URL:** http://contently.com/2025/10/14/how-to-edit-the-ai-isms-out-of-your-content-no-detectors-needed/  
Professional editorial perspective from a major content agency. Practical emphasis on specificity, expert sourcing, and fact-checking. Good framing for agency context: "A Stanford study found edited AI content scored 47% higher on originality metrics than raw outputs."

### Will Francis: How to Stop Claude Writing Like an AI
**URL:** https://willfrancis.com/how-to-stop-claude-writing-like-an-ai/  
Source for the custom instruction set above. Worth reading in full for the explanation of why each pattern matters. The em-dash section alone is useful for anyone who's noticed it and didn't know why.

### Tom Orbach: The Anti-AI Writing Cheat Sheet
**URL:** https://www.marketingideas.com/p/the-anti-ai-writing-cheat-sheet  
The cheat sheet itself is paywalled (paid Substack newsletter), but the preview is free and contains useful framing. Worth subscribing to if you work on AI-assisted content regularly. Orbach's diagnosis: "The problem is that AI writes in very specific patterns that are invisible to the writer but obvious to everyone reading."

### AI Phrase Finder: The 50 Most Common AI Phrases
**URL:** https://aiphrasefinder.com/common-ai-phrases/  
Annotated list with explanations for why each phrase signals AI authorship. Companion reference to the word list in this folder.

---

## A note on AI detection tools

Tools like GPTZero, Originality.AI, and Turnitin score text for the probability that it was AI-generated. For most RDC use cases, these tools are not the primary concern — the goal is producing content that reads well and serves the client, not passing a scanner.

That said, some clients may use detection tools internally or as part of a review process, particularly in regulated industries or public sector contexts. If that's a concern for a specific project, the best approach is still the same: apply the editorial workflow above. Content that has been genuinely edited to sound human — with specifics, varied rhythm, real sources, and an actual point of view — tends to score better on detectors as a byproduct of being better writing.

Running a piece through a humanizer tool (software designed to automatically rewrite AI text to evade detection) is not a recommended substitute for editorial work. These tools can improve detection scores without improving the writing, and experienced readers can still tell.

---

## Quick setup checklist for new RDC writers

- [ ] Set up custom instructions in Claude, ChatGPT, or Gemini using the prompt above
- [ ] Add a personal voice note (2–3 sentences) at the end of the custom instructions
- [ ] Save the general rewrite prompt somewhere accessible (notes app, bookmark, text file)
- [ ] Read the RDC conceptual guide once through
- [ ] Keep the word and phrase list open while editing AI-assisted drafts
- [ ] Before submitting anything: run the editorial checklist in the conceptual guide
