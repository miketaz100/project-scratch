# Tournament Judge 2 — Mechanical Engineering, Safety and Buildability Lens

**Judge:** 2 of 3 (independent; other judges' files and the simplicity engineer's file were not read). **Date:** 2026-10-01.
**Inputs:** BRIEF.md; all six foundation files; all seven candidate files in full. Every kinematic and force-path number below was recomputed by me in a scratch script (crank-rocker coupler curves, scotch-yoke ellipse, elbow-arc gap, leaf and flexure stiffness/stress, yoke inertia and balance, BLDC stall torque and I²R, Bowden losses, head-borne mass). Where my number differs from a team's I say so; where it agrees I say that too.

---

## 0. Cross-cutting findings that drive the scores

Five engineering facts that apply across candidates and that no self-score fully reckons with.

**F1. The force reference of every head-worn design is the strap.** A ratchet suspension seats to roughly ±3 mm on a head that moves and breathes. Force = k × depth, so with a 0.2–0.4 N/mm leaf that is ±0.6–1.2 N per nail — larger than the whole 0.3–0.9 N scratch window (tip-interface §2.5). A, B, C, F and G treat this as a calibration item; it is a drifting reference. Only D (dead weight on a float) and E (torque-controlled axis) have a setpoint that survives head motion. This is the biggest single reason the frame-mounted designs win on my lens.

**F2. At bottom-dead-centre of a closed-path single-motor mechanism, normal force has no handle on the motor.** A's crank-rocker: dz/dθ ≈ −0.1 mm/rad at the loop bottom (dx/dθ ≈ 19); F's scotch yoke: dz/dθ = 8·sin θ ≈ 0 at θ = 0. The mechanism is kinematically rigid in the normal direction exactly where the nails are on skin, so the driver current limit both teams list as a "second layer" gives zero normal-force protection. The spring + stop is the only cap and the actuator-stop check must be perfect; A's margin is zero by its own arithmetic, F's relies on ≤2 mm of band compliance.

**F3. Head-borne mass is under-estimated by the hard-hat designs.** A moulded HDPE shell is 300–350 g before its ~90 g suspension; a 110 × 90 mm window removes ~25 g. A's CCR-3 is 535–585 g by my count, not 420 g — over red line 10. B's 450 g is at the line. C (280 g, nothing electrical on the head) and F (330 g) have margin; G's 300 g is plausible but hangs 130 mm behind the band, ~0.3 N·m of moment on a headgear built for a symmetric load.

**F4. Nobody meets the 0.15 N tangential yield (hair item 7), and nobody can** while passing 0.3–0.5 N of scratch drag through the same mount. I accept H-4.11's own "preload then yield" caveat and judge item 7 on whether the yield is a measurable mechanical element (A, B, C, D, G), an actuator saturation (E) or geometry alone (F). I do not penalise it beyond the teams' own 1.

**F5. The fail-safe lift is where three designs are weakest.** A: a stopped crank is not a lifted crank (admitted). B: a solenoid-released 0.1 N·m torsion spring must raise a ~195 g palm whose CoG is 40–80 mm from the hinge, i.e. against 0.08–0.15 N·m of gravity — marginal to insufficient as specified. G: a bias spring against an unmeasured XL330 back-drive torque. C, D (limp; head is the release), E (counterbalance) and F (mechanical pedal) are sound.

---

## 1. Scoring table

Scores 1–10; weights from the judge brief (total weight 39; maximum 390).

| # | Criterion (w) | A FEED-DOG | B Pendulum | C LEAFHAND | D CRADLE | E LH-1 | F WR-1 | G ARC-RAKE |
|---|---|---|---|---|---|---|---|---|
| 1 | Scratch realism (5) | 6 — right physics, 27 mm one-way, time-jitter only | 8 — 4 independently timed fingers, 46 mm, palm lift; 63→27° attack swing | 6 — 33 mm pull at 1–1.5 Hz, geometric lift; no direction/length jitter | 7 — 15–140 mm at constant radius, dead weight, lift; one-way | 8 — force-rendered, bidirectional to 3.5 Hz, silent; rigid rake | 5 — 27 mm, 23% duty "sweep-and-tap"; speed jitter only | 7 — 15–52 mm with lift, stable attack angle; rigid rake |
| 2 | Contact across curvature / head motion (3) | 6 — 8 mm leaf; seating drift (F1) | 7 — 10 mm/finger + lift feed-forward; seating drift | 6 — 7 mm leaf; stalk–leaf coupling; strap sway | 8 — constant radius + 20 mm float + leaves | 7 — 38 mm travel, impedance ±15 mm; arm bounce | 6 — 8 mm flexure + dip stage; seating drift | 6 — 10 mm leaves, but shoulder must track 35 mm/rad (§2 G) |
| 3 | Hair safety, verified (4) | 7 — my 31/36 | 7 — my 32/36; 9 mm finger offsets in contact | 6 — my 30/36; silicone band in the pile | 8 — my 32/36; leash is a tether | 8 — my 32/36; no guard | 6 — my 30/36; collar step in canopy; stall→stop | 7 — my 32/36; passive lift one-way |
| 4 | Force controllability & cap (3) | 6 — depth screw couples force and chord; 1.8 N; zero stop margin | 6 — 2.3 N stop, 1 mm margin; no per-finger readout | 5 — Bowden ±15–38%; backstop unmeasured | 9 — dead weight + load cell | 8 — force is the command; cap 2.1–5.4 N until measured | 6 — dip couples force and chord; 1.5 N stop robust | 7 — depth × k; 2.0–2.4 N verified; current readout |
| 5 | Mechanical complexity (2) | 6 | 4 | 5 | 4 | 5 | 8 | 6 |
| 6 | Apartment buildability (4) | 5 — ~32–38 h | 4 — ~36–42 h | 5 — ~30–36 h | 5 — ~38–45 h, forgiving | 3 — ~40–50 h; FOC skill gate | 8 — ~16–22 h | 5 — ~34–40 h; IK firmware |
| 7 | Availability & cost (2) | 7 — $270 | 5 — $400 | 6 — $340 | 4 — $470–535 | 5 — $390; GM3506 stock intermittent | 9 — $85–148 | 7 — $290 |
| 8 | Noise (2) | 4 — N20 on head | 5 — 5 servos on head | 8 — motor-free head | 6 — XL430 via forehead bar | 9 — gearless | 4 — N20 + yoke clunk | 6 — 2 XL330 on head |
| 9 | Reliability (2) | 6 — TPU hinge creep | 5 — plastic gears, hub creep | 5 — TPU strap creep | 8 | 6 — heating, thermal drift | 5 — PETG flexure creep | 6 — PETG paddle bend |
| 10 | Research-rig adjustability (3) | 5 | 8 | 6 | 8 | 9 — compliance is a knob | 4 | 8 |
| 11 | Ease of iteration (2) | 5 | 7 | 5 | 7 | 9 | 5 | 7 |
| 12 | Coverage / region change (1) | 3 | 6 | 4 | 8 | 5 | 3 | 5 |
| 13 | Failure modes, fail-safe, red lines (3) | 5 — RL 7/8 partial, RL 10 likely failed | 6 — fail-safe spring marginal | 7 — springs lift; backstop unmeasured | 8 | 7 — cap needs Kt/R; stop mis-placed | 7 — mechanical pedal lift | 6 — bias-spring lift unverified |
| 14 | P(works first time) (3) | 6 | 4 | 5 | 6 | 4 | 8 | 5 |
| | **Weighted total /390** | **221** | **235** | **223** | **270** | **262** | **239** | **248** |
| | **Rank** | 7 | 5 | 6 | **1** | **2** | 4 | 3 |

Build-hour estimates are mine for a competent non-expert with a Pinecil, hex keys and either a budget FDM printer or JLC3DP; they exclude print time and include the firmware each team specifies. Every team under-estimates firmware by roughly 1.5× except F.

---

## 2. Per-candidate engineering verification and the single highest-risk fabricated part

### A — FEED-DOG CCR-3
**Verified:** Grashof crank-rocker (20/100/40 on a 107.7 mm ground). My coupler curve reproduces their loop (47.4 × 22.0 mm), rod tilt ±11.6° (9.3–11.6° in contact), 27 mm chord at 4 mm depth, 25% duty, 25° entry, 47° exit. Leaf k = 0.211 N/mm, 450 MPa at the 8 mm stop (fine for feeler stock at R = 0). Exit speed 0.60 of peak against their 0.42; either satisfies H-5.3.
**Wrong or unproven:** head-borne mass 535–585 g (F3); actuator-stop margin zero by their own arithmetic; the DRV8871 layer is no normal-force protection at BDC (F2); a 2.5:1 speed modulation of a 210:1 gearbox within one revolution is a real velocity-loop and backlash problem (their risk 3). The 50 mm offset L-hanger puts ~105 N·mm of torsion from normal and drag reactions on a printed 8 × 12 mm PETG rod — expect visible comb-bar twist.
**Highest-risk fabricated part:** the TPU 95A comb bar with three 2 × 10 × 3 mm living-hinge necks and D41 detents — a hair-safety-critical calibrated element printed in a creeping elastomer, ±30% before shimming.

### B — Pendulum Hand
**Verified:** ±18° → 46.4 mm chord, 3.67 mm arc rise, 2.98/3.84 mm scalp drop on R90/R70; palm rotation 15° → +15.3/+6.4 mm at the tip; lift-servo stall through the 2:1 lever ≈ 19 N at the tips (their ~17 N), so the down-stop does all the work with a 1 mm margin.
**Wrong or unproven:** the fail-safe spring (F5): ~195 g of palm at 40–80 mm from the hinge is 0.08–0.15 N·m of gravity moment against a 0.1 N·m spring — needs ≥0.2 N·m plus the 20/20 drop test they list. Rear-row beams cranked 36 mm forward are loaded in torsion by drag at 83 mm (PETG, 12→8 mm taper): the rear fingers will wobble. Fingers 0–60 ms out of phase at 150 mm/s are up to 9 mm apart longitudinally in contact — not scissoring (22 mm tracks) but a bridging strand is loaded by relative motion (hair §3.9); their item-5 = 1 is honest.
**Highest-risk fabricated part:** the lift link + solenoid latch pin + torsion spring — the one part red line 8 depends on, loaded at up to the 2.3 N cap when it must release.

### C — LEAFHAND
**Verified:** interference 4.0 / 2.6 / 0.85 / ≈0 mm at x = 0 / 10 / 15 / 17 → 33–34 mm chord; 12.0 mm clearance at ±30°; leaf k = 0.325 N/mm at L = 50 (0.19–0.64 over 60–40 mm), 336 MPa at 7 mm; TPU strap Euler load ≈ 66 N against 7 N; strap pair lateral stiffness ~2 N/mm.
**Wrong or unproven:** (i) leaf–stalk coupling is larger than stated: 0.3–0.5 N of drag 46 mm below the leaf tip is a 14–23 N·mm end moment, raising the tip 1.3–2.1 mm and cutting normal force by 0.4–0.7 N of 1.3 N — stable (drag lifts, never digs) but the setpoint is not what the lift screw says. (ii) Knuckle detent arithmetic is backwards: a D41 at 4 mm offset holds ~16 N·mm → 0.35 N at 46 mm; 0.6–0.8 N needs 28–37 N·mm, i.e. a D61 or two D41s — a shim only reduces. (iii) The backstop beyond the leaf stop is headgear lift-off at "3–6 N est", an unmeasured constant in the normal path. (iv) A silicone band over the pocket mouth 12 mm above the edge is a silicone surface in the pile (H-4.7); use polyolefin or a hard skirt. Bowden hysteresis at μ 0.1–0.15 over 90–180° is ±15–38%, so LIFT-axis force modulation is coarse without a head-end sensor.
**Highest-risk fabricated part:** the TPU 95A ROCK hinge straps (25 × 2 × 40 mm). They *are* pivot P, whose height sets the force ceiling; creep or a creased clamp moves the cap.

### D — CRADLE
**Verified:** dead weight 0.59–2.0 N with a 140 g post; yoke inertia by my masses ≈ 0.021 kg·m² (theirs 0.012–0.017 is light; conclusion holds: 0.47 N·m at 22 rad/s² against 1.5 N·m); hand side 0.088 kg·m vs 0.075 kg·m counterweight — a slow drift as they say; KE at 0.2 m/s ≈ 53 mJ (at the 50 mJ line; carbon arms or 0.18 m/s); forehead pad 3.1 kPa at 15 N; yoke arms 65 mm from the ear canal.
**Wrong or unproven:** cos θ is 0.71 at 45° and 0.50 at 60°, so "within ±15%" holds only after a per-head-tilt trim. The hand's 60 g at 45° contributes 0.42 N of side load to a ~1 N wrist detent — 40% of the snag budget gone before any hair. The 50 mm hand leash is a tether (H-6.4); use a cup. Build: hacksaw-cut 2020, pillow blocks coaxial to ±1 mm, a load cell in series with a printed parallelogram, a dead-man pad — 38–45 h, not 30.
**Highest-risk fabricated part:** the parallelogram float carrier (printed four-bar on four 623ZZ with the load cell in series). Its friction and play decide whether the constant force is constant; play in printed seats turns a 0.6 N setting into 0.4–0.8 N.

### E — LH-1 Listening Hand
**Verified:** 8 mm lift at 45 mm with 0.07 N·m on 4 × 10⁻⁴ kg·m² takes ~45 ms (they say 60–80); cogging ripple 0.02–0.04 N; I²R ≈ 0.9 W at 0.45 N and 2.6 W at 0.75 N — heating is the real limit, as they say.
**Wrong or unproven:** (i) The 2.2 N "physical cap" rests on R = 5.6 Ω being *phase* resistance and Kt = 0.05 N·m/A, both EST; if 5.6 Ω is line-to-line (common in listings) the cap is 4.8 N per hand, and a 1.5 A DC-bus fuse does not bound phase current at stall (bus current ≈ phase current × duty). Red line 2 is "pass after measurement". (ii) A lower stop at "nominal scalp −15 mm" with 8 mm leaves lets the arm bottom the leaves at nominal head position; it must sit at closest-credible-head −5 mm, as their positional check then states — the two conflict. (iii) FOC bring-up for a first-timer (pole pairs, encoder direction, PID, gravity compensation, then impedance and lift primitives) is 40–50 h total and the one place a non-expert can lose a week.
**Highest-risk fabricated part:** the M1 rotating cap with the 10 mm rod socket bonded to the gimbal bell inside a 0.6 mm-clearance labyrinth cup; a 0.5 mm socket offset wobbles the rake. Everything else that matters is bought.

### F — WR-1 Walking Rake
**Verified:** 23% duty and 26.5 mm chord at 3 mm dip on R90; 201 mm/s peak at 1.6 Hz; 7.2 mm clearance at the x-reversal on R90 (5.0 mm on a flat side — exactly H-5.2's minimum); 75% of peak speed at entry/exit; 0.30–0.75 N, cap 1.5 N. Entry to the *local* tangent is 28° (path 19.5° + surface 8.4°), not 20°; still ≤30°.
**Wrong or unproven:** (i) A 15 × 12 × 1.2 mm PETG hinge is k_θ ≈ 230 N·mm/rad; 0.15 N/mm needs a ~45–50 mm hinge-to-edge lever, contradicting "12 mm behind the edge" (the "2.2× further back" line is the consistent one). Cyclic stress 10–20 MPa in PETG: creep is certain, fatigue plausible — their risk 4. (ii) The 0.3 N preload exists only if the finger is printed pre-bent against the up-stop lug. (iii) The lift pin's load reverses sign every cycle (nail reaction up in contact, gravity down in the air): 0.2 mm of slot play is a clunk at every touchdown, felt through the band. (iv) The TM1 seam sits 10 mm above the edge, in the pile; a heat-shrink collar is a 0.3 mm step facing the stroke (H-4.4), so item 6 is a 1. Their fallback — bond the blade to the finger — is right for first human tests.
**Highest-risk fabricated part:** the printed Ø46 double eccentric on a 3 mm D-shaft with two M3/623 pins at two axial levels, mated to two printed 10.2 mm yoke slots. Runout here binds the ellipse; the N20 at 12 N of pin force will either stall or force it.

### G — ARC-RAKE
**Verified:** leaf k = 0.40 N/mm (0.3 × 12.7 at 35 mm) and 0.16 N/mm (0.25 at 40); elbow torque ≈ 0.10 of 0.52 N·m; attack-angle wander ≈ (1 − 75/80)·θ ≈ ±1° plus shoulder coupling — "45° ± 5°" is right.
**Wrong:** the sphere-tracking table and the passive-lift claim. The nail sits 35 mm forward of the elbow at radius 83, i.e. 25° off the arc's lowest point, so dz/dθ at nominal is 83·sin 25° = 35 mm/rad, not zero. With the shoulder frozen, sweeping forward +18° lifts the nail 14 mm (17 mm gap with scalp drop) but sweeping backward −18° drives it 7.4 mm into the scalp (gap −3.4 mm; −4 mm at −10°). Their 3.5 / 6.2 / 9 mm figures assume the arc bottom is under the patch. Consequences: the shoulder (dz/dφ ≈ 30 mm/rad) must co-move roughly equal-and-opposite at every stroke, so IK is mandatory; the "passive backup lift" is true forward only — a frozen shoulder during the −θ return dives the nails to the leaf stop; "Concept 1 mode" as described digs at one end. The leaf cap still bounds force, so this is a realism and first-time-success error, not an injury error. The fix is one geometry change: hang the carrier so the nail is directly below the elbow, which makes the arc symmetric and the passive lift two-sided.
**Highest-risk fabricated part:** the heat-bent 1 mm PETG finger paddle — hand-formed 45° bend, hand-filed 0.3–0.5 mm edge, three to match within ±1 mm, fatigue-loaded at the bend.

---

## 3. Red-line audit (my verdicts, not the teams')

I checked all 13 red lines for all seven. Lines 1, 3, 4, 5, 6, 9, 12 and 13 pass everywhere (F's TM1 shear breakaway of 1.5–2.5 N must be tuned to ≤2 N). Line 11 is the known 0.3-vs-0.4 mm tip conflict; every team runs first sessions on tip B and the Director already holds the resolution. The exceptions:
- **Line 2 (mechanical cap):** E is *conditional* — the cap is a stall torque of 2.1–5.4 N until Kt and R are measured, and the lower stop is specified inconsistently. A passes with zero stop margin; C passes with an unmeasured headgear backstop.
- **Lines 7/8 (spring-return lift, de-energised state):** A partial (admitted: a stopped crank rests nails at ≤1.8 N). B passes only if the latch spring is raised to ≥0.2 N·m. G unverified until XL330 back-drive torque is measured. D is "limp" with the head as the release; F is a mechanical pedal lift but an e-stop leaves ≤0.75 N of spring contact.
- **Line 10 (≤500 g):** A likely fails (535–585 g); B is at the line; C, F, G pass; D, E not applicable.

---

## 4. Rulings on the three decision axes

**(a) Head-worn vs frame/arm-mounted for SP1: frame/arm-mounted.** The strap is not a force reference (F1: ±0.6–1.2 N per nail of drift against a 0.3–0.9 N window); the mass budget disappears, so a dead weight, a load cell and metal-gear or gearless actuators become possible; the head is the quick-release; motor noise is not bone-conducted through a band; and three of five head-worn candidates are at or over 500 g by my count. The cost is a forehead rest and 20 minutes of stillness, which massage cradles prove tolerable, and ±15 mm of head motion, which a float or impedance axis absorbs. Build the module so it can hang from a head mount in SP2 (B's VESA adapter, F's three-mount idea).

**(b) Single-motor path vs 2-DOF servo arm vs force-controlled direct drive: 2-DOF servo arm with a passive cap for SP1; the single-motor rake as the day-one control instrument; direct drive as the SP2 lift-axis upgrade.** The single-motor family (A, F) gets per-stroke physics right by geometry and is cheapest and likeliest to run first time, but is kinematically rigid at BDC (F2), cannot vary length, direction or location, and its "second layer" is fictional. Direct drive (E) has the best sensation hardware and adjustability but is the one candidate where a non-expert can stall on bring-up, and its cap is a motor constant to be measured. The 2-DOF arm (G; D's yoke + tendon is the same class) puts the #1 sensation variable in firmware while the cap stays a spring or weight, on bought smart servos with Arduino-grade firmware. F's WR-1 at $85 should be built regardless as the periodic control and tip-validation wand.

**(c) Passive spring cap vs active impedance: both, strictly ordered.** The ceiling must be a weight or spring-plus-stop (red line 2); the actuator may only modulate *below* it. D's rule — the lift tendon can only reduce force — is the cleanest statement and should be adopted verbatim. E's impedance control is the right modulator but not the right ceiling for first human tests; put it on top of a dead weight (E's own Config B).

---

## 5. The strongest idea in each candidate, worth carrying regardless of rank

- **A:** phase-aware speed modulation from a $3 AS5600 on the crank — the cheapest way to make a periodic machine aperiodic in time; and the moving shroud that travels with the comb bar.
- **B:** the lift feed-forward z(φ) holding spring compression within ±1.5 mm over an arc stroke; and the "Ouija puck" wildcard — the only idea in the tournament with no joint on the hair side.
- **C:** geometric lift-off and passive asynchrony produced by shape (stalk stagger, curved bar), so the two hardest hair/sensation requirements cannot be lost to a firmware bug; and the motor-free head.
- **D:** the dead-weight float with a load cell in series and a lift tendon that can only unload — the force path every design should copy; the forehead-pad dead-man; the W1 "Resting Hand" glove as an SP2 hand.
- **E:** compliance as a firmware variable (K_virtual 0.1–1 N/mm); "measures while it scratches" (contact fraction, force per cycle, snags logged); and the Bowden-hysteresis analysis that kills tendon force control for everyone.
- **F:** the three-mount module (wand day 1, headband day 3, boom optional); the fixed-stroke rig as the program's control condition; the pedal-released dip stage as a purely mechanical dead-man lift.
- **G:** the non-concentric-arc passive lift (once made symmetric) as a hardware backstop under a firmware lift; the 0.7/1/1.3 leaf preload stagger shared with D/E.

---

## 6. Self-scores I believe are inflated

- **A, red line 10 "met at ≈420 g"**: 535–585 g by my count; and "worst case 8 mm = the stop" is zero margin presented as a pass.
- **B, red line 8 "Pass"**: the 0.1 N·m lift spring is below the palm's gravity moment at any plausible CoG. Firmware at 8 h for five servos with lift feed-forward and a snag reflex is 1.5–2× light.
- **C, massager checklist 12/12 PASS**: item 5 (1–1.5 Hz, one pass per cycle) is at the bottom of the band at half the pass rate; items 8 and 12 are UNSURE by the checklist's own rules; hair item 10 = 2 with silicone in the pile should be 1; the knuckle detent cannot be shimmed upward.
- **D**: hair item 11 = 2 with a leash; "±15% over ±45°" only after per-setting trim; 30 h → ~40.
- **E, red line 2 "pass, 2.2 N"**: rests on two EST motor constants and a fuse that does not bound phase current; 28–36 h → 40–50 h for a first-time FOC user.
- **F, 12 build hours**: 16–22 h; hair item 6 = 2 with a collar step in the canopy; "entry 20°" is 28° to the local tangent (legal).
- **G, hair 34/36 and "passive backup lift"**: the arc is asymmetric; passive lift works one way, the other dives; the sphere-tracking table is wrong by 2–3× and in sign on one side.

---

## 7. Top two

**1. D — CRADLE (270).** The only candidate whose normal force is a true mechanical constant independent of position (dead weight on a float), is *measured* in the path (load cell), has no actuator in the normal-force path (sweep is tangential through a detent; lift can only unload), and whose quick-release is "move your head". Metal-gear servos, extrusion and bearings, every critical tolerance slotted, a 250 mm band covered automatically. It carries the heaviest build (38–45 h, ~$500), the most awkward posture, and a P1 ceiling near 2 Hz. **Biggest reason it could still be wrong:** a one-direction rake with a lifted return on a slow, heavy yoke may read as a *sweep*, not a *scratch* (their own risk 2); if bidirectional P1 at 2–3 Hz is what the scalp wants, 0.02 kg·m² of yoke and tendon-lift latency make that the hard case, and the twin-palm module is a patch, not a fix.

**2. E — LH-1 Listening Hand (262).** The simplest force path in the tournament (motor → arm → rod → leaf → nail, nothing geared, all back-drivable), the quietest, and the only design where force, compliance, lift and pattern are all firmware with readout; the empty exclusion zone and 10 ms reflex make its hair story as good as D's. It loses to D only because its ceiling is a motor constant that could be 2× the claim until measured, its lower stop is specified inconsistently, and SimpleFOC bring-up is where a non-expert can lose a week. **Biggest reason it could still be wrong:** M2 heating. Holding 0.75 N per hand through a 45 mm lever is 2.6 W in a 60 g can; if the force–pleasure curve peaks above ~0.6 N per hand (the tip window runs to 0.9 N per *nail*), it cannot hold the vigorous end for 20 minutes without the dead-weight Config B — at which point it has quietly become D's force path with a fancier modulator.

G is a close third and would be second with its arc geometry corrected; as written it needs the §2 fix before anyone prints it.

---

## 8. Proposed hybrid — "LEAF-ARM on a float" (I believe it beats all seven on my lens)

D's force path, G's arm, E's frame, the A/C/G hand, the B/E/G pattern engine, F as the control rig:

| Subsystem | From | Spec |
|---|---|---|
| Mount | E + D | Desk-clamped gas-spring monitor arm ($36) over a massage face cradle ($20) with D's forehead-pad dead-man in the motor rail. Nothing on the head; withdrawal is the release. |
| Stroke axis | G | One XL330 "elbow" on an ~80 mm arm sweeping ±18° (≤52 mm), current-based position mode, horn above a smooth guard. **Nail hung directly below the elbow** so the passive arc lift is symmetric. |
| Normal force | D | Inclined-parallelogram constant-force float (20 mm) between stem and hand; dead weight 0–140 g (0.6–2.0 N cap; cos θ ≤ 5% over ±18°); 1 kg bar load cell in series. The float tracks the sphere passively, so no IK: the arc's ±6 mm rise is absorbed at constant force. |
| Lift axis | D + G | Second XL330 through a Dyneema tendon that can only raise the float; lift while still moving forward; D's electromagnet-latch spring-lift if the Safety Gate wants lifted rather than limp. |
| Hand | A/C/G | Three TM1 holders at 45° on 0.3 × 12.7 mm feeler-stock leaves (0.3–0.4 N/mm, 8–10 mm, hard stop), preloads 0.7/1/1.3, carrier pre-curved R85–90, press-on-nail tips B then A. |
| Tangential | D + G | D's wrist magnetic detent (~0.8 N, microswitch reflex: lift and hold) and G's 3 N untethered hand breakaway. |
| Pattern | B/E/G | PATTERN SPEC v1 on the OpenRB-150 with F's PERIODIC switch; load-cell logging at 80 Hz. |
| Control rig | F | WR-1 in wand mode ($85, a weekend), built in parallel as the periodic control and tip-validation instrument. |

Cost ≈ $300–330 (servos $55, OpenRB $29, PSU $18, arm $36, cradle $20, load cell $10, e-stop/pedal/dead-man $30, feeler stock/springs/magnets/nails $25, prints $40, misc $35) plus $85 for WR-1; build ≈ 30 h. It beats the field on my lens because it has D's force physics and instrumentation at G's cost and compactness, E's frame philosophy without E's skill gate, two bought smart servos with no FOC and no IK (the float removes the sphere-tracking that G's arm needs firmware for), every red line met by a weight, spring, stop, magnet or wire, and nothing on the head. Its highest-risk fabricated part is D's — the printed parallelogram float — so print it first and measure its friction on the kitchen scale before anything else.
