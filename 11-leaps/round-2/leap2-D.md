# LEAP2-D: The pattern layer. A score the pressure-gated orbit can play

**Project SCRATCH · 11-leaps/round-2 · Agent D · 2026-10-02**
Read: LEAP2-BRIEF; leap-B (L1, L2, §3); leap-A (L2, L5); leap-D in full; scratch-model in full (§4 in particular); hair-interaction §2.3–2.4, §3, §5; safety §2, §7; pin-unit §1; concept-A §2–3; leap-E (E2–E4); leap-F (A). Firewall kept: I read no other round-2 file.
Tags: `[KNOWN]` sourced in the files above · `[EST]` computed here · `[UNKNOWN]` needs a head.

---

## 0. The assumption to break

Scratch-model §4.4 writes the pattern in **hand coordinates** (stroke length, reciprocation frequency, per-finger phase), and every machine so far lost something projecting that hand onto its mechanism. The pressure-gated orbit has **native coordinates**: orbit phase φ and frequency f, pad drift velocity v_d, per-pin windows [φ₁, φ₂], and a per-stroke choice between two slowly slewed force rails. In them some primitives get easier, some harder, and some appear that no hand could play. A second assumption sits underneath: the pattern is **timeless and open-loop**. It ignores receptor recovery times and never learns. This file writes the pattern natively, then adds attention, learning, replay and a receptor-timed scheduler.

---

## 1. The one equation, and the master knob κ

Put the drift along +x and let the orbit run counter-clockwise. A pin's velocity in the scalp frame is

  **v = v_d·x̂ + u·(−sin φ, cos φ)**, with orbit speed u = 2πf·r.

Define **κ = v_d / u**. Then:

- scalp-frame speed is u·√(1 + κ² − 2κ sin φ), which runs from u(1−κ) to u(1+κ);
- for κ < 1 the pin moves *backward* relative to the drift over an arc of 180° − 2·asin κ;
- for κ > 1 it never moves backward, and its heading wanders within ±asin(1/κ).

**κ is the master mode knob.** The four regimes are four families of primitive:

```
 κ ≈ 0 (pad parked)         κ ≈ 0.3–0.6 (walking)      κ ≥ 1.3 (curtate)         f = 0 (orbit parked)
   window arcs on a circle    C-arcs that walk forward     continuous bending path    straight drift
      ╭─╮   ╭─╮               ⊂  ⊂  ⊂  ⊂  →                ∿∿∿∿∿∿∿∿∿ →              ────────── →
   rakes (P1), spider (P4)    travelling circles (P3)      sweep with wander (P2')    sweep (P2)
   pins down only in windows  lift on the backward arc     pins may stay down         pins stay down
```

**Firmware invariant (H-5.2, H-5.3, H-5.7 in one line):** a loaded window may not contain a scalp-frame velocity reversal, a self-crossing, or a speed below 0.3·u, and its heading may rotate at most 90° (150° in P3). So every landing and lift happens while moving (H-5.3), and because all pins ride one rigid pad, **tip spacing never changes in contact** (H-5.6 by construction).

**Coupling cost.** A two-window rake gives 2f strokes/s at u = π·r·(strokes/s): at r = 20 mm, 2 strokes/s already means 126 mm/s, where a hand gets 4 strokes/s at 120 mm/s. **The orbit's stroke rate is half the hand's at equal speed** `[EST]`. Fixes: r = 10 mm (4 strokes/s at 126 mm/s, 14 mm chords), or interleaved pin groups (A on 0°/180°, B on 90°/270°: a cross-hatch). Hence this layer's one hardware request: **selectable r** (free on an x–y servo orbit; a 2-step 10/20 mm eccentric otherwise).

| r (mm) | u at f = 0.25 / 0.5 / 1.0 / 1.5 Hz (mm/s) | chord at Δφ = 30 / 45 / 60 / 90° (mm) |
|---|---|---|
| 10 | 16 / 31 / 63 / 94 | 5 / 8 / 10 / 14 |
| 15 | 24 / 47 / 94 / 141 | 8 / 11 / 15 / 21 |
| 20 | 31 / 63 / 126 / 188 | 10 / 15 / 20 / 28 |

Force palette: 7 mm bore (38.5 mm²); 2 / 5 / 9 / 13 kPa give 0.08 / 0.19 / 0.35 / 0.50 N; relief cap 40 kPa = 1.54 N `[EST]`. Each pin picks **rail A or B per stroke** (two valves, leap-B L1), and the rail setpoints slew over 0.5–1 s per phrase. Force thus has two timescales: per-stroke jitter (A/B ≈ 0.7×/1.3× target) and per-phrase level (the build). Never PWM a valve (Pacinian buzz).

Assumed pad: **7 pins, hex, 20 mm pitch**, ~70 mm across; rows of 3 lie on three axes, so a "row of fingers" can sit perpendicular to six headings.

---

## 2. Five candidate leaps

### LEAP D1: THE κ-GRAMMAR. Every primitive becomes a phrase in native coordinates, and four new ones appear

**(a) Assumption broken.** That primitives are separate motion programs. That P2 sweeps need a long stroke mechanism. That circles are banned (H-5.7).

**(b) Principle and parameter table.** A *score* is a list of phrases. A phrase is (region, κ-regime, f, r, v_d path, pin set, window rule, rail pair (A, B), p_B, landing jitter σ, dwell D). A bar is one orbit revolution. A stroke token is (pin, φ_c, Δφ, rail, onset offset).

| Primitive | f (Hz) / r (mm) | v_d (mm/s), κ | Windows | Pins | Rails (N), p_B | σ (ms) | D |
|---|---|---|---|---|---|---|---|
| **P1 rake** | 0.8–1.5 / 15–20 (10 for brisk 4/s) | 3–10 (κ ≤ 0.1); drift is how H-5.5 is met: 20 mm per 8 strokes | 2 per rev on axis ψ ± 180°, Δφ 60–80° (15–26 mm); against-lie windows only if chord ≤ 25 mm | row of 3–5 ⟂ axis | 0.25 / 0.40, 0.4 | 20–80, redrawn each stroke | 4–10 s |
| **P2 sweep** | orbit parked | 40–90, path 60–150 mm | continuous; lift at path end, return lifted | 3–4 abreast ⟂ travel | 0.15 / 0.30, 0.3 | landing only | 2–6 sweeps |
| **P2′ bending sweep** (new) | 0.25–0.4 / 20 | 50–80, κ 1.3–2 | continuous, heading wanders ±30–50°, lateral ±r | 2–4 | 0.15 / 0.30 | — | 2–4 sweeps |
| **P3 travelling C** (newly legal) | 0.6–1.0 / 15 | 25–40, κ 0.3–0.5 | one window per rev, 150°, centred on drift heading; lifted over the backward arc (145–120°) | 2–4 | 0.30 / 0.45, 0.5 | 20–60 | 2–6 s |
| **P4 spider** | 1.0–1.5 / 15–20 | 0–10 | per pin 1–2 random windows per rev, Δφ 30–45° (8–15 mm, 70–125 ms) | all 7, independent phases | 0.10 / 0.20, 0.5 | inherent | 2–6 s |
| **P5 rest / listen** | orbit stopped | 0 | 2–4 pins at 0.1 N for ≤ 1 s, valves sealed (D3 sip) | 2–4 | 0.08–0.12 | — | 0.3–1 s |
| **P5 lift** | any | any | all vented | — | — | — | 0.3–3 s |
| **P6 region change** | any | ≤ 80, all lifted (H-5.8) | first bar = "arrival": rail A only, needle-valve fill 0.2–0.5 s | — | ≤ 0.15 | — | 0.3–1.5 s |
| **P6 slow build** (session) | — | — | mix goes P7/P2 → P2/P3 → P1/P4 | — | setpoints ramp 0.1 → target over 90–180 s | — | 2–3 min |
| **P7 CT trace / edge** | 0.25–0.4 / 15–20 (24–50 mm/s) | 0–15 | 1 window per rev, 60–90° | 1–2 | 0.10 / 0.15 | — | 3–6 s |
| **N1 hover spiral** (new) | P1 or P4 settings | pad circles a target at R 15–25 mm, 5–8 mm/s | as P1/P4 | as P1/P4 | as P1/P4 | as P1/P4 | 10–30 s |
| **N2 tease → relieve** (new, opt-in) | tease: 1.5 / 15 | 0 | tease: short windows on the 2 kPa canopy rail (≤ 0.06 N net) for 0.5–2 s; gap U(0.3, 1.5) s lifted; relieve: P1 at the same pad position | 2–4 | tease 0.06; relief 0.35–0.45 | — | ≤ 1 per 2–3 min |

N1 holds one target without breaking the 8-stroke patch limit: on a 20 mm hover circle at 6 mm/s, 8 strokes at 2.5/s take 3.2 s, in which the patch centre moves ~20 mm `[EST]`.

**Newly possible versus every earlier design:** (1) per-stroke heading over 360° with no yaw servo; (2) hair-legal circles (P3); (3) sweeps with built-in wander (P2′); (4) dwell without re-stroking a patch (N1); (5) "same patch, light then firm" with millimetre registration (N2); (6) two pin subsets on incommensurate window rates (every rev vs every 4/3 rev), a pattern with no common period from one motor.

**(c) Sensory variables.** §7 rank 8 (direction) goes from fixed to per-stroke; rank 9 (length) spans 5–28 mm per window and 60–150 mm per sweep; rank 4 (speed) spans 16–188 mm/s, reaching both the CT and scratch bands; rank 1 gains a categorical dimension of eight families. Leap-A's carrier + grain is P1/P4 at v_d 20–50 mm/s.

**(d) Plausibility.** All rows sit inside leap-B's envelopes (30–60 ms gates vs ≥ 70 ms windows, 0.08–0.5 N, ≤ 200 mm/s). P4 at 30° and 1.5 Hz (56 ms) is below the gate limit, so it needs 45° windows or latency ≤ 40 ms. P2 needs pad travel at 40–90 mm/s: trivial for a virtual pin-field pad, but a physical mechanism must be specified for it (the director's 2–5 cm/s drift is too slow).

**(e) Cheapest experiment ($0, one evening).** The constrained-hand cue-card test in §4.

**(f) Combines.** It replaces §4.4's generator and feeds D2–D5; it needs leap-B L1 + L2 and selectable r.

**(g) Why it might not work.** The half-lifted orbit may feel "dabby" beside a hand's continuous reciprocation. P3 and P2′ in long hair are untested against H-5.7 `[UNKNOWN; wig test]`. A 7-pin hex gives at most 3 pins in a row, one fewer than a hand.

---

### LEAP D2: ATTENTION. Contingent behaviours that read as "someone is paying attention"

**(a) Assumption broken.** That irregularity is the human signature. Leap-E E3 argues that the signature is **contingency**: lagged, imperfect responses to the person.

**(b) Principle.** A salience map over the scalp in 15 mm cells (about 110 cells on the top of the head), with value V(cell) = learned preference (D3) + recent hits. Seven behaviours sit on top:

| Behaviour | Trigger | Response | Lag, probability | Limit |
|---|---|---|---|---|
| **Stay** | "yes" press, or lean ≥ 0.5 mm common-mode for ≥ 1 s | extend the phrase 4–10 s, switch to N1 hover on this cell, vary **one** feature (never replay identically) | 0.3–1.5 s, p 0.7 | ≤ 3 extensions (≤ 40 s inside 50 mm); H-5.5 |
| **Return** | cell tagged "hit" | revisit after 30–90 s (≥ CT recovery), with a variation | p 0.5 per eligible gap | ≤ 3 returns per hit, value decays ×0.6 each time |
| **Build** | phrase starts on a hit cell | 3–6 bars of crescendo: p_B 0.2 → 0.7, f +20 %, σ narrows 80 → 30 ms | — | region force bound |
| **Release ("let it ring")** | after a build peak, or ≥ 2 s stillness | P5 lift 0.5–1.5 s, then P7 or move | — | — |
| **Arrive** | every region change | first bar light (≤ 0.15 N) with short windows, as if "feeling for the spot" | — | — |
| **Tease → relieve** | scheduler, opt-in, only on regions where it tested positive | N2 | gap U(0.3, 1.5) s | ≤ 1 per 2–3 min |
| **Wander** | no reward for 20–30 s | adjacent move (p 0.7), far jump (0.2), pause (0.1) | — | — |

**(c) Sensory variables.** §7 ranks 13–14 (region, dwell) go from random walk to Michael-directed. Component E (attribution) gains its cheapest behavioural cue. The deliberate lag of more than 200 ms keeps the device "external" rather than self-controlled (leap-E §1).

**(d) Plausibility.** It is pure firmware, about 200 lines on top of the engine. The probabilities and lags come from leap-E E3 and leap-A L3/L5 and are starting values.

**(e) Cheapest experiment ($0).** Block KLA vs KL in §4: on a press the helper holds a STAY card (hover, vary one feature) and re-inserts it as RETURN 6 cards later. Michael rates pleasure and "they were paying attention".

**(f) Combines.** It sits between D3 (values) and D5 (constraints), and works on any mount. Lean needs a world-grounded pad (D3).

**(g) Why it might not work.** It can feel needy. Hit tags from a sparse button may be mostly noise. Release pauses may read as the machine stalling.

---

### LEAP D3: SIP-SENSING + A REGIONAL THOMPSON LEARNER. The pins listen during pauses, and a button teaches the device in about four short sessions

**(a) Assumption broken.** That learning needs extra sensors and long training. Also that a constant-force pin cannot sense, since an open pin pushes P·A at any height and is therefore blind to position.

**(b) Principle, part 1: sip-sensing.** During a P5 rest (played every 10–20 s anyway), 2–4 resting pins are **sealed** at 2–3 kPa for 0.5–1.5 s. A sealed pin is a gas spring, so its desk-box sensor reads height: with V ≈ 3.4 ml (1 m of 1.5 mm tube plus bore), Δp = P_abs·A·Δz/V ≈ **1.15 kPa/mm** (1.6 adiabatic); k ≈ 0.044 N/mm, so a 5 mm lean lifts force only from 0.10 to 0.32 N `[EST]`. At ~50 Pa noise that resolves ~0.05 mm. **Common-mode rise across sealed pins = the head leaning in** (leap-E E3); the differential is local contour (free mapping); two sips at 2 and 4 kPa give pile compliance, i.e. canopy vs skin, turning §7 rank 2 into a measurement `[UNKNOWN]`. Breathing (1–2 mm, 0.2–0.5 Hz) is rejected sip-to-sip. Lean exists only on a **world-grounded** pad; head-borne, use the button.

**(b) Principle, part 2: the learner.** Context c = region (6: crown, top, occiput, L-parietal, R-parietal, nape/edge). The per-region decision x has 5 continuous parameters:

| x | Range | Prior mean |
|---|---|---|
| F (rail target) | 0.10–0.50 N | 0.25 N; nape/edge ≤ 0.15 |
| u (orbit tip speed) | 30–180 mm/s | 100 mm/s |
| ψ (axis vs hair lie) | with / across / against, as an angle 0–180° | 90° |
| σ (landing spread) | 0–80 ms | 40 ms |
| D (dwell) | 4–25 s | 10 s |

The grammar and D5 choose the primitive (variety); the learner tunes x.

- **Model.** Bayesian logistic regression on quadratic features (1, xᵢ, xᵢ²: 11 shared weights) plus per-region offsets on (1, F, u, ψ) (24 more), N(0, 1) priors on standardised features, offsets shrunk toward shared. **Nuisance regressors** (D5 familiarity h, minutes into session, session index) stop it blaming a parameter for boredom.
- **Reward.** y = 1 if "yes" is pressed from 0.5 s after phrase start to 1.5 s after its end; lean ≥ 0.5 mm adds a 0.5-weight pseudo-observation. The session-end 0–10 rating is a session-level check, so the learner cannot just chase intensity.
- **Policy.** Thompson sampling within each region's safe box; exploration doubles as irregularity.
- **Volume.** ~5 phrases/min over safety §2.5's 5 → 10 → 20 → 20 min ramp gives ~275 labelled phrases for 35 weights. At a press rate of 0.2–0.4 that should place force and speed optima within about ±25 % per region `[EST]` (leap-D cites human-in-the-loop BO finding a 2-parameter exosuit optimum in ~21 min).

| Session | Length | Content |
|---|---|---|
| S0 calibration | 20 min, no learning | grain map per region (helper draws arrows on a head diagram); per-region force ladder (0.1 / 0.2 / 0.3 / 0.45 N rakes, "too light / right / too much") sets each safe box; per-pin latency and sip baselines |
| S1 | 5 min | learning; high exploration (prior variance ×2) |
| S2 | 10 min | learning |
| S3 | 20 min | learning; 3 A/B pairs ("this or the last?") at minutes 5, 10, 15 |
| S4 test | 3 × 6 min, blind, counterbalanced | learned+D5 vs §4.4 default vs learned frozen (no D5); rating every 60 s. **Pass: learned beats default by ≥ 1.5/10 over minutes 3–6** |

**(c) Sensory variables.** §7 ranks 3, 4 and 8 are set *per region for Michael*, which can correct the program's factor-of-2–3 force dispute (leap-D §0). Rank 2 becomes measurable through the compliance sips.

**(d) Plausibility.** The XGZP6847A sensors are already in leap-B's box; sealing is a valve state; the learner is ~150 lines of numpy. Open: sensor drift and seal leakage over 1.5 s `[UNKNOWN]`.

**(e) Cheapest experiment ($5 + $0).** Bench: one leap-B pin, valve closed, nail on a kitchen scale; push 1, 2, 5 mm with a feeler stack and log Δp (pass: linear within 10 %, leak < 0.1 kPa/s). Human: a laptop runs the learner and prints the next cue card, the helper plays it, Michael holds a $3 button.

**(f) Combines.** It sets D2's V(cell) and D1's phrase parameters. The lean channel favours a world-grounded pad (pillow, frame arm).

**(g) Why it might not work.** Judging breaks the trance. Sparse presses at p ≈ 0.2 may leave the 5-D optimum flat. Preferences drift across days. Breathing may swamp lean on some postures.

---

### LEAP D4: SCORE TRANSCRIPTION. A recorded human becomes orbit windows and travel paths

**(a) Assumption broken.** Leap-D D4: that faithful replay needs per-finger tangential actuators, a moving four-finger hand. It doesn't, if the recording is **transcribed** into the native score rather than replayed as trajectories.

**(b) Principle.** The input is leap-D's scratch roll (hand x, y, yaw in the head frame; f₁..f₄ and contact flags at 200 Hz).

```
 scratch roll ─► low-pass 0.4 Hz ─────────────► pad travel path p_d(t)  (clamped v_d ≤ 80 mm/s, face fence)
      │
      └► residual per finger, segmented at contact flags ─► stroke list {t_k, heading h_k, length L_k,
                                                                     speed s_k, force F_k, finger i}
             │
             ├► orbit speed per bar: u ≈ median s_k (f clipped 0.25–1.5 Hz, r chosen from L_k)
             ├► phase-lock: dynamic programming over per-bar speed trims (±25 %) and onset shifts (≤ ±60 ms)
             │   so that φ(t_k) = h_k − 90°  (the CCW orbit's heading is φ + 90°); unplaceable strokes are dropped
             ├► window Δφ_k = L_k / r, clipped 30–90°
             ├► pin = hex pin nearest finger i after rotating by hand yaw; rail pair = 30th/70th percentile F per phrase
             └► SCORE  +  fidelity report (heading, length, onset, force errors; drop rate)
```

Fingers moving in different directions at one instant (P4) are time-multiplexed into neighbouring windows; everything else maps one-to-one. The bigger win is a by-product: transcribed scores share the generator's format, so **the grammar's distributions can be fitted to human scores**, 1/f stroke correlations included (leap-D §3.3). The generator then speaks with human statistics and never repeats a recording.

**(c) Sensory variables.** §7 rank 1 (structure) and rank 6 (asynchrony, kept as recorded onset offsets). Expected fidelity `[EST]`: P1 heading ≤ ±10°, onset ≤ ±40 ms, force ±0.06 N (rail quantisation); P2 exact via drift; P4 smeared 60–120 ms by multiplexing. Leap-D's tolerances are ±10° and ±0.05 N.

**(d) Plausibility.** Offline Python with a small DP. The pad must reach recorded drift speeds (≤ 80 mm/s after low-pass).

**(e) Cheapest experiment ($0).** Film the helper scratching Michael for 30 s (dot-marked nails, 240 fps). Hand-transcribe it into 15–20 cue cards (heading as a clock face, length, light/firm, fingers). The helper **replays the cards**, blind A/B against free scratching on the same region. If Michael can't tell, transcription keeps what matters.

**(f) Combines.** It is leap-D's best bet (D2 capture plus D1 library) without D4's per-finger hardware. It feeds D1's priors and D3's arm library.

**(g) Why it might not work.** If human magic lives in sub-stroke force envelopes or in true simultaneous multi-direction P4, two rails and one shared velocity cannot carry it.

---

### LEAP D5: THE FATIGUE LEDGER. Schedule by receptor recovery times, not by jitter

**(a) Assumption broken.** That anti-habituation means randomising parameters. Jitter slows central habituation, but it cannot rest a fatigued peripheral class (leap-A L4), and it ignores the known 3–5 minute decline.

**(b) Principle.** Each 15 mm cell keeps a ledger with one state per channel. Every candidate phrase is scored against the ledger before it plays.

| Channel | What it adapts to | Time constant `[KNOWN]` (source file) | Ledger rule |
|---|---|---|---|
| Pacinian (FA2) | vibration | < 1 s (scratch-model §2.1) | no PWM; ≤ 8 valve events/s per pin; nothing > 20 Hz |
| Hair and field units (Aβ RA) | held or identical deflection | fire only during motion (§2.1) | never load a pin stationary > 1 s (2 s safety cap); ≥ 1 feature changes per stroke (σ, rail, Δφ) |
| SA1 | sustained indentation | slows within seconds (§2.1) | rests ≤ 1 s loaded |
| CT | repeated slow stroking of one site | after-effect lasting seconds to minutes; labs space stimuli 10–30 s (leap-A §0.1, Vallbo 1999) | F_CT(cell) += 1 per pass at < 100 mm/s, τ_rec = 20 s; no slow pass while F_CT > 0.5 |
| Central "machine" percept | periodic structure | 10–30 s (§4.3) | familiarity h(feature) with τ = 90 s; the next phrase must change ≥ 2 features with h > 0.5; continuous parameters follow pink (1/f) noise, not i.i.d. |
| Satiety | repeated pleasant touch | decline over the first 100–300 s, then a plateau; a third of people show none; satiety at 3 cm/s but not at 0.3 or 30 cm/s (leap-A §0.1) | build for 2 min; schedule the biggest novelty (far region, P2′, N2) at minutes 3–6; alternate speed regimes, so ≤ 40 % of any 60 s in the 20–50 mm/s band |
| Hair matting | (mechanical) | 8 strokes per ±15 mm (H-5.5) | hard counter, reset by a ≥ 20 mm move or a with-lie comb-out |
| Abrasion | (mechanical) | ≤ 50 passes/min per spot (§3.24) | hard sliding window |

**(c) Sensory variables.** §7 rank 1 and §9 Q5/Q10: the *slope* of pleasure over 10–20 min. Target: flat after minute 3, against the decline over the first 100–300 s reported for brushing `[target]`.

**(d) Plausibility.** It is bookkeeping, ~110 cells × 5 floats. The time constants are literature values from forearms, so they are starting points that S0–S3 refine.

**(e) Cheapest experiment ($0).** Block KL vs K in §4 (same deck, with and without the ledger filter); compare the minute 3–6 slopes.

**(f) Combines.** D5 is the filter between D1, D2, D3 and the player. It is what keeps D2's "stay" from wearing a spot out.

**(g) Why it might not work.** Michael may be in the third that doesn't habituate. Forearm CT constants may not transfer to the scalp. The constraints may over-restrict and make the pattern feel restless.

---

## 3. Pattern engine (pseudocode)

```python
# one score format for generator, learner and replay; the player is the only thing that touches valves
loop every bar (one orbit revolution, 0.67–4 s):
    sense  = sip_readings_if_rest() ; press = button_events()          # D3
    attn.update(press, sense.lean, pad.cell)                           # D2: hits, stay/return queue
    ledger.decay(dt) ; ledger.add(last_bar_passes)                     # D5

    if phrase.done or attn.wants_change():
        if replay_mode: cand = replay_score.next_phrase()              # D4 transcribed phrases
        else:
            region = attn.pick_region(ledger, learner.V)               # stay / return / wander / build
            prim   = grammar.pick_primitive(session.envelope, ledger)  # slow build, novelty at min 3–6
            x      = learner.thompson(region) if learn else priors[region]
            cand   = grammar.compose(prim, region, x, rng_pink)        # κ regime, f, r, windows, rails, σ, D
        phrase = ledger.filter(cand) or grammar.fallback_lift()        # H-5.5, CT, 2-feature novelty, abrasion
        rails.slew_to(phrase.rail_A, phrase.rail_B, t=0.5)             # per-phrase force level
        if region != pad.region: player.play(P6_transition(region))    # all pins vented while travelling

    bar = phrase.next_bar(attn.modifiers())                            # build crescendo, hover spiral, release
    for tok in bar.tokens:                                             # (pin, φc, Δφ, rail, onset)
        assert window_invariant(tok, κ=bar.v_d / bar.u)                # no reversal/self-cross, speed ≥ 0.3u
        t_open  = orbit.time_at(tok.φc - tok.Δφ/2) + tok.onset - latency[tok.pin]
        t_close = orbit.time_at(tok.φc + tok.Δφ/2) - latency[tok.pin]
        valves.schedule(tok.pin, tok.rail, t_open, t_close)
    orbit.set(bar.f, bar.r) ; pad.follow(bar.v_d_path)
    log(bar, press, sense)                                             # learner gets y per phrase
# hardware below firmware: relief valve 40 kPa, de-energised valves vent (all pins lift), hold-to-run, e-stop
```

---

## 4. The cheapest test: a helper plays the machine from cue cards ($0, one evening, about 75 min)

Every leap above can be checked before a valve is bought, because a hand can be made to obey the machine's constraints.

**Constrained-hand technique (5 min practice).** The helper's hand circles flat over the scalp like polishing a table, to a metronome (60–90 bpm = 1–1.5 Hz). Touching nails move together and touch only on the arcs a card names ("12–2 o'clock and 6–8"), so contact never reverses; "drift" means the circle walks slowly in a given direction. Card fields: region, primitive, fingers, arcs (clock face, 12 = toward crown), force (light/medium/firm), bpm, drift, dwell. A laptop script prints the decks.

| Block (6 min each, blind order, Michael rates every 60 s and presses "yes") | Tests |
|---|---|
| **FH**: free hand, helper's own scratching | reference |
| **R**: random deck from §4.4, written in hand terms | baseline engine |
| **K**: κ-grammar deck (D1), constrained hand | does the orbit's grammar lose anything vs FH? |
| **KL**: K deck filtered by the D5 ledger | slope at minutes 3–6 |
| **KLA**: KL plus D2 cards (STAY / RETURN on press, 0.5–1.5 s lag) | contingency |

Also, on the side, run 6 × N2 tease → relieve trials against no-tease trials (leap-A L5 rule: ≥ 1.5 points better at 2 sites), and transcribe 30 s of FH for D4.

**Decision rules:**
- K ≥ FH − 1 → the orbit's kinematics are sufficient and the pattern layer is the product.
- KL vs K, minute 3–6 slope better by ≥ 1 point → keep D5.
- KLA > KL by ≥ 1 point on "paying attention" → keep D2 and build sip-sensing.
- K ≪ FH → the half-lifted orbit is the bottleneck, so smaller r or interleaved groups go first.

---

## 5. Best bet: D1 + D5, the κ-grammar played through a fatigue ledger, as the single score format that everything else writes into

**The case.** The pressure-gated orbit is the first design whose pattern is pure data: every pin's landing, heading, length and force is a valve decision, so the score format, not the hardware, decides what it can play. One kinematic identity, with κ as the knob, turns a never-reversing orbit on a drifting pad into all seven human primitives. A single firmware invariant makes circles and long sweeps hair-legal, and four primitives appear that no hand or earlier design could play: bending sweeps, travelling circles, hover dwell and registered tease-and-relieve. The ledger makes it feel like a person over 20 minutes rather than 20 seconds. It schedules by the receptors' own recovery times (CT ~20 s, central familiarity ~90 s, satiety at minutes 3–6) instead of blind jitter, and it enforces the two hair limits (8 strokes per patch, 50 passes per minute). Attention (D2), learning (D3) and replay (D4) are just further writers into the same score, so building D1 + D5 first loses nothing and makes each later layer a plug-in. The hardware requests that fall out are small: selectable orbit radius (10/20 mm) and pad travel at up to 80 mm/s. It can be tested tonight for $0, with a helper playing printed cue cards under the machine's constraints. That evening (K vs FH) says whether the orbit's grammar matches a free hand before any valve is bought. If it does, the remaining risk lives in the tip and the hardware, and the pattern layer is solved on paper.
