# SP1 FLOAT-ARM — Test Protocols (BRIEF §19 K–P)

**Project SCRATCH · 05-engineering · 2026-10-01 · Test & Experiment Lead**
**Builds to:** 05-engineering/DESIGN-FREEZE.md (binding). **Inherits:** safety-requirements.md §2 limits, §6 template, §7 red lines; hair-interaction.md §7; tip-interface.md §9; scratch-model.md §7–9; redteam-1 ranked attacks; redteam-3 §5–7; judge-3 §0–3.
**Print and keep at the rig:** §K (one sheet, filled before every human session), §O (one sheet per trial), the Session Log and the Packing/Cleaning list at the end.

---

## 0. Conventions used throughout

**Settings notation** (every log line, every form, every table uses these codes):

| Variable | Code | Levels | How it is set | How it is verified |
|---|---|---|---|---|
| Tip | TIP | W, B45, B45-12, A45 (gated), E, H (control), P | TM1 magnetic swap | letter code under the tang (random code for blinded trials) |
| Dead weight (total on three nails) | WT | W1 = 0.9 N (bare float), W2 = 1.2 N (+30 g slug), W3 = 1.5 N (+60 g slug) | weight post | kitchen scale (§L1); ±0.05 N |
| Speed band (peak tip speed) | SPD | S1 ≈ 50 mm/s (pot 0 %), S2 ≈ 100 (pot 50 %), S3 ≈ 150 (pot 100 %) | SPEED pot at tape marks | serial echo of pot value; 240 fps video (§L4) |
| Variation | VAR | V0 = 0 %, V50, V100 | VARIATION pot at tape marks | serial echo |
| Stroke direction vs hair lie | DIR | ALONG (axis parallel to the local lie; a bidirectional stroke alternates with/against), CROSS (axis ⟂ lie). For 45° tips add the loaded-edge sense: ALONG-W (loaded stroke moves with the lie), ALONG-A (loaded stroke moves against) | aim: rotate the module about vertical with the monitor-arm joints; mount 45° tips edge-forward or edge-back | grain map (§M, pre-measure) + tape index marks on the arm |
| Engagement | E | 2 / 4 / 6 mm (contact chord ≈ 25 / 36 / 44 mm by the frozen geometry) | arm height vs. down-stop; read on the float pointer at mid-stroke | pointer reads E at mid-stroke with nails on the scalp and 0 (down-stop) at the stroke ends |
| Mode | MODE | PER (PERIODIC: fixed 18°, no pauses), HUM (HUMAN) | toggle | serial echo |
| Region | REG | CR = crown/vertex, OC = occiput | head tilt in the cradle; arm position | the scalp normal at the contact point is vertical (rail vertical ±5°, phone inclinometer on the frame) |
| Posture | POS | SEAT (seated, tabletop face cradle), PRONE (face cradle cushion on the bed) | — | — |

**Default condition D0** = W · W2 · S2 · V100 · ALONG · E4 · HUM · CR · SEAT. Everything in §N is a deviation from D0 unless stated.

**Hard limits that no protocol below may exceed** (safety-requirements §2, §7): per-nail normal force ≤ 2.4 N at the leaf hard stop; total scalp load ≤ 12 N; tangential ≤ 2.0 N before the wrist breaks away; tip speed ≤ 0.4 m/s; stroke ±28° absolute in firmware; nails rise ≥ 25 mm on loss of actuator-rail power; first human sessions ≤ 5 min continuous, then ≤ 10, then ≤ 20; any tuft pull is a stop-and-redesign event; no first human session without §K complete, the wig-head test (§L8) passed, safety glasses on.

**Trial** = one condition held for 30–90 s followed immediately by a §O form. **Session** = one sitting on one day, ≤ 25 min of total scalp exposure. **Washout** = ≥ 60 s with the hand lifted (hold-to-run released) between trials, ≥ 3 min break with the head out of the cradle every 5 trials. **Day gap** = ≥ 20 h between sessions on the same region; skip a day if any redness persists > 60 min.

---

## K. SAFETY CHECKLIST — pre-human-test, SP1 Float-Arm specific

Fill in every line with a value or N/A, date and initial. **Any unticked box or any value outside its limit blocks the human session.** Sections K1–K4 are done once per build state (re-done after any mechanical, tip or firmware change); K5 is done before *every* session.

Build state ID: ________  Date: ________  Initials: ____  Firmware version (from boot banner): ________

### K1. Visual

| # | Check | Limit | Measured / observed | OK |
|---|---|---|---|---|
| 1.1 | Printed parts: no cracks, delamination, stringing on frame, arm bracket, palm, knuckle plate, paddles, guard plate, VESA adapter | none | | ☐ |
| 1.2 | Load-bearing parts unchanged since proof test (§L6/§L7) | yes | | ☐ |
| 1.3 | All skin-accessible edges radiused: guard plate R ≥ 3 mm, knuckle plate, paddle exits, palm clamshell seam | R ≥ 1 mm (tips ≥ 0.4 mm) | | ☐ |
| 1.4 | Tape sharpness test (§L9) passed on every tip in today's set and on guard/knuckle/paddle edges | no cut through 3 layers | tips tested: ________ | ☐ |
| 1.5 | Tips seated: each TM1 tang fully home, magnet engaged, seam sleeve in place, no rock | hand pull cannot unseat; ≥ 4 N breakaway from §L6 | | ☐ |
| 1.6 | Tips: correct material, no chips, no burr (loupe), no visible wear step at the edge | | | ☐ |
| 1.7 | No fastener tip, wire, zip-tie tail or burr pointing toward the scalp; no screw head below the knuckle canopy | none | | ☐ |
| 1.8 | Gaps: paddle exit holes ≥ 4 mm clearance and covered by the TPU boot / silicone sheet; guard opening ≥ 10 mm from every moving part; **no gap 0.04–3 mm anywhere within 25 mm of hair** (palm seam sealed, TM1 seam sleeved, rail/carriage above the guard) | per DESIGN-FREEZE §1.4, §1.7 | | ☐ |
| 1.9 | Nothing rotates within 30 mm of hair: elbow horn, rail and carriage are above the guard plate | yes | | ☐ |
| 1.10 | Hair-probe: 100 µm nylon monofilament offered to every seam/gap below the guard cannot be fed in or trapped | no capture | | ☐ |

### K2. Mechanical

| # | Check | Limit | Measured | OK |
|---|---|---|---|---|
| 2.1 | **Float free:** carriage slides full travel under its own weight from the up-stop to the down-stop with the rail vertical; no catch anywhere; stiction (§L3) | F_f ≤ 0.1 N (≤ 10 % of W1) | F_f = ______ N | ☐ |
| 2.2 | Carriage travel between up-stop and down-stop | 25–30 mm | ______ mm | ☐ |
| 2.3 | **Down-stop set** for today's E; pointer reads 0 at the down-stop; thumbscrew locked (nut/threadlocker) | E = 2/4/6 mm | E = ______ mm | ☐ |
| 2.4 | **Dead weight** on the kitchen scale with the carriage floating mid-travel (§L1) | W1 0.9 / W2 1.2 / W3 1.5 N ± 0.05 | W = ______ N (slug: ______) | ☐ |
| 2.5 | Per-nail share (§L1b): heaviest nail / lightest nail | 1.2–1.6 (unequal preload intended); no nail > 0.6 N at W2 | ______ / ______ / ______ N | ☐ |
| 2.6 | **Leaf stops:** each leaf deflects to its hard stop at ≤ 2.4 N (§L2); travel 8–10 mm; returns fully with no set | ≤ 2.4 N | nail 1 ____ N, 2 ____ N, 3 ____ N | ☐ |
| 2.7 | Leaf rate (§L2) | 0.1–0.25 N/mm | ______ N/mm each | ☐ |
| 2.8 | **Wrist breakaway force measured** (§L6) in +X, −X, +Y, −Y | 1.5–2.5 N (design 2.0) | ______ / ______ / ______ / ______ N | ☐ |
| 2.9 | Tether: released hand hangs ≤ 60 mm below the carriage, cannot reach the face envelope from any stroke position | ≤ 60 mm | ______ mm | ☐ |
| 2.10 | Tip breakaway (§L6b), each tip in today's set | 4–8 N | ______ | ☐ |
| 2.11 | **Fail-safe lift measured** (§L5): nail-tip rise from working position to up-stop on magnet drop | ≥ 25 mm, ≤ 0.5 s | ______ mm, ______ s | ☐ |
| 2.12 | Lift spring holds the frame at the up-stop with the heaviest hand + W3 slug fitted; magnet re-latches at 5 V | yes | | ☐ |
| 2.13 | Firmware limit ±28° reached before any mechanical interference; at ±28° and the carriage at the down-stop the nails are ≥ 10 mm above the sphere apex plane (§L4) | yes | gap at ±28° = ______ mm | ☐ |
| 2.14 | Monitor arm: clamp tight, gas spring holds the module at the set height for 30 min with no drift; arm joints taped at the aim marks | drift ≤ 2 mm | ______ mm | ☐ |
| 2.15 | Fasteners torque-marked / nyloc / threadlocked; shake test — nothing rattles; weights captured on the post (cannot fall) | | | ☐ |
| 2.16 | Moving hand mass (carriage + wrist + hand + slug) and peak tip speed: KE | mass ≤ 160 g; speed ≤ 0.4 m/s | ______ g, ______ mm/s | ☐ |

### K3. Electrical

| # | Check | Limit | Measured | OK |
|---|---|---|---|---|
| 3.1 | Adapter: UL/ETL/CE mark visible, 5 V 4 A, output metered | 4.75–5.25 V | ______ V | ☐ |
| 3.2 | **No mains in reach:** adapter and its cord are on the floor/under the desk, > 1 m from the head and from the e-stop lead; nothing above 5 V DC on the rig; no lithium cells | yes | | ☐ |
| 3.3 | **Strain relief:** adapter cord, actuator-rail leads, hold-to-run lead and Dynamixel cable all anchored with a service loop at every moving joint (hinge, elbow); no conductor exposed; cable to the hand does not cross the hair zone | yes | | ☐ |
| 3.4 | **Rail loop** wired exactly: adapter(+) → E-STOP (NC) → HOLD-TO-RUN (NO momentary) → [Dynamixel VIN] ∥ [electromagnet]; logic on USB only | per DESIGN-FREEZE §1.10 | | ☐ |
| 3.5 | **E-stop:** press with the servo running → rail reads 0 V, servo torque gone, magnet drops, frame lifts; latches; twist-release does NOT restart motion (firmware waits for a run command / lifted position) | 0 V, lift ≥ 25 mm | ______ V | ☐ |
| 3.6 | **Hold-to-run:** release mid-stroke → 0 V on rail, lift; 10 of 10 trials; button has no latch, no tape, no tie | 10/10 | ______ | ☐ |
| 3.7 | **Fuse** in the rail at the adapter (per ELEC spec, ~1.5× running current, ≤ 4 A); correct value fitted; spare in the kit | value = ______ A | | ☐ |
| 3.8 | Polarity metered at the OpenRB VIN and at the magnet before first power-up of this build state | correct | | ☐ |
| 3.9 | Logic stays up (USB) when the rail is killed; boot banner prints the limits table (position ±28°, velocity, goal-current) | yes | | ☐ |
| 3.10 | 30-min run (§L7): XL330 case, magnet, adapter temperatures | ≤ 48 °C hand-touch, ≤ 43 °C within 10 mm of skin | ______ / ______ / ______ °C | ☐ |
| 3.11 | E-stop position: under the free hand without looking in the test posture; hold-to-run lead ≥ 1.5 m | yes | | ☐ |

### K4. Functional (bench, with the mannequin, no human)

| # | Check | Limit | Measured | OK |
|---|---|---|---|---|
| 4.1 | **Position limits:** command beyond ±28° (serial test command or pot extremes) → motion clamps at ±28°; stroke never exceeds | ±28° | max seen = ______° | ☐ |
| 4.2 | Velocity limit: SPEED pot at 100 % → peak tip speed on 240 fps video | ≤ 150 mm/s nominal, ≤ 0.4 m/s hard | ______ mm/s | ☐ |
| 4.3 | **Watchdog:** halt the firmware deliberately (serial "hang" test command or unplug USB with the rail live) → torque off within 1 s; the rail stays live but the servo is limp and the float rests at dead weight; the hand can be lifted by hand | ≤ 1 s | ______ s | ☐ |
| 4.4 | **Over-current / stall:** block the hand with the palm at mid-stroke → goal-current limit holds tangential force at ≈ 1.2 N (fish scale) and the servo does not push through; fault → torque off; re-arm required | ≤ 1.5 N | ______ N | ☐ |
| 4.5 | Start/stop only lifted: run command from any position → the servo first goes to +25° lifted, 1 s hold, then ramps; stop → finishes the stroke at +25°, torque off | yes | | ☐ |
| 4.6 | Runaway: garbage serial input, pot wiggled during run, toggle flipped mid-stroke → motion stays inside ±28°, no jump > 25° in one step, no force above cap | yes | | ☐ |
| 4.7 | Noise at the ear position (phone SPL meter, A-weighted), HUM S3 | ≤ 70 dBA hard, ≤ 60 target | ______ dBA | ☐ |
| 4.8 | Plug-pull mid-stroke ×10: lift every time, no hang-up of the frame on the up-stop, magnet re-latches when pressed down with power on | 10/10 | ______ | ☐ |

### K5. Environment and person (every session)

| # | Check | OK |
|---|---|---|
| 5.1 | Safety glasses on before the rail is powered | ☐ |
| 5.2 | Hair: tied back / clipped away from everything except the target patch; nothing longer than 15 cm hangs toward the elbow or rail; no hair products that stiffen or tangle (gel, spray) | ☐ |
| 5.3 | No jewelry, no glasses chain, no hood/hoodie strings, no lanyard, no earbuds cable | ☐ |
| 5.4 | Clear space: 0.5 m around the rig, nothing on the desk that could fall on the head, chair stable, cradle clamped | ☐ |
| 5.5 | Phone nearby, unlocked, on the desk: timer running, voice-memo ready, 240 fps ready; a second person informed where you are if no helper is present | ☐ |
| 5.6 | E-stop under the free hand; hold-to-run in the other hand; both tested once (press/release) with the rig over the mannequin before moving it over the head | ☐ |
| 5.7 | Tips wiped with 70 % IPA ≥ 1 min ago; hand/guard lint-rolled; black cloth under the cradle for shed-hair count | ☐ |
| 5.8 | Scalp inspected (photo, flash) — no existing broken skin, rash, sunburn on the target region; not within 24 h of a haircut or chemical treatment | ☐ |
| 5.9 | Settings for the session written on the Session Log *before* starting; serial echo matches | ☐ |
| 5.10 | Session timer set to the stage limit (2 / 5 / 10 / 20 min) with an audible alarm | ☐ |

Signed: ______________  Time: ______

---

## L. BENCH TESTING (non-human) — in order

Run L1–L12 in this order on each new build state; L8–L12 again whenever a tip or hand part changes. Equipment list for the whole section: kitchen scale (1 g), 0–5 N fish/spring scale or 5 kg luggage scale, steel ruler and a 150 mm caliper, phone (240 fps slow-motion, SPL-meter app, inclinometer app, timer), 10× loupe, IR thermometer, 100 µm nylon monofilament (fishing line), a 10 mm rod + 3 layers of 50 µm tape, carbon paper or a whiteboard marker, a 180 mm sphere or hairless styrofoam/foam head (R ≈ 90 mm at the apex — a 90 mm *radius* ball), a cosmetology real-hair training head (one trimmed to 3–5 cm, one long), a synthetic Kanekalon wig as the conservative wrap screen, black card/cloth, lint roller, 15 g / 50 g / 100 g weights with thread and a pulley (or a smooth rod edge), hygrometer, M8 slug sets pre-weighed (+30 g, +60 g).

### L1. Dead-weight calibration (kitchen scale)

**Setup.** Rig over the kitchen scale, rail vertical (inclinometer ±1°), servo torque OFF (USB only, rail dead — the frame will be at the up-stop; hold it down by hand against the stop, or latch with the rail live and the hold-to-run taped **only for this bench test, label the tape, remove it after**). Lower the arm until the nails rest on the scale pan with the carriage floating mid-travel (pointer ≈ 12–15 mm).
**Procedure.** (a) Tare the scale with nothing touching. (b) Read total W with no slug, +30 g slug, +60 g slug. Repeat each 3× lifting the hand off between reads. (c) **Per-nail share:** place a 10 mm block under one nail only (the other two in air) and read; repeat per nail. (d) Record the pointer reading at which the scale first reads > 0 while lowering slowly (float engages) and the reading at the down-stop (should jump to the arm's full weight — do not leave it there).
**Pass.** W1 = 0.90 ± 0.05 N (92 ± 5 g), W2 = 1.20 ± 0.05, W3 = 1.50 ± 0.05; three reads within ±2 g; per-nail shares in the ratio ≈ 0.8 : 1.0 : 1.2 (±0.1), no nail above 0.6 N at W2 or 0.75 N at W3; the sum of per-nail reads = W ± 10 %.
**If it fails.** W1 > 0.95 N: the bare floating mass is too high — remove the slug post, lighten the wrist, or fit the trim-spring hook (see §Q). Shares outside ratio: adjust leaf length/shim. Sum ≠ W: a leaf is preloaded against its stop harder than its share — the stop preloads must sum below W (Red Team 1 attack 5).

### L2. Leaf rate and stop force

**Procedure.** Hand off the rig (or carriage locked at the up-stop). Press one nail onto the kitchen scale with the ruler against the knuckle plate; read force at 2, 4, 6, 8 mm of leaf deflection and at the hard stop. Repeat per leaf. Then push to the stop five times and re-check the free height (set).
**Pass.** Rate 0.1–0.25 N/mm (slope of the 2–6 mm points); hard stop reached at 8–10 mm; force at the stop ≤ 2.4 N; zero permanent set (free height within 0.2 mm). Preload (force at first movement) per leaf recorded; sum of preloads ≤ 0.3 N above W/3-shares.

### L3. Float friction (stiction)

**Procedure.** (a) Rail horizontal (rotate the frame on the bench): thread over a smooth edge from the carriage, add grams until the carriage first moves; F_f = m·g. Three directions of start (from the up-stop, from mid, from the down-stop). (b) Rail vertical, hand on the kitchen scale: lower the arm 1 mm at a time with the monitor arm and log scale reading vs pointer; then raise it. The hysteresis between the lowering and raising curves = 2·F_f.
**Pass.** F_f ≤ 0.1 N by both methods (≤ 10 % of W1); no position along the travel with F_f > 0.15 N; hysteresis loop closes with no step > 0.1 N. **Fail:** re-oil the MGN9H, check rail straightness and bolt stress; check the tether cord and the Dynamixel cable are not touching the carriage.

### L4. Lift-off chord on the R 90 mm form

**Setup.** Hairless foam head or 180 mm sphere clamped so its apex is at the nominal O. Carbon paper (or marker ink on the tips) over the apex. Rail live, PER mode, S1.
**Procedure.** (a) Set E = 4 by arm height (pointer reads 4 at mid-stroke, 0 at the ends). (b) Run 10 strokes; measure each nail's mark length and its centre offset from the mid-stroke line. (c) Repeat at E = 2 and E = 6. (d) 240 fps video from the side at ±25°: measure the visible gap between tip and surface at the stroke ends. (e) At ±28° (firmware limit test command), carriage at the down-stop: gap to the surface.
**Pass.** Mark lengths ≈ 25 / 36 / 44 mm at E = 2 / 4 / 6 (±5 mm); three nails all mark; mark centres within ±5 mm of mid-stroke (else the aim/tilt is off); visible gap ≥ 5 mm at ±25° and ≥ 10 mm at ±28°; no mark continuity through the stroke end (i.e. lift really happens, no scuff at reversal). Also measure peak tip speed from the video at S1/S2/S3 (frames to cross a 20 mm mark): record for §0.

### L5. Fail-safe lift

**Procedure.** Rig over the foam head, hand on it at E = 4, HUM S2. Ten times each: (a) release hold-to-run, (b) press e-stop, (c) pull the adapter plug, (d) kill USB with the rail live (watchdog path — expect limp, not lift; confirm the hand can be lifted by hand at dead weight). For (a)–(c) measure on 240 fps video: time from the event to the first nail movement and the final nail-tip height above the surface (ruler in frame). Also test from the stroke ends and from mid-stroke, with W3 fitted.
**Pass.** Lift ≥ 25 mm in ≤ 0.5 s, 30/30; the frame stays at the up-stop indefinitely; re-latch takes one hand pressing the frame down with power on; nothing dislodged (tips, slug). (d): torque gone ≤ 1 s, hand liftable by hand with ≤ W + 0.2 N.

### L6. Breakaway

**(a) Wrist.** Hand seated, carriage at mid-travel, fish scale hooked to the knuckle plate: pull slowly in +X, −X, +Y, −Y until release; read the peak. Also pull straight down (−Z) — must NOT release below 5 N (it is the dead-weight path). Re-seat and repeat 3× per direction. **Pass:** 1.5–2.5 N tangential each direction; −Z ≥ 5 N; the released hand swings on the tether without reaching below the knuckle plane − 60 mm; re-seats by hand and keys to the same orientation.
**(b) Tips.** Each tip in a holder, tip down, hang weights from the tip: record the pull-out force. **Pass:** 4–8 N; proof-load each tip to 3× its rated 0.8 N (2.4 N) on the leaf hard stop without cracking (loupe after).

### L7. 30-minute cycle (endurance, thermal, noise, firmware)

**Setup.** Foam head, E = 6, W3, HUM S3 V100 (the worst case for current and heat). Phone SPL meter at the ear position (≈ 120 mm from the module, where the ear will be). IR thermometer.
**Procedure.** Run 30 min continuous, hold-to-run taped **for this bench test only** (label, remove after). Log at 0/10/20/30 min: XL330 case temperature, magnet temperature, adapter temperature, dBA (Leq over 30 s), stroke count from serial, any fault lines on serial, pointer behaviour (any sticking), gas-arm height drift. Afterwards: shake test, fastener check, loupe on the tips, re-run L1 (W must not have changed), L3 (F_f).
**Pass.** Zero faults, zero resets, zero magnet drops; temperatures ≤ 48 °C hand-touch / ≤ 43 °C within 10 mm of skin (guard underside); ≤ 70 dBA (≤ 60 target); drift ≤ 2 mm; no loosening; W and F_f unchanged within tolerance; stroke count consistent with 1–3 strokes/s.

### L8. Wig-head hair-entanglement test (real-hair mannequin)

This is the hair gate (safety red line 12, hair-interaction §7.4). Run on the real-hair head at both hair lengths and on the Kanekalon wig; run the full set once per build state and the 20-min endurance again after any hand/tip/boot change.

**Instruments.** Black card under the head; lint roller; hygrometer (record RH; repeat L8.4 below 35 % RH if the first run was above 50 %); 240 fps phone with a side lamp and a macro clip lens; 15 g / 50 g / 100 g tether weights.
**Baseline.** Comb the wig 20 strokes with a wide-tooth comb; count shed hairs on the card = combing baseline B (per 20 strokes). Record comb-through force with the fish scale (pre).

1. **Static reach** (hand-held wand or the rig at rest): press each tip onto the hair at 0.3, 0.5, 1.0 N (kitchen scale under the head); side photo through the pile. Pass: visible edge-to-scalp contact at ≤ 0.5 N for all tips except H at both hair lengths.
2. **Single-stroke drag** (optional if a luggage scale sled is available): with-/cross-/against-grain at S1, W2; drag ≤ 0.6 N per hand with-grain; against-grain not > 3× with-grain and not rising along the stroke.
3. **Reversal / loop test.** 50 reversals PER S2 W2 E4 ALONG, then 50 CROSS, on the real-hair head; 240 fps on 20 of the reversals. Count loops, knots, shed. Pass: zero loops/knots; on video, every strand released before the reversal (no strand visibly tensioned across the reversal frame); lift visible at both ends.
4. **Tethered-strand weight test (snag-yield).** Tie one hair (or 70 µm monofilament) to the 15 g weight over the pulley so the strand lies across the stroke path at scalp level; run 20 strokes HUM S2 W2. Then 50 g, then 100 g. Pass: the 15 g weight is never lifted (snag-yield ≤ 0.15 N target); the 50 g weight is never lifted (≤ 0.5 N hard); if the 100 g weight lifts, the wrist must break away before it rises > 20 mm. Record which element yielded (leaf torsion, float, wrist).
5. **Wrap test.** Long wig draped over the running module in every orientation the head could take (hair toward the elbow, toward the rail, over the guard edge), 5 min HUM S3 V100. Inspect the elbow horn, rail, carriage, hinge, tether cord, cable. Pass: zero wraps, zero strands in any gap.
6. **Gap probe (running).** With the mechanism running at S1, offer single hairs and small (5-strand) tufts with tweezers to the paddle boots, TM1 seams, palm seam, guard opening, tether entry. Pass: zero captures.
7. **20-min endurance / matting.** HUM S3 V100 W3 E6 on the 3–5 cm real-hair head, 10 min ALONG then 10 min CROSS; black card under; photo of the hair state before/after; comb-through force after. Count shed hairs (with bulb vs broken). Pass: shed per 100 machine strokes ≤ 2× the combing baseline per 100 comb strokes (B was counted over 20 comb strokes, so the baseline per 100 is 5·B; the 20-min run is ≈ 2,400 strokes from the serial count), no mat, comb-through force ≤ 1.5× pre.
8. **Static run.** Repeat 7 for 5 min at < 35 % RH; note fly-away and hair clinging to the tips after lift-off. Record only; if hair follows the tips up by > 10 mm, add the antistatic wipe to the cleaning list.
9. **Tip-material comparison** (log for §N, not a gate): same 200 strokes per tip W, B45, B45-12, E, P, H; shed count and any capture per tip.

**Gate to any human session:** zero wraps, zero captures, zero knots in 3/5/6; 15 g never lifted in 4; shed ≤ 2× baseline in 7; all gating items of the hair-interaction §6.8 checklist scored 2 (score sheet attached to the Session Log).

### L9. Tip sharpness tape test

**Procedure.** (Safety §6 A, UL 1439 style.) Wrap a 10 mm rod with 3 layers of 50 µm polyester or PTFE tape. For each tip in the holder on the wand: press at 1.0 N and then 2.4 N (kitchen scale under the rod) and slide 50 mm along the rod axis at ≈ 50 mm/s, three passes each direction, both edge senses for the 45° tips, then across the corners. Also test the guard plate edge, knuckle plate edge and paddle exits by hand at 5 N. Inspect the tape under the loupe.
**Pass.** No cut through any layer at 2.4 N for R ≥ 0.4 mm tips; **A45 (R 0.3 mm) must pass at 2.4 N too or stays gated**; no cut at 5 N for structure edges. Record per tip; re-test any tip after 10 sessions or after any drop.

### L10. Forearm skin test (self)

**Procedure.** Volar forearm, hairy side. (a) **Wand:** per tip, 10 strokes, 40 mm, ≈ 80 mm/s at 0.3 / 0.6 / 1.0 N (practice the force on the kitchen scale first — most people press 2–3× harder than they think). Score sharpness 0–10, forced choice scratch / stroke / pressure, pleasantness 0–10, redness at 10 min. (b) **Machine on forearm:** forearm on a folded towel under the rig, E = 4, W1, PER S1, tip H then W, 30 s each with the hold-to-run in the other hand; then HUM S2 W2 30 s with W. Score the same.
**Pass.** No tip with sharpness ≥ 7 at 0.6 N goes to the scalp; no redness beyond faint transient at 10 min; machine run: no pain, no skin marks, forearm hair not pulled; stop-on-release confirmed by feel.

### L11. Back-of-hand test (self)

**Procedure.** Back of the non-button hand flat on the towel under the rig (sparse hair, thin skin, knuckles give curvature). HUM S2 W2 E4 tip W, 30 s; then S3 W3 E6, 30 s. Move the hand ±15 mm sideways and ±10 mm up/down during the run (the float and leaves must follow with no force spike you can feel); lift the hand away quickly mid-stroke (the nails must drop to the down-stop and lift at the ends, nothing chases the hand).
**Pass.** No pain, no skin marks, no force spike on head-motion simulation, no knuckle catch; comfortable at S3 W3 (if not, note it — this becomes the first-session ceiling).

### L12. Own-palm scratch test (compliance and stop)

**Procedure.** Rig running HUM S2 W2 E4 over the foam head; push the palm of the free hand up into the moving hand from below, then from the side (±X, ±Y). Expect: float rises freely, leaves deflect, the servo stalls at ≈ 1.2 N tangential (goal-current) without pushing through, nothing hurts. Then while the palm is loaded: release hold-to-run → everything stops and lifts within 0.5 s; repeat with the e-stop; repeat the push with the wrist breakaway direction (+X at ≈ 2 N: the hand must release onto the tether, not pin the palm).
**Pass.** Yields in all directions; stall ≤ 1.5 N by feel/fish scale; stop + lift ≤ 0.5 s every time (10/10 on hold-to-run, 5/5 on e-stop); breakaway releases rather than pins.

### L. Results table (one row per test, per build state)

| Test | Build state | Date | Key measured values | Limit | Pass? | Notes / action |
|---|---|---|---|---|---|---|
| L1 dead weight | | | W1 ___ W2 ___ W3 ___ N; shares ___/___/___ | 0.9/1.2/1.5 ± 0.05; ratio 0.8:1:1.2 | ☐ | |
| L2 leaf rate / stop | | | k ___/___/___ N/mm; stop ___/___/___ N | 0.1–0.25; ≤ 2.4 | ☐ | |
| L3 float friction | | | F_f ___ N (horizontal), ___ N (hysteresis/2) | ≤ 0.1 | ☐ | |
| L4 lift-off chord | | | chord E2 ___ E4 ___ E6 ___ mm; gap ±25° ___ mm; speed S1/S2/S3 ___/___/___ mm/s | 25/36/44 ± 5; ≥ 5; ≤ 400 | ☐ | |
| L5 fail-safe lift | | | rise ___ mm; t ___ s; n pass ___/30 | ≥ 25; ≤ 0.5; 30/30 | ☐ | |
| L6 breakaway | | | wrist ___/___/___/___ N; −Z ___ N; tips ___ | 1.5–2.5; ≥ 5; 4–8 | ☐ | |
| L7 30-min cycle | | | T ___/___/___ °C; ___ dBA; faults ___; drift ___ mm | ≤ 48/43; ≤ 70; 0; ≤ 2 | ☐ | |
| L8 wig head | | | wraps ___ captures ___ knots ___; 15 g lifted? ___; shed ___ vs baseline ___; RH ___ % | 0/0/0; no; ≤ 2× | ☐ | |
| L9 tape test | | | tips passed: ___; A45 at 2.4 N: ___ | no cut | ☐ | |
| L10 forearm | | | max sharpness @0.6 N ___ (tip ___); redness ___ | < 7; none | ☐ | |
| L11 back of hand | | | S3 W3 tolerable? ___; spikes? ___ | yes; none | ☐ | |
| L12 palm | | | stall ___ N; stop ___ s; ___/10 ___/5 | ≤ 1.5; ≤ 0.5; all | ☐ | |

---

## M. FIRST HUMAN TEST — staged protocol

### M0. Posture setup

**Primary — SEAT:** chair at the desk, tabletop face cradle (massage face-cradle pad on a clamp or a padded block) so the forehead/cheeks carry the head with the neck relaxed; trunk supported by the chair back or the forearms on the desk. The monitor arm comes over the head from the side/behind. Adjust the cradle height and tilt so that **the scalp normal at the target point is vertical**: put the phone inclinometer on the module frame (rail vertical ±5°), then tilt the head until the three nails, resting at W1 with the carriage floating, touch simultaneously (helper looks; alone, feel it, then photo via a mirror). CR: head flexed ≈ 30–45°; OC: head flexed ≈ 60–80° — if that is uncomfortable seated, OC goes PRONE. **Isolate the cradle from the desk the arm clamps to** if you can feel the stroke rhythm in your forehead (rubber feet / separate stand; Red Team 1 attack 9) — note "rhythm felt in forehead: y/n" on every form.
**Alternative — PRONE:** on the bed, face in a portable face-cradle cushion, monitor arm clamped to the nightstand or a floor stand within 500 mm of the occiput. Gravity is then along the occipital normal (the posture where the dead weight works as designed); breathing drift 5–15 mm is inside the float travel. Use PRONE for OC by default and for any session where SEAT discomfort (neck/forehead) is rated > 3/10 within 5 min.
**Aiming.** Make the grain map first (§M-pre). Mark the target patch with two small hair clips 50 mm apart along the intended axis; a helper aligns the stroke axis to the clips, or Michael does it with a hand mirror + phone camera. Tape index marks on the monitor-arm joints for CR-ALONG, CR-CROSS, OC-ALONG, OC-CROSS so a re-aim takes < 1 min. Remove the clips before running.

### M-pre. One-off measurements (do on Day 0 with the wand)

Michael's hair: length (cm) at CR and OC; grain map (comb test: direction of lie at CR — whorl position and sense; at OC — lie direction, usually downward); approximate density (photo-count 1 cm²) and strand diameter (caliper on a plucked strand) if easy. Human reference: if a helper is available, 30 s of real fingernail scratching at CR and OC, rated on the §O form — this anchors "10 = a real person" on the realism scale and is the gold reference for §P. If no helper: self-scratch 30 s (note it is attenuated) and the helper-less anchor is "the best the wand ever felt".

### M-rule. The free-hand hold-to-run rule

The HOLD-TO-RUN button is in one hand for the whole run; the thumb holds it, nothing else does — **never taped, tied, latched, wedged, or held by a helper**. The other hand rests on the desk/bed under the e-stop. Letting go of the button is the normal way to end *anything*: a snag, a pull, a sharp feel, a wish to reposition, a cough. Releasing costs nothing (the firmware resumes lifted); so **release first, think second.** Both hands stay below the knuckle-plate plane and never go near the module while the rail is live; any adjustment (tip swap, slug, aim) is done with the e-stop pressed in.

### M-stop. Stop rules (apply to every stage)

Release hold-to-run immediately on: any hair pull you feel (not just hear), any pain or sharp/prick event, any snag or "catch", any sensation of the hand pushing rather than resting, any unexpected sound, the module touching anything but hair, any dizziness or neck pain. Then: press e-stop, lift the head out, inspect the hand and scalp before deciding anything. **Tuft pull (more than a few strands at once) = end of session, redesign item logged, no further human testing until the fix passes L8.** Pain ≥ 4/10 = end of stage; the next attempt is at the previous (lower) setting. Any skin break = end of the program's human testing until a safety review.

### Stage table

| Stage | Preconditions | Settings | Duration | Record | GO to next stage if | NO-GO action |
|---|---|---|---|---|---|---|
| **H0 — Hand wand (Day 0)** | Wand built (TM1 holder on the 0.3 × 12.7 leaf, 150 mm handle); tips W, B45, A45, H, P tape-tested (L9) and forearm-screened (L10a); grain map done | Hand-driven, kitchen-scale practice to 0.3–0.5 N; 10 strokes per tip, 30–40 mm, ≈ 80 mm/s; CR then OC; ALONG and CROSS | ≤ 10 min total | §O form per tip; side photo of contact fraction through the hair at 0.3 and 0.5 N; wig: 200 strokes per tip, catches/pulls counted; **blind W vs H and B45 vs H** (helper or eyes-closed swap, code read after) | nail visibly reaches skin at ≤ 0.5 N in Michael's hair; W or B45 beats H on realism by ≥ 3 points blind; zero captures in 200 wig strokes per tip; uni (B45) vs bidirectional (W) preference noted | fix the tip (reach, radius, width) before any motorised build; if nothing reaches skin, the engagement/leaf/paddle question moves to the top of §P |
| **H1 — Machine off, nails resting** | §K complete (all sections); L1–L12 passed; wig gate passed; glasses; e-stop pressed in; rail dead | Tip W; **dead weight 0.6 N total** (trim-spring hook or lightest configuration; if the bare float is 0.9 N, use the hook — see §Q); E4; CR; SEAT | 3 × 20 s rests, lifting the head out between | Feel: "nails or pins?"; even contact of three nails (y/n); forehead pressure comfort 0–10; any pain; then **live fail-safe check**: helper (or Michael) powers the rail with the hold-to-run, nails resting, and releases it → hand lifts ≥ 25 mm off the head, felt and seen | three nails felt, none sharp, pain 0; lift confirmed on the head; head withdraws freely with no hair caught | re-seat tips / re-check leaf shares (L1b); if even 0.6 N feels sharp, the tip set is wrong — back to H0 |
| **H2 — PERIODIC, minimum speed** | H1 passed; W1 fitted (0.9 N) | PER, S1, E4, CR, ALONG, **tip H first (30 s), then tip W (30 s)**; hold-to-run in hand | 2 × 30 s, 60 s washout | §O form after each; snags; hairs on the black cloth; video from the side if a helper is present | pain 0–1, pulling ≤ 1, zero snags; hold-to-run released at least once mid-run and the lift felt; W rated as more "edge/nail" than H (checklist item 1) | if W feels like H: tip/force problem (go to §P-2); if pulling > 1: check DIR vs grain and E (drop to E2) |
| **H3 — HUMAN mode, 1 min** | H2 passed | HUM, S1→S2 (pot at 25 %), V100, W1, E4, CR, ALONG, tip W | 60 s | full §O form; realism, pleasure, machine-ness; snags; shed count; scalp photo at 0 and 10 min | discomfort ≤ 2, pulling ≤ 2, zero snags, no redness at 10 min; nothing on the stop list triggered | if HUM at S1–S2 feels worse than PER: note it (it is data for §P-7); repeat once; if discomfort > 2 at W1, the force is high for this tip — check L1 shares |
| **H4 — Weight steps** | H3 passed; same day or next | HUM S2 V100 E4 CR ALONG tip W; **W1 → W2 → W3**, 45 s each, 60 s washout; e-stop in between for the slug change | 3 × 45 s | §O per step; note the first weight at which "pressing" appears (checklist 3 = no) and at which realism peaks | each step: discomfort ≤ 3, pulling ≤ 2; stop at the first weight with discomfort > 3 and record it as W_max for this tip | W_max = W1: the usable range is below the freeze range — fit the trim hook and add a 0.6 N level to §N; W3 wanted and comfortable: fine, the matrix top stays W3 |
| **H5 — Speed steps** | H4 passed | HUM V100 E4 CR ALONG tip W at the best weight from H4; **S1 → S2 → S3**, 45 s each | 3 × 45 s | §O per step; snags per 45 s at S3; any landing "tap" or buzz noted; dBA at the ear | each step: discomfort ≤ 3, pulling ≤ 2, zero snags at S3; no buzz/tap complaint at ≥ 5/10 | snags appear at S3: cap the matrix at S2 for this tip/direction and log; buzz: ELEC/MECH check leaf-root damping (Red Team 1 attack 8) |
| **H6 — 5-min session** | H5 passed; ≥ 20 h since H3 | best (tip W, weight, speed) from H4/H5; HUM V100 E4 CR ALONG | 5 min continuous; ratings called into a voice memo every 60 s (realism, pleasure, pulling, discomfort) | §O at the end plus the per-minute series; snag count; shed count; scalp photo 0/10/60 min; posture discomfort | discomfort never > 3 and not rising > 2 points over the 5 min; pulling ≤ 2; snags ≤ 1; shed ≤ 5; redness gone by 60 min; "desire to continue" ≥ 5 | realism decays > 3 points by minute 5 → log as habituation (data for §P-3/4); try with head roll ±15° in the second half; posture > 3 → PRONE next session |
| **H7 — 20-min session** | H6 passed; ≥ 20 h; scalp clear next day | same as H6; invite a slow head roll ±15° every 30–60 s; one manual re-aim at 10 min (e-stop, move to a patch 40 mm away, resume) | 20 min; voice-memo ratings every 2 min | §O at 10 and 20 min; per-2-min series; snags; shed; scalp photo 0/10/60 min and next morning; posture; what you wanted to change | no cumulative discomfort rise > 2; no tenderness next day; snags ≤ 2 with none "felt as a pull"; shed ≤ 10; no erythema beyond mild transient; willing to run the matrix | 20 min not tolerable for posture: PRONE, or cap matrix sessions at 10 min exposure; sensation-side failures go to §P, not to a protocol change |

Exposure accounting for the first days (safety §2.5): Day 0 = H0 only. Day 1 = H1–H3 (≈ 2.5 min). Day 2 = H4–H5 (≈ 4.5 min). Day 3 = H6 (5 min). Day 4 = H7 (20 min). Day gaps may be longer; never shorter than 20 h for H3→H6→H7.

---

## N. EXPERIMENT MATRIX

### N0. Design logic

Eight factors (tip 7, WT 3, SPD 3, VAR 3, DIR 2–3, E 3, MODE 2, REG 2) are far beyond any full factorial for one tester (≈ 6,800 cells). Judge 3's lens applies: SP1 is a research rig whose first job is to find **any** condition that reads as fingernails, then learn which knobs move that reading. So the design is sequential:

1. **Screening (S):** wide, fast, un-replicated, all at D0 plus one-factor swings — looking for the first "yes" (realism ≥ 6). Trials of 45 s.
2. **One-factor-at-a-time (OFAT):** around the best screening condition, each factor over its full range, two replicates, with the order randomized within the session.
3. **Paired A/B:** the hypothesis-bearing contrasts, blinded where feasible, ABBA order, replicated across sessions.
4. **Endurance:** one 20-min run at the final best condition with the per-2-min series (habituation).

**Realism rule for ordering:** the realism scale (§O Q1) is the primary outcome; pleasure (Q2) secondary; "desire to continue" (Q9) tertiary. Pulling (Q5) and discomfort (Q6) are constraints (a condition with Q5 or Q6 > 3 is excluded from "best" regardless of Q1).

### N1. Settings and gating

- A45 enters only after L9 at 2.4 N and L10 (sharpness < 7 at 0.6 N) — then it is used at W1–W2 only, never W3.
- B45, B45-12, A45, E and P are 45°-faced (unidirectional loaded edge): in bidirectional strokes their return is a back-of-blade glide. Record the loaded sense (ALONG-W / ALONG-A). W and H are symmetric.
- E = 6 and S3 are allowed only after H5/H4 showed them tolerable; otherwise cap at E4 / S2 and log.
- OC sessions are PRONE unless SEAT at 60–80° flexion was comfortable in H-stages.

### N2. Screening phase (sessions 5–8; 45 s trials; 60 s washout; ratings after each)

| Session | Purpose | Trials (each = D0 with the stated change) | n trials | Exposure |
|---|---|---|---|---|
| S-A (5) | Tip screen, crown | TIP ∈ {H, W, B45, B45-12, E, P} at D0 (B45/B45-12/E/P mounted ALONG-A, i.e. loaded against the lie, the human occiput primitive; on the crown use the whorl-outward sense as "with"). Order randomized by helper/script; tip codes blind. Then the two best plus H repeated in reverse order | 9 | ≈ 7 min |
| S-B (6) | Tip screen, occiput (PRONE) | same six tips at D0 with REG = OC; then the two best plus H reversed | 9 | ≈ 7 min |
| S-C (7) | Mode × variation screen | best tip from S-A/S-B at its region: PER; HUM V0; HUM V50; HUM V100; then the same four at the other region. Mode blinded by helper flipping the toggle (or firmware BLIND command, §Q) | 8 | ≈ 6 min |
| S-D (8) | Direction × engagement screen | best tip, best mode/variation, primary region: DIR ∈ {ALONG, CROSS} × E ∈ {2, 4, 6}; for 45° tips add ALONG-W vs ALONG-A at E4 | 6–8 | ≈ 6 min |

**Screening exit:** the best condition **C*** (highest realism with Q5, Q6 ≤ 3). If no trial reaches realism ≥ 4 in S-A/S-B, do **not** continue to S-C/S-D on the machine — run the wand on the same patch the same day at the same tips (the wand vs machine comparison is §P-7's data) and go to §P.

### N3. OFAT phase (sessions 9–13; 60 s trials; 60 s washout; 2 replicates each, order randomized within the session)

Each session holds all factors at C* and sweeps one:

| Session | Factor swept | Levels | n trials |
|---|---|---|---|
| O-1 (9) | WT | W1, W2, W3 (+ 0.6 N via trim hook if H4 said W1 was already "pressing") | 6–8 |
| O-2 (10) | SPD | S1, S2, S3 | 6 |
| O-3 (11) | E | 2, 4, 6 | 6 |
| O-4 (12) | VAR and MODE | PER, V0, V50, V100 | 8 |
| O-5 (13) | DIR (and sound) | ALONG, CROSS (+ ALONG-W vs ALONG-A for 45° tips); then C* with foam ear plugs vs without (Q9 of scratch-model §9) | 6–8 |

**OFAT exit:** update C* if any level beats the previous best by ≥ 1.5 points on realism averaged over its two replicates; note monotone trends (e.g. realism rising with WT up to W3 means the force window is above the freeze range → §P-6).

### N4. Paired A/B phase (sessions 14–19; 45 s per arm; ABBA within a pair; 60 s washouts; 4–5 pairs per session; order of pairs randomized per session; blinding as stated)

| Pair | A | B | Hypothesis tested | Blinding | Region(s) |
|---|---|---|---|---|---|
| P1 | C* | C* with TIP = H | sanity: an edge beats a ball (massager-vs-scratcher) | tip code | primary |
| P2 | C* (HUM V100) | same, PER | irregularity is a large part of "fingernails" (DECISION hypothesis) | helper toggle / BLIND | both |
| P3 | C* | same with V0 | which part of HUM matters: jitter vs episodes/pauses | helper toggle | primary |
| P4 | W | B45 (loaded ALONG-A) | symmetric bidirectional rake vs nail-mimic 45° (Red Team 1 attack 1) | tip code | both |
| P5 | B45 | B45-12 | width (hair collection vs reach) | tip code | primary |
| P6 | C* | same with TIP = P | zero-fabrication real-nail reference vs printed edge | tip code | primary |
| P7 | C* | same with TIP = E | compliance in the tip | tip code | primary |
| P8 | ALONG | CROSS | direction vs lie | none (aim is visible) | primary |
| P9 | E4 | E2 | engagement/chord | none | primary |
| P10 | best WT | adjacent WT | force window edge | slug is swapped out of sight | primary |
| P11 (gated) | C* | same with TIP = A45 | radius 0.3 vs 0.4–0.5 | tip code | primary, W1–W2 only |

Count: 11 pairs, P2 and P4 at both regions → 13 pair-blocks × ABBA (4 arms) = 52 arms × 45 s ≈ 39 min of exposure spread over 6 sessions (≈ 2 pair-blocks + 1 single-block per session, ≈ 7–9 min exposure each). Each pair's forced choice ("which was more like fingernails / more pleasant") plus the two §O forms. **Win rule:** a pair is decided if the same arm wins ≥ 3 of 4 ABBA presentations on the forced choice *and* the mean realism difference is ≥ 1 point; otherwise "no difference" (which is itself a result: that knob does not matter at this precision).

**Blinding mechanics.** Helper present: helper swaps tips/slugs and flips the toggle behind the head while Michael's eyes are closed and the e-stop is pressed; helper records the condition on the log; Michael rates before being told. No helper: tips carry random two-letter codes under the tang; Michael presses e-stop, closes eyes, picks the next tip from a shuffled box by the order printed by a script (`python3 -c "import random; l=['A','B','B','A']; random.shuffle(l); print(l)"`), seats it, runs, rates, then reads the code. Mode blinding without a helper needs the firmware BLIND command (§Q); until it exists, P2/P3 are unblinded and marked so.

### N5. Endurance (session 20)

C* for 20 min with the per-2-min series as in H7; one re-aim at 10 min; head roll invited. This is the habituation curve that §P-3/4 reads.

### N6. Session count, length, washout

- **Sessions:** 0 (H0) + 4 (H1–H7) + 4 (screening) + 5 (OFAT) + 6 (A/B) + 1 (endurance) = **20 sessions** nominal; minimum 15 if S-C/S-D are folded into OFAT and A/B is cut to P1, P2, P4, P8 (the four that carry the hypothesis); maximum 25 if A45 is admitted, the second region is replicated in OFAT, or any session is repeated for a stop-rule abort.
- **Session length:** 20–35 min wall-clock, ≤ 10 min scalp exposure in S/OFAT/A/B sessions, 20 min in H7 and N5.
- **Washout:** 60 s lifted between trials; 3 min out of the cradle every 5 trials; ≥ 20 h between sessions; a rest day after any session with redness > 60 min or snags ≥ 2.
- **Order of days:** H-stages → S-A → S-B → S-C → S-D → OFAT → A/B → endurance; A/B pairs can be interleaved with OFAT days if a factor is already settled.
- **Replication:** screening unreplicated (by design); OFAT 2×; A/B 4 arms per pair; endurance 1× (2× if the first shows a clear decay).

---

## O. FEEDBACK FORM (one per trial; print; fill within 60 s of the trial while the head is still in the cradle — voice memo first, paper after)

**Session ___  Trial ___  Date ______  Time ______  Build state ______**

| Field | Value |
|---|---|
| TIP (code if blind) | ______ |
| WT (W1/W2/W3/0.6) | ______ |
| SPD (S1/S2/S3) | ______ |
| VAR (V0/V50/V100) | ______ |
| DIR (ALONG / ALONG-W / ALONG-A / CROSS) | ______ |
| E (2/4/6 mm) | ______ |
| MODE (PER/HUM) | ______ |
| REG (CR/OC) · POS (SEAT/PRONE) | ______ · ______ |
| Duration (s) | ______ |
| Snags count (felt catches) · of which pulls felt | ______ · ______ |
| Hairs shed on cloth/roller (with bulb · broken) | ______ · ______ |
| Ear plugs (y/n) · rhythm felt in forehead (y/n) | ______ · ______ |

**Rate 0–10** (0 = none/not at all, 10 = extreme/perfect; anchor Q1 on the human reference from M-pre = 10, tip H on the machine ≈ 0–2):

| # | Scale | 0 ———————————— 10 | Score |
|---|---|---|---|
| Q1 | **Scratch realism** — "this is someone's fingernails" | not at all → exactly | ___ |
| Q2 | Pleasure | none → wonderful | ___ |
| Q3 | Intensity | can barely feel it → as hard as I'd want | ___ |
| Q4 | Tingle / ASMR / shiver | none → strong | ___ |
| Q5 | Hair pulling | none → painful pull | ___ |
| Q6 | Discomfort / pain | none → stop now | ___ |
| Q7 | Perceived coverage | one line → whole region being worked | ___ |
| Q8 | Noise annoyance | silent → intolerable | ___ |
| Q9 | Desire to continue | want it off → don't stop | ___ |
| Q10 | **Machine-ness** — "I can tell it's a machine" | never → constantly | ___ |

**Massager-vs-scratcher checklist (scratch-model §8, as felt) — Y / N:**

| # | As felt | Y/N |
|---|---|---|
| C1 | An edge, not a pad — I feel a line/nail, not a dome or finger pad | ___ |
| C2 | It reaches my skin (not riding on the hair) for most of each stroke | ___ |
| C3 | It is light — resting, not pressing | ___ |
| C4 | It slides across the skin; the skin does not move with it | ___ |
| C5 | Right speed — scratching, not flicking/brushing, and no buzz/vibration | ___ |
| C6 | Hair is moved near the root (I feel the follicles), not just the ends | ___ |
| C7 | Feels like several separate fingers, not one comb | ___ |
| C8 | Irregular — I cannot predict the next stroke | ___ |
| C9 | Follows my head — no force spikes when I move/breathe | ___ |
| C10 | It unloads at the ends of strokes — no dragging reversal | ___ |
| C11 | No hair caught anywhere during or after | ___ |
| C12 | Sounds like a scratch, not a motor | ___ |

**Free text:** What would make it more like a person? ______________________________________________
Anything sharp, any tap/landing, any pattern you noticed, where you wanted it to go next: ______________________________________________

**Pair trials only:** this arm vs the other arm — more like fingernails: A / B / same; more pleasant: A / B / same.

**CSV header line** (one row per trial; append to `sp1_trials.csv`):

```
session,trial,date,time,build_state,tip,tip_code,wt_N,spd,var,dir,e_mm,mode,region,posture,duration_s,snags,pulls_felt,shed_bulb,shed_broken,earplugs,forehead_rhythm,q1_realism,q2_pleasure,q3_intensity,q4_tingle,q5_pulling,q6_discomfort,q7_coverage,q8_noise,q9_continue,q10_machine,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,pair_id,pair_arm,fc_realism,fc_pleasure,free_text
```

---

## P. ITERATION MAP — what SP1 outcomes imply for SP2

Read after the screening phase and again after the A/B phase. Each row: the outcome pattern as it will appear in the data, the SP2 (or Stage 3) change that follows, and the SP1 data that justify it. "Realism" = Q1 mean at the best condition.

| # | Outcome pattern (as it shows in the data) | What it means | SP2 / Stage-3 change | SP1 data that justify it |
|---|---|---|---|---|
| P-1 | **Nothing reaches skin:** C2 = N on all tips at E6 W3; realism ≤ 3 everywhere; wand side-photos show the edge riding on the pile; C6 = N | The canopy problem, not the mechanism: 8 mm edges at ≤ 0.5 N cannot part Michael's hair | Engagement first: E 8 mm (down-stop range), stiffer leaf preload, narrower/longer paddles (≥ 25 mm protrusion), narrower tip (C-type nail-corner 4 mm at ≤ 0.4 N); if the wand also fails → hair-parting is a tip-geometry problem (SP2 tip program before any new mechanism) | S-A/S-B contact fraction photos; H0 side photos at 0.3/0.5 N; OFAT O-3 (E) flat; O-1 (WT) flat |
| P-2 | **Feels like a comb / sweep:** C1 = Y but C7 = N and free text says "comb"; realism 3–5; B45-12 ≤ B45 ≤ W or all equal; realism rises with WT monotonically to W3 | Line load too low for the edge radius (glide region) or three phase-locked lines read as teeth | Tip radius/width/force: R 0.3 (A45) admitted; 4 mm loaded edge (nail-corner); per-nail ≥ 0.4 N (trim the freeze range up, cap stays 2.4 N); carrier yaw stagger 15–20° so the lines are not parallel; 4th nail | P4/P5/P11 pair results; O-1 monotone trend; C7 pattern |
| P-3 | **High realism only in HUMAN:** P2 shows HUM ≫ PER (≥ 2 points), V100 > V0 (P3), but the endurance curve decays > 3 points by minute 5 even in HUM | Irregularity in time works; irregularity in *place* is missing (single patch habituates) | **Stage 3 yaw servo** (XL330 ID 2 at the frozen yaw joint): direction wander ±15–30° and start-point drift in the air; episodes every 5–20 s that change region; head-roll invitation stays | P2/P3 wins; N5 and H7 per-2-min series; the 10-min re-aim restores ≥ 2 points |
| P-4 | **Realism good but habituates:** realism ≥ 6 in the first 2 min of every run, then decays; manual re-aim restores it; free text "wants to move" | The contact is right; the pattern needs region change and longer episodes | Episodes/wander: yaw servo + firmware episode engine (P2 sweeps, pauses, region changes); then SP2 full-coverage (criteria below) | N5 decay slope vs re-aim recovery; Q7 coverage low with Q1 high |
| P-5 | **Pulls hair:** Q5 ≥ 3 at any condition; snags cluster by DIR (ALONG-A ≫ ALONG-W) or by E (E6 ≫ E2) or by SPD (S3) | Direction, lift geometry, or boot/paddle capture | Direction: lock against-grain strokes to ≤ 25 mm (firmware amplitude by direction, needs yaw/aim knowledge); lift: lower E, add a reversal force-dip (float micro-lift via the magnet pulse or a 4th servo in SP2); boot: if shed hairs are found at the paddle holes, redesign the boot/paddle clearance; **any tuft pull: redesign before any further human session** | O-5 snags by DIR; O-3 by E; O-2 by SPD; L8 repeated with the hair pushed into the mechanism; shed counts with bulbs |
| P-6 | **Too weak / too strong:** realism peaks at W1 with "pressing" already at W2 (too strong) or rises monotonically to W3 and C3 = Y still (too weak) | The 0.9–1.5 N window is misplaced for this tip | Weight: add the 0.6 N trim level or extend the slug range to 2.0 N total (per-nail stays ≤ 0.75 N, cap 2.4 N); SP2: constant-force spring float (orientation-independent) and a load cell in the wrist slot for a measured force–pleasure curve | O-1 shape; H4 W_max; per-nail shares from L1b |
| P-7 | **Good on the wand, not on the machine:** H0 realism ≥ 7 for a tip, machine ≤ 4 with the same tip, same patch, same day; free text "taps", "metronome", "step in the middle" | Kinematics/stiction: landing taps, mid-stroke float reversal, fixed-duration events, servo gear ripple | Kinematics: trapezoid in-contact profile, land at ≤ 25 mm/s or plough in while moving, randomize every fixed-duration event; measure F_f again; SP2: head-centred yoke (concentric arc removes the mid-stroke float reversal) or a back-drivable gimbal FOC stroke axis (silent, impedance) | Wand-vs-machine paired ratings; L3 stiction; 240 fps of landings; C5/C9/C10 answers; Q10 high with Q8 low |
| P-8 | **Posture intolerable:** neck/forehead discomfort > 3 within 5 min seated; sessions cut short for posture, not sensation | The rig's physics are fine; the human cannot hold the pose | PRONE as the default (nightstand/floor-stand clamp, face-cradle cushion); SP2: reclined/side-lying needs a constant-force float (orientation-independent) | H6/H7 posture field; forehead-rhythm y/n |
| P-9 | **Machine-ness high even when realism is fair:** Q10 ≥ 6 with Q1 ≥ 5; ear plugs (O-5) drop Q10 by ≥ 2 | Sound/vibration is the tell | Isolation (cradle off the arm's desk, servo muff, rubber at the VESA adapter); SP2: silent direct drive (gimbal + SimpleFOC) on the stroke axis | O-5 ear-plug pair; K4.7 dBA; forehead-rhythm y/n |
| P-10 | **PERIODIC ≈ HUMAN, both ≥ 6** | The per-stroke contact physics carries the sensation; the rank-1 variable matters less than modelled at this patch size | Machine done for SP1's question; spend on tips, regions, sessions and the full-coverage SP2; keep the pattern engine simple | P2/P3 "no difference"; endurance curve flat |
| P-11 | **Three nails read as three scratchers:** C7 = N while C1, C2 = Y; realism 4–6; free text "three things", "rake" | Hand illusion needs per-finger asynchrony/force spread | SP2 hand: per-finger phase/force (B's pendulum fingers or D's tendon Resting Hand on the same float); carrier yaw stagger as the cheap first step | C7 pattern; P4 (W vs B45) indifferent; single-nail OFAT (remove two tips) if run |
| P-12 | **Realism high only at OC (prone) and low at CR seated, or vice versa** | Region/posture confound: gravity alignment, hair lie, follicle density | Keep the winning posture; SP2 coverage design targets the winning region first; re-check rail verticality in the losing posture | S-A vs S-B; O-5 at both regions; inclinometer logs |

### P-GO. "Go to SP2 full-coverage" criteria (all must hold)

1. A condition C* exists with realism ≥ 7 and pleasure ≥ 7 on ≥ 2 separate sessions, with Q5 ≤ 2 and Q6 ≤ 2.
2. "Desire to continue" ≥ 7 at C*, and H7/N5 show either ≤ 2 points of decay over 20 min **or** decay that a manual re-aim reliably restores (≥ 2 points back within 1 min) — i.e. the unmet need is *place*, which coverage solves.
3. Zero tuft pulls across all sessions; shed ≤ 10 per 20 min; no scalp finding beyond transient redness.
4. The massager-vs-scratcher checklist at C* has C1, C2, C3, C4, C6 = Y on ≥ 80 % of trials.
5. The wand does not beat the machine by more than 1 point at the same tip (otherwise fix the kinematics first, §P-7).
6. The HUM-vs-PER result is known (either direction), so SP2 knows whether to carry the pattern engine or simplify it.

### P-STOP. "Abandon this mechanism" criteria (any one is sufficient; the *contact* findings transfer regardless)

1. After the full matrix, no condition reaches realism ≥ 5 **while the wand reaches ≥ 7** with the same tips on the same patch — the stroke generator, not the contact, is wrong, and no OFAT trend points to a fix inside the SP1 envelope.
2. Nothing reaches skin (P-1) at E6/W3 on every tip **and** the wand also fails → a different hair-parting approach (tendon hand, narrower tines, two-stage part-then-scratch), not a Float-Arm revision.
3. Hair pulling Q5 ≥ 4 persists at every DIR × E × SPD combination after one boot/paddle fix cycle, or any tuft pull reproduces after one fix cycle.
4. Machine-ness Q10 ≥ 7 at all settings *with* ear plugs and the cradle isolated — the kinematic signature itself reads as a machine → SP2 is a different stroke generator (yoke or FOC), not more SP1.
5. Posture: neither SEAT nor PRONE tolerable ≥ 10 min after two attempts each — a head-worn or reclined architecture is needed, which this float cannot serve.

---

## SESSION LOG (one per session; staple the trial forms behind it)

```
SP1 SESSION LOG
Session # ____   Date ________   Start ______  End ______   Build state ______  Firmware ______
Stage/phase: H__ / S-__ / O-__ / A/B __ / Endurance        Helper present: y / n   Name: ______
Posture: SEAT / PRONE   Region(s): CR / OC   Cradle isolated from arm desk: y / n
K5 checklist complete (sign): ______   K1–K4 valid for this build state (date): ______
Tips used (IDs and codes): ______________________   Tape test valid (date): ______
Weights available: W1 ___ N  W2 ___ N  W3 ___ N  (L1 date ______)   Trim hook used: y / n
Grain map ref: CR lie ______  OC lie ______   Aim marks used: ______
Serial echo at start: SPEED ___ % VAR ___ % MODE ___   E pointer at mid-stroke ___ mm, at ends 0? y/n
RH ___ %   Room temp ___ °C   Ear plugs: y / n
Planned trial list (condition codes, order as randomized): ______________________________________
Total scalp exposure this session: ___ min (limit ___)
Stops: hold-to-run releases ___  e-stop presses ___  reason(s): ______________________________
Snags total ___   pulls felt ___   tuft pull: y / n (if y: STOP, log redesign item #____)
Shed hairs total: bulb ___  broken ___      Scalp photo 0 min ☐ 10 min ☐ 60 min ☐ next day ☐
Scalp findings (redness / tenderness / marks / none): ______________________________________
Device findings after (hair in gaps, loosening, tip wear, magnet drop): ________________________
Best condition this session (code): ______  Q1 ___ Q2 ___ Q9 ___
One sentence — what would make it more like a person: _________________________________________
Next session plan / changes to build state: ________________________________________________
```

---

## PACKING / CLEANING CHECKLIST

**Before the session (packing in / set-up, ≈ 5 min)**
- ☐ Rig out of the folded position; monitor-arm clamp tightened; arm joints to the taped aim marks for today's REG/DIR
- ☐ Face cradle clamped (SEAT) / cushion placed and arm clamped to the nightstand or stand (PRONE); isolation feet under the cradle
- ☐ Adapter on the floor, > 1 m from the head; USB to the laptop/charger; OpenRB boot banner read (limits table)
- ☐ E-stop on its weighted base under the free hand; hold-to-run lead ≥ 1.5 m, button in the other hand; both tested over the mannequin
- ☐ Tip box with today's set (codes face-down for blind trials), wand, slugs (+30, +60, trim hook), hair clips, mirror
- ☐ Phone: timer, voice memo, 240 fps, SPL app, inclinometer; black cloth under the cradle; lint roller; forms and pen; §K5 signed

**After the session (cleaning and packing away, ≈ 5 min)**
- ☐ E-stop pressed; adapter unplugged **first**; USB unplugged
- ☐ Lint-roll the hand, knuckle plate, boots, guard underside and the cloth; count hairs onto the Session Log (bulb vs broken)
- ☐ Tips out of the TM1 pockets; 70 % IPA wipe each tip, the TM1 pockets, paddles, knuckle plate, guard underside; let flash off; inspect each tip edge under the loupe; retire any chipped tip
- ☐ Check every seam and the boot slits with the loupe for trapped hair; tweezers out anything found and log it (a found hair is a design item, not just debris)
- ☐ Face cradle pad wiped (or its cover to the wash); cushion cover likewise
- ☐ Weights off the post (or confirmed captured); hand re-seated on the wrist keys; tether cord inspected
- ☐ Gas arm folded to the parked position; cables coiled with the service loops intact; e-stop and hold-to-run coiled, not kinked
- ☐ Scalp photo at 10 and 60 min set as phone reminders; CSV row(s) appended; Session Log filed in 05-engineering/results/
- ☐ Weekly: re-run L3 (float friction) and L1 (dead weight); re-oil the MGN9H; replace the TPU boot/silicone sheet if cut or stretched; tape-test any tip past 10 sessions

---

## Q. Testability requirements flagged to the other leads (not deviations from the freeze; additions needed to run this document)

1. **MECH:** a printed or stick-on **mm scale on the rail bracket (0 at the down-stop, ticks to 30 mm) and a pointer on the carriage** — needed to set E and to confirm lift-off at the stroke ends from the side (used in K2.3, L4, every session).
2. **MECH:** the **bare floating weight W1 must be ≤ 0.9 N** (≤ 92 g for carriage + wrist + hand + post), and a **trim-spring hook** (a light elastic from the carriage to the arm bracket, calibrated on the kitchen scale to unload 30 g) so that the H1 feel stage at **0.6 N total** and a 0.6 N matrix level are reachable without rebuilding the hand. Pre-weighed slug sets labelled +30 g and +60 g.
3. **ELEC/FIRMWARE:** a **USB-serial echo at 1 Hz** of SPEED %, VARIATION %, MODE, stroke count, elbow position and fault code; the **SPEED pot active in PERIODIC** as well as HUMAN; serial test commands for "go to +28°", "hang" (watchdog test) and limit printing at boot; optional **BLIND** command that picks PER/HUM at random and reveals it only on request (enables helper-less mode blinding in P2/P3). Tape marks on both pots at 0 / 50 / 100 %.
4. **ELEC:** hold-to-run lead ≥ 1.5 m with a thumb button that cannot be latched; e-stop on a weighted base; the actuator-rail fuse value stated on the wiring diagram and a spare in the kit.
5. **TIP:** a small random two-letter code engraved/labelled on the underside of every tang (blinding), and a tip box with slots.
6. **MECH:** aim index: tape marks on the monitor-arm joints are enough, but the module must be able to rotate about vertical through at least 0°/45°/90° using the monitor-arm head (confirm the VESA head rotates); if not, the 40×40 bolt pattern needs 45° holes.
7. **MECH/BOM:** rubber isolation feet or a separate stand for the face cradle, so the forehead does not feel the stroke rhythm through the desk (confound for Q10).
8. **BOM:** add to the kit: real-hair training head (one trimmed 3–5 cm, one long), Kanekalon wig, 180 mm sphere or hairless foam head, 100 µm monofilament, 50 µm tape, 15/50/100 g tether weights + pulley, carbon paper, foam ear plugs, black cloth, lint roller, IR thermometer, hygrometer, loupe, hair clips, hand mirror.
