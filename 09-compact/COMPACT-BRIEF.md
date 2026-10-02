# COMPACT HEAD-WORN MODULE — design sprint brief (common to all teams)

Why: the ring-crown render (and the engineering) shows a ~180 mm tower over the crown: elbow axis at Z +84, a 70–100 mm vertical float rail above the hand, a weight post, carbon tubes rising from a band. That geometry was inherited from the desk-arm design where height was free. Michael's reaction: "we gotta make this more practical." On a head, height = servo-reaction lever arm, high centre of mass, and bulk.

HARD ENVELOPE (non-negotiable):
- Everything above the scalp fits within 70 mm height over a footprint of at most 190 × 100 mm (X stroke × Y pitch), measured from the scalp surface at the crown.
- Total head-borne mass ≤ 250 g INCLUDING the band/suspension and strap (hand ≈ 60 g floating is a target; the current palm is 3× overweight, so lighten it: thin shells, open frames, fewer screws).
- A bought hard-hat ratchet suspension or a slim printed band may be the structure; a breakaway/elastic chin strap for retention only.

WHAT STAYS (from the engineered hand; read 05-engineering/DESIGN-FREEZE.md §1.7–1.8, DESIGN-FREEZE-ADDENDUM-1.md, mechanical.md §8, tips.md):
- Three nails at 24 mm pitch, each on its own spring-steel leaf (0.1–0.25 N/mm, 5–10 mm travel, hard stop ≤ 2.4 N), TM1 quick-change tips, enclosed leaf roots, knuckle plate, hair rules (no gaps 0.04–3 mm near hair, no rotation within 30 mm of scalp, ≥ 10° draft, no edges).
- Force on the scalp is a MECHANICAL CONSTANT independent of band seating: dead weight, balance beam with rider weight, or a constant-force spring (not a conventional spring × depth). Show it survives ±5 mm seating variation and state the tilt limit.
- Lift-off at both stroke ends (geometric, cam, or linkage), bidirectional contact strokes of 25–40 mm chord at 50–150 mm/s, 1–2.5 Hz (inertia cap), stroke length/timing variable from firmware (irregularity is the rank-1 sensory variable).
- One servo: Feetech STS3032 (20.6 g, 20 × 34 × 23-class body, 0.44 N·m; see 05-engineering/servo-alternatives.md) or XL330 if available. Servo may be mounted flat on the band and drive the stroke through a link, belt, crank or cable.
- Hold-to-run + NC e-stop in the servo rail; tangential breakaway ≤ 2 N; snag reflex = stop.
- Power-loss state: argue limp-at-constant-force vs lifted; propose the lightest acceptable answer.

Read also: 03-tournament/judge-2-engineering.md §0 (F1–F5), 04-redteam/redteam-1-sensation.md (why sweeps ≠ rakes; attack angle), 04-redteam/redteam-2-mechanical.md §2 (flinch), 08-crown/concept-A.md §3–4 (stability and pad numbers you must beat), 02-mechanisms/team-F.md and team-A.md (flat single-motor mechanisms with geometric lift) for reuse.

DELIVER, written to 09-compact/compact-<LETTER>.md (2500–4500 words):
1. Side (XZ) and front (YZ) dimensioned SVGs, plus a plan view; overall height above scalp, footprint, mass budget by part, centre of mass height.
2. Stroke mechanism with numbers: path of the nail tip (chord, lift at ends, attack-angle variation), servo torque incl. inertia at 2.5 Hz, how amplitude/speed/timing are varied, backlash/compliance in the drive.
3. Force mechanism: how the constant force is produced and adjusted 0.6–1.5 N total; sensitivity to seating ±5 mm and to tilt; friction/stiction sources.
4. Stability on the head: reaction torque vs holding moment from the band (hard-hat suspension: 4 pads + ratchet) and strap; margin ≥ 2 upright.
5. Hair safety: gap inventory within 30 mm of scalp; guard geometry.
6. Safety: force cap, breakaway, e-stop, flinch, power loss, doffing ≤ 3 s.
7. Noise path and mitigation.
8. Printed and bought parts with sizes and cost delta vs the hand alone; build hours; what is reusable from 05-engineering/cad/.
9. Top five risks with bench tests.
10. Honest verdict vs the ring crown (concept A) and vs each other's likely approach; what you'd give up.
Reply with ≤200 words: name, height, mass, force mechanism, stroke mechanism, cost, biggest risk.

## Director amendment: YAW AXIS IS IN SCOPE FOR SP1 (Michael's decision)
Add a second servo (same Feetech STS3032 class, or a lighter micro bus servo if torque allows: it only turns slowly, < 0.05 N·m) that rotates the stroke mechanism about a vertical axis OFFSET 20–25 mm from the palm centre, so the patch centre orbits a ~50 mm circle and stroke direction changes with it. Realise it as a low turntable (printed ring on a thin-section or lazy-susan bearing, or a printed sleeve bearing) under the stroke mechanism; budget ≤ 10 mm height and ≤ 30 g; keep all rotation ≥ 30 mm above the scalp and sealed (hair rule). The yaw moves only between strokes or slowly during episodes (≤ 30°/s), driven by the pattern engine. State the stability impact (the yaw servo adds reaction torque about the vertical axis; recompute the band's holding moment) and the cable routing across the turntable (service loop, ±90° range limit). The envelope (≤ 70 mm tall, ≤ 250 g including band) still applies with yaw included.
