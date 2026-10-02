# LEAP 2-B — The pad and its motion: straight strokes from motors that never reverse

**Project SCRATCH · 11-leaps/round-2 · Agent B · 2026-10-02**
**Provocation:** the scratching pad itself: pin count and layout, pad shape and conformity, and the carrier path. Is a circle the best never-reversing motion?
**Read:** LEAP2-BRIEF; leap-B §LEAP 1, §LEAP 2, §3; leap-A Leap 2; scratch-model §1–8; hair-interaction §2–3, §5–6; safety red lines §7; pin-unit §0–3b; concept-A §1–4; leap-E and leap-F (headings, leap-F §0 gravity frame). Firewall kept: no other round-2 file read.
**Tags:** KNOWN = published or in a foundation doc · EST = computed here (scripts in the session scratchpad; every number can be rerun) · UNKNOWN = only a bench or Michael's head can answer.

---

## 0. What the circle actually draws (the finding behind everything below)

In the pressure-gated orbit, every stroke is **a piece of the carrier's path**: a pin down for a phase window scratches exactly the arc the pad traverses in that window. So stroke straightness is set by the path's local radius of curvature.

A human rake is nearly straight. The fingertip is driven by wrist and fingers with an effective radius of ~100–150 mm (EST), so a 30 mm stroke turns its heading by L/R ≈ **11–17°** and bows ≤ 1 mm. Target: **heading change ≤ 20° and bow ≤ 1.5 mm over a 25 mm stroke.**

I swept the candidate closed paths numerically (20 000 samples per cycle, best window per chord length, 1.5 Hz):

| Path (mm) | Peak speed @1.5 Hz (mm/s) | 25 mm stroke: heading change / bow | Path share with R_curv ≥ 75 mm | Headings per cycle |
|---|---|---|---|---|
| **Circle r 20 (round 1)** | 188 (126 at 1 Hz) | **77° / 4.4 mm** | 0 % | all, every stroke a curl |
| Circle r 15 | 141 | 113° / 6.7 mm | 0 % | all, curled |
| Stadium, 30 straight + r 6 ends | 147 constant | 0° / 0 | 61 % | 2 |
| **Line (Tusi couple), a = 15** | 141, sinusoidal | **0° / 0** | 100 % | 2, rotatable |
| Thin ellipse 17 × 3 | 160 | 22° / 1.0 | 38 % | 2, rotatable |
| Ellipse 16 × 6 | 151 | 50° / 2.3 | 0 % | 2 |
| Figure-8 (Lissajous 1:2) 20 × 6 | 220 | 16° / 0.4 | 20 % | 4 (±31°, both senses) |
| Rounded triangle (hypotrochoid k = −2, ρ = R/4) | 226 | 10° / 0.2 | 56 % | 3 (120° apart) |

**The circle misses the target by ~4×.** A 25 mm stroke on the round-1 orbit turns 77°: a flick around a curve, the "circling" risk leap-B §LEAP 2 (g)(2) named. Capping windows at 60° caps strokes near 20 mm, and those still turn 60°. Smaller radii are worse. **No circle gives straight strokes.**

**A second problem hides in the same geometry.** Round 1 gets direction wander "free" by sliding the windows around the circle. But the pin-unit nail is **directional**: its 45° plate trails the edge in one heading (pin-unit §2, DR2), and I estimate it presents properly within ~±35° of that heading (EST). On a circle a fixed nail is therefore right for ~20 % of headings, plate-first for another 20 % and side-on for the remaining 60 %. Firmware can rotate the windows but not the nails, **so most of the circle's direction coverage is unusable with the nail it was paired with.**

Leap 1 straightens the stroke, Leap 2 makes the nail work in any heading, Leap 3 sizes and lays out the pad, and Leap 4 makes the path a firmware variable.

---

## LEAP 1 — TUSI PAD: a straight-line rake from rotation that never reverses

**(a) Assumption broken.** "A motor that never reverses must make a round path, so straight strokes need reciprocation and its backlash knock." That has been false since the 13th century. **A planet rolling inside a ring of twice its pitch diameter carries every point on its pitch circle along a straight diameter** (the Tusi couple, a hypocycloid of ratio 2). Equivalently, two equal cranks counter-rotating at equal speed sum to a line: r·e^{iωt} + r·e^{−iωt} = 2r·cos ωt. The motor turns one way forever; the pad goes back and forth in a line with a sinusoidal velocity profile, roughly a hand's rake.

**(b) Principle and sketch.** One N20 gearmotor turns the planet carrier at the rake frequency. The pad hangs on a bearing at a point on the planet's pitch circle, and a printed Oldham cross-slide between pad and frame stops it rotating, so the pad translates. The ring gear is held by an SG90 servo instead of the frame, and **turning the ring turns the line**: any heading in 180°, set at ~60°/s, without stopping the stroke motor.

```
 TOP VIEW (above the hair guard)                      SIDE SECTION
                                                        N20 gearmotor (1 way, 60–120 rpm)
   ring 36T int. (pd 28.8)  ◄── SG90 turns ring = turns line   │ carrier arm r = 7.2
   ┌──────────────────────┐                             ┌──────┴──────┐ ring 36T, rotatable
   │      planet 18T       │                             │ planet 18T ◯│ (servo, ±90°)
   │   (pd 14.4) ◯───●─────│── pad bearing on pitch circle└──────┬──────┘
   │  ●  traces a straight │                                    ● pad pin + bearing
   │     line, 28.8 long   │                             ═══════╪═══════ Oldham cross-slide
   └──────────────────────┘                             (two printed slots; pad cannot rotate)
                                                          ┌─────┴──────────┐ PAD (rigid cap R 85)
    pad path:  ●<━━━━━━━━━━━━━━━━━━━━━━━━━>●             │ 16 pressure pins│ 76 × 76 mm
               ↑ end zones (outer 15 %):  ↑              └─╥──╥──╥──╥─────┘
               slow (≤ 53 % v_peak), pins   lift and land    ▼  ▼  ▼  ▼ nails (Leap 2 tips)
               here, 88–118 ms per end   hair ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

The line is the ring's pitch diameter, **28.8 mm**, for a module-0.8 36T ring and 18T planet (carrier arm 7.2 mm). Moving the attachment to a distance d from the planet centre gives an ellipse with semi-axes 7.2 + d and |7.2 − d|. So one rig draws a line (d = 7.2), a thin ellipse (d = 5 → 24 × 4 mm) or a circle (d = 0), and the A/B against round 1 is a one-screw change.

**Gating fits the line's rhythm.** On a sinusoid the pad is slowest exactly where a stroke must end. Gate pins inside |x| ≤ 0.85a: the contact stroke is 1.7a (25 mm at a = 14.7); the pin lifts while still moving at 53 % of peak (H-5.3 asks ≥ 30 %), crosses the reversal in the air (H-5.2, DR4) and lands on the return already moving. The end-zone time is the gate's budget:

| Rake freq | End-zone time (lift + land) | v_peak (mm/s) | Speed at gate | Peak accel in contact (H-5.4 ≤ 2 m/s²) |
|---|---|---|---|---|
| 1.0 Hz | 177 ms | 92 | 49 | 0.49 |
| **1.5 Hz** | **118 ms** | **139** | **73** | **1.11** |
| 2.0 Hz | 88 ms | 185 | 97 | 1.97 |
| 2.5 Hz | 71 ms | 231 (> H-5.4's 200) | 122 | 3.1 |

With the pneumatic gate's 30–60 ms per transition (leap-B, EST), **every pin can rake both ways up to ~2 Hz**, which is the human P1 rake at 2f strokes per second per pin (3/s at 1.5 Hz). Above 2 Hz, use **alternating sets**: set A strokes outbound, set B inbound, each pin lifted for a whole half-cycle (≥ 125 ms at 4 Hz). The skin still gets a continuous two-way scrub, at f strokes per second per pin. Shorter strokes at higher frequency come from narrower windows, as with hands.

**(c) Sensory variables.** §7 rank 5 (edge) and rank 8 (direction): every stroke is straight (0°, 0 mm, against 77° and 4.4 mm) with a definite heading the hair-lie map can choose (H-5.1). Rank 4 (velocity): a bell profile that peaks mid-stroke and slows into the lift, where the circle runs at constant speed and chops strokes at full speed. Rank 1 is kept: per-pin windows, landing jitter and force rails are unchanged, and heading wander (±20° per 3 cycles, §4.4) comes from the servo. Hair: every loaded path is monotonic between lift-offs, which is H-5.7's "hair-positive". The circle's loaded arcs turn up to 77°, the curling H-5.7 warns about, and the guard underside now sweeps a 29 mm line instead of a 40 mm circle, so the canopy is combed rather than stirred.

**(d) Plausibility.** Two printed module-0.8 gears (PETG or nylon), a 3 × 7 mm bearing, a cross-slide, an N20 (100 rpm, $6) and an SG90 ($3) [EST]. Shaking force: ~60 g moving × 1.31 m/s² = **0.08 N** at 1.5 Hz, 0.14 N at 2 Hz, under the drag disturbances concept-A §3.1 already absorbs. One new noise source: the pad's inertial load reverses at each line end, so gear backlash changes flank twice per cycle. With pins lifted that is ~0.6 mN·m at the carrier, a faint tick, and a felt drag pad on the planet (≥ 2 mN·m) keeps the backlash from crossing [EST]. The ring servo reacts the stroke drag (4 × 0.1 N × 14 mm ≈ 6 mN·m against ~180 mN·m); a felt brake on the ring stops it chattering with stroke direction. Everything is above the guard (red line 1), and the pad never rotates.

**(e) Cheapest experiment (≈ $15, one evening): Spirograph traces.** Print the 36T ring and an 18T planet drilled for a pen at d = 0, 2.5, 5 and 7.2 mm, and turn the crank by hand. Beside the traces, draw a 20 mm-radius compass circle. Mark chords with a ruler; measure bow with calipers and heading change with a protractor on the end tangents. **Pass:** the line bows ≤ 0.5 mm over 25 mm (predicted 0, against 4.4 mm on the circle); over 20 mm, the d = 5 ellipse bows ≤ 1.2 mm (predicted 0.9 mm, 29°) against 2.7 mm and 60° on the circle. **Weekend follow-up (+$15):** motorise it (N20, Oldham slide, SG90 on the ring), put four felt pens in a printed 4 × 4 plate, and photograph straight parallel rakes at 0°, 30°, 60° and 90° ring settings. Then hold it on your own head with Leap 2 tips, switching line and circle (the d = 0 hole) every 20 s, and rate nail-likeness and circling.

**(f) Replaces / combines.** It replaces the twin-eccentric circle of leap-B §LEAP 2 and keeps the rest: pressure pins, per-pin windows, force rails, a motor that never reverses. The windows now choose **which part of a straight line** each pin scratches, plus which pins and how hard. The circle stays available as a mode.

**(g) Why it might not work.** (1) All active pins share one heading at any instant. So does a hand in P1, but round 1's simultaneous per-pin direction differences (a P4 flavour) are lost. (2) Gate latency caps two-way raking at ~2 Hz; an 80 ms valve drops it to ~1.1 Hz and makes alternating sets the default. (3) Oldham slides and printed gears make sliding and meshing noise 30–40 mm from the ear. It can be enclosed but must be measured. (4) At pad level a line is a reciprocation, so a pin that misses its lift reverses under load. The per-pin pressure sensor must confirm every lift, and a missed lift triggers an all-lift.

---

## LEAP 2 — OMNI-NAIL ON A TRAILING NECK: an edge in every heading, for free

**(a) Assumption broken.** "A nail has a front." The pin-unit nail has one correct heading (±35°, EST), which forces either a pad yaw at every direction change or strokes confined to one family. Any path with direction coverage (circle, rotatable line, rounded triangle, two-way rake) needs a tip without a front.

**(b) Principle.** Make the tip a **body of revolution**: a 90°-included cone truncated to a Ø 2 mm flat with an R 0.3 rim, flaring to Ø 7 mm at 2.5 mm height. Mount it on the existing **round** music-wire neck (pin-unit §3b: 0.38 × 12 mm, k ≈ 17 N·mm/rad, isotropic in bending). In every heading the leading face is a 45° flank (DR2 asks 30–60°), and nothing sits below the rim. Then let drag lean the neck back. A pendulum dragged backward tilts its foot so the **leading rim drops and bears while the trailing rim lifts**. That turns the isotropic tip into an edge aimed along the current heading, with no yaw joint and nothing rotating.

```
   lean from drag (heading →)              tip section (to scale ×5)
        │  pin (pneumatic, vertical)              ╱‾‾‾‾‾‾╲   Ø 7 at 2.5 mm
        │                                        ╱  90° cone ╲  45° flank both ways
         ╲  neck 0.38 wire, 12 mm               ╲__________╱
          ╲ θ = 5–15°                                Ø 2 flat, R 0.3 rim
           ▼═  leading rim bears, trailing rim lifted 0.2–0.5 mm
   ~~~~~~~~~~~~~~~ hair ~~~~~~~~~~~~~~~
```

**Lean (EST).** Drag µF_n acts L = 12 mm below the neck root, and the normal force destabilises, so θ = µF_nL / (k − F_nL). It is stable while k > F_nL (7.2 N·mm/rad at 0.6 N; 17 is safe). That is pin-unit's caster finding stated as a margin.

| F_n | µ = 0.35 (steady) | µ = 0.7 (plowing spike) |
|---|---|---|
| 0.2 N | 3.3° | 6.7° |
| 0.3 N | 5.4° | 11° |
| 0.6 N | 15° | 29° |

**(c) What it does.**
1. **Direction coverage becomes real** on any path. At 10° lean the bearing arc is ~3 mm, inside scratch-model's 2–8 mm. Even at zero lean the Ø 2 flat at 0.3 N gives ~100 kPa, in the nail band (§3.11e) and clear of the "≥ 2 mm radius pad" FAIL. Unlocks §7 rank 8.
2. **Passive plow relief.** On a spike the lean doubles and the attack flattens toward glide, the safe direction (tip-interface §2.3). That is the **tangential** compliance H-4.11 asks for.
3. **The finger's roll at lift and landing.** The gate ramps pressure down over 30–60 ms, so drag falls with F_n and the lean unwinds smoothly with the leading rim rising first, as H-5.2 asks ("rotate about the trailing edge as a finger does"). Stored energy at 15° is only ~0.6 mJ, but it must leave through the ramp: never a hard vent, or it flicks hairs. A pin landing on a moving pad touches down already leaning, the shallow plough-in H-5.3 wants.
4. **Two-way rakes on Leap 1 need nothing else.** The same pin presents a correct edge outbound and inbound, the way a human nail reverses by changing finger angle.

**(d) Plausibility.** The tip is turned, or printed and polished, acetal or PETG on the TM1 tang (mount standard unchanged), ~0.1 g; neck and fatigue as pin-unit V1 (110–220 MPa steady, infinite life). The bearing arc is UNKNOWN until pressed on skin.

**(e) Cheapest experiment (≈ $5, an evening).** Make three tips on 0.38 mm wire necks in a pen body: Ø 2 flat, Ø 3 flat, and a TM1 directional nail as control. Drag each across inked paper on a kitchen scale at 0.3 N in eight headings; the footprints show lean and bearing arc. Then try each on the scalp in eight headings and rate "nail or pad?" (scratch-model §9 Q6). **Pass:** the omni-tip is nail-like in all eight; the TM1 nail in ≤ 3.

**(f) Replaces / combines.** It replaces the directional TM1 nail on any moving pad and removes the case for pad yaw. Leaps 1, 3 and 4 need it, and it improves the round-1 circle too.

**(g) Why it might not work.** (1) It may feel "rounder" than a 4–6 mm straight nail edge; a Ø 3 flat lengthens the arc but drifts toward a pad. (2) Lean depends on force and friction (5–15° across the force rails), coupling attack angle to intensity. (3) Sebum (µ > 1) could lean it past 40° at 0.6 N; a 30° stop (a ferrule lip inside the sleeve) caps that.

---

## LEAP 3 — 4 × 4 "VIRTUAL HAND" ON A RIGID CAP: the pins conform, the pad doesn't

**(a) Assumptions broken.** (i) "A hand-sized pad must conform to the head with hinges or a membrane." (ii) "Pins should copy a hand (a curved row of four) or be hexagonal for isotropy." Both fail once the pins are long-stroke constant-force pistons and firmware chooses which ones act.

**(b) Principle.** Put 16 pressure pins on an **18 mm square grid** (field 54 × 54 mm; pad outline 76 × 76 mm with rounded corners, about a palm) in a **rigid spherical cap, R 85 mm, with pins radial**. For the current Leap 1 heading, firmware picks a **rake row of 3–4 pins** roughly perpendicular to it: lateral gaps 14–28 mm, along-stroke stagger ≤ 12 mm, so the middle pins can lead like a cupped hand's middle finger. Every few strokes the row steps along the heading, a **virtual carrier** inside the pad. After 3–4 row positions (~10 s) the pad moves physically.

```
  pad top view, 18 mm pitch, heading → (rake ⟷)          row choices for 0°, 30°, 45°
   ┌───────────────────────────┐
   │  ○    ○    ○    ●          │     0°:   one column of 4 (gaps 18)
   │  ○    ○    ●    ○          │    45°:   anti-diagonal of 4 (gaps 25.5)
   │  ○    ●    ○    ○          │    30°:   staggered 3–4 (gaps 16–25, stagger ≤ 12)
   │  ●    ○    ○    ○          │     row steps → 0 / 18 / 36 / 54 mm = virtual drift
   └───────────────────────────┘   ● = active row for 45°;  76 × 76 mm pad, 16 pins
```

**Layouts (EST; exhaustive search over pin subsets, headings every 3–5°; rake row = gaps 14–28 mm, stagger ≤ 12 mm):**

| Layout | Pins | Field (mm) | Headings with a 3-nail row | with a 4-nail row | Virtual drift (median) |
|---|---|---|---|---|---|
| Fixed curved row of 5 (fingertip arc R 70) | 5 | 76 × 11 | 38 % | 18 % | 0 (pad must yaw) |
| Square 3 × 3 @ 20 | 9 | 40 × 40 | 77 % | 0 % | small |
| Hex 7 @ 20 | 7 | 40 × 35 | 80 % | 0 % | small |
| Hex 19 @ 18 | 19 | 72 × 62 | 83–90 % | 67–70 % | 60 mm |
| Hex 19 @ 16 | 19 | 64 × 55 | 100 % | 85 % | — |
| **Square 4 × 4 @ 18** | **16** | **54 × 54** | **100 %** | **89 %** | **46 mm** |

**Hex is not the isotropic choice at hand-like pitch.** Its 30°-offset rows sit at √3 × 18 = 31 mm, wider than a hand's 28 mm finger gap; a square grid's diagonals sit at √2 × 18 = 25.5 mm, inside it. The square 4 × 4 beats hex-19 with fewer pins. A fixed fingertip arc is worst: it reads as a hand only when the stroke is perpendicular to it, and otherwise its nails follow one another in a single track.

**Pin count and spacing.** At 4 pins the pad must yaw to turn, at 9 there are no four-nail rows, and at 16 there are rows in nearly every heading plus 46 mm of virtual drift. Each pin beyond that costs $4–8 and a tube for little gain, **so 16 is the knee.** Scalp two-point acuity is UNKNOWN (15–39 mm between forehead and back). At 18 mm, neighbours sit near fusion and pins two apart (36 mm) are surely distinct, so firmware chooses "one broad nail" or "spread fingers": spacing (§7 rank 11) becomes a firmware variable.

**Why rigid.** At the field corner (38 mm out), an R 85 cap mismatches an R 60 occiput by +4.6 mm and an R 150 parietal by −4.1 mm. A 29 mm line on an R 90 head adds up to ~6 mm of height change at the pad edge [EST]. So each pin needs **±10 mm of constant-force float**, which a 7 mm-bore pressure pin has (±15 mm, leap-B). With radial pins, tilt from translation is a/R ≈ 9.5°, inside the neck's ±10–15°. Hinges would put joints in the 30 mm hair zone (red line 1) and are only needed for the concave nape, a later experiment (scratch-model §5). A compliant membrane puts elastomer on the canopy (DR8: µ > 1, grabs hair). **Conformity is the pins' job.**

**(c) Sensory variables.** §7 rank 6 (count, asynchrony) and rank 11 (spacing) become per-stroke choices; ranks 13–14 (region, dwell) get a fine-grain virtual carrier. H-5.5 (≤ 8 strokes per ±15 mm patch, then move ≥ 20 mm) is met by stepping the row two pitches every ~2.7 s at 1.5 Hz.

**(d) Plausibility.** 16 pins × 2–3 g, plus ~25 g of plate, cap and guard, plus ~35 g of Leap 1 drive ≈ **100–110 g** [EST], about leap-F's "deck of cards". Valves and sensors cost $4–8 per pin, **$64–128** in all, and the tube bundle is ~12 mm across. The pad sweeps ~90 × 76 mm, **~11 % of a ~600 cm² hair-bearing scalp**, well under Michael's 50 %.

**(e) Cheapest experiment ($3 of pens on the Leap 1 rig).** Print the 4 × 4 plate. Felt pens in a column, a diagonal and a staggered set, run at 0°, 30° and 45°, draw each heading's "hand footprint". On the head (Leap 2 tips, pins held down), compare 18 mm rows with 36 mm rows: does 36 mm read as "fingers" and 18 mm as "one broad scratch"? That is the program's first scalp two-point datum.

**(f) Replaces / combines.** It replaces the porcupine's 36-pin field and any pad yaw or hinge. It is the virtual half of the brief's hybrid repositioning: fine moves virtual, coarse moves physical.

**(g) Why it might not work.** (1) Sixteen tubes is a real umbilical. 12 pins (4 × 4 minus corners) keeps 100 % of headings for three-nail rows but only 61 % for four. (2) A rigid convex cap cannot reach the nape or temporal fossa well. (3) A 12 mm stagger may read as "uneven" rather than "cupped". If so, a tighter stagger limit costs some four-nail headings.

---

## LEAP 4 — TWO ONE-WAY MOTORS AS A PATH SYNTHESISER (and the epicycloid verdict)

**(a) Assumption broken.** "The path is the mechanism." Every path in §0 is a sum of rotating vectors, and two of them span the useful family.

**(b) Principle.** Stack two parallel-crank stages (Team A's twin eccentrics). The upper stage is fed from a frame motor through an **Oldham coupling**, which passes rotation across a moving offset at exactly 1:1. Two N20s with Hall encoders, **neither ever reversing**, give z(t) = r₁e^{iω₁t} + r₂e^{iω₂t}. With r₁ = r₂ = 7.5 mm, firmware chooses the path:

| Setting | Path | Use |
|---|---|---|
| ω₂ = −ω₁ | **line**, 30 mm; heading = mean phase | P1 rake (Leap 1 without the servo) |
| ω₂ = −ω₁(1 − ε) | line **precessing** 180°·ε per rev (ε = 1/40 → 4.5°/rev, 180° in ~27 s at 1.5 Hz) | never-repeating direction drift with nothing moving back and forth |
| phase step Δ on one motor | heading jumps Δ/2 | wander; hair-lie map |
| ω₂ = +ω₁, phase δ | **circle** of radius 15·cos(δ/2) | round-1 mode for slow CT episodes; amplitude knob |
| ω₂ = −2ω₁ (needs r₂ = r₁/4) | rounded triangle: three 25 mm sides at 120°, 10° turn | 3 headings per rev with Leap 2 tips; needs a second r₂ |

**Epicycloid verdict ("small fast circle on a slow big circle").** It is carrier and grain in one mechanism, and it fails as grain. A 4 mm circle at 4 Hz on a 20 mm loop at 0.25 Hz gives a 31 mm/s carrier (good CT speed) and 100 mm/s local slip. But a 90° gate window on the grain circle lasts **62 ms**, too short for a 30–60 ms valve to land and lift. Ungated, it is a loaded in-place circle with r ≥ 3 mm, which H-5.7 calls hair-negative and §4.4 disables by default (P3). Gated per half-loop, it scratches 8 mm semicircles that turn 180°. **It makes curls at grain scale.** The better carrier-and-grain is leap-A's straight grain on a drifting pad: the line at 3–4 Hz, alternating pin sets, 8–12 mm windows, and the pad drifting 2–5 cm/s, virtually (Leap 3) or physically.

**Other paths rejected.** *Stadium:* straight at constant speed, but curvature steps from 0 to 1/6 mm⁻¹ at each end, a **3.6 m/s²** lateral jolt twice per cycle. That knock is the machine signature the orbit was meant to remove, and it needs a chain or cam track. *Figure-8:* its inflection gives straight X-strokes at ±31° (16°/25 mm), but peak speed is 1.6× mean and it needs a 2:1 Scotch-yoke XY stage with slots; it is a fair third mode at most. *Thick ellipse* (16 × 6): 50° turn.

**(c)–(g) in brief.** Sensation: path morphing and precession add a new irregularity on top of gating (rank 1), and there is continuous direction drift (rank 8). Plausibility: two encoder N20s ($8–12 each), six eccentric bearings, a printed Oldham disc, ESP32 phase-lock at ±2° [EST], ~20 g over Leap 1, no servo. The line is exact only if r₁ = r₂ to ~0.1 mm; a 0.3 mm mismatch opens a 30 × 0.6 mm ellipse, which is harmless and even gives a fresh return lane. Test: Leap 1's ink rig with two motors; pass if a 60 s precession rosette never retraces a stroke within 2 mm. Risks: ~15 mm more height, two gear trains, wear drifting the radii apart. It is Leap 1's upgrade path, not its replacement.

---

## Ranking (1–5, 5 best)

| Leap | Sensation | Plausibility | Hair / safety | Build | Total |
|---|---|---|---|---|---|
| **L1 Tusi pad** | 5 (straight strokes, bell velocity) | 4 | 5 (monotonic loaded paths) | 5 | **19** |
| **L2 Omni-nail + trailing neck** | 4 (direction made usable) | 4 | 5 (plow relief, roll at lift) | 5 | **18** |
| **L3 4 × 4 virtual hand, rigid cap** | 4 | 4 | 4 (16 tubes) | 4 | **16** |
| Round-1 circle (reference) | 2 (77° curls; nail wrong for 80 % of headings) | 4 | 3 | 5 | 14 |
| L4 Two-motor path synthesiser | 3 | 3 | 4 | 3 | 13 |

---

## Best bet: the Tusi pad with omni-nails on a 4 × 4 rigid cap (L1 + L2 + L3)

Round 1 had the right idea: a motor that never reverses, and per-pin phase windows that turn a shared motion into private strokes. It drew those strokes from the wrong curve. On a 20 mm circle a 25 mm stroke turns 77° and bows 4.4 mm, and most of its direction coverage reaches a directional nail side-on or backward. A planet rolling in a ring twice its size turns the same one-way rotation into a **straight 29 mm line** whose speed peaks mid-stroke and slows into the ends. The ends are exactly where the valves need time: 118 ms at 1.5 Hz, enough to lift and land, so every pin rakes both ways without reversing under load up to ~2 Hz. Above that, alternating sets take over. A servo on the ring sets the heading while the stroke motor runs on. **Omni-nails** (90° cone, Ø 2 mm flat, R 0.3 rim) on the existing round neck lean 5–15° with drag, which gives a leading edge in every heading, plow relief and the finger's roll at lift. **Sixteen pins on an 18 mm square grid** in a rigid R 85 cap (76 × 76 mm, ~105 g, ~11 % of the scalp) give a three-nail row in every heading, four nails in 89 %, and 46 mm of virtual drift, with curvature absorbed by the pins' constant-force stroke. First test: about $15 and one evening with a printed 36T ring and 18T planet, drawing a line, ellipses and a circle beside a 20 mm compass circle, then measuring bow and heading with ruler and protractor.
