# LEADING ARCHITECTURE v0 — "SP1 FLOAT-ARM" (Director's synthesis for red-team attack)

Status: DRAFT for adversarial review. Not yet the decision.

## Tournament outcome
Combined judge totals (/1170): D CRADLE 809 · E LH-1 799 · G ARC-RAKE 743 · F WR-1 726 · B 698 · C 684 · A 644.
All three judges independently ruled: (a) frame-mounted for SP1 (headband seating slop ±3 mm × leaf rate = ±0.6–1.2 N/nail, larger than the 0.3–0.9 N scratch window; nothing on the head; head withdrawal = release); (b) 2-DOF with the stroke axis on a geared smart servo and the normal axis in FORCE mode; single-motor closed paths are kinematically rigid at bottom-dead-centre and become the periodic control instrument; direct-drive FOC is an SP2 upgrade because of the bring-up skill gate; (c) passive mechanical ceiling (weight or spring+stop) with the actuator only modulating below it — "the lift tendon can only reduce force."

## The architecture (subsystems and their origin)
1. MOUNT (E + D): desk-clamped gas-spring monitor arm (VESA plate) positioned over/behind a seated user whose forehead rests on a massage-chair face cradle. Forehead pad carries a normally-open dead-man switch in the actuator power rail: no forehead contact → no motor power. Head withdrawal is the primary release. Nothing is worn on the head.
2. STROKE AXIS (G): one Dynamixel XL330-M288 "elbow" in current-based position mode, horn above a smooth drafted guard plate, swinging an ~80 mm arm through ±18° (≤ 52 mm chord). The hand hangs directly below the elbow pivot so the arc rise (~±6 mm) is symmetric and small.
3. NORMAL-FORCE FLOAT (D): inclined-parallelogram constant-force float (≈20 mm travel) between the arm and the hand; dead weight 0–140 g sets the hand-level force (0.6–2.0 N total cap, i.e. 0.2–0.65 N per nail) as a MECHANICAL CONSTANT independent of servo torque; the float passively follows scalp curvature and ±15 mm head motion with no inverse kinematics; a 1 kg bar load cell (HX711) is in series for logging.
4. LIFT AXIS (D + G): second XL330 pulling a Dyneema tendon that can ONLY raise the float. Lift-before-reversal while still moving forward; lift between episodes; snag reflex = lift and hold. Power loss → tendon slack → hand rests at dead-weight force (bounded) — Safety Gate to decide whether a spring/electromagnet-latched lifted fail-safe is required instead.
5. HAND (A/C/G, with Judge 1's correction): three SP1-TM1 tip holders at 45° attack, 20 mm pitch, each on a 0.3 × 12.7 mm spring-steel feeler-stock leaf (0.3–0.4 N/mm, 8–10 mm travel, hard stop → ≤2.4 N/nail absolute), preloads deliberately unequal (≈0.7/1.0/1.3 ×) for asynchrony; leaves oriented so drag LIFTS the nail (trailing-leaf "dig" geometry rejected); carrier pre-curved R≈90 mm; tips = press-on-nail / PETG blade tip B (0.6 mm) first, tip A (0.3–0.4 mm) after forearm screening; 1 mm drafted paddles, ≥25 mm protrusion past the guard, TM1 seams sleeved.
6. TANGENTIAL YIELD (D + G): wrist magnetic detent ≈0.8 N with microswitch → firmware lift-and-hold; 3 N untethered magnetic hand breakaway.
7. ELECTRONICS (component-landscape Stack A): OpenRB-150, 2× XL330, 5 V 4 A UL adapter, 22 mm NC mushroom e-stop + hold-to-run foot pedal + forehead dead-man all in series in the actuator rail, INA219 rail monitor, HX711 load cell, intensity pot, mode switch, OLED.
8. PATTERN ENGINE (B/E/G + F): PATTERN SPEC v1 — stroke length 15–50 mm, velocity 50–150 mm/s, 1–3 Hz, jitter ±25–30% on length/force/timing, pauses, lift-offs, episode changes every 5–20 s; a PERIODIC mode as control; load-cell logging ~80 Hz.
9. CONTROL INSTRUMENT (F): WR-1 Walking Rake built in wand mode (~$85) in parallel: validates tips/compliance on day 0–3 and provides the fully periodic comparison.
10. STAGED BUILD: Day 0–3 hand wand (TM1 holder + leaf + 6 tips) → WR-1 wand → float + hand on the arm with the elbow servo only → add lift servo → add pattern engine.

Cost ≈ $300–330 + $85 (WR-1) + ~$60 test gear. Build ≈ 30 h + 12 h (WR-1).
Coverage: one ~50 × 40 mm patch per aim (occiput or crown); manual re-aim of the arm between episodes.

## Known open items
- Tip edge radius: safety red line 11 (≥0.4 mm) vs tip-interface baseline 0.3 mm → SP1 default 0.5 mm (tip B family), 0.3 mm only as an experimental variant after forearm screening and tape test.
- Fail-safe lift: limp-at-dead-weight vs lifted. Safety Gate decides.
- Parallelogram float friction/stiction (highest-risk printed part) — print and measure first.
- Whether a single 50 × 40 mm patch with manual re-aim gives enough spatial variation to avoid habituation in a 5-minute test.
- Whether forehead-on-cradle posture is tolerable for 20 min with scratching at the occiput/crown.
