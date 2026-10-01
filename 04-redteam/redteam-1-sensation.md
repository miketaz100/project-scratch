# RED TEAM 1 — SENSATION: Why SP1 FLOAT-ARM v0 will not feel like fingernails

**Project SCRATCH · 04-redteam · 2026-10-01 · Target: 03-tournament/LEADING-ARCHITECTURE-v0.md**
**Mandate:** prove the leading design wrong from the sensory side. Numbers are derived from the foundation documents (scratch-model, tip-interface, hair-interaction) and from the v0 geometry itself; every attack names its mechanism, probability, severity and fix. Where I think an attack is weak I say so.

## 0. The thesis in four sentences

The v0 synthesis took Team G's short-radius elbow arc but dropped the shoulder servo that made G's nail track the sphere, and took Team D's dead-weight float but dropped the head-centred pivot that made D's float stationary. The result is a float that must extend 7 mm and reverse its own direction at the middle of every stroke, an inclined float that converts scalp friction into extra normal force (N = 1.4–2.4 × dead weight at scalp friction coefficients), and a one-way 30 mm comb-stroke on one 50 × 40 mm patch delivered by a 0.6 mm edge at a line load that the tip-interface document itself classifies as a glide. Each of these alone degrades the sensation; together they make the default configuration a light three-tooth comb being drawn repeatedly down one spot of the head by a machine that the forehead can feel through the desk. The fixes are mostly cheap, and the ranked table at the end says which ones to make before the first human session.

---

## 1. Why it will NOT feel like fingernails — the readings it can produce instead

| Reading | Mechanism in v0 | P | Severity | Fix |
|---|---|---|---|---|
| **"A comb"** | Three parallel 0.6 mm edges at 20 mm pitch on a rigid carrier, drawn one way, with-grain, lifted return, same line every time. That is the definition of a wide-tooth comb stroke; hair-interaction §4.3 literally names comb teeth as the reference geometry. At 0.2 N/nail tip B is below the scratch window (§5 below), so the skin feels three teeth gliding, not three nails ploughing | 0.6 | major | bidirectional rake with the symmetric wedge tip; per-nail force ≥ 0.3 N; tip R 0.4 on a 4 mm loaded edge; yaw wander |
| **"A sweep / being petted"** | 30 mm one-way strokes at ~2 passes/s, with-grain by default (H-5.1). Humans do either bidirectional 1.5–4 Hz rakes (P1, 60 % of time) or 6–15 cm sweeps (P2, 20 %). A 30 mm one-way lifted stroke repeated every 500 ms is in neither category; it is a shortened P2 run at P1 cadence, a primitive not in the human ethogram (scratch-model §4.1) | 0.5 | major | both directions in contact (needs the wedge tip W) + against-grain short up-strokes at the occiput |
| **"A machine"** | (a) the 150 ms air return is a fixed-duration event the jitter does not touch — a metronome under the jitter; (b) XL330 gear mesh (two geared servos 15–25 cm from the ears) and the 2 Hz stroke reaction travel through the desk into the forehead cradle, so the forehead feels the rhythm; (c) every landing is a tap (§3); (d) one location | 0.7 | major | randomize return height/speed/pause; cradle on a separate stand or rubber-isolated; land at ≤ 25 mm/s or plough in while moving; yaw wander |
| **"A massager / pressure"** | Float friction-coupling (§4) raises N to 1.4–2.4× the dead weight on a sebum-rich scalp; at 100–140 g the heaviest nail sits at 0.9–1.8 N — pad-like pressure through a 0.6 mm edge; at 1.0 N a 0.6 mm edge is in the "." (pressure) region of the tip window chart | 0.4 | major | vertical float; constant-force spring instead of mass; ≤ 60 g |
| **"A brush / nothing" (riding the pile)** | At the 0.6 N minimum (0.2 N/nail) in medium hair the 12 mm-wide 45° plate collects hair ahead of the edge; scratch-model 3.14 gives 40–70 % skin contact in medium hair and this is UNKNOWN for Michael's hair. Against-grain strokes build the hair wave within ~25 mm and the nail rides up | 0.35 (medium hair) / 0.1 (short) | fatal if it happens | narrower edge (8 mm nail, 4 mm loaded), ≥ 0.3 N/nail, against-grain ≤ 25 mm with lift; measure contact fraction on the wand day 0 |
| **"Tapping / pecking"** | 60 ms controlled lower = 83 mm/s landing of a 60–200 g hand onto three 0.35 N/mm leaves: peak = v√(km) = 0.66–1.2 N for 12–22 ms, on top of the dead weight, twice per second at the same spot | 0.6 | minor-major | lower at ≤ 25 mm/s (0.2–0.36 N spike) or land while moving tangentially |
| **"Buzz"** | leaf + holder resonance ≈ 50 Hz (k 0.35 N/mm, 4 g tip mass) rings on every tap; servo gear ripple at 80 mm; both in the Pacinian band the model says "will dominate if the device vibrates" | 0.3 | minor | soft landing; damped (TPU-backed) leaf root |

The readings that matter most are the first two, because they are produced by the *default* primitive, not by a fault.

---

## 2. Does a rigid 3-nail carrier on one arc kill the "another person's hand" illusion?

What a human hand supplies that a rigid carrier cannot (scratch-model §4.2): per-finger landing spread 20–80 ms **re-drawn every stroke**, per-finger force ±30–50 % re-drawn every stroke, slightly converging (not parallel) paths because fingers curl toward the palm, direction wander ±15–30° and location wander because the wrist moves, four or five contacts, and the weight and warmth of a resting palm.

What the staggered-preload leaf gives instead: a **fixed** offset. The same nail lands first by the same interval with the same extra force on every stroke. The sensory system does not reward spread; it rewards unpredictability (the self-tickle argument, §4.3). A fixed stagger is learned in three to five strokes and thereafter contributes nothing to the "alive" quality that the model ranks third of five components.

Two quantitative problems with the stagger itself:

1. **Time spread and force balance are the same knob.** If the stagger is a height offset Δh and the hand lands at 30 mm/s, the time spread is Δh/30 mm/s and the force spread is k·Δh. For a 20–80 ms spread you need Δh = 0.6–2.4 mm, which at 0.35 N/mm is ±0.2–0.8 N — larger than the 0.2–0.3 N mean per nail. You cannot have human timing spread and human force balance from one passive leaf at this stiffness.
2. **If "preload" means a stop preload, the leaves lock.** With three stop preloads summing to 0.9 N (0.21/0.30/0.39 N) and a dead weight of 0.6 N, no leaf deflects at all; the hand is a rigid three-point rake until the float carries more than ΣP. Checklist item 9 (compliant at the tip) then fails at the lightest setting. v0 gives ratios, not absolute values; the condition is ΣP ≤ 0.5·W_min ≈ 0.3 N.

Does the "different leaf lengths → different resonances" idea restore independence? No. Leaf-tip resonance is ~50 Hz; changing free length 30→40 mm moves it between ~40 and 70 Hz. Nothing at 1–4 Hz changes; it only makes the three nails carry different forces and may add Pacinian-band ringing. Discard.

Is it enough to kill the illusion? My judgment: a rigid three-point rake with fixed stagger reads as "a tool with three points" with probability ~0.6, because at scalp two-point acuity (15–40 mm; prior-art §3.3) three contacts at 20 mm are only marginally resolved, so the "hand" percept is carried almost entirely by the temporal/force pattern across them — the one thing the carrier fixes.

**Minimum change that restores enough independence, in cost order:**

- **Yaw the carrier 15–20° relative to the stroke direction (cost: zero).** The nails are then staggered ~5 mm along the stroke, so on a tangential plough-in each nail enters the contact zone 30–50 ms after the previous one at 100–150 mm/s — and the spread changes with the per-stroke sampled speed, so it is re-drawn every stroke by the existing jitter. This is also how a real hand sits on a head (fingers are oblique to the stroke). It costs nothing and should be the default.
- **Per-nail micro-servo at the leaf root (3 × SG90, ~$10, 4 h, three PWM pins on the OpenRB-150).** Each servo lifts its leaf root 0–3 mm with per-stroke random timing and amplitude: true asynchrony, per-nail force jitter and a real P4 "spider" at 3–6 Hz, while tip spacing never changes (H-5.6 satisfied because only the normal direction is independent). Cost on the hand is ~27 g of float mass, which is why §4's lighter-hand fix matters.
- Two carriers out of phase (second elbow + second float, ~$80, 8 h) is not the minimum and doubles the float problems. Per-nail cams put rotation near hair; reject.
- Add the fourth nail (Judge 1 F2): +33 % follicle drive for one holder and 10 g.

---

## 3. Stroke kinematics

**Geometry.** ±18° of an 80 mm arm = 49.4 mm chord. Arc rise 3.9 mm; scalp sagitta over ±24.7 mm is 3.4 mm (R 90) or 4.4 mm (R 70). Because the pivot is above the scalp, the arc curves the *opposite* way to the head: the two add, and the float must extend **7.3–8.3 mm** per half-stroke and **reverse direction at mid-stroke** on every stroke. A 30 mm stroke needs 2.7 mm. The float has 20 mm, so reach is not the issue; what the float does with that motion is (§4).

**Attack angle vs local tangent — not a strong attack.** For a pendulum of radius r over a sphere R, the nail's angle to the local tangent drifts by θ(1 − r/R): ±2° on the crown, ±2.6° on the occiput at ±18°. The leaf end-slope adds ~2–4° of load-dependent tilt (δ = 1.5 mm on a 35 mm leaf gives 3.7°), which is the DIP-like modulation the judges want. Judge 1's F3 is correct; v0's 45° holder is fine on both regions.

**Lift-before-reversal latency.** Command → zero force requires: bus and servo latency (5–10 ms), tendon slack take-up (the tendon must carry ≥ 8 mm of slack at mid-stroke or it steals dead weight at the stroke ends, so 1–3 mm of margin plus whatever the float has already extended), float stiction breakaway, then 5 mm of lift (11.5° on a 25 mm horn; 19 ms at no-load, ~35 ms under 2–3.6 N of tendon load). Realistic total **50–80 ms**. v0 commands lift at 80 % of the stroke: for 30 mm at 100 mm/s that leaves 60 ms — marginal; at 150 mm/s, 40 ms — the nail reverses under load, violating DR4/H-5.2 and reinforcing the hair wave. Consequence: lift must be commanded at 60–70 %, contact duty falls to ~40–45 %, and the architecture's "1–3 Hz" is honestly **1–2 Hz** (D's own risk 3 said this).

**Contact duty and follicle drive.** 30 mm one-way at 2 passes/s × 3 nails × 10 hairs/mm = 1,800 hairs/s; with the earlier lift ~1,400. Human P1 is 2,000–4,000. Four nails bidirectional at 2 Hz is 4,800. v0 chose the configuration with the lowest drive of the available ones.

**Does 1–3 Hz on one patch habituate within 30 s?** A 50 × 40 mm patch engages roughly 20 cm² × 17 hair units/cm² ≈ 35 Aβ hair units plus field units; at 2 passes/s the same ~35 units are driven 120 times a minute while a human changes region every 5–20 s. Time jitter changes *when*, not *where*; SA1 and central gating adapt to where. My estimate: P(reads as "a machine on one spot") ≈ 0.4 by 30 s, ≈ 0.8 by 2 min. The ±11 mm start-drift available inside a 52 mm arc for a 30 mm stroke is one-axis and 22 mm wide; it does not count as region change.

**Unidirectional raking = sweeping.** See §1. The air return also makes the rhythm a metronome: the return is 150 ms at servo max speed regardless of the sampled stroke parameters.

**Direction.** v0 inherits H-5.1's with-grain default. At the occiput that is a crown→nape down-stroke. Hair exits at 10–30°; a 45° plate moving with the lean lifts each hair from ~20° to ~45° (≈ 25° of root deflection); moving against the lean it folds the hair from +20° past −45° (≈ 65°): **2.6× the follicle moment per hair**, which is why humans scratch the occiput with short up-strokes (scratch-model §5, "vigorous P1 rakes, up-strokes against the lie") and why hair-interaction permits against-grain ≤ 25 mm with lift. v0's default at the sweet-spot region is the lowest-drive direction. On the crown (radial whorl) outward with-grain is fine. The fix is a remount and a sign flip: zero cost.

---

## 4. Force: what the scalp actually feels per nail

**The inclined float converts friction into normal force.** D's float travel is inclined 30° from the scalp normal so that retraction is up-and-forward. Resolve forces on the free hand along the float axis: N·cos30° = m·g·cos30° + F_drag·sin30°, so **N = mg / (1 − tan30°·μ)**. On a sebum-rich scalp μ is 0.6–1.0 (tip-interface §2.6):

| μ | 0.3 | 0.5 | 0.7 | 1.0 |
|---|---|---|---|---|
| N / dead weight | 1.21 | 1.41 | 1.68 | 2.37 |

So the "mechanical constant independent of servo torque" is a function of friction, and a snag (which raises drag) raises the normal force that pins the strand — the same positive-feedback "dig" Judge 1 caught in Team C's leaf orientation (F6), reproduced one level up. The 2.0 N red-line cap becomes 2.8–4.7 N total at μ 0.7–1.0. Inclining the other way gives N = mg/(1 + 0.577 μ) = 0.63–0.85 mg: self-limiting, like a finger. A vertical float gives N = mg exactly. The leaves' own "drag lifts the nail" orientation does not rescue this: leaf deflection only redistributes force between nails; the total is set at the float.

**Per-nail force at the nominal settings**, including friction coupling (×1.4–1.7), inertial ripple (§ below, ±5–25 %) and the stated 0.7/1/1.3 spread: at the 0.6 N setting the heaviest nail sees 0.35–0.55 N (in window); at 1.0 N, 0.6–0.9 N; at 2.0 N, 1.2–1.8 N — three times the model's "pleasure does not scale above ~0.5 N" ceiling and the 0.6 N comfort limit. The usable dead-weight range is therefore ~40–80 g, not 0–140 g, until the float is fixed.

**Inertia.** With a trapezoid profile the float's vertical acceleration during the constant-velocity plateau is c·v² with c = 1/r + 1/R = 23.6 m⁻¹: 0.24 m/s² at 100 mm/s (2.4 % of g), 0.53 at 150 (5 %), 0.94 at 200 (10 %) — a uniform force *reduction*, modest. With the minimum-jerk profile the hybrid specified, peak velocity is 1.9× mean: a 30 mm/250 ms stroke peaks at 225 mm/s (12 % dip at mid-stroke), 50 mm/300 ms at 312 mm/s (23 %). So this attack is **minor with trapezoids, major with min-jerk at long strokes**; it argues for a light hand and the trapezoid, not for abandoning the float.

**Stiction → stick-slip at mid-stroke, every stroke.** This one is geometric and unavoidable with a pivot above the scalp: the gap is minimum at mid-stroke, so the float's velocity (ż = c·x·v: 59 mm/s at the stroke ends, 0 at the centre) passes through zero at the centre of every stroke. Stiction re-engages there and the force steps by 2·F_friction. A printed bearing parallelogram with a load cell, a tendon guide and a magnet detent in the chain has 0.05–0.15 N of breakaway (D's own risk 1 allows 0.6–1.0× the setting, i.e. up to 0.4 N at 1 N). That is a 10–60 % force step in the middle of every stroke at the 0.6 N setting. Only a concentric arc (pivot at head centre — D's yoke) removes the reversal; a flexure parallelogram (two 0.2 × 12.7 mm feeler leaves, 80 mm long, ~$3, 1 h) removes the stiction.

**Does the parallelogram's constant force follow curvature?** Yes along the float axis, but across the three nails only the leaves do, and §2 showed they may be locked by preload.

---

## 5. The tip

**0.6 mm at the stated force is a glide, by the tip document's own window.** The scratch window (tip-interface §2.5) is edge radius 0.2–0.6 mm at line load 0.05–0.15 N/mm. v0's per-nail force is 0.2–0.65 N over a 6 mm loaded edge:

| F per nail | 0.2 N | 0.3 N | 0.4 N | 0.65 N |
|---|---|---|---|---|
| line load (6 mm edge) | 0.033 | 0.050 | 0.067 | 0.108 N/mm |
| tip B (R 0.6) reads as | glide | borderline | scratch | scratch |
| tip A (R 0.3) reads as | glide | scratch | scratch | scratch |

The scratch-model's typical 0.15–0.3 N per nail and the tip window overlap only at the top end, and only with tip A. v0 starts with tip B at a total of 0.6 N: 0.033 N/mm, inside the "~~ stroke/glide" region. Tip B's own description says "may become a stroke below 0.5 N". A 0.6 mm full-round edge on a 1.2 mm body is also thicker than any fingernail (0.35–0.5 mm) and is exactly the radius of a comb tooth, which is how it will read in combination with §1.

Resolution of the safety/tip conflict that does not sacrifice the sensation: **R 0.4 mm (meets red line 11) on a 4 mm loaded edge** — an 8 mm-wide press-on nail with R 9 transverse curvature touches the scalp over ~3–4 mm, so 0.3 N gives 0.075–0.1 N/mm, mid-window. That is tip C's logic (nail corner) at the safety radius; the first dozen can be made from press-on nails in an afternoon.

**45° at the occiput where hair exits at 10–30°.** The angle is not the problem (§3): with-grain the hairs slide up the 45° plate and off; against-grain the plate folds them and the wave builds, which is why against-grain is limited to 25 mm. What *does* put the nail on top of the hair is the plate's **width**: a 12 mm plate presents a 12 × 8 mm ramp that collects a bundle in medium hair at 0.2 N. Narrower (8 mm) nails and ≥ 0.3 N per nail are the fix, and the day-0 wand must photograph contact fraction from the side (hair-interaction 7.3.1) in Michael's actual hair before any force setpoint is trusted.

---

## 6. Spatial variation

One 50 × 40 mm patch with manual re-aim is the single largest sensation failure and it is baked in. Beyond habituation (§3), it violates two foundation rules by construction:

- **H-5.5 dwell limit** (≤ 8 strokes per ±15 mm patch, then relocate ≥ 20 mm): with 22 mm of one-axis start drift there is nowhere to relocate to; the firmware rule cannot be satisfied without a hand on the arm.
- **Scratch-model 3.24** (no spot > 50 passes/min): each nail path in the patch receives 120 passes/min at 2 passes/s. Matting (hair §3.5) starts at 10–20 un-lifted passes in one spot; v0 lifts, which helps, but backcombing of a fixed 50 mm line for five minutes is a real risk if any against-grain strokes are used.

Cheapest ways to add wander, ranked:

1. **Let the head move (cost zero).** The float (20 mm) and leaves (8 mm) tolerate ±15 mm; invite Michael to roll the head slowly ±15° on the cradle during episodes. Location becomes self-generated and slow while scratch timing stays machine-generated, so attribution is only partly lost. The dead-man stays closed. Do this in session one regardless.
2. **A yaw servo at the elbow (XL330 $27, printed bracket, ~3 h).** Rotate the whole elbow module about the vertical axis through the elbow pivot, in the air only (H-5.7 forbids in-plane rotation of a multi-tine head in contact). A 50 mm stroke rotated through ±45° sweeps a ~50 mm disc, and it supplies the ±15–30° **direction wander** that every design in the tournament lacked and that cross-grain-at-varying-angle strokes need. Combined with the ±11 mm start drift this turns the patch into ~70 mm.
3. **Programmed start drift alone** is already in v0 and is insufficient (one axis, 22 mm).
4. A slow second axis on the monitor arm is not credible — gas-spring arms are not actuators.
5. D's 250 mm yoke band is the complete answer but is a different mount (§7 and §8).

---

## 7. Posture

**Forehead on a cradle, scratching the occiput/crown, seated.** The forehead carries 10–20 N over ~48 cm² (2–4 kPa, D's estimate). The forehead is the most densely innervated hairy-skin site on the body (48 Aβ units/cm², 3× the scalp): a sustained 15 N there is a slowly adapting pressure percept that sits in the model's "massage/deep pressure" column and competes with the scratch for attention. The posture is neck flexed 20–30°, eyes down — a dentist or massage-table context, not "head in someone's lap". Component E (social attribution) is ranked last, so I do not call this fatal; but two mechanical consequences are:

- **Gravity no longer points along the occipital normal.** With the head flexed 30–45°, the occiput's normal is 45–60° from vertical: the dead weight delivers 0.5–0.7 of its value along the float axis and 0.7–0.87 of it *tangentially* (0.4–1.7 N), which sits permanently on the 0.8 N wrist detent (broken in one direction, rigid in the other) and loads the parallelogram sideways. D solved this with 45° flexion plus a trim spring, i.e. the force reference becomes a spring again. The dead-weight float is a crown-with-upright-head device; for the occiput it wants the head flexed ~90° (prone face-cradle, the actual massage posture, where breathing drift of 5–15 mm is inside the float's 20 mm).
- **The forehead dead-man cuts power when the head shifts, with the hand down.** v0's fail-safe is limp-at-dead-weight. Every yawn, swallow or settle that decompresses the pad by > 8 mm stops the elbow mid-stroke and leaves three loaded nails stationary on the skin (forbidden > 1 s by PATTERN SPEC GLOBAL and H-5.5), then restarts under load when contact resumes (violating H-5.9 "start lifted"). Each such event is a snag-class sensory interruption. Fix: 300–500 ms debounce, "resume = lift first" in firmware, and D's electromagnet-latched spring lift ($8, 2 h) so the de-energised state is lifted.

**Better postures.** Crown: seated upright, elbow on the desk, chin in the hand or on a slit-lamp-style chin rest — forehead free, head free to roll, gravity vertical on the vertex. Occiput: prone with a face cradle (gravity along the occipital normal, the one posture where the dead weight works as designed) or reclined ~30° with a cervical pillow under the neck (occiput exposed, truly relaxed, dead-man as a pressure switch in the pillow). Seated-forehead-on-bar is the worst of the three for the occiput and middling for the crown.

---

## 8. The massager test (scratch-model §8), item by item

| # | Item | Verdict | Reasoning |
|---|---|---|---|
| 1 | Edge, not pad | PASS | 0.3–0.6 mm radius keratin-class edge; but see 3 |
| 2 | Reaches the skin ≥ 40 % at ≤ 0.3 N in 5–10 cm hair | UNSURE → FAIL in medium hair at 0.2 N/nail | 12 mm plate collects a bundle; contact fraction UNKNOWN (3.14); nothing in v0 measures it before the force setpoint is chosen |
| 3 | Light (0.05–0.5 N per contact, ceiling 0.6 N) | FAIL above ~80 g | friction coupling ×1.4–1.7 plus the 1.3× nail puts the heaviest nail over 0.6 N from ~80 g upward; at 2.0 N it is 1.2–1.8 N |
| 4 | Slides ≥ 10 mm with slip | PASS | 0.2–0.5 N cannot move the scalp; 30–50 mm slip |
| 5 | Right speed band, no > 20 Hz component | PASS/UNSURE | 50–150 mm/s, 1–2 Hz; but 12–22 ms landing taps at 0.7–1.2 N, 50 Hz leaf ringing and gear ripple are all Pacinian-band |
| 6 | Deflects hair near the root | PASS if 2 passes; halved by with-grain default at the occiput |
| 7 | Multiple independent contacts, ≥ 20 ms / ≥ 20 % spread, not phase-locked | FAIL as drafted | fixed stagger is phase-locked by definition; "UNSURE acceptable if deliberate experiment" only if v0 declares it one |
| 8 | Irregular in length, speed, force, direction, location | UNSURE | time-domain jitter PASS; direction 0°, location one axis × 22 mm: FAIL |
| 9 | Compliant at the tip ≤ 0.5 N/mm, ≥ 5 mm | UNSURE | PASS at zero preload; FAIL if stop preloads sum above the dead weight (unspecified) |
| 10 | Unloads at reversal, lifts between bouts | PASS ≤ 2 Hz / FAIL ≥ 2.5 Hz | 50–80 ms lift latency vs 40–60 ms available |
| 11 | Hair-safe geometry | PASS | nothing rotates within reach; TM1 seams sleeved |
| 12 | Sounds like a scratch, not a motor | UNSURE → likely FAIL | two geared servos 15–25 cm from the ears on a desk shared with the forehead cradle; no isolation specified |

Two FAILs among items 1–6 (2 and 3), both configuration-dependent. By the model's rule, as drafted and at the default settings, v0 does not clear the gate.

---

## 9. The bet

Decompose "yes, that is someone scratching my head" on the first good session into independent gates: the edge reaches skin and feels nail-like on the wand (0.7, de-risked by the day-0 wand); per-nail force actually in the window with tip B and the float as drafted (0.55); the motion signature reads as raking rather than sweeping/combing (0.5); no machine attribution from taps, metronome return, desk conduction and the single patch inside a 5-minute session (0.6). Product ≈ **0.12; call it 15 % (range 10–20 %)**.

The first 10–20 seconds decide the rating, and they are decided by contact physics and the motion signature, not by habituation. So the single change that raises the probability most is to **make it rake, not sweep**: both directions in contact with the symmetric wedge tip (Team C's tip W; one holder variant, ~1 h), a force dip and 5 mm lift at each reversal (the lift axis already exists), and against-grain short up-strokes as the occiput default. That is the canonical human P1 primitive; without it SP1 is performing a primitive humans do not use. I estimate it moves the probability to ~30 %. The second change (vertical flexure float, ≤ 60 g, tip R 0.4 on a 4 mm edge at ≥ 0.3 N/nail) moves it to ~40 %; the third (yaw wander + carrier yaw stagger) is what keeps the "yes" past minute two.

A note on the simpler alternative the brief asks about: the day-0 hand wand with Michael moving it is the first real test and will answer most of §5 before any motor turns; if the wand feels right and the machine does not, the gap is motion signature and independence — which argues for D's W1 Resting Hand (tendon-curled fingers with independent timing, warmth and weight) as the SP2 hand on the same float, not for a different frame.

---

## RANKED ATTACK TABLE

| Rank | Attack | Severity | Likelihood | Recommended fix | Cost |
|---|---|---|---|---|---|
| 1 | One-way 30 mm lifted strokes read as comb/sweep; follicle drive 1,400–1,800 hairs/s vs 2,000–4,000 human; occiput default direction is the lowest-drive one | fatal to "scratch" attribution | 0.5–0.6 | bidirectional rake with symmetric wedge tip W, lift-dip at both ends, against-grain ≤ 25 mm up-strokes at the occiput; 4th nail | wedge holder + 4th holder ~$5, 2 h; firmware 2 h |
| 2 | Inclined float converts friction to normal force: N = 1.4–2.4× dead weight at scalp μ 0.5–1.0; cap becomes friction-dependent; snags dig | major (safety-adjacent) | 0.8 (it is geometry) | vertical float travel, or incline the other way (N = 0.63–0.85 mg) | reprint carrier housing, ~$5, 2 h |
| 3 | Tip B at 0.2–0.3 N/nail over 6 mm is 0.033–0.05 N/mm: a glide by the tip window; reads as a 3-tooth comb | major | 0.7 at the 0.6 N default | first scalp tip R 0.4 mm on a 4 mm loaded edge (8 mm press-on nail); per-nail ≥ 0.3 N; keep tip B as the "gentle" arm | $2, 1 h |
| 4 | Single 50 × 40 mm patch: habituation (P 0.4 at 30 s, 0.8 at 2 min); violates H-5.5 and 3.24 (120 passes/min) by construction | major | 0.8 | invite head roll (free); yaw servo at elbow for ±45° direction/location wander in the air | $27 + 3 h |
| 5 | Fixed 0.7/1/1.3 stagger is phase-locked; time spread and force balance share one knob; stop preloads may lock the leaves below ΣP | major for "hand" illusion | 0.6 | yaw carrier 15–20° (free); 3 × micro-servo leaf-root lift for per-stroke random timing/force; specify ΣP ≤ 0.3 N | $0 / $10 + 4 h |
| 6 | Float must reverse at mid-stroke every stroke (pivot above scalp) → stiction step of 2F_f = 0.1–0.4 N at stroke centre | major at ≤ 1 N settings | 0.7 | flexure parallelogram (two 0.2 mm feeler leaves, zero stiction); geometric cure is D's head-centred yoke | $3, 1 h / ~$40, 5 h + new mount |
| 7 | Forehead dead-man + limp fail-safe: each head shift leaves loaded nails stationary then restarts under load | major (sensory interruption every few minutes) | 0.7 | 300–500 ms debounce, resume-with-lift, electromagnet-latched spring lift | $8, 2 h + firmware 1 h |
| 8 | Landing tap 0.7–1.2 N for 12–22 ms twice a second; 50 Hz leaf ringing | minor–major | 0.6 | lower at ≤ 25 mm/s or plough in while moving; TPU-backed leaf root | firmware; $0 |
| 9 | Desk-shared cradle conducts XL330 gear mesh and 2 Hz reaction into the forehead; servos 15–25 cm from ears | major for "machine" cue | 0.6 | cradle on its own stand or rubber-isolated clamps; servo muffs; measure dBA at the ear | $15, 1 h |
| 10 | Lift latency 50–80 ms vs 40–60 ms available at ≥ 2 Hz: reversal under load, duty ~40 % | major above 2 Hz | 0.8 | lift at 60–70 % of stroke; cap SP1 at 2 Hz; smaller horn radius; electromagnet release | firmware |
| 11 | Dead weight off-axis at the occiput with a flexed head (0.5–0.7 normal, 0.4–1.7 N tangential on the detent) | major for occiput sessions | 0.9 | crown first with chin rest; occiput prone or 90° flexion; disable detent for occiput | $0–20 |
| 12 | Metronome air return (fixed 150 ms) survives all jitter | minor | 0.8 | randomize return height, speed, pause | firmware |
| 13 | Float inertia ripple (2–10 % trapezoid, 12–23 % min-jerk) | minor | 0.5 | trapezoid in contact; hand ≤ 60 g; part of the force from a constant-force spring | $8, 1 h |
| 14 | Monitor-arm bounce (400–450 g module, ~4–7 Hz natural) at 2 Hz stroke | minor–major | 0.5 | reach-stop ring, shortest arm extension; 2020 cage if bounce > 2 mm | $0 / $40 |
| 15 | Attack angle drift ±2–3° vs local tangent | not an attack | — | none; v0 is right | — |
