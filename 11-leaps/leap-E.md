# LEAP E — The whole experience, and the body in the loop

Leap agent E · Project SCRATCH · 2026-10-01 · Provocation: the head is not a passive target, and the contacts are not the only channel.
Tags: `[KNOWN]` literature value (link given), `[EST]` derived here, `[UNKNOWN]` only a test answers it.

---

## 0. The assumption every design so far shares

All three architectures (desk hand, resting crown, porcupine helmet) rest on one picture: **the head is a still, passive target. The device is the only thing that moves and the only thing that sends a signal.** Effort goes into enriching the device's motion and into holding it steady against a head that will not stay put (float, dead weight, soft springs, suspension).

Three facts from the foundations sit badly with that picture:

1. **The head is the most capable actuator in the room, and it is free.** It weighs 4–5 kg, it rolls ±30–40° without effort, and it already supplies "free, uncorrelated jitter", as Team F and Red Team 1 noticed. Every design treats its motion as a disturbance to reject.
2. **The best-placed person-sensor in the room is also the head.** A human scratcher's best feedback is the head pressing into the hand ("there"), the shiver, the stillness. A head-worn device cannot feel any of it, because it moves with the head. **You cannot lean into a helmet.**
3. **Component E (warmth, palm weight, sound, "someone is doing this to me") is ranked last** (scratch-model §1.3) and is designed out entirely: the porcupine's inner shell rides 20–25 mm above the scalp, so nothing ever rests on the head. Newer work says attribution changes processing in S1 and even the spinal cord, independent of kinematics; ranking E last may be the program's largest unexamined judgment.

The five leaps below each break part of that picture. All are argued from the sensory variables in scratch-model §1, §2, §7. The last section names the best bet.

---

## 1. First, re-open Team F's rejection: is head-generated motion "self-touch"?

Team F rejected F4 (the head moves against static nails) because "self-generated touch is centrally attenuated (the self-tickle mechanism)". Red Team 3 and the hybrid memo repeat it. The literature is more specific than that, and the specifics matter for this whole leap file.

- **Attenuation needs an efference copy of an *active* movement.** Touch on a still finger is attenuated when another finger's active movement produced it, not a passive one ([Kilteni & Ehrsson, iScience 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC6997587/)). `[KNOWN]`
- **It is tuned to body-on-body contact and spatiotemporal match.** A spatial gap between the fingers, or producing the force through a joystick, removes it ([PMC8193814](https://pmc.ncbi.nlm.nih.gov/articles/PMC8193814/)); it scales with body ownership ([PNAS 2017](https://www.pnas.org/doi/10.1073/pnas.1703347114)). Tickliness rises as delay grows 0→200 ms or the trajectory is rotated 0→90°; at ≥ 200 ms a self-produced stimulus is rated like an external one ([Blakemore, Frith & Wolpert 1999](https://wolpertlab.neuroscience.columbia.edu/sites/wolpertlab.neuroscience.columbia.edu/files/content/papers/BlaFriWol99.pdf)). `[KNOWN]`
- **Touch on the moving part is a different effect.** Predictive attenuation lowers the *intensity* of reafferent touch on a passive limb; tactile gating lowers the *precision* of touch on a moving limb ([Kilteni & Ehrsson, iScience 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8968059)). A head rolling against a fixed nail is the gating case. `[KNOWN for the arm; head UNKNOWN]`
- **The penalty is real for hand-on-own-body.** Self-stroking deactivates social/affective areas, down to the spinal cord ([Boehme et al., PNAS 2019](https://www.pnas.org/doi/full/10.1073/pnas.1816278116)); being stroked by a partner beats self-stroking and alone slows heart rate, though self-stroking is still pleasant ([Triscoli et al. 2017](https://www.sciencedirect.com/science/article/abs/pii/S0031938417301336)).
- **Against the rejection:** in itch, active self-scratching was *more* pleasurable than passive scratching by an investigator and recruited VTA reward activity ([Papoiu et al., PLoS ONE 2013](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0082389)).

**Verdict.** "Self-generated, therefore attenuated" holds for a hand scratching its own head. It is **not established** for a head moving against a world-fixed nail field: no efference copy for the nail, no body-on-body contact, no hand ownership. What the brain *can* predict is the contact's **timing and path**, so that is what the device must own, and 200 ms / 90° says how far to decorrelate it. F4's real weakness is that a static field has no bite events of its own, which is fixable (E2).

---

## 2. Leap E1 — THE SCRATCHING PILLOW: gravity is the force reference, and the occiput is the target

**(a) Assumption broken.** That the device must be held to the head (straps, suspension) or held against a head that wanders (frame plus float). Lying down, the head **registers itself**: 40–50 N of head weight seats it on a support to within a millimetre or two. That is a better datum than any strap and costs nothing.

**(b) Principle.** A ring (donut) pillow carries the head's weight on its rim. In the 70–80 mm hole under the occipital bun sits a small nail field: the porcupine's own pin units, pointing up, on a carrier plate that a 2-servo XY stage moves under the ring. Each nail rides a soft long-travel spring, so it presses at 0.3 N whatever the head's sink. **Head weight never reaches a nail**: past the pin's travel, or when retracted, the pin hides below the ring plane. The head's slow roll adds a sweep (E2).

```
          side section, supine (head rests on ring rim; nail zone in the hole)

                    ____ occipital bun (R 60–80 mm)
               ___/      \___
   ring  ▓▓▓▓▓/   ^  ^  ^    \▓▓▓▓▓  ring pillow (closed-cell, 40–60 cm² contact)
   rim   ▓▓▓▓▓    |  |  |     ▓▓▓▓▓  sagitta of occiput into a 70 mm hole ≈ 8 mm
                  |  |  |  ← 3–5 released pins, 0.02 N/mm springs, 0.3 N each
         ═════════╧══╧══╧═════════   carrier plate, XY ±15 mm (2 servos)
         [servos + selector in foam-isolated base, 80–120 mm below scalp]
```

**(c) Why it could step-change the sensation.**
- *Force constancy (§7 rank 3, rank 7).* Judge 2's F1 problem (±3–5 mm seating slop × spring rate) becomes **±1–2 mm head sink × 0.02 N/mm ≈ ±0.04 N** `[EST]`. That is the best force reference in the program, obtained with no float, no strap and no dead-weight slide.
- *Region (§7 rank 13; §5).* The occipital bun is the model's "sweet spot": most force-tolerant, in the densest hairy-skin band (~17 Aβ units/cm²). A hard-hat suspension runs its band across it, so the helmet under-serves it; the frame rigs reach it only with the head flexed 45–90° (Red Team 1's posture objection). Supine, gravity lies exactly along the occipital normal.
- *Context (§1 component E).* Head in a lap, lying back, eyes closed is the canonical being-scratched posture. Among ASMR users, 82 % use it to fall asleep ([survey summary, Barratt & Davis 2015 lineage](https://www.researchgate.net/publication/274397023_Autonomous_Sensory_Meridian_Response_ASMR_a_flow-like_mental_state)). A pillow fits the use the experience is actually for.
- *Mass and noise budgets* stop being head budgets: no 500 g ceiling (red line 10); servos sit 80–120 mm below the scalp in foam.

**(d) Physical plausibility.**
- Head load supine ~40–50 N. On a 40–60 cm² ring contact that is 7–12 kPa `[EST]`, comparable to an ordinary firm pillow `[EST; occipital interface-pressure data not looked up]`. It is fine for 20 min and needs the same reposition rule as safety H13.
- Occiput sagitta into a 70 mm hole is R − √(R² − 35²) ≈ 8 mm at R 80 `[EST]`, so pins need ~8 mm of rise plus ±5 mm of working travel. The pin-unit's 0.02 N/mm, ~40 mm springs fit easily in a 60–80 mm-deep base.
- A head roll of ±20° moves the scalp across the hole by R·θ ≈ 28 mm, and ±30° moves it 42 mm. A 70–80 mm field of 9–12 pins at 20–24 mm pitch keeps 3–5 under the occiput at any roll.
- Side-lying puts the parietal region and behind-ear over the hole; crown and top stay the frame arm's job. Lift-off and selection carry over from the porcupine.

**(e) Cheapest experiment (≈ $20, one evening).** A $15 ring cushion on a bed. (1) A partner's fingers reach up through the hole; compare with the same partner scratching the occiput while you sit. (2) The Day-0 wand's three-leaf carrier fixed upright in the hole, 0.3 N on the kitchen scale; roll the head slowly. (3) Same, with the partner jiggling the carrier irregularly. Count shed hairs on a dark pillowcase.

**(f) Replaces or combines.** It replaces the hard-hat suspension and the 500 g budget, not the pin. The porcupine's pin unit, selector and shell drive (a flat XY stage instead of a spherical one) move into a pillow **unchanged in concept**. The SP1 sector could be an *occiput pillow sector* built from the same parts. The pillow is complementary to the frame arm (crown and top) and largely replaces the helmet for the occiput and nape.

**(g) Honest reasons it might fail.**
- **Pinned hair.** Hair under the ring is clamped by 40 N. A nail that drags a hair whose far end is pinned loads it in tension, which is the one load hair cannot take (scratch-model §6). The hole must be large relative to stroke length (stroke ≤ 25 mm inside a ≥ 70 mm hole). Lift-off must be frequent (DR7), and pins must lift on head roll above a set rate. Long hair spread over the pillow is the worst case. This is a C7-class test, not an assumption.
- **Withdrawal.** The head is the quick-release only if the user lifts it, and gravity pushes the head *into* the device. The safeguard is mechanical: unpowered or e-stopped pins sit below the ring plane. Hold-to-run on a hand switch becomes the sleep detector: fall asleep, release, stop. Sleep is otherwise a red-line problem.
- **Posture.** It requires lying down, so it is not a desk device.

---

## 3. Leap E2 — CO-GENERATION: the head supplies the sweep, the device supplies the bite

**(a) Assumption broken.** That every degree of freedom of the stroke must be actuated. The program spends its two shell servos on 25–35 mm strokes and slow group wander. The user's neck delivers 30–80 mm sweeps, region changes and dwell for free.

**(b) Principle.** Split the scratch into two layers with different owners:
- **Gross layer (user):** slow head roll, nod or lean. It gives P2-like sweeps of 30–80 mm at 2–6 cm/s, region changes and dwell. This layer *is* predictable, which is the right place for predictability: it is "where".
- **Bite layer (device):** short, fast, externally timed events. These are 5–15 mm P1/P4 micro-rakes at 2–4 Hz, per-nail phase jitter, force pulses and lift/land events, oriented across the user's motion (≥ 60–90° from it) and timed independently of it (no lock, effective decorrelation ≥ 200 ms).

```
   user roll  ───────────────►  (slow, 2–6 cm/s, predictable: WHERE)
   nail bite        ↕  ↕   ↕↕     ↕   (fast 5–15 mm, ⟂ to roll, random onset: WHEN/HOW)
   felt path   ─/\─/\/\──/\/\/\────/\──  = sweep carrying irregular rakes
```

**(c) Why it could step-change the sensation.** Irregularity is §7 rank 1, and its expensive part is *location and direction wander* (Red Team 1: every design lacked it; the yaw servo was bought for it). Co-generation gets it free and spends actuation on the sub-second events that drive hair and field units (§2.1). It also matches the two velocity optima in §2.2 *simultaneously*: the user's slow roll sits in the CT band (~3 cm/s), and the device's bites sit in the hair-unit band (10–15 cm/s). By the attenuation literature, the bite layer meets both conditions for "external" (no efference copy, a decorrelated time course). The gross layer is at worst gated (less precise), which may even blur it toward "fizz".

**(d) Plausibility.** A bite layer needs only ±5–8 mm of travel at 2–4 Hz. Peak velocity for ±7 mm at 3 Hz is 2π·3·7 ≈ 130 mm/s `[EST]`, inside the scratch band. 30–60 g of pins and carrier is trivial for one STS3032-class servo or the existing shell servos. Roll direction comes from a $3 IMU or the pins' deflection (E3), so bites can be steered across it.

**(e) Cheapest experiment ($0, 40 min, partner plus Day-0 wand).** Three conditions in random order, 60 s each, eyes closed, rated 0–10 for "someone is scratching me" and for pleasure:
- **SELF:** the partner holds the wand rigidly against the occiput and the user rolls the head.
- **EXTERNAL:** the user is still and the partner moves the wand.
- **CO:** the partner holds the wand and adds irregular small wiggles while the user rolls.

If CO ≥ EXTERNAL > SELF, co-generation is a real lever and F4 was wrongly killed. If SELF ≈ EXTERNAL, the attenuation worry was unfounded for this case altogether.

**(f) Combines with.** Any world-grounded mount: the pillow (E1), a headrest, or the frame arm with its float (the float already tolerates ±15 mm). It **cannot** combine with a head-worn device, because a helmet cancels the relative motion. It shrinks the shell drive's job from "stroke plus wander" to "bite", and it makes the yaw servo unnecessary.

**(g) Why it might not work.** Users relaxing toward sleep stop moving, so the gross layer dies exactly when the session matters most. The device must then take it back, so a full drive is still needed, just used less. Gating data are from arms; the scalp is `[UNKNOWN]`.

---

## 4. Leap E3 — THE LISTENING DEVICE: lean-in as input, contingency as "attention"

**(a) Assumption broken.** That the pattern is open-loop: the firmware decides where and how long, and the user's only inputs are on, off and an intensity knob.

**(b) Principle.** A human scratcher reads **press** (stay, harder), **follow** (go there) and **stillness or shiver** (hit; repeat later). The device senses press as per-pin spring deflection. Each active porcupine-type pin already has 0.02 N/mm and ±5 mm of travel, so a $0.30 analog hall sensor plus a 2 mm magnet on the pin cap reads position to ~0.05 mm, which is ~1 mN `[EST]`. On the frame arm, the MGN9 float's position is one channel of the same thing. The response is **lagged and probabilistic** (300 ms–2 s, p ≈ 0.6–0.8), not a servo loop. It extends dwell, intensifies the bite layer (3 → 5 pins, against-lie, P1 over P2, faster) and logs "hits" to revisit after 30–90 s. **Force never rises with press**; intensity is spent on count, direction and rhythm.

```
   head presses here ──►  pin 4 deflects +2 mm (Δ +0.04 N), pins 3,5 +1 mm
                          ▼  (after 0.3–2 s, p≈0.7)
   selector re-centres group on 4 · dwell +10 s · releases 5 pins · against-lie rakes
   head stills 3 s ──►    tag region "hit"; revisit in 30–90 s with a variation
```

**(c) Why it could step-change the sensation.** It moves §7 rank 13 (region) and rank 14 (dwell) from random-walk to *right*, so the device spends its time where this user's pleasure is. More importantly, it manufactures the ASMR trigger "personal attention" (69 % endorsement, [Barratt & Davis 2015](https://www.researchgate.net/publication/274397023_Autonomous_Sensory_Meridian_Response_ASMR_a_flow-like_mental_state)). The behavioural signature of attention is **contingency**: the other agent responds to you, late and imperfectly. Social attribution changes S1 processing independent of touch kinematics ([Gazzola et al., PNAS 2012](https://www.pnas.org/doi/10.1073/pnas.1113211109)). Known robot touch is liked less than human touch, but unknown-source robot touch matches human ([Pleasant stroke on the back by human and robot, PMC9919452](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9919452/); [trust and robot touch, Sci Rep 2024](https://www.nature.com/articles/s41598-024-57582-1)). The cue that betrays a machine is behavioural, and contingency is the cheapest one to add. The lag is deliberate: a < 200 ms response that tracks the head exactly would make the device a self-controlled tool and invite attenuation.

**(d) Plausibility.** 12 hall sensors (~$5) and an ADC mux, or the existing float. Breathing (~1–2 mm, 0.2–0.5 Hz) is filtered out. Shiver is harder; "≥ 3 s stillness after a bout" or a squeeze bulb is the proxy.

**(e) Cheapest experiment ($0, Wizard-of-Oz).** Two 3-minute partner sessions, order randomised, user blind: (A) partner follows a printed region schedule; (B) partner responds to leans with a deliberate ~1 s delay. Rate pleasure and "they were paying attention". If B wins, add one hall sensor on the SP1 float and a 20-line firmware hook.

**(f) Combines with.** Pillow and frame (world-grounded) fully. On the helmet it works **only partially**: pins still deflect with scalp shape and slop, but the user cannot lean into a helmet. This is a structural argument for world-grounded mounts that the program has not yet weighed.

**(g) Why it might not work.** Press signals may be swamped by seating and breathing noise. Users may not lean at all when relaxed. A device that "chases" can feel needy rather than attentive, so the probabilities and lags need tuning that only sessions can set.

---

## 5. Leap E4 — THE SECOND HAND: an asymmetric two-group device with warmth, weight, sound and a slow build

**(a) Assumption broken.** That the experience equals the contacts: one group of 3–5 nails, one drive, one rhythm, no palm, no heat, sound treated as noise to suppress.

**(b) Principle.** Model what two human hands do when they play with a head:
- **Holding hand.** A warm (33–35 °C), weighted (1–2 N over 40–60 cm², ≈ 0.3 kPa) soft palm resting on another region. It occasionally makes a slow fingertip stroke at 2–4 cm/s and ≤ 0.1 N (the CT channel), and it rocks slightly when the other hand works.
- **Scratching hand.** The nail group on its own drive at P1/P4 rhythms.
- **Two clocks.** The two hands run incommensurate rhythms (e.g. 0.3 Hz holding drift vs 1.7–2.9 Hz rakes with jitter). The combined pattern has no common period.
- **Sound.** A piezo on one nail, amplified (< 10 ms) into earbuds: the user hears the scratch crisper, motor noise masked.
- **Slow build.** 0–60 s: holding hand only, plus CT-speed hair play (pins at the canopy, 0.05 N). 60–180 s: single nails, P2 sweeps at 5–8 cm/s, 0.15 N. Then: full P1 rakes at 0.25–0.4 N, returning to the slow mode at least once a minute (already a §4.4 rule).

```
   [holding palm 35 °C, 1.5 N, slow drift]          [nail group, own drive, 2–3 Hz rakes]
        ~~~~ parietal L ~~~~                              ^^^ occiput ^^^
   clock A: 0.3 Hz drift, CT strokes                 clock B: jittered P1/P4
   + piezo on nail ─► amp ─► earbuds (crisp hiss, < 10 ms)
```

**(c) Why it could step-change the sensation.**
- *Irregularity (§7 rank 1) at no firmware cost.* Two independent clocks at incommensurate ratios cannot be learned as one period. The brain must track two predictions, which is the regime that defeats habituation (§4.3).
- *The two optima in parallel.* §2.2 says CT (≈ 3 cm/s) and hair units (10–15 cm/s) want different speeds. A one-drive device time-multiplexes them, while a two-hand device delivers both at once, as humans do.
- *Warmth, not contrast.* CT afferents fire most to stroking at skin temperature and less at 18 or 42 °C ([Ackerley et al., J Neurosci 2014](https://www.jneurosci.org/content/34/8/2879)), so thermal contrast lowers CT drive. Contact temperature T_c = (e₁T₁ + e₂T₂)/(e₁ + e₂), e = √(kρc): skin (e ≈ 1100, 34 °C) on a 22 °C PETG nail (e ≈ 550) gives ≈ 30 °C; on a real nail (e ≈ 700, 30 °C) ≈ 32 °C; on steel (e ≈ 8000) ≈ 23 °C, cold metal `[EST]`. A 1–3 mm² line has negligible thermal summation, so **polymer nails are already warm enough; avoid steel.** Warmth is perceptible only over a palm-sized area, which the program lacks (only Team D's W1 noticed).
- *Sound.* In the parchment-skin illusion, changing the spectrum of the friction sound changes perceived skin texture and dryness ([Jousmäki & Hari, Curr Biol 1998](https://research.aalto.fi/en/publications/parchment-skin-illusion-sound-biased-touch/)). Crisp sounds trigger ASMR for 64 % ([Barratt & Davis 2015](https://www.researchgate.net/publication/274397023_Autonomous_Sensory_Meridian_Response_ASMR_a_flow-like_mental_state)); hair play is the top real-life tactile trigger (73 %, [Poerio et al. 2023](https://www.sciencedirect.com/science/article/pii/S1053810023001216)). Live scratch sound plausibly raises "nail-likeness" (§8 item 12) for $10; the program treats sound only as noise.
- *Slow build.* Repeated identical strokes lose "wanting" faster than "liking" ([Triscoli et al., touch satiety, PLoS ONE 2014](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0113425)). Starting below the target and escalating spends novelty over minutes instead of seconds. Anticipation is what a person's slow approach supplies.

**(d) Plausibility.** A 60 × 80 mm gel pad with a 2–3 W heater, thermistor control at 35 °C and a 40 °C hard thermostat; one more servo (or two half-shells) for the second clock; $8 of piezo and preamp.

**(e) Cheapest experiment (≈ $15, 1 evening, on the Day-0 wand or SP1).** A 2×2 within-subject design: **palm** (hand-warmer pouch in a sock, 1–2 N on the parietal, vs none) × **sound** (earplugs plus white noise vs a live piezo on the wand nail into headphones). Then a separate partner session for **two-hand asymmetry**: one hand holding and stroking slowly while the other scratches at a different rhythm, vs both hands scratching in sync.

**(f) Combines with.** Every architecture. On the helmet, a resting palm violates the 20–25 mm standoff only locally and adds weight to the head. It sits most naturally on the pillow, where the palm can be part of the ring, or on a frame arm.

**(g) Why it might not work.** Warmth and weight can push the experience toward "massage/comfort", which is §8's neighbour column. A palm pressing at 1–2 N is an SA2 pressure percept. Amplified sound can feel "creepy close-mic" to non-responders (prior-art §3.5). These are modulators; they cannot rescue bad contact physics.

---

## 6. Leap E5 — THE NAIL GLOVE: whose hand, and moved by whom?

**(a) Assumption broken.** That the device must replace the human. It could instead *augment* a human hand, the user's or a partner's.

**(b) Principle, three variants.**
- **G1, own hand, active.** The user wears a glove with powered nail tips (mini-servo or tendon micro-rakes of 5–10 mm on each fingertip) and scratches their own head.
- **G2, own hand, passive.** The user rests the gloved hand on the head with the elbow propped on a pillow. Only the glove moves the nails.
- **G3, partner's hand.** A partner wears it and rests or slowly moves the hand. The glove supplies the tireless 3–6 Hz P4 spider and P1 bites, and the partner supplies presence, warmth, coverage and attention.

**(c) Analysis.**
- **G1** is the canonical attenuation case (active hand on own body; [Boehme 2019](https://www.pnas.org/doi/full/10.1073/pnas.1816278116)), and an overhead arm tires in minutes. It wins on coverage, force reference (arm compliance, §3.12), snag safety and cost (~$60–150). **It does not beat a head-worn device for the target experience, being scratched while passive**; it beats every device as an *instrument*.
- **G2:** no active movement, so no efference copy and no predictive attenuation ([Kilteni 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC6997587/)), but the brain knows it is its own hand: no social attribution.
- **G3** attacks the real scarcity, **partner endurance**: partners stop after a few minutes because the arm tires `[EST, observation]`. A partner resting a gloved hand keeps components C and E and offloads the work.

**(d) Plausibility.** 5–8 g fingertip units (nail on a 10 mm flexure, sub-micro servo or Bowden tendon from a ~100 g wrist pod). Hair safety is the weak point: splayed fingers form apertures and fabric snags (DR5, DR8), so the glove must stop at the DIP joint with the nail unit as a smooth cap.

**(e) Cheapest experiment ($10, 30 min).** A cotton glove with press-on nails glued on (no motors). Four conditions:
1. The user scratches their own head actively.
2. The user's gloved hand rests on the head while the partner moves the user's wrist (passive own hand).
3. The partner wears the glove and scratches.
4. The partner's bare nails.

A living-room version of Kilteni's efference-copy test: it separates "my body", "my motor command" and "another person". If 2 ≈ 3, G2 is a product; if 3 ≫ 2, attribution is the lever and E3/E4 outrank any mechanism.

**(f) Combines with.** G3 needs no head mount. The glove's fingertip unit is the porcupine pin's nail plus neck, made wearable.

**(g) Why it might not work.** G1 is self-touch and is expected to lose. G3 needs a partner, which is the thing a scratching machine exists to make unnecessary. Glove hair-safety is the weakest of any concept here.

---

## 7. Best bet: E1 + E2, the scratching pillow with co-generated sweep

**The case.** The program's hardest unsolved engineering problem, stated by all three judges and re-solved four times (float, dead weight, crown, soft long-travel pin springs), is the **force reference against a head that will not hold still**. Lying down solves it with physics already present: 40–50 N of head weight seats the skull on a ring to a millimetre or two. That leaves the pin springs a ±0.04 N swing instead of a ±0.1–1 N one. The pillow also delivers the occiput, the region the model rates highest-value and most force-tolerant, with gravity exactly along its normal. Freed from the 500 g budget, it carries the porcupine's own pins, selector and an XY stage unchanged, and adds three things no head-worn design can have:
- the head's free slow roll as the gross sweep (location and direction wander for zero actuators, in the CT velocity band);
- lean-in sensing from the pins' own deflection, so the device can be attentive;
- a posture (lying back, eyes closed, head held) that is how people are actually scratched and how most ASMR users actually use the experience.

The F4 rejection that would have killed it rests on a reading of the attenuation literature that does not apply to a head moving against a world-fixed object. Predictive attenuation needs an efference copy for the touching effector and body-on-body contact. The device's externally timed bites, decorrelated by more than 200 ms and turned 60–90° from the roll, meet every published condition for "external". It is a $20 evening to find out. Ring cushion, the Day-0 wand's three-leaf carrier upright in the hole, kitchen scale, partner: run SELF / EXTERNAL / CO, then count hairs on a dark pillowcase. If CO beats SELF and the hair count is clean, SP1 should be an occiput-pillow sector built from porcupine parts, not a helmet sector.
