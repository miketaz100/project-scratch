# DIRECTOR'S DECISION 2 — SP1 "PUPPET HALO" (2026-10-02)

Supersedes 03-tournament/DECISION.md (desk-arm FLOAT-ARM), 08-crown (crown concepts) and 10-porcupine (full pin helmet) as the SP1 architecture. Those remain in the repo as reference.

## How we got here
Leap round 1 (11-leaps/leap-*.md) → Michael picked the PRESSURE-GATED ORBIT (air pins, force = pressure × area; per-pin landing windows) with a small pad that repositions over the scalp. Round 2 (11-leaps/round-2) replaced the plain circle (curls, hair winding) with straight-line capable drives, added hover-and-bite landings, omni nails, palm skids, the κ-grammar pattern layer; Michael overruled the cradle: HELMET REQUIRED; and asked for CIRCLE AND LINE both. Round 3 (11-leaps/round-3) converged 4/5 on the "puppet": all drive motion generated off-head and copied to the pad through sealed air lines; skeleton halo; slow travel motors at the ear axis.

## Binding decisions (Michael)
1. Head-worn helmet.
2. Pad scrub modes: PRECESSING LINE (default; opposite-direction cranks with ~2.5 % speed difference, ~4.5°/stroke), STRAIGHT LINE (30 mm), CIRCLE (variable radius 0–15 mm), switchable in firmware at any moment.
3. Drive box is a free-standing, portable unit: it must sit on a desk, hang from the back of a chair, or rest on the back of a couch, near a comfortably seated user. Not built into any furniture. One umbilical to the helmet.
4. ONE pad built for SP1. The parts for a SECOND pad (mirror half-bail, twin hands) are bought now and the halo has provisions for it, so it can be added later without redesign.
5. Begin engineering (2026-10-02).

## Binding decisions (Director, from rounds 2–3)
- PUPPET DRIVE: the circle/line synthesiser is a MASTER in the drive box; three sealed lines copy its motion to a FOLLOWER on the pad (leap3-B best bet; leap3-D D2; leap3-E E1). No motors, valves or wires on the pad.
- AIR PINS: force = rail pressure × piston area; mechanical relief cap; vent = lift; valves in the drive box; HOVER-AND-BITE (pins hover ~5 mm above the scalp between bites, leap2-F L3); OMNI NAIL on a trailing neck (leap2-B L2); circle mode lifts each pin fully clear once per revolution (leap3-E E3).
- PAD REGISTRATION: RCC palm with three dome skids (leap3-C C1).
- STRUCTURE: skeleton halo on a bike-helmet-style dial cradle gripping under the occiput; one bail on ear-axis hubs (leap3-D D1, leap3-A L1); travel motors in the ear-axis hub pods with cable drums, spring-balanced (leap3-A L1).
- LISTENING: squeeze egg (leap3-C C3) and the first-use head scan + per-session whorl check (leap3-C C4); IMU/bone-mic listening deferred.
- PATTERN LAYER: κ-grammar + fatigue ledger "score" format (leap2-D D1 + D5); per-region yes-button learner later.
- FAIL-TO-FREE: spring lifts the pad clear on power loss / e-stop (leap3-E E4); hold-to-run + NC e-stop retained; all safety red lines (01-foundations/safety-requirements.md) apply.

## Hypothesis SP1 tests
"Air-pin nails with constant force, hovering and biting along a slowly precessing straight scrub (with circle and straight-line alternatives), on a small pad that drifts over the scalp under a κ-grammar score, feel like a person's fingernails scratching the head, on a helmet light and quiet enough to want to wear every evening."

## NORTH STAR AMENDMENT (Michael, 2026-10-02)
"It doesn't have to feel like actual fingernails, it just has to deliver an on-par scratching sensation."
The success criterion is now: a scratching sensation as satisfying as being scratched well by a person (crisp edge reaching the scalp, right force and speed, coverage, no habituation), NOT the illusion that a human hand is doing it. Person-illusion features (human-likeness of timing, "attention", social cues) drop from requirements to nice-to-haves; anti-habituation variation stays a requirement because habituation kills satisfaction regardless. The massager-vs-scratcher distinction still applies: it must be a SCRATCH, not a massage, vibration or brush.
