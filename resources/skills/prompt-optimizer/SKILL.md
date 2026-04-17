---
name: prompt-optimizer
description: Compress a long, meandering brain-dump into a concise, actionable prompt. Use this skill whenever the user says things like "optimize this prompt", "compress this", "distill this prompt", "make this shorter", "clean up this prompt", or pastes a long block of text and asks for a tighter version. Also trigger when the user says "run the prompt optimizer" or any variation indicating they want a brain dump turned into an efficient prompt. The output is a compressed prompt ready to copy-paste and run — not a revised document or polished prose.
---

# Prompt optimizer

Compress a long, meandering brain dump into a concise, actionable prompt. Output goes in chat as plain text for copy-paste. After outputting, ask: "Want me to run this?"

## What this skill does

Takes a verbose or disorganized prompt and returns a shorter version that:
- Preserves all load-bearing intent and context
- Drops noise: restatements, throat-clearing, excessive hedging, redundant examples
- Keeps a moderate rewrite level — restructures for clarity and concision, but doesn't strip the prompt down to a skeleton
- Works for any target tool (Claude, Midjourney, GPT, etc.) — compress the intent only, leave tool-specific formatting to the user

## Load-bearing vs. noise

When compressing, distinguish:

**Keep (load-bearing):**
- The core task or instruction
- Constraints that change the output (format, tone, scope, length, audience)
- Specific context the model needs to do the task well (client name, project type, technical details)
- Examples that clarify ambiguous intent
- Explicit exclusions ("don't do X")

**Drop (noise):**
- Restatements of the same idea
- Filler phrases and throat-clearing ("I was thinking maybe...", "So basically what I want is...")
- Over-explanation of why the task matters
- Redundant examples (keep the clearest one, drop the rest)
- Meta-commentary about the prompt itself

## Output format

1. Output the compressed prompt as a plain text block (no label, no preamble)
2. On a new line after the prompt, ask: "Want me to run this?"

Do not explain what you changed or why. Do not add headers or labels to the output. Just the prompt, then the question.

## Intervention level

Moderate rewrite. You may restructure sentences and reorder for clarity, but don't strip so aggressively that the user has to add back essential detail. The output should feel like a tighter version of what they wrote, not a different prompt.
