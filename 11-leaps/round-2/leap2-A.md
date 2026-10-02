# LEAP 2-A — HOW THE SMALL PAD GETS AROUND THE HEAD

**Project SCRATCH · 11-leaps/round-2 · Agent A · 2026-10-02**
Provocation: find the step-change in repositioning the small pressure-gated orbit pad.
Inputs read: LEAP2-BRIEF; leap-B (Leaps 1, 2, §3); leap-A (Leap 2); scratch-model §1–5, §7; hair-interaction §3–6; safety-requirements §2, §7; pin-unit §0–1; 08-crown/concept-A §1–5; leap-E (E1); leap-F (A–C, F). Firewall kept: no other round-2 file was read.
Tags: **[KNOWN]** sourced in the inputs · **[EST]** computed here · **[UNKNOWN]** only a bench answers it.

---

## 0. What the pad is, and what travelling has to do

**The pad (baseline for every option).**
- Seven pressure-bus pins (leap-B L1) at 20 mm hex pitch.
- An orbit carrier: r_o = 20 mm, one N20 with twin eccentric cranks (leap-B L2).
- About 110 mm across and ≈ 105–120 g [EST].
- The nails reach ≈ 40 mm from the pad axis, which is ±25° of arc on R 90.

**Head, in a skull-centred frame.** Put the centre O 45 mm above and ~10 mm behind the ear canal; this matches concept-A's R 90 sphere. Measured from O, the scalp lies at:
- 75 mm on the parietal sides;
- 85–90 mm at the vertex;
- 95–100 mm at the forehead and the occipital bun [EST: head 190–195 × 140–155 mm, auricular height ~130 mm].

Two consequences follow:
- A pad held on a radius from O sees the scalp move **±12–13 mm** along that radius.
- The scalp normal leans off the radius by up to **14°** on the sides (atan((a² − b²)/2ab), with a = 96 and b = 75), and by 15–20° on the flanks of the bun [EST].

The hair-bearing scalp is ≈ **600 cm²** [EST].

**What travel must deliver:**
- slow drift at 2–5 cm/s over 6–15 cm (leap-A's carrier);
- P6 region changes of 3–10 cm in 0.3–1 s;
- coverage in the order of scratch-model §5: occiput, then crown, then top, then sides;
- pins roughly normal to the scalp and inside their stroke.

The pneumatic pin is what makes the last item easy. Its force does not depend on seating (±15 mm at constant force, leap-B §L1 c), so **the travel mechanism has left the force path.** It no longer has to be stiff, precise, or worn on the head. Every leap below exploits this.

---

## 1. Survey: every travel mechanism, with numbers

The coverage map uses five regions: C crown, T top, O occiput (bun), S sides/temples, N nape. ✓ means reached, ½ means partly reached, ✗ means not reached.

| # | Mechanism | Coverage C/T/O/S/N | Drift 2–5 cm/s? | Motors | Mass on head | Hair safety of the travel mechanism | Force reference and normal through travel | Umbilical | Positioner cost [EST] |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Skull-centred bail, head-mounted** (ear-axis pitch plus carriage) | ✓ ✓ ½ ½ ✗ (hoop blocks the lower band, as in concept-A §5) | ✓ continuous | 2 | **350–420 g** (hoop 95, bail 26, servos 36–110, pad 110, rest 40) | Bail ≥ 55 mm up; hoop static in the hair | Radial axis 14–20° off normal; needs a datum (L2) | On the head | $80–100 |
| 2 | **Same bail, world-mounted on a face cradle** (Leap 1) | ✓ ✓ ✓ ✓ ½ (≈ 85–90 % of the hair-bearing scalp) | ✓ continuous | 2 | **0 g** | As 1, with no hoop in the hair | Same; head registered ±5 mm by the cradle | Never on the head | $90–110 |
| 3 | Lat-long: azimuth ring plus meridian arc | ✓ ✓ ½ ½ ✗ | ✓, except at the **pole, which sits on the crown whorl** | 2 | 420–480 g | **Ring bearing at band level, where long hair hangs** (red line 1) | As 1 | On the head | $110–130 |
| 4 | Fixed sagittal arch plus carriage (1 axis) | ✓ ✓ ✓ ✗ ½ (midline strip ±55 mm with the orbit and pin field) | ✓ along the midline only | 1 | 0 g (world) / ~300 g (hoop) | Rail static and ≥ 55 mm up | Same | Off-head when world-mounted | $35–50 |
| 5 | **Walking pad**: orbit as stride, pins as feet (L4) | As its mount; free: a ±45° gravity cap | **Stepwise**, 1.7–5 cm/s | 1 (the orbit) | free puck 200–280 g (≥ Σ pin force) | Pins plant ≤ 0.3 s in stance | Needs a normal-force source; gravity fails on the sides | Boom; 0.1–0.5 N drag matters | +$10–25 |
| 6 | Cable polargraph puck (leap-F B) | ✓ ✓ ½ ✗ ✗ (±45° cap) | ✓ 2–20 cm/s | 3 (off-head) | 200–280 g puck | Thin lines ≥ 30 mm up, but near long hair | Tilt follows line pull; "towed" feel | Tubes tug the puck | $60–90 |
| 7 | Pillow: the head rolls over a fixed pad on an XY stage (leap-E E1) | ✗ ✗ ✓ ½ ½ (occiput; parietal when side-lying) | Only ±15 mm XY; the rest is self-generated head roll | 2 (in the base) | 0 g | **Hair pinned under the rim** by 40–50 N | Best of all: the head's weight registers it, P × A upward | In the base | $35–50 |
| 8 | **Virtual full-head field** (valves pick the active area) | ✓ ✓ ✓ ✓ ½ | ✓ instant hand-off | 1–2 (shell orbit) | **510–590 g** (77–111 pins at 30–25 mm pitch): red line 10 | 77–111 bore exits to seal | Pin stroke absorbs ±5 mm | **77–111 tubes, 22–28 mm bundle** | $460–670 |
| 9 | Hybrid: 19-pin pad that hops (L3) | As its positioner | ✓ in-pad, 5–7 cm per placement | 2 + 1 | +35 g | Moves only when lifted (H-5.8) | As 1–2 | 21 tubes | +$60 |

**Verdicts from the table:**
- **Virtual (row 8) fails on mass and tubes.** A sparse 30 mm field still covers continuously, because each pin sweeps a 40 mm circle. But a parallel rake's spacing equals the pitch, so hand-like 16–28 mm spacing needs 25 mm pitch: 111 pins, 590 g. A crown-plus-occiput field (46 pins) is just the porcupine sector again.
- **The lat-long ring (row 3) loses to the bail on every column.**
- **The bail is the finalist.** The walker and the hybrid are ways of changing what the bail has to do.

---

## LEAP 1 — THE HALO ON THE CRADLE: a skull-centred bail whose poles are the ears, taken off the head

**(a) Assumption broken.** "The positioner must ride on the head, because the force reference must be registered to the head."
- **Why it no longer holds.** With P × A pins and a palm datum (Leap 2), the head need only stay within the pins' ±15 mm and the palm's 50 mm float. A $20 face cradle holds it to about ±5 mm [EST], so the positioner can stand on the desk.
- **A second, smaller break.** "A two-axis gimbal has a singularity somewhere." Put its axis through the ears and the singularity sits where red line 6 already forbids anything to go.

**(b) Principle and sketch.** A semicircular bail of radius 165 mm about O. Its pivots on a U-frame from the cradle base sit on the ear-to-ear axis through O. Servo A (pitch α) swings the bail from the hairline over the crown and occiput to the nape. A carriage driven by servo B (latitude β) slides along the bail. On the carriage, a spring-returned radial air piston points at O and carries the pad (Leap 2). The user sits leaning forward with the face in the cradle. Crown, occiput and nape are fully exposed, and the face is physically fenced by the cradle. This is the inverse of the pillow: **register the head on the side you are not scratching.**

```
 SIDE VIEW (pitch plane), user leaning ~40° into face cradle          FRONT VIEW (bail plane)
                                                                       
              α=+60° (crown→occiput)                                     carriage + servo B
           .-~~~~~~~~-.   bail R165 about O                          .-~~~~~[■]~~~~-.  R 165
        .'     [■]     '.     ■ = carriage + radial                .'       ║        '.
  α=0 /   pad ▼ ║ radial  \       air piston (50 mm stroke)      /    pad ▼▼▼          \
     |    .-""""""-.       |                                     |    .-""""""-.        |
  ═══O════|  skull |═══════O═══ pivot axis = ear axis (poles)  ●═╪═══|   O    |════════╪═● pivots Y±165,
     |    | O●     |       |    servo A at one pivot            |    |  skull |        |   ≥110 mm from
      \   '-.____.-' nape /                                      \   '-.____.-'        /    ear canal
       '.  face→[cradle]  '.  α=+115° stop                        '.  ear ●    ear ●  .'
         U-frame from cradle base                                     β stops ±55° (hardware)
  O = skull centre, 45 mm above / 10 mm behind ear canal; scalp at 75–100 mm from O
```

Dimensions [EST]:
- **Bail:** carbon tube 12 × 10 mm, 518 mm long, 26 g.
- **Hardware stops (red line 13):**
  - pad axis α from −30° to +115°;
  - β ±55°.
- **Nail reach:** α −62° (frontal hairline) to +147° (nape); β ±87°. That is ≈ 20 mm above the helix and ≥ 35 mm from the ear canal.
- **Pivots:** 110 mm from the ear canal.
- **Moving mass:** 236 g, giving 0.38 N·m of worst-case gravity torque. A bus servo (ST3215 class, ~2.9 N·m) has a margin of 7.6, so no counterweight is needed.

**(c) Sensory variables moved.**
- **Region (§7 #13), from "crown plus upper occiput" to ≈ 85–90 % of the hair-bearing scalp.** That adds the lower occiput, nape top and parietal sides. Concept-A §5 states the band-mounted crown cannot reach the lower occiput, inion or nape.
- **Dwell, adjacency and wander (#14, #1).** Drift paths become free curves on the sphere, for example spokes outward from the crown whorl, which are with-grain everywhere (H-5.1).
- **Dual-band velocity (#4).** Continuous servo drift at 2–5 cm/s under the orbit's 6–14 cm/s gives leap-A's carrier + grain as a true vector sum.
- **Context (E).** The posture is the massage-table one. Nothing is strapped to the head, and you leave by lifting your face.

**(d) Plausibility [EST].**
- **Drift and hops.** 3 cm/s is 19°/s, which a 4096-step bus servo (0.14 mm per step at the scalp) runs smoothly. Hops at 15–20 cm/s are 10× inside its no-load speed.
- **Scratch reaction.** ≤ 1.1 N (4 pins × 0.54 N × µ 0.7), giving 0.19 N·m and a bail deflection of 0.14 mm.
- **Backlash.** 0.5–1° maps to 0.8–1.6 mm at the scalp, a 4 % loss of orbit.
- **Kinetic energy.** 5 mJ, against the ≤ 50 mJ limit.
- **Scalp load.** ≤ 5 N in total, against ≤ 12 N.
- **Cost.** ≈ **$95–110** for the positioner (cradle $20, servos $36, carbon and bearings $25, carriage $10). The whole rig is ≈ **$250**.

**(e) Cheapest experiment (≈ $35, one weekend).**
1. Cut a plywood bail at R 165, hinge it on two bolts at the ear axis of the desk-clamped cradle, and fit a hand-slid carriage with a dummy 110 mm pad.
2. Measure three things:
   - O-to-scalp distance at 15 grid points (prediction: 75–100 mm);
   - radial-to-normal angle with a phone gyro (prediction: ≤ 20°);
   - head drift in the cradle over 10 minutes, from video (prediction: ≤ ±5 mm).
3. Then drive a figure-8 at 3 cm/s with two $8 MG996R servos to check the stops and clearances.

**(f) Replaces or combines.**
- **Replaces:** the helmet or hoop, the portal, the strap, the quick-release and the head-mass budget.
- **Needs:** Leap 2. Leaps 3 and 4 are optional.
- **Staging:** servo A alone, with the carriage locked at β = 0, already gives a ±55 mm midline strip over crown, top and occiput: the two highest-value regions (scratch-model §5).

**(g) Honest reasons it might fail.**
1. **Posture.** It is a session device, not a sofa device. The fallback is the head-mounted bail at 350–420 g, which loses the lower occiput.
2. **Coverage gaps.** The cradle pad hides the frontal hairline (P7).
3. **Fidgeting.** A head turned more than 15° misaligns the poles, and the β stop then no longer guarantees ear clearance. The fix is to vent everything when the palm-float reading leaves its range.
4. **The halo itself.** A 330 mm halo swinging over the head may feel imposing [UNKNOWN].

---

## LEAP 2 — THE PALM DATUM: let the scalp, not the machine, set the pad's standoff and tilt

**(a) Assumption broken.** "A positioner must know the head's shape (map, servo radial axis, precise centre) to keep the pins in stroke and normal." It need not. A human hand doesn't: **the palm rests on the head and the fingers work from there** (scratch-model §3.3 counts 0–3 N of resting palm weight).

**(b) Principle.**
- **Mount.** The pad hangs from the radial air piston (12 mm bore; 2.3 N at 20 kPa, capped at 4.5 N by the 40 kPa relief) on a ±20° tilt joint with an air lock.
- **Skids.** Three polished POM dome skids (R 15 mm, drafted, 28 mm proud) sit on a 100 mm circle, outside the 80 mm orbit field.
- **Landing.** With the lock open, the skids settle on the canopy. That sets the tilt (≤ 5° from normal [EST]) and the standoff.
- **Scratching.** The lock closes and the pins start, always mid-stroke.

```
              radial air piston (50 mm stroke, constant force 2.3 N, spring retract)
                         ║
                    ┌────╨────┐  tilt joint ±20°, air-locked after landing
     skid post ─┐   │ ◎ orbit │   ┌─ skid post (POM dome R15, 0.4–1 N each)
                │ ══╧═════════╧══ │  shroud, ≥30 mm above skin, drafted, sealed pin exits
                │    ▼   ▼   ▼    │  7 P×A pins, mid-stroke whatever the head shape
   canopy ~~~~~(●)~~~~~~~~~~~~~~~(●)~~~~~
   scalp  ─────────────────────────────── 
          |<-------- 100 mm --------->|
```

**(c) Sensory variables moved.**
- **Reaching the skin (#2) and force constancy (#3).** Pins always operate at the same extension, so the cos-error from a 14–20° misalignment (3–6 % force, plus 0.1–0.2 N of side load on the bore) goes away, and penetration is the same over the crown, the bun and the sides.
- **Context (E).** A light, warm-ish "hand resting" of 1–3 N [UNKNOWN whether it helps or reads as a weight].
- **A free snag and exit sensor.** A potentiometer on the radial piston reads palm float. A sudden change means the head moved or a bundle jammed, so the firmware vents everything (H-6.6).

**(d) Plausibility [EST].**
- **Skid load.** F_radial − Σ F_pins = 0.2–2.3 N over three domes of ≈ 1.5 cm², which is ≤ 5 kPa (the sustained-pad limit, safety §2.2).
- **Tipping.** Scratch drag gives a 0.033 N·m tipping moment. A 15 mm bladder lock at 40 kPa holds 0.056 N·m.
- **Mass and cost.** +25 g, ≈ $12.
- **The alternative without skids** is a 30-second contact map built from the per-pin pressure sensors' fill transients. It works only with a registered head.

**(e) Cheapest experiment (< $15, one evening).** A printed palm with three POM domes around leap-B's three-pin block, on a ball joint, pressed by a spring at 2 N. A helper slides it at 3 cm/s, crown to occiput, with-grain and then against-grain. Phone-gyro the tilt and watch a mark on one pin for its extension. Count shed hairs on a dark cloth and check for matting after 5 minutes each way.

**(f) Replaces or combines.** It replaces the radial position axis, the head map and concept-A's float with its 30 mm travel. It is required by Leap 1 and useful for any positioner, including the head-mounted bail and the polargraph.

**(g) Why it might not work.**
1. **Against-grain sliding.** Domes loaded at 1–2 N and pushed against the grain could backcomb long fine hair (hair-interaction §3.5). Mitigations: a with-grain drift bias, skids lifted at hops, and a measured matting threshold.
2. **Thick hair.** In thick or curly hair the skids ride the canopy 10–20 mm up, which eats pin stroke. The skid height must be adjustable.
3. **A new contact on the hair.** The skids are something new touching the hair, and judges will ask whether they are guard-standoff violations (H-6.3).

---

## LEAP 3 — HOP, DON'T DRIVE: put the slow drift inside the pad, and let the positioner only place it

**(a) Assumption broken.** "The positioner must make the slow drift, so it must move smoothly under scratch load." Instead, the valves make the drift by handing the active set across a medium pin field. The positioner only re-places a lifted pad every 3–20 s, to ±10 mm.

**(b) Principle.** A 19-pin hex pad (18 mm pitch) on the same r 20 orbit:
- An active "hand" of 3–5 pins migrates across the field, with a hand-off every 0.36–0.9 s for 2–5 cm/s.
- The phase windows place strokes anywhere on each pin's 40 mm circle, so the motion has no step size.
- At the field edge (after 70 mm), everything lifts, the bail hops 50–70 mm in 0.4 s, and the pad lands and continues.

```
 pad (top view), 19 pins, orbit r20 shared        time →
   ○ ○ ○            ●=active  ○=lifted           [traverse 70 mm, 2.3 s @3 cm/s][lift][hop 0.4 s][land 0.3 s][traverse…]
  ○ ● ● ○ ○         active "hand" slides  →→        valves only                   bail only (pins+palm lifted)
 ○ ● ● ○ ○ ○
  ○ ○ ○ ○ ○
   ○ ○ ○
```

**(c) Sensory variables moved.**
- **Irregularity (#1).** Drift paths, speeds and hand sizes are all firmware, and the positioner's cadence disappears because it moves only during lifts.
- **Contact count (#6).** 1–5 active pins.
- **Long sweeps (P2).** Apparent motion across 70 mm, carrying real nail strokes.
- **Hair.** H-5.8 holds by construction.

**(d) Plausibility [EST].**
- **Cost and size.** +$60 and +12 tubes (a 14 mm bundle). The pad gets +30 g and grows to 125 mm across.
- **The positioner relaxes** to two $8 hobby servos (±1.6 mm), or one.
- **Lift time.** Hops cost 0.7 s per traverse: 15–25 % lift time, close to the human 10 % of pauses.

**(e) Cheapest experiment (< $25).** Extend leap-B's 3-pin bench to 7 pins in a printed hex block, held still by a helper on the head. Blind A/B/C, 20 s each:
- (1) static hand;
- (2) valve hand-off drift at 3 cm/s;
- (3) the helper physically sliding the block at 3 cm/s with the hand fixed.

Rate "moving hand" against "flickering points." If (2) ≈ (3), Leap 3 is in.

**(f) Replaces or combines.** It makes Leap 1's servos a commodity, and it is the only way the head-mounted bail can stay silent while scratching, because the positioner is static then.

**(g) Why it might not work.**
1. Hand-off may read as **hopping points, not a gliding hand**. Apparent-motion fusion at 18 mm pitch with 0.4–0.9 s steps is not proven on the scalp [UNKNOWN]. Leap-A's own Relay leap carries the same risk.
2. Triple the valves and a bigger pad, for a benefit that a smooth bus servo also delivers.

---

## LEAP 4 — THE FEED-DOG: the orbit walks the pad, and twin antiphase orbits let it scratch without an anchor

**(a) Assumption broken.** "Travel needs its own motors." The orbit is already a stride generator. A sewing machine's feed dog moves fabric by gripping it during one half of an elliptical orbit. Here the pins grip the scalp during one window and the **pad body** moves instead.

**(b) Principle.** Whether a down pin scratches or walks depends only on what holds the pad body:
- **Body anchored** (mount braked): the pins slide, which is a scratch.
- **Body free** (balanced, unbraked): the pins grip and the body moves by minus the window's chord, 28 / 35 / 40 mm for 90 / 120 / 180° windows.
- **Pins lifted:** the body stays put.

So **drift = chord × f**, in the direction of the window's mean phase, with no added motor.

**Twin antiphase carriers** remove the anchor altogether. Two 3-pin groups sit 55 mm apart, driven 180° apart from one shaft:
- both groups down on mirrored windows: the friction forces cancel, so they scratch with no anchor;
- one group down alone: the pad walks.

The carriers also balance each other's 0.024 N shaking force.

```
  one revolution (single carrier), passive balanced mount, 2 air brakes on the mount joints
  phase:   0°        90°        180°       270°      360°
  brakes:  |--OFF--|----------------ON-----------------|
  pins:    [GRIP]   [lifted]    [SCRATCH ←]  [lifted]          stride = 2·r·sin(Δφ/2)
  body:    moves −chord           fixed                          v = stride × f

  twin carriers (antiphase, one shaft):  group A ●●●  ←55 mm→  ●●● group B
     both down on mirrored windows → forces cancel → scratch, no anchor needed
     A down alone → A grips → body walks       min spacing during orbit = 55 − 40 = 15 mm
```

**(c) Sensory variables moved.**
- **Drift (#4).** The geometry happens to match the two velocity optima: stride/orbit-speed = chord/2πr ≤ 0.32, and CT-optimal 3 cm/s over a 10–12 cm/s scratch is 0.25–0.3.
- **Two-hand asynchrony and P4 (#6).** In the twin version, converging and spreading strokes are the "fingers curling toward the palm" that leap-F and Red Team 1 call human.
- **Planted presses.** Stance gives a 0.25 s pressed nail between scratches: P5-like contact without slide.

**(d) Plausibility.**
- **Landing load.** Pin grip is µ_s Σ N = 0.4 × 3 × 0.54 ≈ 0.65 N. Accelerating a 0.25 kg effective body from 0 to the carrier speed in a 40 ms valve ramp takes 0.4 N at 0.5 Hz (63 mm/s): it grips. At 1 Hz it takes 0.8 N, so the pins slip a few millimetres at landing.
- **Walking speed.** At 0.5–0.75 Hz with 120–180° windows the pad walks **1.7–3 cm/s** [EST]: the low end of the drift band.
- **Brakes.** Each mount joint needs 0.19 N·m. A 20 mm bladder at 37 kPa gives 11.6 N on a 40 mm brake ring at µ 0.4, about 10 g and $5 each.
- **A free puck.** It needs mass ≥ Σ F_pins + margin, ≥ 250 g, and gravity limits it to a ±45° cap (leap-F §0). On a mount it needs a balanced (counterweighted) bail.

**(e) Cheapest experiment (< $30).** A desk-lamp arm counterweighted to neutral, carrying an N20 orbit plate with leap-B's 3 pins, over a foam head in a fake-fur wig. A clothespin on the lamp joint is the "brake." Gate 120° windows and measure stride per revolution by phone video against the 35 mm prediction, along with the slip fraction. Then add a second eccentric 180° out of phase with 2 pins on it, and check that mirrored windows hold the arm still.

**(f) Replaces or combines.** It can remove Leap 1's carriage servo: β becomes a passive, air-braked axis walked by the pad. It can also replace leap-F's six servos with one gearmotor. The twin-carrier pad is worth keeping for its dynamic balance alone.

**(g) Why it might not work.**
1. **Stance windows are not scratches.** Walking halves the scratch duty and makes the drift stepwise (one 35 mm step every 1.3–2 s) where carrier + grain wants it continuous.
2. **Position is dead-reckoned.** It needs encoders and slip correction.
3. **Gravity.** The mount must be balanced, or the pad creeps downhill on the occiput (µ Σ N ≈ 0.65 N against 1.2–1.5 N of weight on slopes > 25°).
4. **The twin-carrier version bends H-5.6.** Spacing between groups changes while both are in contact (minimum 15 mm). It needs the wig test.

**This is the honest answer to the provocation: yes, the orbit can propel the pad, at the right speed, for about $10. But it trades away the continuous glide that is the point of the drift.**

---

## 2. Ranking

| Leap | Coverage | Drift quality | Head mass and hair safety | Simplicity and cost | Risk | Total /25 |
|---|---|---|---|---|---|---|
| **L1 Halo on the cradle** | 5 (85–90 %, incl. the sweet spot) | 5 (continuous vector sum) | 5 (0 g; only the pad near hair) | 4 (2 servos, ~$100) | 3 (posture) | **22** |
| **L2 Palm datum** (enabler) | — | 4 (constant penetration) | 3 (skids touch hair) | 5 ($12) | 4 | 16 + enables L1 |
| L3 Hop, don't drive | (as positioner) | 3 (apparent motion [UNKNOWN]) | 5 (H-5.8 by construction) | 3 (19 valves) | 3 | 14 |
| L4 Feed-dog / twin orbit | (as mount) | 2 (stepwise, halved duty) | 4 | 4 ($10, one motor) | 2 | 12 |
| Virtual full field (survey) | 5 | 5 | 1 (510–590 g, 77–111 tubes) | 1 ($460–670) | 2 | 14 |

---

## 3. Best bet: the halo on the cradle, with a palm-datum pad (L1 + L2)

Pneumatic pins took the force out of the positioner, so the positioner can come off the head:
- **The cradle registers the head.** Face-down in the $20 massage cradle SP1 already lists, the head is held to ±5 mm and the crown, occiput and nape face the machine.
- **The bail puts its singularities at the ears.** A 165 mm carbon bail pivots on the ear-to-ear axis through the skull centre, so the gimbal's poles sit where red line 6 already forbids anything to go. The pad points within 14–20° of the scalp normal everywhere.
- **The palm removes the rest of the error.** It tilts the pad flat and sets the standoff, so the pins always work mid-stroke.

Numbers:

| | |
|---|---|
| Coverage | ≈ 85–90 % of the 600 cm² hair-bearing scalp: hairline-to-nape midline, both parietal sides and temples down to ~20 mm above the helix (hardware stops at α −30/+115°, β ±55°) |
| Mass on the head | 0 g |
| Total scalp load | ≤ 5 N |
| Motors | 3: two bus servos for travel, one N20 for the orbit |
| Valves | 9–10 (7 pins, palm, tilt lock, plus the dump) |
| Umbilical | 10 tubes, routed along the bail, never touching the head |
| Drift | continuous 2–5 cm/s with the orbit scratching underneath (true carrier + grain) |
| Region change | lifted hops at 15–20 cm/s |
| Cost | ≈ $100 for the positioner, ≈ $250 for the rig |

Build it in stages:
1. **Pitch servo only**, carriage locked at β = 0. That gives a midline strip ±55 mm wide over crown, top and occiput for $50.
2. **Add the carriage servo.**
3. **Adopt the 19-pin hop mode (L3)** only if the valve hand-off A/B shows it glides.
4. **Keep the twin-carrier feed-dog (L4)** as the experiment that would let the travel axis go passive.

**The first weekend:** a plywood bail on the cradle with a hand-slid dummy palm. Measure O-to-scalp distance, normal error and head drift. That retires the geometry for $35 before any valve is bought.
