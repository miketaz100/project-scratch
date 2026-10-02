# LEAP 2-E — The thing you wear or lie on, and how it feels to use

Leap-2 agent E · Project SCRATCH · 2026-10-02 · Provocation: form factor and experience for a small travelling pad running the pressure-gated orbit.
Read: LEAP2-BRIEF, leap-B (L1, L2, §3), leap-A (L2), leap-E (all), leap-F (§0, A), scratch-model §1–5, §7, hair-interaction §5–6, safety §2, §3.7–3.10, §7–8, pin-unit §0–1, crown concept-A §1.4–4. Firewall kept (no other round-2 files).
Tags: `[KNOWN]` sourced · `[EST]` computed here (arithmetic shown) · `[UNKNOWN]` only a test answers it.

---

## 0. What the chosen direction changes about form factor

Every earlier mount (desk arm, crown hoop, porcupine suspension) existed to hold a **position datum**. Nail force came from a spring or float, so ±5 mm of seating slop meant ±0.1–0.9 N of force error. An air pin pushes P·A anywhere along its 25–30 mm stroke (leap-B L1: 0.39 N at 10 kPa, ±0.01 N). **The mount now only has to put the pad within about ±10 mm of the scalp and react about 1 N of drag.** That frees the mount to be the head itself, using its weight as registration, or the furniture.

A hand-sized pad (3 × 3 pins at 20 mm pitch, 70 × 70 mm footprint, ~50 mm tall) weighs about **55 g**: 9 × 2.5 g pins, a 25 g sealed shell and 8 g of manifold `[EST]`. The product is whatever carries it, moves it and feeds it air.

Shared assumption I attack: **the device is something you put on.** Every concept from crown to porcupine is donned, adjusted, tethered and doffed. Michael's evening use will be decided by the number of steps between lying down and being scratched.

---

## 1. Six form factors compared

| | Helmet, hard-hat suspension | Soft cap with internal frame | Pillow, pad underneath (leap-E E1) | High-back "wing" headrest | Over-the-bed arm | **Head-spa cradle (L1)** |
|---|---|---|---|---|---|---|
| **Regions** | crown, top, upper parietal; the band sits on the occipital bun, so the bun is under-served | as helmet, in principle | occipital bun, upper nape; lower parietal with head roll; travel only ±15 mm in the hole | occiput (centre), parietal (wings); crown only with a hood | crown, top; the front hairline is over the face | upper occiput, crown, top-back, both parietals; not nape or temples |
| **Posture, 20 min** | upright only (cannot be leaned on); 455 g is tolerable (hard hats are worn all shift) but not relaxing; the umbilical tugs on every turn | upright; cap creeps (below) | supine; ring at 7–12 kPa ≈ firm pillow | reclined 20–40°, the TV posture; head leans 15–22 N into the rest `[EST: 45 N × sin 20–30°]` | supine; arm over the face is oppressive | supine, neck cradle, ≤ 15° extension; `[UNKNOWN]` comfort, though head-spa sessions run 30–60 min in it `[EST, not verified]` |
| **Mass on head** | 455 g (§2) | 250–350 g | 0 (unit 2–3 kg) | 0 (1.5–2.5 kg on chair) | 0 (3–5 kg arm) | 0 (2.5–3.5 kg) |
| **Cost** beyond pins + valves (~$100) | $70–110 | $50–80 | $60–100 | $100–160 | $80–120 | $110–170 |
| **Doffing** | lift by the brim against a 12 N magnetic chin fuse and a 15 N nape plug: 1–2 s | 1 s, but tubes follow | lift head, < 1 s | lean forward, < 1 s | slide out, 1–2 s; sitting up hits the arm | lift or turn head, < 1 s |
| **Cheapest test** | $15 hard hat + 450 g of coins at the crown + a 1.2 m dummy 9-tube bundle; wear 20 min watching TV | beanie + cardboard arc; push a 1 N block at 1 Hz and watch a marker line creep | $15 ring cushion, partner's fingers through the hole | travel U-pillow + cardboard wings on the couch, partner reaches round | $35 monitor arm + cardboard pad over a supine head | **$35 mixing bowl + cervical roll, partner's hands in the bowl (L1e)** |

**Verdicts.**
- **Soft cap: reject.** Its compliance eats the orbit. A knit cap on hair yields roughly 5–10 mm per newton in shear `[EST]`, so ~1 N of orbiting drag moves the cap ±5–10 mm out of a 20 mm orbit, rubbing the hair beneath it at 1 Hz, which is massage. Fabric over hair is also the opposite of the hair-shedding guard (H-6.3). A cap carrying a rigid arc is the crown hoop in a sock.
- **Over-the-bed arm: fold in.** Its useful reach is the crown from the headboard side, which is L1's hub. From above, it hangs a moving mass over the eyes (red line 6).
- **Pillow, pad underneath:** right instinct, wrong load path. Head weight lands on the scratched region, which pins the hair (leap-E's own first failure mode) and leaves no room to travel, which was Michael's modification.
- **Helmet and wing headrest survive.** The wing headrest is L1 tilted upright (§3).

---

## 2. The helmet, honestly, with a travelling pad

**Mass** `[EST]`:

| Item | g |
|---|---|
| Suspension and sweatband | 110 |
| Inner hair-shedding shell (1 mm PETG) | 80 |
| Two carbon travel arcs and nodes | 60 |
| Two 40 g gimbal motors (L2) | 80 |
| Carriage and arm | 25 |
| Pad | 55 |
| Chin fuse and nape plug | 15 |
| Umbilical share hanging from the head | 30 |
| **Total** | **455** |

That leaves 45 g under the 500 g red line.

**Centre of mass.** The moving 105 g (pad, carriage, arm) at r ≈ 150 mm travels 90° from crown to occiput, a 212 mm chord. The helmet's CoM therefore wanders 105 × 212 / 455 ≈ **49 mm**, and the gravity moment swings by 0.105 × 9.81 × 0.15 ≈ **0.15 N·m**. That is a third of the crown's friction hold at µ 0.3 (0.49 N·m, concept-A §3.2) and a third of the neck's 0.45 N·m at 20° tilt. Survivable, but the hat will be felt leaning toward the pad, and no human hand makes your hat slide.

**Orbit reaction.** 1 N of drag rotating at 1 Hz shears the suspension by 0.2–0.3 mm (concept-A §3.2 pad compliance). Negligible.

**Noise.** Anything on a helmet couples to the skull. A geared servo reversing at 1 Hz is ~45–55 dBA at 0.3 m in air `[EST]` and worse by bone conduction. A direct-drive gimbal motor under FOC has no mesh and no backlash; it is likely below 30 dBA `[EST, measure in L2e]`.

**Umbilical.** 2.5 mm OD PU tubes pack in circles of 3.61 d, 4.03 d and 4.62 d for 9, 12 and 16 tubes: **9.0, 10.1 and 11.5 mm** `[KNOWN packing ratios]`. With a sleeve and a 4 mm motor cable the bundle is **11–14 mm**, slimline-CPAP-hose size. Each tube weighs π/4·(2.5² − 1.5²) mm² × 1.2 g/cm³ = 3.8 g/m, so 12 tubes plus sleeve come to ~55 g/m. Route it from a nape plug, clipped at the collar, so head turns twist the 300 mm between nape and shoulder rather than the helmet.

**The CPAP warning.** CPAP is the only mass experience of nightly hosed headgear, and reported non-adherence runs 29–83 % (Weaver & Grunstein, Proc ATS 2008) `[KNOWN, cited from memory; check]`. CPAP users have a medical reason to persist. A scratch helmet user has none.

---

## LEAP 1 — THE HEAD-SPA CRADLE: carry the head by the neck, leave the scalp free in a bowl, move the pad on a remote-centre arc

**(a) Assumption broken.** That lying down means resting the scratched region on the device (E1), and that a travelling pad must ride on the head. The salon backwash and the Japanese head-spa bed already solved this. The head's weight goes on a **neck cradle** under the suboccipital shelf, and the back and top of the scalp hang free over a bowl, reachable from every side. Being scratched during a shampoo is arguably the canonical version of the experience.

**(b) Principle and sketch.** A U-shaped, heated silicone neck cradle sits on a pillow-sized base. A ~35 cm bowl surrounds the back of the head, concentric with the head centre C, with ≥ 40 mm of clear space to the scalp. The pad rides a **remote-centre-of-motion (RCM) arc**, so every movement is a rotation about C and nothing mechanical comes near the head except the pad. Two motors drive it:
- **M1** rolls the arc about the head's long axis, from left parietal to right.
- **M2** drives the pad along the arc, from crown to upper occiput.

Both motors sit in a hub **behind the vertex at the headboard end, ~165 mm from C**: away from the face and ears (red line 6) and outside the 30 mm hair zone (red line 1).

```
   SIDE SECTION, supine, head toward headboard (left); C = head centre; mm
   headboard   hub [M1 roll | M2 pitch]  gimbal BLDCs, counterweighted
      ║        ●━━━━━━━━━━━━━━━┓  arc rail R 160 about C, cantilevered from hub
      ║       ╱   pad @ 30°     ┃   (crown: pins point toward the feet)
      ║ bowl ╱   ▼▼▼           ┃
      ║ R175╱  ╭───────────╮    ┃   pad travels 20°→110° along the arc;
      ║    │  ╱   vertex    ╲   ┃   M1 swings the arc ±60° to either side
      ║    │ │       C       │  ┃
      ║    │  ╲   occiput   ╱ ◀▲▲▲  pad @ 100° (upper occiput, pins point up)
      ║     ╲  ╰─────┬─────╯  ≥ 40 mm clear to bowl
      ║      ╲_______│_______╱
      ║  neck cradle ▓▓▓ 34 °C silicone, carries 40–50 N, ≤ 15° extension
      ║  ════════════▓▓▓══════════════  mattress  → shoulders
   valve island in the base (foam pocket); pump + reservoir on the floor 1.5 m away (L3)
```

**(c) Sensory variables moved.**
- *Region (§7 rank 13; §5).* One pad reaches the **two highest-value regions**, crown and occiput (scratch-model §5 conclusion 1), plus both parietals, in one posture. The helmet's band blocks the occipital bun, and E1 reaches only the bun. Pitch 20–110° from the roll axis × ±60° of roll is a band of R²·Δφ·(cos 20° − cos 110°) = 95² × 2.09 × 1.28 ≈ **240 cm², ~45 % of the ~550 cm² hair-bearing scalp** `[EST]`, and head roll adds more of each side. This is Michael's "moves around" as real travel, not ±15 mm in a hole.
- *Force reference (rank 3).* ±10 mm of head registration (cradle give plus roll offset) sits inside the pins' stroke, so force stays P·A ±0.01 N. No strap, no seating error, and no head weight ever reaches a nail.
- *Penetration and hair (rank 2; §6).* **Nothing presses the scratched hair to the head.** Hair hangs free into the bowl. The only pinned hair is at the nape under the cradle, and the pad keeps ≥ 40 mm from the cradle edge so no stroke pulls against a pinned line.
- *Context (§1 E).* Supine, eyes closed, head held: the being-scratched posture, and the pre-sleep one (leap-E: 82 % of ASMR users use ASMR to fall asleep).

**(d) Plausibility.**
- *Size.* Occiput to C ~100 mm and vertex ~110 mm. Adding 25 mm pin standoff and a 30 mm pad body puts the arc at R ≈ 160 and the bowl at ≈ 175, so a **35 cm bowl** `[EST]`.
- *Torque.* Radial pin forces pass through C and put **no torque on the motors**. Drag is 1 N × 0.10 m = 0.10 N·m. A hub-side counterweight cancels the gravity load of 115 g at 0.16 m (≤ 0.18 N·m). Travel at 2–5 cm/s is 0.2–0.5 rad/s.
- *Singularity.* The roll axis must not pass through a region to be scratched: within ~15° of it, roll spins the pad instead of moving it. **Tilt the roll axis ~30° toward the forehead**, so the crown whorl sits at 30° of pitch and the pad never works nearer the axis than 20°.
- *Neck.* Supine head weight of 40–50 N on ~40 cm² of cradle is **10–12 kPa**, firm-pillow level. Salon backwash hyperextension is the cause of "beauty-parlour stroke syndrome" (vertebral artery injury; Weintraub, JAMA 1993) `[KNOWN]`, so the cradle is **specified at ≤ 15° extension, no rotation under load**.
- *Doffing.* Each pin bore gets an **end-of-stroke bleed hole**. A pin extending past 28 mm uncovers a 0.5 mm vent and loses pressure, so a pin cannot chase a lifted head. Lifting the head becomes a mechanical quick-release, not a firmware one.

**(e) Cheapest experiment (≈ $35, one evening, partner).**
1. Set up a 32–36 cm plastic mixing bowl ($12), a memory-foam cervical roll ($15) and towels on the bed against the headboard.
2. Put a phone inclinometer on the forehead and build up the roll until neck extension is ≤ 15°.
3. Check with a ruler that the scalp-to-bowl gap is ≥ 40 mm at the occiput and crown.
4. Lie for 20 min while the partner's hands work inside the bowl: crown, then occiput, then sides. Rate neck comfort at 5, 10 and 20 min.
5. Compare against (a) the partner scratching while Michael sits upright and (b) E1's ring cushion.
6. Next morning, ask: "would you do that again tonight?"

**(f) Replaces or combines.** It replaces:
- the helmet suspension, the 500 g budget and the chin strap;
- doffing;
- the over-bed arm (the hub *is* the arm) and E1.

The pressure-gated pins and windows are unchanged. E2 co-generation is native, because the user's slow ±30° roll adds sweep over the pad's travel. E3 lean-in works because the head is free to press back.

**(g) Why it might not work.**
1. Twenty minutes in a neck cradle may ache. Flattening it lets the occiput sink toward the bowl floor.
2. Long hair drapes onto the pad top and arc, so both must be smooth, drafted and gap-free (H-6.3). Michael's hair length decides how hard this is.
3. A 35 cm object living on the bed may be vetoed by a partner or the room.
4. Supine, the hair lies toward the bowl, so the with-grain map (H-5.1) is posture-specific `[UNKNOWN]`.

---

## LEAP 2 — THE GIMBAL ORBIT: the travel motors draw the circle, so the pad is a passive pin block

**(a) Assumption broken.** That the fast orbit and the slow travel need separate drives. Leap-B put an orbit motor on the shell and kept a separate selector or travel drive, and leap-A's carrier + grain assumed the same split.

**(b) Principle.** Both travel axes (L1's, or the helmet's arcs) are rotations about C. Command each as **drift plus a sinusoid**, 90° apart. The pad then translates in a circle of radius R_s·a on the scalp while the circle's centre wanders. With R_s ≈ 95 mm, a 20 mm orbit needs a = 0.21 rad (12°). The motors are **direct-drive gimbal BLDCs under field-oriented control (FOC)**:
- no gears, so silent and with no backlash knock;
- back-drivable, so the head can push the arc away (red line 7).

The pad carries only pins, tubes and a shell.

```
   axis 1:  θ₁ = drift₁(t) + a·sin(ωt + φ_jitter)     a = (5–25 mm)/R_s, re-drawn every revolution
   axis 2:  θ₂ = drift₂(t) + a·cos(ωt + φ_jitter)     ω/2π = 0.5–1.5 Hz, wandering; optional 2:1 ellipse
   pad on scalp:  ○→○→○→○  circle of chosen size riding a slow path   (drift = carrier, orbit = grain)
   per pin:       leap-B L2 valve windows on the orbit phase, unchanged
```

**(c) Sensory variables moved.** With a crank, the orbit radius is fixed. Here **radius, centre and shape are per-revolution choices**:
- *Stroke length (rank 9; rank 1).* With r drawn from 5–25 mm, a 60° window gives strokes of 5–25 mm instead of a fixed 20 mm, matching the hand's ±25–35 % length jitter (scratch-model §4.2).
- *Direction (rank 8).* A 2:1 ellipse gives long strokes along one axis and short ones across it, a steerable preferred rake direction to set against the hair lie.
- *Carrier and grain.* Leap-A's two timescales become one drive signal.
- *Noise (rank 15).* The gear train, and with it the "metronome" knock, is gone.

**(d) Plausibility.** Arc plus pad inertia ≈ 0.2 kg × 0.16² = 0.005 kg·m². At a = 0.21 rad and 1 Hz, α = (2π)² × 0.21 ≈ 8.3 rad/s², giving 0.04 N·m. Adding 0.10 N·m of drag makes **~0.15 N·m peak per axis** `[EST]`. That is the 40–60 mm gimbal-motor class (vendor torque to be checked), with a $15–25 SimpleFOC-type driver and a magnetic encoder per axis. Composing two orthogonal rotations leaves a parasitic pad spin of order a²/2 ≈ 1.3° `[EST]`, which is negligible. A 10 × 8 mm carbon arc, 300 mm long, deflects ~0.2 mm under a 1 N tip load `[EST]`. The pad drops from ~85 g with an orbit motor and cranks to **55 g**.

**(e) Cheapest experiment (≈ $40, an afternoon).**
- *Rig:* a 40–50 mm gimbal motor, a SimpleFOC mini driver, an AS5600 encoder and a 160 mm arm carrying a 55 g dummy pad.
- *Run:* a ±12° sinusoid at 1 Hz over a slow drift.
- *Measure:* dBA at 30 cm by phone, against an SG90 and an STS3032 doing the same motion; tracking error from a pen trace on paper over a wig head.
- *Pass:* < 30 dBA and < 1 mm error.

**(f) Replaces or combines.** It replaces the orbit motor, eccentrics, anti-rotation linkage and separate travel drive. It works on the cradle, the headrest and the helmet; the helmet gains most, losing ~30 g and its only gear noise at the skull.

**(g) Why it might not work.** Gimbal motors are weak for their size, and an un-counterbalanced arc makes them hold gravity and heat up. A 12° oscillation at 1 Hz on a long arc may excite a resonance you can hear and feel. FOC tuning is its own weekend.

---

## LEAP 3 — ONE PLUG, NO DESK BOX: the valve island lives in the furniture, and unplugging is the fail-safe

**(a) Assumption broken.** That a desk box 1–1.5 m away feeds a 12–17 mm hose to the user (leap-B L1 g3). With a world-grounded mount, the umbilical never needs to touch the person.

**(b) Principle.**
- **Valve island in the base.** The 9 valves and sensors sit in a foam pocket in the cradle base, 0.3–0.4 m of tube from the pad, with the tubes running *inside* the arc. Only a 4 mm air line and a 12 V cable leave the furniture, to a pump and reservoir on the floor.
- **One magnetic face-seal plug** joins the pad to the arc: printed 9-port blocks, a silicone grommet per port and two 10 mm N35 magnets. The pad comes off for cleaning in one pull. On a helmet the same plug at the nape is the quick-release.
- **Unplugged means lifted.** Each pad-side port opens straight into its bore. Pulling the plug vents every pin to air, and the return springs lift them all. This is the same state as the e-stop (red line 8).

```
   PAD 55 g                   ARC (or NAPE)                    BASE                          FLOOR
   9 bores ═ 9 ports ╗◉ ◉╔ 9 ports ─ 9 tubes 0.3–0.4 m ─► valve island ── 4 mm, 1.5 m ──► pump + 1 L tank
                     ╚═══╝  grommets; pull-off 12–18 N      (9 × 3-way + P)                 + 40 kPa relief
   unplug → every bore open to air → all pins lift (= e-stop state)
```

**(c) Sensory variables moved.**
- *Asynchrony (rank 6), via latency.* Tube RC scales with length, so 0.35 m instead of 1.2 m cuts the tube term from ~4 to ~1.5 ms `[EST, from leap-B's 4 ms/m]`. Orifice fill (~20 ms) then dominates, for **~25–45 ms per gate** instead of 30–60. That makes the 60° window at 1.5 Hz (111 ms), which leap-B put "at the limit", controllable.
- *Sound (rank 15).* The pump (~50–60 dBA at 30 cm `[EST]`) moves to the floor in foam, giving < 30 dBA at the ear. The valve pocket hangs on sorbothane so nine solenoids ticking at 2–4 Hz do not become a typewriter in the cradle.

**(d) Plausibility.**
- *Separating force:* 15 kPa × 7 mm² ≈ 0.1 N per port, trivial.
- *Pull-off:* grommet friction ~0.5 N × 9 against ~2 × 8–10 N of magnet hold gives **12–18 N** `[EST]`, under safety §3.9's 20 N and matching the crown's 12 N fuse.
- *Leakage:* a 1.8 L/min pump covers a few ml/min of grommet leak.
- *Tubing:* multi-core ribbon tubing (SMC, Festo; part numbers not checked) could replace the 9 loose tubes inside the arc.

**(e) Cheapest experiment (≈ $15, an evening).** Print the port-block pair and fit 9 grommets, 2 magnets and three leap-B bench pins. Pass criteria:
- leak-down from 15 kPa below 1 kPa/min;
- pull-off of 12–18 N on a kitchen scale;
- all pins lifted within 150 ms of unplugging (phone at 240 fps).

**(f) Replaces or combines.** It replaces the desk box with a floor brick and removes the hose from the body. On a helmet it merges the umbilical clip and the doffing step.

**(g) Why it might not work.** Printed face seals leak. The magnets may disturb leap-E E3's hall-sensor lean-in array. Valve clicks reach the mattress unless isolated, and a partner will hear them.

---

## LEAP 4 — THE SUPPORT IS THE OTHER HAND: warmth, weight, sound and ritual come from the cradle, not the pad

**(a) Assumption broken.** That component E (warmth, a hand's weight, "someone is doing this") must come from the scratching device; leap-E E4 added a second heated palm to get it. In a cradle **the head is already held**. The support can be the holding hand while the pad is the scratching hand.

**(b) Principle.**
- **A warm hand under the neck.** A 5–10 W silicone heater holds the cradle at **34 °C**, with a thermistor loop and a 40 °C bimetal cut-out (below the 41 °C contact limit, safety §2.6). Forty square centimetres under 40–50 N is felt as a palm. CT afferents prefer skin temperature (Ackerley 2014, via leap-E) `[KNOWN]`.
- **The tips are warm enough already.** Polymer tips contact at ~30 °C (leap-E's √(kρc) estimate), so steel stays out of the pins. Heating the air is pointless: 1 ml per landing carries ~1 mJ/°C.
- **The bowl is a reflector.** With silent motors (L2) and the pump on the floor (L3), the loudest thing in the bowl is the nail hiss, and a 35 cm bowl around the ears returns it. That is what leap-E's piezo and earbuds were reaching for. Felt on the bowl's outside stops it ringing.
- **The ritual:**
  - *Arrival:* the cradle is already warm (on a timer, or switched on by weight). Lie down and press the hold switch.
  - *First touch:* all 9 pins land together at 0.1 N on a 0.5 s ramp, with no orbit for 3 s: a hand arriving.
  - *Build:* slow carrier, then orbit, then rakes (leap-E E4's 0–60–180 s build).
  - *Departure:* releasing the switch lifts the pins on a 0.5 s ramp rather than a snap, the pad retreats along the arc, and the heat stays on for 2 min. Release doubles as the sleep detector.

**(c) Sensory variables moved.** Component E goes from absent and ranked last (scratch-model §1.3) to three channels (warmth, held weight, audible scratch) with no new actuator on the pad. Ranks 15 and 16 are addressed. The head-level machine signatures are gone: no hum, no leaning hat (§2), no hose on the body.

**(d) Plausibility.** The heater is a $8, 12 V, 0.5 A part. A concave reflector of R 175 mm with the ears 60–80 mm from its surface gives a few dB above ~1 kHz, which is the hiss band `[EST, order of magnitude; UNKNOWN in practice]`.

**(e) Cheapest experiment (≈ $10, inside the L1 evening).**
- *Warmth:* a microwaved wheat pack in the cervical roll against a room-temperature roll, 2 × 5 min with the partner scratching in the bowl. Rate "being cared for" and pleasure, 0–10 each.
- *Sound:* record with a phone at ear position, with and without the bowl, while the partner scratches.

**(f) Combines with.** L1 natively, and the wing headrest likewise, since a headrest is also a holding hand. It is impossible on a helmet, where nothing holds the head.

**(g) Why it might not work.** Warmth and holding push toward "comfort/massage", scratch-model §8's neighbour. Amplified hiss can read as "creepy close-mic" to non-responders. Both are modulators and cannot rescue bad contact physics.

---

## 3. Best bet: the head-spa cradle (L1) + gimbal orbit (L2) + one plug (L3) + warm support (L4)

**The case.** The pressure-gated orbit dissolved the force-datum problem, so the mount can be chosen for the experience instead of for stiffness. Michael asked to be scratched, passively, by something that moves around his head. The cradle is the only form that gives the small pad real travel over **both** high-value regions in one posture: ~45 % of the scalp, crown to upper occiput and both sides. It does this with:
- **zero head-borne mass**;
- no hose on the body;
- no hair clamped under a support;
- doffing in under a second by lifting the head, with bleed holes that stop any pin from following.

L2 makes the pad a 55 g passive pin block whose travel motors also draw the orbit, re-sized every revolution, which is carrier + grain in one signal, silently. L3 hides the valves in the base and the pump on the floor, so the nails are the only sound. L4 turns the support into the warm, holding second hand. The $35 mixing-bowl evening tests the two things that could kill it, 20-minute neck comfort at ≤ 15° extension and a ≥ 40 mm scalp-to-bowl gap, before anything is printed. The pins and windows are unchanged and can be benched in parallel on leap-B's three-pin rig. The same arc docks on a high-back chair headrest (the wing form: the cradle tilted 30°) if the bed proves wrong.

**What Michael would actually use every evening, honestly.** Count the steps.
- **Helmet:** shelf, plug, don, ratchet, chin fuse, sit upright (it cannot be leaned on), hold the switch. Afterwards there is helmet hair and a bundle to coil. That is seven steps, a posture that is not his evening posture, and CPAP's adherence record. He would use it for a fortnight, then at weekends.
- **Cradle:** lie down, press. He would use it nightly *if it can stay on the bed*. That is its real risk: a 35 cm object replacing a pillow can be evicted by a shared bed or a tidy room.
- **Couch headrest:** the fallback, with the same arc, for the evening TV posture. Doffing there is leaning forward.

My prediction: the cradle on the bed if he sleeps alone or the partner tolerates it, otherwise the couch headrest. After the first month, never the helmet.
