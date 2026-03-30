---
name: family-meeting-transcript
description: Process family meeting transcripts related to Mart's mental health crisis coordination. Use this skill whenever the user provides a meeting transcript, asks to "analyze this family meeting," wants a "meeting summary," mentions processing or reviewing a family meeting recording, or says anything about creating summaries or action items from family coordination meetings. Also trigger when user uploads audio/text files that appear to be meeting transcripts, especially if they mention family members (Mom, Dad, Matt, Steve, Joe) or Mart's situation.
---

# Family Meeting Transcript Processor

Process transcripts from family coordination meetings about Mart's ongoing mental health crisis (Episode 4, bipolar disorder with substance use). Creates concise summaries for family distribution and detailed analysis for strategic planning.

## Context

**The situation:**
- Mart (age 39): Bipolar I disorder + alcohol use disorder
- Episode 4 crisis cycle: December 2025 - ongoing March 2026
- Multiple hospitalizations, failed rehab, foreclosure proceedings
- Family coordination team: Mom, Dad, Matt, Steve, Joe
- Active interventions: AR Intervention (social work), SSDI application, permanent supportive housing research, potential AOT/conservatorship

**The family:**
- **Mom & Dad**: Primary caregivers, bearing heaviest burden, experiencing burnout
- **Matt** (youngest brother): Protective of parents, boundary-focused, direct communicator
- **Steve** (third brother): NYC-based, analytical, neutral stance with Mart
- **Joe** (second brother): Bellingham WA-based, documentation lead, strategic coordinator

**Key ongoing issues:**
- Mart still manic as of March 2026 (3+ months post-hospitalization)
- Cathy Tobben (girlfriend/informal case manager) ended relationship early March
- House foreclosure (March 9 court date, auction estimated Aug-Sept)
- No Release of Information (ROI) - family cannot coordinate with providers
- Voluntary treatment repeatedly failed
- Strategic shift toward structural solutions (AOT, SSDI, PSH, conservatorship)

## Core Workflow

When user provides a meeting transcript:

1. **Read the transcript carefully**
   - Note meeting date, participants, duration
   - Identify key topics discussed
   - Track who said what (especially strategic positions)
   - Notice what WASN'T discussed (often revealing)

2. **Create the family meeting summary** (2-3 pages max)
   - This goes to the whole family via email
   - Format: Markdown, sentence case headings
   - Length: Concise but substantive - aim for ~2000-2500 words
   - Tone: Clear, direct, factual, slightly warm
   
3. **Provide strategic analysis** (for Joe's reference)
   - Patterns observed
   - Strategic implications
   - What's working / not working
   - Underlying tensions or disagreements
   - What needs to happen next

## Meeting Summary Format

```markdown
# Family meeting summary
[Date]

**Participants:** [List]

---

## [Topic 1 - Use descriptive section names]

**Specific development:**
- Key point about this development
- Another detail with concrete facts
- Direct quote if impactful: "exact words from transcript"

**Related subtopic:**
- Specific information
- Another bullet with 1-2 sentences max
  - Sub-bullet for additional detail if needed
  - Keep sub-bullets concise too

## [Topic 2]

**What happened:**
- Bullet point
- Bullet point
- Bullet point

**Decision made:**
- What was decided
- Why it matters

## Action items

**[Person]:**
- Specific task with deadline
- Another assigned task

**[Person]:**
- Their task

## Next meeting

- When scheduled (or TBD)
- What will be assessed
- Any specific agenda items mentioned

---

## [Optional: Overall sentiment or realistic assessment]

- Brief assessment if appropriate
- Keep to bullets even here
```

### Section naming principles

- Use **descriptive, specific section names** that tell you what's in the section
- Good: "AR Intervention update," "SSDI application timeline," "Foreclosure developments"
- Bad: "Updates," "Discussion," "Next steps"
- Good: "Family discussion: AR Intervention approach" 
- Bad: "AR Intervention" (too vague - update? decision? problem?)

### Content organization rules

1. **Group related information together** - don't scatter the same topic across multiple sections
2. **Lead with most important/actionable items** - Mart's status, immediate decisions, urgent matters
3. **Use bold subheadings** to break up content within sections - but sparingly, only when genuinely helpful
4. **NO PARAGRAPHS - USE BULLETS EXCLUSIVELY**: Every section must use bulleted lists. Never write blocks of text or paragraphs. Break all content into scannable bullet points.
5. **Bullet points**: Keep bullets concise (1-2 sentences max). Each bullet should be a discrete piece of information. If a bullet runs long, break it into sub-bullets.
6. **Paraphrase, don't quote**: Summarize what was said in your own words. No direct quoted phrases or sentences - this is too granular for a high-level record-keeping document.
7. **Numbers/specifics**: Always include concrete details (dates, dollar amounts, timelines) but skip minor specifics
8. **High-level overview**: This is for record-keeping and scanning - key takeaways only, not comprehensive detail

### What to emphasize

- **Decisions made** - be explicit about what was decided
- **Key developments** - major changes or new information only
- **Mart's current status** - high-level overview, not every detail
- **Action items** - who's doing what by when
- **Timeline pressures** - important dates only (foreclosure, appointments, deadlines)
- **Strategic positions** - when family members have different views (Mom vs brothers on AOT, boundaries, etc.)

### What to downplay or omit

- Lengthy explanations of things the family already knows
- Repetitive discussion that didn't lead anywhere
- Small talk, pleasantries, off-topic tangents
- **Granular details and play-by-play** - this is high-level record-keeping, not transcript
- **Every single thing discussed** - only key takeaways per topic
- **Direct quotes** - paraphrase instead; quotes are too detailed for this document
- **Minor specifics** - keep dates/numbers but skip small details

### Tone and style requirements

**DO:**
- Write in clear, direct sentences
- Use active voice
- Be specific and concrete
- Sound like a competent family member writing to other family members
- Include just enough warmth to not sound robotic
- Use "Mom said" / "Matt pointed out" / "Steve offered" - attribute quotes naturally
- **Make it scannable: bullets only, no paragraphs anywhere**
- Keep individual bullets to 1-2 sentences maximum
- Use sub-bullets when you need to add detail

**DO NOT:**
- Use AI-isms like "it's not X, it's Y" constructions
- Over-format with excessive headers/bullets/bold text
- Sound like a corporate meeting minutes
- Use phrases like "delve into," "navigate," "landscape," "unpack"
- Include meta-commentary about the summary itself
- Apologize or hedge unnecessarily
- Use title case for headings (always sentence case)
- **Write paragraphs or blocks of text - bullets only**

### Length calibration

- Target: **Maximum 2 pages** when formatted as Google Doc
- Rough word count: **1500-2000 words MAX** 
- This is a high-level overview for record-keeping, not a detailed transcript
- If first draft exceeds this, condense by:
  - Raising level of abstraction
  - Removing granular details
  - Combining related bullet points
  - Cutting secondary information
  - Keeping only key takeaways per topic

**Length test**: If it would take more than 3-4 minutes to read aloud, it's too long.

## Strategic Analysis Format

After creating the summary, provide separate analysis covering:

### Patterns and observations

- What keeps coming up across meetings?
- Where is there family alignment vs. divergence?
- What's the gap between what's said vs. what's happening?
- Behavioral patterns in Mart (if discussed)
- Family dynamic patterns

### Strategic implications

- What does this meeting tell us about the trajectory?
- What's working? What's clearly not working?
- Where is the family stuck?
- What needs to shift?

### Tensions and disagreements

- Where do family members disagree (even if not explicitly stated)?
- Common: Mom's hope vs. brothers' realism
- Common: desire for voluntary cooperation vs. need for structural intervention
- Common: immediate safety vs. long-term solutions

### What needs to happen next

- Based on this meeting, what are the logical next steps?
- What's urgent vs. important?
- What's being avoided that shouldn't be?

### Assessment of progress

- Is the family moving forward or treading water?
- Are structural solutions advancing or stalled?
- Is Mart's condition improving, stable, or deteriorating?

## Special Situations

### When transcript quality is poor

- Auto-generated transcripts often have speaker misattributions
- Use context clues (Mom/Dad mention each other, brothers reference each other)
- Note when uncertain: "Unclear who said this, but someone mentioned..."
- Focus on content over perfect attribution

### When multiple transcripts provided

If user provides two versions (auto-transcript + manual cleanup):
- Prefer the manually cleaned version
- Cross-reference if unclear
- Note in analysis if transcripts diverged significantly

### When meeting was short/urgent

- Emergency meetings get shorter summaries (1-2 pages)
- Focus only on the urgent issue discussed
- Note that it was emergency/short meeting

### When Joe wasn't present

- Note Joe's absence at top
- Rely on other participants for his views if referenced
- Summarize as if for someone who wasn't there (which Joe wasn't)

## Common Meeting Types

### Regular weekly family meetings

- Broadest scope - Mart's status, multiple workstreams, coordination
- Usually 45-60 minutes
- Summary should cover all active tracks (AR, SSDI, housing, foreclosure, etc.)

### Emergency/crisis meetings

- Focused on single urgent issue
- Shorter (15-30 minutes)
- Summary should be brief, action-oriented

### Strategic planning meetings

- Discussing longer-term approaches (AOT, conservatorship, housing)
- May involve significant disagreement/alignment building
- Summary should capture strategic positions clearly

### Post-event debrief meetings

- After hospitalization, discharge, major incident
- Focus on what happened and immediate response
- Summary should clarify timeline and next steps

## Quality Checks

Before finalizing summary, verify:

- [ ] Title and date clear
- [ ] Participants listed
- [ ] **Maximum 2 pages (ideally 1.5-2 pages)**
- [ ] **Word count 1500-2000 words MAX**
- [ ] Sentence case headings throughout
- [ ] No AI-ism phrases
- [ ] **ALL content in bullets - zero paragraphs or text blocks**
- [ ] **Individual bullets are 1-2 sentences max**
- [ ] **No direct quotes - paraphrase everything**
- [ ] **High-level overview only - not comprehensive detail**
- [ ] Action items clearly assigned
- [ ] Next meeting specified if mentioned
- [ ] Important dates/numbers included (skip minor specifics)
- [ ] Tone is clear and slightly warm, not corporate
- [ ] Strategic positions captured when they diverge
- [ ] Most important content first
- [ ] **Highly scannable - someone can skim entire doc in 60 seconds**
- [ ] **Reads like record-keeping document, not meeting transcript**

## Example Feedback Patterns

**If user says "too long":**
- Cut to 60-70% of current length
- Remove explanatory sections family already knows
- Tighten bullet points
- Combine related sections
- Focus only on decisions and new information

**If user says "too detailed":**
- Raise level of abstraction
- Remove play-by-play, keep only outcomes
- Cut tangential discussions
- Focus on "what was decided" not "how we got there"

**If user says "sounds too AI":**
- Remove excessive formatting (headers, bold, bullets)
- Write in more natural voice
- Vary sentence structure
- Remove hedging language
- Make it sound like a smart family member wrote it, not a committee

**If user asks for "action items":**
- Create clear action items section at end
- Format: **[Person]: Specific task by deadline**
- Only include actual assignments, not vague hopes

## Context Integration

The skill should pull from uploaded project files for background:
- Current_Situation_Snapshot_March2026.docx
- Understanding_Marts_Illness_March2026.docx  
- Family_Coordination_Decisions_March2026.docx

Use these to:
- Understand family member roles and perspectives
- Know which issues are ongoing vs. new
- Contextualize strategic positions
- Avoid over-explaining established facts

## Final Notes

- **Primary audience**: The whole family (Mom, Dad, Matt, Steve, Joe)
- **Primary purpose**: High-level record-keeping for scanning and reference
- **Secondary purpose**: Shared understanding of key decisions and next steps
- **NOT a comprehensive transcript**: This is a summary, not a detailed account
- **Tone target**: Professional family member, not consultant or therapist
- **Length is critical**: Maximum 2 pages - summaries that are too long don't get read
- **Detail level**: High-level overview with key takeaways only
- **Concise ≠ superficial**: Brief but captures what matters
- **Test**: Can someone who missed the meeting scan this in 60 seconds and know the key points?
