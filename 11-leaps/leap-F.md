# LEAP F — Radically different architectures (anything goes)

**Project SCRATCH · 11-leaps · Agent F · 2026-10-01**
Provocation: make the strongest case for at least four architectures no earlier round took seriously. Judge them on the scratching experience first and plausibility second.
Read: brief-listed foundations, DECISION, redteam-1, porcupine brief/pin-unit, 02-mechanisms heads (incl. D's W1 "Resting Hand", G's rejected "Bowden spider"). Firewall kept.
Tags: [K] = from the foundation documents · [E] = my estimate, derivation shown · [U] = only a test can say.

---

## 0. The assumption every design so far shares

Every architecture since the first desk arm has kept three beliefs:
1. **The force reference is a structure.** Nail force comes from a spring or a dead weight on a float registered to a frame (desk arm, C-arm) or a helmet (crown, porcupine). The program's hardest fights all come from this: ±3–5 mm seating slop, the 40 mm-long 0.02 N/mm spring, the 180 mm tower, the 500 g limit.
2. **Coverage takes a structure as large as the area covered:** a head-spanning yoke, or a helmet with dozens of pins.
3. **The machine carries the contacts; the contacts never carry the machine.**

Suppose all three are false. The head is an upward-facing dome, and anything resting on it presses with its own weight: no drift, no seating, follows the head, hard ceiling. A hand's worth of scratch force is **3.5 nails × 0.3 N ≈ 1.05 N = the weight of 107 g** [E], about a deck of cards. The tournament's winning idea was "force = dead weight"; taken to its limit the dead weight needs no rail. **The dead weight is the hand**, and it can carry its own actuators, because here **mass is a budget you must spend, not a limit**. Humans do the same: scratch-model §3.3 counts "0–3 N of resting palm/finger-pulp weight".

A, B and C follow from this inversion. D and E attack a different shared belief: that the pattern (rank 1, §7 priority 25) must be hand-written in firmware, and that the machine must replace the human. §F dismisses three named candidates with numbers.

**Gravity's one limit, stated once.** A free body on nail feet (μ ≈ 0.35, §3.4) holds position up to atan 0.35 ≈ 19° of slope; with a leash or strings giving uphill support, to about 45°, where normal force is cos 45° ≈ 0.7 of weight (less a little leash pull). A 45° cap on an R 90 head is 2πR²(1 − cos 45°) ≈ **150 cm² per posture** [E], about 25–30% of the hair-bearing scalp. Posture picks the cap: upright → crown/top; leaning forward into the face cradle SP1 already has → crown/occiput, the "sweet spot" (§5); side-lying with the head in a lap (the classic being-scratched posture) → one parietal side. A bonus: upright, force falls as cos θ on the sloping sides, which is the human rule "force drops ~50% going from occiput to temple" (§5) [K].

---

## A. LEASHED SCALP SPIDER — a hand that walks (best bet)

**Breaks:** beliefs 1, 2 and 3. Force is gravity, coverage is locomotion, the stroke is the gait.

**Principle.** A smooth 100–130 g dome, 60 mm across, stands 35–40 mm above the scalp on **six legs**. Each leg is one smooth music-wire stalk (0.8–1.0 mm, ~45 mm) ending in a TM1-style nail foot (edge R 0.3–0.4 mm, 4–6 mm wide, 45° attack), swung by **its own 4 g sub-micro servo** about a hip axis sealed inside the dome. The foot's arc is concave-up and the scalp convex, so **each leg lifts off by geometry at both ends of its swing**: FLOAT-ARM's winning trick (DECISION §3), now per leg. With L = 40 mm over R = 90 mm, gap = L·θ²/2·(1 + L/R) = 28.9·θ² mm. With 3 mm leg-spring engagement the foot touches over ±18.5° (a **25 mm chord**) and is **5.5 mm clear** at ±25° [E]. Reversal happens in the air, so DR4/H-5.2 hold by construction. A light leash (2 × 28 AWG silicone, ~2 g/m) from a short post on a soft headband over the vertex, or from a boom, carries power and mechanically fences out the face and ears.

```
            leash (power + range limit) from post/boom above the vertex
                 \
          ___.----\----.___        dome 100-130 g, smooth, drafted, >=35 mm tall
         /  [s1] [s2] [s3] \       6 sub-micro servos = ballast = force budget
        |___[s4]_[s5]_[s6]__|      hips sealed inside, >=35 mm above scalp
          /  |   |   |   |  \
         /   |   |   |   |   \     one spring-wire stalk per leg, no knee in the hair
   hair ~~\~~~|~~~|~~~|~~~|~~/~~~
   scalp ──▼──▼───(▼)──▼──▼──▼──   nail feet; any 3-4 in contact carry the weight
            <-25 mm->   each leg arcs and lifts 5.5 mm at both ends
```

**Gaits are scratch primitives.**
- *Relocate (P6):* stance legs sweep the same way, feet grip, the body walks and lands softly.
- *Scratch (P1):* stance legs sweep against each other (front pulls back, rear forward, like fingers curling toward a palm); the friction forces cancel, so every foot must slide.
- *Sweep (P2):* the robot pulls against the leash and stance feet slide in parallel away from the anchor. From a vertex anchor every such stroke is radial from the crown whorl, i.e. **with-grain everywhere** (H-5.1) [E].
- *Spider (P4):* independent random leg phases at 3–6 Hz, 5–15 mm, the model's highest-unpredictability tingle driver.

**Why it could step-change the sensation.**
- *Force (ranks 3, 7):* per foot mg/n_contact = **0.29–0.39 N** at 120 g with 3–4 feet down [E]: upper end of the 0.15–0.3 N typical, inside the 0.05–0.5 N envelope and tip-interface's 0.3–0.9 N window (ballast is the knob). The contact set changes every phase, so force varies **±25–35%, re-drawn every step** (§4.2 asks ±30–50%). Nods add ±10–30%. There is no seating slop: it rides the head.
- *Irregularity, asynchrony (ranks 1, 6):* red team 1 (§2) showed a fixed stagger is learned in 3–5 strokes. Here every foot has its own actuator and random phase, so landing spread is re-drawn every cycle. It is the only architecture where per-contact actuators cost nothing in force terms: their mass is ballast the force budget needs anyway.
- *Follicle drive (A):* 3.5 feet × 25 mm each way at 2 Hz = 3.5 × 100 mm/s × 10 hairs/mm ≈ **3,500 deflections/s** [E], against human P1's 2,000–4,000 and FLOAT-ARM v0's 1,400–1,800 (redteam-1 §3).
- *Region wander (§4.2, H-5.5):* free. It walks 20–60 mm between bouts; dwell and adjacency become path planning.
- *Context (E):* a warm, weighted thing moving by itself on your head may carry "someone is doing this" better than a buzzing helmet [U].

**Independence and coverage.** Six independent contacts, 3–4 active at 25–40 mm spacing. ~150 cm² per posture within the leash radius; three postures cover crown, top, occiput and upper sides. Nape and temples stay a later low-force experiment, as §5 advises.

**Hair safety.** Walking natively obeys the hard rules: stance is a one-direction stroke, swing is in the air, every reversal is lifted (H-5.2/5.3/5.7). No rotation within 30 mm (hips sealed ≥ 35 mm up). No knee, gap or seam in the canopy (H-4.4, H-4.9). Music-wire legs give ~0.3 N/mm tangential yield (H-4.11). The robot itself is a 120 g breakaway: a captured strand sees at most ~μ·mg ≈ 0.4 N plus leash tension before the robot is dragged or lifted. **It bends H-5.6:** in scratch mode opposed feet converge (~70 → 50 mm) while in contact, as curling human fingers do. Spacing never nears the 3 mm danger band, but it needs a wig test first.

**Plausibility.** *Torque:* a 0.3 N plough spike at 40 mm is 12 N·mm; a 4 g servo gives ~78 N·mm (0.8 kg·cm), 6× margin, and up to 400 mm/s at the foot against 50–150 needed. *Mass:* servos 24 g, ESP32-C3 3 g, IMU 1 g, dome 25 g, legs 12 g, leash 5 g = 70 g; ballast to 110–130 g. *Cost:* ~$60–90, no battery (leash power). *Sensing:* the IMU knows the slope, hence roughly where on the head it is, and refuses > 50°; servo current flags snags per leg. *Precedent:* hobby micro-hexapods exist; the new part is a gait designed to slip, not grip.

**Cheapest experiment (< $50, one weekend).**
1. *Passive gravity puck ($10, one evening).* Printed 60 mm dome, four to six 0.8 mm wire legs ending in press-on nails cut to 5 mm, ballast at 80/110/140 g. Rest it on the crown; a helper (not Michael: self-touch is attenuated) drags it by a thread and rocks it with a chopstick. This answers the question A, B and C share: **do gravity-loaded nails at 0.2–0.4 N reach the skin through Michael's hair and read as nails?** Count snags on a dark cloth.
2. *One live leg (~$15).* One servo swings one leg ±25° with Arduino-random timing while passive legs carry the dome. Measures geometric lift on a real scalp, whether one leg reads as a nail, and **bone-conducted servo noise**.
3. *$0 pre-test.* A helper does P4 wiggle vs P1 rake on Michael, blind, 10 trials each. A clear P4 win strengthens the spider case.

**Replaces / combines.** Replaces the porcupine's helmet, pins and selector, and FLOAT-ARM's float, rail and yoke. Keeps TM1, the hair rules, the pattern engine (now per leg), and hold-to-run/e-stop on the leash. Falls back to B: the same puck works under strings.

**Honest killer risks.** (1) **Riding the canopy:** 0.3 N of gravity may skate on dense medium hair where a human adds a directed push; step 1 retires it in an evening. (2) **Bone-conducted servo whine:** six cheap servos with feet coupled to the skull carry 1–4 kHz gear noise and PWM hold-buzz, the "machine" reading (§8 item 12). Mitigations: spring-wire stalks as a low-pass, digital servos with deadband, power cut to idle legs. (3) **Creepiness and the face fence:** some people will hate it, and the leash must make the eyes and ears physically unreachable.

---

## B. HEAD POLARGRAPH — a gravity puck steered by three strings

**Breaks:** beliefs 1 and 2. A's conservative sibling, built from proven tech: a string "wall plotter" turned onto a dome.

**Principle.** A 100–120 g smooth puck carrying 3–4 TM1 nails on independent leaves rests on the head. Three 0.2 mm Dyneema lines (no stretch) run from its top, ≥ 30 mm above the scalp, to spools on a ring ~200 mm out and 50–80 mm above the head top. Three motors (NEMA17 + TMC2209, silent in StealthChop; or STS3032) set line lengths: two tangential DOF plus **lift**. Shortening all three lifts the puck at every reversal and region change, and the pay-out rate is the landing ramp. Lines tied to three rim points add yaw.

```
     spool 1 ●                      ● spool 2      (ring/tripod, motors off-head)
              \    PUCK 110 g      /   lines enter puck top >=30 mm above scalp
               \  .----------.    /
                \/  ▼   ▼   ▼ \  /    3 nails on leaves; gravity = force
      hair ~~~~~~~~~~~~~~~~~~~~~~~~~~
      scalp (crown, or occiput in the face cradle)        ● spool 3 (behind)
```

**Why it could step-change the sensation.** The yoke's region wander and long P2 sweeps (≥ 100 mm, any direction, so direction vs hair lie is free per stroke, rank 8), on a puck that cannot over-press: the ceiling is mg. The head moving under world-fixed strings changes where the puck lands, not how hard it presses. **Position does not need precision (cm-scale receptive fields, §2.2); force does, and gravity supplies it.** Weak point: the nails are a rigid group, so asynchrony needs red team 1's leaf-root micro-servos, whose 10–30 g is welcome ballast.

**Independence and coverage.** 3 (or 4) contacts; a ±40–45° cap, ~120–150 cm² per posture. Lines must stay ≥ 30 mm off the scalp, which limits going "over the top" from a far spool; enforce it as a firmware workspace.

**Hair safety.** Only the puck touches hair (smooth drafted underside, FLOAT-ARM hand rules). Lines run above the exclusion zone. Nothing rotates on the head; no apertures. Pull on a snag is bounded by line tension (firmware ~1.5 N, spool slip-clutch for a mechanical cap).

**Plausibility.** Drag μN ≈ 0.35 × 1.1 ≈ 0.4 N, plus ~0.2 N to reverse 100 g at 2 m/s². At 20° line elevation this lifts 0.15–0.2 N of the 1.1 N weight: a 15–20% direction-dependent force change, predictable, so it can be compensated or kept as jitter. Lifting 5 mm in 50 ms needs ~0.4 N extra. String plotters run ≥ 200 mm/s. Cost ~$90–130.

**Cheapest experiment.** A's passive puck, then three 28BYJ-48 steppers ($12) on 40 mm spools on a cardboard ring, run in the face cradle at 20–60 mm/s (the CT-optimal band, as it happens). Under $35. Asks: do string-steered gravity strokes feel deliberate or "dragged"?

**Replaces / combines.** Replaces the helmet, or the SP2 C-arm yoke. Reuses the FLOAT-ARM hand minus float, rail and weight post: the hand becomes the weight.

**Honest killer risk.** **It may feel towed.** The nails trail the attachment point and attack angle depends on line direction, so strokes may read as an object pulled across the head, not fingers raking. Pendulum swing on lifts and tension-to-normal coupling add a machine signature. And the workspace is world-referenced, so Michael must stay in the cradle.

---

## C. CRAWLING RESTING HAND — soft tendon fingers, motors on the desk

**Breaks:** beliefs 1 and 3. Team D floated W1; Team G rejected the Bowden version because "tendon friction/hysteresis (10–20%) kills force fidelity". **That objection disappears once gravity sets the force:** the tendon sets only curl (position and timing), where hysteresis is just more jitter.

**Principle.** A 150–200 g printed hand rests on the head: a satin-over-foam palm with a hand-warmer sachet, four TPU living-hinge fingers (e-NABLE/Flexy-Hand-style) with press-on nails, and four PTFE/Dyneema Bowden tendons hung slack from a boom to four desk servos. Pulling a tendon curls a finger so its nail drags 20–30 mm toward the palm: P1 the way a hand does it, with **converging** paths (redteam-1 §2). An elastic return extends it.

```
   desk: [srv][srv][srv][srv] ==== 4 Bowden tendons, hung slack from boom ====.
                     palm pad (warm, 150-200 g)  ____________                  |
          ,---------------------------------(heel)           )<-- tendons enter on back
         /  finger (TPU hinges, no pins)  curl ->
  ~~~~~▼~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ hair     nail drags 20-30 mm toward the palm
```

**The force cap is a lever.** Curl torque reacts against the hand's weight, so before the heel lifts, total nail force ≤ W·(heel→CG)/(heel→nail) = 1.8 N × 40/110 = **0.65 N for all curling fingers together** [E]: ≤ 0.65 N on one nail, ~0.16 N each with four. That is a mechanical constant set by ballast placement, whatever the tendon does. On release, curl torque vanishes and the return drags at preload (~0.02–0.05 N), so **force drops > 90% at every reversal** (DR4) with no lift mechanism. For the nails to slip rather than the palm: palm 1.2 N × 0.3 = 0.36 N > nails 0.6 N × 0.35 = 0.21 N [E]. With a slicker palm the hand **crawls** toward its fingertips instead (inchworm region change from the same four actuators).

**Why it could step-change the sensation.** It is the only candidate that delivers component E (palm weight plus 32–34 °C warmth: "a hand is resting on me") together with converging, independently timed fingers (P1 + P4), and it has no actuator on the head, so no bone-conducted whine.

**Independence and coverage.** Four fully independent fingers; one ~60 × 80 mm patch per placement, slow crawl, otherwise posture or B's strings.

**Hair safety: the weakest of the five.** Living hinges in the canopy must be gap-free TPU (H-4.9). Worse, **a finger curling toward the palm closes an aperture**, so hair swept into the crease can be pinched. Stop the curl with the nail ≥ 15 mm from a drafted palm skid, and end the tendon housings on the back of the hand.

**Plausibility.** e-NABLE hands are mature, free and print in TPU in a day; four servos plus an Arduino cost $20–60. Bowden loss over 90° with PTFE (μ ≈ 0.1) is ~15%, irrelevant here. The real issue is **housing stiffness shoving the hand**: four slack 2 mm tubes from overhead keep side load ~0.1 N [E], below the 0.36 N palm friction.

**Cheapest experiment (~$25).** One TPU finger-and-palm segment, 150 g ballast, a hand warmer; a helper pulls the tendon by hand with random timing. Then four fingers on desk SG90s against the A/B puck.

**Replaces / combines.** Replaces head-borne actuation. It can be B's end effector (strings move the hand, tendons curl the fingers).

**Honest killer risk.** **Crease pinch and canopy gaps:** soft fingers are the most hair-hostile geometry here, and the hand may comb hair into the palm. One patch at a time.

---

## D. DESK ARM + DEMONSTRATION LIBRARY (and why the "real robot hand" is wrong)

**Breaks:** the hidden belief that a scratch pattern can be *specified*. Here it is *recorded*. **Principle:** an open-source leader–follower arm (LeRobot SO-101 class, ~$250 follower + ~$120 leader; verify) behind the face cradle carries the FLOAT-ARM hand on its dead-weight float. A partner scratches Michael *through* the robot via the leader; the follower logs 50 Hz trajectories; the pattern engine replays re-sequenced, ±20% time-warped, mirrored, region-shifted 2–10 s segments, so the rank-1 variable carries real human statistics (§4.2: ±25–35% length, ±20% speed, ±15–30° direction) instead of a hand-written jitter table. **Robot hand:** open dexterous hands (~400 g, 8 micro-servos, e.g. Pollen's AmazingHand) sit at hobby-arm payload limits, are stiff and position-controlled, and would need leaf compliance anyway; P4 is cheaper as three leaf-root micro-servos. Arm yes, dexterous hand no. **Sensation:** crown/occiput/upper sides, any direction, landing ramps, human-statistics patterns (the best answer to §4.3's "machine within 10–30 s"). **Plausibility:** STS3215 (~3 N·m stall) must only position; force stays in the float; ±1–2 mm repeatability is fine against cm-scale fields. **Cheapest experiment:** don't buy the arm. A $30 **scratch recorder** (wrist IMU + four thin FSRs under adhesive nail tips) logged while a partner scratches Michael for 10 min is scratch-model §9.13's "highest-value experiment" and feeds every architecture's pattern engine. **Killer risk:** cost, noise (six geared servos ~30 cm from the ear) and safety of a 1 kg arm by the face; and replays may still feel like replays.

---

## E. HUMAN AMPLIFIER — make a person's scratching 10× better

**Breaks:** the assumption that the product must replace the human, who already supplies rank 1 (irregularity), component E and social attribution for free. What limits a human: **fatigue** (raised-arm shoulder gives out in 2–5 min), **bad edges** (short, bitten or sharp nails), **4 contacts per hand**, **inconsistent force**. **Principle ("nail thimbles"):** TPU finger cots, each with **two** press-on nails 12 mm apart on short feeler-steel leaves (~0.3 N/mm, hard stop ~0.8 N): TM1-quality 45° edges on any finger, **8 contacts per hand**, a mechanical force cap. Plus a posture kit (receiver side-lying, head in the lap; scratcher's forearm on a cushion) and D's recorder inside the thimbles. **Why 10×:** contacts 4 → 8 (2× follicle drive) × session 3 → 15 min (5×), plus fixed edges for partners with short nails [E]. **Hair:** two nails on one finger move together (H-5.6 holds). **Plausibility:** $10, an evening. **Test:** one thimble vs bare nails, blind, same scratcher. **Killer:** needs a partner; by self-attenuation (§4.3) much weaker for self-use. It is an instrument and data source, not the product, but on experience-first it is the shortest path to the best scratch in the program.

---

## F. Considered and rejected, with numbers

- **Hair-tugging (follicle channel without skin contact).** It loads hair in tension, the one mode §6 forbids. 3 N on a gripped 100-hair bundle averages 0.03 N/hair, but clamp load-sharing is very uneven: the 5–10 tautest hairs pass the 0.36 N anagen extraction force. Plucking also evokes seconds-long CT afterdischarge (prior-art §3.2), and neither scratch signature (§1.2) is present.
- **Under-hair flat nails, micro-moving.** Fails by topology: hair is rooted at ~200/cm² (~0.7 mm spacing), so anything "under the hair" is threaded by hundreds of shafts per cm² and forms a pinch line at each (DR5, H-4.9). A 2–5 mm stroke fails §8 item 4 (≥ 10 mm slide), and a flat face is a pad (item 1). It solves rank 2 by building the worst possible hair interface.
- **Electrotactile.** Stimulates axons directly: tingle or prickle, not pressure. Dry electrodes on hairy scalp run 100 kΩ–1 MΩ, so 1–10 mA needs 100–1,000 V. A moving line at ≤ 5 mm pitch over ~600 cm² means ~2,400 gelled electrodes. Component A (hair) is zero.
- **Vibrotactile.** LRAs (150–250 Hz, 10–50 µm, ~5 kPa over 8 mm) drive the Pacinian channel, which adapts in under 1 s and "will dominate if the device vibrates" (§8 item 5 FAIL). Apparent motion over 25–40 actuators renders "something moving", not a 100–200 kPa edge, and parts no hair. **Salvage:** a $10 bone-conduction exciter playing recorded nail-on-hair hiss (component D) is a cheap add-on to any scratcher and a test of §9.9.

---

## G. Comparison

| | Experience ceiling | Asynchrony / P4 | Coverage per posture | Hair risk | Cost | P(works in an apartment) |
|---|---|---|---|---|---|---|
| **A Scalp spider** | highest machine ceiling | native, per leg | ~150 cm², walks | medium (H-5.6 bend) | $60–90 | 0.35 |
| B Head polargraph | high | needs leaf micro-servos | ~120–150 cm², strings | low | $90–130 | 0.6 |
| C Crawling resting hand | high (component E) | native, 4 fingers | one patch + crawl | **high** (crease) | $25–60 | 0.4 |
| D Arm + demonstrations | high | via library | large | low | $370+ | 0.4 |
| E Human amplifier | highest overall, needs a partner | human | whole head | low | $10 | 0.95 |

---

## Best bet: the Leashed Scalp Spider (A), with the gravity puck as its first test

The program spent three architectures making a structure hold a force constant against a head that moves. The spider removes the problem instead of solving it. A 120 g body standing on nail feet presses with 0.29–0.39 N per contact because that is what it weighs. Nothing can seat badly, nothing drifts when Michael nods, and nothing on it can ever press harder than its own weight.

Once mass is the force budget rather than a penalty, giving every contact its own actuator is free. That buys the two things red team 1 found a rigid carrier cannot give:
- **per-contact asynchrony re-drawn on every stroke**, and
- **region wander**,
plus a P4 "spider" primitive that is the literal gait.

Walking also satisfies the hardest hair rule natively: every leg lifts before it reverses, by the same geometric lift that won FLOAT-ARM. Follicle drive (about 3,500 deflections/s) is about twice FLOAT-ARM's.

Its risks are concrete and cheap to retire:
- whether gravity-loaded nails reach the skin through Michael's hair: a $10 passive puck answers it in one evening;
- whether bone-conducted servo noise spoils it: one live leg, $15, answers it the same weekend.

If the puck reaches the skin but self-locomotion disappoints, the same puck goes under three strings (B) at low risk. If the puck test passes, the porcupine's helmet, selector and 40 mm springs are no longer needed; if it fails (gravity nails skate on Michael's hair), the gravity family (A–C) is dead in one evening for $10 and the program loses nothing.
