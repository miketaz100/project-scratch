# Mechanism Team Brief (common to all teams)

You are one of several INDEPENDENT mechanism-design teams on PROJECT SCRATCH. Other teams exist; you are firewalled from them. Do NOT read any other file in 02-mechanisms/ and do NOT read 01-foundations/prior-art.md (you get prior art after convergence). Do not search the web for existing head-scratcher products; you may search for component data, mechanism references, and physics.

READ FIRST (all required):
- 00-brief/BRIEF.md
- 01-foundations/scratch-model.md  (the sensation spec; sections 3, 7, 8 are your acceptance criteria)
- 01-foundations/hair-interaction.md (rules H-4.x/H-5.x/H-6.x and the 18-item checklist)
- 01-foundations/safety-requirements.md (13 red lines; mechanical force cap principle)
- 01-foundations/tip-interface.md (adopt the SP1-TM1 tip mount; tip family A–H)
- 01-foundations/component-landscape.md (real parts and prices)

YOUR TASK
1. Generate at least 3 distinct concepts within your assigned seed family (plus at least 1 wildcard outside it). One paragraph + ASCII sketch each.
2. Select your strongest concept and develop it to a concept-level engineering design:
   a. Working principle and why it will feel like FINGERNAILS (not a massager) — argue from scratch-model sections 1–3 and 8.
   b. Architecture: where it mounts (head-worn / headband module / stationary lean-in frame / hand-positioned), coverage area, number of contacts, DOF.
   c. Kinematics with numbers: stroke length, velocity profile, cycle rate, lift-off mechanism (mandatory per H-5.2), how irregularity/variation is produced, how region changes happen (or are done manually).
   d. Force path: how normal force is set and mechanically capped (F_max = preload + k·x_max with a hard stop), tangential yield/breakaway, compliance per contact and across scalp curvature.
   e. Hair safety: score yourself on the 18-item checklist from hair-interaction.md; list every gap/joint/rotation within 30 mm of scalp and how it is sealed or eliminated.
   f. Safety: check all 13 red lines; e-stop, fail-safe on power loss, head mount release.
   g. Adjustability: which of force / speed / stroke / frequency / angle / contacts / spacing / pattern are adjustable and how (knob vs reprint vs firmware).
   h. Components: a rough BOM with real parts and prices from component-landscape.md; estimated total cost; printed parts list with approximate sizes.
   i. Buildability in an apartment: fabrication steps, tools, risky tolerances, estimated build hours.
   j. Honest weaknesses, top 5 risks, and what bench test would retire each.
   k. Self-score on the 12-item massager-vs-scratcher checklist (scratch-model §8).
3. Produce one SVG schematic of the selected mechanism (inline in the markdown, simple line art, labeled) showing side view with scalp, hair canopy, tip, compliance element, actuator, and guard.

OUTPUT: write to 02-mechanisms/team-<LETTER>.md (3000–6000 words). Reply with a ≤250-word summary: concept name, one-sentence principle, cost, contact count, coverage, biggest risk.
