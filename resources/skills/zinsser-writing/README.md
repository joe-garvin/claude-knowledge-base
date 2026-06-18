# zinsser-writing

A Claude skill that brings the craft principles of William Zinsser's *On Writing Well* to bear on your writing. It diagnoses drafts and helps shape new ones, across both personal/literary and professional/business registers.

The defining behavior: it **diagnoses rather than rewrites**. When you share a draft, it itemizes what's working against you (named principle, exact line, the problem, a direction to take it) and hands the decision back to you. It produces a clean rewrite only when you explicitly ask for one. The idea, borrowed from Zinsser's own teaching, is to install the editorial eye rather than do the pruning for you.

## What it does

- **Diagnoses a draft.** Share writing and ask for a read. You get an itemized critique ordered by what matters most: structure and clarity first, then economy, then sound and freshness. No silent rewrite.
- **Shapes a new draft.** When you're starting from scratch or stuck, it brings the principles to bear as the prose forms: the lead, one point, unity, economy, the ending.
- **Answers pointed questions.** "How should I start this?" or "what's a better verb here?" gets a direct answer at the scope you asked, not a full rewrite.
- **Reads register.** It distinguishes personal/literary writing (memoir, essays, criticism) from professional/business writing (marketing, reports, B2B) and flexes the principles accordingly. Zinsser targets clutter, not architecture, so a long sentence under control is treated as voice, not a defect.

## How to use it

Drop the `zinsser-writing/` folder into your Claude skills directory. The skill triggers on natural requests like:

- "take a look at this"
- "is this any good?"
- "tighten this" / "cut the clutter"
- "edit this for clarity"
- "fix the lead"
- "how should I start this?"

It stays in diagnosis mode by default. To get edited prose back, say so directly: "rewrite this," "give me a clean version," "fix it."

## What's in the folder

```
zinsser-writing/
├── SKILL.md                        the entry point and routing logic
├── README.md                       this file
├── references/
│   ├── principles-core.md          the four pillars, audience, words and sound
│   ├── cutting-clutter.md          the clutter catalog and how to remove it
│   ├── unity-and-structure.md      the unities, the lead, the ending, rewriting
│   ├── the-human-element.md        voice, taste, enjoyment, confidence
│   ├── editing-protocol.md         the two modes and how to itemize a critique
│   └── register-notes.md           how the principles flex between registers
├── templates/
│   └── critique-report.md          the shape of an itemized diagnosis
└── examples/
    └── worked-critique.md          two diagnosed passages, one per register
```

Claude reads the reference files on demand, matching the file to the problem at hand rather than loading everything up front.

## A note on customization

The skill respects stated style preferences: if you've told Claude how you want your writing to read, those preferences take precedence and Zinsser fills the gaps around them. Out of the box it does the general craft work without assuming anything about your voice.

It deliberately stays out of one lane: detecting AI writing patterns (validator phrases, contrastive negation, machine-tell texture). Zinsser's clutter and jargon material catches many of the same offenders, so those still get flagged, but a dedicated AI-pattern pass is a separate concern from the craft assessment this skill performs.

## Credit

Built on the principles in William Zinsser's *On Writing Well* (HarperCollins). The book is the source; this skill is a tool for applying it, not a substitute for reading it. If the principles here are useful to you, read the original.

## License

Released for public use. Adapt it to your own workflow.
