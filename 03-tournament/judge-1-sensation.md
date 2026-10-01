# Tournament Judge 1 — Sensation & Neuroscience Lens

**Project SCRATCH · 03-tournament · 2026-10-01**
**Mandate:** be the harshest possible judge of whether each candidate will feel like *another person's fingernails* rather than a machine, a massager, a brush or a sweep. Read: BRIEF, all six foundation files (including prior-art §7), all seven candidates in full.

**The questions I put to every candidate, in order of how much I weight them:**
1. Does the stimulus keep *changing something on a 2–10 s timescale* (scratch-model §2.2, §4.3) — above all its *location*, since a human changes region every 5–20 s (§4.2) and predictable periodic touch is centrally gated within 10–30 s?
2. Is the hair-follicle drive engaged at human rates — hairs deflected within 2–5 mm of the root, per second? (Component A is ranked first of five; CT afferents fire to single-hair deflection, Moore 2025.)
3. What is the force profile *within* a stroke, and does it vary stroke to stroke?
4. Attack angle: measured against the **local scalp tangent**, not a flat plane.
5. Contact asynchrony across nails (20–80 ms, ≥20 % force spread; §4.2).
6. Velocity band and profile; contact duty cycle (a human P1 rake has the nails on skin most of the time).
7. What happens in the 300 ms after a snag? A plucked hair drives CT after-discharge for seconds (prior-art §3.2) — a single snag poisons the next several seconds of sensation, so snag *response* is a sensation criterion, not only a safety one.
8. What else does the skull hear and feel? Gear-mesh vibration conducted through a headband is a Pacinian stimulus (§2.1 "will dominate if the device vibrates") and a "machine" attribution cue.

Two neuroscience corrections I apply throughout: pleasant touch is **not CT-only** (Aβ block abolishes it; a CT-suppressing film barely dents it), so the Aβ edge/pressure percept is load-bearing and "too gentle to scratch" is a real failure; and **hair deflection alone is pleasant**, so a rake that moves many hairs near the root is doing real work even between skin contacts.

---

## 1. Cross-candidate sensation findings (computed, not asserted)

| Metric | A FEED-DOG | B Pendulum | C LEAFHAND | D CRADLE | E LH-1 | F WR-1 | G ARC-RAKE | Human P1 |
|---|---|---|---|---|---|---|---|---|
| Contact duty cycle | 25 % (const) / 46 % (modulated) | ~54 % | ~41 % | 60–70 % | ~60 % | **23 %** | ~60 % | ~60 % |
| Passes per second | 1.2–1.7 | 1.4–2.2 | 1.0–1.5 | ~2 (P1) | 1–2 uni | 0.5–1.6 | 1.5–3.5 | 2–4 |
| Follicle drive (hairs/s, 10/mm × chord × passes × nails) | 970–1,380 | **2,160** | 1,240 | 1,800 | 1,800 | **810–1,300** | 1,800 | 2,000–4,000 |
| Attack-angle drift vs local tangent at stroke ends | ±1° + ≤9° load-dependent | **±3°** (team says ±18°) | ±3° | 0° | **±2°** (team says ±14°) | 0° | ±1° (+4° coupling) | varies with DIP flexion |
| Force profile within stroke | fixed bell 0.15→0.95→0.15 N | flat ±0.2 N (feed-forward lift) | fixed bell 0→1.2→0 N | constant (dead weight) + tendon unload | **any commanded shape** | fixed bell 0.3→0.75→0.3 N | ramped, depth-commanded | bell, ±30–50 % per stroke |
| Longest stroke | 30 mm | 46 mm | 33 / 55 mm | **140 mm** | ~50 mm usable | 33 mm | 52 mm | 10–150 mm |
| Nail asynchrony | passive 20–50 ms | **driven 0–60 ms** | passive 20–40 ms | passive 20–80 ms | passive 50–100 ms | passive 10–15 ms | passive 20–60 ms | 20–80 ms |
| Autonomous location change | none | ±8 mm | none | **250 mm band, 3 lanes** | 70 mm nudge | none | ±20 mm | 3–6 regions/min |
| Snag: tangential yield / response | 0.5 N detent swings-and-rises; forward-park | 0.5 N hub; lift ~60 ms | 0.6–0.8 N knuckle rises 6 mm; lift 100 ms | ~1 N hand detent; lift | **0.4 N torque saturation; lift in ~10 ms** | 1.5–2.5 N shear; stall→**stop, no lift** | paddle tilts (bite falls); 3 N; lift | hand feels it <100 ms |
| Motor on the skull | N20 at 70 mm | 5 geared servos | **none** | none (frame) | none (frame) | N20 at 60 mm | 2 geared servos | — |
| Force reference | band depth screw | band + lift servo | band + lift stop | **gravity + load cell** | **impedance (commanded)** | band dip screw | band + IK depth | pulp + joints |

Findings:

**F1. Location monotony is the dominant failure mode and five of seven have it.** A, B (±8 mm), C, F and G (±20 mm) sit on one 40 × 30 mm patch until a hand moves them. A person dwells 5–20 s per region, and "a machine running a fixed trajectory becomes a machine within ~10–30 s even if the first strokes feel right." Every single-patch team offers time jitter (speed, pauses) in compensation; I do not believe time jitter alone defeats a spatially fixed stimulus, because SA1 and central gating adapt to *where* as much as *when*. Only D (start-angle shifts along a 250 mm band) and, weakly, E's nudge mode supply spatial unpredictability without a hand on the rig.

**F2. No candidate reaches human follicle-drive rate.** The best (B, with four nails) is ~2,160 hairs/s; the single-motor designs are 800–1,400 hairs/s, a third of a brisk human rake. The cheap fixes are a fourth nail and ≥50 % contact duty — the hybrid should take both.

**F3. Attack angle is not the problem anyone thinks it is — but two teams mis-measured it.** For a pendulum of radius r over a sphere of radius R_s, the nail's angle to the *local* tangent drifts by only θ(1 − r/R_s). B's "63° → 27° finger-flattening" and E's "±14° wander" are flat-plane artefacts; against the real crown the drift is ±3° and ±2°. B's risk #1 is largely a non-risk, and its "finger-like flattening" story is wrong in both directions. G stated the radius-matching principle correctly. The within-stroke angle modulation a human finger actually has (DIP give as force rises) is reproduced *passively* by the leaf end-slope in A, C, D, E and G — a feature — and is absent in B's axial plunger and F's stiff flexure.

**F4. Geometric designs couple force to stroke length.** In A, C and F the depth screw sets both chord and peak force. Turn A down to the model's 0.3 N and the chord shrinks to ~19 mm; turn C to 0.65 N and the chord is 22 mm. A long, light stroke — the "luxurious" P2 sweep, and the CT-band slow stroke the model asks for once a minute — is unavailable. D (dead weight over 140 mm), E (commanded force) and G/B (commanded depth) do not have this coupling.

**F5. Default forces in A and C are too high.** A's mean 0.67 N and C's 1.2 N peak sit above the model's 0.15–0.3 N typical and its "pleasure does not scale above ~0.5 N" ceiling; pleasantness falls with force, faster at speed (bioRxiv 2026). Both are adjustable, but see F4.

**F6. Team C's leaf orientation makes drag *dig*, not lift.** C's leaves trail the knuckle bar (−x), the stalk hangs 46 mm from the free end, and the pull is +x. Drag on the nail (−x) applies a 0.3–0.5 N × 46 mm moment to the leaf tip; on a 0.4 × 12.7 × 50 mm 1095 leaf that is 1.3–2.1 mm of tip deflection in the *downward* sense — +0.4–0.7 N of extra normal force whenever friction rises. A grabby patch or a snagged strand makes C's nail bite harder until the 0.6–0.8 N knuckle detent lets go. C's "drag bends the leaf in-plane by 0.004 mm" considered only axial load. Reversing the leaf (root behind, free end ahead) flips this to self-limiting. A has the same geometry but a ~15 mm holder: +0.17 N, tolerable. G's forward-extending leaf with the paddle flexure is in the self-limiting sense.

**F7. Bidirectional raking with a one-way nail scoops.** E's headline "1–3.5 Hz bidirectional rake" and B's bidirectional mode both drag a 45° blade plate-first on alternate strokes (H-4.3; F's analysis of its own F5 concept is correct). Only C and G name the symmetric-wedge tip that makes bidirectional contact lawful. E's cycle-rate claim should be halved for the unidirectional case.

**F8. Skull-conducted motor noise is a sensation hazard, not a nuisance.** A, F (N20 gearmotor at 60–70 mm), B (five geared servos) and G (two) put gear-mesh vibration into the headband and hence the skull. The one consumer device users describe affectively (the wire spider) is silent. C (motor-free head), D and E (frame) are the only candidates whose scalp hears nothing but nail-on-hair hiss.

**F9. Snag response ranking (sensation lens: how long is the next few seconds poisoned?)** E (0.4 N saturation on a back-drivable axis + 10 ms lift) > A and C (passive detents that swing the nail back *and raise it*) ≈ B > G > D (1 N hand-level) > F (stall → stop with the strand still loaded, no lift). Nobody meets 0.15 N; E's 0.4 N is the closest in spirit to H-4.11's "preload to the scratch load, yield above."

**F10. Head-worn force reference is the wrong reference.** Operating force is 0.1–0.5 N = 0.5–2.5 mm of a 0.2 N/mm leaf. A headband wanders ±1–3 mm under stroke reaction (A risk 4, C R2, G R3). That is ±50–100 % of the operating force, before any head motion. Gravity (D) and impedance (E) are immune to it within their 15–20 mm float.

---

## 2. Scoring table

Scores 1–10; weights per the brief; justification is the phrase after the score.

| # | Criterion (w) | A FEED-DOG | B Pendulum | C LEAFHAND | D CRADLE | E LH-1 | F WR-1 | G ARC-RAKE |
|---|---|---|---|---|---|---|---|---|
| 1 | Scratch realism (5) | **5** correct per-stroke physics; one patch, 25 % duty, force=chord, whine on skull — reads as a machine on one spot | **7** best head-worn irregularity, driven asynchrony, 4 nails; servo chorus on skull, shared-lift tracking | **6** silent head, geometric bell and lift; 1–1.5 passes/s, force=chord, drag digs (F6) | **7** constant light force over 15–140 mm sweeps, auto region change, constant angle; one plane, big-inertia geared sweep | **8** commanded force/velocity shape, silent, 10 ms snag lift; cogging grain, bidirectional scoop (F7), one patch | **4** 23 % duty "flick" rhythm, phase-locked, everything fixed — the control condition, not the stimulus | **7** radius-matched angle, programmable length/depth/±20 mm location, passive+active lift; servos on skull, band reference |
| 2 | Contact across curvature / head motion (3) | 5 — 8 mm leaves; band slop ±0.6 N; stopped crank stays down | 6 — 10 mm plungers + feed-forward; 450 g on headgear | 5 — 7 mm leaves; headgear lifts; strap wobble | 7 — constant radius, 20 mm float; head ±15 mm | 8 — impedance follows ±15 mm; arm bounce | 5 — 8 mm flexures on a band | 6 — IK + leaves; band rocks ±1 mm |
| 3 | Hair safety (4) | 7 — 32/36 credible; 25° plough-in firm | 6 — 33/36 generous: seam at 26 mm, four sweep windows, scoop mode | 7 — 31/36 fair; motor-free head; F6 pins strands | 8 — 33/36 fair; nothing moves near hair | 7 — 32/36; bidirectional mode breaks H-4.3 | 6 — 31/36 honest; stop-no-lift snag | 7 — 34/36 slightly generous; call it 33 |
| 4 | Force control & cap (3) | 5 — depth screw couples force and chord; no readout | 6 — preload cap + lift knob; no per-finger | 6 — lift stop + servo; Bowden hysteresis | 9 — dead weight with load-cell readout | 8 — commanded with readout; drift, cogging | 4 — dip knob, coupled | 7 — depth setpoint; band undermines |
| 5 | Complexity / parts (2) | 6 — one motor, 4-bar + hanger | 4 — 5 servos + solenoid | 6 — 2 servos, 2 Bowdens | 4 — cage, yoke, float, load cell | 6 — 2 motors, simple arm | 8 — fewest parts | 6 — 2 servos, 2 links |
| 6 | Apartment buildability (4) | 6 — ~30 h; pins in printed seats | 5 — ~30 h; 400 g prints; 5-servo firmware | 5 — ~28 h; grommet slits, Bowden routing | 5 — ~30 h; largest physical build | 4 — ~32 h; FOC bring-up is a skill gate | 9 — 12 h | 6 — ~34 h; 2R IK |
| 7 | Availability & cost (2) | 7 — $270 | 5 — $400–415 | 6 — $340 | 4 — $470–535 | 5 — $390; fewer vendors | 10 — $85–148 | 7 — $290 |
| 8 | Noise (2) | 4 — gearmotor on the skull | 4 — five geared servos on the skull | 9 — motor-free head | 7 — muffed servos, isolated bar | 9 — gearless | 4 — N20 near the ears | 4 — two servos, band-coupled |
| 9 | Reliability (2) | 6 — TPU hinge creep | 5 — plastic gears, hub creep, 5× count | 5 — strap creep, Bowden wear | 7 — rigid; gravity does not drift | 6 — heating, drift; no gears | 6 — flexure fatigue | 6 — paddle fatigue |
| 10 | Research adjustability (3) | 5 — time only | 8 — most in firmware; 1–4 nails | 6 — force/speed/pattern | 8 — force readout, 15–140 mm, auto location | 9 — everything a knob, logged | 4 — speed, dip | 7 — force/speed/length/location |
| 11 | Ease of iteration (2) | 5 — reprints | 7 — firmware | 5 — stalk reprints | 7 — firmware + palm | 8 — firmware | 5 — eccentric swap | 7 — firmware |
| 12 | Coverage (1) | 3 | 5 | 4 | 8 — 250 mm × 3 lanes | 5 | 3 | 5 |
| 13 | Failure modes / red lines (3) | 5 — red lines 7/8 partial | 7 — solenoid-latch lift | 8 — pull-only tendons; springs lift | 7 — limp on loss; dead-man | 7 — counterbalance lifts; encoder-loss unaddressed | 6 — Bowden dead-man; stall→stop | 6 — unmeasured back-drive |
| 14 | P(works first time) (3) | 6 — modulation through backlash | 5 — shared-lift tracking, mass | 5 — hysteresis, straps, chatter | 6 — alignment, cos θ, smoothness | 4 — FOC, drift, bounce | 8 — it will run | 6 — IK, back-drive |
| | **Weighted total (max 390)** | **214** | **230** | **234** | **264** | **265** | **230** | **248** |
| | **Rank** | 7 | 5 (tie-break: criterion 1) | 4 | 2 | 1 | 6 | 3 |

E and D are a statistical tie at the top, and that is the finding: they fail in opposite places and the hybrid in §7 is their union.

---

## 3. Rulings on the three decision axes

### (a) Head-worn vs frame/arm-mounted for SP1 — **frame-mounted.**

Sensation reasons, in order: (1) the force reference. Every head-worn candidate sets normal force by depth against a band that floats on hair and slips under stroke reaction; ±1–3 mm of band wander is ±50–100 % of the operating force (F10). Gravity and impedance are referenced to physics, not to a hat. (2) Silence. Head-worn motors (A, B, F, G) put gear mesh into the skull; the only head-worn design that avoids this is C, at the cost of Bowden hysteresis in the one axis that sets force. (3) Spatial unpredictability. A frame carries a travel axis for free (D's 250 mm band); a band cannot, so head-worn designs are one-patch machines by construction (F1). (4) Mass: four nails, a load cell, a dead weight and a fan are free on a frame. The counter-arguments — head motion and context — are weaker than they look: a 20 mm dead-weight float or a ±15 mm impedance axis tolerates more head motion in *force* terms than a depth-set leaf on a band, and the "someone's hand" context (component E) is ranked last of five. The real cost is posture: nobody — head-worn or frame — lets Michael recline, and D's forehead bar is the least relaxing of all. SP1 accepts that; a recliner-headrest mount is the SP2 fix.

### (b) Single-motor geometric path vs 2-DOF programmable arm vs force-controlled direct drive — **2-DOF, with the normal axis in force mode.**

The single-motor path (A, F) is ruled out *as SP1* on sensation: it fixes stroke, direction and location, couples force to chord (F4), spends 54–77 % of each cycle in the air (duty 23–46 %), and phase-locks the nails. It is exactly the "fully periodic" control condition scratch-model §7 demands, and F's wand is the cheapest instrument in the programme — build it, but do not call it the prototype. Between geared 2-DOF (B, D, G) and direct drive (E): the scalp does not feel the actuator, it feels the leaf (0.3 N/mm) in series with whatever is behind it. On the *stroke* axis a geared servo off the head is acceptable if reversals happen in the air (backlash clunks where nothing touches). On the *normal* axis the difference is decisive: a position-mode servo must track a 6–8 mm gap profile at 2 Hz through a floppy reference to hold ±0.1 N (B's and G's hardest risk); a force-mode axis — dead weight (D) or torque-mode direct drive (E) — holds it by physics. Ruling: stroke axis geared and off-head; normal axis force-mode.

### (c) Passive spring cap vs active impedance — **both, at different levels.**

Per-nail passive leaves are non-negotiable: they are what make three or four nails land asynchronously with a force spread (§4.2), what follows curvature, and what gives the DIP-like angle-with-load modulation (F3). Pure impedance on a rigid rake loses all three and leaves the cap to firmware. But a passive cap alone cannot shape force within a stroke, ramp a landing, or lift in 10 ms on a snag, and it inherits the band reference problem. So: leaf per nail (cap = k·x_max), dead weight or torque source at hand level (cap = m·g or τ_stall/L), and impedance/tendon modulation on top for shape and reflex.

---

## 4. The strongest idea in each candidate (carry into the winner regardless of rank)

- **A — the snag detent that swings *and rises*.** A TPU hinge + magnet detent at the leaf root that, past ~0.5 N tangential, lets the nail swing back, flatten and lift — a passive snag reflex with the right kinematics (never reverse, unload upward). Also A's W1 "the head is the actuator" afternoon: the cheapest test of whether three leaf-sprung nails feel like a hand.
- **B — driven per-finger phase.** Four sweep servos with 0–60 ms start offsets and per-finger length/speed resampling is the only candidate that can answer open question 4 (locked vs independent asynchrony). Keep as a hand-module variant. Also the solenoid-latch spring lift (fail-safe with no reliance on back-drive).
- **C — "tendons can only pull, so runaway = lifted", and the symmetric-wedge tip W.** A pull-only drive with spring return makes the de-energised state lifted by geometry; the symmetric wedge is the only lawful way to rake in both directions.
- **D — dead weight through a load cell on a float, and a travel axis through the head centre.** Gravity as the cap, the load cell as the instrument, constant radius and attack angle over 250 mm, and automatic region change — plus the forehead-bar dead-man. W1 Resting Hand (warm, heavy, tendon-curled) is the best "context E" idea in the project.
- **E — a torque-mode normal axis with a 10 ms snag reflex, and measuring while scratching.** Force-rendered landings, dips at reversal, per-stroke force jitter and contact-fraction logging from one silent motor; deliberate 0.7/1/1.3 leaf preloads to guarantee asynchrony.
- **F — build it anyway.** The $85 wand is the programme's fully periodic control condition and tip-screening instrument; its finger geometry (hinge 2.2× further back than the edge is below it, so drag makes the finger firmer but never self-locking) is a rule every leaf design should check.
- **G — radius-matched arc.** Make the nail's arc radius ≈ the local scalp radius about a pivot above the scalp: attack angle stays constant to ±1° while the centre offset gives passive lift at the stroke ends. Plus the tangential paddle flexure (bite falls under snag, like DIP give).

---

## 5. Self-scores I believe are inflated

- **B.** Hair item 3 = 2 rests on the pocket seam being 26 mm up, "outside" a 25 mm band; four 60 × 18 mm windows swept by rocking fingers are hair-entry paths the score does not weigh; the bidirectional mode scoops. Massager item 5 "gear ripple filtered by the spring" is true normally, false tangentially (the hub is rigid until breakaway). Credible hair score ~31. Conversely B's risk #1 (attack-angle swing) is overstated 6× (F3).
- **C.** Massager 12/12 PASS is too clean: item 8 (no direction or location jitter, 1–1.5 passes/s) is UNSURE at best; the force path omits the stalk drag moment (F6) that adds +0.4–0.7 N under friction and pins strands harder; the attack-angle sweep of the rocker is not discussed (it is small, ±3°, but it was not derived).
- **E.** "Bidirectional 1–3.5 Hz" ignores plate-leading scoop (F7); "direction drift ±20° via M1 bias" is not available from a planar arm (direction is manual); massager item 8 "full PATTERN SPEC" should carry that caveat. Hair 32/36 is otherwise fair.
- **G.** 34/36: item 3 = 2 with the TM1 seam at exactly 30 mm, and item 13 = 2 for a per-seating flag rather than a grain map; 32–33 is honest. Realism 0.80 in its own selection table is optimistic for a one-patch head-worn rig (F1).
- **A, D, F** are not inflated; A and F are candid about being one-patch periodic machines and D about its single plane and cos θ. D's "nothing can vibrate" slightly undersells a 1.5 N·m geared servo swinging 0.017 kg·m² — mitigated because reversals are in the air.

---

## 6. Top two

**1. E — LH-1 Listening Hand (265).** It is the only candidate whose normal axis is a force source rather than a position source, and that is the single biggest determinant of whether the scalp feels a pulp-backed nail or a machine holding a depth. Commanded force gives the bell, the dip at reversal, the ±30 % stroke-to-stroke force jitter, the 0.3 s soft landing and the once-a-minute CT-band slow stroke, all as firmware; gearless drive means the skull hears nail-on-hair hiss and nothing else; the 10 ms lift on a snag is the best answer to the after-discharge problem; and it logs force, lag and contact fraction, so the experiment matrix produces data. Its passive leaves with staggered preloads keep the asynchrony that pure impedance would lose. **The biggest reason it could be wrong:** execution. Voltage-mode torque through ±0.02–0.03 N of cogging on a 350 g module hanging from a consumer monitor arm at 2 Hz may feel grainy and bouncy, and FOC bring-up is a real skill gate for a first-timer — P(works first time) 4/10 is the lowest in the field. If the first bench run shows ripple >10 % of setpoint or arm bounce, E degrades to D's physics, which is why the hybrid carries D's float underneath it.

**2. D — CRADLE (264).** Gravity is the cleanest force cap and the cleanest force *source* in the tournament: 0.07–0.65 N per nail, constant along 15–140 mm sweeps, read by a load cell, with constant radius and attack angle because the axis passes through the head centre. It is the only candidate that changes region by itself every few strokes (F1) and the only one that can do the long P2 sweep the model calls "luxurious" at a light force (F4). **The biggest reason it could be wrong:** rhythm and attribution. One sagittal plane, one direction with a lifted return, a 1 kg-counterweighted yoke on a geared XL430, and a forehead on a bar may read as "a slow machine sweeping a line down my head" rather than fingers raking — especially since brisk 2–3 Hz P1 raking, the canonical scratch, is at the edge of its tendon-lift latency. Its own risk #2 (sweeping ≠ scratching) is the right fear.

Third is **G** (248): the best head-worn design, with the correct attack-angle geometry and real length/location jitter, held back by two servos on the skull and a band as the force reference.

---

## 7. Proposed hybrid — "CRADLE-LH"

A combination beats all seven because E and D fail in complementary places. Subsystem by subsystem:

1. **Frame and travel axis — from D.** Desk-clamped 2020 cage; U-yoke on 608 pivots through the head centre; XL430 (or STS3215-12V) at one pivot, muffed, rubber-isolated from the forehead bar; hard stops −45°/+115°; three manual lanes. This supplies constant radius, constant 45°, 15–140 mm strokes, and *automatic region change every 5–20 s* along the band, with reversals in the air so gear backlash never reaches the scalp.
2. **Hand carrier — from D, actuated by E.** D's inclined parallelogram float with the 1 kg bar load cell and dead-weight post (0–140 g → cap 2.0 N by physics, limp-on-scalp or electromagnet-lifted on power loss). Replace D's XL430 tendon with **E's GM3506 + SimpleFOC Mini in torque mode acting directly on the float through a short lever**: it subtracts from the dead weight for landing ramps, force jitter, CT-band strokes, lift at every reversal and the 10 ms snag reflex, and it is silent. Force is then dead weight − motor torque: bounded above by gravity, shaped by current, logged by the cell. **Fallback if FOC bring-up fails:** D's tendon lift on the identical float — nothing is reprinted.
3. **Nails — four, not three, at 20 mm.** Independent 0.3 N/mm spring-steel leaves, 8 mm stop, preloads staggered 0.7/1/1.3 (E), **leaves extending forward so drag lifts the nail** (the F6 check), G's 1 mm tangential paddle flexure between leaf and TM1 holder, and A's magnet detent at the leaf root that swings-and-rises past ~0.5 N. Four nails raise follicle drive to ~2,400 hairs/s at 2 passes/s (F2).
4. **Tips — TM1 family A/B default; C's symmetric wedge W** for the bidirectional-rake experiment; first scalp sessions on tip B (0.5–0.6 mm) per the safety/tip-interface conflict.
5. **Pattern engine — B's per-cycle resampling** (length, speed, force, start, pause, episode weights), D's region scheduler, E's seeded PRNG, logging and PERIODIC control switch, with minimum-jerk velocity in contact.
6. **Instruments built first — F's WR-1 wand ($85, a weekend)** as the fully periodic control condition and the tip/force screening tool, and D's Mode 0 (dead-weight hand, motors off) as the first human contact. Both are needed to interpret the hybrid's results.
7. **Not included:** head-worn anything for SP1; B's driven per-finger phase (an SP2 hand module on the same crossbar, as is D's W1 Resting Hand); E's monitor arm (too compliant at 2 Hz with a 400 g module — the 2020 cage replaces it).

Cost ≈ D's $470 (STS3215 variant) − one servo + GM3506/Mini + fourth nail ≈ **$500–520**, plus $85 for the wand; ≈ 34 h; zero head-borne mass. Expected sensation: a silent, light, long-stroked, four-nail rake that lands softly, dips at reversal, varies force and speed every stroke, moves to a new spot every few seconds, and lets go in 10 ms when it catches a hair. The one §1 failure it does not fix is posture — SP2's problem.

---

## 8. Reply (≤200 words)

**Ranking:** 1 E LH-1 (265) · 2 D CRADLE (264) · 3 G ARC-RAKE (248) · 4 C LEAFHAND (234) · 5 B Pendulum Hand (230) · 6 F WR-1 (230) · 7 A FEED-DOG (214).

**Axis (a):** frame-mounted. Head-worn designs reference force to a band that wanders ±1–3 mm (±50–100 % of operating force), put gear mesh into the skull, and are one-patch machines — spatial monotony is the dominant sensation failure and only a frame can change region unattended.

**Axis (b):** 2-DOF with the normal axis in force mode (dead weight or torque-mode direct drive); the stroke axis may be a geared servo off the head with reversals in the air. Single-motor paths (A, F) are the periodic control condition, not SP1.

**Axis (c):** both — per-nail passive leaves (asynchrony, curvature, DIP-like angle modulation, hard cap) under a hand-level force source with active modulation and a ≤10 ms snag lift.

**Hybrid "CRADLE-LH":** D's cage, yoke through the head centre, float + load cell + dead weight; E's GM3506 torque-mode on the float; four staggered-preload leaves oriented so drag lifts; G's paddle flexure and A's rising detent; C's wedge tip; B's pattern engine; F's wand built first as the control.
