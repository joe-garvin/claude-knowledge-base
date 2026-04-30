# Avoiding AI tells in client content: a guide for RDC writers

For Red Door Collaborative writers using Claude, ChatGPT, or Gemini to assist with client work. Covers what makes AI-assisted writing recognizable, why it matters for clients like Microsoft, Databricks, and the City of Seattle, and what to do about it.

---

## Why this matters

AI-assisted writing has a recognizable signature. Your clients' audiences — the developers reading a Databricks blog post, the IT administrators reading a Microsoft glossary, the city employees reading a Seattle newsletter — encounter enough AI-generated content to have developed an instinct for it. They can't always explain why something feels off, but they feel it, and when they do, they stop trusting the content. More critically, they stop trusting the brand behind it.

The goal isn't to hide that you used AI. The goal is to produce writing that reads as if a knowledgeable person wrote it — because in the best version of the AI-assisted workflow, a knowledgeable person did. You used AI as a drafting tool, and then you did your job as a writer.

Tom Orbach, a Director of Growth Marketing at Google, puts it bluntly: "Every time they scroll past, you lose a tiny bit of credibility. And credibility, once lost, is really hard to earn back."

---

## What "sounds like AI" actually means

The recognition is usually faster than the analysis. A reader encounters a paragraph and something fires — this is machine-made — before they can articulate why. That instinct is responding to a cluster of overlapping signals.

### Vocabulary

AI gravitates toward a small rotation of words that sound authoritative but add nothing. You've seen them. They cluster into recognizable families:

**Elevation verbs** that sound formal but are vague: *delve, harness, leverage, navigate* (used figuratively), *streamline, foster, cultivate, empower, spearhead.*

**Approval adjectives** that assert quality without demonstrating it: *robust, seamless, comprehensive, cutting-edge, pivotal, holistic, multifaceted, transformative, innovative, groundbreaking.*

**Metaphor nouns** borrowed from a corporate thesaurus: *landscape, tapestry, realm, ecosystem, beacon, symphony, cornerstone, paradigm.*

**Fancy substitutes for "is" and "has"**: *serves as, features* (used as a verb), *boasts, presents, encompasses, underpins.*

These words are massively overrepresented in AI text. Research found that words like these spiked in published writing by over 50% after ChatGPT launched — including in human writing, as writers unconsciously absorb AI's vocabulary. The fix is almost always simpler: "use" instead of "leverage," "strong" instead of "robust," "smooth" instead of "seamless."

**The canonical example: "delve."** This word became the public shorthand for AI writing because ChatGPT used it at such frequency it became a meme. "Let's delve into this topic." It sounds thorough and it says nothing. It's now so associated with AI that many editors flag it on sight.

### Phrases and structure

Beyond individual words, AI produces recognizable phrase patterns:

**Scene-setting openers** that delay the actual point: "In today's rapidly evolving digital landscape…" "In an era where [X]…" "In the realm of…" These are how AI warms up before saying anything. For a Microsoft blog post or a Databricks technical article, they read immediately as filler.

**Significance inflation** applied to routine things: "marking a pivotal moment in the evolution of," "a watershed moment for the industry," "a testament to human ingenuity." AI treats every development as historic. If you can delete the inflation phrase and the sentence still works, delete it.

**The "not X, it's Y" construction**: "It's not just a platform — it's a paradigm shift." "This isn't about speed. It's about trust." These mimic the shape of insight without containing any.

**Vague attribution**: "Experts believe," "Studies show," "Research suggests." AI can't name the expert or the study because it's approximating. For a Microsoft or Databricks piece, this is a credibility problem — their audiences know how to look things up.

**Filler transitions**: "Moreover," "Furthermore," "Additionally," "In conclusion," "It's worth noting that." These are AI's essay-structure scaffolding. They signal a paragraph is ending rather than connecting it to the next idea.

**The false balance**: AI presents multiple perspectives even when one is clearly stronger, hedging with "perhaps," "could potentially," "it's important to note." This is AI protecting itself from being wrong. For client content that's supposed to have a point of view, it reads as mealy-mouthed.

### Structure

AI defaults to a predictable architecture across almost any piece: broad contextual opening → enumerated points or bulleted list → summary conclusion that restates what was just said. It tells you what it's about to do, does it, then tells you what it just did.

The most flagged single pattern: bullet lists where each item starts with a **Bold term:** followed by an explanation sentence. If you've seen this in an AI draft, you know what it looks like. It's everywhere. It's also the strongest single structural signal of AI authorship.

Other structural tells:
- Every paragraph roughly the same length
- Every sentence roughly the same length (15–25 words, metronomic)
- Excessive headers and subheaders in short pieces
- "Overview," "Key Points," "Summary," "Conclusion" as section headers — AI scaffolding, not editorial judgment

### Cognitive tells

These are subtler but often what readers are actually responding to when they feel something is "off":

**No genuine opinion.** AI is relentlessly neutral. Pieces that are supposed to take a position — a Databricks thought leadership post, a Microsoft perspective piece — need to actually argue something. AI defaults to presenting both sides and landing nowhere.

**No specific experience.** AI cannot have been somewhere, tried something, or changed its mind. For content where personal or professional experience would naturally appear, its absence reads as hollow.

**No specificity.** AI says "many organizations" instead of naming one. It says "significant improvement" instead of citing a number. It says "experts" instead of naming a person. Specifics are what make content trustworthy. Specifics are also what AI can't generate reliably — it will sometimes invent them, which is a different problem.

**Emotional claims without emotional content.** "What surprised me most," "I was fascinated to discover," "What struck me was." If the content doesn't earn the emotion, the claim is just a flag. State the surprising thing; let the reader be surprised.

**Chatbot residue.** Phrases that belong in a chat interface and not in a published piece: "I hope this helps!", "Great question!", "Certainly!", "Let me know if you need anything else," "In this article, we will explore," "Let's dive in!" Remove on sight.

---

## The RDC editorial workflow

Here's a practical sequence for catching and fixing AI tells before anything goes to a client.

### Step 1: Rewrite the opener yourself

The first two or three sentences are the highest-density location for AI tells — introductions are where AI patterns cluster most. Don't just edit the AI's opener. Replace it entirely, in your own voice, with the actual point. Delete the grand contextual statement. Start with the news, the claim, or the specific.

Bad: "In today's rapidly evolving cloud landscape, organizations are increasingly turning to data intelligence platforms to drive competitive advantage."

Better: "Databricks just made it significantly easier to query across cloud providers without moving data. Here's what that means for how your team builds pipelines."

### Step 2: Run the vocabulary pass

Go through the piece looking specifically for Tier 1 flagged words — the ones that should always be replaced. See the word and phrase list for the full table. This is the most mechanical step and the fastest to execute. "Leverage" → "use." "Robust" → "strong." "Seamless" → "smooth." "Tapestry" → [describe the actual thing].

### Step 3: Break the structure

Identify the AI default scaffold (broad opener → list → summary) and disrupt it. Lead with the point instead of building toward it. If there's a bullet list in every section, ask whether the content actually warrants a list or just defaulted to one. Convert bulleted items into prose where the content is sequential thinking, not a genuine enumeration.

Specifically: if you see the **Bold term: explanation** list pattern, rewrite it as prose. Every time.

### Step 4: Inject specifics

Find every vague attribution and replace it with a real source. Find every round number or sweeping claim and replace it with something verifiable. For Microsoft and Databricks content especially — where the audiences are technical and will notice — vague claims erode trust quickly.

"Experts believe this approach reduces latency" → "According to Databricks' 2024 benchmark, this approach reduced query latency by 40% in production environments."

If you can't verify a specific claim AI generated, remove it or rephrase it as a general point. AI hallucinates citations confidently. Always check.

### Step 5: Add what only a writer can add

This is the step most people skip. AI can draft a structure. It cannot have a perspective on the City of Seattle's actual procurement challenges. It cannot have a sense of humor about enterprise software. It cannot have heard something at a conference last month that changed how you think about Databricks' positioning.

Where the piece is supposed to have a voice, give it one. Where it's supposed to take a position, take one. Where an expert quote or a specific example would add credibility, get it — HARO (relaunched 2025), LinkedIn, and the client's own internal subject matter experts are all sources.

### Step 6: Read it aloud

This is not optional. Reading aloud surfaces the metronomic rhythm that reading silently misses. If every sentence sounds like it could be delivered by a text-to-speech engine without sounding weird, the rhythm is too uniform. Human writing has natural variation — some sentences short, some longer, some that break the pattern entirely with a fragment or a question.

If you stumble over a sentence, rewrite it. A reader will stumble there too.

### Step 7: Check the opener and the close

Delete any opening sentence that makes a grand statement about the state of the world. Start with the second sentence.

Delete any closing that says "The future looks bright," "Only time will tell," "As we move forward," or "This is just the beginning." These are AI's generic wrap-ups. End on something specific to the piece's argument.

---

## Content type notes

### Blog posts and thought leadership
These are the highest-stakes format for AI tells because readers engage closely with prose arguments. Structural tells (the scaffold, the bullet-list default) and epistemic cowardice (the false balance, the hedge) matter most here. The piece should argue something. Take the position.

### Glossary pages and technical explainers
The vocabulary tells matter most here because these pieces depend on precision. AI often uses technically adjacent words that are slightly off — close enough to sound authoritative, not accurate enough to be useful to a developer or IT administrator. Verify definitions against primary documentation (Microsoft Docs, Databricks documentation) rather than trusting AI summaries.

### Video scripts and show copy
Sentence rhythm is the primary concern here — the script will be read aloud. Uniform rhythm is more noticeable in voice than on the page. Scripts also need natural contractions, interruptions, and the small irregularities that make spoken language feel human.

### Social copy
Short-form content exaggerates AI tells because there's no room to hide them. "Harness the power of" in a 120-character LinkedIn post is deafening. Every word earns its place. Enthusiasm should be specific: say what's worth being excited about.

### Newsletters
Mix of the above. Watch especially for the significance inflation pattern — newsletter leads that treat every development as historic. Write news items the way a well-read colleague would summarize them, not the way a press release would.

### Slide deck copy
Bullet-heavy by nature, which means the **Bold term: explanation** pattern needs active management. If slide bullets are all the same length and all follow the same grammatical structure, break the uniformity. Fragments are fine on slides. Short declarative statements read better than noun-phrase constructions.

### E-books
Long-form. The metronomic rhythm problem compounds over length. Build in deliberate variation — short chapters, section breaks, occasional one-sentence paragraphs that punctuate the pace. The scaffold problem is acute here: AI will produce an e-book with a perfect, dead-symmetric structure. Break it.

### Infographic copy
Ultra-compressed. Every word is a decision. AI-isms at this scale are brutal — a single "leverage" in a headline reads immediately as machine-made. Write infographic copy yourself; use AI for research and structure suggestions, not headline copy.

---

## The pattern that underlies all of it

AI is optimized to produce what is most expected next. Every pattern on this list — the vocabulary, the structure, the epistemic hedging — is the output of a system trying to produce the most statistically likely good-sounding text.

That optimization produces writing that is grammatically correct, structurally tidy, and stylistically inert. It reads like the average of a billion documents rather than the work of any individual. The fix isn't a different AI tool. It's a writer who knows what they're doing, using AI as a drafting tool and then doing the actual job.

---

## Quick reference checklist

Before submitting any AI-assisted piece:

- [ ] Opener rewritten by hand — no grand contextual statement
- [ ] Vocabulary pass complete — Tier 1 flagged words replaced
- [ ] No **Bold term: explanation** bullet list pattern
- [ ] No "It's not X, it's Y" constructions
- [ ] No vague attributions — every claim either sourced or reframed
- [ ] Structural scaffold broken — piece leads with the point
- [ ] Specifics injected — names, numbers, dates, examples
- [ ] Read aloud — rhythm varied, no press-release sentences
- [ ] Closing is specific — no generic wrap-up phrases
- [ ] Chatbot residue removed — "Certainly!", "I hope this helps!", etc.
