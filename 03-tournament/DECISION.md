# DIRECTOR'S CONVERGENCE DECISION — SP1 "FLOAT-ARM" (final architecture)

## The decision
SP1 is a FRAME-MOUNTED, SINGLE-SERVO (yaw servo as a gated add-on), DEAD-WEIGHT-FORCED, BIDIRECTIONAL THREE-NAIL RAKE with GEOMETRIC LIFT-OFF, hung from a desk-clamped monitor arm over a face cradle. Nothing is worn on the head.

## Why it won
1. All three tournament judges independently ruled frame-mounted: a headband is not a force reference (±3 mm seating × 0.2–0.4 N/mm leaf = ±0.6–1.2 N per nail, larger than the entire 0.3–0.9 N scratch window). A dead weight on a vertical slide makes the hand-level force a true mechanical constant that survives head motion and servo faults. This is the single most important engineering fact the program found.
2. The stroke axis goes on one bought smart servo (Dynamixel XL330) so the rank-1 sensory variable, pattern irregularity (length, speed, timing, pause, direction), lives in ~100 lines of firmware, while the ceiling on force stays a weight and a stop. Single-motor closed-path mechanisms (Teams A, F) are kinematically rigid at bottom-dead-centre and cannot vary anything; they survive only as the PERIODIC mode of this rig.
3. Lift-off before every reversal, which every foundation document demands, is obtained for free from geometry: the hand hangs below the elbow pivot, so the tip arc is concave-up while the scalp is convex; the gap grows as Lθ²/2·(1+L/R). With L = 80 mm, R ≈ 90 mm and a 3–4 mm engagement set by the float's down-stop, the nails are in contact over a ~36 mm chord and lift ~10 mm by ±25°. No lift servo, no firmware, no tendon.
4. Red Team 1 showed one-way lifted strokes read as "a 3-tooth comb sweeping"; geometric lift at BOTH ends makes the return stroke a scratch too (human primitive P1, bidirectional rake), with a symmetric wedge tip as the default and the 45° nail-mimic family available through the same TM1 mount.
5. Red Team 2 and 3 both independently found the inclined parallelogram float amplifies friction into normal force (N = W/(1−0.577µ), 1.4–2.4×) and is the highest-risk printed part. Replaced by a bought vertical MGN9 miniature rail: N = W for any µ, zero printed tolerance, $12.
6. It is the design Michael is most likely to finish: ≈ $250–300, ~17–22 build hours after a 3-hour hand wand, two toolchains at most (printing, Arduino-style firmware), every printed part supplied as OpenSCAD + STL.

## What was rejected and why
- Head-worn (A, B, C, G as drafted): force reference drift; mass at/over 500 g; bone-conducted gear noise; one-patch; no quick release except unbuckling.
- Direct-drive FOC (E): best sensation hardware, but FOC bring-up is a skill gate for a non-expert and the cap is a motor constant to be measured; designated SP2 upgrade for the stroke axis.
- Full C-arm yoke (D): right physics, $500+ and 42 h; its float/dead-weight/load-cell ideas are adopted, the yoke is SP2 if region wander proves decisive.
- Lift servo + tendon (v0): deleted; geometry does it. A second servo, if earned by Stage 2 results, is spent on YAW (direction + patch wander), the next-ranked sensory variable.
- Separate WR-1 control wand: deleted as a build; the PERIODIC firmware mode is the control condition. The motorless Day-0 hand wand stays.
- Forehead dead-man switch, OLED, INA219, load cell: cut or deferred (hold-to-run handheld button + NC e-stop is the dead-man; a kitchen scale calibrates the dead weight).

## Hypothesis SP1 tests
"A stiff narrow edge (R 0.4–0.5 mm) at 0.3–0.5 N per contact, sliding 50–150 mm/s over a 30–40 mm chord with lift-off at every reversal, three contacts at 20 mm pitch with unequal preloads, and irregular timing, is perceived as a person's fingernails scratching the scalp rather than as a machine — and irregularity (vs. PERIODIC) is a large part of that."
