# RED TEAM 3 — Simplicity, Usability, "Will He Actually Build and Use It"

**Target:** LEADING-ARCHITECTURE-v0 "SP1 FLOAT-ARM". **Date:** 2026-10-01.
**Read:** BRIEF §3/14/15/16/17; LEADING-ARCHITECTURE-v0; hybrid-and-simplicity; judge-3-experiment; team-F/G/D/C; scratch-model §7–9; component-landscape §8–10; DIRECTOR-LOG; judge-1/2 posture remarks.
**Stance:** adversarial. I am paid to prove v0 will not get built, or will get built and not used. Where v0 is right I say so briefly.

---

## 0. The one-paragraph read

v0 is a good research rig designed by people who will not have to build it. It carries two servos, a load cell, three safety switches in series, a parallelogram float the Director himself calls the highest-risk printed part, a ~15-feature firmware, and a second complete mechanism (WR-1) on a second toolchain — all before anyone knows whether a motorised nail on Michael's scalp feels like a person for thirty seconds. Its stage plan is incoherent: the "elbow servo only" stage has no lift-at-reversal, because v0 hung the hand under the pivot to *minimise* arc rise and then added a float that absorbs what is left, so that stage either violates the gating hair rule or silently depends on the lift servo. Its posture (seated, forehead on a cradle clamped to a desk, foot on a hold-to-run pedal) is a treatment posture; judge 1 already called it "the least relaxing of all". The fix is not a different mechanism — the teams and judges are right about the hand, the dead weight and the frame — it is **one servo, one float with a down-stop that gives geometric lift, one hand, one pedal, one pot, on a bed**, PERIODIC-vs-HUMAN in week two, and data buying every further part. That costs ~$245 and ~17 hands-on hours after the wand, at roughly double v0's chance of being finished and used.

---

## 1. Count the parts, the skills, and the honest probability

### 1.1 Inventory of v0 as drafted

| Category | Count | Notes |
|---|---|---|
| Bought line items, rig | ≈ 30 | arm, cradle, 2 × XL330, OpenRB, brick, fuse, e-stop, pedal, forehead switch, wrist switch, INA219, HX711 + cell, pots, OLED, bearings, leaves, nails, magnets ×3 grades, Dyneema, slugs, hardware, pad |
| Bought line items, WR-1 | ≈ 10 | N20, DRV8871, Pico, Hall, bearings, rods, springs, second tip set |
| Test gear | 5–6 | mannequin, 0.1 g scale, luggage scale, loupe, lint roller, 240 fps phone |
| Distinct printed designs | ≈ 30 (≈ 40 pieces) | rig ≈ 20 (adapter, guard + tower, arm, float housing, links, cell adapters, post, wrist plate, carrier, clamps, tang blocks, collars, pad carrier, box, lift mount, guide); WR-1 ≈ 8; wand 2–3 |
| Hand-fabricated | ≈ 15 | 6–9 tips filed to R 0.3/0.5 mm under a loupe; 3 heat-bent paddles; 3 leaves; shims; detent gap tuned; tendon rigged and zeroed |
| Firmware features, OpenRB | ≈ 15 | bus + current-position mode; trapezoid; lift/stroke phasing; pattern sampler; PERIODIC; tendon force jitter; snag reflex; stall trip; INA219 watchdog; HX711 logging; pots/switch; OLED; limits table; soft start; timeout |
| Firmware features, Pico (WR-1) | ≈ 6 | a second toolchain entirely |
| Distinct skills | ≈ 11 | **CAD (nobody has said who makes the STLs)**; 3D printing (own/library/JLC, 7–14 day lead); soldering; Arduino + Dynamixel SDK; HX711 calibration; Pico + DRV8871; printed-mechanism tuning (stiction, detent gap, tendon zero); hand-filing to 0.1 mm radius; heat-forming PETG; kitchen-scale calibration; running a blinded self-rating alone |

The CAD line deserves its own sentence. The brief asks for "dimensions sufficient to fabricate", not STL files. Thirty printed designs with ±0.1–0.2 mm pockets, a drafted guard window and bearing seats is 20–40 hours of CAD for someone who has not done it, and it sits *before* the first print. If the package does not ship STLs (or parametric OpenSCAD), halve every probability below.

### 1.2 Probability of finishing in three weekends

Three weekends is six days; a motivated amateur gets ~5 focused hours a day, so ~30 hands-on hours, with print turnaround (library days; JLC 7–14 days) and shipping interleaved. v0's own estimate is 30 + 12 h (WR-1) = 42 h, excluding CAD, printing and any reprint. A 1.5× first-timer multiplier is conservative: ~60 h.

- **P(v0 finished and first human session within 3 weekends):** ≈ 10–15 % with STLs supplied; ≈ 5 % without.
- **P(v0 finished within two months):** ≈ 35–40 %.
- **P(Michael uses v0 for ten sessions):** ≈ 20–25 %, limited by posture and setup friction (§5), not the mechanism.

### 1.3 The three most likely abandonment points

1. **Weekend 1 ends with nothing physical.** Parts arrive; prints do not (no printer, library prints PLA only, first parallelogram links bind). Michael has spent a weekend on CAD and ordering and has not touched his scalp with anything — the classic death of a hobby robot. The Day-0 wand only partly inoculates, because it too needs a printed tang block and handle.
2. **The float-and-load-cell loop (weekend 2).** A float with 0.2 N of stiction under a 0.6 N dead weight is a ±30 % force error — the rig's reason for existing — and the fix is print-measure-reprint. Add HX711 wiring, calibration and logging, and a scratch session is still a week away. Motivation is lost to instrumentation of a sensation nobody has felt.
3. **The first machine session says "machine".** After 25–40 hours: two minutes, forehead on a desk, foot on a pedal, one 50 × 40 mm patch, XL330 10 cm from his ear. It feels mechanical. The remaining knobs are firmware, which means leaving the cradle for the laptop. No obvious next physical action, so no next session.

---

## 2. What in v0 does not help answer the question

The question (BRIEF §15): *does this help determine whether automated human-like scratching can feel excellent?* Information yield in sessions 1–10, per part.

| Part | Decision | Why |
|---|---|---|
| **Load cell + HX711** | **DEFER** to stage 3 | Force is a mechanical constant set by slugs; a constant you set, you already know — press the hand on the kitchen scale at the aimed angle, once per weight. The cell's yield (ratings-vs-measured-N, contact fraction, snag events) matters when he sweeps force systematically, not in sessions 1–10. The cost is wiring, calibration, logging code and a tethered laptop he cannot see. |
| **OLED** | **CUT** | The hybrid cut it; v0 reinstated it by copying Stack A. Laptop serial shows the same table; prone, he sees neither. |
| **INA219** | **DEFER, pending Safety Gate** | A firmware watchdog; the fuse is the hardware barrier (red line 13) and XL330 Present Current already feeds the stall trip. Reinstate if the Safety Gate demands a rail monitor. |
| **Second (lift) servo** | **DEFER** to stage 2, data-gated | §3(c): a float **down-stop** plus ±25° over-swing gives ≥ 5 mm lift at zero force at every reversal by geometry, so H-5.2 is met with one servo. The lift servo uniquely adds force jitter, soft-landing shaping, commanded lift height and *unidirectional* 45° raking with an air return. Only the last may be decisive, and the Day-0 wand answers it (uni vs tip W) before any servo is bought. |
| **Wrist magnetic detent** | **KEEP** | Passive, $4, the only hand-level tangential yield. |
| **Wrist detent microswitch** | **DEFER** | With one servo the reflex is "swing on to park", which geometry already does; Present Current does the detection. Add if tether tests show the detent breaking in normal use. |
| **Forehead dead-man switch** | **CUT** for SP1 | Three switches in series for a 0.6–2 N dead-weight hand with two magnetic breakaways. It adds a printed carrier, a pad microswitch, a cable to the cradle and a false-trip mode (every head shift drops the motor mid-stroke, hand resting at dead weight — the state it exists to prevent). Safety mandates "a foot pedal *or* hand switch"; the pedal is the dead-man, and head withdrawal is the release regardless. |
| **Hold-to-run pedal** | **KEEP for staging; latching after** | Twenty minutes on a pedal is a cramp; the safety doc scopes hold-to-run to "staged tests". Latching run switch + NC e-stop in hand after the staged protocol. |
| **Pattern engine (episodes, start-x drift, force jitter, logging, snag reflex)** | **SIMPLIFY** to ≤ 100 lines | Stage 1 needs amplitude, centre, speed, per-stroke uniform resampling of (amplitude, speed, pause) with a jitter-% pot, and a PERIODIC toggle — three `random()` calls. Episodes, drift and logging are stage 2–3; force jitter and snag lift need the deferred servo. |
| **WR-1 as a separate build** | **CUT** from SP1's path | A second mechanism on a second toolchain (Pico + DRV8871 + N20 + Hall), eight printed parts, one risky tolerance (the ellipse must not bind), 12 h of the only builder's time. Its justifications — tips under real kinematics, a faithful periodic control, the predictability penalty — are delivered by the swing servo in PERIODIC mode (0.13 mm/count at the nail, below what sliding skin resolves). "In parallel" is parallel only with two builders. |
| **Monitor arm** | **KEEP** | Judge 1's "too compliant at 2 Hz" concerned a 400 g two-servo module; a ~150 g one-servo module at 1 N reaction is fine and the float absorbs the rest. |
| **Parallelogram float on 623ZZ** | **KEEP, print first** | It *is* the force physics. Bearings, not printed pins; go/no-go on measured stiction. |
| **3-leaf hand, TM1, tips, slugs, e-stop, fuse, brick, OpenRB, one XL330** | **KEEP** | These are the experiment. |

Net effect on sessions 1–10: no loss of information about whether it feels like a person; loss of a force log and of force jitter, both recoverable in an afternoon when the data asks.

---

## 3. The strongest case for a simpler SP1

All four options keep force a mechanical constant and lift before reversal.

### (a) Hand wand only — Michael's arm is the actuator

**Cost / hours:** $30 plus scale and mannequin; 3 h. **Answers:** Q1 reach (the "fatal and invisible" risk), Q3 force band, Q6 edge, Q7 direction, Q8 penetration, compliance 0.2 vs 0.4 N/mm, tip-level hair safety, uni-vs-W. **Can never answer:** whether it feels like *someone else* (self-touch is centrally attenuated, scratch-model §4.3 — the one thing the north star cannot tolerate), the predictability penalty, any pattern question, habituation, hands-free. **Verdict:** the mandatory gate, not SP1. Keep it at Day 0 and let it kill the project cheaply if the tip cannot reach skin.

### (b) WR-1 wand only ($85, one weekend)

**Answers:** a motorised, lift-every-reversal fixed stroke on his scalp; PERIODIC vs speed-jitter; whether 23 % contact duty reads as flicks. **Cannot answer:** length, location or force jitter — and that is the asymmetry: if WR-1 feels good the big question is answered *yes* cheaply; if it feels like a machine you cannot tell whether the fault is fixedness (which the model predicts) or per-stroke physics. In headband mode its force is seating-coupled (the judges' decisive objection); in wand mode it is not hands-free; and its critical print (double eccentric in two yoke slots) must run without binding or the weekend is lost. **Verdict:** a fine product seed; a poor first instrument because it answers the question only when the answer is yes.

### (c) Single-servo swing on the monitor arm with a gravity hand — the recommended SP1-S

A correction first: "gravity hand, no float" is a contradiction. Something must let the hand descend under its own weight, and that is a float; without one, force is leaf stiffness × depth under a head wandering ±10–20 mm — the head-worn failure the judges rejected. The minimal float is v0's parallelogram on four 623ZZ bearings; keep it.

**The one change that removes the lift servo:** give the float a **down-stop** 3–4 mm below the θ = 0 contact position and over-swing to ±25°. With the hand under an 80 mm arm over an R 90 scalp, arm–scalp separation grows ≈ 80(1 − cos θ) + (80 sin θ)²/180: ≈ 7 mm at ±18°, ≈ 14 mm at ±25°. The float follows for its first 3–4 mm at constant dead-weight force, hits the stop, and the arm carries the nails off the skin for the last ~10° of swing — ≥ 5 mm clear at zero force at every reversal, by geometry, no firmware, no second actuator. Contact chord ≈ 36 mm; park = +25°; lift between episodes = park; snag response = continue to park (never reverse, H-5.9). The down-stop never adds force: it limits how far the hand hangs *below* the arm, not how hard the arm can push, and the float keeps its full upward travel for head motion. This is Team G's Concept 1 with Team D's force physics, a strict subset of v0; the lift servo bolts on later.

**The honest cost:** both half-swings are in contact, so a 45° nail scoops on the return (Team F's F5 analysis). SP1-S therefore runs tip W (C's symmetric wedge) bidirectionally. The Day-0 wand decides uni-vs-W in forty seconds; if a unidirectional 45° nail is clearly better, the lift servo is bought with that data. If W is fine, SP1-S is the whole machine.

**Cost:** XL330 $27, OpenRB $29, brick $18, e-stop + hand switch $20, monitor arm $36, cushion $20–25, bearings $7, leaves $8, nails/picks $11, magnets $8, slugs/hardware $18, pots/wire $15, prints $30 → **≈ $245**, plus $45 test gear. **Hours:** ≈ 14–17 after the 3 h wand (the hybrid's own week-1 figure). **Answers:** the "someone else" attribution, Q2 speed, Q4 count, Q5 predictability with length/location/speed/pause jitter, Q7 direction, Q9 sound, Q10 habituation to 10 min, noise, posture — the big question. **Cannot answer:** force jitter and soft-landing shaping (lift servo), measured-N force curve (load cell), region wander beyond re-aim (§4).

### (d) Reclined-headrest, face-up, module from above/behind

Face-up, the occiput and nape are on the headrest; the sides have horizontal normals, so a dead weight does not load them; what is left is the crown/front-top, reached by a module *over the face* — which safety red line 6 ("no moving element above the eyes unguarded") forbids. Cost: a $120–200 recliner plus a side mount. **Verdict:** rejected on red line 6 and on gravity geometry. The reclined *intent* (relaxed, head supported) is right and is met by the prone posture in §6.

---

## 4. The case for *more* ambition on the one axis that matters

v0 is under-engineered on **region wander**. It scratches one 50 × 40 mm patch until Michael reaches back and re-aims by hand. Scratch-model §4.2 and Q10 say a human moves every 5–20 s, and the rank-1 variable explicitly includes "region changes". Judge 1 praised D as "the only candidate that changes region by itself"; v0 lost that with the yoke.

**The cheap addition with outsized sensory value is a second XL330 as a yaw axis, not a lift axis.** A servo with its horn vertical, carrying the swing-servo bracket above the guard, rotates the stroke plane about an axis offset ~40 mm from the hand: ±30° of yaw moves the patch ±20 mm *and* changes direction relative to the hair lie (rank 8), with no IK, one printed bracket, 30 lines of firmware and a cable loop. Against the lift servo it buys two top-nine variables instead of sub-dimensions of one. Still stage 2: build it only if HUMAN beats PERIODIC but goes dead in one patch within five minutes. A fourth contact is a tip-removal experiment first; per-finger independence is forbidden in the canopy (H-5.6) and supplied by compliance; neither needs hardware.

---

## 5. Usability: the first ten sessions, v0 as drafted

Session 1, v0 as drafted. Annoyance 1 (ignore) – 5 (quits).

| Step | What actually happens | Rating |
|---|---|---|
| Setup | Clear the desk edge he works at, clamp the cradle, swing the arm over, plug in brick + USB, open the laptop. ~5 min; it will not live on a working desk in an apartment. | 3 |
| Aiming | He cannot see the back of his own head. Reaching back blind to put a 3-nail hand on a 50 × 40 mm patch with his forehead down; the float fixes depth, nothing fixes position. | 4 |
| Forehead on cradle | Trunk unsupported, neck flexed, forehead taking 10–20 N, sinus pressure, breathing into the desk. Massage clients tolerate this *prone, body supported*; seated it is a dentist's chair. | 4 |
| Pedal | Hold-to-run under one foot for the whole session; a cramp by minute 8. Any forehead shift trips the dead-man mid-stroke, nails resting at dead weight. | 3 |
| Intensity mid-session | Slugs are physical: stop, reach back, unscrew, add 20 g, re-aim. v0's "intensity pot" acts only through the tendon unload, i.e. the servo he may not have built. No live knob in the one-servo stage. | 4 |
| Tip swap | Magnetic, 10 s — but behind his head: swing the arm round, swap under a lamp, swing back, re-aim. | 2 |
| Recording feedback | Forehead down: cannot write or see the laptop. Needs a phone voice memo with a 30 s chime; unspecified. | 2 |
| Cleaning | Sebum and shed hair on nails, clamps, collars and float; sweaty pad. 3–4 min with a lint roller. | 2 |
| Packing away | Arm + module + cradle + e-stop box + brick + laptop cable on a desk he uses: a robot lives on his desk or costs 5 min each way. | 3 |
| Noise | Plastic-gear XL330 ~100 mm from the ear, through the arm. | 2–3 |

**What makes him stop after session 3:** 5-minute setup, blind aiming and a posture that hurts his neck, applied to a 2-minute session that feels like a slow machine stroking one spot. None of that is the mechanism. Fixes, all cheap: prone on the bed (§6); tape marks on the arm joints and a phone as a mirror; latching run switch + e-stop in hand after staging; three pre-weighted slugs and a *speed/jitter pot within reach* so there is something to turn; voice memos with a chime; the arm lives folded against the nightstand.

---

## 6. Posture: pick one

| Posture | Gravity on float | Support / stillness | Relaxation | Fabrication | Verdict |
|---|---|---|---|---|---|
| Seated, forehead on cradle at desk (v0) | good | neck holds it; drifts | poor ("least relaxing of all") | cradle clamp, pad switch | reject for sessions 1–10 |
| Reclined, face-up, module from above | fails (sides horizontal; occiput occluded) | excellent | excellent | recliner + side mount | reject: red line 6, geometry |
| Side-lying on bed, module from behind | fails (exposed normals horizontal) | excellent | excellent | nightstand clamp | only with a constant-force-spring float (orientation-independent; SP2 idea) |
| Sitting, chin on hands | poor; bobs with breathing | poor | poor | none | reject |
| **Prone on bed, face in a portable face-cradle cushion, arm from the nightstand or a 2020 floor stand** | **good** (occiput and crown normals vertical) | **excellent** (body supported, no neck load; massage clients hold it 30–60 min) | **good** (nap-able — literally "being scratched while lying down") | $20–25 cushion, no printed parts | **recommend** |

Prone keeps every piece of v0's force physics (vertical dead weight, head withdrawal as release), deletes the desk, the cradle clamp and the forehead switch, and makes the session something he will do on a Tuesday night. Hold-to-run becomes a thumb switch on the e-stop lead. The one new requirement is a clamp surface within ~500 mm of his occiput — nightstand edge, bed-frame rail, or a $30 2020 floor stand — which the package must specify.

---

## 7. Staged-build audit and rewrite

v0's stages: hand wand → WR-1 wand → float + hand + elbow servo → lift servo → pattern engine. Faults: (i) WR-1 is on the critical path and is not a subset of the final rig; (ii) "elbow servo only" has no lift-at-reversal unless the float down-stop (§3c) is designed in, which v0 does not mention; (iii) the pattern engine is last, but PERIODIC-vs-HUMAN is the week-2 question; (iv) load cell, INA219, OLED, wrist switch and forehead switch arrive in stage 3 by default with no gate; (v) there are no go/no-go criteria anywhere.

**Rewritten stage plan**

| Stage | Build | Cost / hours | GO criterion (to next stage) | NO-GO action |
|---|---|---|---|---|
| **0 — Hand wand** (days 0–3) | Printed handle + tang block + leaf; tips A, B, C, F, H, W; kitchen scale; mannequin. All stage-1 orders placed in parallel. | $35 / 3 h | Nail reaches skin at ≤ 0.5 N in *his* hair (side photo); A or B beats ball H blind; zero captures in 200 wig strokes; collar probe clean; **uni-vs-W decided**. | Fix the tip. Nothing motorised is assembled. |
| **1 — SP1-S** (weekends 1–2) | One XL330 + arm + guard; float on 623ZZ with down-stop and slug post; 3-leaf hand; OpenRB, brick, fuse, e-stop, thumb hold-to-run; speed pot, jitter pot, PERIODIC toggle; arm on nightstand; prone cushion. Firmware ≤ 100 lines. | +$210 / 14–17 h | **Bench:** float stiction ≤ 10 % of lightest weight; lift ≥ 5 mm at zero force at ±25° on 240 fps; kitchen-scale force ±15 % of setting at aimed angle; plug-pull 20× leaves the hand at dead weight with free travel; safety §6; wig run. **Human (2 → 5 → 10 min):** HUMAN rated "feels like a person" ≥ 6/10 for > 2 min, and he wants session 6. | PERIODIC ≈ HUMAN, both ≥ 6: machine done; spend on tips, regions, sessions. Both < 4: fault is per-stroke physics, noise or posture — ear-plug A/B, wand sweep; do **not** add servos. |
| **2 — second servo, data-chosen** | **Yaw** (HUMAN > PERIODIC but one patch dead < 5 min) or **lift** (wand said uni-45° ≫ W, or return-stroke scoop reported). | +$30 / 4–6 h | Same criterion sustained 10–20 min with region changes every 5–20 s. | Revert to stage 1; servo to the drawer. |
| **3 — instrumentation** | HX711 + cell for the force sweep (Q3); wrist microswitch if tether tests demand; INA219 if the Safety Gate demands. | +$25 / 3 h | — | — |
| **Off-path** | WR-1 (someone else, or product seed); OLED never; forehead dead-man only if the Safety Gate overrules §2. | | | |

Exposure if stage 0 fails: $35 and reusable electronics. If stage 1 fails on sensation: ~$245 and the knowledge that the per-stroke physics is wrong — exactly what the programme needs to know.

---

## 8. Verdict

**Recommendation to the Director.** Do not ship v0 as drafted; ship **v0 simplified to SP1-S**: one XL330 swing on an 80 mm arm, the dead-weight parallelogram float with a 3–4 mm down-stop and ±25° over-swing so lift-at-reversal is geometric, the 3-leaf TM1 hand with tips chosen by the Day-0 wand, one speed pot, one jitter pot, a PERIODIC toggle, NC e-stop plus a hand-held hold-to-run, a monitor arm clamped beside his bed, and Michael prone with his face in a $25 cushion. Cut the forehead dead-man, the OLED and the WR-1 side build; defer the lift servo, load cell, wrist microswitch and INA219 behind explicit gates; if a second servo is earned, spend it on yaw before lift. Require STL or OpenSCAD files for every printed part, because the CAD gate is the first abandonment point and nobody owns it. This keeps every decision the tournament got right — frame-mounted, dead-weight constant, lift before reversal, nothing on the head, withdrawal as release — and removes everything that is instrumentation of a sensation nobody has felt yet.

**One line:** P(Michael finishes and uses it for ten sessions) — v0 as drafted ≈ 20–25 %; SP1-S ≈ 55–60 %; either number halves if he has to make his own STLs.

---

## 9. Final cut / keep / defer table

| Item | Decision | Gate to reinstate |
|---|---|---|
| Hand wand + 6 tips (Day 0) | **KEEP** (mandatory first) | — |
| Monitor arm (desk/nightstand clamp) | **KEEP** | — |
| Prone face-cradle cushion on bed | **KEEP** (replaces desk cradle) | — |
| Seated desk face cradle + forehead dead-man switch + pad carrier | **CUT** | Safety Gate overrules; or prone proves intolerable |
| XL330 #1 (swing) + 80 mm arm + guard plate | **KEEP** | — |
| Parallelogram float on 623ZZ + dead-weight slugs | **KEEP** (print and measure first) | — |
| Float down-stop + ±25° over-swing (geometric lift) | **ADD** (new) | — |
| XL330 #2 as **lift** + Dyneema tendon | **DEFER** | wand says uni-45° ≫ W, or return-stroke scoop reported |
| XL330 #2 as **yaw** (region/direction wander) | **DEFER** (preferred use of a second servo) | HUMAN > PERIODIC but one patch dead < 5 min |
| 3-leaf hand, TM1 tang blocks, collars, paddles, unequal preloads, D61 hand breakaway | **KEEP** | — |
| Wrist magnetic detent | **KEEP** | — |
| Wrist detent microswitch | **DEFER** | detent breaks in normal use on tether test |
| 1 kg load cell + HX711 + 80 Hz logging | **DEFER** | force–pleasure sweep (Q3) begins |
| INA219 rail monitor | **DEFER** | Safety Gate demands it |
| OLED | **CUT** | never |
| OpenRB-150, 5 V brick, fuse, NC e-stop | **KEEP** | — |
| Foot pedal hold-to-run | **KEEP for staging → latching run switch + hand e-stop after** | — |
| Intensity pot (tendon-unload) | **CUT**; replace with speed pot + jitter pot + 3 pre-weighted slugs | returns with lift servo |
| Pattern engine: episodes, start-x drift, force jitter, snag lift-and-hold | **DEFER** | stage 2 servo exists |
| Pattern engine: per-stroke uniform jitter + pauses + PERIODIC toggle (≤ 100 lines) | **KEEP** | — |
| WR-1 Walking Rake (second build, Pico toolchain) | **CUT** from SP1 path | a second builder, or product-seed interest after SP1 |
| 4th contact / alternate pitch carriers | **DEFER** | 1/2/3 tip-removal results |
| Mannequin, kitchen scale, loupe, lint roller, phone 240 fps | **KEEP** | — |
| Luggage scale, hygrometer | **DEFER** | tether/antistatic tests |
| STL / OpenSCAD files for every printed part | **ADD** to the package as a hard deliverable | — |
