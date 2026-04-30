Avoiding AI writing

[View the conceptual guide](ai-writing-tells-guide.md) — the full taxonomy: what AI writing is, why it sounds the way it does, the detection science (perplexity, burstiness, fingerprint persistence), and the complete manual editorial workflow. This is the "understand it" document.

[View the word/phrase list](ai-writing-word-list.md) — the operational reference: the full tiered replacement table (109 Tier 1/2/3 entries), the 50 most common AI phrases, all the structural phrases to cut, and the per-model vocabulary signatures. This is the "use it while editing" document.

[View the tools and resources catalog](ai-writing-tools-and-resources.md) — things other people have built on this topic: the avoid-ai-writing skill and integration instructions, Will Francis's full custom instruction prompt (verbatim), the Nate B. Jones 20-prompt system, all the detection tools with accuracy caveats, all the humanizer tools with their limits, and the full reading list with annotations.

The most counterintuitive finding from this research: AI writing patterns persist even after being rewritten, translated, or summarized by another LLM. The patterns are encoded at the word-distribution level. Running AI text through a humanizer tool or asking a second AI to rephrase it doesn't reliably remove the fingerprint. The remediation *must* involve actual human intervention.

The most actionable structural finding: Pangram Labs (which trains classifiers on 28 million human documents) weights structural regularity *higher* than vocabulary. If you fix all the flagged words but leave sentence length uniform and rhythm metronomic, the text still reads as AI-generated. The word list is necessary but not sufficient.

Install the Will Francis custom instruction prompt in your Claude settings today — it suppresses patterns at generation, which is far less work than editing them out afterward.
