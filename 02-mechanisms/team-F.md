# TEAM F — Radical Simplicity and Unconventional Physics

**Seed family:** mechanisms a clever person builds in a weekend for about $80 that might still beat multi-servo robots on sensation.
**Selected concept:** **WR-1 "Walking Rake"** — a single N20 gearmotor driving two scotch-yokes on one shaft, so three independently sprung fingernails trace a flat ellipse: pull across the scalp for ~30 mm, lift 13 mm, return in the air, land again. The sewing-machine four-motion feed, inverted and pointed at a head.
**Status:** concept-level engineering design per the Team Brief. Firewall respected (no other team files, no prior-art file read).

---

## 1. Family exploration — seven concepts

Every concept is judged first against scratch-model §1.2 (does the contact land in the SCRATCH column?) and §8 items 1–6, then against hair-interaction H-5.2 (lift at every reversal) and safety red line 1 (no exposed rotation within 30 mm of hair). The ones that fail a gating rule are dismissed quickly but honestly.

### F1 — Motorized scratch wand (semi-automatic)

A hairbrush-sized handle containing a motor and a 3-finger rake that reciprocates ~30 mm along the handle axis; Michael holds it and chooses the region, the machine does the fine stroke. This is the fastest route to a sensation answer — no mounting problem, no coverage problem, no region-change mechanism — and the hand provides free "irregularity" (drift, pauses, re-angling). Its faults: it is not hands-free (brief §1), and if the stroke is a plain reciprocation, the return stroke runs with the nail plate leading (scoop, H-4.3 violation) unless the mechanism lifts on return. Conclusion: keep the wand not as a mechanism but as a **mount mode** for whichever mechanism wins — the module must be small and self-contained enough to bolt onto a handle on day 1 and onto a headband on day 3.

```
      hand ──> [======= handle: N20 + crank ======]
                                          ║ guard
                                     ╭────╨────╮
                                     │ carrier │ ← reciprocates 30 mm
                                     ╰─┬──┬──┬─╯
                                       │  │  │   3 sprung fingers, 20 mm pitch
                              hair  ~~~\~~\~~\~~~~
                              scalp ────▼──▼──▼────
```

### F2 — Gravity / pendulum rake (passive-inertial)

A rake of 3–4 fingers hangs from a pivot ~80 mm above the crown on a stationary frame; a slow eccentric mass or a nudging crank at the pivot keeps it swinging. Dead weight sets the normal force (the cleanest force cap in safety §3.1: 60 g → 0.6 N, impossible to exceed), gravity plus inertia give the stroke, and the arc of the swing lifts the tips at each end. Problems: (1) the swing is a pure sinusoid at the pendulum's natural frequency — the most predictable stimulus possible (scratch-model §4.3, item 8 FAIL); (2) both half-swings are in contact, so one of them runs plate-leading; (3) stroke amplitude is set by damping, i.e., by how much hair drag there is, so it is uncontrolled. The dead-weight idea is excellent; the pendulum is not. Rejected, but its lesson (a mechanical constant for force) is carried into WR-1.

```
          frame ──┬── pivot
                  │
                  │  rod (swings ±20°)
                  │
             [ weight ]
              ╭──┴──╮
              │rake │   tips trace an arc; contact at the bottom
            ~~\~~\~~\~~  hair
            ───▼──▼──▼──  scalp
```

### F3 — Rolling nail wheel ("paddle wheel"/cam wheel) with full shroud

A wheel of 6–8 radial nail blades, axle ~20 mm above the scalp, turning so each blade plants, drags through an arc, and lifts — like feet. It is attractive because each blade leaves the skin by rotation (exactly the finger-like lift-off H-5.2 asks for) and the stroke needs no reciprocation. Three findings kill it:

1. **Attack angle inverts within one contact arc.** A radial blade enters leaning the right way (plate trailing, ~42° to the skin at entry for R 30 / h 20), passes vertical at the bottom (90°, "digs and catches"), and exits leaning the wrong way (plate leading = scoop). Swept or hinged blades move the problem, they do not remove it: any blade fixed to a rotating hub crosses 90° during contact.
2. **The 30 mm rule cannot be satisfied by a shroud.** A shroud is a stationary dome with a slot through which tips protrude. The slot is an open sliding gap in the hair zone — the exact feature red line 1 names ("or any open sliding slot in the hair zone"). Per-blade boots are impossible on a continuously rotating hub (a boot cannot rotate forever). A hair that enters the slot meets a rotating hub: capstan trap, S3–S4 (hair-interaction §3.1). The shroud does not satisfy the rule; it only hides the violation.
3. **No lift between bouts, no pause.** The wheel either turns or it does not; it cannot "rest the nails" (P5) without stopping in contact.

The only lawful relative of the wheel is a finite rocking foot (< 1 turn, H-6.2 method 2), which is concept F5. Rejected on red line 1 and H-4.3, not on sensation.

```
                 axle (rotating!)             ╭─ shroud with slot = open sliding gap
            \   │   /                          │
         ────●──┼──●────  blades                ▼
            /   │   \                 ╭──────────────────╮
       ~~~~~~~~\│/~~~~~~~ hair        │ ====== slot ===== │
       ─────────▼────────  scalp      ╰──────────────────╯
            entry 42° → bottom 90° → exit scoop
```

### F4 — Head moves against static nails (headrest rake)

A fixed, compliant 3–5 finger rake on a headrest or on the back of a chair; the user nods or rolls slowly, or a slow motor rocks the headrest. Zero actuators on the head, trivial hair geometry (nothing moves relative to the frame except the head). Two fatal problems: (1) the stroke is self-generated, and self-generated touch is centrally attenuated (scratch-model §4.3, the self-tickle mechanism) — the one thing the north star cannot tolerate; (2) if a motor rocks the headrest instead, it moves a 4–5 kg head to produce a 30 mm stroke (KE and neck loading far outside safety §2.4, and no lift-off control at all). The motorized-headrest variant is the same relative motion as moving the rake, with 100× the moving mass. Rejected. One useful residue: in any lean-in or head-worn design, the user's own small head movements are free, uncorrelated jitter, and WR-1 counts on that.

```
                 headrest ──────┐
          static sprung rake    │
                 \  \  \        │
       head ──>  ~~~~~~~~~ hair │
       moves     ───────── scalp│
       (nods ±30 mm)            │
```

### F5 — Single-servo oscillating "finger wiggle" arm

One servo swings a 45–50 mm arm about a pivot above the scalp; three sprung fingers on the arm end sweep an arc. The arc itself lifts the tips at the ends of the swing: with pivot height 45 mm and a 3 mm dip the tips are in contact over a ~35–40 mm chord and 5–7 mm clear at ±40°, so every reversal happens in the air (H-5.2 satisfied by geometry, not by control). Fully programmable amplitude, speed, pauses and per-stroke jitter — the strongest "pattern" machine in this family, and the natural programmable sibling of WR-1. Its single serious defect is physical, not electronic: **both half-swings are in contact, in opposite directions, with one fixed nail angle.** A nail at 45° is a one-way tool; on the return half the plate leads and scoops hair under the edge (H-4.3). I examined passively flipping nails (a pawl that re-leans at each reversal): friction and inertia both drive a free-pivoted tine to the trailing, plate-leading orientation — physics wants the wrong lean on every stroke, so the lean must be forced by a second actuator or cam. That turns F5 into a two-DOF module (servo + lift/tilt), which is a fine design but no longer radically simple. Kept as the recommended upgrade path (SP2) if the predictability penalty proves large.

```
              servo ●── pivot (45 mm above scalp)
                     \
                      \  arm swings ±40°
                       \
                   ╭────┴────╮ carrier + 3 sprung fingers
                 ~~\~~\~~\~~~~~ hair
                 ───▼──▼──▼──── scalp   (arc lifts tips at both ends)
```

### F6 — WR-1 "Walking Rake": one motor, two eccentrics, pull–lift–return  (SELECTED)

One N20 gearmotor turns a printed double-eccentric. Pin 1 (r = 20 mm) rides in a vertical slot of the finger carrier and gives x = 20·sin θ (a 40 mm stroke); pin 2 (e = 8 mm, set 90° later on the same disc) rides in a horizontal slot of the lift frame that carries the carrier's slide rods and gives z = 8 − 8·cos θ (a 16 mm lift). The carrier therefore translates around a flat ellipse with no rotation anywhere below the housing. Three printed fingers with integral flexures hang from the carrier, each ending in an SP1-TM1 pocket holding a nail blade at 45°. On the bottom of the ellipse the nails are pressed into the scalp by a set dip (3–5 mm of flexure travel); on the top they are 11–13 mm clear. Result: a unidirectional 27–33 mm pull at 60–180 mm/s, lift-off at a 20–30° ramp while still moving forward, a fast return in the air, and a 20–30° plough-in landing — the human P2 "sweep, lift, return" primitive at P1 stroke length, with every reversal lifted. Sewing machines have done this since 1854 (the four-motion feed dog); nobody has pointed it at a scalp. Developed in §2.

```
   housing (sealed) ┌────────────────────────────────┐
                    │  N20 ──■ double eccentric      │
                    │          r=20 pin → carrier slot│   all rotation here,
                    │          e=8  pin → frame slot  │   ≥ 50 mm above scalp
                    │  lift frame ═╤═ vertical rods   │
                    │  carrier ──┬─┴─ horizontal rods │
                    └────guard───┼───────────────────┘
                      3 flexure  │  fingers (gapless)
                        \    \   │ \      path of a nail:   ╭──── return (lifted 13 mm)
                    ~~~~~\~~~~\~~~~\~~~  hair           ╭──╯            ╰──╮
                    ──────▼────▼────▼──  scalp     land ╰── pull 30 mm ──╯ lift
```

### W1 — Wildcard: air-jet near-root canopy sweep

A 1 mm nozzle on a slow 2-axis sweep (or simply a hand-held wand) blows a 20–40 L/min jet at the scalp at 45°, parting the canopy and bending hairs near the root without any solid contact. It is the only way to test scratch-model open question 1 (is near-root hair deflection alone pleasurable?) with zero hair-safety risk: nothing can wrap, pinch or pull. It fails the scratcher test by construction (item 1: no edge; item 2: never touches skin; item 4: no slide), so it cannot be SP1. It costs $15 (aquarium pump or a blower fan + printed nozzle) and one evening, and it would tell us how much of the pleasure is component A. Recommended as a side experiment, not a candidate. (Electrostatic hair-lifting and a tendon-plucked "nail harp" were also considered; both fail item 1 or item 4 and add nothing the air-jet does not.)

```
      pump ──[tube]──> nozzle ╲ 45°
                               ╲  air jet
                       ~~~~~~~~~\~~~~~~ hair parts near root
                       ───────────────── scalp (no contact)
```

### Selection

| Criterion (brief §13) | F1 wand | F2 pendulum | F3 wheel | F4 headrest | F5 servo arm | **F6 WR-1** |
|---|---|---|---|---|---|---|
| Edge reaches skin, slides, 2–20 cm/s | yes | yes | yes | yes | yes | **yes** |
| Lift at every reversal (gating) | no (plain recip.) | ends only | by rotation | no | yes (arc) | **yes (cam/ellipse)** |
| Plate trailing on every contact stroke | no | no | no | no | no | **yes** |
| Red line 1 (no rotation in zone) | yes | yes | **FAIL** | yes | yes | **yes** |
| Not self-generated | yes (motor stroke) | yes | yes | **FAIL** | yes | **yes** |
| Irregularity available | hand | none | none | hand | full | speed/pause + hand |
| Hands-free possible | no | yes | yes | yes | yes | **yes (band)** |
| Cost, parts | $50 | $40 | $40 | $20 | $90 | **$85–115** |
| Weekend build | yes | yes | yes | yes | yes | **yes** |

WR-1 is the only concept that passes every gating item while staying a one-motor machine. F5 is its programmable sibling; F1 is its day-one mount.

---

## 2. WR-1 "Walking Rake" — concept-level engineering design

### 2a. Working principle, and why it will feel like fingernails rather than a massager

Scratch-model §1.2 says a scratch is: a hard keratin-like edge (R 0.1–0.3 mm, 3–6 mm line), 0.1–0.5 N per contact, sliding 10–50 mm on the skin at 3–20 cm/s, 1–4 Hz, hair deflected within 2–5 mm of the root, several contacts with unlocked timing. §1.2's two unique signatures are (1) a stiff narrow edge that reaches the skin through the hair and (2) hair deflected near the root rather than at the tips.

WR-1 delivers each of these by construction, not by control:

- **Edge, reach, root deflection (components A and B).** The contacts are tip-family blades A/B/C on the standard TM1 tang, 12 mm wide, 0.3–0.6 mm edge radius, presented at 45°, protruding 36 mm below the carrier (H-4.5 asks ≥ 25 mm). A narrow blade finds inter-hair lanes (hair-interaction §2.1, parting force < 10 mN) and reaches skin; it is the same blade that the tip track's T3 scalp A/B will have validated on the hand wand before WR-1 moves it. The mechanism's only job is to move a proven nail the way a hand does.
- **Light force with a hard mechanical ceiling.** Each finger is a sprung cantilever: F = 0.3 N preload + 0.15 N/mm × dip. At the baseline 3 mm dip, F runs 0.30 N at touch-down, peaks ~0.75 N mid-stroke (the scalp's convexity adds ~1.7 mm of dip at the centre of a 27 mm chord), and falls back to 0.3 N at lift-off. That bell-shaped force profile — light at entry, firm in the middle, light at exit — is the human stroke-to-stroke force shape of scratch-model 3.10 (force dip at the ends) produced by geometry. Per-finger force sits in the tip-interface "crisp scratch" window (0.3–0.9 N for a 6 mm loaded edge). The hard stop at 8 mm of flexure travel caps any finger at 0.3 + 1.2 = 1.5 N whatever the motor does.
- **Slide, not press (component B's plough-and-release).** The nail translates 27–33 mm across the skin per cycle with slip (the scalp cannot follow a 0.5 N edge for 30 mm); the normal-direction motion is 16 mm of lift *between* strokes, never oscillation during one. Tip-interface §2.3: "the scratch sensation is the skin being ploughed and released, not pressed."
- **Speed band.** Mean in-contact speed 57 mm/s at 0.5 Hz to 184 mm/s at 1.6 Hz (peak 201 mm/s at 1.6 Hz = the H-5.4 cap, so the firmware ceiling is 1.6 Hz). The slow end is the C-tactile band (1–10 cm/s), the fast end is self-scratch speed (11–18 cm/s). Both optima of §2.2 are reachable with one knob.
- **Multiple contacts.** Three blades at 20 mm pitch, each on its own flexure with 8 mm of independent travel: on the crown's R ≈ 90 mm the outer fingers see ~2 mm less dip than the centre one, so forces spread by ~0.3 N across the hand (≥ 20 % spread, item 7), and the three edges land within ~10–15 ms of each other because of the different dips. Timing asynchrony is weaker than a human hand's 20–80 ms; see 2j.
- **Every reversal in the air (component C's "alive" quality is partly this).** Hair-interaction §2.4 lists three things lift-off does: releases the wave of hair ahead of the edge, resets any strand that slipped under the nail, and re-randomises which lane the nail enters. WR-1 lifts 11–13 mm every cycle, so each stroke starts fresh in a new lane; in medium hair that alone makes consecutive strokes feel different.
- **Why not a massager.** Draw WR-1's contact on the §1.2 table: hard 0.3 mm edge, 0.3–0.75 N, 130 kPa line pressure, 27–33 mm of sliding, 60–180 mm/s, 0.5–1.6 Hz, hair parted at the root — every entry lands in the SCRATCH column. There is no pad, no vibration (the only periodic component above 4 Hz is the N20's gear noise, mechanically isolated from the fingers by the flexures), and no scalp translation.

What WR-1 does *not* reproduce: stroke-length jitter, direction wander, and per-finger timing of a hand. Those are component C (ranked third of five in §1.3) and are addressed by speed jitter, random pauses, manual relocation and the user's head motion. Whether that is enough is the experiment WR-1 exists to run (§2j, §4).

### 2b. Architecture

**Module.** A sealed PETG housing 95 × 65 × 50 mm containing the motor, double eccentric, lift frame and carrier; below it, exposed, only the carrier's smooth underside and three fingers. Mass ~150 g (motor 10, eccentric 8, frame 20, carrier + fingers 30, rods 15, housing 60, wiring 5). Moving element (carrier + fingers) ~30 g.

**Three mounts, same module, same TM1 tips:**

1. **Wand mode (day 1, semi-automatic, the sensation instrument).** The module bolts to a printed 130 mm handle. Michael positions it; the hand sets the dip by feel within the 8 mm flexure window (a wide, toothbrush-like sweet spot) and chooses region, direction relative to the grain, and pauses. Not hands-free; used for the tip and force experiments and the first scalp sessions.
2. **Headband mode (primary, hands-free).** A hard-hat 4-point ratchet suspension ($12–23) with a printed ring that takes its four clip tabs. The ring carries two dovetail sockets: **socket A** in the rear quadrant between the two rear crown straps (upper occiput / crown-rear — the highest-value, simplest-curvature region, scratch-model §5) and **socket B** hanging below the band at the back, over the occipital bun. Each socket accepts the module in four orientations (0/90/180/270°) so the stroke runs with, across, or against the local grain. Between the socket and the module sits a 12 mm sprung **dip stage**: a compression spring pushes the module away from the scalp; a bicycle brake cable (Bowden) to a foot pedal pulls it down to a thumbscrew stop. Pedal down = scratching at the set dip; pedal released = module up 12 mm, zero contact, regardless of power. Region change: lift the module out of one socket and drop it in the other (5 s), or rotate the band for the sides.
3. **Boom mode (optional).** The module on a gas-spring monitor arm ($36) over a chair, dip set by the arm; for anyone who prefers "withdraw the head" as the release (safety §5.5). Not developed further here.

**Coverage per placement:** 40 mm wide (3 fingers × 20 mm) × 27–33 mm stroke ≈ 12–13 cm². Two sockets × four orientations cover the crown-rear and occiput, the two regions scratch-model §5 ranks highest and tolerant of the most force. Sides, nape and temples are wand-mode-only in SP1 (they need ≤ 0.15 N and are explicitly a later experiment).

**DOF:** 1 actuated (motor), 3 passive (finger flexures), 1 manual (dip), plus discrete manual region/orientation changes.

### 2c. Kinematics with numbers

Path of the carrier (and, when not deflected, of each nail edge) relative to the housing: x = r·sin θ, z = e·(1 − cos θ), with r = 20 mm, e = 8 mm, θ the shaft angle; the lowest point is θ = 0.

Computed on a convex crown (R 90 mm), 3 mm dip, k = 0.15 N/mm, 0.3 N preload (script in the team scratchpad; the numbers below are its output):

| Shaft rate | Peak tip speed | Mean speed in contact | Contact chord | Contact per cycle | Force in contact | Landing / lift-off angle to skin | Clearance at the x-reversal (θ = ±90°) | Clearance at top |
|---|---|---|---|---|---|---|---|---|
| 0.5 Hz | 63 mm/s | 57 mm/s | 26.6 mm | 23 % (463 ms) | 0.30–0.75 N | 20° / 20° | 7.2 mm | 13.0 mm |
| 1.0 Hz | 126 | 115 | 26.6 | 23 % (231 ms) | 0.30–0.75 | 20° / 20° | 7.2 | 13.0 |
| 1.3 Hz | 163 | 149 | 26.6 | 23 % (178 ms) | 0.30–0.75 | 20° / 20° | 7.2 | 13.0 |
| 1.6 Hz (cap) | 201 | 184 | 26.6 | 23 % (145 ms) | 0.30–0.75 | 20° / 20° | 7.2 | 13.0 |

Effect of the dip knob (1.0 Hz, R 90): dip 1 mm → chord 16 mm, 0.30–0.45 N, landing 10°; dip 5 mm → chord 33 mm, 0.30–1.05 N, landing 30°; dip 6 mm → chord 35 mm, 0.30–1.20 N, landing 37°, reversal clearance 4.2 mm. **Operating range: dip 2–5 mm.** On a flat side-of-head surface the chord grows to 31 mm and reversal clearance drops to 5.0 mm — still at the H-5.2 minimum. On the occipital bun (R 70) chord 25.5 mm, clearance 7.9 mm.

Alternative eccentrics (printed, 8 g, swap in 2 min): r = 15 → 21 mm chord (short rake); r = 25 → 31 mm chord, landing 14°, speed cap 1.3 Hz; e = 6 → 9 mm top clearance, 29 mm chord; e = 10 → 17 mm top clearance, 25 mm chord (for 8 cm hair).

Velocity profile in contact: sinusoidal, 75 % of peak at touch-down, 100 % mid-stroke, 75 % at lift-off — the bell shape of a hand stroke. The tip leaves the skin while moving forward at ≥ 60 % of stroke speed (H-5.3 asks ≥ 30 %) and enters at 20–30° to the skin (H-5.3 asks ≤ 30°), both consequences of the ellipse's aspect ratio e/r = 0.4.

**Lift-off mechanism (H-5.2, mandatory):** positive, by the lift yoke, every cycle, 11–13 mm above the scalp at the top and ≥ 5 mm with zero contact force at the instant of x-reversal, on every surface in scope. No reversal ever happens in contact. Between bouts the firmware parks the shaft at θ = 180° (top of the ellipse, sensed by a Hall pulse) so a pause is a full lift (DR7).

**Irregularity (the honest part):**
- *Speed*: the shaft rate is re-drawn every revolution from U(0.6, 1.5) Hz (per-stroke speed jitter ±40 %, beyond scratch-model §4.4's ±20 %), and the force profile follows it (friction rises with speed through hair).
- *Pauses*: with p = 0.15 per cycle, park at the top for U(0.3, 2) s; every 4–20 cycles a bout ends with a 1–3 s pause (P5).
- *Slow-mode episodes*: once a minute, 4–8 cycles at 0.5 Hz (CT band, ≤ 0.45 N at dip 1–2 mm if the user turns the knob; otherwise force is unchanged).
- *Location/direction*: manual (socket, orientation, band rotation, or the hand in wand mode) plus the user's own head micro-motion, which in headband mode shifts the stroke a few mm cycle to cycle.
- *Fully periodic control condition*: a switch position with constant speed and no pauses — this is the "fully periodic" control scratch-model §7 item 1 requires, and WR-1 is the cheapest way to produce it faithfully.
- *Not available*: stroke-length jitter, direction wander within a placement, per-finger phase. These are the design's known sensation gap (2j).

### 2d. Force path

Scalp → nail edge → TM1 tang (magnet + pocket walls) → finger body → finger root flexure → carrier → horizontal slide rods → lift frame → lift yoke/pin 2 → eccentric → motor shaft → housing → dip stage → band.

- **Normal force is a mechanical constant (safety §3.1):** F_max per finger = preload + k·x_max = 0.3 N + 0.15 N/mm × 8 mm = **1.5 N**, from the flexure's up-stop lug on the carrier. Three fingers: 4.5 N total. Both well inside red lines 2 and 3 (2.5 N / 12 N). Actuator-stop check: the deepest the lift yoke can put the carrier is the ellipse bottom; with the dip stage at its 6 mm maximum and the head pushed up into the band, flexure travel at the bottom is 6 + 1.7 (curvature) + ≤ 2 (band compliance) < 8 mm, so the flexure cannot be bottomed by the actuator. If the head comes up further, the band's suspension carries it, not the fingers.
- **Compliance per contact:** 0.15 N/mm (adjustable 0.1–0.4 by swapping the finger: the flexure is 1.0 / 1.2 / 1.6 mm thick in three printed variants), travel 8 mm. Scratch-model 3.12 asks 0.1–0.5 N/mm with ≥ 5 mm travel; tip-interface §5.4 asks 0.3–0.6. WR-1 sits at the soft end deliberately: a 1 mm head movement changes force by 0.15 N, not by a stall.
- **Across scalp curvature:** over the 40 mm finger span on R 90 the sagitta is 2.2 mm; each finger absorbs its share within its 8 mm travel. Along the 30 mm stroke the convexity (1.3–1.7 mm) is what makes the force bell-shaped.
- **Tangential yield/breakaway (H-4.11, H-4.13, red line 3):** three layers. (i) The TM1 magnet (N52 6×2 against a 6×1 steel disc) gives 4–8 N axial, which is **~1.5–2.5 N in shear** (component-landscape §3: shear is 1/3–1/5 of axial); a nail dragged by a snagged strand shears off its magnet and falls out of the hair with no tether. Tune by shim to measure ≤ 2 N. (ii) The DRV8871 current limit set to 0.5 A holds motor torque at ~40 % of stall (≈ 0.8 kg·cm → ≤ 4 N at the carrier before the limit, shared by three fingers). (iii) Hall-pulse stall detection: no pulse within 1.5× the expected period → motor off within 300 ms. The hair rule's ideal of 0.15 N tangential yield per element is **not** met by WR-1 (nor, I suspect, by anything that also delivers 0.5 N of scratch drag through a rigid carrier); the primary hair protection is geometric (lifted reversals, gapless fingers, trailing plate) and the normal-direction softness: a strand trapped under an edge lifts the edge at ~0.15 N upward because the flexure is that soft.
- **Finger stability under drag:** the flexure hinge sits 30 mm above and ~12 mm behind the edge; drag at the edge creates a small "dig" moment that normal force opposes. With the finger body at 30° from the scalp (hinge 2.2× further back than the edge is below it), net moment stays lifting for µ up to 1.5, so a grabby patch makes the finger firmer, never self-locking.

### 2e. Hair safety

**Exclusion volume (H-6.1):** everything within 30 mm of the scalp. In WR-1 that volume contains: the three nails, the three finger bodies, the three finger flexures (at 28–32 mm, the boundary), and nothing else. The carrier underside is at 30–33 mm when scratching and 44–46 mm at the top of the ellipse; the horizontal rods, lift frame, yokes, pins, bearings and eccentric are at ≥ 50 mm inside the housing.

**Every joint and gap within 30 mm, with its exclusion method:**

| Item | Where | Method |
|---|---|---|
| Finger root flexure (3) | 28–32 mm above scalp | No joint: a printed living flexure, no gap, radiused ≥ 1 mm; H-6.2 not needed |
| TM1 tang/pocket seam (3) | within 10 mm of the edge | 0.15 mm clearance is in the trap band; **sleeved** per H-4.9 with a 12 mm polyolefin heat-shrink collar over the pocket mouth, renewed with each tip change; magnet seam under the collar |
| Finger-to-carrier dovetail (3) | 32–36 mm | Above the zone for design-basis hair; dovetail runs transverse, mouth faces up, covered by the carrier lip |
| Carrier underside | 30–46 mm | Smooth convex plate, R ≥ 2 mm edges, drafted 15°; acts as the hair-shedding guard for the carrier interior |
| Housing floor window (one) | 50 mm | Open-ended gap ≥ 10 mm all round the lift frame's two columns throughout the cycle (DR5); nothing rotates in or near it |

Nothing within 30 mm rotates, slides, or changes a gap. Long hair (> 15 cm) extends the zone to the housing interior and is out of scope for SP1 (state in item 18).

**Checklist self-score (hair-interaction §6.8):**

| # | Item | Score | Note |
|---|---|---|---|
| 1 | No exposed rotation in zone (gating) | 2 | eccentric at ≥ 50 mm, housed |
| 2 | Every joint in zone has a method (gating) | 2 | table above |
| 3 | No changing / 40 µm–3 mm gap within 25 mm (gating) | 1 | TM1 seam sleeved; verify with the 100 µm line probe |
| 4 | Lift before every reversal (gating) | 2 | ellipse; ≥ 5 mm at every x-reversal |
| 5 | Elements move as a rigid group (gating) | 2 | one carrier; spacing never changes |
| 6 | Blade, drafted, no re-entrant (gating) | 2 | tip A/B; finger widens 12 → 16 mm root-ward; pocket collar |
| 7 | Mount yields ≤ 0.15 N tangential (gating) | 1 | normal softness 0.15 N/mm lifts a trapped strand; tangential breakaway 1.5–2.5 N |
| 8 | Protrusion ≥ 25 mm | 2 | 36 mm |
| 9 | Spacing ≥ 8 mm | 2 | 20 mm pitch, 8 mm edge gap |
| 10 | Low-friction polished, no silicone/TPU | 2 | nail/PETG polished, polyolefin collar |
| 11 | Breakaway 3–5 N, no tether | 2 | TM1 magnet, tune to 4–5 N axial |
| 12 | Hair-shedding guard | 2 | carrier underside + housing floor |
| 13 | With-grain bias / grain map | 1 | direction set per placement by hand; no map in firmware |
| 14 | Dwell/repetition limits | 2 | bouts 4–20 cycles, pauses; relocation manual |
| 15 | Snag reflex lift-and-retract | 1 | stall → stop (not lift); pedal release lifts 12 mm mechanically |
| 16 | Antistatic | 1 | PETG insulating; nylon pick (tip F) and steel (tip G) variants available |
| 17 | Tool-free removal for cleaning | 2 | tips magnetic, fingers dovetail, carrier accessible |
| 18 | Hair variants stated | 2 | short–medium straight/wavy in scope; coarse OK (raise dip); long and curly out of scope |
| | **Total** | **31 / 36** | no gating zero |

### 2f. Safety — the 13 red lines

1. No exposed rotation/open slot within 30 mm: **pass** (housed at ≥ 50 mm; window is open-ended ≥ 10 mm).
2. Normal force bounded by a mechanical constant ≤ 2.5 N: **pass** (1.5 N flexure stop; actuator-stop check in 2d).
3. ≤ 12 N total; ≤ 2 N tangential before something gives: **pass** (4.5 N; TM1 shear breakaway, measured ≤ 2 N).
4. NC e-stop in series with motor power, within reach; hold-to-run for staged tests: **pass** (22 mm NC mushroom on a 1.5 m lead in the free hand; foot pedal is both the Bowden dead-man and a momentary NC contact on the motor rail).
5. No mains, ≤ 24 V, no lithium: **pass** (5–6 V from a certified USB-C or barrel adapter).
6. No moving element anterior to the hairline, within 25 mm of an ear, or above the eyes unguarded: **pass** (sockets are crown-rear and occiput; the module cannot be mounted forward of the band's crown pad; wand mode is procedural).
7. No self-locking drive in the force path without a downstream spring cap and spring-return lift: **pass with note** — the eccentric/yoke is upstream of the finger springs (cap) and the dip stage is a spring-return lift independent of the motor.
8. No contact held after power loss / e-stop / stall: **pass in headband mode** via the Bowden dead-man (release = 12 mm lift, purely mechanical); in wand mode the hand is the release; residual static contact between stop and release is ≤ 0.75 N spring force, not actuator force.
9. No push-fit-only, PLA or brittle tips; proof-loaded 3×: **pass** (TM1 magnet + pocket walls; press-on ABS/nylon blades on PETG tangs; 4.5 N normal / 6 N lateral proof test).
10. One-hand ≤ 3 s release, no chin strap, ≤ 500 g: **pass** (lift the suspension off; ~330 g head-borne incl. suspension).
11. Edges ≥ 1 mm, tips ≥ 0.4 mm: **pass with a tip choice** — first human sessions use tip B (0.6 mm) per safety §3.5; tip A (0.3 mm) after the tape test and T2 forearm screen.
12. First session only after the checklist, wig-head test, glasses, ≤ 5 min: procedural, **planned**.
13. Firmware never the sole barrier for S ≥ 3: **pass** (every S ≥ 3 hazard has a mechanical constant: flexure stop, magnet, dead-man stage, housed rotation).

**Fail-safes:** motor power path = adapter → fuse (1 A) → NC e-stop → foot-pedal NC contact → DRV8871. Logic (Pico) on its own USB branch stays up. Hall watchdog cuts PWM on stall. Power loss or e-stop stops the shaft wherever it is; the pedal (always released when a hand leaves it) lifts the module.

### 2g. Adjustability

| Variable | Range | How | Type |
|---|---|---|---|
| Normal force | 0.3–1.2 N (cap 1.5) | dip thumbscrew 0–6 mm; preload/k by finger variant (1.0/1.2/1.6 mm flexure) | knob / swap |
| Speed | 57–184 mm/s mean | shaft rate 0.5–1.6 Hz, pot | knob + firmware jitter |
| Stroke (chord) | 16–35 mm | dip (coupled to force) and eccentric r = 15/20/25 | knob / reprint (8 g part) |
| Frequency | 0.5–1.6 Hz | same pot | knob |
| Lift height | 9–17 mm | eccentric e = 6/8/10 | reprint |
| Contact angle | 35/45/55° | finger variant (pocket angle) | reprint (three fingers, 10 g) |
| Contacts | 1, 2, 3 | remove tips (magnet) | seconds |
| Spacing | 20 mm; 16 or 25 by carrier variant | reprint carrier | reprint |
| Pattern | periodic / jittered / paused / slow-mode | switch + firmware | firmware |
| Direction vs grain | 4 orientations × 2 sockets; any in wand mode | manual | seconds |
| Tip geometry/material | tip family A–H | TM1 swap | seconds |

Force has a readout: a printed pointer on each finger against a scale on the carrier (0–8 mm = 0.3–1.5 N) visible in a mirror or phone camera; the Hall period gives speed on the OLED/serial.

### 2h. Components and cost

Prices from component-landscape.md; (~) marks its unverified estimates.

| Qty | Item | Unit | Ext. |
|---|---|---|---|
| 1 (+1 spare) | N20 micro metal gearmotor 150:1, 6 V (generic 2-pack ~$8; Pololu HP 150:1 $24 if consistency matters) | — | $8 |
| 1 | Adafruit DRV8871 driver (ILIM resistor sets 0.5 A) | $7.50 | $7.50 |
| 1 | Raspberry Pi Pico | $5 | $5 |
| 1 | A3144 Hall sensor + 3 mm disc magnet (shaft index) | ~$2 | $2 |
| 1 | 10 kΩ pot + knob, 1 toggle, 1 button | ~$4 | $4 |
| 1 | 22 mm NC mushroom e-stop | $8–14 | $10 |
| 1 | Momentary foot switch (NC contact used) | ~$5 | $5 |
| 1 | 5 V 3 A certified adapter (USB-C PD or barrel); a phone charger qualifies | $0–15 | $10 |
| 4 | 623ZZ bearings (2 yoke rollers + 2 spare), from a 10-pk | ~$7 | $7 |
| 2 + 2 | 3 mm × 100 mm and 4 mm × 100 mm steel rod (drill rod, or 3 mm brass tube) | ~$8 | $8 |
| 1 | Compression + extension spring assortment (dip stage, pedal return) | ~$10 | $10 |
| 6 | N52 6×2 disc magnets + 6×1 steel discs / M3 washers | <$1 | $3 |
| 1 | Press-on nail pack (24) and one Tortex 1.14 pick (tip F) | ~$6 | $6 |
| 1 | Bicycle brake cable + housing (Bowden dead-man) | ~$8 | $8 |
| 1 | Hard-hat 4-point ratchet suspension | $12–23 | $15 |
| — | M2/M3 screws, M3 grub screw, heat-set inserts, JST leads, 22 AWG wire, heat-shrink | ~$12 | $12 |
| — | PETG printing, ~280 g (library $0.10/g, or JLC3DP ~$30) | ~$28 | $28 |
| | **Total, headband + wand** | | **≈ $148 all-new; ≈ $115 if adapter, fasteners and wire are in the drawer** |
| | **Wand-only core (no suspension, Bowden, stage)** | | **≈ $85** |

Not included: tools (component-landscape §8), mannequin head and kitchen scale (shared program test gear).

**Printed parts (PETG unless noted, 0.2 mm layers, 4 perimeters on load-bearing parts):**

| Part | Approx. size | Notes |
|---|---|---|
| Housing, two halves | 95 × 65 × 50 mm | motor cradle (TPU 95A insert optional for noise), vertical 4 mm rod seats, Hall pocket, floor window 60 × 28 mm with ≥ 10 mm clearance to the frame columns |
| Double eccentric | Ø 46 × 18 mm | D-bore for the 3 mm N20 shaft + M3 grub; pin 1 at r 20, pin 2 at e 8, 90° apart on two axial levels; each pin an M3 screw carrying a 623 bearing; variants r 15/25, e 6/10 |
| Lift frame | 70 × 40 × 20 mm | two 4.1 mm vertical bores (ream with a 4 mm drill), horizontal yoke slot 26 × 10.2 mm, seats for the two 3 mm carrier rods |
| Carrier | 70 × 24 × 16 mm | two 3.1 mm bores, vertical yoke slot 42 × 10.2 mm, three transverse dovetail sockets with M2 locking screws, up-stop lugs, pointer scale, smooth convex underside |
| Finger ×3 (+3) | 48 × 12–16 × 8 mm | root flexure 15 × 12 × 1.2 mm; body at 30° to the scalp plane; TM1 pocket at 45° (35°/55° variants); printed on its side with layers along the flexure; edges ≥ 1 mm |
| Dip stage | 50 × 40 × 30 mm | 12 mm sprung travel on two 3 mm pins, M5 thumbscrew stop, Bowden anchor |
| Band ring + sockets | Ø 190 × 25 mm (two halves) | four slots for the suspension clip tabs; socket A (rear quadrant) and socket B (hanging rear) |
| Wand handle | 130 × 35 × 25 mm | dovetail to the housing |
| Desk box lid | 100 × 70 | Pico, DRV8871, e-stop, fuse, terminals |

### 2i. Buildability in an apartment

**Tools:** the component-landscape §8 kit (Pinecil, hex keys, calipers, needle files, 3 mm and 4 mm drill bits used as reamers, CA glue, flush cutters, multimeter). No lathe, no mill, no laser.

**Steps (≈ 12 hands-on hours plus ~10 h unattended printing):**
1. Print all parts (one JLC3DP order or two library sessions). Ream rod bores to a sliding fit; polish rods with 1000-grit.
2. Press 623 bearings onto M3 screws in the eccentric pins; fit the eccentric to the N20 D-shaft, grub screw with threadlocker. Check runout by eye.
3. Assemble lift frame on the vertical rods inside the lower housing; drop pin 2 into its slot. Assemble carrier on the horizontal rods in the frame; drop pin 1 into its slot. Turn the shaft by hand through 360°: the carrier must trace the ellipse with no binding (the one risky tolerance — see below).
4. Fit three fingers (dovetail + M2). Make six tip A/B tangs from press-on nails per tip-interface §4 (CA to printed tangs, file to R 0.3/0.6, 2000-grit), epoxy steel discs, seat magnets in the pockets, add heat-shrink collars. Proof-load each tip (4.5 N normal, 6 N lateral) on the kitchen scale.
5. Wire: adapter → fuse → e-stop → pedal NC → DRV8871 → motor; Pico PWM + Hall + pot. Flash the ~80-line firmware (speed draw per revolution, pause logic, top-dead-centre parking, stall watchdog).
6. Bench: force vs dip on the kitchen scale (expect 0.3 N at touch, ~0.75 N at 3 mm, 1.5 N at the stop); film the path at 240 fps against a ruler; measure noise at 10 cm; 20-minute thermal run.
7. Wand handle on; run hair-interaction §7.3 tests 1–9 on the mannequin head (real hair). Then tip-interface T2 (forearm) and T3 (scalp A/B) using WR-1 as the stroke source.
8. Print and fit the band ring, dip stage, Bowden; repeat the entanglement test with the band on the mannequin; then the safety §6 checklist and the staged human protocol.

**Risky tolerances:** (a) yoke slot vs 10 mm bearing: print 10.2 mm, accept up to 0.3 mm play — it becomes a small dwell at the ends of the stroke, harmless; (b) rod bores: too tight binds, too loose rattles — ream to a free slide, lubricate with a drop of PTFE oil (above the hair zone, inside the housing); (c) eccentric D-bore on a 3 mm D-shaft: print 2.9 mm and file; (d) finger flexure thickness ±0.1 mm changes k by ±25 % — calibrate each finger on the scale and label it; (e) TM1 pocket per the standard (±0.1 mm).

### 2j. Honest weaknesses, top-5 risks, and the bench test that retires each

**Weaknesses, plainly:** (1) stroke length and direction are fixed per placement; (2) the three fingers are phase-locked except for curvature-induced ~10–15 ms spread; (3) contact occupies only ~23–31 % of each cycle, so at 1 Hz the scalp feels a 230 ms pull then 770 ms of nothing — a sweep-and-return rhythm, not a rake's continuous back-and-forth; (4) coverage per placement is ~13 cm² and region change is manual; (5) the N20 is on the head, 60 mm from the ears.

| # | Risk | Why it matters | Bench test that retires it |
|---|---|---|---|
| 1 | **Predictability penalty.** A fixed-stroke machine reads as "a machine" within 10–30 s (scratch-model §4.3) and speed jitter plus pauses are not enough | It is the #1-ranked sensation variable; if true, WR-1 loses to F5/multi-servo | Scalp sessions: periodic mode vs jittered mode vs jittered-plus-manual-relocation, 3 min each, rated every 30 s on a 0–10 "still feels like a person" scale; also informs every other team's firmware (this is the control condition the program needs) |
| 2 | **Low contact duty cycle feels like tapping-sweeps rather than scratching** | Component B needs sustained plough-and-release; 23 % duty may read as "flicks" | Compare e = 6 (26 %, 9 mm lift) vs e = 8 vs dip 5 mm (31 %); and r = 25 at 0.8 Hz; if all read as flicks, swap the lift yoke for a dwell cam (printed, same shaft) that holds contact for 50 % of the cycle |
| 3 | **TM1 pocket seam traps hair at the fingertip** | A 0.15 mm seam 10 mm from the edge is in the trap band; the collar must actually seal | Hair-interaction 7.3.5 gap probe with single hairs and the 100 µm line at every collar, 5 min running; any capture → bond the blade directly to the finger (non-swappable finger variants) for the human tests |
| 4 | **PETG flexure creep/fatigue** | 0.3–1.2 N for 20 min, ~2 400 cycles per session at ~0.3 % strain; creep lowers preload, fatigue cracks are fragments near the scalp | 10 000-cycle run on the bench (70 min at 2.4 Hz against a foam head), re-measure k and preload, loupe inspection; if > 15 % drift, switch to the torsion-spring knuckle variant or MJF nylon fingers |
| 5 | **Gear whine near the ears dominates the scratch hiss** (item 12) and bone-conducts through the band | A noisy device fails the ASMR context and annoys within minutes | Phone SPL meter at 10 cm and at the ear position on the mannequin; target ≤ 60 dBA; mitigations in order: 100:1 ratio at lower PWM, TPU motor cradle, mass-loaded housing, Pololu HP motor; last resort move the motor to the desk with a 3 mm flex shaft (component-landscape §4) |

Secondary risks: yoke slot wear (print the slot with a 1 mm PETG wall thickening or line with a 0.5 mm brass strip); the hand in wand mode pressing past the sweet spot (the stop caps it at 1.5 N, so the risk is only "too firm", not injury); and the band's crown pad occluding the true vertex (accepted: crown-rear and occiput are the targets).

### 2k. Massager-vs-scratcher self-score (scratch-model §8)

| # | Item | Score | Evidence |
|---|---|---|---|
| 1 | Edge, not pad | PASS | tip A/B/C, E > 1 GPa, R 0.3–0.6 mm, 4–6 mm loaded line |
| 2 | Reaches the skin | PASS (UNSURE in 8 cm hair) | 36 mm protrusion, narrow blade; penetration fraction is open question 8 for every team |
| 3 | Light | PASS | 0.30–0.75 N typical, 1.5 N mechanical cap; force set by dip, not by strap tension |
| 4 | Slides | PASS | 27–33 mm per cycle with slip; normal motion only between strokes |
| 5 | Right speed band | PASS | 57–184 mm/s, 0.5–1.6 Hz; no component > 4 Hz at the tip |
| 6 | Deflects hair near the root | PASS | blade at skin level, trailing plate, lift re-randomises lanes |
| 7 | Multiple independent contacts | UNSURE | 3 at 20 mm, independent force (≥ 20 % spread), timing spread ~10–15 ms (< 20 ms target) |
| 8 | Irregular | PASS with caveat | speed jitter, pauses, slow-mode, manual relocation; fixed stroke/direction is explicitly the control-condition experiment |
| 9 | Compliant at the tip | PASS | 0.15 N/mm, 8 mm travel, follows R 60–150 |
| 10 | Unloads at reversal, lifts between bouts | PASS | every reversal ≥ 5 mm clear at zero force; parks lifted |
| 11 | Hair-safe geometry | PASS | no rotation/aperture within 30 mm; collar on the only seam |
| 12 | Sounds like a scratch | UNSURE | N20 whine to be measured; nail-on-hair hiss present |

No FAIL on 1–6. The design is a scratcher by the model's own test; its open items are 7, 8 and 12.

---

## 3. Schematic — side view through the stroke plane

<svg viewBox="0 0 720 470" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif" font-size="11">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker>
  </defs>
  <!-- scalp and hair -->
  <path d="M40 400 Q360 330 680 400" fill="none" stroke="#333" stroke-width="2"/>
  <text x="44" y="420">scalp (R ≈ 90 mm)</text>
  <g stroke="#999" stroke-width="1">
    <line x1="120" y1="383" x2="110" y2="360"/><line x1="160" y1="376" x2="150" y2="352"/><line x1="200" y1="370" x2="190" y2="346"/>
    <line x1="240" y1="365" x2="232" y2="340"/><line x1="280" y1="361" x2="272" y2="336"/><line x1="320" y1="358" x2="312" y2="333"/>
    <line x1="400" y1="358" x2="408" y2="333"/><line x1="440" y1="361" x2="448" y2="336"/><line x1="480" y1="365" x2="488" y2="340"/>
    <line x1="520" y1="370" x2="530" y2="346"/><line x1="560" y1="376" x2="570" y2="352"/><line x1="600" y1="383" x2="610" y2="360"/>
  </g>
  <text x="560" y="332" fill="#777">hair canopy (pile 5–20 mm)</text>
  <!-- housing -->
  <rect x="200" y="40" width="330" height="150" rx="10" fill="#f4f4f4" stroke="#333" stroke-width="2"/>
  <text x="208" y="58" font-weight="bold">sealed housing (all rotation here, ≥ 50 mm above scalp)</text>
  <!-- motor -->
  <rect x="215" y="95" width="60" height="30" fill="#ddd" stroke="#333"/>
  <text x="217" y="140">N20 150:1</text>
  <line x1="275" y1="110" x2="300" y2="110" stroke="#333" stroke-width="3"/>
  <!-- eccentric disc -->
  <circle cx="330" cy="110" r="32" fill="#e8e8ff" stroke="#333"/>
  <circle cx="330" cy="110" r="3" fill="#333"/>
  <circle cx="330" cy="130" r="5" fill="#fff" stroke="#333"/>
  <text x="340" y="136">pin 1, r = 20 (stroke)</text>
  <circle cx="338" cy="110" r="4" fill="#fff" stroke="#333"/>
  <text x="365" y="106">pin 2, e = 8 (lift)</text>
  <text x="300" y="80">double eccentric, printed</text>
  <!-- lift frame -->
  <rect x="300" y="150" width="130" height="14" fill="#cfe" stroke="#333"/>
  <text x="440" y="162">lift frame (horizontal yoke slot, on 4 mm vertical rods)</text>
  <line x1="310" y1="60" x2="310" y2="190" stroke="#333" stroke-dasharray="3,3"/>
  <line x1="420" y1="60" x2="420" y2="190" stroke="#333" stroke-dasharray="3,3"/>
  <!-- guard floor with window -->
  <line x1="200" y1="190" x2="290" y2="190" stroke="#333" stroke-width="3"/>
  <line x1="440" y1="190" x2="530" y2="190" stroke="#333" stroke-width="3"/>
  <text x="536" y="194">guard floor, open window ≥ 10 mm clear</text>
  <!-- carrier -->
  <rect x="280" y="205" width="170" height="24" rx="8" fill="#cfe" stroke="#333"/>
  <text x="458" y="222">carrier (vertical yoke slot, on 3 mm rods), smooth underside = guard</text>
  <!-- ellipse path -->
  <ellipse cx="365" cy="300" rx="40" ry="16" fill="none" stroke="#c33" stroke-width="1.5" stroke-dasharray="4,3"/>
  <path d="M330 300 L335 303" stroke="#c33" marker-end="url(#arr)"/>
  <text x="408" y="290" fill="#c33">nail path: 40 × 16 mm ellipse</text>
  <text x="408" y="304" fill="#c33">pull ~30 mm in contact, return lifted 13 mm</text>
  <!-- finger: flexure, body, pocket, blade -->
  <path d="M365 229 L365 246" stroke="#333" stroke-width="5"/>
  <text x="372" y="244">root flexure 15 × 12 × 1.2 mm (compliance, k ≈ 0.15 N/mm, 8 mm stop)</text>
  <path d="M365 246 L395 300 L402 320" stroke="#333" stroke-width="7" stroke-linecap="round" fill="none"/>
  <text x="300" y="275" text-anchor="end">finger body (PETG, widens root-ward)</text>
  <rect x="396" y="312" width="16" height="16" rx="3" transform="rotate(45 404 320)" fill="#fff" stroke="#333"/>
  <text x="418" y="326">TM1 pocket, 45°, magnet, heat-shrink collar</text>
  <path d="M402 328 L392 352" stroke="#333" stroke-width="2.5" stroke-linecap="round"/>
  <text x="396" y="368">nail blade (tip A/B), edge R 0.3–0.6 mm</text>
  <!-- stroke direction -->
  <line x1="470" y1="345" x2="400" y2="345" stroke="#333" marker-end="url(#arr)"/>
  <text x="474" y="349">stroke direction (edge leads, plate trails)</text>
  <!-- neighbor fingers hint -->
  <path d="M305 229 L305 246 L335 300" stroke="#bbb" stroke-width="5" fill="none"/>
  <path d="M425 229 L425 246 L455 300" stroke="#bbb" stroke-width="5" fill="none"/>
  <text x="200" y="254" fill="#777">3 fingers, 20 mm pitch</text>
  <!-- dimensions -->
  <line x1="150" y1="229" x2="150" y2="352" stroke="#333" stroke-width="1" marker-start="url(#arr)" marker-end="url(#arr)"/>
  <text x="96" y="295">36 mm protrusion</text>
  <line x1="570" y1="229" x2="570" y2="258" stroke="#333" stroke-width="1" marker-start="url(#arr)" marker-end="url(#arr)"/>
  <text x="576" y="248">30 mm exclusion</text>
  <text x="576" y="260">zone boundary</text>
  <!-- mount -->
  <rect x="330" y="20" width="70" height="20" fill="#eee" stroke="#333" stroke-dasharray="2,2"/>
  <text x="404" y="34">to dip stage → band ring, or wand handle</text>
  <!-- e-stop note -->
  <text x="40" y="455" fill="#333">Force path: scalp → blade → TM1 → finger → flexure (F_max = 0.3 + 0.15 × 8 = 1.5 N) → carrier → rods → lift frame → yoke → eccentric → housing → dip stage (12 mm spring-return dead-man) → band.</text>
</svg>

---

## 4. Could WR-1 beat a multi-servo design on the north star? An honest argument

**Where it should win.** The sensation model's top two carriers (A: near-root canopy sweep; B: edge-on-skin plough-and-release) are per-stroke physics: edge geometry, reach, force in the 0.3–0.9 N window, 60–180 mm/s, trailing plate, and a clean lift at both ends. WR-1 produces those by geometry, with a bell-shaped force profile and a lifted reversal that a position-controlled servo finger has to be *programmed and tuned* to approximate, and with 30 g of moving mass on 0.15 N/mm springs that a servo horn cannot match for softness. It is also quieter than three or four geared servos, and it has no firmware in its force path. If the test program finds that a single excellent stroke, repeated with modest jitter, is what the scalp wants (open questions 1–3, 6), WR-1 wins outright at one fifth of the cost and a tenth of the failure modes — and the Director's §14 question "could a radically simpler mechanism win?" is answered yes.

**Where it should lose.** Component C — pattern irregularity — is ranked #1 for adjustability (importance 5, uncertainty 5) precisely because nobody knows how fast a repeating machine stroke goes dead. WR-1 can jitter speed and pauses and borrow randomness from the user's head and hand, but it cannot vary stroke length or direction within a placement, cannot un-lock the three fingers in time, and cannot move regions by itself. If the predictability penalty acts in seconds rather than minutes, a multi-servo module with per-finger drive and a region axis will feel more "alive" even with worse per-stroke physics, and WR-1 becomes what it also is: the best fixed-stroke control instrument the program could have.

**What settles it.** One afternoon with WR-1 in wand mode on Michael's scalp — periodic versus jittered versus jittered-plus-hand-relocation, rated every 30 s — is the cheapest experiment in the whole tournament that bears on the #1 variable. The multi-servo teams need that number as much as this team does. Build order recommendation to the Director: let WR-1 be built regardless of which architecture wins, because it costs $85, takes a weekend, validates the tip family under real stroke kinematics, and measures the predictability penalty that every other design's firmware is guessing at.

**Hybrid if neither wins alone (SP2):** mount the WR-1 module on a single slow servo axis (region drift ±40 mm along a concentric rail) and replace the double eccentric with an r-adjustable slotted crank; that adds stroke-length and location variation for ~$35 while keeping the one-motor stroke engine that makes the nails behave.

---

*Team F. Scratchpad scripts used for the kinematic numbers: elliptical path with a convex scalp (r 20, e 8, dip 1–6 mm, k 0.15, preload 0.3, R 90/70/flat), and a four-bar coupler-curve search that established why a Hoeken/Chebyshev straight-line linkage cannot be used (its straight segment lies on the pivot side of the loop, so the lifted return would be on the scalp side).*
