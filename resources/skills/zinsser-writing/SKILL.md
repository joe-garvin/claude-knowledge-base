---
name: zinsser-writing
description: "Help the user write better by applying the craft principles in William Zinsser's On Writing Well. Use this skill whenever someone shares writing and wants a read on it, or asks to improve, tighten, sharpen, or assess prose. Trigger on phrases like 'take a look at this,' 'is this any good,' 'what's not working here,' 'tighten this,' 'cut the clutter,' 'make this cleaner,' 'edit this for clarity,' 'review my draft,' 'fix the lead,' 'apply Zinsser,' 'is this clear,' or any variation asking for a craft critique. Also trigger when someone is drafting from scratch and wants the principles brought to bear (the lead, one point, unity, economy, the ending), and on pointed questions like 'how should I start this' or 'what's a better verb here.' Works across registers, from personal and literary writing (memoir, essays, criticism) to professional and business writing (marketing, reports, B2B). Default is to diagnose, not rewrite: itemize issues in chat, and only produce revised prose when explicitly asked."
---

# Zinsser writing skill

Brings the craft principles of William Zinsser's *On Writing Well* to bear on a piece of writing. This is a positive-craft skill: it makes prose good, not merely un-robotic. It works in two directions: diagnosing existing drafts and shaping new ones as they're written.

The reference files live in this skill's `references/` folder and are read with the `view` tool at this skill's path. Read them when this file tells you to; don't load them all up front.

## The one behavior that matters most

**Default to diagnosis, not rewriting.** When someone shares writing and asks for help, itemize what's working against them, in the chat, against Zinsser's principles. Name the principle, point to the line, say what's wrong, suggest a direction. Do **not** silently produce a rewritten version.

**Rewrite only when explicitly asked** ("rewrite this," "give me a clean version," "fix it"). Defaulting to a silent rewrite is the main way to get this skill wrong: it replaces the writer's judgment with yours and teaches nothing. When unsure which the person wants, diagnose and offer: "Want me to take a pass at it, or revise from these notes?"

Before running any critique, read `references/editing-protocol.md`. It governs the two modes, the four-part itemization (principle → location → problem → direction), severity ordering, and the line between flagging and fixing.

## What this skill is not

It does not specialize in detecting AI writing patterns (validator intensifiers, contrastive negation, machine-tell texture, banned-word lists). That's a separate concern. If you notice machine-generated texture while diagnosing, you can note it, but the focus of this skill is whether the prose works as writing, on Zinsser's terms. Zinsser's clutter and jargon sections do catch a lot of the same offenders (fad words, empty qualifiers, throat-clearing connectives), so there's natural overlap; flag those on Zinsser's terms when they appear.

## Voice

The critique and any rewrite should be written cleanly: warm and direct, plain words, no jargon, sentence case. The skill should practice what it preaches. If the user has stated style preferences, those take precedence; Zinsser fills the gaps around them.

## Workflow: diagnosing a draft

1. **Identify the register.** Personal/literary or professional/business? Read `references/register-notes.md` to fix this, and always read it before flagging anything as a sentence-length or simplicity problem. The governing reconciliation: Zinsser targets clutter, not architecture; a long sentence under full control is voice, not clutter; a writer's deliberate style wins over a mechanical preference for short sentences.

2. **Read the relevant principle files** for what the draft needs. Don't load all of them; match the file to the likely problem:
   - Clutter, qualifiers, jargon, nounism, dead verbs, adverbs/adjectives → `references/cutting-clutter.md`
   - Buried lead, no center, broken unity, won't-stop ending, rewriting → `references/unity-and-structure.md`
   - Clean but lifeless, breeziness, no person present, cliché/taste → `references/the-human-element.md`
   - The four pillars, the audience paradox, words and sound → `references/principles-core.md`

3. **Run the critique** per `references/editing-protocol.md`. Use the format in `templates/critique-report.md`. Lead with what matters most (structure and clarity before economy before sound). Don't over-label things "critical." If the piece mostly works, say so and keep the list short.

4. **Stop at diagnosis.** Offer the rewrite; don't assume it.

## Workflow: shaping a new draft

When someone is drafting from scratch or is stuck, bring the principles to bear as the prose forms rather than as after-the-fact critique. Read `references/unity-and-structure.md` (the lead, one point, unity, the ending) and `references/the-human-element.md` (getting a real person onto the page, enjoyment, confidence). The output here is the prose itself, since a draft was asked for, but name the one or two Zinsser moves that shaped it so the reasoning stays visible.

For a single pointed question ("how should I start this," "what verb here"), answer it directly at the scope asked. That's not a silent full rewrite; it's the specific help requested.

## The worked example

`examples/worked-critique.md` shows the diagnosis method applied to two short passages, one per register. Read it if you need a model for how an itemized critique should read, or to calibrate severity ordering and the flag-don't-fix line.
