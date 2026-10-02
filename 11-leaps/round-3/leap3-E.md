# LEAP 3-E — The skeptic of the helmet version, who proposes leaps

**Project SCRATCH · 11-leaps/round-3 · Agent E · 2026-10-02**
Provocation: find the biggest hidden flaws specific to putting the air-pin travelling pad, with a circle-and-line drive, on a helmet. Quantify each, and propose the leap that removes it.
Read: LEAP3-BRIEF; leap2-A (§0–L2), leap2-B (all, esp. L4), leap2-C (§0, C1, §5), leap2-D (grep for travel and sweeps), leap2-E (all), leap2-F (all); safety-requirements §1, §2, §7; hair-interaction §1, §3, §5–6; scratch-model §3, §5, §7; concept-A §1.4–7; redteam-2-mechanical (all); judge-2 §0. Firewall kept: no other round-3 file was read.
Tags: `[KNOWN]` sourced in those files · `[EST]` computed here (script in the session scratchpad; arithmetic shown) · `[UNKNOWN]` only a bench or Michael's head can answer it.

---

## 0. Verdict in five sentences

The helmet does not fail on force: P × A pins ignore seating, and every torque sits below a snug suspension's hold. It fails on **what the wearer feels besides the nails**:
- gears and pin stops ring through the band into the skull, 10–50 dB above the bone-conduction threshold;
- a 130 g pad wandering 150 mm from the head centre leans the hat by 0.19 N·m;
- every scrub reaction comes back as shear at the forehead, because the pads are soft so that they isolate noise;
- the hat line sits on the occipital bun, so the most valuable region is where the helmet holds itself.

Three numbers break the current paper architecture outright:
- **525 g** head-borne with a 16-pin synthesiser pad (red line 10 is 500 g);
- **0.19 J** of free fall if the travel motors lose power with the pad at the side, about 4× the 50 mJ kinetic-energy limit;
- **~1,060 hairs** under every hovering tip's 15 mm circle, so circle mode with hover-and-bite still winds hair.

The leaps take every motor, valve and gear off the head, move the hold below the bun, make circles leave the hair once per revolution, and make "free" the failure state.

---

## 1. Flaw ledger

Severity S1–S4 follows hair-interaction §3. Likelihood is per session, before the leap.

| # | Flaw (helmet-specific) | The number that matters | Sev. | Likelihood | Leap | Cheapest test |
|---|---|---|---|---|---|---|
| 1 | **Helmet rotates or creeps** under scrub, travel and umbilical loads | Static bias 0.19 (CoM) + 0.03 (umbilical) N·m, plus ±0.04–0.16 N·m of scrub at 1–2 Hz, gives a **0.38 N·m peak against a 0.44–0.61 N·m friction hold** (µ 0.27, ΣN 18–25 N). Margin 1.2–1.6, with an oscillation on top of a bias, which is the recipe for ratcheting creep. Creep moves the travel fence relative to the face. | S2 (S4 if the fence reaches the face) | 0.4 | **E2** form-locked cradle (pitch hold ~1–1.5 N·m, by geometry not µ) | $15 bike helmet + 130 g coin bag moved front/back every 10 s; a helper pushes 1 N at 1.5 Hz with a spring scale; ink line on the forehead, read creep after 20 min |
| 2 | **Chin strap**: jaw motion, comfort, breakaway | Concept-A's 0.1 N/mm elastic gets 5 mm when talking (2 N per side), but **40 mm on a yawn or a popcorn bite (5.5 N per side)**. The 12 N fuse never sees a snag, because the helmet slips first (4.9–6.8 N). | S1 | 0.8 (nuisance) | **E2**: no chin strap; the sub-occipital cradle retains | 20 min of TV in a bike helmet with and without the strap: chew, yawn, shake ×10, tilt 30° |
| 3 | **Temples, nape and bun versus the band**; ears and eyes (red line 6) | A level hat band sits on the bun and 10–20 mm above the helix. The 76 mm pad cannot enter the 10–20 mm temple strip under it. Reach is **~50–55 % of ~575 cm²**, with the bun (§5's "sweet spot") under the band. In return, **the band is a fixed guard between pad and eyes and ears**: red line 6 holds by construction until windows are cut to reach temple or nape. | S2 (lost value); S4 if windows are cut | certain | **E2** tilted band frees the bun and keeps the band as the fence. Temples and nape stay out of scope (§5 already says "later"). | Eyeliner the band line; roll a 76 mm cardboard disc over the head and shade where the pins reach |
| 4 | **Umbilical tugging the helmet** | 12–16 tubes = 55–70 g/m. A 0.6 m hanging share pulls 0.32 N (0.03 N·m), which is harmless. The hidden case is a snag: the user leans back on the bundle or stands up. A 12–18 N face-seal plug (leap2-E L3) puts **1.5 N·m** on the helmet before it releases, 2.5–3.5× the hold, **so the helmet rotates before the fuse opens.** | S2 | 0.5 for a snag, at least once a week | **E4** overhead hanger with a 3 N clip. The un-strapped helmet (~10 N lift-off) is the last fuse. | 14 aquarium tubes, 1.5 m, from the helmet to (a) a collar clip and (b) a $15 CPAP hose hanger; luggage scale at the helmet; head turns ±70°, lean back |
| 5 | **Mass and neck fatigue** | Leap2-E's 455 g ledger, with its 55 g passive pad replaced by the Director's 16-pin synthesiser pad (~125 g), comes to **525 g; 8 pins gives 485 g** (judge-2 F3 says hard-hat ledgers run low). The added flexion moment at 20° is 0.35 N·m. Separately, **you cannot lean back**: the pad works the bun. | S2 | 0.6 | **E1** (~300 g, flexion moment 0.20 N·m); posture is open (§4) | Coins to 300 g and to 500 g in a hard hat, 20 min each, neck rated at 5/10/20 min; blind "where is the 130 g bag?" test for CoM wander |
| 6 | **Circle mode winds hair** (leap2-F F2) | Hover-and-bite keeps tips 5 mm deep in a 10–25 mm pile. Each tip's r 15 circle encloses **707 mm², ~1,060 shafts**, once per revolution and cumulatively. A strand gets a capstan gain of ×4.8 per turn and **×111 after three turns** (µ 0.25). **Line mode with hover is fine**: net winding per cycle is zero, and hover is at zero force (H-5.2's "≥ 5 mm at zero force" clause). | S3 | 0.1 at ≤ 5 cm hair; 0.45 at 5–8 cm | **E3** exit-per-revolution circles on a still dome | $15 Kanekalon wig at 6–8 cm; a hand-orbited three-pen plate, hover-circle against park-between-bites, 5 min each; count twists, measure comb-out force |
| 7 | **Bone-conducted noise** | An N20's first-stage mesh force of 0.04–0.17 N, with 10 % ripple at ~1.5 kHz, is **4–17 mN against a bone-conduction threshold of ~0.1 mN at 1 kHz and ~36 µN at 2 kHz** (ISO 389-3 mastoid RETFL, `[KNOWN, from memory; verify]`). That is 30–50 dB above threshold before the band, and 10–30 dB after it. Vacuum-parked pins hitting top stops at 0.4–0.6 m/s add a click per park. | S1 (decisive for the "machine" reading) | 0.7 | **E1**: nothing on the head turns or ticks; soft top stops | N20 taped to a bike helmet, earplugs in (bone path only): audible? Phone accelerometer under the band |
| 8a | **Valve stuck open** | Loaded circles at 60–120/min, or a loaded pin dragged by 2–8 cm/s travel (H-5.8) | S3 | low per hour | Per-pin bleed + rail dump on mismatch (leap2-F §4), plus E4 radial lift | Fault-inject on the wig |
| 8b | **Pad stalled at a temple** | 0.39 N where §5 says ≤ 0.15 N; the orbit keeps scrubbing one patch (H-5.5) | S2 | low | N/A in the minimum helmet (midline only); geographic relief ramp for the two-axis version | — |
| 8c | **Power loss mid-travel** | Back-drivable gimbal travel with 105–130 g at r 150 swings free: **0.155–0.19 J, 1.7 m/s at the stop**, against the 50 mJ limit. Shorting the phases gives ~6 × 10⁻⁴ N·m·s/rad, **useless as a brake**. With the head pitched forward, the pad falls toward the front fence. | S3 | 0.3 over the programme | **E1** hydrostatic travel holds position unpowered | Dummy 130 g pad on a hinged arc: cut power at 60° and film at 240 fps |
| 8d | **Tube kink** | A pinned pin traps 10 kPa while travel drags it | S3 | 0.2 with a nape exit (lying back) | E4 overhead exit + per-pin bleed | Pinch the line on the bench, time the decay |
| 8e | **Helmet knocked** | A two-axis bail is a 330 mm halo. A 5–7 N push at r 165 (0.8–1.2 N·m) turns the whole helmet; the pad goes with it, the band-fence goes with it. | S1–S2 | 0.3 | E2 (the fence moves with the helmet) + slim sagittal arc in the minimum helmet | Bump the coin-loaded helmet on a door frame |
| 9 | **Doffing with a pad in the hair** | After power loss the pins are limp (0.05 N), not parked, and the user tilts the hat off: tips drag tangentially through the pile, and a strand looped on a 0.38 mm neck is H-3.4's lasso | S3 | 0.15 | **E4** spring radial lift on any vent (50 mm in ~90 ms) | Three pens pressed into the wig on a dummy pad; doff eyes-closed one-handed ×10, with and without the lift |

**Not flaws, on inspection:** orbit inertia (0.04–0.31 N, under the drag); travel acceleration (0.013 N·m); hair anchored under a static band or cradle (a strand under 20 mm of foam at 5 kPa pulls out at ~10 mN, below the 0.05 N tug threshold); red line 6 at the ears (the band is the guard while nothing reaches under it).

---

## 2. The leaps

### E1 — THE PUPPET HELMET: nothing on the head is powered, geared or switched

**(a) Assumption broken.** "The synthesiser lives on the pad and the travel motors on the arcs." Every head-borne noise source (§1 row 7), half the mass (row 5) and the free-fall fault (8c) come from that one assumption.

**(b) Principle.** Keep the Director's two-crank synthesiser, at the desk. It drives a **master plate** carrying three bellows at 120° (leap2-C C1's slave geometry, mirrored). Three sealed air lines go to an identical **slave plate** on the pad.

Why the slave copies any planar path: for a displacement d, bellows k changes volume by A·(d·n_k), and Σn_k = 0. So the master's three volume signals reproduce **any** planar path at the slave: circle, line, precessing line or heading jump. No air is consumed. Leap2-C's three-throw crank could only make a circle; a master plate driven by the synthesiser makes everything in leap2-B's L4 table.

Travel uses a **hydrostatic pair**:
- a desk stepper on a lead screw drives two water-filled rolling-diaphragm cylinders (Whitney's rolling-diaphragm transmission, Disney Research 2016, `[KNOWN, recall]`);
- these turn a pulley at the rear of the arc, which pulls a closed Dyneema loop inside the arc channel;
- the loop moves the carriage.

```
 DESK (foam box)                                        HEAD (plastic, air, water; no wires)
 N20a ─ecc─┐                                             slave plate (3 bellows @120°, flexure legs)
 N20b ─Oldham─ecc─► MASTER PLATE ═3 sealed air lines═══►  └ ball-slides ─► pins tilt through STILL DOME (E3)
 stepper─lead screw─► ⊂⊃⊂⊃ rolling diaphragms ═2 water lines═► pulley ─ Dyneema loop in arc ─► carriage
 8 × S070 valves + sensors ════════════ 8 pin lines ══════════► pins (P×A, relief 40 kPa, bleed)
 1 valve ═══════════════════════════════ radial line ═════════► radial piston + palm skids (E4)
                 14 tubes ≈ 11–13 mm bundle, exits up-back to a hanger (E4)
```

**(c) Variables moved.**
- *Sound (§7 rank 15):* from 10–30 dB above the bone-conduction threshold to nail hiss and bellows.
- *Mass (rows 5, 8c):* 485–525 g down to **~300 g**.
- *Reaction feel (row 1):* with no noise source on the head, the band no longer needs soft isolator blocks. A **stiff, full-perimeter band** becomes possible: 142 cm² of 3 mm closed-cell foam at G ≈ 75 kPa is ~350 N/mm in shear, so 1 N of scrub moves the forehead **~3 µm instead of concept-A's ~250 µm** (four blocks at ~1 N/mm each). That is below the tens-of-µm low-frequency touch threshold `[EST]`, though the forehead skin's own shear compliance may add some of the motion back.

**(d) Plausibility** `[EST]`:
- *Synchro stiffness:* 1.4–2 N/mm per line (leap2-C), so 0.5–1.7 N of drag costs 0.3–1 mm of a 15 mm radius. Line mode becomes a thin ellipse ≤ 1 mm wide, which leap2-B calls harmless.
- *Slave dynamics:* 60 g on 2–3 N/mm resonates at ~30 Hz, far above 1–2 Hz.
- *Hydrostatic stiffness:* 0.2 N·m of gravity torque on a 15 mm pulley needs 13 N, which is 42 kPa on a Ø20 diaphragm. A 1.5 m PU line swells 0.03 ml under it, which is **0.1 mm of piston and 0.4° of pulley**.
- *Unpowered:* the lead screw holds, so **the 0.19 J fall cannot happen**. A runaway stepper puts 2.6 mJ into the carriage (0.13 kg at 0.2 m/s), and a relief valve in the water circuit caps the cable tension.
- *Drift:* the compensating port only re-zeroes on paths that reach each master's extreme. A capillary bleed to p₀ (τ ≫ 1 s) or a homing circle every ~60 s handles line mode.
- *Cost:* ~$60 over the bench parts.

**(e) Cheapest experiment (~$30, a weekend).**
1. Three Ø20–25 suction-cup bellows on a flexure plate, connected by 1.2 m lines to a hand-driven master plate with three more. Draw a circle, a line and a precessing line on paper with the master; the slave carries a pen.
2. Two 10 ml syringes joined by 1.5 m of water-filled tube turning a pulley (syringe stiction is accepted; rolling diaphragms come later).

Pass: slave-to-master path error ≤ 1 mm at 1.5 Hz, and the pulley holds within 1° under a 0.2 N·m hanging weight.

**(f) Replaces / combines.** Replaces the on-pad N20s, encoders, Oldham coupling, gimbal travel motors, motor cables and every on-head connector. Combines with E2–E4. The synthesiser gains room at the desk: bigger bearings, an encoder per crank.

**(g) Why it might fail.**
Fourteen tubes are a stiffer bundle than 9; bellows fatigue at ~11,000 cycles per session `[UNKNOWN]`; master–slave mismatch drifts with temperature; a water leak (S1) ends the session.

---

### E2 — THE BUN-FREE FIT: forehead band plus a sub-occipital cradle; no chin strap; the band is the fence

**(a) Assumption broken.** "A helmet holds by friction at the hat line and needs a chin strap." The hat line is where the bun is, and friction is the weakest kind of hold (§1 row 1).

**(b) Principle.** Use a bicycle-helmet fit system:
- a stiff, full-perimeter forehead band at brow + 30 mm, running back level over the ears (10–20 mm above the helix);
- a **dial-tightened cradle under the occipital shelf**, below the inion, on the suboccipital nape.

The ring is tilted ~20–30° (front high, back low), so the whole bun sits **inside** the ring, free. The cradle hooks under the bun's overhang, so the helmet can tip forward or lift only by riding the cradle up over the bun. That is a form lock, not friction.

```
 SIDE VIEW                       pad envelope (crown → top → BUN), all above the ring
            .-~~~~~~~~-.   sagittal arc R≈165 about O, from forehead band to cradle
          /   ▼▼▼ pad    \
  forehead|band  ●O        )  bun free (inside the ring)
  brow+30 ╲______        _╱
          ears ⊂⊃  ╲_____╱◄ dial cradle under the occipital shelf (form lock, ~10 N to override)
```

**(c) Variables moved.**
- *Region (rank 13):* the bun moves from "under the band" to reachable. Midline pin reach runs from hairline + 20 mm to the lower bun, about 240 mm of arc × 84 mm of swept width, **~200 cm², ~35 % of the scalp** on one axis.
- *Comfort and jaw (row 2):* no chin strap. Yawning and chewing load nothing.
- *Safety (row 3):* a continuous ring between the pad envelope and the eyes and ears makes red line 6 structural. Creep (row 1) moves the fence *with* the pad.
- *Doffing (row 9):* tilt back and up by the front band, and the cradle slides off the nape, in 1–2 s. The form lock (~10 N) doubles as the breakaway that red line 10 asks of a strap.

**(d) Plausibility** `[EST]`:
- *Pitch hold:* override needs the cradle arms (~1 N/mm) to ride a ~10 mm overhang, ~10 N at 0.1–0.15 m, so **~1–1.5 N·m against 0.38 N·m of peak demand**, a margin of 3–4 independent of sweat.
- *Yaw:* still friction, 0.27 × 25 N × 0.085 m ≈ 0.57 N·m against ~0.1 N·m of side scrub.
- *Lift-off:* a 1 g jerk (4.5 N) is below the 10 N lock.
- *Mass:* about 65 g for band, cradle and pads, against leap2-E's 110 g for suspension and sweatband. Bike fit systems are 35–60 g `[EST]`.

**(e) Cheapest experiment (~$25, an evening).** Use a $25 bike helmet with its dial cradle and chin strap removed.
- With a luggage scale, pull the front edge upward until it tips; pull the crown sideways until it yaws.
- Wear it with 300 g of coins at the crown for 20 min of TV.
- Eyeliner the ring, then roll a 76 mm disc over the bun and check that it stays inside.

Pass: tip force ≥ 8 N, no creep at the ink line, bun reachable.

**(f) Replaces / combines.** Replaces the hard-hat suspension, chin strap, magnetic chin fuse and the inner hair-shedding shell (the arc is ≥ 55 mm up; E3's still dome is the shell). Combines with E1's stiff band.

**(g) Why it might fail.**
Dial cradles press on the suboccipital nerves for some people over 20 min; looking down slides nape skin 5–10 mm under the cradle; a shallow bun weakens the lock.

---

### E3 — EXIT-PER-REVOLUTION CIRCLES on a still dome

**(a) Assumption broken.** "Hover-and-bite plus a selectable circle is hair-safe." It is for line mode, and not for circles (§1 row 6).

**(b) Principle.** Two rules.

*Rule 1: nothing hair-facing orbits.* The slave plate (E1) sits above a **still dome** that moves only with travel (leap2-F L2). Pins pass through bonded silicone diaphragm pivots and tilt, so only the tips trace the path.

*Rule 2: in circle mode a tip leaves the canopy once per revolution.* After its 60–90° window the pin vents fully to park (20 mm) and descends again at a metered speed v_d ≤ tan 30° × v_t, a plough-in of ≤ 30° (H-5.3). It never hovers in the pile. Line mode keeps hover-and-bite.

```
 circle mode, one pin, one revolution (r 10–15 mm):
   ════bite 90°════► lift (vent, 50 ms) ─ park 20 mm above skin ─ metered descent ≤30° ─► bite
 winding per entry ≤ (bite + plough arc) ≈ 210° → capstan ≤ e^(0.25·3.7) = 2.5×, never cumulative
 line mode: hover-and-bite unchanged (net winding 0 per cycle, zero force at hover)
```

**(c) Variables moved.**
- *Hair (H-5.7):* cumulative winding becomes bounded and resets each revolution. Tip time in the pile drops from 100 % to ~50–60 %, all of it monotonic (bite or plough-in).
- *Landing (leap2-F F3):* a 2 g pin at 50–67 mm/s lands at **0.05–0.07 N, against 0.46–0.85 N** for a 20 mm drop in 30–40 ms.
- *Sensation:* Michael keeps the circle. Each bite enters as a finger does, on the move.

**(d) Plausibility** `[EST]`. Feasibility needs off-window time ≥ 20 mm / (0.58 × 2πr f) + 50 ms, with off-time = 0.75/f for 90° windows. That reduces to **r ≥ ~8 mm at any f up to 4 Hz**.
- At 1 Hz, r 15: descent at 50 mm/s takes 400 ms against a 750 ms off-time; plough 28°.
- At 1.5 Hz, r 15: 400 ms against 500 ms; plough 19°.
- Circles under ~8 mm cannot park between bites. They are also below what reads as a circle on the scalp, so drop them.

Air: one 0.8 ml park per revolution per pin, ~8 ml/s for 8 pins at 1 Hz, inside one KPM27C. Descent metering is S070 PWM at the desk.

**(e) Cheapest experiment.** Leap2-F's wig test ($15), with a hand-orbited plate of three spring pens: (A) tips held 5 mm into the pile throughout, (B) tips lifted clear once per revolution, 5 min each at 6–8 cm. Count twists and measure comb-out force. Then ink-on-moving-paper for the landing streak.

**(f) Replaces / combines.** Replaces "hover in all modes". Needs E1's slave plate above a still dome.

**(g) Why it might fail.** Park-and-descend on every revolution may read as "tapping in circles". Two seals per pin (diaphragm and wiper) double the leak sites. The ±16–25° tilt swing changes the attack angle within a bite.

---

### E4 — FAIL TO FREE: pad lifts, travel holds, tubes hang from above, and the helmet is the last fuse

**(a) Assumption broken.** "Fail-safe means pins vent." On a helmet the pad also has mass, the travel can fall (8c), the bundle can yank (row 4), and the wearer may doff in the dark (row 9).

**(b) Principle.** Four mechanical layers:
1. **Radial spring lift.** The pad rides leap2-A's radial air piston with palm skids. A 3 N return spring retracts the whole pad 50 mm whenever the radial line vents: e-stop, hold-to-run release, rail dump, or power loss (the valve is normally open to vent).
2. **Travel holds unpowered** (E1's lead screw).
3. **Overhead umbilical.** The bundle leaves the helmet's top rear, behind the arc's rear stop, rises to a CPAP hose hanger (a CPAP top-of-head hose with a $15 hose lift `[KNOWN product class]`), and is held there by a **3 N magnetic clip** with a 0.5 m slack loop beyond it. Without a chin strap, the helmet lifts off at ~10 N, so the chain is: clip at 3 N, then the helmet comes off, away from the face.
4. **Per-pin bleed** (0.15 mm, τ < 1 s) and a normally-open rail dump on any sensor/command mismatch (leap2-F §4).

```
   hanger ─ 3 N clip ─╮ slack 0.5 m ─► desk
                      │ bundle (11–13 mm) rises from the top rear
   radial piston ║ ← spring retract 50 mm on vent (88 ms)
   pad ▼▼▼ + skids    any fault → pad up, travel frozen, pins vented
```

**(c) Variables moved.**
- *Rows 8a–8d and 9:* every fault ends with the pad 50 mm out of the hair, nothing loose, and no pull on the scalp.
- *Row 4:* the snag torque on the helmet drops from 1.5 N·m to ≤ 0.3 N·m.
- *Row 1:* the static umbilical tension now points up and helps.

**(d) Plausibility** `[EST]`:
- *Lift timing:* a = 3 N / 0.13 kg − g ≈ 13 m/s², so 50 mm in **~90 ms**.
- *Clip margin:* static bundle tension is 0.16–0.32 N, so a 3 N clip is about 10× above it and half the helmet's slip force.
- *Bleed cost:* 0.4 L/min at 5 pins pressed (leap2-F).
- *Mass:* about +35 g for the radial piston, skids and spring.
- *Unpowered drift:* the radial piston's spring retract has no electromagnet to fail (it is pneumatic), and E1's travel cannot drift.

**(e) Cheapest experiment (~$20).**
- A syringe-driven radial piston with a 3 N spring, carrying a 130 g dummy pad with three pens in the wig: vent it and film at 240 fps (pass ≤ 120 ms, no strand pulled).
- The row 4 bundle test on the hanger: lean back and stand up, and log helmet force on the luggage scale.

**(f) Replaces / combines.** Replaces the 12–18 N nape face-seal, the chin fuse, the electromagnet latch and the travel brake.

**(g) Why it might fail.**
A hanger ties the helmet to one chair; skids sliding at 0.7–2 N could backcomb against the grain (leap2-A (g)); a 3 N clip may drop on ordinary head turns (safe, annoying).

---

## 3. Best bet, the most likely failure, and the minimum viable helmet

**Best bet: E2 + E1, with E4's radial lift and hanger, and E3 before circles run in hair over 5 cm.** E2 is the cheapest and settles the most: a $25 bike helmet answers in one evening whether a sub-occipital cradle can hold 300 g against a moving load with the bun free and no chin strap. E1 is the step change. It takes the synthesiser Michael chose and moves it to the desk, where its noise, mass and failure modes stop mattering, and lets the master–slave air link deliver circle, line and precession to a pad that weighs ~80 g and carries no wire. It also dissolves a trade-off nobody had named: the helmet's pads were soft so that they isolate motor noise, and soft pads are what let every scrub reaction be felt at the forehead. Remove the noise and the band can be stiff. Hydrostatic travel then makes the free fall physically impossible rather than braked.

**The most likely reason the helmet fails (P ≈ 0.35): the hat is felt doing it.**
- The force loop closes through the head. In a real scratch the scratcher's arm takes the reaction; here the forehead band does.
- The pad's 130 g leans the hat as it travels: 0.19 N·m, comparable to holding a 190 g object 10 cm off the head.
- Anything geared rings through the skull.

Any one of these cues, in the first minute, turns "hands in my hair" into "a machine on my head", and no pattern layer recovers it.

The other likely failures:
- *Posture (P ≈ 0.25):* the pad works the bun, so the head cannot rest back, and the evening is spent sitting upright. CPAP's adherence record applies (leap2-E).
- *Mass creep (P ≈ 0.15):* 12–16 pins, two axes and the safety parts push past 500 g.

**Minimum viable helmet (~300 g, one axis, 8 pins)** `[EST ledger]`:

| Part | g |
|---|---|
| E2 fit system: stiff forehead band, sub-occipital dial cradle, closed-cell skin, no chin strap | 65 |
| Sagittal carbon arc R 165, forehead band to cradle, with end clamps (slim: ~170 mm wide, no ear pivots) | 38 |
| Enclosed POM-roller carriage | 15 |
| Hydrostatic pulley, two rolling diaphragms, Dyneema loop in the channel | 40 |
| E4 radial piston, palm skids, 3 N return spring | 35 |
| Pad: 8 omni-nail P × A pins, still dome, three-bellows slave plate (E1/E3) | 80 |
| Umbilical share (14 tubes, top-rear exit to hanger) | 15 |
| Fasteners and misc | 12 |
| **Total** | **300** |

What it does and does not cover:
- *Coverage:* the midline strip from hairline + 20 mm to the lower bun, ~200 cm², which holds scratch-model §5's two highest-value regions.
- *Out of scope by construction:* temples and nape, because the ring is the fence.
- *Second axis:* a two-axis bail (leap2-A's poles at the ears) is the upgrade only after the minimum helmet passes, because it adds 60–80 g and a 330 mm halo.
- *Off the head:* every motor, valve and sensor stays at the desk.
- *Patterns:* circle (r ≥ 8 mm, exit-per-revolution) and line (hover-and-bite) are selectable from the desk synthesiser.
- *Faults:* any fault lifts the pad 50 mm in ~90 ms. Doffing is: release the hold-to-run, tilt back, lift, in under 2 s.

**First weekend, under $50:**
1. The bike-helmet fit test (E2): $25.
2. The suction-cup master–slave plates and syringe water pulley (E1): $30, run against the N20-on-helmet earplug test.
3. The coin-bag CoM-wander detection test, which costs nothing.

If Michael can tell where a silently moved 130 g bag sits more than 75 % of the time, the arc needs a mirrored counterweight on the Dyneema return run (+130 g, still ≤ 430 g) before anything else is built.
