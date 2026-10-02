# LEAP ROUND — brief (common to all leap agents)

## Why this round exists
The program has moved through three architectures: (1) a three-nail hand on a desk arm, (2) the same hand on a head-resting crown, (3) a "porcupine" helmet: dozens of spring-loaded thin pins with nail tips on an inner shell moved by two servos, with a one-motor selector choosing which 3–5 pins touch. The last step was a genuine leap because it DECOUPLED three things that earlier designs had welded together: which contacts are active (selector), how contacts move (shell drive), and what sets the force (per-pin spring). Michael now wants agents whose sole job is to find the NEXT leap: a change in design strategy that could step-change the scratching experience, not an incremental improvement to the porcupine.

## What "the experience" means (read these; they are the spec)
01-foundations/scratch-model.md (§1 phenomenology, §2 receptors, §3 numbers, §4 human patterns, §7 ranked variables, §8 massager-vs-scratcher checklist, §9 unknowns) · 01-foundations/prior-art.md (§2 neuroscience corrections; what to borrow/avoid) · 01-foundations/hair-interaction.md (what hair does) · 01-foundations/tip-interface.md (what the nail does). Skim 03-tournament/DECISION.md, 04-redteam/redteam-1-sensation.md, 10-porcupine/PORCUPINE-BRIEF.md and 10-porcupine/pin-unit.md §1 to know the current state. Skim 02-mechanisms/*.md summaries (first 60 lines each) so you do not re-propose what was already explored.

## Rules
- Do not optimise the porcupine. Attack the frame it sits in. Ask what assumption every design so far shares and what happens if it is false.
- A leap must be arguable from the physics/physiology of the sensation (scratch-model, prior-art), not from novelty. For each candidate, say which sensory variable it moves and by how much (even roughly).
- Physical plausibility is required; cost/buildability is secondary at this stage, but say what it would take.
- Produce 3–5 candidate leaps. For each: (a) the shared assumption it breaks; (b) the principle in one paragraph with a sketch (ASCII or SVG); (c) why it could step-change the sensation, tied to scratch-model §1–§3 and §7; (d) physical plausibility with numbers; (e) the cheapest experiment that would show whether it works (ideally < $50, < 1 weekend); (f) what it would replace or combine with in the current architecture; (g) the honest reason it might not work.
- End with your single best bet and a one-paragraph case for it.
- Firewall: do not read other 11-leaps/*.md files.

Write 2000–4000 words to 11-leaps/leap-<LETTER>.md. Reply with ≤200 words: your 3–5 leaps in one line each and your best bet.
