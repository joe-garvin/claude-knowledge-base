# Writers and content specialists — interview guide

## Role context

Writers at RDC produce a wide range of content types: blogs, glossary pages, ebooks, customer stories, newsletters, video scripts (for shows like Azure Essentials Show), social copy, and executive documents. Most projects involve working from a client brief or source material, adapting content to a known structure, and going through multiple review rounds with clients and internal stakeholders.

Common work patterns:
- Receiving a brief or source deck and translating it into a draft
- Iterating through v1 → v2 → v3 revisions based on client feedback
- Writing to a known format/template that varies slightly project to project
- Starting new projects in a new chat with no context from previous work
- Managing several active projects simultaneously across different clients

## Likely friction areas to probe

- **Cold starts**: Starting a new chat with no project context, having to re-explain voice, format requirements, or client background every time
- **Reformatting output**: Claude's default formatting doesn't match their preferred style and requires cleanup
- **AI-isms in drafts**: Catching and rewriting AI-generated language patterns after the fact
- **Brief-to-draft translation**: Turning a vague or incomplete brief into a first draft that's on-structure and on-voice
- **Revision tracking**: Writing up what changed between versions, why it changed, and communicating that clearly
- **Research synthesis**: Pulling from multiple source documents without losing track of what came from where
- **Script-specific challenges** (if applicable): Managing the outline-then-script sequence, calibrating technical depth for audience

## Question sequence

**Q3 — Content mix** (buttons):
> "What types of content do you write most often?"

Options: Long-form (ebooks, guides, reports) / Blog posts and glossary content / Decks and presentations / Video scripts or show content / Social copy and short-form

**Q4 — Where time goes** (buttons):
> "On a typical project, which part usually takes the most time?"

Options: Getting started — figuring out structure, angle, or approach / The actual writing and drafting / Revisions and incorporating feedback / Reformatting or cleaning up output / Something else

**Q5 — The frustrating part** (buttons):
> "What's the part of writing work that you find most draining or tedious?"

Options: Starting from scratch when I already know the structure / Cleaning up drafts so they don't sound like AI wrote them / Keeping track of what changed between versions / Re-explaining context every time I start a new chat / Something else

**Q6 — Drill-down** (buttons, branch on Q5 answer):

If "starting from scratch":
> "When you sit down to start a new draft, what usually slows you down most?"
Options: Not knowing where to begin with structure / Having to re-read all the source materials / Having to remind Claude of the client voice and format every time / Getting a first draft that misses the mark / Something else

If "cleaning up AI writing":
> "When you get a Claude draft and it doesn't sound right, what's usually wrong with it?"
Options: Vague, hedge-y language that doesn't say anything concrete / Sentences that are too long or too formal / Transitions that feel generic ("Additionally...", "Furthermore...") / Structure that's correct but doesn't flow like how we write / Something else

If "revision tracking":
> "What's the messiest part of managing revisions?"
Options: Remembering what changed between rounds and why / Writing up version summaries for the client or PM / Keeping track of what feedback was addressed / Managing conflicting feedback from multiple reviewers / Something else

**Q7 — Open-text moment** (see Step 4 in SKILL.md)

**Q8 — AI experience** (buttons):
> "Have you used Claude or any AI writing tools before?"

Options: Yes, fairly regularly / A few times, with mixed results / Once or twice but it didn't really stick / Not really

**Q9 — Barrier check** (buttons):
> "What would make an AI solution feel too complicated to be worth trying?"

Options: If it requires a lot of setup or copying in long prompts / If I have to learn a new tool or workflow / If the output still needs a lot of cleanup / If it only works sometimes and I can't rely on it / Something else

## Output guidance

Strong recommendation candidates for this role:
- A reusable project context prompt they paste at the start of any new chat to load voice, format, and client background instantly
- A "clean up the AI-isms" prompt tuned to RDC voice and the specific client's tone
- A version summary: paste notes on what changed, get a clean change summary formatted for the client
- A brief-to-outline workflow: paste the brief, get a structured outline to react to before drafting
- A revision incorporation prompt: paste the draft and feedback, get a revised draft with rationale

Example "Where to start" prompt for the output document:
> "You're helping me write for [client]. Their voice is [brief description]. The format is [brief description]. Here's the brief: [paste brief]. Give me a structured outline to react to before I start drafting."
