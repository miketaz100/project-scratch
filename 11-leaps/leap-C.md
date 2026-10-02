# LEAP C: the contact element and how it moves

**Project SCRATCH · 11-leaps · Agent C · 2026-10-01**
Provocation: every design so far moves discrete nail tips on a reciprocating carrier. What if the contact is continuous or travels instead?
Tags: `[KNOWN]` from foundation docs or literature · `[EST]` my own arithmetic, shown · `[UNKNOWN]` only a test can answer it.
Firewall: no other 11-leaps file was read.

---

## 0. The assumption every design shares

From the three-nail rake (FLOAT-ARM) to the porcupine, every design ties the motion of the contact to the motion of its carrier, and the carrier reciprocates. Four consequences follow, and the program has spent most of its effort working around them:

1. **The reversal is where the danger is.** Loop and lasso formation (hair-interaction §3.4), the gating rule to lift before every reversal (H-5.2), the 50–80 ms lift latency that Red Team 1 showed cuts duty and pushes 1–3 Hz down to 1–2 Hz, and the "metronome" of a fixed-duration air return: all of these exist only because the contact turns around.
2. **Duty is at most about 50%.** A nail is either dragging or flying back. Red Team 1 measured v0 at about 1,400 hair deflections per second against a human P1 rate of 2,000–4,000.
3. **The contacts move in lock-step.** H-5.6 actually requires that elements inside the canopy move as a rigid group. That forbids by rule the thing scratch-model §4.2 calls "probably perceptually important": per-finger asynchrony (20–80 ms in P1, fully independent 3–6 Hz in P4, "the highest unpredictability; strong tingle driver").
4. **Selecting which contacts touch takes its own mechanism.** The porcupine needs a selector motor, a latch per pin and parked states, because every pin rides the same oscillating shell.

The family below breaks that tie. The carrier **circulates** (a chain or a drum) or **waves** (a crankshaft phased along a row, or a membrane). Each nail still plants, drags and lifts, but the sequence of contacts comes from geometry rather than from reversing a carrier. Two physical facts make this more than a novelty:

- **A circulating or orbiting nail never reverses while touching the scalp.** Its path through the hair is monotonic from landing to lift-off, which is exactly H-5.7's "hair-positive" pattern, delivered by construction.
- **A phase difference between neighbouring nails can be built in mechanically, and tactile apparent motion turns it into a percept.** Discrete touches with a suitable stimulus-onset asynchrony (SOA) fuse into one contact that seems to move continuously `[KNOWN: Sherrick & Rogers 1966; Kirman 1974, Percept. Psychophys. 15:1; Israr & Poupyrev, "Tactile Brush", CHI 2011, optimal SOA ≈ 0.32·d + 47 ms for duration d]`. At 20 mm pitch the nails sit inside the scalp's 15–40 mm two-point threshold (prior-art §3.3), so a phased row should read as one continuous travelling scratch, not as points. That is the "continuous contact" the provocation asks for, achieved perceptually instead of mechanically.

Four candidates follow (C1–C4), then the two ideas I folded (inchworm, magnetic drag) and my best bet.

---

## C1. RACETRACK: a circulating nail chain with a height-cam guide

**(a) Assumption broken:** contact requires a reversing carrier, and choosing which pins touch takes a selector.

**(b) Principle.** A side-flexing plastic conveyor chain (the "multiflex / side-flexing table-top" type used in bottling lines) runs in a horizontal racetrack in a plane parallel to the scalp, driven by one sprocket. A nail post hangs straight down from every link. The chain rides on a stationary guide rail whose **height profile is a cam**: the rail is low over the contact segment (posts reach the skin) and 20 mm higher everywhere else (posts are lifted). Because the loop turns about axes normal to the scalp, the posts never rotate toward the head: they stay vertical everywhere except for a gentle pitch on the ramps. The rail profile decides which nails touch, so it replaces the porcupine's selector, and a swapped rail gives a different pattern. A ≥ 120 mm stretch of chain carries no posts (the **rest gap**). Parking it over the contact segment lifts every nail with no second motor, which provides P5 pauses and makes a reversal of the drive legal.

```
 PLAN (looking down onto the scalp)                    SIDE (run A, stroke →)
   sprocket Ø40          idler Ø40                    rail height above scalp
    ╭───────── run B (lifted, return) ─────────╮        56 ┤▔▔▔╲              ╱▔▔▔ lifted, posts clear
    │  ○   ○   ○   ○   ○                       │           │    ╲ entry 30°  ╱ exit 15° ramp (75 mm long)
    │                      [ rest gap ≥120 ]   │        36 ┤     ╲________╱   contact arc, concentric with scalp
    ╰── run A: ● ● ● ● (contact segment 70) ───╯           │      |←  48 →|   (+7 mm entry, +15 mm exit tip contact)
         posts alternate ±10 mm → 2 lanes, 20 mm pitch   0 ┼─────────────────── scalp
 overall 200 × 60 mm footprint, 70 mm tall          post: 36 mm drafted stem + porcupine-style axial
 chain pitch 25.4 mm, one post per link              spring (0.02–0.05 N/mm, 0.3 N preload, stop at 0.6 N),
                                                    6 mm mini nail with a 45° trailing face
```

| Item | Value |
|---|---|
| Nail path | Lands on the entry ramp moving forward and down at about 30° (H-5.3 asks for a ≤ 30° plough-in, met), drags about 70 mm along the contact arc, lifts on the 15° exit ramp while still moving forward at v·cos15° = 0.97 v (H-5.3: lift while moving at ≥ 30% of stroke speed, met). Lift is 20 mm. |
| Velocity profile | Flat: constant chain speed through the whole contact, 20–150 mm/s, set by one motor. On the exit ramp the post pitches 15° with its tip leading, so the nail face goes from 45° to 60° (window 25–65°, met). |
| Contacts | 70 mm contact zone over 25.4 mm post pitch gives 2.75 posts touching, in alternating lanes. That is 3 most of the time and 2–4 as posts enter and leave. It drops to 0 while the rest gap passes. |
| Hair | No reversal in contact. Paths are monotonic and lift every 70 mm, so the against-grain hair wave (§2.3) collapses each pass. Chain, sprockets and rail sit at 36–60 mm, above the 30 mm exclusion plane (H-6.2 method 1). Only translating, drafted posts enter the zone. In the U-turns the posts are lifted and sweep a 20 mm-radius semicircle, like a comb tooth leaving the hair, not a spinning surface. |
| Force bound | Per-post axial spring and stop: the porcupine pin unit (pin-unit §0) reused, giving 0.3 N ±0.1 N over ±5 mm and ≤ 0.6 N at the stop (red line 2, met). Landing transients are negligible: moving mass about 0.8 g, k = 20 N/m, normal landing speed at most 0.5·v. At v = 100 mm/s the spike is v_n·√(km) ≈ 0.05 × 0.126 = 0.006 N `[EST]`, about 100× below v0's hand-tap spike, because only the nail lands, not a 60–200 g hand. |
| Coverage | One 70 × 20 mm double lane per module. A head would carry 4–6 modules aligned with the hair lie (crown→nape, crown→temples), so the default strokes run with or across the grain (H-5.1). |
| Motors | 1 per module (an N20 or a bus servo in wheel mode). The selector, latches and the 2-servo shell drive all disappear. |
| Noise | No reversal impulses. Chordal action at link rate v/p = 4 Hz is quiet with plastic chain on a UHMW wear strip `[EST]`. Gear whine is steady, not rhythmic. |
| §7 variables moved | **Rank 4, velocity:** a constant-speed contact, so the CT optimum (≈ 3 cm/s, scratch-model §2.2) can be held for a whole episode, which a crank cannot do. **Component A, follicle drive:** 2.75 contacts × 100 mm/s × 10 hairs/mm ≈ 2,750 deflections/s with no dead time, against 1,400 for v0, at the same 3-nail count. **Rank 2, reach:** the lift every 70 mm keeps nails from riding up onto a hair wave. **Rank 1, irregularity:** only weakly, through speed jitter, the gap and drive reversal. |

**(c) Why it could step-change the sensation.** It is the only architecture here that delivers a P2 long sweep (scratch-model §4.1: "luxurious", most follicles per pass) as a continuous state rather than one event followed by a return. The nearest human pattern is hand-over-hand alternating strokes. The flat velocity profile lets a slow-mode episode sit on the CT peak instead of passing through it twice per crank cycle.

**(d) Plausibility.** Side-flexing plastic chain and UHMW wear strips are standard conveyor stock. Load is 3 posts × 0.1 N of drag plus about 1 N of chain friction, about 0.03 N·m at a 20 mm sprocket. Mass is about 150 g per module, of which posts are 13 × 3.6 g (a 446 mm loop is 18 links, 5 of them left empty for the rest gap). Height is 70 mm. All posts are identical.

**(e) Cheapest experiment (about $25, one evening).** A Tamiya 70100 Track & Wheel set ($10) plus a Tamiya gearbox ($12) or a hand crank. Hot-glue 6 posts (1.2 mm brass rod, 35 mm long, with cut press-on nails) to tread links, and print a side frame with a hump in the bottom guide. Run it hand-held over the wig head first (snag count, hair-interaction §7), then the crown. A/B it against the same nails on a rigid bar dragged by hand at the same speed. The question is whether continuous procession reads as a scratch or as a comb.

**(f) Replaces / combines.** It replaces the porcupine's shell drive and selector with one motor per module. The pin unit survives unchanged as the post. On FLOAT-ARM it can replace the rake as a module on the arm, and the arm's yaw servo supplies direction and region change.

**(g) Why it might not work.** (1) **It could read as a comb or a conveyor.** Every nail in a lane follows the same line at the same speed, and landings arrive every p/v = 254 ms. That makes it periodic, and periodic stimuli habituate in 10–30 s (scratch-model §4.3). Speed jitter changes the rate but not the lane. (2) **Line dose.** A spot on the lane takes about 2 passes per second. That is acceptable inside a 5–20 s bout but needs module wander (a second motor or several modules taking turns) to stay under the 50 passes/min working rule (scratch-model 3.24). (3) **Long hair.** Hair over about 8 cm reaches the chain, the same caveat every design carries.

---

## C2. METACHRONAL RAKE: one crankshaft, a travelling wave of nails

**(a) Assumption broken:** contacts move as a rigid group (H-5.6), and asynchrony has to be added as jitter.

**(b) Principle.** Four nails sit side by side at 20 mm pitch, like a hand, and all stroke in the same direction. Each nail rides its own throw on one crankshaft, so each traces its own closed path: plant, drag 30 mm, lift 13 mm, return in the air. The throws are clocked 90° apart. A wave of contacts therefore runs across the row: nail 1 lands, then nail 2 one quarter-cycle later, and so on, like millipede legs or a ciliary carpet (a metachronal wave). It is Team F's WR-1 "walking rake" with its eccentrics re-clocked, and one of the two lawful descendants of the nail wheel (see C4).

```
 FRONT (row of 4, crankshaft along the row)           SIDE (one nail, stroke →)
  crankshaft Ø6, throws e = 15 mm, clocked 0/90/180/270°    shaft axis, 62 mm above scalp
  ═══╤═══════╤═══════╤═══════╤═══ (sealed housing ≥ 35 mm)   ┌───────────┐ scotch yoke (WR-1)
     │ 0°    │ 90°   │ 180°  │ 270°                          │  ↺ e=15   │ tip path: flat ellipse
   boot    boot    boot    boot   TPU bellows (Ø30, ±16 mm)  └─────┬─────┘ 30 mm × 13 mm
     ┃       ┃       ┃       ┃    drafted stems, sprung tips       ┃
     ▼               ▼            ← nails 1 and 3 in contact   ╭───╯╮  lift 13 ╭╮
  ───●───────────────●──────── scalp (2 of 4 touching)         ●═══════drag 30══●  ← one way, then up
     |←20→|←20→|←20→|  row 60 mm, swath 80 × 30 mm         land          lift
```

| Item | Value |
|---|---|
| Nail path | WR-1 flat ellipse, 30 mm drag and 13 mm lift. Every nail lifts before its own reversal (H-5.2, met by geometry). A Hoeckens four-bar (7 mm crank) gives a flatter 31 mm run but only about 6 mm of lift `[EST, my simulation]`, so start from WR-1. |
| Velocity profile | Sinusoidal on the yoke: peak X·ω = 15 mm × 12.6 rad/s = 190 mm/s at 2 Hz, about 120 mm/s mean in contact. |
| Contacts | About 50% duty per nail, so with 4 nails at 90° exactly 2 are always touching. The scratch never stops, yet each nail lifts once per cycle. |
| Phase / SOA | The SOA between neighbours is Δφ/(360°·f) = 125 ms at 2 Hz, and contact duration is about 250 ms. Tactile Brush's optimum for d = 250 ms is 0.32 × 250 + 47 = 127 ms. **A 90° clock is close to the apparent-motion optimum.** Because SOA and d scale together with motor speed, the ratio stays at 0.5 against optima of 0.41–0.60 across 1–3 Hz. The wave crosses the 60 mm row at 160 mm/s. |
| Hair | Lateral spacing is fixed at 20 mm, so no gap ever closes (the scissoring of §3.8 is impossible). Nails touching at the same moment move the same way. Over their 90° overlap their fore-aft offset swings 15→21→15 mm, so a hair draped across both sees its 25–29 mm diagonal span change by 4 mm. It slides off the smooth faces and nothing clamps it `[EST]`. The crankshaft sits above the 30 mm plane in a sealed housing. Each stem passes the guard through a TPU bellows that only orbits within ±16 mm, so a boot is possible here, which Team F showed it is not on a continuous hub. |
| Force bound | Per-nail spring and stop (pin unit, or Team C's leaf), cap ≤ 0.6 N (red line 2, met). |
| Coverage | One hand-sized 80 × 30 mm patch, 24 cm². |
| Motors | 1. Reversing the motor reverses both the drag direction and the wave direction, which gives two percepts from one motor. Reverse only when no nail is touching (see (g)). |
| Noise | One steady gearmotor. Torque ripple at the landing rate N·f = 8 Hz, small. No reversal clunk. |
| §7 variables moved | **Rank 6, contact count and asynchrony:** moved from 0 ms (rigid) to a structural 125 ms ladder, the P4 regime. **Component C, "alive":** a moving contact that is perceived as larger than the hardware. **Rank 1, irregularity:** partly, through wave-direction flips and speed jitter. Follicle drive is 4 × 30 mm × 2 Hz × 10 = 2,400/s, the same as a rigid 4-nail rake. The gain is temporal structure, not hair count. |

**(c) Why it could step-change the sensation.** Red Team 1's central finding was that a rigid carrier with a fixed stagger reads as "a tool with three points" (P ≈ 0.6), because three contacts at 20 mm are barely resolved on the scalp and the "hand" percept must come from the pattern across them. The metachronal row turns that weakness into the mechanism. Below two-point acuity, a correctly timed sequence fuses into one moving scratch, which reads as a hand moving, not as points. Its phase relationship is also the one property that P4 (the "spider", ranked as the strongest tingle driver) has and no rigid rake can have.

**(d) Plausibility.** The 4-throw crankshaft is printed or made from a 6 mm rod with clamped eccentric hubs. WR-1 already showed one N20 driving yokes on one shaft. Torque: 2 contacts × 0.1 N drag × 15 mm = 3 mN·m plus yoke friction, trivial for an N20 at 100:1. Mass about 150 g. Housing 62 mm tall. Re-clocking the hubs (0°, 30°, 90°, 180°) is a 2-minute screwdriver job, which makes phase an experimental variable.

**(e) Cheapest experiment (about $15, one evening, no new mechanics).** Emulate the wave in firmware. Four SG90 servos, each swinging one TM1 nail on a 30 mm horn with a cam-ramp lift, phased by an Arduino. Rate phase 0° (the rigid control), 30°, 90° and 180° blind in random order on the crown. Ask two questions: "one moving thing or separate points?" and "how much like fingers, 0–10?". If 90° beats 0° clearly, print the crankshaft (about $20, one weekend).

**(f) Replaces / combines.** It replaces FLOAT-ARM's rigid 3-nail rake as the hand on the existing arm, which keeps the arm's dead-weight float, yaw and region change. On the porcupine it replaces the 2-servo inner shell and the selector for a sector: the phase itself chooses which 2 nails touch at any instant.

**(g) Why it might not work.** (1) **Formication.** A wave of small touches running across the scalp is also the signature of "something crawling in my hair", which is aversive. Slow waves at low force are the riskiest; this is the first thing the SG90 test must answer. (2) **The wave is deterministic and could be learned in 10–30 s.** Mitigations: speed jitter, direction flips, and a phase-shifter (a second motor driving a differential on half the shaft) if needed. (3) **No rest phase at 90°.** Two nails always touch, so a pause or a legal reversal needs the whole-hand lift that FLOAT-ARM already has. Alternatively, clock the throws at 30° (all four lift together over a 90° window), at some cost to apparent motion. (4) **Yoke drag speed is sinusoidal.** A nail landing at zero speed overlaps one at peak, so neighbours differ by up to X·ω ≈ 190 mm/s. A flat-run linkage would fix this but needs more lift than my Hoeckens check gave.

---

## C3. PERISTALTIC SKIN: a travelling-wave membrane with moulded nails

**(a) Assumption broken:** the hair guard and the moving element are separate parts with a seam between them. That seam is where every gap, slot, wiper and boot rule lives.

**(b) Principle.** The underside of the module is one continuous silicone/TPU sheet, 1.5 mm thick, with nail posts moulded into it. Above the sheet, eight spring-loaded followers on a helical camshaft press the sheet down in sequence, as in a linear peristaltic infusion pump. A transverse wave runs along the sheet. **The sheet does not slide, the wave moves.** A post of length h below the sheet tilts with the local slope, so its tip moves sideways by h·∂w/∂x. The tip therefore traces an ellipse, as a stator point on a travelling-wave ultrasonic motor does (Sashida; Canon USM), and at the trough it moves *against* the wave. Each nail plants, drags and lifts in place; only the zone of contact travels.

```
 SIDE (wave travels →, nails drag ←)          λ = 100 mm, A = ±6 mm, followers at 12.5 mm (45° steps)
  helical camshaft ═◎══◎══◎══◎══◎══◎══◎══◎═    (sealed above, ≥ 40 mm)
     followers      ┃  ┃  ┃  ┃  ┃  ┃  ┃  ┃     each through a spring (force cap)
  sheet  ╲____╱‾‾‾‾╲____╱‾‾‾‾╲            sheet mid-plane 40 mm above scalp, ±6 mm
          ╲  ╱      ╲  ╱                  posts h = 40 mm moulded in, 25 mm pitch; 3 lanes, 20 mm apart, staggered 8 mm
  scalp ───●──────────●───────  tip: ellipse ±6 mm vertical × ±15 mm horizontal; contact ±60° of phase
           ← drag 26 mm at each trough
```

| Item | Value `[EST]` |
|---|---|
| Nail path | Vertical motion is ±A = ±6 mm. Horizontal semi-axis is h·k·A = 40 × 0.063 × 6 = 15 mm. With 3 mm interference, contact covers ±60° of phase, giving a 26 mm drag and lift at both ends while the tip is still moving horizontally (H-5.3 met). |
| Velocity profile | v = h·k·A·ω·cos θ: 95–190 mm/s at 2 Hz, about 157 mm/s mean in contact. |
| Attack angle | Slope × drag couples: the post rocks ±19° during contact, so a 45° face spans 26–64° (window 25–65°, just met). That rocking is a bounded rotation of less than one turn (H-6.2 method 2). |
| Contacts | 4 posts per wavelength per lane, touching 1/3 of the time, so 1.33 per lane and about 4 in total across 3 lanes. The 8 mm stagger between lanes spreads lane phase by 29°. |
| Hair | **The best story in the program.** The hair sees one smooth, undulating, closed skin with drafted posts bonded into it. No slot, gap, seam, boot, wiper or rotating part exists below 34 mm. Every hair-checklist gating item scores 2 by construction. |
| Force bound | The followers are spring-loaded against the cam with a stop (as linear peristaltic pump fingers are), and the post compliance adds in series. Force is capped mechanically but couples across about one follower pitch, so independence per nail is partial. |
| Motors | 1. Reversing the motor reverses the wave and the drag. |
| Noise | Followers on the cam, close to a peristaltic pump. The sheet itself is silent. |
| §7 variables moved | Same asynchrony and apparent-motion gain as C2, along the drag axis instead of across it. **Follicle drive** about 3 × 1.33 × 157 mm/s × 10 ≈ 6,300/s, the highest here. **Rank 2, reach:** 26 mm drags with lift. |

**(c) Why it could step-change the sensation.** The contact zone sweeps forward at c = λf = 200 mm/s while each nail scratches backward at about 160 mm/s. A hand cannot do that, but each half has a sensory argument: local plough-and-release (component B) and a large moving envelope (component A). The bigger step-change is indirect. It removes the hair-safety tax (seals, boots, guards, breakaways) that has driven mass in every design, and that budget can go to coverage.

**(d) Plausibility.** Arc-length excess of the wave is (kA)²/4 ≈ 3.6%, which a silicone sheet takes easily, or the sheet edges can float in a stationary groove at 40 mm. Fatigue: 7,200 cycles per hour, within what silicone sheet tolerates. Mass about 180 g. Moulding silicone with embedded posts is a new skill for Michael: Smooth-On Dragon Skin and a printed tray mould.

**(e) Cheapest experiment (about $45, one weekend).** Print a helical camshaft with 8 followers (open "linear peristaltic pump" designs exist). Pour a 1.5 mm Dragon Skin sheet with 4 brass posts and nails. Crank it by hand over a grid and film at 240 fps: does the tip trace the predicted 26 mm contact arc of the 30 × 12 mm ellipse? Then run the wig-head snag test.

**(f) Replaces / combines.** C3 is the hair-sealed production form of C2 (C2 with its boots merged into one skin). On a helmet, 4–6 skins replace the porcupine's inner shell, pins, wipers and selector.

**(g) Why it might not work.** (1) Drag length and attack-angle swing are locked together (rocking = D/2h). Longer drags mean taller posts or larger angle swing. (2) Force comes from wave amplitude plus springs, so force and stroke are coupled and a smaller wave means a weaker scratch. (3) The moulding toolchain is outside the two-toolchain budget. (4) The same formication risk as C2.

---

## C4. WALKING DRUM: Team F's nail wheel, re-examined

**(a) Assumption broken:** scratching and region change are separate motions, and the nail wheel is unlawful.

**Re-examining Team F (02-mechanisms/team-F.md, F3).** Team F gave three reasons to reject the wheel:

1. **Attack angle inverts within one contact arc.** This dies to a 1:1 planetary (fixed sun, idler, equal planet): every nail *hanger* translates without rotating, as a Ferris-wheel gondola or a paternoster car does. The attack angle stays constant at 45°.
2. **A shroud slot is an open sliding gap.** This dies only if the shroud is dropped. Put the drum, its planets and its spokes above the 30 mm exclusion plane (H-6.2 method 1), and hang long hangers down into the hair. Hangers only translate, so nothing rotates in the hair zone.
3. **No pause.** This dies to a phase gap. With 3 hangers at 120° and a 66° contact arc each (198° in total), 162° of drum angle exist at which no hanger touches. Park there.

So the lawful nail wheel exists. With a **fixed axle** it reduces to something already covered: either a single-lane procession on a circular path (C1 with a round track, which needs a cantilevered axle so the hangers' plane contains no hub) or one hanger per lane with phased throws (C2). The new thing appears only when the drum **rolls**.

**(b) Principle.** A pinion of pitch radius a rolls on top of two side racks that follow the head at 51 mm, outboard of the nail lanes. Hanger pivots sit at radius b > a, so each pivot traces a *prolate trochoid*: near the bottom of its loop it moves **backward** relative to the scalp at V·(b/a·cos θ − 1). The nail plants, drags backward, lifts and swings forward, while the whole unit walks forward at V. A true no-slip contact at the nail would be a press-walk, a massage that fails §8 item 4. **The scratch is exactly the slip b/a − 1.**

```
 SIDE (unit walks →, nails drag ←)
                  pinion a = 6 ◎ hub at 57 mm, rolling on side racks at 51 mm (outboard of lanes)      pivots on b = 25 (3 at 120°), planetary keeps hangers vertical
             ╭────────┼────────╮
             ●        │        ●  pivot circle (lowest 32 mm: stays above the 30 mm plane)
             ┃ hanger s = 36   ┃
             ▼                 ▼  tip loop: drag 20 mm backward, then rise to 46 mm
  scalp ─────────●═══════●──────────  successive plants advance 2πa/3 = 12.6 mm
```

| Item | Value `[EST, trochoid arithmetic]` |
|---|---|
| Nail path | Tip height = 21 − 25·cos θ, giving 4 mm interference at the bottom. Contact while θ ≤ 33°. Drag = 2·|aθ − b·sin θ| = 2·|3.5 − 13.6| = 20 mm. Then the tip rises up to 46 mm on the forward swing. Plants advance 12.6 mm each, so every spot is scratched about 1.6 times per pass and **then left**. Hangers ride an outboard plane on a cantilevered axle and clear each other by ≥ 7 mm. The planetary's fixed sun is tied to the carriage, so hangers stay normal to the arch, which means radial to the head. |
| Velocity profile | Drag speed is 2.5–3.2 V. For 100 mm/s drag, the unit walks at V ≈ 35 mm/s and crosses a 150 mm region in about 4 s. |
| Hair / force | Hangers only translate. Paths are monotonic and lift while still moving. Pivots stay above 32 mm. Sprung hangers with stops. |
| Coverage / motors | One motor drives scratch **and** traverse along the arch, giving a P6-style adjacency progression and H-5.7's "slow raster" for free. 3 lanes on one axle, clocked 40° apart. |
| §7 variables moved | **Ranks 13 and 14, region and dwell:** wander is built into the geometry. **Abrasion dose** (3.24) becomes a geometric constant (about 1.6 passes per spot per traverse) instead of a firmware limit. **Rank 1, irregularity:** location never repeats within a pass. |

**(c)–(g), compressed.** (c) Habituation is driven by repetition at one spot (scratch-model §4.3); a walking scratch never repeats a spot. (d) Plausible: one N20, a 1:1 planetary, and a rack on FLOAT-ARM's yoke or a helmet arch. (e) The 5-minute version: tape a pen to a hanger and roll the drum along a ruler to draw the loop. Then a $20 printed rack. (f) It adds wander to C2. On a frame it fits FLOAT-ARM's yoke-arc idea (Team D). (g) Drag is only about 20 mm. It cannot scratch in place except by walking back and forth, parking on the gap at each turn. It needs a rail over the head. Below about 10 mm/s walking speed the drag becomes too slow for anything but the CT range.

---

## Also considered and folded

- **Inchworm / caterpillar finger.** To crawl, it needs an anchor. On the scalp that anchor means gripping hair or pressing skin, which is exactly the hazard (hair-interaction §3.9, anchored strands). Anchored on a rail instead, it becomes C4 with a worse gait. Folded into C4.
- **Magnetically dragged tips under a thin shell.** One motor turning a helical magnet array (a "magnetic lead screw") could carry Team B's W-1 pucks around a racetrack on a sealed keel. Coupling suffices: an N52 6×3 pair at a 3 mm gap gives about 2 N normal and 0.5–1 N shear against 0.1–0.3 N of drag `[EST]`. Team B's own objection stands, though: a puck sliding on the shell presses any hair under it with about 2 N, an anchored-strand trap. C3 seals the shell with nothing sliding on the hair side. Parked.

---

## Comparison

| | C1 Racetrack | C2 Metachronal | C3 Peristaltic skin | C4 Walking drum |
|---|---|---|---|---|
| Reversal in contact | never | never | never | never |
| Contacts at once | 2–4 (0 at gap) | 2 constant | ≈ 4 | 1–3 |
| Asynchrony | lane stagger, periodic | **structural, 125 ms, apparent-motion optimum** | structural, along the drag axis | 40° lane clock |
| Follicle drive /s | 2,750 | 2,400 | **6,300** | ≈ 1,700 |
| Hair checklist | good (all rotation above 30 mm) | good (bellows) | **perfect by construction** | good |
| Motors | 1 | 1 | 1 | 1, including traverse |
| Cheapest test | $25, evening | **$15, evening, firmware only** | $45, weekend | $0 pen test, then $20 |
| Main risk | comb / conveyor reading | formication, learnable wave | moulding; drag tied to angle | short drag; needs rail |

---

## Best bet: C2, the metachronal rake (with C3 as its sealed form)

The program's deepest unresolved sensory problem is that a machine with several nails reads as "a tool with points" and not "a hand". Red Team 1 gave that P ≈ 0.6 and traced it to the contacts being locked together. The hair rules made the locking mandatory (H-5.6), so every design since has added asynchrony back as jitter on a rigid carrier: a fixed stagger the nervous system learns within a few strokes. The metachronal rake removes the conflict instead of patching it. Each nail plants, drags and lifts on its own phase from one shaft. No nail ever reverses while touching. Lateral spacing never closes, so the clamping hazard behind H-5.6 cannot occur. Two nails are always in contact, so the scratch has no dead time. The 90° clock lands on the published apparent-motion optimum (SOA ≈ 0.32·d + 47 ms) across the whole 1–3 Hz scratch band, because SOA and contact time scale together with motor speed. That lets four nails at 20 mm, below the scalp's two-point acuity, be perceived as one continuous scratch travelling across the head. It is the "continuous contact" the provocation asked for, delivered by the nervous system rather than by a belt. It is also the least expensive to falsify: four SG90s and an evening, rating 0° against 90° phase, answers the core question before any mechanism is printed. If the answer is yes, the build is WR-1 with re-clocked hubs on FLOAT-ARM's existing arm. The path to a full helmet is C3: the same wave carried by one sealed silicone skin, the only architecture in which every gating hair rule is met by construction. The honest risk is formication: a wave that reads as an insect instead of a hand. That is exactly what the first evening will show.

### Prior art leaned on
Tactile apparent motion: Sherrick & Rogers 1966; Kirman 1974; Israr & Poupyrev, CHI 2011 (Tactile Brush SOA rule). Metachronal waves: millipede gaits and ciliary carpets. Linear peristaltic "finger" infusion pumps (helical camshaft with sprung fingers). Travelling-wave ultrasonic motors (Sashida 1982; Canon EF USM): elliptical surface-point motion. Side-flexing "multiflex" plastic conveyor chain and UHMW wear strips. Tamiya 70100 track set (experiment). Paternoster and Ferris-wheel 1:1 planetary leveling. Prolate trochoid and Chebyshev's plantigrade walking machine. Robot-vacuum brushroll wrap (hair-interaction §3.1) is the reason every rotating part here sits above the 30 mm plane. WR-1 (Team F), the porcupine pin unit (10-porcupine/pin-unit.md), FLOAT-ARM (03-tournament/DECISION.md).
