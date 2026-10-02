# LEAP 3-C — CONTACT QUALITY AND LISTENING ON A HELMET

**Project SCRATCH · 11-leaps/round-3 · Agent C · 2026-10-02**
**Provocation:** keep the travelling pad square and at standoff on a real head under a helmet that moves and slips; replace the cradle's lean-in sensing; map Michael's head once with the pins as a probe, then personalise.
**Read:** LEAP3-BRIEF; leap2-A to F; safety §2, §3.9–3.10, §7; hair-interaction §1–6; scratch-model §3, §5, §7; concept-A §3–4; leap-E §E3. Firewall kept.
**Tags:** **[KNOWN]** sourced · **[EST]** computed here (script in the session scratchpad) · **[UNKNOWN]** needs a bench or Michael's head.

---

## 0. What the helmet changes

**1. Air pins are blind to geometry.** A pin open to a rail pushes P × A at any extension. That is why seating stopped mattering. It also means constant-force pins give **no restoring moment when the pad tilts**, so the pad's plane must be set by something with stiffness (a skid, a sealed pin, a stop) or by measurement.

**2. On a helmet, head-to-pad motion is zero, but the shell sees the head perfectly.**
- Lean-in (leap-E E3, leap2-D D3) is gone.
- A shell IMU is rigidly coupled to the skull, so it reads tilt, stillness and breathing.
- Slip is small under steady load. The suspension's rotational stiffness is ≈ 4 × 1 N/mm × (90 mm)² = 32 N·m/rad, so leap2-E's 0.15 N·m CoM-wander swing tilts the helmet **0.27° (0.4 mm)** [EST].
- **Quick head turns are the slip risk.** At 60–100 rad/s² the helmet (I ≈ 4.6 × 10⁻³ kg·m²) needs 0.27–0.46 N·m, against a 0.49 N·m hold at µ 0.3. Each donning also seats ±5–10 mm differently [EST].

**3. The scalp moves under the pad.** It lies 75–100 mm from the helmet centre (±12.5 mm along travel), its normal sits up to 14–20° off radial, and the canopy adds 5–25 mm on top. The pins' ±15 mm stroke absorbs most of this, but not a tilt beyond ~10°: the attack angle must stay in 25–65°, and the omni-nail's lean already uses 5–15° of it. Nor does it absorb stacked standoff error (12 + 5 + 5 > 15).

| Option from the provocation | Verdict | Deciding number |
|---|---|---|
| Air-floated pad | **Reject** | 1 N on a 60 mm cushion needs 357 Pa. That is ~24 m/s through any gap in the hair, and even a 0.1 mm mean gap round a 190 mm rim passes **27 L/min** against a 1.8 L/min pump. A hissing hair dryer [EST]. |
| Rigid radial pad, no skids | Only with a map (C4) | 14–20° tilt error on the flanks and bun |
| Skids on a pivot above the pad (leap2-A L2) | Works, heavy-handed | 0.56–1.12 N of drag × 55 mm = 31–62 N·mm of tipping. It needs **1.2–2.5 N of skid load** or an air lock that freezes tilt during drift. |
| **Compliant gimbal with its pivot at the contact plane** | **C1** | Pivot ≤ 10 mm from the contact: ≤ 11 N·mm, so **0.45 N** of skid load suffices |
| Comb-ring skid (tines to the skin) | Variant | Skin datum ±1 mm (canopy ±5 mm). But every tine is a continuous stroke (H-5.8), so with-grain sweeps only, and there is a formication risk [UNKNOWN]. |
| Per-pin pressure as the listener | Not sufficient | It reads height and compliance (sip: 1.15 kPa/mm, ~0.05 mm), never intent |
| Frontalis or temporalis EMG in the sweatband | Later | Sweat on dry electrodes plus the scrub's 1–2 Hz artefact [UNKNOWN] |

---

## LEAP C1 — THE RCC PALM: pivot at the scalp, a 0.45 N tripod, a palm that never pats

**(a) Assumption broken.** "Keeping a pad square needs a firm palm (1–2 N) or a tilt lock." Both follow from a pivot *above* the pad, which gives drag a lever arm. Assembly robots solved this with the **remote-centre-compliance (RCC) wrist** (Draper Laboratory, Whitney) [KNOWN]: inclined struts whose lines meet at a point outside the mechanism. Put that point at the nail plane and drag translates the pad but cannot tip it.

**(b) Principle.**
- **The struts.** Three ball-ended 2 mm carbon struts (~6 g) run from a Ø 110 ring on the radial air float, ~80 mm above the scalp, to a Ø 76 ring on the pad top, 55 mm up. They lean **35° to the axis** (slope 38/55), so their lines cross at the contact plane under the pad centre.
- **The tripod.** Three POM domes (R 15) on a Ø 100 circle rest on the canopy at **0.15 N each** and set the plane geometrically. Each skid stem has a magnet over a $1 analog hall sensor (height ±0.05 mm).
- **The drag sensor.** A 3-axis hall (TMAG5273 class, ~$2) at the strut ring reads lateral deflection, with TPU strut sleeves set to ~2 N/mm. It is a drag vector and the snag sensor H-6.6 asks for.
- **Hairline and ear mode.** Each skid has a two-position air latch. Near the hairline or an ear fence the leading skid retracts and the orbit parks into a P7 trace, while the two nearest pins go **sealed** (a gas spring of ~0.06 N/mm at 0.10–0.15 N, per leap2-D D3's physics) and become the third leg. No skid is ever put in front of the hairline (red line 6).

```
            radial air float (constant bias)
                      ║
          ┌───────────╨───────────┐  ring Ø110, ~80 mm up
           ╲                     ╱   3 struts at 35°, TPU sleeves 2 N/mm lateral;
            ╲                   ╱    3-axis hall here = drag vector / snag
          ┌──╲─────────────────╱──┐  pad-top ring Ø76, 55 mm up
   skid ─┐│   ╲   orbit stages╱   │┌─ skid: POM R15, 0.15 N, hall height, air latch
         ││  ▼  ▼ ╲  ▼  ▼  ╱▼  ▼  ││  16 pins (hall per pin), omni-nails
 canopy ~(●)~~~~~~~~╲~~~~~╱~~~~~~(●)~~
 scalp ───────────────── V ─────────────  V = virtual pivot, within ±10 mm of the nail plane
```

**Never pats.** With a constant-force float, skid load = F_float − ΣF_pins. If four 0.5 N pins cycle at stroke rate, the skids swing 0.45 ↔ 2.45 N at 2–3 Hz: a rhythmic palm, which is a machine signature. Two near-free fixes:
1. **A constant-support gait in the κ-grammar.** Keep ΣF_active within ±0.15 N during a phrase by having set A lift as set B lands, which is leap2-B's alternating-set mode. Only P5 rests and region changes move ΣF, and they last 0.3–1 s, slow enough for the float to follow.
2. **The float rail as "pin 17".** Command it to bias + ΣF_scheduled, with its gates fired early by its measured latency.

**(c) Variables moved.**
- **Skid load:** 1.2–2.5 N → **0.45 N**.
- **Skid drag on hair:** ~0.3–0.5 N → **~0.09 N**, which is leap2-A's backcombing worry divided by about 4.
- **Tilt:** followed continuously through drift instead of being frozen at landing. A 1.12 N spike at ≤ 10 mm of pivot error gives ≤ 11 N·mm, against a tripod resisting ~11 N·mm, so **< 2°** [EST].
- **Hardware removed:** the air lock and its valve and tube.
- **The resting hand (component E):** constant, not patting.
- **Free measurements:** every skid and pin height is a profilometer reading (for C4), and the lateral hall resolves **±20 mN of drag at 1 kHz**, enough for a lift-on-snag reflex within 100 ms.

**(d) Plausibility [EST].**
- **Mass:** the struts, rings, three skid halls, the lateral hall and two latches weigh ≈ 16 g, less the ≈ 10 g tilt joint and lock they replace: **net +6 g**. Per-pin halls (for C4, and to confirm every lift per leap2-B L1(g4)) add 11 g and ~$20.
- **Skid pressure:** 0.15 N over 50–100 mm² of canopy is 1.5–3 kPa, under the 5 kPa sustained limit.
- **Region changes:** the skids' sagitta at 50 mm is 20.8 / 14.7 / 8.3 mm at R 60 / 85 / 150. Posts tuned to R 85 keep the pins within ±6 mm of mid-stroke.
- **Height cost:** the pad grows ~25 mm, to ~80 mm. Leap2-E's arc radius goes from ~150 to ~175 mm and the CoM-wander moment from 0.15 to ~0.18 N·m, still a third of the hold.

**(e) Cheapest experiment (~$15, an evening).**
1. Print two rings and six ball sockets and fit three 2 mm carbon rods. Use three nylon furniture glides as skids, a dummy 76 mm pad loaded to 0.45 N with washers, and a phone running phyphox as the tilt meter.
2. On a wig head, pull at the nail plane with a luggage scale up to 1.1 N, with the struts at 35° and then rebuilt vertical with a top ball pivot.
   - **Pass:** RCC < 2°; conventional > 10°.
3. Hand-slide the pad 10 × 15 cm crown to occiput, then count shed hairs and photograph the canopy, against 2 N skids.

**(f) Combines.** It replaces leap2-A's tilt joint, lock and 1–2 N palm, and keeps its idea that the scalp sets the plane. It needs the gait rule in leap2-D's grammar, and it feeds C4 and the snag reflex.

**(g) Might fail.**
1. **The pivot has a fixed depth but the contact plane moves.** Pins touch skin, skids ride the canopy, and the canopy is 5–25 mm deep. In 25 mm of hair, the pivot error and the skid load needed both double (0.9 N).
2. **A pad-body dwell spiral would circle the loaded skids,** which H-5.7 calls hair-negative. Spirals must come from the orbit plate, and pad-body paths must be monotonic.
3. **Long hair draped upward** can reach the strut ends, which then need boots.

---

## LEAP C2 — THE LISTENING SHELL: the IMU reads the melt, the sigh and the tilt-into; a bone microphone hears "mmm"

**(a) Assumption broken.** "Lean-in is the implicit 'there'." A human scratcher reads a family of signs: press, stillness, the head sinking into the hand, a slower breath, a sigh, a murmur. On a helmet only press is lost. The rest are kinematic or bone-acoustic, and **a helmet is the best-coupled such sensor a head can wear.**

**(b) Principle.** A $3 IMU (ICM-42688 / BMI270 class) and a $1 piezo disc bonded inside the shell.

| Detector | Signature | Resolution, latency | False-positive estimate [EST] | Meaning |
|---|---|---|---|---|
| **Melt** | 2–8 s after a phrase starts: head angular-speed RMS (0.3–3 Hz) < 0.5× its 20 s baseline for ≥ 3 s, **and** pitch sinks ≥ 1.5° along gravity | < 0.05° over 2 s (0.0028 °/s/√Hz); decision 3–8 s | Spontaneous settling follows 5–15 % of phrases. **Likelihood ratio ≈ 2–4: a weak vote.** | "good" (slow) |
| **Tilt-into** | Rotation that moves the pad's spot outward along its normal (v·n̂ > 0, v = ω × (spot − neck pivot ~80 mm below head centre)), ≥ 3° in 1 s, held ≥ 1 s | Decision ~1.2 s | 1–3 head moves/min × ¼ in cone × 0.4–0.6 held = **0.1–0.45/min** | "there, more" |
| **Sigh** | One breath ≥ 2× the running tidal pitch amplitude (0.15–0.5 Hz) | A 4th-order 0.5 Hz low-pass removes the orbit's 1 Hz by 24 dB and 1.5 Hz by 38 dB; 3–5 s | ~1 per 5–10 min unrelated [UNKNOWN] | "release": end the build |
| **Breath rate** | Head-IMU respiration while still (BioGlass, Hernandez, McDuff & Picard 2014 [KNOWN; check accuracy figures]) | ±1 br/min per 30 s | n/a | session trend per region |
| **Hum** | Voiced burst 0.3–1.5 s, F0 80–250 Hz, steady spectrum, on the bone microphone; valve and pin noise gated by known timing | 0.3–0.6 s | Own voice ~20–30 dB above TV via bone [EST]; ~1–3 per hour while talking | "yes" (implicit) |

The crown has no tilt-into: its normal is parallel to the neck axis. There, melt, hum and the egg (C3) do the work.

**Respond as attention, not control.**
- Implicit signals change only **where and how long**, never force.
- **Lag:** 0.4–1.5 s for tilt-into and hum, 2–10 s for melt.
- **Probability:** 0.6–0.8.
- **Acknowledge, then act:** all pins hover 150–250 ms (a hand's "hm?"), then stay 4–10 s with **one** feature varied.
- **Return:** tag a hit and come back 30–90 s later with a variation.
- **At most one overt response per 20–30 s.**

The > 200 ms lag and imperfect obedience keep the touch "external" (leap-E §1).

**(c) Variables moved.** §7 ranks 13–14 (region, dwell) become user-weighted at zero effort. Component E gains contingency, the cheapest behavioural cue of attention (leap-E E3, citing Barratt & Davis 2015 and Gazzola 2012). The D3 learner gets ~2–6 implicit labels per minute instead of sparse presses.

**(d) Plausibility.**
- **Hardware:** 3 g and $4.
- **Orbit vibration** (0.01–0.1 m/s², leap2-F F5) is removed by synchronous subtraction against the encoders.
- **CoM-wander tilt** (0.27°) changes over 5–30 s, below the breath band.
- **The open question is behavioural:** will Michael keep tilting into a pad he can't press? Probably at first by habit, then because it works [UNKNOWN].

**(e) Cheapest experiment ($0, two evenings).**
1. **Night 1:** a phone running phyphox (gyro and accelerometer at 100 Hz, plus microphone) taped to a cap. A partner scratches Michael on the couch for 3 × 10 min and taps a second phone at each lean, melt or murmur. Run the detectors offline.
   - **Pass:** tilt-into and hum reach ≥ 60 % recall at ≤ 0.3 false positives per minute.
2. **Night 2:** a Wizard of Oz in which the partner responds only to detector flags, with the lag rules, against a fixed schedule, blind. Rate "paying attention" and pleasure.

**(f) Combines.** It replaces E3's lean and D3's lean pseudo-label on the helmet, feeds D2 and D3, and sits under C3.

**(g) Might fail.** Deeply relaxed users stop moving, so melt loses contrast. A TV posture fills the tilt cone with glances. A visible reward for humming turns the hum into a button.

---

## LEAP C3 — THE SQUEEZE EGG: "yes", "there" and "stop" through air, with no electronics in the hand

**(a) Assumption broken.** "Explicit input means a remote with buttons, a battery and a radio." The system is pneumatic, and the desk box already reads pressure per line. **A rubber chamber on a 1.5 mm tube is a sensor with no battery (red line 5).** A chambered egg lets the hand *point*.

**(b) Principle.** A palm-sized silicone egg (55 × 70 mm, cast with a $20 kit) with **three chambers** (front, back, top) and raised "nose" and "ear" nubs for orientation by feel. Each chamber has 1.5 m of tube to a 0–100 kPa sensor in the desk box, plus a 0.3 mm bleed (τ ≈ 2 s) to cancel thermal and grip creep. The chambers are ~20 ml, so a 5 / 10 / 15 ml squeeze reads **13 / 31 / 55 kPa** [EST].

| Gesture | Response |
|---|---|
| Light squeeze (5–15 kPa, < 0.6 s) | **"There."** After 0.4–1.0 s: a 150 ms hover acknowledges, then the pad stays 6–10 s with one feature varied and tags a hit |
| Hold one chamber > 1 s | **"That way."** The pad drifts there at 2–3 cm/s, overshoots 10–15 mm, then **searches** with an N1 spiral converging over 2–4 s. A light squeeze during the search fixes the centre. |
| Double squeeze | "Not there; move on" |
| **Hard squeeze > 40 kPa** | A mechanical pressure switch opens the valve-power loop and every pin vents and lifts. This is hardware in series with the NC e-stop (§3.10), not a replacement for it. |

**(c) Variables moved.**
- **Spatial "there":** the egg recovers about 60 % of lean-in's best feature (three regions plus search-and-settle).
- **Labels:** near-zero-false-positive labels for D3's ~275-phrase personalisation.
- **Stop:** a stop channel in the hand that is already holding something.

**(d) Plausibility [EST].**
- **Latency:** 4.4 ms of tube + 1 ms of sensor + 20 ms of debounce ≈ **30 ms**, against a deliberate 400–1000 ms response lag.
- **False positives:** grip shifts stay below 3 kPa, against a 5 kPa threshold, so ≈ 0 false "yes" per hour. Falling onto the egg trips a stop, which fails safe.
- **Cost and routing:** $3–5 of sensors and $10–15 for the pressure switch. The three tubes go to the desk box, not to the head.

**(e) Cheapest experiment ($12, an evening).**
1. Tape two blood-pressure bulbs back to back as front and back, on 1.5 m of tube to one XGZP6847A and the bench ESP32.
2. With a partner scratching, run two 6-minute conditions, order blind:
   - **(A)** squeezes are obeyed instantly, straight to the spot;
   - **(B)** the partner waits 0.5–1.5 s, arrives a little off, and feels for the spot.
3. Rate "obeying me" against "attending to me", and pleasure.
   - **Pass:** B beats A by ≥ 2/10 on attention, with pleasure no worse. That would show the *response style*, not the input, creates attention.

**(f) Combines.** It is the explicit layer over C2 and the label source for leap2-D D3. It replaces any electronic remote.

**(g) Might fail.**
1. **Judging breaks the trance** (leap2-D D3(g)).
2. **The egg's front and back may not map onto his own head.** It then falls back to one chamber (yes / move on / stop), and spatial "there" is lost.
3. **Lint can clog the bleeds,** so they need sintered filters.

---

## LEAP C4 — THE FIVE-MINUTE HEAD SCAN: the pad maps shape, hair depth, grain and give; the whorl registers the helmet each session

**(a) Assumption broken.** "A head map needs a scanner, and grain is drawn on a diagram by a helper" (leap2-D D3 S0). C1's pad is already a contact profilometer *and* a tribometer, sitting exactly where the map is used.

**(b) Principle.** On the first wearing, the pad visits **~18 stations** at 50 mm spacing (crown, top, upper parietals, upper occiput; ~400 cm²), ~8 s each:

1. **Shape.** With the orbit parked, all 16 pins land at 0.08 N. The per-pin halls give heights to ±0.05 mm, and a quadric fit over the 54 mm field gives:
   - the normal to **±0.04°**, or **±0.2°** with 0.3 mm of hair scatter [EST, Monte Carlo];
   - the principal radii to ±2–5 %, from a 4.3 mm sagitta at R 85;
   - the radius from the helmet centre to ±0.3 mm.
2. **Give.** Stepping to 0.3 N, each pin's Δh gives compliance: stiffer over the vertex bone, softer over the temporalis or a hair mat [EST]. This is the program's first measurement of §7 rank 2.
3. **Canopy depth.** Skid height minus the pin plane at the skid radius (sagitta removed) gives hair depth to ±1–2 mm.
4. **Grain.** C1's lateral hall reads drag on two ≤ 25 mm lifted Tusi strokes in each of **8 headings** at 0.2 N, which is H-5.1-legal. With-grain to against-grain drag runs 1 : 3–5 (hair-interaction §2.3), so the drag rose gives the grain heading to **±15°** and its strength. The divergence of the field locates the **crown whorl** to ±5–10 mm.
5. **Sensitivity, the one human step (~2 min).** Rakes at 0.15 / 0.3 / 0.45 N at six region centres. Michael squeezes the egg for "too much" and double-squeezes for "too light", which sets each region's force box (D3 S0).

**Total: about 5 minutes, done once.**

**Uses.**
- **Feed-forward:** travel carries the standoff and tilt the head needs, so C1 only absorbs small residuals.
- **Per-cell strokes:** with-grain sweeps run as spokes from the measured whorl; against-grain rakes go only where the grain is strong and the hair short; force caps drop over compliant ground and flagged spots.
- **15-second registration each session:**
  - one drag rose near the last whorl position, plus three profile stations;
  - a 1° yaw changes the side radius by 0.35 mm on a 96 × 75 mm section, so yaw resolves to ~1° and fore-aft to ~2–3 mm;
  - with the whorl, seating is known to **±3 mm**;
  - soft fences (hairline, ears) shift to match, while hardware stops stay helmet-fixed with ≥ 10 mm of margin.
- **Slip watch:** a persistent > 2 mm residual on ≥ 3 stations, or a > 60 rad/s² head turn followed by a residual, triggers pause, re-register and resume.

**(c) Variables moved.**
- **Ranks 2–3 (penetration, force):** a measured per-cell depth and compliance.
- **Rank 8 (direction against the lie):** a measured ±15° grain field.
- **Rank 13 (region):** registered to Michael's whorl, not the helmet.
- **Fences:** head-referenced.
- **The D3 learner:** cells in Michael's coordinates, so Tuesday's learning holds on Wednesday at a 7 mm different seating.

**(d) Plausibility.** Mapping is firmware only, given C1's halls. The data are a few kB. The fits and the whorl search take milliseconds on an ESP32. The weak link is the drag rose through hair: humidity and sebum shift µ by ±30 %, but the with:against *ratio* is what is used [EST].

**(e) Cheapest experiment (~$20, a weekend).** Test the novel claim, grain from drag.
1. Mount an omni-nail in a pen body on a $10 HX711 load cell, sprung to 0.2 N.
2. At 10 marked spots on Michael's head, a helper drags 25 mm strokes in 8 headings, two of each, and photographs the hair lie.
   - **Pass:** at ≥ 8 of 10 spots, the maximum-drag heading falls within ±30° of the visibly against-grain direction, with a ratio of ≥ 1.8.
   - **Whorl:** spots around the crown should show a field pointing out of one centre.

**(f) Combines.** It needs C1's instrumentation, replaces D3's drawn grain map, and gives D2 and D3 their cells.

**(g) Might fail.**
1. **Long hair (≥ 15 cm):** the drag rose measures today's styling, not growth direction.
2. **Two whorls, or a diffuse one:** the landmark is ambiguous, and registration falls back to shape plus brim seating.
3. **The 8-direction rose is about one 8-stroke patch per station,** at H-5.5's limit, so each station needs a with-grain comb-out pass.

---

## Ranking

| Leap | Experience | Plausibility | Hair / safety | Cost / mass | Risk | /25 |
|---|---|---|---|---|---|---|
| **C3 Squeeze egg** | 4 | 5 | 5 (stop in the hand) | 5 (0 g on head) | 3 | **22** |
| **C1 RCC palm** | 4 (constant 0.45 N hand, tilt tracked) | 4 | 5 (skid drag ÷4, snag sensor) | 5 (net +6 g) | 3 | **21** |
| **C4 Head scan** | 4 (right direction and force per cell, day to day) | 4 | 5 (head-referenced fences) | 5 (firmware) | 3 | **21** |
| **C2 Listening shell** | 4 | 3 | 4 | 5 (3 g) | 2 (false positives in TV posture) | **18** |
| Air-floated pad | — | 1 (27 L/min) | 2 | 2 | 1 | 6 |

---

## Best bet: the instrumented RCC palm (C1) that scans the head once (C4) and listens through a squeeze egg (C3), with the IMU (C2) as a quiet second voice

Air pins took force out of the geometry and left the pad blind to it. So on a helmet that slips, contact and listening both have to come from one honest reference plus measurement.

**Contact.** Michael's pad hangs on three struts whose lines cross at his scalp, so drag cannot tip it. It rests on three 0.15 N domes: a felt palm that never pats, because the gait keeps the pins' summed force constant. That is a quarter of leap2-A's skid load, with no lock.

**The scan.** The first evening, the same pad spends five minutes measuring:
- his skull, to a third of a millimetre;
- his hair depth;
- his grain, to about 15°, and his whorl;
- where 0.45 N is too much.

After that, a 15-second whorl check registers the helmet to ±3 mm wherever it sat today. The pad arrives square and mid-stroke, rakes against the grain only where the hair allows, and fences the hairline and ears from his head, not from the helmet.

**Listening.** He can't lean into a helmet, so he squeezes an egg:
- a light squeeze means "there";
- holding the back means "go back there", and the pad overshoots and feels for the spot;
- a hard squeeze lifts every pin through a pressure switch, with no electronics in his hand.

Meanwhile the shell's IMU and bone microphone notice when he stills and sinks, sighs or murmurs. Those signals only ever steer where the pad spends its time and when it returns, always late, imperfectly and sparingly. That is what attention looks like.

**Cost:** ~+20 g on the head (inside leap2-E's 45 g margin), ~$45, and no new actuator.

**The first weekend costs under $50:** the RCC tipping rig ($15), the grain-from-drag rose on his own head ($20), the two-bulb Wizard-of-Oz egg ($12), and a free phone-on-a-cap night for C2.
