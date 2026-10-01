# SP1 ENGINEERING PACKAGE — "FLOAT-ARM" (PROJECT SCRATCH)

**Project SCRATCH · 07-package · 2026-10-01 · Package integrator.** This is the single document Michael builds from. It stands alone: a reader who opens only this file can order parts, print parts, assemble, wire, flash, bench test and run the first human session. It consolidates 03-tournament/DECISION.md, 05-engineering/DESIGN-FREEZE.md as amended by DESIGN-FREEZE-ADDENDUM-1.md, mechanical.md, tips.md, electronics-firmware.md, test-protocols.md, bom.md, firmware/README.md and cad/tips/README.md, with the addendum's rulings applied everywhere they touch.

**Precedence used when sources disagreed:** addendum > mechanical.md > tips.md > electronics-firmware.md > test-protocols.md > freeze. Every resolution is listed in Appendix 1 (Integration notes). Where two documents disagree on a number and the right one could not be determined, both are kept in the text with a **[CONFLICT]** tag and listed in Appendix 1. Every **[VERIFY]** tag from the sources is kept in place and collected in Appendix 2 (Verify before ordering/printing).

**Tag legend.** **[cited]** price or number taken from a project document; **[est]** estimate (prices ±30 %); **[verify]** / **[VERIFY]** must be confirmed against a vendor drawing, listing or the part itself before paying or printing; **[KNOWN] / [EST] / [UNKNOWN]** literature value / engineering estimate / must be measured; **[CONFLICT]** unresolved disagreement between source documents; **[MECH CHOICE: range]** a number the mechanical lead picked inside a range the freeze left open.

**Units:** mm, N, g, s, °C unless stated. Coordinate frame: Z up (gravity −Z), X = stroke direction, Y = across the stroke (nail pitch). Origin O = edge of the centre nail at mid-stroke with the float on its down-stop and the leaves unloaded; the scalp is a sphere R 90 mm with its apex at (0, 0, +4) and centre (0, 0, −86).

**Contents.** 0 Build order and first weekend · A Design overview · B Mechanical architecture · C Dimensions · D Component selection · E Bill of materials · F Fabricated (printed) components · G Scratching tips, TM1 mount, hand wand · H Electronics · I Control logic and firmware · J Assembly · K Safety checklist · L Bench testing · M First human test · N Experiment matrix · O Feedback form · P Iteration map · Quick reference card · Appendix 1 Integration notes · Appendix 2 Verify before ordering/printing · Appendix 3 Session log and packing/cleaning list.

---

## 0. BUILD ORDER AND FIRST WEEKEND

SP1 is built in gated stages. Nothing motorised is ordered until the Stage-0 hand wand has answered the question it exists to answer: does a stiff narrow edge at 0.3–0.5 N reach Michael's scalp through his hair and feel more like a fingernail than a ball does?

### 0.1 Day 0: order (about 30 minutes)

Place **Cart A** (§E, order group A): every Stage-0 row of the tip list (N52 6 × 2 mm magnets, 6 × 1 mm steel keeper discs, 0.30 × 12.7 mm feeler stock, ABS press-on nails, Dunlop 0.88 mm nylon picks, 3 mm chrome-steel balls, M3 × 8 screws, thin and gel CA, 5-minute epoxy, wet-and-dry 400/600/1000/2000, nail files, 0.5–3.0 mm drill-bit set, 0.3 mm marker and clear varnish), one 1 kg spool of bright PETG and one small spool of TPU 90A, the bench-kit rows marked "buy with S0" (short real-hair training head and its table clamp, 10× loupe, 50 µm polyester tape, 10 mm rod, carbon paper, IPA/pipe cleaners/cotton) and the tools marked "buy with S0" (0.1 g kitchen scale, 150 mm calipers, hex keys, aviation snips, flush cutters/stripper/screwdrivers). Cash from an empty shop: $282 (S0 $141 + bench kit $70 + tools $71). If you own a printer with a 220 mm bed, direct drive and a 250 °C hotend you are set; otherwise decide between a printer (about $300–400 [est]) and a print service (about $150–250 [est] for the whole 1.1 kg of PETG, 2–3 weeks).

**Print-test-first parts** (print these the first evening, before anything else, and adjust the slicer's hole compensation from them): the TM1 pocket (one `paddle_with_pocket.stl` with the magnet pause at 23.1 mm print height) and one tip (`tip_W.stl` on its side at 0.10 mm) to prove the tang slides home and cannot enter rotated; then, once Cart B parts are in, P15 (625 bearing press fit), P2 (623 bearing press fit), P13 (XL330 pocket, only after the servo is in hand) and P34 with a leaf scrap (groove grip).

### 0.2 First weekend: the Stage-0 wand (about 3 hours hands-on plus one unattended print night)

Evening before: print plate A in PETG at 0.20 mm (wand handle, two clamp bars, the paddle with the magnet pause, a spare paddle), plate B in PETG at 0.10 mm (W × 2, B45 × 2, H, A45 carrier, P carrier × 2; W/B45 on their sides, carriers tang down), plate C in TPU 90A (two seam sleeves). About 4.5 h of printer time [EST].

Day: follow §G.5 (3-hour build table): clean and test-fit tangs; bond keepers; edge work 400→2000 grit; cut and clamp the 80 mm leaf at 38 mm free length; calibrate the leaf on the kitchen scale to 0.13–0.18 N/mm; practise 0.3 N and 0.5 N ten times each; breakaway and tape test every tip; write blinding codes. Then run the Day-0 tests (§G.6 and §M stage H0): tape test and forearm screen per tip, ink-mark loaded-edge length, wig-head static reach and 200 strokes per tip, then 10 strokes per tip on your own crown and occiput with a blind W-vs-H and B45-vs-H comparison.

**Stage-0 GO** (§M, H0): a nail visibly reaches skin through your hair at ≤ 0.5 N; W or B45 beats H on realism by ≥ 3 points blind; zero hair captures in 200 wig strokes per tip. **NO-GO:** fix the tip (reach, radius, width) before any motorised part is ordered; if no tip reaches skin, the engagement/leaf/paddle question goes to the top of the iteration map (§P-1).

### 0.3 Day after GO: order Cart B and start Stage 1 (about 15 h build over two or three weekends)

Place every Stage-1 cart the same day (§E.10), **Robotis first** (longest lead time; put the second XL330 in that cart as the spare). Before ordering, work through Appendix 2: the three items that change what you click are the lift-spring part number (box 2A), the monitor arm's printed minimum load, and whether a 340 mm X3P cable exists. While parts ship: print the frame, float and hand parts (about 0.9 kg PETG, two to three print days), weighing every float part as it comes off against the 92 g budget (§F.3); set inserts; cut and stone the three leaves. Then build in the §J order, which front-loads the bench tests: hand (Phase A, 5 h, with L2 on the bare hand), float on the bench (Phase B, 3 h, with L3, L6, L1), elbow (Phase C, 3 h), frame/hinge/arm (Phase D, 3 h, with L5 before the servo is even plugged in), electronics bring-up (§I.7, B0–B14), alignment, L4, then L7–L12 and the §K checklist. First human session H1 only after §K is complete and the wig gate (L8) has passed.

### 0.4 Stage summary

| Stage | Time / cash | What | Gate |
|---|---|---|---|
| 0 Hand wand | 3 h hands-on, about $39 marginal ($141 S0 cart from an empty shop) | one TM1 holder on a 0.3 × 12.7 feeler leaf on a 150 mm printed handle; tips W, B45, A45, H, P | nail reaches skin through Michael's hair; W or B45 clearly beats H blind; zero wig captures |
| 1 Full rig | about 15–17 h, $762.50 S1 cart (lean $668.50, see §E.0.4) | monitor-arm-mounted frame, fail-safe hinge, one XL330 elbow, MGN9C float, three-nail hand, PERIODIC + HUMAN firmware | bench L1–L12 and §K pass; wig head passes; first human sessions rate "fingernails" ≥ 4/7 on at least one tip |
| 2 Experiment matrix | 0 h build, about 15 sessions | §N on Stage-1 hardware: tips × weight × speed × variation × direction × engagement | §P decides SP2 |
| 3 Gated upgrades | 3 h, $43.49 | yaw servo (XL330 ID 2 on a lazy-Susan bearing) if habituation/monotony dominates; 5 kg bar load cell in the wrist slot if force data are needed | earned by Stage-2 feedback only |

---

## A. DESIGN OVERVIEW

### A.1 What SP1 is

SP1 is a **frame-mounted, single-servo, dead-weight-forced, bidirectional three-nail rake with geometric lift-off**, hung from a desk-clamped monitor arm over a face cradle. Nothing is worn on the head. Michael sits (or lies prone) with his face in a massage cradle; the module hangs above his crown or occiput; three fingernail-like tips on spring-steel leaves rest on his scalp under a dead weight of 0.9–1.5 N total (0.3–0.5 N per nail) and are swept back and forth over a 30–40 mm chord by one Dynamixel XL330 servo, lifting clear of the hair at both ends of every stroke purely by geometry. A hold-to-run button in one hand and an NC e-stop under the other hand are in series with the only power that can move anything; letting go of the button lifts the whole hand ≥ 25 mm off the head in about 0.1 s by spring.

### A.2 The hypothesis SP1 tests (from DECISION.md)

"A stiff narrow edge (R 0.4–0.5 mm) at 0.3–0.5 N per contact, sliding 50–150 mm/s over a 30–40 mm chord with lift-off at every reversal, three contacts at 24 mm pitch* with unequal preloads, and irregular timing, is perceived as a person's fingernails scratching the scalp rather than as a machine — and irregularity (vs. PERIODIC) is a large part of that."

*DECISION.md and the freeze wrote 20 mm; the addendum (D2) sets 24 mm because at 20 mm paddle roll under leaf bending closes adjacent tip gaps to 0.4 mm (inside the hair-trap range). 24 mm is inside the human 20–25 mm spread-finger range; the Sensation Gate must assess whether 24 mm changes the fingernail illusion, and the experiment matrix keeps pitch as a noted constant (§N.1).

In Michael's terms: we are not building a massager that happens to have points on it. We are building a machine whose only job is to put something that behaves like the free edge of a fingernail against the skin of the scalp, lightly, moving, through the hair, with the timing of a person who is not thinking about it, and then to let Michael say whether it feels like a person. Every knob that the sensation model ranked as important (tip edge, per-nail force, stroke speed, chord length, lift at reversal, timing irregularity, direction relative to the hair lie, engagement depth) is a dial or a swap on this rig, so the first sessions are an experiment, not a demo.

### A.3 Why this mechanism won (DECISION.md, in Michael's terms)

1. **A headband is not a force reference.** All three tournament judges independently found that anything worn on the head drifts: ±3 mm of seating × 0.2–0.4 N/mm of leaf stiffness is ±0.6–1.2 N per nail, larger than the whole 0.3–0.9 N scratch window. A dead weight on a vertical slide makes the hand-level force a true mechanical constant that survives head motion and servo faults. This is the single most important engineering fact the programme found.
2. **One bought smart servo does the stroke, so the pattern lives in firmware.** The rank-1 sensory variable, pattern irregularity (length, speed, timing, pause, direction), becomes ~100 lines of code, while the ceiling on force stays a weight and a stop. Single-motor closed-path mechanisms (cams, cranks) are kinematically rigid and cannot vary anything; they survive only as this rig's PERIODIC control mode.
3. **Lift-off at every reversal comes free from geometry.** The hand hangs 84 mm below the elbow pivot, so the tip path is concave-up while the scalp is convex; the gap grows as Lθ²/2·(1 + L/R). With H = 80 mm, R ≈ 90 mm and a 4 mm engagement set by the float's down-stop, the nails are in contact over a ~37 mm chord and are fully lifted (≥ 5.7 mm on the last nail, 11.2 mm on the centre nail) by ±25°. No lift servo, no firmware, no tendon.
4. **Both strokes are scratches.** Red Team 1 showed one-way lifted strokes read as "a 3-tooth comb sweeping"; geometric lift at both ends makes the return stroke a scratch too (human primitive P1, bidirectional rake), with a symmetric wedge tip (W) as the default and the 45° nail-mimic family available through the same TM1 mount.
5. **A bought rail instead of a printed parallelogram.** Red Teams 2 and 3 both found an inclined parallelogram float amplifies friction into normal force (N = W/(1 − 0.577 µ), 1.4–2.4×) and is the highest-risk printed part. A vertical MGN9 miniature rail gives N = W for any µ, zero printed tolerance, $12.
6. **It is the design Michael is most likely to finish.** Named major parts about $250 (whole cash BOM from an empty shop is larger, §E.1), ~17–22 build hours after a 3-hour hand wand, two toolchains at most (printing, Arduino-style firmware), every printed part supplied as OpenSCAD + STL.

**Rejected:** head-worn designs (force drift, ≥ 500 g on the head, bone-conducted gear noise, one patch, no quick release); direct-drive FOC (best sensation hardware, but a skill gate and an unmeasured torque cap; it is the SP2 stroke-axis upgrade); full C-arm yoke ($500+, 42 h; its float/dead-weight/load-cell ideas are adopted, the yoke is SP2 if region wander proves decisive); lift servo + tendon (geometry does it; a second servo, if earned by Stage 2, goes on YAW); a separate control wand (the PERIODIC firmware mode is the control condition; the motorless Day-0 hand wand stays); forehead dead-man switch, OLED, INA219, load cell (hold-to-run + NC e-stop is the dead-man; a kitchen scale calibrates the dead weight; a 40 × 12 mm load-cell slot is reserved in the wrist for Stage 3).

### A.4 Massager-vs-scratcher self-check (scratch-model §8)

| # | Criterion | SP1 |
|---|---|---|
| 1 | Edge, not pad: stiff (E > 1 GPa) edge R 0.05–0.5 mm, contact length 2–8 mm | PETG wedge/plate R 0.4–0.5 mm, about 4 mm loaded at 0.3 N; tip H (3 mm ball) is the deliberate massager control |
| 2 | Reaches the skin at ≤ 0.3 N in medium hair | the Stage-0 wand question; paddles protrude 37.5 mm below the knuckle plate |
| 3 | Light: 0.05–0.5 N per contact, total ≤ 2.5 N | 0.24–0.59 N per nail, 0.88–1.47 N total (W1–W3), dead-weight set |
| 4 | Slides ≥ 10 mm per cycle with slip at the interface | 26–46 mm chord, sliding, scalp carried by the cradle |
| 5 | 2–20 cm/s, 1–4 Hz, no component > 20 Hz | 50–150 mm/s peak, 1–3 strokes/s |
| 6 | Deflects hair near the root | edge at skin level, paddles through the canopy |
| 7 | 3–5 independent contacts at 16–28 mm pitch, ≥ 20 % force spread | three leaves at 24 mm pitch, 0.8 / 1.0 / 1.2 shares, ±8 mm stagger (80 ms landing spread at 100 mm/s) |
| 8 | Irregular, with pauses and lift-offs | HUMAN mode pattern engine; PERIODIC is the control |
| 9 | Compliant at the tip ≤ 0.5 N/mm, travel ≥ 5 mm | leaves 0.12 / 0.15 / 0.18 N/mm, 5 mm to the stop, plus the 28 mm float |
| 10 | Unloads at reversal, lifts between bouts | geometric lift at both ends; pauses at the +25° park |
| 11 | Hair-safe geometry: no rotation or closed aperture within hair reach | servo and idler at |Y| ≥ 101 mm, ≥ 75 mm above the scalp; only tips, paddles, boot and knuckle plate inside the 30 mm zone; no 0.04–3 mm gaps |
| 12 | Sounds like a scratch, not a motor | UNSURE (K4.7 ≤ 70 dBA hard, ≤ 60 target; ear-plug pair O-5 tests it) |

---

## B. MECHANICAL ARCHITECTURE

### B.1 The stack, top to bottom

1. **Monitor arm.** Desk-clamp gas-spring single-monitor arm, VESA 75 × 75 (and 100), minimum rated load ≤ 2.0 kg, reach ≥ 400 mm, VESA centre reachable 300–650 mm above the desk, head tilt ≥ ±45°, head swivel (pan about a vertical axis) ≥ ±90°, lockable rotation, desk clamp 10–85 mm with its steel reinforcement plate. The arm reaches over the seated user's head from the side/behind. **Stage-1 yaw aim (0/45/90°) is set with the arm's head swivel by tape marks** (addendum ruling 8); the module's internal 40 × 40 joint works only at 0°/180° in Stage 1.
2. **Ballast stack.** 3 mm mild-steel plates 100 × 100 mm (235 g each) between the arm's VESA plate and the adapter, so the arm is at or above its printed minimum load + 10 % (a gas arm below its minimum creeps upward). For a 2 kg-minimum arm: 2.2 − 1.1 = 1.1 kg, five plates; remove plates until the arm holds height (K2.14). A 1–6.5 kg "light" arm needs none. Ballast is fixed to the arm, never to the hinged module.
3. **VESA adapter P1 (printed).** 6 mm PETG plate 140 (Y) × 145 (Z) mm with two ribs, VESA 75 holes; carries the two hinge ears (to the pin at X −60, Z 84), the magnet arm (magnet seat at X −81…−66, Z 34, face toward +X), the adjustable up-stop boss (M4 screw with rubber cap, between the ears), the electronics tray seat (front face, Y +15…+50, Z 120–165), two pulley bosses on the top edge at Y ±60 (623ZZ on M3 × 16), two spring channels on the rear face at Y ±60 (outboard of the arm's VESA plate) and two spring-anchor hooks at Z 30.
4. **Fail-safe hinge.** M6 × 80 socket-head screw as a pin, nyloc nut, through the adapter ears (Y ±25…±35) and the printed frame knuckle P5 (Y ±24) bolted to the bottom of the 2020 post, 0.5 mm PTFE/nylon washers between, bores Ø 6.3 reamed. Hinge axis parallel to Y at X −60, Z 84: 60 mm behind the elbow axis and level with it (most vertical nail motion per degree). Working position = frame rotated down with the steel keeper (25 × 25 × 3 mm on the keeper lever P6, 50 mm below the pin) held against the **5 V holding electromagnet** (Adafruit 3872, P20/15, 25 N) on the adapter's magnet arm, one layer of 0.075 mm PTFE tape on the magnet face. **Two extension springs** (6.5 N each at working extension, addendum D11) pull the frame up through 1.0 mm Dyneema cords over the two 623ZZ pulleys to the cord bar P7 on the post 64 mm above the pin. Power to the magnet comes only from the actuator rail (§H): loss of rail power → frame rotates up 25° to the rubber up-stop → nails rise 32.9 mm (≥ 29 mm clear of the scalp at any engagement 2–8 mm) in ≤ 0.14 s. Reset by pulling the reset cord (toggle at the desk edge, about 10 N) or pressing the reset tab on the spine (about 11 N) until the keeper clicks onto the live magnet.
5. **Module frame (2020 aluminium extrusion + printed nodes, addendum D8).** Post 104 mm (vertical, X −70…−50, Z 92–196) **[CONFLICT: see Appendix 1 note 1 — the frame CAD generator models the post as 122 mm, Z 94–216]**; spine 80 mm (horizontal, X −50…−15, Z 196–216, bracketed to the post's front face, reset tab P10 at its front end); elbow-carrier beam 270 mm (along Y, X −35…−15, Z 164–184) hung from the spine through the yaw joint plates (P8 under the spine with 8 M3 inserts at 45° spacing on Ø 56.6; P9 on the beam with 4 holes on a 40 × 40 square; yaw axis X −25, Y 0; 4 × M3 × 14 [verify length]). Two printed drop legs P11/P12 bolt to the beam ends (M5 end tap + T-nuts) and come down and forward to the elbow axis: the −Y leg ends in the **servo cradle P13**, the +Y leg in the **idler housing P15**. Both legs carry smooth guard caps G2/G3 (P17/P18) below them.
6. **Elbow axis.** Dynamixel XL330-M288-T in the cradle **beside the palm on the −Y side** (body Y −101…−127, Z 74–108 [VERIFY axis 10 mm from body end]), output axis parallel to Y at (X 0, Z 84), **horn facing +Y**, driving a **two-sided yoke** (addendum D6): cheek A (P19) on a printed horn adapter disc P16 (4 × M3 × 10 on Ø 18), cheek B (P20) on a Ø 5 × 25 mm shoulder screw through a 625-2RS bearing pressed into the idler housing (Y +101…+111). The idler housing is slotted ±1.5 mm in X and Z so the idler is aligned to the servo axis after assembly (yoke swings freely through ±32° with no tight spot). TPU bumpers on the cradle stop a lug on cheek A at ±32°, outside the firmware's ±28° absolute and ±25° nominal. A Ø 3.1 mm **zero-pin hole** through cheek A and the cradle flange is coincident at θ = 0°: servo zero is set with a 3 mm pin in this hole, never by letting the arm hang (it is top-heavy).
7. **Arm (yoke) and radial float.** The two 5 mm PETG cheeks (Y ±93…±98) reach from the axis forward to X +57 and are joined by the crossbar P21 (196 × 16 × 16 box beam, X +45…+57, Z 80–96) whose middle carries the **rail mast** (24 wide × 5 thick, X +40…+45, from Z 64 to an R 90 arc about the axis). The **MGN9 rail, 100 mm** (Z 68–168) is on the mast's −X face, aligned radially (plumb at θ = 0°); the **MGN9C carriage** (16 g, seals and wipers removed, one drop of oil; addendum D7) carries the printed riser P26 (L-bracket back over the palm to the upper wrist seat at X 0). Carriage travel 24 + e mm between a TPU up-stop pad and an **M3 × 16 knurled thumbscrew down-stop** that sets the engagement e = 2–8 mm (default 4 mm, L_max = 84.0 mm from the axis to the free centre-nail edge). A printed scale strip P25 on the rail shroud and a pointer fin on the riser read carriage rise above the down-stop. Dead weight W = carriage + riser + wrist + hand (bare W1 = 90.1 g = 0.884 N, budget ≤ 92 g) + M8-washer slug sets on the Ø 8 weight post (+30 g, +60 g, up to +100 g), captured by a cap and nylon thumbscrew. A trim-spring hook (0.5 mm elastic cord to a cleat on the mast) unloads 30 g for the 0.6 N level.
8. **Wrist: keyed magnetic breakaway seat.** Lower seat moulded into the palm lid P33 (flat ring Ø 40/30 at Z 69, 45° cone boss Ø 18/12 × 3 with a 12 × 1.5 mm steel keeper flush in its top, Ø 3 round-ended key peg at r 17 on +X); upper seat P28 on the riser arm (Ø 44 × 5 plate, conical recess, K&J D61 N42 disc flush in the recess floor under one layer of 0.05 mm PTFE tape, 3.3 × 2.2 radial key slot). The seat releases by tipping about the ring edge at **1.9–2.1 N tangential at the nail tips** (red line 3) and never below 5 N straight down. A **25 mm loop of 1.0 mm Dyneema** (addendum ruling 3) between eyelets in the upper seat and the lid, stowed folded in a cup in the lid, tethers a released hand so it can only drop 25 mm (which the 32.9 mm fail-safe lift still clears) and can never reach the face. The riser-to-seat joint carries a 41 × 13 × 8 mm pocket bridged by a printed filler P47 in Stage 1 and a 40 × 12 mm bar load cell in Stage 3.
9. **Hand.** Three nails at **24 mm pitch in Y** (span 48 mm), stepped ±8 mm in X as a diagonal (L at (−8, −24), C at (0, 0), R at (+8, +24)); the outer edges sit 3.6 mm lower than the centre so all three leaves deflect equally on an R 90 mm head. Each nail is the tip lead's drafted PETG paddle (T1 outer, T2 centre with a 9 mm riser) carrying a TM1 pocket, clamped without holes to its own **0.30 × 12.7 mm spring-steel feeler leaf** cantilevered along Y: L 70 mm (0.12 N/mm), C 67 mm (0.15 N/mm), R 64 mm (0.18 N/mm), giving preload shares 0.8 / 1.0 / 1.2 by rate, not shims. Leaves root in the enclosed palm tray P32 on pre-tilted seats (L 4.4°, C 4.7°, R 5.0° about X, so each paddle hangs vertical at the nominal 2.67 mm deflection); L and R root outboard at level 0, C roots on the −Y side one level up (+9 mm) and crosses over L. Each leaf has an **M3 nylon hard-stop screw at 5.0 mm of tip travel** (addendum D5; force at the stop 0.6–0.9 N; the stop structure is proof-loaded to 7.5 N per nail). Drag twists each leaf 3.6–5.0° at 0.3 N (addendum D13), a useful ~0.1 N/mm tangential compliance. The palm is a clamshell (tray P32 + lid P33, 52 × 169 × 33 mm overall, seam at Z 48–66 taped with 0.05 mm PTFE) above a smooth spherical **knuckle plate P30** (R 90 underside, 1.6 mm thick, 37.5 mm above the centre edge, all edges R 3, Ra ≤ 0.8 µm). The three paddles exit through **one shared slot** (≥ 4.5 mm clear of L and R, 6.0 mm of C) sealed by **one slack 0.25 mm Shore 40A silicone membrane bonded to each paddle** at z 26–28 with Sil-Poxy (addendum D4): no sliding contact, no 0.04–3 mm gap. Nail edges are 37.5 mm below the plate at rest (34.9 mm at nominal load).
10. **Tips.** SP1-TM1 magnetic tang/pocket mount (§G): 10 × 4 × 12 mm chamfered tang, 10.3 × 4.3 × 12.5 mm pocket, N52 6 × 2 mm magnet + 6.0 × 3.9 × 1.0 mm steel slug, 4–8 N axial breakaway, TPU 90A seam sleeve over the joint. Tip set W (default), B45, B45-12, A45 (gated), E, H (control), P.
11. **Face cradle.** Tabletop massage face cradle on its own stand (SEAT, crown) or a horseshoe face cushion on the bed (PRONE, occiput default). The cradle must not share the arm's desk, or stands on an 18 mm plywood baseboard on four Ø 30 × 15 mm isolation feet (stroke rhythm through the desk is a confound).

### B.2 Degrees of freedom and motion generation

| DOF | Driven by | Range | Role |
|---|---|---|---|
| Stroke (elbow, about Y) | XL330-M288-T, current-based position mode | ±25° nominal (firmware clamp), ±28° absolute (servo EEPROM), ±32° mechanical bumpers | the scratch; chord 26–54 mm depending on engagement; lift-off at both ends by geometry |
| Radial float (along the arm) | gravity (dead weight) on the MGN9C carriage | 24 + e mm between stops (28 mm at e = 4) | sets the normal force as a mechanical constant N = W; absorbs head motion and breathing (5–15 mm) |
| Per-nail compliance | three feeler leaves | 5.0 mm to the hard stop | follows curvature; unequal shares; tangential torsion compliance |
| Wrist breakaway | magnetic keyed seat | releases at ~2 N tangential | red line 3: no nail ever carries > 2 N tangential |
| Fail-safe lift (about the hinge) | two springs vs electromagnet | 25° up to the stop (nails +32.9 mm, +28.2 mm forward) | red line 8: de-energised state is lifted-off |
| Yaw (aim about vertical) | monitor-arm head swivel, tape marks | 0 / 45 / 90° | direction vs hair lie (Stage 1); XL330 ID 2 on the internal joint in Stage 3 |
| Pitch / roll (rail plumb) | monitor-arm head tilt and rotation screw | ±45° / lock | aim at crown or occiput; rail vertical ±1° |
| Height (engagement) | monitor arm + apex gauge; down-stop thumbscrew | e = 2–8 mm | contact chord and dead-weight plateau |

### B.3 General arrangement, side elevation (XZ, looking along +Y)

Drawn by the integrator from the mechanical.md §2 coordinates (module latched, arm at 0°, float on its down-stop). Scale 1.6 px/mm. Y positions are not shown; see the plan view for the yoke, servo and idler.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 540" width="720" height="540" font-family="Helvetica, Arial, sans-serif" font-size="10">
  <rect x="0" y="0" width="720" height="540" fill="#fff"/>
  <text x="10" y="16" font-size="13" font-weight="bold">SP1 Float-Arm, side elevation (XZ). +X to the right (stroke), +Z up. Latched, θ = 0°, float on its down-stop.</text>
  <!-- origin: X=0 at px 330, Z=0 at py 440; 1.6 px/mm -->
  <!-- scalp sphere R90 centre (0,-86): arc from X=-60 to +60 -->
  <path d="M 234 470.2 A 144 144 0 0 1 426 470.2" fill="none" stroke="#999" stroke-width="1.5" stroke-dasharray="5 3"/>
  <text x="440" y="474" fill="#777">scalp sphere R 90, apex Z +4</text>
  <line x1="330" y1="433.6" x2="330" y2="446" stroke="#999" stroke-width="1"/><text x="334" y="452" fill="#777">O (centre nail edge, Z 0)</text>
  <!-- monitor arm VESA plate X -139..-126, Z 72.5..147.5 -->
  <rect x="107.6" y="204" width="20.8" height="120" fill="#ddd" stroke="#333"/>
  <text x="60" y="200" fill="#333">monitor-arm VESA plate</text>
  <text x="60" y="212" fill="#333">+ ballast stack</text>
  <!-- adapter plate P1 X -126..-120, Z 25..170 -->
  <rect x="128.4" y="168" width="9.6" height="232" fill="#f6d6a8" stroke="#333"/>
  <text x="70" y="398" fill="#333">P1 VESA adapter</text>
  <!-- hinge ears: from X -120 to -60 at Z 70..98 -->
  <polygon points="138,283.2 234,290 234,310 138,328" fill="#f6d6a8" stroke="#333"/>
  <text x="150" y="340" fill="#333">hinge ears</text>
  <!-- hinge pin at (-60,84) -->
  <circle cx="234" cy="305.6" r="5" fill="#fff" stroke="#000" stroke-width="2"/>
  <text x="196" y="352" fill="#000" font-weight="bold">hinge pin (−60, 84)</text>
  <!-- magnet arm and magnet X -81..-66, Z 24..44 -->
  <polygon points="138,392 200,392 200,384 138,384" fill="#f6d6a8" stroke="#333"/>
  <rect x="200.4" y="369.6" width="24" height="32" fill="#c9c9c9" stroke="#333"/>
  <text x="148" y="418" fill="#333">magnet P20/15 (face +X)</text>
  <!-- keeper lever: post foot down to keeper at X -66..-54, Z 19..49 -->
  <polygon points="224.4,361.6 243.6,361.6 243.6,290 224.4,290" fill="#f6d6a8" stroke="#333"/>
  <rect x="224.4" y="361.6" width="19.2" height="48" fill="#f6d6a8" stroke="#333"/>
  <rect x="224.4" y="370" width="4.8" height="40" fill="#777" stroke="#333"/>
  <text x="250" y="400" fill="#333">P6 keeper lever + 3 mm steel keeper</text>
  <!-- up-stop boss near (-115, 104) -->
  <rect x="140" y="268" width="14" height="8" fill="#555"/><text x="100" y="262" fill="#333">up-stop (M4 + bumper)</text>
  <!-- post X -70..-50, Z 92..196 -->
  <rect x="218" y="126.4" width="32" height="166.4" fill="#bcd" stroke="#333"/>
  <text x="252" y="140" fill="#333">2020 post 104 mm</text>
  <!-- cord bar at Z148, X -76..-38 -->
  <rect x="208.4" y="193.6" width="60.8" height="8" fill="#f6d6a8" stroke="#333"/>
  <!-- cord to pulley at (-123,148) -->
  <line x1="208" y1="197.6" x2="133" y2="197.6" stroke="#06c" stroke-width="1.5"/>
  <circle cx="133.2" cy="203.2" r="8" fill="#fff" stroke="#06c" stroke-width="1.5"/>
  <text x="60" y="186" fill="#06c">P2 pulley (623ZZ)</text>
  <!-- springs down the rear face X -130, Z 30..148 -->
  <line x1="122" y1="203" x2="122" y2="392" stroke="#06c" stroke-width="2" stroke-dasharray="3 3"/>
  <text x="40" y="300" fill="#06c">2 × lift springs</text><text x="40" y="312" fill="#06c">(rear face, Y ±60)</text>
  <!-- spine X -50..-15, Z 196..216 -->
  <rect x="250" y="94.4" width="56" height="32" fill="#bcd" stroke="#333"/>
  <text x="262" y="88" fill="#333">spine 80 mm · reset tab P10</text>
  <!-- yaw plates X -60..10, Z 184..196 -->
  <rect x="234" y="126.4" width="112" height="19.2" fill="#f6d6a8" stroke="#333"/>
  <text x="350" y="140" fill="#333">P8/P9 yaw plates (axis X −25)</text>
  <!-- carrier beam X -35..-15, Z 164..184 (section) -->
  <rect x="274" y="145.6" width="32" height="32" fill="#bcd" stroke="#333"/>
  <text x="310" y="170" fill="#333">2020 carrier beam 270 mm (along Y)</text>
  <!-- drop leg from beam (-25,164) to axis (0,84) -->
  <polygon points="282,177.6 298,177.6 338,300 322,312" fill="#f6d6a8" stroke="#333"/>
  <text x="352" y="200" fill="#333">P11/P12 drop legs (Y ±115…±135)</text>
  <!-- servo body X -10..10, Z 74..108 (at Y -101..-127, behind) -->
  <rect x="314" y="267.2" width="32" height="54.4" fill="none" stroke="#333" stroke-dasharray="3 2"/>
  <text x="352" y="286" fill="#333">XL330 (Y −101…−127)</text>
  <!-- elbow axis -->
  <circle cx="330" cy="305.6" r="5" fill="#fff" stroke="#000" stroke-width="2"/>
  <text x="352" y="310" fill="#000" font-weight="bold">elbow axis (0, 84)</text>
  <!-- yoke cheek outline: axis to X+57, Z 64..104 -->
  <polygon points="310,276 421,276 421,337.6 330,337.6" fill="#e0e8c0" stroke="#333" opacity="0.8"/>
  <text x="352" y="330" fill="#333">yoke cheeks A/B (Y ±93…±98)</text>
  <!-- crossbar X 45..57, Z 80..96 -->
  <rect x="402" y="286.4" width="19.2" height="25.6" fill="#f6d6a8" stroke="#333"/>
  <text x="426" y="296" fill="#333">P21 crossbar</text>
  <!-- mast X 40..45 Z 64..175 -->
  <rect x="394" y="160" width="8" height="177.6" fill="#f6d6a8" stroke="#333"/>
  <text x="426" y="176" fill="#333">rail mast (top: arc R 90 about the axis)</text>
  <!-- rail X 33.5..40, Z 68..168 -->
  <rect x="383.6" y="171.2" width="10.4" height="160" fill="#888" stroke="#333"/>
  <text x="426" y="216" fill="#333">MGN9 rail 100 mm</text>
  <!-- carriage X 30..40, Z 74..103 -->
  <rect x="378" y="275.2" width="16" height="46.4" fill="#444" stroke="#000"/>
  <text x="426" y="256" fill="#333">MGN9C carriage (at the down-stop)</text>
  <!-- down-stop thumbscrew at X 29, Z 69 -->
  <rect x="372" y="326" width="6" height="12" fill="#555"/><text x="426" y="336" fill="#333">down-stop thumbscrew (e = 2–8 mm)</text>
  <!-- riser arm X 0..30 at Z 69..74 -->
  <rect x="330" y="321.6" width="48" height="8" fill="#f6d6a8" stroke="#333"/>
  <!-- weight post X -4..4, Z 74..108 -->
  <rect x="323.6" y="267.2" width="12.8" height="54.4" fill="#f6d6a8" stroke="#333"/>
  <rect x="318" y="267" width="24" height="5" fill="#333"/>
  <text x="262" y="262" fill="#333">weight post + M8 slugs</text>
  <!-- upper seat Z 69..74, X -22..22 -->
  <rect x="294.8" y="321.6" width="70.4" height="8" fill="#f6d6a8" stroke="#333"/>
  <text x="196" y="328" fill="#333">wrist seat Z 69 (D61 + keeper)</text>
  <!-- palm X -26..26 Z 38..66 -->
  <rect x="288.4" y="334.4" width="83.2" height="44.8" fill="#f6d6a8" stroke="#333"/>
  <text x="200" y="362" fill="#333">palm P32/P33 (Y −88…+81)</text>
  <!-- knuckle plate Z 33..38 arc -->
  <path d="M 279 388 A 144 144 0 0 1 381 388" fill="none" stroke="#333" stroke-width="4"/>
  <text x="200" y="392" fill="#333">knuckle plate P30 (R 90)</text>
  <!-- paddles: three at X -8, 0, +8, from Z 37.5 down to pocket mouths ~Z 12.5/8.9, tips Z 0 / -3.6 -->
  <polygon points="308,382 330,382 326,420 312,420" fill="#f9c04a" stroke="#333"/>
  <polygon points="320,382 342,382 338,422 324,422" fill="#f9c04a" stroke="#333"/>
  <polygon points="332,382 354,382 350,420 336,420" fill="#f9c04a" stroke="#333"/>
  <polygon points="312,420 326,420 320,446 318,446" fill="#f90" stroke="#333"/>
  <polygon points="324,422 338,422 331,440 330,440" fill="#f90" stroke="#333"/>
  <polygon points="336,420 350,420 344,446 342,446" fill="#f90" stroke="#333"/>
  <text x="372" y="412" fill="#333">paddles T1/T2 + TM1 tips (L, C, R at X −8, 0, +8)</text>
  <!-- dimension: axis to O = 84 -->
  <line x1="300" y1="305.6" x2="300" y2="440" stroke="#c00" stroke-width="1"/>
  <line x1="296" y1="305.6" x2="304" y2="305.6" stroke="#c00"/><line x1="296" y1="440" x2="304" y2="440" stroke="#c00"/>
  <text x="246" y="376" fill="#c00" font-weight="bold">L_max 84</text>
  <!-- dimension: hinge to axis 60 -->
  <line x1="234" y1="296" x2="330" y2="296" stroke="#c00" stroke-width="1"/><text x="262" y="292" fill="#c00" font-weight="bold">60</text>
  <!-- fail-safe arrow -->
  <path d="M 440 460 q 30 -40 10 -70" fill="none" stroke="#c00" stroke-width="2"/><polygon points="446,386 456,392 452,400" fill="#c00"/>
  <text x="456" y="440" fill="#c00">rail off: frame lifts 25°,</text><text x="456" y="452" fill="#c00">nails +32.9 mm, +28.2 mm forward</text>
  <text x="10" y="528" fill="#555">Colours: tan = printed PETG, blue = 2020 extrusion, grey = bought steel/rail, yellow/orange = tip-lead paddles and tips, blue lines = springs/cords. Not to be used for dimensions: see §C.</text>
</svg>

### B.4 General arrangement, plan view (XY, looking down)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 520" width="720" height="520" font-family="Helvetica, Arial, sans-serif" font-size="10">
  <rect x="0" y="0" width="720" height="520" fill="#fff"/>
  <text x="10" y="16" font-size="13" font-weight="bold">SP1 Float-Arm, plan view (XY). +X to the right (stroke), +Y up the page (nail pitch). Scale 1.6 px/mm.</text>
  <!-- origin X=0 at px 360, Y=0 at py 270 -->
  <!-- adapter plate X -126..-120, Y -70..70 -->
  <rect x="158.4" y="158" width="9.6" height="224" fill="#f6d6a8" stroke="#333"/><text x="60" y="166" fill="#333">P1 adapter (Y ±70)</text>
  <!-- VESA plate X -139..-126 Y -50..50 -->
  <rect x="137.6" y="190" width="20.8" height="160" fill="#ddd" stroke="#333"/><text x="60" y="200" fill="#333">arm VESA plate</text>
  <!-- pulleys at X -123, Y ±60 -->
  <circle cx="163" cy="174" r="6" fill="#fff" stroke="#06c"/><circle cx="163" cy="366" r="6" fill="#fff" stroke="#06c"/>
  <!-- hinge ears Y ±25..±35, X -120..-60 -->
  <rect x="168" y="214" width="96" height="16" fill="#f6d6a8" stroke="#333"/><rect x="168" y="310" width="96" height="16" fill="#f6d6a8" stroke="#333"/>
  <line x1="264" y1="206" x2="264" y2="334" stroke="#000" stroke-width="2" stroke-dasharray="6 3"/><text x="226" y="200" fill="#000" font-weight="bold">hinge axis X −60</text>
  <!-- knuckle Y ±24 -->
  <rect x="248" y="231.6" width="32" height="76.8" fill="#f6d6a8" stroke="#333"/>
  <!-- post X -70..-50, Y ±10 -->
  <rect x="248" y="254" width="32" height="32" fill="#bcd" stroke="#333"/><text x="284" y="246" fill="#333">post</text>
  <!-- spine X -50..-15 Y ±10 -->
  <rect x="280" y="254" width="56" height="32" fill="#bcd" stroke="#333"/>
  <!-- yaw plates 70x70 centred X -25, Y 0 -->
  <rect x="264" y="214" width="112" height="112" fill="none" stroke="#333" stroke-dasharray="3 2"/><text x="290" y="212" fill="#333">yaw plates 70 × 70, axis (−25, 0)</text>
  <!-- carrier beam X -35..-15, Y -135..135 -->
  <rect x="304" y="54" width="32" height="432" fill="#bcd" stroke="#333"/><text x="250" y="60" fill="#333">carrier beam 270 (Y ±135)</text>
  <!-- drop legs at Y ±115..135: from beam to X 0 -->
  <polygon points="336,54 336,86 360,86 360,70" fill="#f6d6a8" stroke="#333"/><polygon points="336,454 336,486 360,486 360,470" fill="#f6d6a8" stroke="#333"/>
  <!-- servo body X -10..10, Y -127..-101 (Y negative = down the page) -->
  <rect x="344" y="431.6" width="32" height="41.6" fill="#999" stroke="#333"/><text x="382" y="458" fill="#333">XL330 body (Y −101…−127), horn faces +Y</text>
  <!-- horn Y -104..-101 -->
  <rect x="344" y="431.6" width="32" height="4.8" fill="#555"/>
  <!-- idler housing Y +101..+111 -->
  <rect x="344" y="92.4" width="32" height="16" fill="#999" stroke="#333"/><text x="382" y="104" fill="#333">idler (625-2RS) Y +101…+111</text>
  <!-- elbow axis line along Y at X 0 -->
  <line x1="360" y1="86" x2="360" y2="470" stroke="#000" stroke-width="1.5" stroke-dasharray="8 3"/><text x="364" y="84" fill="#000" font-weight="bold">elbow axis X 0</text>
  <!-- yoke cheeks Y ±93..±98, X -10..57 -->
  <rect x="344" y="113.2" width="107.2" height="8" fill="#e0e8c0" stroke="#333"/><rect x="344" y="418.8" width="107.2" height="8" fill="#e0e8c0" stroke="#333"/>
  <text x="456" y="120" fill="#333">cheek B (idler side)</text><text x="456" y="426" fill="#333">cheek A (servo side)</text>
  <!-- crossbar X 45..57, Y ±98 -->
  <rect x="432" y="113.2" width="19.2" height="313.6" fill="#f6d6a8" stroke="#333"/><text x="456" y="270" fill="#333">P21 crossbar + rail mast (X 40…57)</text>
  <!-- mast X 40..45 Y ±12 -->
  <rect x="424" y="250.8" width="8" height="38.4" fill="#f6d6a8" stroke="#333"/>
  <!-- rail X 33.5..40 Y ±4.5 -->
  <rect x="413.6" y="262.8" width="10.4" height="14.4" fill="#888" stroke="#333"/>
  <!-- carriage X 30..40 Y ±10 -->
  <rect x="408" y="254" width="16" height="32" fill="#444"/>
  <!-- riser arm X 0..30 Y ±6 -->
  <rect x="360" y="260.4" width="48" height="19.2" fill="#f6d6a8" stroke="#333"/>
  <!-- upper seat Ø44 at (0,0) -->
  <circle cx="360" cy="270" r="35.2" fill="#f6d6a8" stroke="#333" opacity="0.9"/><text x="300" y="300" fill="#333">wrist seat Ø 44</text>
  <!-- palm X -26..26, Y -88..81 -->
  <rect x="318.4" y="140.4" width="83.2" height="270.4" fill="none" stroke="#333" stroke-width="1.5"/><text x="404" y="150" fill="#333">palm 52 × 169 (Y −88…+81)</text>
  <!-- nails: L(-8,-24) C(0,0) R(8,24); 8 mm wide edges along Y -->
  <rect x="345.2" y="301.6" width="4" height="12.8" fill="#f90" stroke="#333"/><text x="300" y="312" fill="#333">L (−8, −24)</text>
  <rect x="358" y="263.6" width="4" height="12.8" fill="#f90" stroke="#333"/><text x="366" y="262" fill="#333">C (0, 0)</text>
  <rect x="370.8" y="225.2" width="4" height="12.8" fill="#f90" stroke="#333"/><text x="380" y="236" fill="#333">R (+8, +24)</text>
  <!-- pitch dimension -->
  <line x1="300" y1="231.6" x2="300" y2="308" stroke="#c00"/><text x="262" y="274" fill="#c00" font-weight="bold">pitch 24</text>
  <!-- stroke arrow -->
  <line x1="480" y1="300" x2="560" y2="300" stroke="#c00" stroke-width="2"/><polygon points="560,295 570,300 560,305" fill="#c00"/><polygon points="480,295 470,300 480,305" fill="#c00"/>
  <text x="476" y="316" fill="#c00">stroke ±25° (chord 26–54 mm)</text>
  <!-- electronics tray on adapter front face Y +15..+50 -->
  <rect x="168" y="190" width="30" height="56" fill="#cfe" stroke="#333"/><text x="200" y="196" fill="#333">P3 tray</text>
  <text x="10" y="508" fill="#555">Hair exclusion: everything that rotates (horn, idler) is at |Y| ≥ 101 mm and ≥ 75 mm above the scalp; the rail's lowest point is 71 mm above the scalp at X +35. Only tips, paddles, boot and knuckle plate are inside the 30 mm zone.</text>
</svg>

### B.5 Guards and hair safety

| Guard | Covers | Geometry |
|---|---|---|
| G1 knuckle plate (P30) | everything inside the hand | spherical underside R 90, all faces drafted ≥ 15°, perimeter edge R 3, slot edge R 1.5 with 15° lead-in, ≥ 4.5 mm to every outer paddle and 6.0 mm to the centre paddle |
| G2 servo guard cap (P17) | horn, cradle, cheek A root | smooth PETG shell 2 mm thick under the cradle and around the horn, 15° drafted sides, R 3 edges; cheek A passes its inner edge with ≥ 10 mm all round through ±32° |
| G3 idler guard cap (P18) | bearing, shoulder screw, cheek B root | mirror of G2 |
| G4 rail shroud (P22) | lower 40 mm of rail, down-stop block, carriage at the down-stop | U-channel fixed to the mast, closed bottom, 2 mm walls, drafted 10° outside; the riser leaves through a 25 mm wide slot ≥ 10 mm clear on both sides |

The servo and idler sit at |Y| ≥ 101 mm, 75 mm or more above the scalp at that Y on an R 90 head, and the rail's lowest point is 71 mm above the scalp at X +35, all outside the 30 mm hair-exclusion zone for 2–8 cm hair. The only parts inside it are tips, paddles, the boot and the knuckle plate. No guard has a gap between 0.04 and 3 mm to anything that moves; the one static seam near hair (palm lid to tray, Z ≥ 48) is lapped and taped. **Long hair (> 15 cm) is excluded from SP1 sessions** (K5.2: nothing longer than 15 cm hangs toward the elbow or rail) because hair reach then exceeds the guard distances; the L8.5 wrap test with the long wig is the screen.

Gap table (adjacent nails unless stated; worst case = every combination of 0–5 mm on each leaf with the roll pre-tilt):

| Gap | Static, free state | Worst case | Rule |
|---|---|---|---|
| Tip edges, W (8 mm wide) | 16.0 mm | 8.4 mm | ≥ 8 mm (H-4.6), ≥ 3 mm (freeze §1.4) |
| Tip edges, B45-12 (12 mm wide) | 12.0 mm | 4.4 mm (6.2 mm in normal use) | ≥ 3 mm |
| Seam sleeves (10.3 mm band) | 13.7 mm | 7.1 mm | ≥ 3 mm |
| Paddles at the knuckle plate (17.8 mm sections) | 6.2 mm | 4.2 mm (tip lead's model: 4.5–4.7 mm) | ≥ 3 mm |
| Paddle to slot edge, outer / centre | 4.5 / 6.0 mm | 3.4 / 3.4 mm | ≥ 3 mm |
| Paddle root blocks (inside the palm) | 10.0 mm | 8.6 mm | enclosed |
| C leaf over L paddle (inside the palm) | 3.2 mm | 1.8 mm | enclosed, above the boot |

### B.6 Safety architecture (mechanical)

| Hazard | Primary mechanical barrier | Number |
|---|---|---|
| Excessive normal force | dead weight on a free float; leaf hard stops at 5 mm; stop structure proofed to 7.5 N | W ≤ 1.5 N total while the float is free; 0.6–0.9 N per nail at the leaf stop. **D10 residual:** if the float is jammed on its up-stop (head rise > 24 mm with the button held) force can rise to the frame yield, 8–11 N total at the nails. Procedural cover: hold-to-run release; bench test L5 plus the deliberate float-jam test. The Safety Gate rules on D10. |
| Excessive tangential force / hair tuft load | magnetic wrist breakaway | 1.9–2.1 N at the nails (≥ 5 N straight down); servo goal current ≈ 1.2 N, Current Limit ≈ 1.9 N |
| Element held on the scalp after power loss, e-stop, watchdog or stall | magnet on the actuator rail only; two springs; one spring alone must lift (L5 redundancy) | nails rise 32.9 mm in ≤ 0.14 s (requirement ≥ 25 mm in ≤ 0.5 s) |
| Hair entanglement | sealed seams, drafted paddles, bonded membrane, guards, rotation ≥ 75 mm from the scalp | no gap 0.04–3 mm within 25 mm of hair; wig-head gate L8 |
| Sharp edges | tip radius ≥ 0.4 mm (A45 R 0.3 gated), tape test L9; structure edges R ≥ 1 mm (plate R 3) | UL 1439-style tape test at 2.4 N (tips) and 5 N (structure) |
| Pinch / runaway | mechanical stops ±32° at the elbow, hinge up-stop; firmware ±25°/servo ±28° | tip speed ≤ 0.36 m/s (cap 0.4); float KE ≈ 10 mJ (≤ 50 mJ) |
| Falling hand | 25 mm tether | a released hand drops ≤ 25 mm and stays above the head |
| Face / eyes | hand ~100 mm behind the hairline on the crown; for CROSS aims the idler side (+Y) faces forward so guard G3 is between cheek B and the eyes; nothing moving within 25 mm of the ear canals | red line 6 |

---

## C. DIMENSIONS SUFFICIENT TO FABRICATE

### C.1 Top-level dimension stack (global frame; Z and X in mm; module latched, arm at 0°, float on its down-stop, leaves unloaded)

| Level | Item | X | Z | Notes |
|---|---|---|---|---|
| 1 | Monitor-arm VESA plate (vertical, facing +X), ballast stack between it and the adapter | −139 to −126 | 72.5–147.5 (VESA 75 holes centred at 110) | 4 × M4 × 50 |
| 2 | VESA adapter plate P1 (printed) | −126 to −120 | 25–170 | carries hinge ears (to X −60), magnet arm, pulleys, electronics tray |
| 3 | Spring pulleys (2, at Y ±60) on the adapter top edge; springs hang down its rear face | −123 | 148 | cords run forward, horizontal, to the post |
| 4 | Fail-safe hinge pin (M6, along Y, ears at Y ±30) | −60 | 84 | 60 mm behind the elbow axis, level with it |
| 5 | Electromagnet face (P20/15, facing +X) / keeper on the keeper lever | −66 | 34 | r_m = 50 mm below the hinge |
| 6 | Module frame post (2020, vertical) | −70 to −50 | 92–196 | cord bar at Z 148 (p = 64 mm above the hinge). Length 104 mm (addendum D8) [CONFLICT: CAD generator 122 mm, Z 94–216; see Appendix 1 note 1] |
| 7 | Module frame spine (2020, horizontal, bracketed to the post's front face) | −50 to −15 | 196–216 | reset tab at its front end |
| 8 | Yaw joint plates, 70 × 70 (frame side / carrier side) | −60 to +10, axis −25 | 190–196 / 184–190 | 40 × 40 M3 pattern + 45° holes |
| 9 | Elbow carrier beam (2020, along Y, 270 mm) | −35 to −15 | 164–184 | drop legs at Y ±115 to ±135 come down to the axis |
| 10 | Elbow axis: XL330 horn (−Y side) and idler shaft (+Y side) | 0 | 84 | servo body Z 74–108 [VERIFY axis 10 mm from body end] |
| 11 | Yoke crossbar (moves with the arm) | +45 to +57 | 80–96 | Y −98 to +98 |
| 12 | Rail mast and MGN9 rail, 100 mm | mast +40 to +45; rail top face +33.5 | rail 68–168, mast top an arc R 90 about the elbow axis | carriage face at X +30 |
| 13 | Float down-stop thumbscrew tip / up-stop | +29 | 69 / 69 + 28 | sets L_max 82–88 (e = 2–8 mm) |
| 14 | Carriage (MGN9C) at the down-stop | +30 to +40 | 74–103 | riser (L-bracket) X +27 to +30 |
| 15 | Weight post top / upper wrist seat | 0 | 108 / 69–74 | M8 slugs on a Ø 8 post |
| 16 | Wrist seat plane (keyed magnetic seat) | 0 | 69 | h = 69 mm to the centre edge |
| 17 | Palm lid top | −26 to +26 | 66 | palm 52 × 169 × 33 overall |
| 18 | Centre leaf floor (level 1) / outer leaf floors (level 0) | 0 / ∓8 | 53.0 / 40.4 | leaves along Y |
| 19 | Knuckle plate underside (spherical, R 90) | | 37.5 at centre, 33.9 at outer nails | 25.0 mm above each pocket mouth |
| 20 | Pocket mouths (TM1) | | 12.5 / 8.9 | |
| 21 | Nail edges: centre / left and right | 0 / −8, +8 | 0 / −3.6 | outer nails at Y −24, +24 |
| 22 | Scalp apex (contact) | 0 | +4 | |

**Plan layout.** The hand is centred on Y = 0 under nothing fixed. XL330 at Y −101 to −127 with its horn facing +Y; idler bearing at Y +101 to +111; yoke cheeks at Y ±93 to ±98; crossbar X +45 to +57; palm Y −88 to +81; the fixed frame is behind (X ≤ −15) and above (Z ≥ 130) everything that swings or floats.

**Swept-volume checks (the CAD must confirm ≥ 8 mm clearance at each; the frame CAD generator runs them):** (a) palm rear-top corner (X −26, Z 66) at ±28° reaches X −31, Z 80, Z 112 at the float up-stop: 52 mm under the carrier beam (Z 164); (b) weight-post top (Z 108, 136 at the up-stop) swings to X −24, Z 130 at ±28°: 34 mm under the beam; (c) every arm-mounted point lies within R 91 of the elbow axis above the axis, so nothing on the arm rises above Z 175; the yaw plates start at Z 184: 9 mm; (d) palm ends (Y +81, −88) vs cheek inner faces at |Y| 93: 5 and 12 mm sliding gap, 70 mm or more above the scalp; (e) during the fail-safe lift at the 25° up-stop the post top (Z 196) moves back 47 mm to X −107, 13 mm short of the adapter front face (X −120); the keeper lever bottom moves forward 19 mm, away from the magnet.

### C.2 Lift-off and contact-chord table (H = 80, R = 90)

The freeze formula d(θ) = (H + R) cos θ − √(R² − (H + R)² sin² θ) gives the distance from the axis to the sphere along the arm; d − H is the gap for a tip at L = 80 (freeze figures). The real free tip sits at L_max = 84, so its clearance along the ray is d − 84 (addendum D12). The "vertical clearance" column is what a ruler next to the free centre tip reads at e = 4; the last two columns are the outer nails, which lead or trail by ±8 mm in X (pairs read "at −θ / at +θ").

| θ | d − H (freeze) | d − 84 (free centre tip, along the arm) | Vertical clearance, centre | Left nail (−8, −24) | Right nail (+8, +24) |
|---|---|---|---|---|---|
| 0° | 0.0 | −4.0 (4 mm engagement) | −4.0 | −4.0 | −4.0 |
| ±10° | 2.4 | −1.6 | | | |
| ±13° | 4.2 | +0.2 | +0.2 | +4.2 / −3.1 | −3.1 / +4.2 |
| ±18° | 8.6 | 4.6 | 3.9 | +9.6 / −0.3 | −0.3 / +9.6 |
| ±22° | 14.0 | 10.0 | 7.8 | +14.9 / 2.8 | 2.8 / +14.9 |
| ±25° | 19.9 | 15.9 | 11.2 | +19.4 / 5.7 | 5.7 / +19.4 |
| ±28° | 28.5 | 24.5 | 14.9 | +24.3 / 9.1 | 9.1 / +24.3 |

All three nails are clear of the sphere by ±22°; the trailing outer nail is the last to leave, 5.7 mm clear at ±25° (L4 asks ≥ 5 mm) and **9.1 mm at ±28° (K2.13 amended to ≥ 9 mm for the outer nails, addendum ruling 6; the centre nail ≥ 10 mm)**. Reversals always happen beyond ±18°, where every nail is clear. Mechanical bumpers at ±32°: centre tip 19 mm clear, nothing on the arm meets the frame.

**Contact chord by engagement** (contact lasts while the sphere is above the free tip; the outer nails' windows are shifted ±5.2° ≈ ±8 mm, so the hand lands and leaves one nail at a time):

| e (geometric engagement, apex gauge) | Half-angle | Chord per nail | Protocol target (L4, ±5 mm) |
|---|---|---|---|
| 2 mm | 9.0° | 26.2 mm | 25 |
| 4 mm (default) | 12.75° | 37.4 mm | 36 |
| 6 mm (candidate default, addendum ruling 4) | 15.7° | 46.1 mm | 44 |
| 8 mm | 18.3° | 53.6 mm | — |

**Where the dead weight is in charge.** The leaves are in series with the float: near the chord ends the carriage sits on its down-stop and force is set by leaf compression, falling smoothly to zero; the float lifts off its stop (force = W) only where the sphere is more than δ = W/Σk (Σk = 0.45 N/mm) above the free tip. Chord over which the force equals W:

| e | W 0.6 N | W1 0.88 N | W2 1.18 N | W3 1.47 N |
|---|---|---|---|---|
| 2 mm | 15 mm | 0 (never floats) | 0 | 0 |
| 4 mm | 31 mm | 27 mm | 22 mm | 16 mm |
| 6 mm | 41 mm | 38 mm | 35 mm | 32 mm |
| 8 mm | 50 mm | 47 mm | 45 mm | 42 mm |

**Engagement E is geometric engagement** (down-stop position relative to the scalp apex, set with the apex gauge P43 and read on the rail scale); the pointer at mid-stroke reads e − δ, not e (1.4 mm at E4/W2). E4 stays the default for the first sessions; **E6 is added to the matrix as a candidate default if the dead weight does not float at E4** (addendum ruling 4). At E2 with W1 or more the float never leaves its stop and the force is a leaf constant (≤ 0.9 N, still capped).

**Force variation along the stroke from rail inclination:** N = W cos θ / (1 ∓ µ sin θ) → 0.92–1.08 W at ±7°, 0.84–1.16 W at ±13° for µ = 0.7; beyond about ±7–15° the float is on its stop anyway. Float inertia adds about 3 % at 2 Hz.

### C.3 Hand layout and leaves

| Nail | Edge (X, Y) at mid-stroke | Free edge Z (down-stop) | Leaf rate | Share of W | Leaf runs from paddle toward | Leaf level (floor Z) | Cut length | a (bar edge to bar edge) | Free length face to face | Root floor Z | Root pre-tilt β |
|---|---|---|---|---|---|---|---|---|---|---|---|
| L (left) | (−8, −24) | −3.6 | 0.12 N/mm | 0.8 × W/3 | −Y (root outboard) | 0 (40.4) | 70 mm | 48.3 mm | 42.3 mm | 44.1 | 4.4° |
| C (centre) | (0, 0) | 0 | 0.15 N/mm | 1.0 × W/3 | −Y, crossing over L | 1 (53.0) | 67 mm | 44.5 mm | 38.5 mm | 56.7 | 4.7° |
| R (right) | (+8, +24) | −3.6 | 0.18 N/mm | 1.2 × W/3 | +Y (root outboard) | 0 (40.4) | 64 mm | 41.7 mm | 35.7 mm | 44.0 | 5.0° |

Leaf stiffness uses the clamp-corrected formula k = EI / (a³/3 + a²b + ab²) with EI = 200 GPa × (12.7 × 0.3³/12) = 5715 N·mm², a = flexible length from root bar edge to paddle bar edge (face-to-face free length + 6 mm, because the leaf flexes 3 mm inside each wall slot), b = 4 mm (tip beyond the paddle bar edge). The naive 3EI/L³ overstates k by 1.9–2.1× at these lengths. Trimming 1 mm of free length changes k by 6–7 %; ±0.005 mm of stock thickness is ±5 %.

| Setting | δ = W/Σk | L | C | R | Heaviest / lightest |
|---|---|---|---|---|---|
| 0.6 N (trim cord) | 1.33 mm | 0.16 N | 0.20 N | 0.24 N | 1.5 |
| W1 0.88 N | 1.96 mm | 0.24 N | 0.29 N | 0.35 N | 1.5 |
| W2 1.18 N | 2.62 mm | 0.31 N | 0.39 N | 0.47 N | 1.5 |
| W3 1.47 N | 3.27 mm | 0.39 N | 0.49 N | 0.59 N | 1.5 |

Hard stop at 5.0 mm of tip travel (D5): force on the leaf at the stop L 0.60 N, C 0.75 N, R 0.90 N (all ≤ 2.4 N). Leaf stress 88–115 MPa nominal, 165–216 MPa at the stop, against hardened feeler stock yielding at 1.2–1.5 GPa (infinite life once corners are rounded R 1 and edges stoned). Torsion under 0.3 N drag: 3.6–4.2° outer, 4.6° centre (2.8–4.3 mm of edge motion in X). Paddle roll under leaf bending: 1.63 / 1.76 / 1.87° per mm of tip travel (L, C, R).

**Knuckle-plate slot:** union of three R 4-cornered rectangles, 31.8 × 26.8 at (−8, −24) and (+8, +24) and 34.8 × 29.8 at (0, 0); overall 47.8 × 74.8 mm. Paddle section at the plate 22.8 (X) × 17.8 (Y) with 10° draft on all faces. **Boot:** 0.25 mm Shore 40A silicone cut with template P35: 8 mm flange outside the slot, three holes at 70 % of the paddle section (stretched 40 % over the paddle at z 26–28, bonded with a 2 mm Sil-Poxy bead), sheet between paddles and slot cut 40 % longer than the span so it lies in a loose fold (coupling < 0.002 N/mm [EST]).

### C.4 Hinge, springs, magnet

| Quantity | Value |
|---|---|
| Moving module mass (everything on the hinge, float included, no slug) | 733 g (post 36, spine 36, carrier beam 130, drop legs 70, servo + cradle 41, idler 33, yoke cheeks 30, crossbar 45, mast/rail/stops 64, shroud 15, float 92, hinge knuckle 20, keeper lever 25, yaw plates 30, brackets 30, guards 16, cables 10, misc 10) |
| Fixed parts on the adapter | about 260 g (adapter 120, magnet 30, springs/cords/pulleys 25, tray + OpenRB + terminal 70, fasteners 15) |
| Module CoG (no slug) | X −10.7, Z 106: 49.3 mm in front of the hinge; gravity moment 0.355 N·m (0.390 with +60 g, 0.414 with +100 g) |
| Moment of inertia about the hinge | 3.5–3.9 × 10⁻³ kg·m² (+0.5 × 10⁻³ allowance) |
| Springs (each of two) | rate 0.095 N/mm [MECH CHOICE: 0.08–0.11], initial tension 1.5 N [1.0–2.0], free length inside hooks 64 mm [55–70], OD 9.5 mm, 0.8 mm music wire, zinc plated, machine hooks; working extension 53 mm (117 mm hook to hook) at **6.5 N**; at the 25° up-stop 26.8 mm shorter, 3.9 N; max extended length ≥ 125 mm; max load ≥ 10 N |
| Spring moment, latched | 2 × 6.5 N × 0.064 m = 0.832 N·m; net lift held by the magnet 0.477 N·m (no slug), 0.442 (+60 g), 0.418 (+100 g); at the up-stop net +0.185 / +0.152 / +0.130 N·m: stays up with any slug |
| Magnet load at the keeper (r_m = 50 mm) | static 9.5 N (no slug) / 8.4 N (+100 g); + nails resting (W ≤ 1.5 N at 60 mm) 1.8 N; + servo reaction at 450 mA (0.16 N·m) 3.2 N: **14.5 N worst case running** |
| Magnet available | 25 N × 0.9 (tape gap) × 0.85 (coil warm) = 19 N; 22.5 N cold; margin 1.3 running, 2.0 static. Fallback: Adafruit 3873 P25/20 (50 N) on a Ø 25 seat |
| Frame overload yield (float jammed on its up-stop) | push × 60 mm + 0.477 N·m > F_hold × 50 mm → **8–11 N total at the nails** (D10) |
| Fail-safe lift timing (integrated) | nail centre up 25 mm at 80 / 85 / 89 ms (no slug / +60 / +100 g); reaches the 25° stop at 91 / 97 / 102 ms at 0.85 / 0.78 / 0.74 m/s; + 30 ms release allowance: ≤ 0.14 s vs the 0.5 s requirement |
| Lift geometry | nails rise 32.9 mm and move 28.2 mm forward (+X, away from the hinge); clearance above the scalp at the stop 33.4 mm at e = 4, 29.4 mm at e = 8 |
| Under-voltage | frame lifts statically below about 3.3–3.5 V, while stroking below about 4.0 V; the XL330 runs from 3.7 V. **Firmware rail-sense treats < 4.0 V as rail-dead and torques off** (addendum ruling 7) |
| Up-stop | M4 × 25 with a Ø 10 × 6 rubber cap, strikes the post rear face 20 mm above the hinge at 25° [adjustable 22–27°] |
| Down-stop (working position) | keeper on the taped magnet face; M3 washers under the magnet's rear screw: each 0.5 mm moves the frame 0.57° and the nails 0.6 mm |
| Monitor-arm clamp moment | 2.1 kg × 9.81 × 0.45 m = 9.3 N·m + the arm's own 5–7 N·m: about a third of a 2–9 kg arm's design; desk ≥ 18 mm solid, no glass |

### C.5 Wrist seat and breakaway

| Feature | Lower seat (hand side, in P33) | Upper seat (carriage side, P28) |
|---|---|---|
| Contact land | flat ring Ø 40 outer / Ø 30 inner, top at Z 69 | matching flat face, Ø 44 × 5 plate (Z 69–74) |
| Centring | 45° cone boss Ø 18 base / Ø 12 top, 3.0 tall | conical recess Ø 18.4 / 12.4, 3.1 deep |
| Magnetic pair | 12 × 1.5 mm mild-steel keeper disc bonded flush in the cone top | K&J D61 (3/8 × 1/16 in N42, 9.4 N rated) bonded flush in the recess floor, one layer of 0.05 mm tape over it |
| Orientation key | Ø 3 peg, hemispherical end, 2 tall, at r 17 on +X | radial slot 3.3 wide × 2.2 deep |

Breakaway: F_t × h = s × (F_m + W_upper) with s = 20 mm (ring edge), h = 70 mm (nail height below the seat), F_m = 6.5 N design (5.5–7.5 N estimated, measured in L6):

| Float setting | W_upper | F_t at breakaway (at the nails) |
|---|---|---|
| W1 (no slug) | 0.29 N | 1.94 N |
| W2 (+30 g) | 0.59 N | 2.03 N |
| W3 (+60 g) | 0.88 N | 2.11 N |
| hand lifted, hanging | | 1.69 N |

Same in every tangential direction (circular ring). Straight-down release at about 5.9 N. At the knuckle plate (31.5 mm below the seat) the same seat lets go at 4.3–4.7 N, which is why **L6(a) pulls at nail height with the P46 clip** (addendum ruling 2). Tuning: each 0.05 mm tape layer lowers F_m about 10 % [EST]; a second D61 stacked raises it about 40 % [EST].

### C.6 Bare floating weight ledger (budget ≤ 92 g = 0.90 N)

| Item | Mass |
|---|---|
| MGN9C block, seals off | 16.0 g |
| Riser P26 with pointer and trim hook (PETG) | 5.0 g |
| 4 × M3 × 6 steel screws (riser to block) | 1.6 g |
| Upper wrist seat P28 with weight post and load-cell slot (PETG) | 4.5 g |
| Seat magnet K&J D61 | 0.9 g |
| Weight cap P29 with M3 × 8 nylon thumbscrew | 1.0 g |
| 2 × M3 × 8 aluminium screws (riser arm to seat) | 0.4 g |
| Tether cord (25 mm loop) | 0.2 g |
| **Carriage side subtotal** | **29.6 g** |
| Palm lid P33 with lower seat cone and keeper (PETG + 12 × 1.5 steel disc) | 7.3 g |
| Palm tray P32 with root blocks and stop beams | 9.0 g |
| Knuckle plate P30 | 4.0 g |
| Silicone boot and its clamp frame P31 | 2.0 g |
| 3 leaves, 0.3 × 12.7, 70 / 67 / 64 mm | 6.0 g |
| 3 root clamp bars P34, 6 × M2 × 6 steel screws, 6 M2 inserts | 2.2 g |
| 3 nylon M3 stop screws, 3 M3 inserts | 1.1 g |
| 6 × M2 × 6 lid screws, 6 M2 inserts | 1.2 g |
| 3 paddles (2 perimeters, 10 % gyroid; outer 5.0 g each, centre with riser 6.5 g) | 16.5 g |
| 3 paddle clamp bars T3, 6 × M3 × 8 aluminium screws | 3.3 g |
| 3 TM1 magnets (N52 6 × 2) and 3 TPU seam sleeves | 2.5 g |
| 3 tips type W | 5.4 g |
| **Hand subtotal** | **60.5 g** |
| **Bare floating mass W1** | **90.1 g = 0.884 N** |

The margin is 2 g, inside print-to-print scatter: weigh every subassembly before final assembly. Over 92 g: (1) swap the remaining steel screws for aluminium (−1.5 g); (2) fit the trim cord set to bring W1 to 0.90 ± 0.05 N; (3) last resort, MGN7C on an MGN7 rail (−6 g, reprint P21 mast and P26). Under 90 g: add M3 washers (0.12 g each) under the weight cap so W1 = 0.90 N exactly. Slug sets: DIN 9021 M8 washers (8.4 × 24 × 2, about 6.2 g): **+30 g = 5 washers** trimmed to 30.0 ± 0.5 g with taped M3 washers, yellow tape; **+60 g = 10 washers**, red tape; the post takes up to 16 (100 g). W2 = 1.18 N and W3 = 1.47 N with the 90.1 g float; trim with M3 washers to 1.20 / 1.50 ± 0.05 N. Moving float mass at W3 ≈ 150 g (K2.16 limit 160 g); KE at 0.36 m/s ≈ 10 mJ (safety §2.4 carriage limit 50 mJ).

### C.7 Face cradle and posture

| | SEAT (primary, crown) | PRONE (occiput default, fallback for neck discomfort) |
|---|---|---|
| Support | tabletop massage face cradle (horseshoe pad about 280 × 220, adjustable tilt) on its own stand | portable face-cradle cushion (horseshoe foam, about 300 × 250 × 100) on the bed |
| Head attitude | flexed 30–45° for the crown so the scalp normal at the target is vertical | face down; gravity along the occipital normal (the posture the dead weight is designed for) |
| Arm mount | desk clamp, arm reaching over from behind or the side | nightstand clamp (top ≥ 18 mm solid) or a floor-stand monitor pole within 500 mm of the occiput |
| Head motion the float absorbs | ±5–10 mm | 5–15 mm breathing drift, inside the 24 mm free up-travel |
| Forehead pressure | 15 N over about 60 cm² ≈ 2.5 kPa (limit 5 kPa sustained) | similar |

Setup aids: tilt wedges P42 (15°, under the cradle's front feet); apex height gauge P43 (12 mm stick, rings at 80/82/84/86/88 mm from the foot: with the module latched, arm at 0°, nails free, stand it on the target point and raise or lower the arm until the 80 mm ring is level with the elbow-axis mark scribed on cheek A, so H = 80 and e = L_max − 80). Clearances: on the crown the hand is about 100 mm behind the hairline; for CROSS aims turn the module so the idler side (+Y) faces forward; ear canals are about 120 mm below the crown plane, the hand ends at |Y| ≤ 88 at Z ≥ 38 above it.

---

## D. COMPONENT SELECTION

Every bought part, with the reason it was chosen and what it must do. Quantities, prices and vendors are in §E.

### D.1 Actuator and controller (Stack A)

| Component | Selection | Why |
|---|---|---|
| Stroke servo | **Dynamixel XL330-M288-T** (5 V, 3.7–6.0 V, 0.52 N·m stall at 1.47 A, K_t ≈ 0.354 N·m/A, 18 g, 4096 ticks/rev, protocol 2.0, ID 1) | current-based position mode (operating mode 5) gives position goals under a hard servo-side current ceiling (Goal Current 300 mA ≈ 1.26 N at the tip, Current Limit 450 mA ≈ 1.9 N), EEPROM position limits ±28°, a Bus Watchdog register, readable present current, 50 Hz bus loop at 1 Mbps. Required torque 1.2 N × 0.084 m = 0.10 N·m, a fifth of stall. Substitute XL330-M077-T (0.22 N·m) with goal current re-derived |
| Controller | **OpenRB-150** (SAMD21G18A, 4 DXL TTL ports, FET-switched DXL power, USB-C, screw terminal for VIN) | the servo-bus supply (Terminal VIN with the jumper on **VIN(DXL)**) is physically separate from USB logic power and is FET-gated by firmware (off at every reset), so a watchdog reset makes the servo limp; SAMD21 hardware WDT; 7 ADC pins; Arduino toolchain. The `USB(5V)` jumper position is forbidden (it would put the servo on the laptop side of the safety loop) |
| Stage-3 yaw servo | second XL330-M288-T, ID 2, on a 100 mm lazy-Susan ring under the yaw plates | a 270 mm, 0.5 kg carrier on one horn repeats the side-load problem; the bearing carries it |
| Stage-3 load cell | 5 kg bar cell + HX711 on D2/D3 (40 × 12 mm slot in the wrist) [verify a 40 mm 5 kg cell exists] | a 1 kg cell is destroyed by a 20 N push |

### D.2 Power and safety loop

| Component | Selection | Why |
|---|---|---|
| Brick | **Adafruit 1466**, 5 V 4 A, UL-listed, 100–240 V in, 5.5 × 2.1 mm centre-positive, 20 W | certified external adapter, regulated 5 V, no mains on the rig; with 22 AWG rail wire keeps the drop under 0.2 V at 0.6 A (addendum ruling 7). Alternative Mean Well GST25A05 [verify] |
| Fuse | 1 A fast-blow 5 × 20 (F1AL250V) in an inline screw holder at the adapter | running rail current ≈ 0.6 A (servo ≤ 0.30 + magnet 0.22 + board 0.05); a servo that has lost its limits stalls at 1.47 A and opens it; the brick's ≈ 4 A OCP is the absolute ceiling. 1.25 A fast is the only permitted step-up if it nuisance-trips |
| E-stop | **TWTADE YW1B-V4E02R boxed**, 22 mm NC mushroom, latching push-lock / twist-release, 10 A, on a steel plate (weighted base) on the desk | red line 4: NC hardware contact in series with motor power, under the free hand. Panel-mount alternative APIELE 1NC LA139A-ES542 in a printed box |
| Hold-to-run | **uxcell 30 mm momentary arcade button** (N.O. microswitch, 3 A) in the printed handle P39/P40 (Ø 36 × 110, button face 3 mm below a 36 mm rim so nothing flat can hold it), 1.5 m 2-core 22 AWG cable with a gland and zip-tie anchor | the dead-man: the thumb holds it; releasing kills servo power and the magnet. Bought alternative Philmore 30-825 (extend its cord to 1.5 m). No cheap handheld switch is proof against a deliberately inserted wedge; the §M rule (never taped, tied, latched, wedged) stands |
| Holding electromagnet | **Adafruit 3872 P20/15**, 5 V, 0.22 A, 25 N on thick steel, Ø 20 × 15, M3 rear thread, 270 mm leads; 1N5819 Schottky flyback across the coil (band to +) | holds the frame down only while the rail is live; 19 N warm vs 14.5 N worst-case load. Fallback Adafruit 3873 P25/20 (50 N) on a Ø 25 seat |
| Rail protection | 470 µF 10 V electrolytic + SMAJ5.0A TVS across the OpenRB terminal; rail-sense divider 10 k/10 k + 100 nF to A2 (read-only) | clamps reversed or spiked input; no series diode (it would drop the bus toward the XL330's 3.7 V floor) |
| Wire | 22 AWG silicone (rail), 26 AWG (signals), 6-core 26 AWG (panel), braided sleeve on the DXL cable across the hinge, Wago 221-413 rail node in a printed cover, Dupont for the panel, crimp forks/spades at the e-stop and microswitch | safety §2.8: ≥ 22 AWG for motor runs ≤ 1.5 A; no bare terminals |
| DXL cable | ROBOTIS X3P (JST-EH 3-pin) **340 mm or longer** [verify available; else crimp one] | tray → adapter → hinge (60 mm service loop) → carrier beam → −Y drop leg → servo is about 330 mm; the stock 180 mm cable is too short |
| Panel | 2 × 10 kΩ linear pots with knobs (SPEED, VARIATION), SPST toggle (PERIODIC/HUMAN), 5 mm LED + 330 Ω, in the printed box P37/P38 with 0/50/100 % tick recesses | the three experiment inputs, 1 m from the tray so the panel sits on the desk |

### D.3 Motion, structure and compliance hardware

| Component | Selection | Why |
|---|---|---|
| Linear float | **MGN9 rail 100 mm + MGN9C block** (16 g), seals and wipers removed, one drop of light oil [verify hole pitch 20 mm / 10 mm ends and the block's 15 × 10 M3 pattern] | N = W for any µ; rolling friction 0.01–0.03 N (seals would add 0.1–0.3 N); MGN9H (26 g) allowed only if the scale shows margin; MGN7C is the −6 g fallback |
| Lift springs | 2 (+2 spare) extension springs, 3/8 in OD, 0.031 in music wire, 2.5 in inside hooks, 0.54 lbf/in, IT 1.0–2.0 N, max load ≥ 10 N, max extended ≥ 5 in; **McMaster 9654K family, suffix [verify]**, or any 3/8 in spring that passes the luggage-scale test (6.5 ± 0.5 N at 117 mm, 3.9 ± 0.5 N at 90 mm) | two in parallel: one alone must still lift the module (L5 redundancy) |
| Cords | 1.0 mm braided UHMWPE (Dyneema), about 45 kg break, 3 m: two hinge cords, the reset cord, the 25 mm wrist tether | keeps the spring line of pull horizontal over the pulleys (constant 64 mm lever) |
| Pulleys / idler bearings | 2 × 623ZZ (3 × 10 × 4) in printed sheaves P2 on M3 × 16 + nyloc; 1 × 625-2RS (5 × 16 × 5) pressed into P15 | bearing pulleys so the lift is not slowed by friction; sealed idler |
| Idler shoulder screw | Ø 5 × 25 mm shoulder, M4 × 6 thread, alloy steel, M4 nyloc [verify part number] | fixed in cheek B; the bearing in the fixed housing |
| Hinge pin | M6 × 80 socket head (smooth shank in the Ø 6.3 bores), M6 nyloc, 2 × 0.5 mm nylon/PTFE washers | free rotation, no play |
| Frame | 2020 aluminium extrusion (one 4 × 500 mm pack: 270 + 104 + 80 mm) with M5 drop-in T-nuts, M5 × 10 screws and 2 corner brackets | the 270 mm beam is longer than most print beds and must stay straight to ±0.3 mm; extrusion does not creep under the permanent 13 N spring + 14.5 N magnet + 8 N weight preload; T-slots give free alignment |
| Keeper | 25 × 25 × 3 mm mild steel (cut from 1/8 × 1 in flat bar), flattened on 400 grit on glass | full flux return needs ≥ 3 mm and ≥ Ø 20 |
| Magnet-face tape | 0.075 mm PTFE thread-seal tape, one layer | stops residual magnetism holding the keeper after power is cut |
| Wrist magnet | **K&J D61** (3/8 × 1/16 in N42, 9.4 N rated) + 12 × 1.5 mm mild-steel keeper disc [verify thickness] + 0.05 mm PTFE film tape | sets the ~2 N tangential breakaway; tuned by tape layers or stacking |
| Leaves | 0.30 × 12.7 × 305 mm spring-steel feeler stock (0.012 × 1/2 × 12 in), Precision Brand or McMaster [verify part number]; 2 strips for the rig (1 spare) + 2 for the wand | hardened stock: 0.12–0.18 N/mm at 36–42 mm free length, infinite life at the 5 mm stop; the same part number on the wand and the rig so wand results transfer |
| Slugs | DIN 9021 M8 washers 8.4 × 24 × 2 (about 6.2 g), 20 | +30 g and +60 g sets on the Ø 8 post, captured by the cap |
| Boot | 0.25 mm Shore 40A silicone sheet about 150 × 150 (makes 4) [verify] + Smooth-On Sil-Poxy | one slack membrane bonded to the paddles: no sliding seal, no friction |
| Seam tape | 0.05 mm PTFE film tape (3M 5490 class) [verify thickness] | palm lid-to-tray seam; over the D61 |
| Bumpers / feet | self-adhesive Ø 10 × 6 rubber bumpers (up-stop cap, panel feet); Ø 30 × 15 rubber or Sorbothane feet in cups P41 if the cradle shares the desk | |
| Thumbscrews | 3 × M3 × 16 knurled stainless (down-stop with jam nut, trim cleat, scale lock); nylon M3 × 8 thumbscrew (weight cap); 3 × nylon M3 × 10 (leaf stops) | tool-free settings; nylon stop screws bear on the leaf without marking it |
| Ballast | 5 × 3 mm mild-steel plates 100 × 100, 4 × Ø 4.5 on 75 × 75 (235 g each), laser cut (SendCutSend) or steel VESA extension plates | only if the arm's minimum load is above the 1.1 kg module |
| Monitor arm | HUANUO / VIVO class single gas-spring arm, VESA 75/100, minimum load ≤ 2.0 kg (ideally ≤ 1.0 kg), reach ≥ 400 mm, tilt ≥ ±45°, swivel ≥ ±90°, lockable rotation, clamp 10–85 mm [verify the listing] | a mic boom arm is not stiff enough for 1.1 kg |
| Face cradle | tabletop massage face cradle on its own stand with tilt (SEAT) [verify]; horseshoe face cushion (PRONE) | |
| Fasteners and inserts | brass heat-set M3 (4.0 hole, 4 long, 55 used), M2 (3.2 hole, 3 long, 18 used), 1 × M4 × 6; socket-head M2/M3/M4/M5 per table 3A; aluminium M3 × 8 for the paddle clamps and riser-to-seat (mass budget); M3 × 6 flat heads for the keeper plate | PETG takes inserts well; aluminium screws save 1.5 g where it counts |

### D.4 Tips, paddles and wand materials

PETG (one bright colour, orange or yellow) for every tip, carrier, paddle and bar; TPU 90A for the seam sleeves and the E pad; nylon 6/6 (Dunlop 0.88 and 1.0 mm picks or sheet) for the A45 and E blades; G25 3.0 mm chrome-steel balls for H; ABS full-cover press-on nails (size 1–2) nested in pairs for P; N52 6 × 2 mm discs (one per pocket, 6 × 3 mm for breakaway tuning); 6 × 1 mm mild-steel discs filed to 3.9 mm flats (or 1 mm sheet slugs) for the tang keepers; thin and gel CA, 5-minute epoxy. PLA is allowed only for the wand handle and never near skin; standard SLA resin is banned at the scalp (red line 9).

### D.5 Tools (beyond what most apartments have)

Arduino IDE 2.x on a laptop; 3D printer with a ≥ 220 × 220 mm bed, direct drive and a 250 °C hotend (or a print service); temperature-controlled soldering iron (Pinecil V2) with M2/M3 heat-set tips; 63/37 solder and flux; multimeter; 0.1 g kitchen scale (500 g); 10 g luggage scale (springs, magnet pull-off, 7.5 N proof, frame yield); 0–5 N spring scale (wrist breakaway); 150 mm calipers; steel ruler; ball-end metric hex keys 1.5–5 mm; M5 tap and handle (carrier-beam ends); 1/4 in and 5.0 mm drill bits (hinge bores, cheek B); mitre box and 32 tpi hacksaw (2020); deburring tool and needle files; sandpaper 220/400 and plastic polish (knuckle plate Ra ≤ 0.8 µm); aviation snips and a fine stone (leaves); flush cutters, wire stripper, small screwdrivers; optional crimp tool and helping hands; phone (240 fps, SPL meter, inclinometer, timer apps); 10× loupe; IR thermometer; hygrometer.

---

## E. BILL OF MATERIALS

One apartment build, US delivery, USD before tax and shipping, as of October 2026. **[cited]** from a project document; **[est]** ±30 %; **[verify]** confirm the part number, size or listing before paying. Web lookups were blocked when the BOM was compiled, so no [est] price was checked against a live cart; where a SKU was uncertain a search string is given. **Stage codes:** S0 Stage-0 hand wand · S1 Stage-1 rig · S3 gated Stage-3 upgrades · BK bench and test kit · T tools you keep. *Optional* rows are left out of every total; *can wait* rows are in the totals but can be bought later.

### E.0 How to order

**E.0.1 Order groups (carts)**

| Order | When | What | Cash (USD) |
|---|---|---|---|
| Cart A, Stage 0 | now | every S0 row (tip rows except 5.04 and 5.09, PETG spool 1, TPU spool), the BK rows marked "buy with S0" (short real-hair head and clamp, loupe, polyester tape, 10 mm rod, carbon paper, cleaning consumables) and the T rows marked "buy with S0" (kitchen scale 0.1 g, calipers, hex keys, aviation snips, cutters set). Plus a printer or print service if you have neither (row 8.01) | **$282.00** (S0 $141.00 + BK $70.00 + T $71.00) |
| Gate | after the Stage-0 build | Stage 0 GO (§M H0): the nail reaches skin through your hair at ≤ 0.5 N, W or B45 beats H by ≥ 3 points blind, no hair capture in 200 wig strokes. Run these before any motorised part is ordered | none |
| Cart B, Stage 1 | the day after GO; all carts the same day | every S1 row, split by vendor in §E.10. Place the Robotis order first (longest lead time). Then the rest of the bench kit (needed before L1–L12) and the rest of the tools (soldering iron and insert tip, multimeter, luggage scale, M5 tap, mitre box and saw) | **$762.50** (S1) + $170.00 (rest of BK) + $156.00 (rest of T) |
| Cart C, Stage 3 | only if Stage-2 feedback earns it | lazy-Susan bearing and load-cell kit. The second XL330 is counted in S3 but belongs in the Stage-1 Robotis cart: it is the spare for the single most critical part and saves a second shipment | **$43.49** |

**E.0.2 What to buy first for Stage 0.** The wand needs tip items 1, 3, 5, 6, 7 and 10 plus screws, glue and abrasives: rows 5.03, 5.05–5.08, 5.10–5.17, PETG spool 1 (4.01) and the TPU spool (4.03, for the wand paddle's seam sleeve). The day-0 tests also need the kitchen scale (practice 0.3 and 0.5 N), the loupe, the 50 µm tape on the 10 mm rod (L9), carbon paper for the loaded-edge mark, and the short real-hair head on its clamp (L8.1 static reach, L8.9 200 strokes per tip).

**E.0.3 What can wait for Stage 3.** Rows 6.33–6.35: second XL330 (yaw, ID 2), lazy-Susan bearing, 5 kg bar load cell with HX711. The 40 × 12 mm wrist slot is bridged by the printed filler P47 until then. Total $43.49, inside the freeze's +$27–45.

**E.0.4 What can wait inside Stage 1** (in the totals, skip in a lean first order):

| Row | Item | Line (USD) | Skip it when |
|---|---|---|---|
| 2.02 | Ballast plates | $45.00 | your arm's printed minimum load is 1.0 kg or less (a light arm) |
| 2.06 | Spare MGN9C block | $8.00 | you accept a few days' downtime if a block loses balls |
| 2.28 | Isolation feet | $10.00 | the face cradle stands on its own stool or table (preferred) |
| 2.31 | Face cradle cushion (PRONE) | $20.00 | until the first OC (occiput) sessions or neck discomfort in SEAT |
| 5.04 | Tip item 4: 6 × 3 mm magnets | $6.00 | L6(b) reads ≥ 4 N on every tip with the 6 × 2 mm magnets |
| 5.09 | Tip item 9: 1.0 mm nylon picks or sheet | $5.00 | until the Stage-2 E tip and B45 slot mode |
| | **Total that can wait** | **$94.00** | |

**E.0.5 Check before ordering.** All [verify] items are in Appendix 2. Three of them change what you click: the spring part number (box 2A), the monitor arm's minimum load (row 2.01), and whether a 340 mm X3P cable exists (row 6.18). Print-test P15, P2, P13 and P34 with a leaf scrap before the rest. P13 (servo cradle) and P16 (horn disc) depend on XL330 drawing dimensions marked [VERIFY]: print those only after the servo has arrived.

### E.1 Totals

**E.1.1 Group × stage (USD, optional rows excluded, shipping excluded)**

| Group | S0 wand | S1 rig | S3 upgrades | BK bench kit | T tools | Total |
|---|---|---|---|---|---|---|
| 2 Structural and mechanical | $0.00 | $359.42 | $0.00 | $0.00 | $0.00 | $359.42 |
| 3 Fasteners and inserts | $0.00 | $110.00 | $0.00 | $0.00 | $0.00 | $110.00 |
| 4 Printing (filament) | $54.00 | $25.00 | $0.00 | $0.00 | $0.00 | $79.00 |
| 5 Tips | $87.00 | $11.00 | $0.00 | $0.00 | $0.00 | $98.00 |
| 6 Electronics | $0.00 | $257.08 | $43.49 | $0.00 | $0.00 | $300.57 |
| 7 Bench and test kit | $0.00 | $0.00 | $0.00 | $240.00 | $0.00 | $240.00 |
| 8 Tools (printer excluded) | $0.00 | $0.00 | $0.00 | $0.00 | $227.00 | $227.00 |
| **Total** | **$141.00** | **$762.50** | **$43.49** | **$240.00** | **$227.00** | **$1,413.99** |

**E.1.2 The three totals Michael asked for**

| Total | What it covers | USD |
|---|---|---|
| **Lean rig** (Stage 0 + Stage 1, minus the six can-wait rows) | the machine, first order | **$809.50** |
| **Full rig** (Stage 0 + Stage 1, everything) | the machine, every row | **$903.50** |
| **Bench kit + tools** (printer excluded) | test gear $240.00 + tools $227.00 | **$467.00** |
| Stage 3 (gated) | yaw servo, bearing, load cell | $43.49 |
| Grand total, all stages, no printer, no shipping | | $1,413.99 |
| Estimated shipping (Adafruit, Robotis, McMaster, K&J) | | $33.00 |
| **Grand total with shipping, without a printer** | | **$1,446.99** |

Not in the table: optional rows $89.95; a 3D printer if you have none (about $300–400 [est], or $150–250 [est] at a print service for 1.1 kg of PETG).

**E.1.3 Against the DECISION and freeze targets**

| Budget line | Target | This BOM (cash from an empty shop) | Comment |
|---|---|---|---|
| Stage 0 wand | about $30 (freeze); about $39 cash if screws, CA, abrasives and a marker are already in the shop (tips) | $141.00 S0, plus $70.00 bench kit and $71.00 tools bought with it | S0 includes two whole filament spools ($54) and full packs of every tip consumable; the wand's marginal parts cost is about $39 |
| Rig (Stage 0 + 1 parts, no bench kit, no tools) | $250–300 (DECISION); about $250 (freeze Stage 1) | $903.50; lean $809.50 | 3.0–3.6× the target in cash. The named major parts (arm, extrusion and brackets, rail, springs, bearings, magnets, brick, e-stop, button, OpenRB-150, XL330, feeler stock, PETG spool 2) add up to **$249.50**, inside the target: the target covers major parts only. The gap is small parts, packs, consumables and spares ($393), the face cradle/cushion/feet/ballast ($120) and the tip set with its filament ($141) |
| Stage 3 | +$27–45 | $43.49 | inside |
| Test gear | $45–70 (component landscape) | $240.00 | the protocol asks for two real-hair heads, a wig, IR thermometer, hygrometer, weights and more |
| Tools | $150–190 from nothing | $227.00 (printer excluded) | adds the luggage scale, M5 tap, mitre box, snips, stone and polish |

**Where to cut if cash matters.** Already-owned stock decides most of the gap: a screw assortment, heat-set inserts, CA, epoxy, wire and an electronics component kit on the shelf remove about $90–130. A light arm instead of ballast removes $45. A starter electronics component kit (about $15–20 [est]) replaces rows 6.19–6.23 and the Dupont kit ($40 together). **Do not cut** the spare springs, the spare fuse, the 340 mm DXL cable with its hinge service loop, or anything on the actuator rail: these are safety items.

### E.2 Structural and mechanical

Monitor-arm rating needed: moving module 733 g + fixed adapter parts about 260 g = 1.0–1.1 kg at the VESA plate, CoG 49 mm in front of the hinge; the arm must hold this at 350–500 mm reach without creeping up; ballast to the arm's printed minimum + 10 % (2–9 kg arm: 1.1 kg, 5 plates; 1–6.5 kg arm: none); clamp moment 9.3 N·m + the arm's own 5–7 N·m; solid desk ≥ 18 mm, not glass; pass = ≤ 2 mm drift in 30 min (K2.14).

| # | Item | Qty | Spec | Unit (USD) | Line (USD) | Source | Substitute | Stage |
|---|---|---|---|---|---|---|---|---|
| 2.01 | Monitor arm | 1 | Single gas-spring arm, VESA 75 and 100; load range minimum ≤ 2.0 kg; reach ≥ 400 mm; VESA centre 300–650 mm above the desk; tilt ≥ ±45°, swivel ≥ ±90°, lockable rotation; desk clamp 10–85 mm with its steel plate | $36.00 [cited] [verify] | $36.00 | HUANUO or VIVO class (component landscape §5.4). Search "single monitor arm gas spring VESA 75 4.4 lbs minimum" [verify the printed minimum load and swivel range] | Light arm (1–6.5 kg, minimum ≤ 1.0 kg): no ballast, saves 2.02. A mic boom arm is not acceptable | S1 |
| 2.02 | Ballast plates | 5 | 3.0 mm mild steel 100 × 100, 4 × Ø 4.5 on 75 × 75, 235 g each; between the arm VESA plate and the adapter, never on the hinged module; remove plates until the arm holds height | $9.00 [est] | $45.00 | SendCutSend laser cut (about $29 minimum order [cited]); upload a 100 × 100 square with 4 holes | Steel VESA extension plates (weigh them) or 1/8 in flat bar cut and drilled; not needed with a light arm | S1, can wait |
| 2.03 | 2020 aluminium extrusion | 1 pack (4 × 500 mm) | European 2020, 6 mm slot; cut 270 (carrier beam), 104 (post) and 80 (spine) from one bar; tap both carrier-beam ends M5 | $28.00 [cited] | $28.00 | Search "2020 aluminum extrusion 500mm 4 pack" | Misumi HFS5-2020 cut to length with tapped ends [verify] | S1 |
| 2.04 | 2020 corner bracket kit | 1 kit (about 40 sets) | Corner brackets with M5 drop-in T-nuts and M5 × 10 screws; the rig uses 2 brackets, about 20 T-nuts, 22 screws | $15.00 [cited] | $15.00 | https://www.amazon.com/Aluminum-Extrusion-Connectors-Hardware-Accessories/dp/B0FF9ZBTZJ | Any 2020 kit with drop-in (hammer) M5 T-nuts | S1 |
| 2.05 | MGN9 rail 100 mm with MGN9C block | 1 kit | MGN9 rail 100 mm, 9 wide, 6.5 tall, M3 counterbored holes at 20 mm pitch, 10 mm ends (10/30/50/70/90) [verify]; MGN9C block 16 g, M3 tapped holes on 15 × 10 [verify]; pull both end seals and wipers, keep the end caps, oil one drop | $12.00 [cited] [verify] | $12.00 | Search "MGN9C 100mm linear rail" (the component-landscape link is the MGN9H 150 mm listing, not this part) | MGN9H block (+10 g; allowed only if the scale shows margin). Never cut a longer hardened rail | S1 |
| 2.06 | Spare MGN9C block | 1 | On its plastic retainer; slide on with the retainer butted to the rail end | $8.00 [est] [verify] | $8.00 | Search "MGN9C carriage block" [verify it ships on a retainer] | A second rail kit | S1, can wait |
| 2.07 | Hinge pin set | 1 set | M6 × 80 socket head, partially threaded (smooth shank in the Ø 6.3 bores), M6 nyloc, 2 × M6 nylon/PTFE washers about 0.5 mm | $4.00 [est] | $4.00 | Hardware store | Amazon M6 × 80 and nylon washers | S1 |
| 2.08 | 623ZZ bearings | 1 pack of 10 | 3 × 10 × 4 shielded; 2 in the pulley sheaves P2, 1 as the L8.4 bench pulley | $7.00 [cited] | $7.00 | Search "623ZZ bearing 10 pack" | F623ZZ flanged | S1 |
| 2.09 | 625-2RS bearing | 1 pack of 10 | 5 × 16 × 5 sealed; 1 in the idler housing P15 (press fit, dot of CA on the outer ring) | $8.00 [est] | $8.00 | Search "625-2RS bearing 10 pack" | 625ZZ | S1 |
| 2.10 | Idler shoulder screw | 2 (1 + 1 spare) | Ø 5 × 25 shoulder, M4 × 6 thread, alloy steel; M4 nyloc in §E.3 | $3.00 [est] [verify] | $6.00 | McMaster metric alloy-steel shoulder screws [verify part number]; search "shoulder screw 5 mm shoulder diameter 25 mm shoulder length M4" | Amazon shoulder-bolt assortment with a 5 mm shoulder, or Misumi | S1 |
| 2.11 | Dyneema cord | 1 spool (3 m needed) | 1.0 mm braided UHMWPE, about 45 kg (100 lb); 2 hinge cords, the reset cord, the wrist tether tied as a **25 mm** loop | $12.00 [est] | $12.00 | Search "1mm braided UHMWPE line 100 lb" (kite or fishing line) | Braided PE fishing line 80–100 lb, doubled if thinner than 0.8 mm | S1 |
| 2.12 | Trim cord | 1 roll | 0.5 mm clear elastic beading cord (Stretch Magic type), 120 mm loop | $5.00 [est] | $5.00 | Craft store or Amazon | Any 0.5 mm clear elastic cord | S1 |
| 2.13 | Hinge lift springs (box 2A) | 4 (2 + 2 spare) | Extension spring, music wire, zinc plated, machine loops; OD 3/8 in, wire 0.031 in, 2.50 in inside hooks, rate 0.54 lbf/in (accept 0.45–0.66), IT 0.22–0.45 lbf, max extended ≥ 5.0 in, max load ≥ 2.2 lbf; working 117 mm at 6.5 N each, 90 mm at 3.9 N | $10.00 [est] [verify] | $10.00 | McMaster-Carr 9654K family, part number 9654K___ [verify]: filter https://www.mcmaster.com/9654K/ per box 2A | Amazon or hardware-store 3/8 in OD extension spring, accepted only by the luggage-scale test | S1 |
| 2.14 | Spring fallback assortment | 1 | Extension spring assortment; only springs passing the bench test are used | $10.00 [cited] | ($10.00) | Amazon 200-pc about $10 | Hardware-store single 3/8 in OD springs | S1, optional |
| 2.15 | Holding electromagnet | 1 | Adafruit 3872 P20/15, 5 V 0.22 A, 25 N, Ø 20 × 15, M3 rear thread, 270 mm leads; wired only on the rail after the hold-to-run | $5.95 [est] | $5.95 | https://www.adafruit.com/product/3872 | Adafruit 3873 P25/20 (2.16) | S1 |
| 2.16 | Fallback electromagnet | 1 | Adafruit 3873 P25/20, 5 V, 50 N; fit only if the frame unlatches in a run (K4.8, L7); needs a Ø 25 seat | $7.95 [est] | ($7.95) | https://www.adafruit.com/product/3873 | Generic 5 V P25/20 module, measured on the luggage scale | S1, optional |
| 2.17 | Keeper plate stock | 1 bar | Mild steel flat bar 1/8 × 1 in, 12–36 in; cut one 25 × 25 × 3 keeper, flatten on 400 grit on glass | $8.00 [est] | $8.00 | Hardware store | Add a 25 × 25 square to the SendCutSend order | S1 |
| 2.18 | PTFE thread-seal tape | 1 roll | 0.075 mm, one layer on the magnet face | $2.00 [est] | $2.00 | Hardware store plumbing aisle | Any PTFE plumber's tape | S1 |
| 2.19 | Wrist magnet K&J D61 | 3 (1 + 2 spare) | 3/8 × 1/16 in N42 disc, 9.4 N rated, 0.9 g | $0.49 [cited] | $1.47 | https://www.kjmagnetics.com/d61-neodymium-disc-magnet | Amazon 3/8 × 1/16 in N42 discs (measure in L6) | S1 |
| 2.20 | Wrist keeper discs | 2 (buy a pack) | Mild steel 12 × 1.5 mm, bonded flush in the palm-lid cone | $7.00 [est] [verify] | $7.00 | Search "12mm x 1.5mm steel disc" [verify thickness] | Cut from 16 ga sheet; last resort a DIN 125 M6 washer (12 × 1.6), lower pull, re-tune in L6 | S1 |
| 2.21 | Feeler stock, rig leaves | 2 strips (1 + 1 spare) | Spring steel 0.30 × 12.7 × 305 (0.012 × 1/2 × 12 in); leaves cut 70 / 67 / 64 mm, corners R 1, edges stoned | $4.00 [cited] [verify] | $8.00 | Precision Brand feeler stock or McMaster feeler-gauge stock [verify part number]; search "feeler stock .012 x 1/2 x 12" | Precision Brand 0.012 × 1/2 in coil; width must be 12.7 mm | S1 |
| 2.22 | M8 slug washers | 20 | DIN 9021 M8, 8.4 × 24 × 2, about 6.2 g; +30 g (5, yellow tape), +60 g (10, red tape); the post holds 16 | $0.30 [est] | $6.00 | Hardware store | 5/16 in USS fender washers, trimmed on the scale | S1 |
| 2.23 | Zero pin | 1 | Ø 3 mm steel, 30 mm: the shank of the 3.0 mm bit from the drill set (5.16) | $0.00 [est] | $0.00 | No purchase | 3 mm dowel pin pack, about $6 | S1 |
| 2.24 | Silicone membrane sheet | 1 sheet (makes 4 boots) | 0.25 mm, Shore 40A, about 150 × 150; cut with P35, bonded slack to each paddle | $10.00 [est] [verify] | $10.00 | Search "0.25mm silicone rubber sheet" [verify thickness and hardness] | 0.2–0.3 mm silicone, 30A–50A | S1 |
| 2.25 | Silicone adhesive | 1 tube | Smooth-On Sil-Poxy, 2 mm bead at paddle z 26–28, 1 h cure | $14.00 [est] | $14.00 | Search "Smooth-On Sil-Poxy" | Another RTV adhesive rated for silicone rubber | S1 |
| 2.26 | PTFE film tape 0.05 mm | 1 roll | Adhesive-backed 0.05 mm PTFE film (3M 5490 class): palm-seam band and one layer over the D61 | $10.00 [est] [verify] | $10.00 | Search "PTFE film tape 0.05mm" [verify thickness; 3M 5490 itself is thicker] | Any thin PTFE film tape; each extra 0.05 mm cuts the wrist hold about 10 % | S1 |
| 2.27 | Rubber bumpers | 1 assortment | Self-adhesive Ø 10 × 6: 1 up-stop cap (glued), 4 panel feet, spares | $6.00 [est] | $6.00 | Search "self adhesive rubber bumper feet assortment" | Any Ø 10 bumper | S1 |
| 2.28 | Isolation feet | 4 | Rubber or Sorbothane Ø 30 × 15 in cups P41; only if the cradle shares the arm's desk | $2.50 [est] | $10.00 | Search "rubber feet 30mm x 15mm" or "Sorbothane hemisphere 1.25 in" | A separate stool or table (preferred, free) | S1, can wait |
| 2.29 | Baseboard | 1 | 18 mm plywood 350 × 300, only if the cradle shares the desk | $12.00 [est] | ($12.00) | Hardware store project panel | Any 15–20 mm board | S1, optional |
| 2.30 | Face cradle (SEAT) | 1 | Tabletop massage face cradle, horseshoe pad about 280 × 220, adjustable tilt, own stand; forehead load about 15 N over 60 cm² | $45.00 [est] [verify] | $45.00 | Search "tabletop massage face cradle adjustable" [verify it has a stand and tilt] | A massage-chair face-cradle attachment on a separate stool | S1 |
| 2.31 | Face cradle cushion (PRONE) | 1 | Horseshoe foam face cushion about 300 × 250 × 100 | $20.00 [est] | $20.00 | Search "face down pillow massage face cushion" | Folded towels in a U (first OC trials only) | S1, can wait |
| 2.32 | Light machine oil | 1 | Sewing-machine oil, one drop on the MGN9C block, weekly | $4.00 [est] | $4.00 | Hardware store | Any light machine oil | S1 |
| 2.33 | Medium threadlocker | 1 | Loctite 243 class (rail screws, leaf stops) | $6.00 [cited] | $6.00 | Hardware store | Any blue medium-strength threadlocker | S1 |

Section 2 subtotal in the totals: **$359.42**; optional rows add $29.95.

**Box 2A. Lift spring, pinned.** Order McMaster-Carr Precision Extension Spring, family **9654K** (zinc-plated music wire, machine loops), **part number 9654K___ [verify]**: open https://www.mcmaster.com/9654K/ and filter material music wire, OD 3/8 in, wire 0.031 in, length 2-1/2 in; take the row whose rate is nearest 0.54 lbf/in; check it against every line below; write the full part number on the order; buy 4 [verify pack size].

| Parameter | Order value | Acceptance window | Basis |
|---|---|---|---|
| Outside diameter | 0.375 in (9.5 mm) | 0.36–0.39 in | spring channels on the P1 rear face |
| Wire | 0.031 in (0.8 mm) music wire, zinc plated | 0.029–0.035 in | |
| Length inside hooks (free) | 2.50 in (64 mm) | ≤ 2.50 in (shorter is fine; the cord takes up the difference) | L0 + (6.5 N − IT)/k ≤ 117 mm between the anchor at Z 30 and the pulley at Z 148 |
| Rate | 0.54 lbf/in (0.095 N/mm) | 0.45–0.66 lbf/in (0.078–0.116 N/mm) | the cord shortens 26.8 mm at the 25° up-stop; force there must be 3.9 ± 0.5 N: k = (6.5 − F_up)/26.8 |
| Initial tension | 0.34 lbf (1.5 N) | 0.22–0.45 lbf (1.0–2.0 N) | |
| Working extension, force | 53 mm (117 mm hook to hook), 1.5 + 0.095 × 53 = **6.5 N** each | 6.5 ± 0.5 N | 13 N total, 0.832 N·m on the 64 mm lever |
| At the 25° up-stop | 26.2 mm extension (90 mm hook to hook), **4.0 N** (mechanical table: 3.9 N) | 3.9 ± 0.5 N | holds the frame up with any slug (net +0.13 N·m with +100 g) |
| Maximum extended length | ≥ 5.0 in (127 mm) | ≥ 125 mm, no set | |
| Maximum load | ≥ 2.2 lbf (10 N) | ≥ 10 N | |

Plausibility: k = G d⁴ / (8 D³ Nₐ) with G = 11.5 × 10⁶ psi, d = 0.031 in, D = 0.344 in (index 11.1): 0.54 lbf/in needs about 60 active coils, a 1.9 in body plus two 0.3 in loops ≈ 2.5 in, matching the spec; Wahl-corrected shear stress about 48 ksi at 6.5 N and 75 ksi at 10 N, below the ~135 ksi body limit [est]. **Substitute route:** search "3/8 inch OD extension spring 2.5 inch 0.031 wire", or the assortment (2.14), or hardware-store singles; use a spring only if it passes the binding bench test on the luggage scale through the cord after tie-off: 6.5 ± 0.5 N at 117 mm hook to hook and 3.9 ± 0.5 N at 90 mm; two must pass, and the L5 single-spring redundancy check must still lift the module. For a different free length, tie the cord off where the spring reads 6.5 N with the frame latched, then check 3.9 ± 0.5 N at the up-stop; the hook-to-hook length at 6.5 N must be ≤ 117 mm.

### E.3 Fasteners and inserts

| # | Item | Qty | Spec | Unit (USD) | Line (USD) | Source | Substitute | Stage |
|---|---|---|---|---|---|---|---|---|
| 3.01 | Heat-set inserts M3 | 1 pack of 100 | Brass M3 × 4 mm, for a 4.0 mm hole; 55 used | $9.00 [cited] | $9.00 | $8–10 per 100 | One M2–M5 insert kit (about $15 [est]) replaces 3.01–3.03 | S1 |
| 3.02 | Heat-set inserts M2 | 1 pack of 50 | Brass M2 × 3 mm, for a 3.2 mm hole; 18 used (palm tray P32) | $7.00 [est] | $7.00 | Search "M2 heat set insert 3mm" | Same kit | S1 |
| 3.03 | Heat-set inserts M4 | 1 small pack | Brass M4 × 6 mm; 1 used (up-stop boss in P1) [VERIFY hole on the insert kit, 5.6 mm modelled] | $6.00 [est] | $6.00 | Search "M4 heat set insert" | Same kit | S1 |
| 3.04 | Metric screw and nut assortment | 1 kit (about 1000, M3/M4/M5) | Socket-head M3 × 6/8/10/12/16/20, M4 and M5, hex nuts, washers; covers M3 × 6 (4), M3 × 10 (20), M3 × 12 (4), M3 × 16–20 (4), M3 jam nuts (3), M3 washers (30, also the 0.12 g trims) | $20.00 [cited] | $20.00 | $15–25 | Each M3 length in 10 or 25 packs | S1 |
| 3.05 | M3 × 14 socket head | 1 pack of 10 | Steel, 4 used (yaw plates P8–P9); rarely in assortments; the 6 + 6 mm plate stack may want M3 × 10 or × 12 [verify against the CAD] | $5.00 [est] [verify] | $5.00 | Search "M3 x 14 socket head cap screw" | McMaster M3 × 14 | S1 |
| 3.06 | M3 × 6 flat-head (countersunk) | 1 pack of 10 | Steel, 2 used (keeper plate on P6, with epoxy) | $5.00 [est] | $5.00 | Search "M3 x 6 flat head countersunk" | Epoxy alone plus a button head | S1 |
| 3.07 | Nyloc nut assortment | 1 | M3 (2, pulleys), M4 (1, shoulder screw), M6 (1 hinge spare) | $8.00 [est] | $8.00 | Search "nylon insert lock nut assortment M3 M4 M5 M6" | Hardware-store singles | S1 |
| 3.08 | M2 socket-head assortment | 1 kit | M2 × 6 (14: root bars 6, palm lid 6, servo side holes 2), M2 × 8 (10: knuckle plate 6, OpenRB-150 mount 4 [verify hole size]), spares for the XL330 horn screws [verify they ship with the servo] | $9.00 [est] [verify] | $9.00 | Search "M2 socket head screw assortment" | Hardware-store singles | S1 |
| 3.09 | Aluminium M3 screw assortment | 1 kit (6/8/10) | 8 × M3 × 8 (6 paddle clamps, 2 riser to seat), 2 × M3 × 10 if the riser-to-seat pair passes through the P47 filler, 4 × M3 × 6 for the mass fallback; snug only, 0.3 N·m | $9.00 [est] | $9.00 | Search "aluminum M3 socket head screw assortment" | Nylon M3 for the riser-to-seat pair only | S1 |
| 3.10 | Nylon M3 screw assortment | 1 kit | Nylon M3 × 10 (3 leaf stops), nylon M3 × 8 (1 weight-cap screw) | $8.00 [est] | $8.00 | Search "nylon M3 screw assortment" | Nylon M3 thumbscrews | S1 |
| 3.11 | Knurled M3 × 16 thumbscrews | 1 pack of 10 | Stainless, 3 used (down-stop with jam nut, trim cleat, scale lock) | $8.00 [est] | $8.00 | Search "M3 x 16 knurled thumb screw" | Socket-head M3 × 16 plus a printed knob | S1 |
| 3.12 | M4 screws for VESA, ballast, up-stop | 1 lot | 4 × M4 × 50 with 4 washers (VESA plate + 15 mm ballast stack), 1 × M4 × 25 (up-stop); with no ballast M4 × 16–20 (often supplied with the arm) | $5.00 [est] | $5.00 | Hardware store | Amazon singles | S1 |
| 3.13 | M5 × 12 and M5 × 16 socket head | 10 of each | For printed nodes the kit's M5 × 10 may not reach through (P6, P7 are 12 mm parts) [verify against the CAD] | $6.00 [est] [verify] | $6.00 | Hardware store or Amazon | Longer screws if the bracket kit has them | S1 |
| 3.14 | Wood screws #4 × 1/2 in | 8 | For the 4 foot cups P41 on the baseboard | $3.00 [est] | ($3.00) | Hardware store | M3 × 12 wood screws | S1, optional |
| 3.15 | Zip ties | 1 pack (100) | 100 and 200 mm; cable anchors at the hinge, carrier beam and handle; P36 clip slots | $5.00 [est] | $5.00 | Search "zip ties assorted" | Hook-and-loop ties | S1 |

Section 3 subtotal in the totals: **$110.00**; optional rows add $3.00.

**Table 3A. Every fastener**

| Size | Count used | Where | Bought in row |
|---|---|---|---|
| M2 × 6 socket head | 14 | root clamp bars 6, palm lid 6, XL330 side holes 2 | 3.08 |
| M2 × 8 socket head | 10 | knuckle plate 6, OpenRB-150 to tray bosses 4 [verify hole size] | 3.08 |
| M2 horn screws | 4 | P16 horn disc to the XL330 horn: the servo's own screws [verify supplied] | XL330 box; spares 3.08 |
| M3 × 6 socket head, steel | 4 | riser P26 to MGN9C block (never longer than 6 mm) | 3.04 |
| M3 × 6 socket head, aluminium | 4 | mass fallback for the 4 carriage screws | 3.09 |
| M3 × 6 flat head | 2 | keeper plate on P6 | 3.06 |
| M3 × 8 socket head, steel | 28 | rail 5, mast parts 8, magnet rear 1, tray lid and panel lid 6; wand handle bar 4, wand paddle bar 2, spare wand paddle 2 | 5.11 (50-pack) |
| M3 × 8 socket head, aluminium | 8 | paddle clamp bars 6, riser arm to upper seat 2 | 3.09 |
| M3 × 10 socket head, steel | 20 | cheek A 4, servo strap 2, idler housing 2, P47 filler 2; tray P3 to adapter P1 4, servo cradle P13 to drop leg P11 4, reset-cord guide P45 2 with nuts [verify] | 3.04 |
| M3 × 10 nylon | 3 | leaf stop screws | 3.10 |
| M3 × 8 nylon | 1 | weight cap P29 | 3.10 |
| M3 × 12 socket head | 4 | crossbar to cheeks | 3.04 |
| M3 × 14 socket head | 4 | yaw plates P9 to P8 [verify length] | 3.05 |
| M3 × 16 socket head | 4 | pulley axles 2, hold-to-run housing P39 to P40 2 (M3 × 16–20 [verify]) | 3.04 |
| M3 × 16 knurled thumbscrew | 3 | down-stop, trim cleat, scale lock | 3.11 |
| M3 nyloc nut | 2 | pulley axles | 3.07 |
| M3 hex nut | 3 + 2 | jam nuts on the thumbscrews; P45 guide nuts | 3.04 |
| M3 washer | 30 | magnet depth shims (0.5 mm each = 0.6 mm at the nails), weight trims (0.12 g each) | 3.04 |
| M4 × 50 socket head + washer | 4 + 4 | VESA plate plus ballast stack | 3.12 |
| M4 × 25 socket head | 1 | up-stop with rubber cap | 3.12 |
| M4 nyloc nut | 1 | shoulder screw | 3.07 |
| Shoulder screw Ø 5 × 25, M4 | 1 (+1) | idler | 2.10 |
| M5 × 10 socket head | 22 | 2020 end taps 2, T-nut joints 20 | 2.04 kit |
| M5 drop-in T-nut | 20 | drop legs 4, keeper lever 2, cord bar 2, yaw plates 4, corner brackets 4, hinge knuckle 2, spare 2 | 2.04 kit |
| M5 × 12 / × 16 | as needed | printed nodes thicker than M5 × 10 reaches [verify against CAD] | 3.13 |
| 2020 corner bracket | 2 | post to spine | 2.04 kit |
| M6 × 80 socket head + nyloc + 2 nylon washers | 1 set | hinge pin | 2.07 |
| #4 × 1/2 in wood screw | 8 | foot cups P41 (only with the baseboard) | 3.14 (optional) |

**Table 3B. Heat-set inserts by part** (brass; M3: 4.0 mm hole, 4 long; M2: 3.2 mm hole, 3 long)

| Part | M3 | M2 | M4 |
|---|---|---|---|
| P1 VESA adapter (tray seat; up-stop) | 4 | 0 | 1 |
| P3 electronics tray (lid) | 2 | 0 | 0 |
| P8 frame yaw plate (45° pattern) | 8 | 0 | 0 |
| P11 drop leg, servo side | 4 | 0 | 0 |
| P12 drop leg, idler side | 2 | 0 | 0 |
| P13 servo cradle (strap) | 2 | 0 | 0 |
| P19 yoke cheek A | 6 | 0 | 0 |
| P20 yoke cheek B | 2 | 0 | 0 |
| P21 crossbar and mast (rail 5, stops/shroud/cleat 8) | 13 | 0 | 0 |
| P23 down-stop block | 1 | 0 | 0 |
| P27 trim cleat | 1 | 0 | 0 |
| P28 upper wrist seat (weight post) | 1 | 0 | 0 |
| P32 palm tray (stops 3; root bars 6, lid 6, knuckle plate 6) | 3 | 18 | 0 |
| P37 control panel box | 4 | 0 | 0 |
| P40 button housing half B | 2 | 0 | 0 |
| **Total used** | **55** | **18** | **1** |
| Bought | 100 | 50 | 1 small pack |

Paddles and the wand use 2.6 mm thread-forming holes for their M3 × 8 clamp screws (inserts optional there with a 4.0 mm hole).

### E.4 Printing (filament)

| Material | Need | With 30 % waste | Buy | Notes |
|---|---|---|---|---|
| PETG | 900 g (P1–P48, 60 pieces) + 120 g (tips, carriers, paddles, bars, handle) + 30 g (tip box) = 1,050 g | 1,365 g | 2 × 1 kg spools | about 635 g left for the [VERIFY] reprints (P13, P16) and fit tests |
| TPU 90A | 20 g (pads, bumpers) + 10 g (seam sleeves × 4, E pads × 2) = 30 g | 39 g | 1 small spool | 90A, not 95A, for the sleeves |
| Resin | none | | | standard SLA resin is banned at the scalp (red line 9) |
| PLA | none required | | | allowed only for the wand handle; never near skin |

| # | Item | Qty | Spec | Unit (USD) | Line (USD) | Source | Substitute | Stage |
|---|---|---|---|---|---|---|---|---|
| 4.01 | PETG filament, spool 1 (bright colour) | 1 kg | 1.75 mm, orange or yellow: tips must be one bright colour (visible in dark hair, identical across tips for blinding). Stage 0 uses about 150 g | $25.00 [cited] | $25.00 | Search "PETG 1.75 1kg orange" | Any PETG; never PLA near skin | S0 |
| 4.02 | PETG filament, spool 2 | 1 kg | 1.75 mm, any colour: frame nodes, adapter, yoke, guards, boxes | $25.00 [cited] | $25.00 | | Same | S1 |
| 4.03 | TPU 90A filament | 1 small spool | 1.75 mm, Shore 90A (e.g. Polymaker PolyFlex TPU90): seam sleeves, E pads, servo-stop bumpers, up-stop pad, wedge pads; 30 g used | $29.00 [cited] | $29.00 | | TPU 95A for bumpers and pads only; the sleeves need 90A | S0 |

Section 4 subtotal: **$79.00**. Printer notes: 0.4 mm nozzle (brass is fine); bed ≥ 220 × 220 mm because P21 lies 196 × 108 on the bed (a 180 mm bed will not do) and P32/P33 are 169 mm long; textured PEI or glue stick on smooth PEI for PETG; TPU 90A needs direct drive at 15–20 mm/s; dry PETG and TPU if they string; inserts at 220–230 °C square to the surface.

### E.5 Tips

Tips items 1, 2 and 18 are bought as whole spools in §E.4 and carry $0 here; the other 15 items total $98. Items 11–13 and 16 also serve the rig (the M3 × 8 pack covers the 20 rig steel M3 × 8; the CA and epoxy cover the keeper bonds; the 3.0 mm drill shank is the servo zero pin). Rig leaves are row 2.21.

| # | Item | Qty | Spec | Unit (USD) | Line (USD) | Use | Stage |
|---|---|---|---|---|---|---|---|
| 5.01 | PETG filament, one bright colour | 120 g | 1.75 mm | $0.00 [cited] | $0.00 | all tips, carriers, paddles, bars, handle (spool 4.01) | S0 |
| 5.02 | TPU 90A filament | 10 g | 1.75 mm | $0.00 [cited] | $0.00 | seam sleeves × 4, E pads × 2 (spool 4.03) | S0 |
| 5.03 | Neodymium magnets | 50 pack | N52, 6 × 2 mm disc, axial | $9.00 [cited] | $9.00 | one per pocket | S0 |
| 5.04 | Neodymium magnets | 20 pack | N52, 6 × 3 mm disc, axial | $6.00 [cited] | $6.00 | breakaway tuning (below 4 N) | S1, can wait |
| 5.05 | Steel keeper discs | 50 pack | mild steel 6 × 1 mm (or 1 mm sheet 100 × 100) | $7.00 [cited] | $7.00 | tang keepers, flats filed to 3.9 mm | S0 |
| 5.06 | Feeler stock | 2 strips | spring steel 0.30 × 12.7 × 305 | $8.00 [cited] | $8.00 | wand leaf and spares | S0 |
| 5.07 | Press-on nails | 1 box | ABS full cover, sizes 0–3, 100+ | $7.00 [cited] | $7.00 | P tips (two nested per tip) | S0 |
| 5.08 | Nylon picks | 12 pack | Dunlop nylon 0.88 mm | $5.00 [cited] | $5.00 | A45 blades | S0 |
| 5.09 | Nylon picks or sheet | 12 pack | Dunlop nylon 1.0 mm, or nylon 6/6 sheet 1.0 mm | $5.00 [cited] | $5.00 | E blades, B45 slot blades | S1, can wait |
| 5.10 | Steel balls | 100 pack | G25 chrome steel, 3.0 mm | $5.00 [cited] | $5.00 | H tips (or `PRINTED_BALL = true`) | S0 |
| 5.11 | Screws | 50 pack | M3 × 8 socket or button head | $5.00 [cited] | $5.00 | wand bar 4, paddle bars 2 each; also the 20 rig steel M3 × 8 | S0 |
| 5.12 | Cyanoacrylate | 2 | thin and gel, 20 g each | $8.00 [cited] | $8.00 | blades, nails, balls, sleeve rim; also the rig gel CA | S0 |
| 5.13 | Epoxy | 1 | 5-minute, twin syringe | $6.00 [cited] | $6.00 | keepers, P fill; also the keeper plate and wrist disc | S0 |
| 5.14 | Abrasive paper | 1 sheet each | wet-and-dry 400, 600, 1000, 2000 | $8.00 [cited] | $8.00 | edge radius | S0 |
| 5.15 | Nail files and buffer | 1 set | 180 / 240 file, 3-way buffer block | $4.00 [cited] | $4.00 | plan corners, P trimming | S0 |
| 5.16 | Drill-bit set | 1 | 0.5–3.0 mm by 0.1 mm | $10.00 [cited] | $10.00 | radius reference shanks (0.6, 0.8, 1.0); the 3.0 mm shank is the zero pin | S0 |
| 5.17 | Marker and varnish | 1 each | 0.3 mm permanent marker, clear nail varnish | $5.00 [cited] | $5.00 | blinding codes | S0 |
| 5.18 | Tip box | 1 | printed block (30 g PETG) or pill organiser with foam | $0.00 [cited] | $0.00 | coded tip storage (spool 4.01); do not also print P48 | S0 |

Section 5 subtotal: **$98.00**. The tip subsystem costs about $103 with filament pro rata, about $132 if a TPU spool must be bought; the Stage-0 wand's marginal cost is about $39.

### E.6 Electronics

Fuse rule: 1 A fast-blow 5 × 20 (F1AL250V) in the rail at the adapter; running current about 0.6 A; a stalled XL330 at 1.47 A opens it; 1.25 A fast is the only permitted step up; one spare fuse lives in the kit (K3.7).

| # | Item | Qty | Spec | Unit (USD) | Line (USD) | Source | Substitute | Stage |
|---|---|---|---|---|---|---|---|---|
| 6.01 | 5 V 4 A power adapter | 1 | Adafruit 1466: 5 V 4 A, UL-listed, 100–240 V, 5.5 × 2.1 centre-positive, 20 W; with 22 AWG rail wire keeps the drop under 0.2 V at 0.6 A | $14.95 [est] | $14.95 | https://www.adafruit.com/product/1466 ($15–24 [cited]) | Same part at Jameco; Mean Well GST25A05 [verify] | S1 |
| 6.02 | DC jack to screw-terminal adapter | 1 | 5.5 × 2.1 female jack to 2-pin screw terminal | $2.00 [est] | $2.00 | Adafruit 368 | Generic pack | S1 |
| 6.03 | Fuses 1 A fast-blow 5 × 20 | 1 pack of 10 | F1AL250V glass: one fitted, one spare taped inside the tray lid | $5.00 [est] | $5.00 | Search "F1AL250V 5x20 fuse" | Bussmann GMA-1A | S1 |
| 6.04 | Inline fuse holder | 1 | Screw-type inline holder for 5 × 20, 18 AWG leads | $7.00 [est] | $7.00 | https://www.amazon.com/uxcell-Inline-Screw-Holder-Gauge/dp/B07SM5KYZ7 | Panel 5 × 20 holder in the tray | S1 |
| 6.05 | Fuses 1.25 A fast 5 × 20 | 1 pack | Only permitted step up if 1 A nuisance-trips; note it on the diagram | $5.00 [est] | ($5.00) | Search "1.25A fast blow 5x20" | None (never higher) | S1, optional |
| 6.06 | E-stop, boxed | 1 | 22 mm NC mushroom, latching (push-lock, twist-release), 10 A, boxed; second NC contact unused | $14.00 [cited] | $14.00 | https://www.amazon.com/TWTADE-Mushroom-Emergency-Warranty-YW1B-V4E02R-BOX/dp/B07NNZB41H | APIELE 1NC LA139A-ES542 panel mount https://www.amazon.com/APIELE-Emergency-Stop-Button-Switch/dp/B0F2F8TYMY in a printed box | S1 |
| 6.07 | E-stop weighted base | 1 plate | Steel plate about 100 × 100 × 3 or heavier; screw the e-stop box to it | $9.00 [est] | $9.00 | A 6th plate in the SendCutSend order | Steel mending plate or any 0.5 kg steel object | S1 |
| 6.08 | Hold-to-run button | 1 (pack) | uxcell 30 mm momentary arcade push button, N.O. microswitch, 3 A 250 V, snap-in; P39 deck hole Ø 29.6 [verify against the button] | $8.00 [est] [verify] | $8.00 | https://www.amazon.com/uxcell-Mounting-Momentary-Button-Switch/dp/B08HH78XMH [verify pack size] | Philmore 30-825 (6.11) | S1 |
| 6.09 | Hold-to-run cable | 1 spool (1.5 m used) | 2-core 22 AWG stranded, through the printed gland and zip-tie anchor | $9.00 [est] | $9.00 | Search "22 AWG 2 conductor stranded wire 25 ft" | Two 22 AWG silicone wires twisted and sleeved | S1 |
| 6.10 | Hold-to-run housing | 1 set | Printed PETG handle Ø 36 × 110 (P39, P40), button face 3 mm below the rim | $0.00 [cited] | $0.00 | Printed | 6.11 | S1 |
| 6.11 | Hold-to-run, bought alternative | 1 | Philmore 30-825 hand-held momentary N.O. SPST, 3 A 125 V, die-cast; extend its cord to 1.5 m | $10.00 [est] | ($10.00) | https://www.amazon.com/Hand-Held-Button-Switch-30-825/dp/B00T6RCGNC | Printed housing | S1, optional |
| 6.12 | Electromagnet | see 2.15 | Adafruit 3872 P20/15 | $0.00 | $0.00 | Row 2.15 | Row 2.16 | S1 |
| 6.13 | Flyback diode | 1 pack | 1N5819 Schottky 40 V 1 A across the coil, band to + | $5.00 [est] | $5.00 | Any distributor | 1N5817 or 1N5822 | S1 |
| 6.14 | Bulk capacitor | 1 pack | 470 µF electrolytic ≥ 10 V at the OpenRB terminal | $5.00 [est] | $5.00 | Any distributor | 470–1000 µF, 16 V | S1 |
| 6.15 | TVS diode | 1 pack | SMAJ5.0A (SMD, DO-214AC) across + and − at the terminal, on perfboard pads | $6.00 [est] [verify] | $6.00 | Any distributor | Through-hole SA5.0A (DO-15) [verify] | S1 |
| 6.16 | OpenRB-150 controller | 1 | SAMD21G18A, 4 DXL TTL ports, FET-switched DXL power, USB-C, terminal block supplied; jumper on VIN(DXL), never USB(5V); tray pocket about 66 × 25 [verify outline] | $28.64 [cited] | $28.64 | https://www.robotis.us/openrb-150/ ($24.90–28.64) | See §E.9 | S1 |
| 6.17 | Dynamixel XL330-M288-T (elbow) | 1 | 5 V (3.7–6.0 V), 0.52 N·m stall at 1.47 A, 18 g, 4096 ticks/rev, protocol 2.0, ID 1; ships with a horn and a short X3P cable [verify contents] | $27.49 [cited] | $27.49 | https://www.robotis.us/dynamixel-xl330-m288-t/ | See §E.9 | S1 |
| 6.18 | DXL cable 340 mm or longer | 1 (pack) | ROBOTIS X3P (JST-EH 3-pin, 2.5 mm pitch) ≥ 340 mm: the tray-to-servo run is about 330 mm including the 60 mm hinge service loop; the stock 180 mm cable is too short | $8.00 [est] [verify] | $8.00 | Search robotis.us "Robot Cable-X3P" [verify a ≥ 340 mm length exists] | Make one with JST-EH 3-pin housings and crimps (22–26 AWG) | S1 |
| 6.19 | Potentiometers 10 kΩ linear with knobs | 1 pack | 2 used (SPEED, VARIATION), 7 mm bushing for the Ø 7.2 panel holes; tape marks 0/50/100 % | $8.00 [est] | $8.00 | Search "B10K potentiometer with knob" | Alpha 9 mm pots | S1 |
| 6.20 | Toggle switch | 1 pack | SPST (or SPDT as SPST), 6 mm bushing: PERIODIC/HUMAN on D4 | $7.00 [est] | $7.00 | Search "mini toggle switch 6mm" | Any 6 mm bushing toggle | S1 |
| 6.21 | Status LED | 1 pack | 5 mm LED, on D5 | $5.00 [est] | $5.00 | Search "5mm LED assortment" | Any 5 mm LED | S1 |
| 6.22 | Resistor assortment | 1 kit | 1/4 W: 330 Ω (LED), 2 × 10 kΩ (rail-sense divider) | $7.00 [est] | $7.00 | Search "resistor kit 1/4W" | Singles | S1 |
| 6.23 | Ceramic capacitors 100 nF | 1 pack | 100 nF from A2 to GND | $5.00 [est] | $5.00 | Search "100nF ceramic capacitor" | Assortment | S1 |
| 6.24 | 22 AWG silicone wire | 1 kit (6 colours) | Rail wiring, red and black | $12.00 [cited] | $12.00 | | PVC hook-up wire 22 AWG | S1 |
| 6.25 | 6-core 26 AWG cable | 1 m used | Control panel P37 to tray: 3V3, GND, A0, A1, D4, D5 | $9.00 [est] | $9.00 | Search "6 conductor 26 AWG cable" | Ribbon cable with Dupont ends | S1 |
| 6.26 | Heat-shrink assortment | 1 kit | Magnet lead splices and terminations | $6.00 [cited] | $6.00 | | Any assortment | S1 |
| 6.27 | Braided sleeving | 2 m | 6 mm expandable PET sleeve on the DXL cable across the hinge | $7.00 [est] | $7.00 | Search "braided cable sleeve 6mm" | Spiral wrap | S1 |
| 6.28 | Wago 221-413 lever connectors | 1 pack | 3-way lever splice for the rail + node (and a − node), inside a printed cover | $9.00 [est] | $9.00 | Search "Wago 221-413" | Screw terminal block | S1 |
| 6.29 | Dupont kit | 1 kit | Housings, crimp pins and jumpers: pots, toggle, LED, HX711 header | $8.00 [cited] | $8.00 | | Pre-crimped female jumpers | S1 |
| 6.30 | Perfboard | 1 pack | Rail board 30 × 20 (divider, TVS, 470 µF) plus spares | $7.00 [est] | $7.00 | Search "perfboard prototype board" | Stripboard | S1 |
| 6.31 | USB-C cable | 1 | Data-capable USB-C, 2 m; tie-wrapped down the arm | $8.00 [est] | $8.00 | Search "USB C data cable 2m" | Any data USB-C (not charge-only) | S1 |
| 6.32 | Insulated crimp terminals | 1 assortment | Fork terminals (e-stop block), 4.8 mm female spades (microswitch) | $10.00 [est] | $10.00 | Search "insulated crimp terminal assortment" | Solder and heat-shrink | S1 |
| 6.33 | Dynamixel XL330-M288-T (spare, Stage 3 yaw) | 1 | Second servo, ID 2; recommended in the Stage-1 Robotis cart as the spare for the single point of failure | $27.49 [cited] | $27.49 | https://www.robotis.us/dynamixel-xl330-m288-t/ | XL330-M077-T | S3 |
| 6.34 | Lazy-Susan bearing ring | 1 | About 100 mm ring under the yaw plates for the Stage-3 yaw servo | $6.00 [est] | $6.00 | Search "lazy susan bearing 4 inch" | Printed thrust ring with 6 mm balls | S3 |
| 6.35 | Bar load cell 5 kg with HX711 | 1 kit | 5 kg bar cell for the 40 × 12 wrist slot [verify a 40 mm long 5 kg cell exists; common ones are about 80 mm]; HX711 on D2/D3 | $10.00 [cited] [verify] | $10.00 | $8–12 kit; HX711 alone $4.95 https://www.sparkfun.com/products/13879 | SparkFun HX711 plus a separate cell | S3 |

Section 6 subtotal in the totals: **$300.57**; optional rows add $15.00. **Safety-critical, do not substitute casually:** the brick must be UL-listed, 5 V regulated (no LiPo, no unregulated wall wart); the e-stop must be NC and latching; the hold-to-run must be momentary NO; the electromagnet must hang on the rail after the hold-to-run and nowhere else; the OpenRB jumper must be on VIN(DXL) (bench test B3 is a hard gate).

### E.7 Bench and test kit

| # | Item | Qty | Spec | Unit (USD) | Line (USD) | Source | Substitute | Stage |
|---|---|---|---|---|---|---|---|---|
| 7.01 | Real-hair training head, short | 1 | Cosmetology mannequin, 100 % human hair; trim to 3–5 cm yourself | $32.00 [cited] | $32.00 | $28–36 (https://www.amazon.com/wig-heads/s?k=wig+heads) | Human-hair wig on the foam head | BK, buy with S0 |
| 7.02 | Real-hair training head, long | 1 | Same, left long | $32.00 [cited] | $32.00 | | Human-hair wig, $65–100 | BK |
| 7.03 | Mannequin table clamp | 1 | Table clamp for the training heads | $8.00 [cited] | $8.00 | | C-clamp and a dowel | BK, buy with S0 |
| 7.04 | Kanekalon synthetic wig | 1 | Long synthetic wig in Kanekalon fibre: the conservative wrap screen | $18.00 [est] [verify] | $18.00 | Search "Kanekalon synthetic wig long" [verify the fibre] | Any long synthetic wig | BK |
| 7.05 | Styrofoam ball 7 in | 1 | 178 mm diameter (R 89, within 1.2 % of the R 90 form) for L1, L4 and the apex gauge | $7.00 [est] | $7.00 | Craft store | 180 mm foam sphere | BK |
| 7.06 | Foam wig head | 1 | Hairless styrofoam head for fit checks and L5 | $7.00 [cited] | $7.00 | | The 7 in ball | BK |
| 7.07 | Nylon monofilament 100 µm | 1 spool | 0.10 mm nylon (about 2 lb test): the hair probe (K1.10, L8.6) | $5.00 [est] | $5.00 | Search "0.10mm nylon monofilament" | Fly-fishing tippet 6X–7X | BK |
| 7.08 | Polyester film tape 50 µm | 1 roll | 50 µm polyester or PTFE tape, 3 layers on the rod (L9) | $6.00 [cited] | $6.00 | | 3M 850-type polyester tape | BK, buy with S0 |
| 7.09 | Rod 10 mm | 1 | 10 mm steel rod or 3/8 in dowel, about 150 mm | $2.00 [cited] | $2.00 | | Any 10 mm rod | BK, buy with S0 |
| 7.10 | Calibration weight set | 1 set (1–100 g) | 15 / 50 / 100 g tether weights (L8.4), gram weights for L3, scale check | $12.00 [est] | $12.00 | Search "calibration weight set 1g 100g" | Fishing sinkers trimmed on the scale | BK |
| 7.11 | Pulley for tether weights | 1 | Spare 623ZZ from 2.08 on an M3 screw clamped to the table edge | $0.00 | $0.00 | No purchase | Smooth rod edge | BK |
| 7.12 | Carbon paper | 1 pack | Lift-off chord marks (L4), day-0 loaded-edge marks | $5.00 [est] | $5.00 | Office supply | Whiteboard-marker ink on the tips | BK, buy with S0 |
| 7.13 | Foam ear plugs | 1 pack | For the O-5 sound condition | $5.00 [est] | $5.00 | Pharmacy | Any foam plugs | BK |
| 7.14 | Black cloth and card | 1 set | About 0.5 m black felt under the cradle, black card under the wig head | $6.00 [est] | $6.00 | Craft store | A black T-shirt | BK |
| 7.15 | Lint roller | 1 | Hand, knuckle plate and cloth after every session | $4.00 [est] | $4.00 | | Tape | BK |
| 7.16 | IR thermometer | 1 | Non-contact; servo, magnet and adapter temperatures in L7 | $18.00 [est] | $18.00 | Search "infrared thermometer gun" | Thermocouple on the multimeter | BK |
| 7.17 | Hygrometer | 1 | Digital thermo-hygrometer: RH for L8 | $9.00 [est] | $9.00 | Search "digital hygrometer" | Phone weather app (less accurate) | BK |
| 7.18 | 10× loupe | 1 | Edge silhouette checks and seam inspection | $8.00 [cited] | $8.00 | | Phone macro lens | BK, buy with S0 |
| 7.19 | Hair clips | 1 pack | Target-patch marks 50 mm apart; hair clipped back | $5.00 [est] | $5.00 | Drugstore | Bobby pins | BK |
| 7.20 | Hand mirror | 1 | Self-aiming with the phone camera | $5.00 [est] | $5.00 | | Phone front camera | BK |
| 7.21 | Safety glasses | 1 | On before the rail is powered, every session | $8.00 [est] | $8.00 | Hardware store | Any ANSI Z87.1 glasses | BK |
| 7.22 | Spring scale 0–5 N | 1 | 0–500 g pull scale, 5 g divisions: L6(a) wrist breakaway at nail height | $12.00 [est] | $12.00 | Search "spring scale 500g" | Luggage scale (coarse for L6) | BK |
| 7.23 | Steel ruler 150 mm | 1 | Leaf deflection (L2), lift height in the video (L5) | $5.00 [est] | $5.00 | | Caliper depth rod | BK |
| 7.24 | Phone macro clip lens | 1 | Edge photos and 240 fps side video | $10.00 [est] | ($10.00) | Search "phone macro clip lens" | Loupe held to the phone | BK, optional |
| 7.25 | Wide-tooth comb and fine tweezers | 1 each | Combing baseline (L8), removing trapped hairs | $8.00 [est] | $8.00 | Drugstore | Any | BK |
| 7.26 | Cleaning consumables | 1 lot | 70 % IPA 16 oz, pipe cleaners, cotton balls | $9.00 [est] | $9.00 | Pharmacy | Alcohol wipes | BK, buy with S0 |
| 7.27 | Paint pen | 1 | Torque marks on every tightened screw (K2.15) | $4.00 [est] | $4.00 | Hardware store | Nail varnish | BK |

Section 7 subtotal in the totals: **$240.00**; optional rows add $10.00.

### E.8 Tools

Buy only what you do not own. The tip-finishing grits, nail files and the 0.5–3.0 mm drill set are rows 5.14–5.16.

| # | Item | Qty | Spec | Unit (USD) | Line (USD) | Source | Substitute | Stage |
|---|---|---|---|---|---|---|---|---|
| 8.01 | 3D printer (if not owned) | 1 | Bed ≥ 220 × 220, direct drive for TPU 90A, hotend ≥ 250 °C, textured PEI; e.g. Bambu Lab A1 (256 mm bed), about $300–400 [est]; not in the totals | $0.00 [est] | $0.00 | (the A1 mini at $199–249 is too small for P21) | Print service: JLC3DP $8–25 per 100 g part + $8–15 shipping, about $150–250 for 1.1 kg [est], 2–3 weeks; library makerspaces are often PLA-only (not allowed) | T, buy with S0 |
| 8.02 | Soldering iron | 1 | Pinecil V2 USB-C (+ a 65 W USB-C PD charger if none) | $30.00 [cited] | $30.00 | https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/ | Any temperature-controlled iron | T |
| 8.03 | Heat-set insert tip | 1 set | Pinecil/TS100 compatible, M2 and M3; 220–230 °C | $10.00 [cited] | $10.00 | | An old conical tip | T |
| 8.04 | Solder and flux | 1 lot | 63/37, 0.6 mm, plus a flux pen | $10.00 [cited] | $10.00 | | Any rosin-core 63/37 | T |
| 8.05 | Digital calipers 150 mm | 1 | Leaf lengths, tang fit, insert holes, slug stack | $15.00 [cited] | $15.00 | | Steel rule (coarse) | T, buy with S0 |
| 8.06 | Kitchen scale 0.1 g | 1 | 0.1 g resolution, 500 g max: W1 = 92 ± 5 g, per-nail shares, slug sets, leaf rate, wand force practice | $12.00 [cited] | $12.00 | | 1 g / 5 kg kitchen scale (the minimum) | T, buy with S0 |
| 8.07 | Luggage scale | 1 | Digital hanging scale 110 lb, 10 g resolution: springs 6.5 / 3.9 N, magnet pull-off ≥ 19 N, 7.5 N leaf proof, frame yield 8–11 N | $12.00 [cited] | $12.00 | https://www.walmart.com/ip/G-force-Digital-Hanging-Luggage-Scale-110-lbs-Max/40900467 | Spring scale | T |
| 8.08 | Multimeter | 1 | Polarity and rail 0 V checks (B1, B3), brick 4.75–5.25 V | $20.00 [cited] | $20.00 | AstroAI class | Any DMM | T |
| 8.09 | Metric hex keys, ball end | 1 set | 1.5 (M2), 2.5 (M3), 3 (M4), 4 (M5), 5 mm (M6) | $10.00 [cited] | $10.00 | | Hex bit set | T, buy with S0 |
| 8.10 | M5 tap and tap handle | 1 set | M5 × 0.8 for the two carrier-beam ends; no M2/M3 taps needed | $10.00 [est] | $10.00 | Hardware store | Misumi extrusion with tapped ends [verify] | T |
| 8.11 | Drill bits 1/4 in and 5.0 mm | 1 each | 1/4 in (6.35) opens the Ø 6.3 hinge bores (P1, P5); 5.0 mm for the cheek B shoulder bore (P20) | $6.00 [est] | $6.00 | Hardware store | 6.3 and 5.0 mm reamers | T |
| 8.12 | Mitre box and hacksaw | 1 set | 32 tpi blade for aluminium | $18.00 [est] | $18.00 | Hardware store | A hardware-store cutting service | T |
| 8.13 | Deburring tool and needle files | 1 each | Extrusion ends, printed bores | $18.00 [cited] | $18.00 | | Utility knife | T |
| 8.14 | Sandpaper 220 and 400 | 1 pack | Printed parts; keeper, seat and mast faces flattened on glass | $6.00 [cited] | $6.00 | | Wet-and-dry from 5.14 | T |
| 8.15 | Plastic polish | 1 | Knuckle plate to Ra ≤ 0.8 µm after 400 grit; nylon blades | $8.00 [est] | $8.00 | Search "plastic polish" | Fine toothpaste | T |
| 8.16 | Aviation snips | 1 | Cut 0.30 mm feeler-stock leaves | $12.00 [est] | $12.00 | Hardware store | Heavy scissors (dull quickly) | T, buy with S0 |
| 8.17 | Fine stone | 1 | Stone the leaf edges and ends | $8.00 [est] | $8.00 | Search "pocket sharpening stone fine" | 1000-grit diamond file | T |
| 8.18 | Flush cutters, wire stripper, small screwdrivers | 1 each | Support removal and electronics | $22.00 [cited] | $22.00 | | Multi-tool | T, buy with S0 |
| 8.19 | Crimp tool | 1 | Dupont pins and insulated terminals (and JST-EH if you make the DXL cable) | $20.00 [est] | ($20.00) | Search "dupont crimping tool" | Pre-crimped jumpers plus solder | T, optional |
| 8.20 | Helping hands | 1 | Holding leads while soldering | $12.00 [cited] | ($12.00) | | Blu-tack on the desk | T, optional |

Section 8 subtotal in the totals: **$227.00**; optional rows add $32.00.

### E.9 Substitutes and single points of failure

| Part | Why it matters | First substitute | Second substitute | What changes |
|---|---|---|---|---|
| XL330-M288-T | only actuator; current-based position control is the electronic clutch | Same part from Trossen Robotics or the ROBOTIS Amazon store; buy two in Stage 1 (6.33) | XL330-M077-T (same body, 0.22 N·m, 258 rpm, about $27 [cited, unverified]) | M077: re-derive goal current and the velocity scale (§I) [verify]; 0.22 N·m is still twice the 0.1 N·m the 1.2 N cap needs; no mechanical change |
| OpenRB-150 | FET-switched DXL power on VIN(DXL), logic on USB, Arduino sketch | Same part from Trossen, RobotShop or the ROBOTIS Amazon store; wait for stock | Stack B: Waveshare Servo Driver with ESP32 ($15–16) + Feetech STS3215 7.4 V ($14–20) | Stack B is a redesign: 7.4 V rail, 12 V or 7.4 V magnet, 2 A fuse, 20 AWG, no servo bus watchdog (add an INA219 rail trip), a firmware port, and a 55 g servo needing a new cradle; about a week; last resort |
| MGN9 rail / MGN9C block | the float: N = W for any µ; 92 g budget | MGN9H block on the 100 mm rail (+10 g; only if the scale shows margin, then use the trim cord) | MGN7C on an MGN7 rail (−6 g); or genuine HIWIN MGN9C from Misumi [est $40–60] | MGN7: new hole pattern; reprint the P21 mast and P26 riser. Never cut a hardened rail, never let a block run off the rail without its retainer |
| Electromagnet P20/15 | holds the frame down; loss of power must lift the nails ≥ 25 mm | Adafruit 3873 P25/20, 50 N (2.16) | Generic 5 V P20/15 or P25/20 module, ≤ 0.3 A at 5 V, M3 rear thread [est $7], pull-off measured ≥ 19 N warm | P25/20: Ø 25 seat on the P1 magnet arm. Never a 12 V magnet on the 5 V rail; never fed from anywhere but the rail |
| Lift springs | two in parallel; one alone must still lift | Box 2A substitute route with the luggage-scale test | Lee Spring or Century Spring stock springs with the box 2A numbers [verify] | none if the numbers are met |
| 5 V 4 A brick | the rail supply; UL listing is K3.1 | Jameco 1466 (same part) | Mean Well GST25A05 5 V 4 A UL desktop adapter [verify] | barrel must be 5.5 × 2.1 centre-positive or the jack adapter changes |
| K&J D61 | sets the 2.0 N wrist breakaway | Amazon 3/8 × 1/16 in N42 discs | Two D41 (1/4 × 1/16 in) stacked [est] | re-tune with tape layers in L6(a) at nail height |
| Feeler stock 0.30 × 12.7 | leaf rates 0.12 / 0.15 / 0.18 N/mm | McMaster feeler-gauge stock [verify] | Precision Brand 0.012 × 1/2 in coil | ±0.005 mm thickness = ±5 % rate; trim free length in L2 |
| TPU 90A | seam sleeves must stretch over the nose | Other 90A brands | Print service TPU | 95A only for bumpers and pads |

Spares already in this BOM: springs (2), fuse (9), MGN9C block (1), shoulder screw (1), D61 (2), membrane sheet (3 more boots), feeler stock (1 rig strip + 1 wand strip), 6 × 2 mm magnets (47), 623ZZ (8), 625-2RS (9), inserts (45 M3, 32 M2), the second XL330 (6.33).

### E.10 Order checklist by vendor

| Vendor | S0 | S1 | S3 | BK | T | Subtotal | Shipping [est] | With shipping | Lead time |
|---|---|---|---|---|---|---|---|---|---|
| Amazon | $87.00 | $538.00 | $16.00 | $210.00 | $181.00 | $1,032.00 | $0.00 | $1,032.00 | 1–2 days (Prime) |
| Adafruit | $0.00 | $22.90 | $0.00 | $0.00 | $0.00 | $22.90 | $10.00 | $32.90 | 2–5 days |
| Robotis US | $0.00 | $64.13 | $27.49 | $0.00 | $0.00 | $91.62 | $10.00 | $101.62 | 2–5 days; order first |
| McMaster-Carr | $0.00 | $16.00 | $0.00 | $0.00 | $0.00 | $16.00 | $8.00 | $24.00 | same or next day ground |
| K&J Magnetics | $0.00 | $1.47 | $0.00 | $0.00 | $0.00 | $1.47 | $5.00 | $6.47 | 1–3 days |
| SendCutSend | $0.00 | $54.00 | $0.00 | $0.00 | $0.00 | $54.00 | $0.00 | $54.00 | 2–5 days [est] |
| Filament supplier | $54.00 | $25.00 | $0.00 | $0.00 | $0.00 | $79.00 | $0.00 | $79.00 | 1–2 days on Amazon |
| Hardware store | $0.00 | $41.00 | $0.00 | $30.00 | $46.00 | $117.00 | $0.00 | $117.00 | same day |
| **All vendors** | **$141.00** | **$762.50** | **$43.49** | **$240.00** | **$227.00** | **$1,413.99** | **$33.00** | **$1,446.99** | |

**Amazon ($1,032.00).** *Stage 0:* 5.03 magnets $9; 5.05 keeper discs $7; 5.06 feeler stock $8; 5.07 press-on nails $7; 5.08 nylon picks $5; 5.10 steel balls $5; 5.11 M3 × 8 $5; 5.12 CA $8; 5.13 epoxy $6; 5.14 abrasives $8; 5.15 nail files $4; 5.16 drill set $10; 5.17 marker and varnish $5. *Stage 1:* 2.01 monitor arm $36; 2.03 2020 extrusion $28; 2.04 bracket kit $15; 2.05 MGN9 rail + MGN9C $12; 2.06 spare block $8 (can wait); 2.08 623ZZ $7; 2.09 625-2RS $8; 2.11 Dyneema $12; 2.12 trim cord $5; 2.14 spring assortment $10 (optional); 2.20 wrist keeper discs $7; 2.21 feeler stock $8; 2.24 silicone sheet $10; 2.25 Sil-Poxy $14; 2.26 PTFE film tape $10; 2.27 bumpers $6; 2.28 isolation feet $10 (can wait); 2.30 face cradle $45; 2.31 cushion $20 (can wait); 3.01 M3 inserts $9; 3.02 M2 inserts $7; 3.03 M4 inserts $6; 3.04 screw assortment $20; 3.05 M3 × 14 $5; 3.06 M3 × 6 flat $5; 3.07 nylocs $8; 3.08 M2 assortment $9; 3.09 aluminium M3 $9; 3.10 nylon M3 $8; 3.11 thumbscrews $8; 3.15 zip ties $5; 5.04 6 × 3 magnets $6 (can wait); 5.09 1.0 mm nylon $5 (can wait); 6.03 fuses $5; 6.04 fuse holder $7; 6.05 1.25 A fuses $5 (optional); 6.06 e-stop $14; 6.08 button $8; 6.09 button cable $9; 6.11 Philmore $10 (optional); 6.13 1N5819 $5; 6.14 470 µF $5; 6.15 TVS $6; 6.19 pots $8; 6.20 toggle $7; 6.21 LED $5; 6.22 resistors $7; 6.23 100 nF $5; 6.24 22 AWG $12; 6.25 6-core $9; 6.26 heat-shrink $6; 6.27 sleeving $7; 6.28 Wago $9; 6.29 Dupont $8; 6.30 perfboard $7; 6.31 USB-C $8; 6.32 crimp terminals $10. *Stage 3:* 6.34 lazy-Susan $6; 6.35 load cell $10. *Bench kit:* 7.01 short real-hair head $32; 7.02 long head $32; 7.03 clamp $8; 7.04 Kanekalon wig $18; 7.06 foam head $7; 7.07 monofilament $5; 7.08 50 µm tape $6; 7.10 weights $12; 7.12 carbon paper $5; 7.13 ear plugs $5; 7.14 black cloth $6; 7.15 lint roller $4; 7.16 IR thermometer $18; 7.17 hygrometer $9; 7.18 loupe $8; 7.19 hair clips $5; 7.20 mirror $5; 7.22 spring scale $12; 7.23 ruler $5; 7.24 macro lens $10 (optional); 7.25 comb and tweezers $8. *Tools:* 8.02 iron $30; 8.03 insert tip $10; 8.04 solder $10; 8.05 calipers $15; 8.06 kitchen scale $12; 8.07 luggage scale $12; 8.08 multimeter $20; 8.09 hex keys $10; 8.13 deburring/files $18; 8.14 sandpaper $6; 8.15 polish $8; 8.17 stone $8; 8.18 cutters/stripper/screwdrivers $22; 8.19 crimp tool $20 (optional); 8.20 helping hands $12 (optional).

**Adafruit ($22.90):** 2.15 electromagnet $5.95; 2.16 fallback magnet $7.95 (optional); 6.01 brick $14.95; 6.02 jack adapter $2.00.
**Robotis US ($91.62):** 6.16 OpenRB-150 $28.64; 6.17 XL330 $27.49; 6.18 DXL cable $8.00; 6.33 second XL330 $27.49 (S3, recommended now).
**McMaster-Carr ($16.00):** 2.10 shoulder screws $6.00; 2.13 lift springs $10.00.
**K&J Magnetics ($1.47):** 2.19 D61 × 3.
**SendCutSend ($54.00):** 2.02 ballast plates $45 (can wait); 6.07 e-stop base plate $9.
**Filament supplier ($79.00):** 4.01 PETG bright $25; 4.03 TPU 90A $29 (S0); 4.02 PETG spool 2 $25 (S1).
**Hardware store ($117.00):** 2.07 hinge pin $4; 2.17 steel bar $8; 2.18 PTFE tape $2; 2.22 M8 washers $6; 2.29 baseboard $12 (optional); 2.32 oil $4; 2.33 threadlocker $6; 3.12 M4 lot $5; 3.13 M5 × 12/16 $6; 3.14 wood screws $3 (optional); 7.05 7 in foam ball $7; 7.09 rod $2; 7.21 safety glasses $8; 7.26 cleaning $9; 7.27 paint pen $4; 8.10 M5 tap $10; 8.11 drill bits $6; 8.12 mitre box and saw $18; 8.16 snips $12.
**No purchase needed:** zero pin (3.0 mm drill shank), tether-weight pulley (spare 623ZZ), hold-to-run housing and tip box (printed), phone apps (240 fps, SPL meter, inclinometer, timer).

---

## F. FABRICATED (3D-PRINTED) COMPONENTS

### F.1 General print rules

All parts PETG unless stated (IPA-wipeable; no PLA near skin), 0.4 mm nozzle, 0.2 mm layers unless stated. "W/I" = perimeters / infill. Inserts are brass heat-set (M3: 4.0 mm hole, 4 mm long; M2: 3.2 mm hole, 3 mm long; M4: 6 mm long, hole 5.6 mm [VERIFY on the insert kit]). Hole sizes are as printed; drill or ream where noted (Ø 6.3 hinge bores with a 1/4 in bit, Ø 5.0 cheek B bore with a 5.0 mm bit). Dimensions X × Y × Z are in the installed orientation. Clearance holes: M2 2.4, M3 3.4, M4 4.5, M5 5.5; thread-forming pilots M2 1.8, M3 2.6. Bed ≥ 220 × 220 mm (P21 lies 196 × 108; P32/P33 are 169 long). TPU 90A on a direct-drive extruder at 15–20 mm/s. Weigh every float part (P26–P34, paddles, bars, sleeves, tips) as it comes off the printer and log it against the §C.6 ledger. Print-test first: P15 (625 bearing fit), P2 (623 bearing fit), P13 (servo fit, only after the servo has arrived), P34 with a leaf scrap (groove grip), one paddle and one tip (TM1 tang fit).

### F.2 Printed parts P1–P48 (frame, float, hand, desk-side)

| # | Part | Qty | Mat. | X × Y × Z (mm) | Key features (mm) | Print orientation | W/I | Inserts | Post-processing | Mates with |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VESA adapter | 1 | PETG | 66 × 140 × 145 | 6 mm base plate; VESA 75 holes Ø 4.5 counterbored Ø 8 × 3; 2 hinge ears 10 thick × 28 tall reaching 60 to the Ø 6.3 pin bore at (X −60, Z 84); magnet arm with Ø 3.4 hole for the magnet's rear M3 and a Ø 20.4 × 2 locating counterbore; up-stop boss (M4 insert); 2 pulley bosses at Y ±60 with Ø 3.2 axle holes; 2 spring-anchor hooks at Z 30; tray seat with 4 M3 inserts; ribs 4 | base plate flat on the bed | 5 / 40 % | 4 × M3 (tray), 1 × M4 × 6 (up-stop) | ream pin bore Ø 6.3 | arm VESA plate + ballast stack, P5, P2, P3, magnet |
| P2 | Pulley sheave | 2 | PETG | Ø 16 × 5 | V-groove for 1 mm cord, bore Ø 10 for 623ZZ press fit | flat | 4 / 100 % | none | press bearing | P1, cords |
| P3 | Electronics tray | 1 | PETG | 32 × 36 × 92 | pocket for OpenRB-150 (approx 66 × 25 [VERIFY]) on 4 Ø 2.5 bosses, pocket for Wago 221-413 and the 30 × 20 rail perfboard, USB-C opening 12 × 7, cable slots 8 × 4 top and bottom | open side up | 3 / 20 % | 2 × M3 (lid) | none | P1, P4 |
| P4 | Electronics tray lid | 1 | PETG | 2 × 36 × 92 | vent slots 2 × 20, 2 × Ø 3.4, label recess | flat | 3 / 20 % | none | none | P3 |
| P5 | Frame hinge knuckle | 1 | PETG | 24 × 48 × 30 | Ø 6.3 pin bore along Y 8 above its base; 2020 socket 20.2 × 20.2 × 12 with 2 × M5 holes; PTFE-washer faces | bore axis horizontal, socket up | 6 / 50 % | none | ream Ø 6.3 | P1 ears, 2020 post |
| P6 | Keeper lever | 1 | PETG | 12 × 30 × 60 | clamps the post foot (2 × M5 T-nut); foot pad 30 × 30 with 25 × 25 × 3 recess for the steel keeper (epoxy + 2 × M3 × 6 countersunk); keeper face at r = 50 below the pin; reset-cord eyelet Ø 2.5 | lying on its side | 6 / 60 % | none | flatten keeper face on 400 grit on glass | P5, magnet |
| P7 | Cord bar | 1 | PETG | 12 × 140 × 12 | clamps the post at Z 148 (2 × M5 T-nut); cord eyelets Ø 2.5 at Y ±60 with bowline posts | flat | 5 / 50 % | none | round eyelet edges | post, cords |
| P8 | Frame yaw plate | 1 | PETG | 70 × 70 × 6 | 8 M3 inserts on Ø 56.6 at 45° spacing; 2 × M5 slots to the spine | flat | 5 / 50 % | 8 × M3 | none | spine, P9 |
| P9 | Carrier yaw plate | 1 | PETG | 70 × 70 × 6 | 4 × Ø 3.4 on a 40 × 40 square; 2 × M5 slots to the carrier beam | flat | 5 / 50 % | none | none | P8, carrier beam |
| P10 | Reset tab and spine end cap | 1 | PETG | 25 × 30 × 25 | caps the spine end, finger tab 25 × 20 with R 5 edges | tab flat | 4 / 30 % | none | none | spine |
| P11 | Drop leg, servo side (−Y) | 1 | PETG | 50 × 20 × 105 | 2020 end socket with M5 end-tap screw and 2 T-nut slots; leg 20 × 12 section ribbed; foot flange with 4 × M3 inserts for P13 | on its side | 5 / 40 % | 4 × M3 | none | carrier beam, P13 |
| P12 | Drop leg, idler side (+Y) | 1 | PETG | 50 × 20 × 105 | mirror of P11; foot with 2 M3 inserts and 2 slots for P15 | on its side | 5 / 40 % | 2 × M3 | none | carrier beam, P15 |
| P13 | Servo cradle | 1 | PETG | 30 × 30 × 44 | pocket 20.4 × 34.4 × 23.5 open at the horn face (+Y) and cable end; 2 × Ø 2.2 for M2 into the servo [VERIFY]; TPU-bumper lugs at ±32°; zero-pin bore Ø 3.1 | horn face up | 4 / 40 % | 2 × M3 (strap) | none | servo, P11, P14, P17 |
| P14 | Servo strap | 1 | PETG | 30 × 4 × 10 | 2 × Ø 3.4, 0.3 interference on the servo back | flat | 4 / 100 % | none | none | P13 |
| P15 | Idler housing | 1 | PETG | 30 × 14 × 40 | bore Ø 16.0 × 5 for the 625-2RS (press, 0.05 interference after test print), shoulder relief Ø 8; 2 × M3 slots ±1.5 in X and Z | bore axis vertical | 6 / 60 % | none | test-fit bearing | P12, bearing |
| P16 | Horn adapter disc | 1 | PETG | Ø 24 × 3 | 4 holes for the XL330 horn's M2 pattern [VERIFY], centre relief Ø 6 for the horn screw, 4 × Ø 3.4 on Ø 18 to cheek A | flat | 4 / 100 % | none | none | XL330 horn, P19 |
| P17 | Guard cap G2 (servo) | 1 | PETG | 60 × 40 × 30 | 2 mm shell under P13 and around the horn, 15° drafted sides, R 3 edges, cheek A passes ≥ 10 clear through ±32° | open side up | 3 / 20 % | none | sand edges | P13 |
| P18 | Guard cap G3 (idler) | 1 | PETG | 60 × 40 × 30 | mirror of P17 around P15 | open side up | 3 / 20 % | none | sand edges | P15 |
| P19 | Yoke cheek A (servo side) | 1 | PETG | 75 × 5 × 40 | 4 M3 inserts on Ø 18 for P16; zero-pin bore Ø 3.1 at θ = 0 against P13; stop lug; 2 × M3 inserts for P21 | flat (XZ plane on the bed) | 6 / 60 % | 6 × M3 | none | P16, P21 |
| P20 | Yoke cheek B (idler side) | 1 | PETG | 75 × 5 × 40 | Ø 5.0 reamed bore + M4 nut trap for the shoulder screw at the axis; 2 × M3 inserts for P21 | flat | 6 / 60 % | 2 × M3 | ream Ø 5.0 | shoulder screw, P21 |
| P21 | Yoke crossbar with rail mast | 1 | PETG | 17 × 196 × 108 | box beam 196 × 16 × 16, 2 mm walls; mast 24 × 5 from Z 64 to an R 90 arc about the axis; 5 M3 inserts at 20 pitch for the rail; 1 mm rail reference lip on the −Y edge; holes for P22–P24, P27 | mast face down, beam along the bed X | 5 / 40 % | 5 × M3 (rail) + 8 × M3 (stops, shroud, cleat) | check mast face flat to 0.1 with a straightedge, sand if needed | P19, P20, rail, P22–P24, P27 |
| P22 | Rail shroud G4 | 1 | PETG | 16 × 34 × 50 | U-channel, 2 walls, closed bottom, 25 wide slot for the riser, dovetail for P25 | open side up | 3 / 20 % | none | sand edges R 3 | P21, P25 |
| P23 | Rail down-stop block | 1 | PETG | 12 × 20 × 8 | 1 × M3 brass insert vertical for the thumbscrew; 2 × Ø 3.4 to the mast | flat | 6 / 100 % | 1 × M3 | none | P21, thumbscrew |
| P24 | Rail up-stop block | 1 | PETG | 12 × 20 × 8 | 2 mm TPU pad recess; 2 × Ø 3.4 to the mast | flat | 6 / 100 % | none | glue TPU pad | P21 |
| P25 | Float scale strip | 1 | PETG | 2 × 8 × 45 | dovetail, 1 mm ridges 0.4 wide, 5 mm long ticks, numerals 0/10/20/30, M3 lock screw slot | flat, face up, 0.12 mm layers | 3 / 100 % | none | ink the ticks | P22 |
| P26 | Carriage riser (L-bracket) with pointer and trim hook | 1 | PETG | 32 × 20 × 34 | plate 20 × 34 × 3 with 4 × Ø 3.4 on 15 × 10 [VERIFY]; arm 32 × 12 × 4 to P28 (2 × Ø 3.4); foot tab for the down-stop; pointer fin 0.6 edge; trim hook | on its side | 4 / 30 % | none | none | MGN9C block, P28 |
| P27 | Trim cleat | 1 | PETG | 10 × 16 × 12 | cord channel 1 mm, M3 clamp thumbscrew into an insert | flat | 4 / 50 % | 1 × M3 | none | P21, trim cord |
| P28 | Upper wrist seat with weight post | 1 | PETG | Ø 44 × 39 | plate Ø 44 × 5; conical recess Ø 18.4/12.4 × 3.1; D61 pocket Ø 9.6 × 1.6 at the floor; key slot 3.3 × 2.2; post Ø 8.0 × 34 with M3 insert at the top; load-cell pocket 41 × 13 × 8 with filler P47; tether eyelet Ø 2 | seat face down, post up | 3 / 15 % | 1 × M3 | sand seat face flat on glass | P26, P33, P29 |
| P29 | Weight cap | 1 | PETG | Ø 16 × 4 | Ø 3.4 hole, finger knurl | flat | 3 / 50 % | none | none | P28 |
| P30 | Knuckle plate | 1 | PETG | 64 × 90 × 8 (spherical cap, 1.6 thick) | underside R 90; shared slot 47.8 × 74.8 (union of 31.8 × 26.8 at (∓8, ∓24) and 34.8 × 29.8 at (0, 0), R 4 corners); slot edge R 1.5 with 15° lead-in; perimeter R 3; 6 × Ø 2.4 | convex side up: print the underside as the top surface, 0.12 mm layers, ironing on (a supported underside is not acceptable) | 3 / 30 % | none | 400 grit then buff, Ra ≤ 0.8 µm; IPA wipe | P31, boot, P32 |
| P31 | Boot clamp frame | 1 | PETG | 60 × 86 × 1.2 | ring following the slot + 8 flange, 6 × Ø 2.4 | flat | 3 / 100 % | none | none | P30, boot |
| P32 | Palm tray | 1 | PETG | 52 × 169 × 28 | walls 0.8 with 1.2 ribs; 3 root blocks with β tilt (L 4.4°, C 4.7°, R 5.0°), 12.9 × 1.0 slots 3 long, 24.2 × 8.4 windows, floors at Z 44.1 / 56.7 / 44.0; 3 stop beams each with 1 M3 insert (L at Y −34, X −11; C at Y −10, X 0; R at Y +34, X +8); 6 M2 inserts for root bars, 6 for the lid, 6 for P30 | upside down (lid face on the bed) | 2 / 15 % (4 perimeters locally at root blocks) | 3 × M3, 18 × M2 | none | P30, P33, leaves, P34 |
| P33 | Palm lid with lower wrist seat | 1 | PETG | 52 × 169 × 9 | 1.6 top, 2 lap skirt; seat ring Ø 40/30; cone Ø 18/12 × 3 with keeper recess Ø 12.2 × 1.5; key peg Ø 3 × 2 hemispherical at r 17 on +X; tether cup Ø 12 × 6 and eyelet; 6 × Ø 2.4 | top face down | 2 / 15 % | none | sand seat land flat | P32, P28 |
| P34 | Root clamp bar | 3 | PETG | 24 × 8 × 3 | groove 12.9 × 0.25; 2 × Ø 2.4 at ±8.6 | groove up | 4 / 100 % | none | none | P32, leaves |
| P35 | Boot cutting template | 1 | PETG | 76 × 104 × 1 | outline of slot + 8 flange; 3 hole windows at 70 % of paddle section; alignment marks | flat | 2 / 100 % | none | none | silicone sheet |
| P36 | Cable clip | 6 | PETG | 12 × 10 × 8 | 2020 T-slot snap, 5 mm cable loop, zip-tie slot | flat | 3 / 100 % | none | none | 2020, DXL cable, reset cord |
| P37 | Control panel box | 1 | PETG | 100 × 60 × 40 | 2 × Ø 7.2 pot holes with anti-rotation slots, 1 × Ø 6.2 toggle hole, 1 × Ø 5.2 LED hole, 0/50/100 % tick recesses around each pot, cable gland Ø 6, 4 corner M3 inserts, rubber-foot recesses | face down | 3 / 20 % | 4 × M3 | none | P38, pots, toggle, LED |
| P38 | Control panel lid (base) | 1 | PETG | 100 × 60 × 2 | 4 × Ø 3.4, 4 × Ø 10 foot recesses | flat | 3 / 20 % | none | none | P37 |
| P39 | Handheld button housing, half A | 1 | PETG | Ø 36 × 110 (half) | split along the axis; top cup: 36 rim, 2 mm rim wall, button deck 2.0 thick with Ø 29.6 hole [VERIFY against the uxcell 30 mm button], deck placed so the button face is 3.0 below the rim; 2 × Ø 3.4 counterbored; half of the gland boss Ø 12 × 10 with Ø 6 cable bore; zip-tie anchor bar 8 above the gland | split face down | 3 / 25 % | none | sand rim R 2 | P40, button, cable |
| P40 | Handheld button housing, half B | 1 | PETG | Ø 36 × 110 (half) | mirror of P39 with 2 M3 inserts; alignment pins Ø 3 × 3 | split face down | 3 / 25 % | 2 × M3 | sand rim R 2 | P39 |
| P41 | Cradle foot cup | 4 | PETG | Ø 40 × 12 | Ø 30.4 × 8 cup for the rubber foot, 2 × Ø 3.4 countersunk for wood screws | flat | 3 / 30 % | none | none | baseboard, rubber feet |
| P42 | Cradle tilt wedge | 2 | PETG | 120 × 60 × 32 | 15° wedge, anti-slip ribs, 2 mm TPU pad recess | flat face down | 3 / 20 % | none | glue pads | face cradle feet |
| P43 | Apex height gauge | 1 | PETG | 12 × 12 × 120 | rounded foot R 6; engraved rings at 80/82/84/86/88 from the foot | lying flat | 3 / 30 % | none | ink rings | scalp / foam head, cheek A mark |
| P44 | Reset cord toggle | 1 | PETG | Ø 14 × 40 | cord bore Ø 2.5, knot pocket | lying | 3 / 50 % | none | none | reset cord |
| P45 | Reset cord guide | 1 | PETG | 15 × 20 × 15 | screws to the magnet arm (2 × M3 × 10 with nuts [verify]); Ø 3 polished cord channel, R 3 entry | flat | 4 / 50 % | none | none | P1, reset cord |
| P46 | Tip-height pull clip (for L6a) | 1 | PETG | 18 × 13 × 20 | loop that slips over the centre seam sleeve, hook eye at nail height | flat | 3 / 100 % | none | none | fish scale |
| P47 | Load-cell filler bar (Stage 1) | 1 | PETG | 40 × 12 × 6 | 2 × Ø 3.4 matching P26 and P28 | flat | 5 / 100 % | none | none | P26, P28 |
| P48 | Tip box with slots | 1 (only if the tip lead's box is not printed; §G supplies one, so normally **not printed**) | PETG | 120 × 60 × 25 | 8 slots 11 × 5 for TM1 tangs, label recesses for blinding codes | flat | 2 / 15 % | none | none | tips |

Small TPU 90A pieces implied by the table and generated by the frame CAD: 2 × servo-stop bumpers (on P13 lugs), 1 × up-stop pad (P24 recess, 2 mm), 2 × wedge pads (P42); plus a P15S idler spacer that the CAD agent found necessary (see cad/frame/CONFLICTS.md).

**Count:** 48 part designs, 60 printed pieces (P2 × 2, P34 × 3, P36 × 6, P41 × 4, P42 × 2, all others × 1), plus the 9 tip-lead pieces for the hand (T1–T4) and the tips. Estimated filament: 0.9 kg PETG, 20 g TPU.

### F.3 Tip-lead printed parts for the hand and wand (T1–T4, wand, tips)

| Ref | STL | Setting | Qty SP1 hand | Qty wand | Mass each [EST] | Print |
|---|---|---|---|---|---|---|
| T1 | `paddle_with_pocket.stl` | `RISER = 0`, outer paddle (L, R) | 2 | 1 + 1 spare | 4.5–5.5 g (hand), about 8 g (wand) | nose up, root block on the bed; **pause at 23.1 mm print height** (model z 11.9) and drop the N52 6 × 2 magnet into the Ø 6.2 recess with a dot of CA, any polarity |
| T2 | `paddle_with_pocket_riser9.stl` | `RISER = 9`, centre paddle (C) | 1 (+1 spare) | 0 | 5.7–6.7 g | nose up; **pause at 32.1 mm print height**; mark "C" on its root block (it is 9 mm taller and must sit on C only) |
| T3 | `paddle_clamp_bar.stl` | | 3 | 1 | 0.7 g | groove up |
| T4 | `tm1_seam_sleeve.stl` (TPU 90A) | 10° nose (post-addendum; a sleeve printed for the old 5° paddle is 0.5 mm narrower and must not be used) | 3 + 2 spares | 1 + 1 spare | 0.4 g | standing, bottom (z −5.5) end on the bed, 2 perimeters (0.8 mm wall) |
| — | `hand_wand_handle.stl` | | 0 | 1 | | PETG or PLA, flat, window up, 3 perimeters, 15 % |
| — | `hand_wand_clamp_bar.stl` | | 0 | 1 | | groove up, 100 % |
| — | tips `tip_W`, `tip_B45`, `tip_B45_12`, `tip_A45`, `tip_E_carrier` (+`tip_E_pad` TPU, `tip_E_blade` template), `tip_H_ball`, `tip_P_carrier` | see §G.3 | 3 of the session tip + duplicates of every tip compared blind (at least W, B45, H, A45, P × 2) | W × 2, B45 × 2, H, A45, P × 2 | 1.6–2.2 g | see §F.4 |

Hand paddles print at **2 perimeters, 10 % gyroid, with a slicer modifier giving 4 perimeters around the two screw holes** (mass budget). Wand paddles print at 4 perimeters, 30 %. The two paddle kinds are identical below z 25 (nose, pocket, magnet recess, drafted body, section at the knuckle plate), so every tip and sleeve fits both.

### F.4 Tip print settings (cad/tips/README §3)

All tips in ONE bright colour of PETG (orange or yellow): fragments must be visible in dark hair, and a colour difference between tips would break the blinding. PLA never touches the scalp.

| Part | Material | Layer | Orientation on the bed | Walls / infill | Supports | Notes |
|---|---|---|---|---|---|---|
| tip_W, tip_B45, tip_B45_12 | PETG | 0.10 mm | **ON ITS SIDE**: model Y vertical (rotate 90° about X), band −Y face on the bed; the edge line then runs up the print and its cross-section is traced by the perimeters (no layer staircase across the edge; the plate bends in-plane, not across layer bonds) | 3 perimeters, 100 % | under the tang (2.5 mm gap) and, for B45-12, under the band (1.5 mm); support Z gap 0.2 mm; nothing on the working faces | slow outer wall (20 mm/s), seam on the tang end, never on the edge |
| tip_A45, tip_P_carrier, tip_E_carrier, tip_H_ball | PETG | 0.10 mm | tang DOWN, working end up | 3 perimeters, 100 % | none (cone 39° and 45° overhangs; bonding faces face up) | carriers: the edge is sheet stock, so orientation does not shape it |
| tip_E_pad | TPU 90A | 0.20 mm | lying on a Y face (dovetail and 45° chamfer in the print plane) | 3 perimeters, 100 % | none | 15–20 mm/s, direct drive |
| tip_E_blade | 1.0 mm nylon sheet or pick | | print the STL flat in any filament only as a scribing template | | | never use a flat-printed blade at the scalp (its edge would be a layer staircase) |
| paddle_with_pocket, paddle_with_pocket_riser9 | PETG | 0.20 mm (0.16 for a crisper pocket) | NOSE UP, root block on the bed | hand: 2 perimeters, 10 % gyroid, 4 perimeters around the screw holes; wand: 4 perimeters, 30 % | none (window floor and leaf slots are 8.4 and 12.9 mm bridges; the 3 mm transition flares 32° from vertical, printable) | PAUSE at 23.1 mm (`RISER = 0`) or 32.1 mm (`RISER = 9`), drop in the magnet with a dot of CA; check in the slicer preview that the next layer starts to roof the recess |
| paddle_clamp_bar, hand_wand_clamp_bar | PETG | 0.20 mm | groove side up | 100 % | none | |
| tm1_seam_sleeve | TPU 90A | 0.20 mm | standing, bottom end on the bed | 2 perimeters (0.8 mm wall) | none | |
| hand_wand_handle | PETG or PLA | 0.20–0.28 mm | flat, window up | 3 perimeters, 15 % | none (leaf slot ceiling is a 12.9 mm bridge) | |

Paddle fasteners: M3 × 8 socket or button head, thread-forming into the 2.6 mm holes (set `SCREW_HOLE_D = 4.0` in the SCAD for heat-set inserts); two per paddle bar, four per wand bar; on the SP1 hand use aluminium M3 × 8 at 0.3 N·m. Keep the paddle band at z 26–28 clean (no CA, varnish or slicer seam: put the seam on a +X or −X corner) because the silicone boot bonds there.

### F.5 File index

**Tips and paddles: `05-engineering/cad/tips/` (exists; SCAD is the source of truth, `gen_tips_stl.py` is a Python mirror that regenerates `stl/` with numpy + trimesh 5.x + manifold3d and checks every mesh is watertight and inside its expected bounding box; with OpenSCAD installed `openscad -o stl/tip_W.stl tip_W.scad`, `openscad -D 'PART="pad"' -o stl/tip_E_pad.stl tip_E_carrier.scad`, `openscad -D 'RISER=9' -o stl/paddle_with_pocket_riser9.stl paddle_with_pocket.scad`).** Frame used in every tip file: +Z into the pocket (toward the leaf), −Z toward the scalp, X = stroke, Y = across; origin = centre of the pocket-mouth plane; the working edge of W/B45/B45-12/A45 is 12.5 mm below the mouth.

| Part | .scad | .stl | bbox X × Y × Z (mm) | z range | volume (mm³) |
|---|---|---|---|---|---|
| TM1 library (tang, shoulder, band, pocket negative, B45 blade module) | `cad/tips/tm1_tang_lib.scad` | (include only) | | | |
| Tip W | `cad/tips/tip_W.scad` | `cad/tips/stl/tip_W.stl` | 14.00 × 9.00 × 24.50 | −12.50 to 12.00 | 1428.8 |
| Tip B45 | `cad/tips/tip_B45.scad` (`BLADE_MODE = "slot"` for a 1.0 mm sheet blade carrier) | `cad/tips/stl/tip_B45.stl` | 14.00 × 9.00 × 24.50 | −12.50 to 12.00 | 1299.2 |
| Tip B45-12 | `cad/tips/tip_B45_12.scad` | `cad/tips/stl/tip_B45_12.stl` | 14.00 × 12.00 × 24.50 | −12.50 to 12.00 | 1335.2 |
| Tip A45 carrier (gated) | `cad/tips/tip_A45.scad` | `cad/tips/stl/tip_A45.stl` | 14.00 × 9.00 × 21.67 | −9.67 to 12.00 | 1227.4 |
| Tip H ball | `cad/tips/tip_H_ball.scad` (`PRINTED_BALL = true` prints the ball solid) | `cad/tips/stl/tip_H_ball.stl` | 14.00 × 9.00 × 23.00 | −11.00 to 12.00 | 1326.6 |
| Tip E carrier / pad / blade | `cad/tips/tip_E_carrier.scad` (`PART = "carrier" / "pad" / "blade" / "assembly"`) | `cad/tips/stl/tip_E_carrier.stl`, `tip_E_pad.stl`, `tip_E_blade.stl` | 14.00 × 9.00 × 20.51 / 10.00 × 10.00 × 7.84 / 8.00 × 9.00 × 1.00 | −8.51 to 12.00 / −14.50 to −6.66 / 0 to 1.00 | 1226.1 / 493.2 / 68.2 |
| Tip P carrier | `cad/tips/tip_P_carrier.scad` | `cad/tips/stl/tip_P_carrier.stl` | 14.00 × 9.00 × 23.50 | −11.50 to 12.00 | 1440.7 |
| T1 paddle, outer | `cad/tips/paddle_with_pocket.scad` (`PART = "paddle"`, `RISER = 0`, `DRAFT_Y = 10`) | `cad/tips/stl/paddle_with_pocket.stl` | 28.00 × 17.82 × 35.00 | 0 to 35.00 | 8814.8 |
| T2 paddle, centre | same, `RISER = 9` | `cad/tips/stl/paddle_with_pocket_riser9.stl` | 28.00 × 17.82 × 44.00 | 0 to 44.00 | 12465.5 |
| T3 paddle clamp bar | same, `PART = "bar"` | `cad/tips/stl/paddle_clamp_bar.stl` | 24.00 × 8.00 × 3.20 | 0 to 3.20 | 531.2 |
| T4 seam sleeve (TPU) | same, `PART = "sleeve"` | `cad/tips/stl/tm1_seam_sleeve.stl` | 15.86 × 10.86 × 8.50 | −5.50 to 3.00 | 352.4 |
| Wand handle | `cad/tips/hand_wand_handle.scad` (`PART = "handle" / "bar" / "assembly"`) | `cad/tips/stl/hand_wand_handle.stl` | 28.00 × 180.00 × 16.00 | 0 to 16.00 | 63237.3 |
| Wand clamp bar | same, `PART = "bar"` | `cad/tips/stl/hand_wand_clamp_bar.stl` | 24.00 × 24.00 × 3.20 | 0 to 3.20 | 1650.9 |

**Frame, float, hand and desk-side parts: `05-engineering/cad/frame/`** — being generated in parallel by the CAD agent. The generator `cad/frame/gen_frame_stl.py` exists now and writes one STL per piece P1–P48 into `cad/frame/stl/` (plus the three TPU pads and the P15S idler spacer), runs the §C.1 swept-volume, §B.5 gap and float/lift checks on the solids (stdout and `stl/checks.txt`), and exits non-zero if any mesh is not watertight or outside its expected bounding box. **The SCAD files are the source of truth** (`sp1_frame_lib.scad` shared constants + one `pNN_<name>.scad` per part or part group). Parts on the module are written in their installed position in the global frame (so the STLs load together as the assembly) and are rotated in the slicer per `cad/frame/README.md`; desk-side parts (P35, P37–P44, P46, P48) use a local frame. **When the frame CAD lands, read `cad/frame/README.md` and `cad/frame/CONFLICTS.md` before printing** — CONFLICTS.md records every place the CAD had to deviate from mechanical.md (C-F1 is the post length, see Appendix 1 note 1). File names confirmed from the generator header are marked (confirmed); the rest follow the same naming pattern and are **expected names** to be checked against the README:

| Part(s) | Expected .scad | Expected .stl (in `cad/frame/stl/`) |
|---|---|---|
| shared constants | `sp1_frame_lib.scad` (confirmed) | — |
| P1 | `p01_vesa_adapter.scad` (confirmed) | `p01_vesa_adapter.stl` |
| P2, P5, P6, P7, P10, P44, P45 | `p02_p07_hinge_parts.scad` (confirmed) | `p02_pulley_sheave.stl`, `p05_hinge_knuckle.stl`, `p06_keeper_lever.stl`, `p07_cord_bar.stl`, `p10_reset_tab.stl`, `p44_reset_toggle.stl`, `p45_reset_cord_guide.stl` |
| P3, P4 | `p03_p04_electronics_tray.scad` (confirmed) | `p03_electronics_tray.stl`, `p04_tray_lid.stl` |
| P8, P9 | `p08_p09_yaw_plates.scad` | `p08_frame_yaw_plate.stl`, `p09_carrier_yaw_plate.stl` |
| P11, P12 | `p11_p12_drop_legs.scad` | `p11_drop_leg_servo.stl`, `p12_drop_leg_idler.stl` |
| P13, P14, P15 (+P15S), P16 | `p13_p16_elbow_parts.scad` | `p13_servo_cradle.stl`, `p14_servo_strap.stl`, `p15_idler_housing.stl`, `p15s_idler_spacer.stl`, `p16_horn_disc.stl` |
| P17, P18 | `p17_p18_guard_caps.scad` | `p17_guard_cap_servo.stl`, `p18_guard_cap_idler.stl` |
| P19, P20, P21 | `p19_p21_yoke.scad` | `p19_cheek_a.stl`, `p20_cheek_b.stl`, `p21_crossbar_mast.stl` |
| P22, P23, P24, P25, P27 | `p22_p27_rail_parts.scad` | `p22_rail_shroud.stl`, `p23_down_stop.stl`, `p24_up_stop.stl`, `p25_scale_strip.stl`, `p27_trim_cleat.stl` |
| P26, P28, P29, P47 | `p26_p29_float_parts.scad` | `p26_riser.stl`, `p28_upper_seat.stl`, `p29_weight_cap.stl`, `p47_filler_bar.stl` |
| P30, P31, P35 | `p30_p31_knuckle_plate.scad` | `p30_knuckle_plate.stl`, `p31_boot_frame.stl`, `p35_boot_template.stl` |
| P32, P33, P34 | `p32_p34_palm.scad` | `p32_palm_tray.stl`, `p33_palm_lid.stl`, `p34_root_clamp_bar.stl` |
| P36 | `p36_cable_clip.scad` | `p36_cable_clip.stl` |
| P37, P38 | `p37_p38_control_panel.scad` | `p37_panel_box.stl`, `p38_panel_lid.stl` |
| P39, P40 | `p39_p40_handheld_button.scad` (electronics-firmware.md calls it `cad/handheld_button.scad`; the frame CAD owns it) | `p39_button_half_a.stl`, `p40_button_half_b.stl` |
| P41, P42, P43 | `p41_p43_cradle_aids.scad` | `p41_foot_cup.stl`, `p42_tilt_wedge.stl`, `p43_apex_gauge.stl` |
| P46 | `p46_pull_clip.scad` | `p46_pull_clip.stl` |
| P48 | `p48_tip_box.scad` | `p48_tip_box.stl` (normally not printed) |
| TPU pads | in the part files | `tpu_servo_bumper.stl` (× 2), `tpu_upstop_pad.stl`, `tpu_wedge_pad.stl` (× 2) |

**Firmware: `05-engineering/firmware/sp1_scratch/sp1_scratch.ino`** (+ `firmware/README.md`).

---

## G. SCRATCHING TIPS, TM1 MOUNT AND THE STAGE-0 HAND WAND

### G.1 The SP1-TM1 mount as built

Origin = centre of the pocket-mouth plane; +Z into the pocket.

| Feature | Value | Note |
|---|---|---|
| Tang section | 10.0 (X) × 4.0 (Y) mm | |
| Tang length | 12.0 mm (z 0 to 12.0) | |
| Orientation key | 2.0 × 45° chamfer on the +X+Y corner, full length | a mirrored tip cannot enter |
| Tang end chamfer | 0.5 mm all round | insertion lead-in |
| Pocket section | 10.3 × 4.3 mm (0.15 mm clearance per side), matching key chamfer | |
| Pocket depth | 12.5 mm | tang bottoms on the magnet at 12.0 |
| Pocket mouth lead-in | 0.6 mm chamfer | |
| Magnet recess | Ø 6.2 mm, z 11.9 to 14.0 | captured by 0.85 mm ledges of the pocket walls; dropped in at the print pause |
| Magnet | N52 6 × 2 mm disc, axial | |
| Steel keeper | 6.0 × 3.9 × 1.0 mm slug (or a 6 × 1 disc with two flats filed to 3.9) in a through-notch at the tang end, bonded flush (epoxy or gel CA) | a round 6 mm disc cannot fit a 4.0 mm tang; covers 76 % of the magnet face |
| Shoulder | cone from the tang section at z 0 to a 14 × 9 mm (R 1 corners) band at z −2.5; band to z −5.5 | band = paddle nose size, carries the seam sleeve |
| Working part | below z −5.5; edge of W, B45, B45-12, A45 at z −12.5 | |
| Heavy-tip option TM1-B | M3 cross-bolt at z 6.0 (not used in SP1) | |

Normal scratch force pushes the tip deeper and never loads the magnet; drag is carried by the 12 mm deep pocket walls. **Axial breakaway** F = F_rated (≈ 8 N for an N52 6 × 2 on thick steel [EST]) × 0.76 (slug area) × ~0.7 (1 mm keeper saturates [EST]) × 0.8–1.0 (gap [EST]) + 0.5–1.5 N (sleeve grip [EST]) ≈ **4–6 N**, inside the 4–8 N spec at its low end; measured in L6(b). Below 4 N: N52 6 × 3 mm magnet (`TM1_MAG_H = 3.0`, +35 % [EST]); above 8 N: one 0.1 mm tape layer on the slug (−15–20 % per 0.1 mm [EST]) or a 5 × 2 magnet. Loads that pull a tip out in use (tip weight 0.02 N, stroke inertia 0.01 N) are > 100× below any hold; the breakaway only backstops bundle snags (one anagen hair pulls out at about 0.36 N [KNOWN], far below the magnet), so the primary hair protection is geometric and the rig's wrist breaks away at 2.0 N.

**Seating:** align the key chamfer with the chamfered pocket corner, push until the magnet pulls the last millimetre home with a click, press on the working part to confirm no rock; a tang that stops short of 12.0 is the wrong way round or has varnish or a support scar. **Release:** grip the working part and pull straight along the axis with 4–6 N; no tool, under 10 s. **Seam sleeve:** the V-gap between the paddle nose face and the tip shoulder (0.15 mm at the mouth to 2.5 mm at the band) is exactly the forbidden 0.04–3 mm range, so a TPU 90A sleeve (0.8 mm wall, 0.2 mm interference per side) is stretched over the drafted nose and covers z +3.0 down to z −5.5; outline 15.2 × 10.2 at the bottom, 15.9 × 10.9 at the top (10° nose); one dot of gel CA at the sleeve's top rim keeps it on the nose when a tip is pulled. Probe it with the 100 µm monofilament at every tip change.

### G.2 Tip family

Every edge is crowned (R 9 mm, index-nail value), so the loaded edge grows with indentation: about 4 mm at 0.3 N [EST], full width at about 1 mm. Measured on day 0 with the ink-mark test.

| Code | Geometry | Loaded edge (at 0.3 N) | Edge radius | Width | Material | Sensory variable it isolates | Stage gate |
|---|---|---|---|---|---|---|---|
| **W** | symmetric wedge, two 45.7° faces (88.6° included), R 9 crown, plan corners R 1.5; 1.8 g | about 4 mm [EST], 8 max | **0.4 mm** | 8 mm | PETG, printed on its side | DEFAULT; a symmetric edge so both senses of the bidirectional rake are identical scratches | Stage 0 wand and first human session (H0, H1) |
| **B45** | 1.0 mm plate at 45° toward +X from an R 0.5 edge, pulp lump behind; open 68° V on the −X side (edge-first stroke drives hair up the plate into it); 1.65 g | about 4 mm [EST], 8 max | 0.5 mm (full half-round of the plate) | 8 mm | PETG, on its side | nail-like thin plate vs wedge at similar radius; stroke-sense asymmetry (plate-first +X vs edge-first −X) | Stage 0 wand; Stage 1 human sessions |
| **B45-12** | as B45, 12 mm plate, lump 9 mm; 1.70 g | about 4 mm [EST], 12 max (needs 2.2 mm indentation) | 0.5 mm | 12 mm | PETG, on its side | width: hair collection ahead of the plate, loaded length at higher force | Stage 2 matrix (after B45 is characterised) |
| **A45** | 0.8 mm nylon sheet (Dunlop 0.88 pick filed flat) cut 8 × 9 with a convex R 9 end, edge filed to R 0.3, CA-bonded on a true 45° carrier face with its top butted under the band; edge at z −12.5; 1.56 g + 0.07 g | 4–5 mm [EST] | **0.3 mm** | 8 mm | nylon 6/6 on PETG | radius 0.3 vs 0.5 at constant geometry (vs B45) | **GATED:** L9 tape test at 2.4 N and L10 forearm sharpness < 7 at 0.6 N first; then W1 and W2 only, never W3 |
| **E** | B45 geometry: 1.0 mm nylon blade (8 × 9, R 9 end, 2.0 mm overhang) CA-bonded on the 45° face of a TPU 90A pad (10 × 10 × 6 block on a 4.7/6.7 × 1.85 dovetail rail, slid in along Y with a drop of CA) in a 3.0 mm drafted carrier block; **edge 4.0 mm lower than W (z −16.5): set the float down-stop 4.0 mm higher for E**; carrier 1.56 g, pad 0.60 g, blade 0.08 g | 4–5 mm [EST] | 0.5 mm | 8 mm | nylon blade, TPU 90A pad, PETG carrier | soft backing behind the edge (damping of chatter, a less "ringing" contact), **not** macroscopic compliance (the pad is ~1000× stiffer than the leaf) | Stage 2, only after B45 is characterised |
| **H** | 3.0 mm chrome-steel ball CA'd into an R 1.55 cup at the end of a drafted cone (Ø 4.0 at z −11.0); ball bottom z −12.8 (0.3 mm below W); 1.68 g + 0.11 g | contact circle about 4 mm (Hertz, 0.3 N) | 1.5 mm (sphere) | 3 mm | G25 ball in PETG | edge vs no edge: the **massager control** every edge tip must beat; every blind pair starts against H | Stage 0 control |
| **P** | trimmed ABS press-on nail (two nested, wicked with thin CA, total 10 mm long, free edge rolled to R 0.4–0.5, plan corners R 1–1.5) gel-CA'd concave-down on a convex R 8.5 bed rising toward +X at 45°, gel CA under the overhang (≤ 3 mm unsupported), root fillet; edge about z −14.3 (one nail) / −15.0 (two); 1.83 g + 0.15 g | about 4 mm [EST] | 0.4–0.5 with two nested nails; 0.3 max with one | 8–9 mm | ABS on PETG | a real nail's shape and material vs the printed W and B45 | Stage 0 with nested nails; a single-thickness P is A45-class and gated |

All radii are post-finishing targets verified per §G.4. Nothing below R 0.4 goes on the scalp before the A45 gate is passed (red line 11). B45-family tips are direction-dependent; in bidirectional strokes their return is a back-of-blade glide, and the wig test L8.9 counts captures per stroke sense (any capture in the −X sense moves B45 to one-way use or to a filled V: `s_lump` 1.5 mm).

### G.3 Materials and assembly notes per tip

PETG for W, B45, B45-12 (a 1.0 mm plate scuffs and whitens rather than shattering, wear raises the radius, survives IPA; printed on its side at 0.10 mm, 3 perimeters, 100 %). Nylon 6/6 stock (not printed) for the A45 and E blades and B45 slot mode (sand the faying face with 240 grit and wipe with IPA before CA, or it will not bond). TPU 90A for the E pad and the sleeves (never forms an edge). Standard SLA resin is banned at the scalp (red line 9); PLA is excluded from every tip. Thin CA for nylon-to-PETG and nail-to-nail; gel CA for gap filling under the P overhang and the sleeve rim; 5-minute epoxy as the alternative for the steel keepers. Never let adhesive squeeze onto a working face: a cured drop at the edge is a burr. **Keeper:** 6 × 1 mm disc with two flats filed to 3.9 mm, or a 6.0 × 3.9 × 1.0 slug from 1 mm sheet, bonded flush in the tang-end notch. **H:** CA the ball into the cup (12 mm² bond; the glue is the retention). **A45:** cut, file the edge first (two blended 0.3 mm chamfers), then bond. **E:** pad into the dovetail along Y with a drop of CA; blade on the 45° face with 2 mm overhang. **P:** size 1–2 full-cover ABS press-on (8–9 mm wide, 0.6 mm thick); nest two, clamp 1 min; cut the cuticle end with flush cutters to 10 mm total; file the free edge square then roll to R 0.4–0.5; ABS crazes in IPA, so clean P with soap and water and treat it as a weekly consumable.

### G.4 Edge radius control and verification

**The failure that matters** is not a slightly wrong radius but a flat with two broken corners: a 1.0 mm plate end sanded flat and only softened at the corners is two edges of R 0.1–0.2, sharper than A45, although a caliper still reads 1.0 mm.

1. **Clean up.** Remove supports, brim and stringing; knock the seam zit off with a fresh blade, never on the edge; round the plan corners of every edge to R 1.5 with a nail file (180 then 240).
2. **Shape.** Wrap 400-grit wet-and-dry around a flat stick; stroke ALONG the edge (Y) while rolling the stick over the apex through the full included angle (90° for W; 180° over the plate end for B45, B45-12, E and P, so the end becomes one half-round tangent to both faces).
3. **Refine and polish.** Same rolling stroke with 600, 1000, 2000, wet, until no scratch is visible at 10× (Ra < 1 µm). PETG and ABS may get one optional 1 s pass of a lighter flame (no dwell); nylon gets plastic polish, never flame.
4. **Loupe check.** Edge-on beside drill-bit shanks on back-lit white card: 0.6 mm shank = R 0.3, 0.8 = R 0.4, 1.0 = R 0.5. The silhouette must be at least as round as its reference shank (W 0.8; B45/B45-12/E 1.0; P 0.8), one continuous arc, no flat. Phone macro photo next to a ruler, filed with the tip code. Sharper than the reference: sand again. Never sand a tip sharper to "hit" a number.
5. **Burr check.** Cotton ball dragged along the edge both ways (any snagged fibre marks a burr), then the back of the hand at about 1 N.
6. **Tape test (L9).** 10 mm rod wrapped with 3 layers of 50 µm polyester or PTFE tape; tip in the holder on the wand; press at 1.0 N, then 2.4 N (kitchen scale under the rod); slide 50 mm at about 50 mm/s, three passes each direction, both edge senses for 45° tips, then across the corners; inspect under the loupe. Pass: no cut through any layer at 2.4 N. A45 must pass at 2.4 N too or stays gated. Re-test after 10 sessions or any drop.
7. **Proof load (safety §3.6, addendum ruling 1).** 3× rated: about 7.5 N normal and 6 N lateral on the bench before first use; any tip that cracks, chips or whitens is discarded.
8. **Record** measured radius, test date and results against the tip's code on the key card.

Optional profile check: press the edge 1 mm into firm modelling putty, cut the impression across, view the cut face under the loupe against the shanks. **Wear:** PETG edges scuff and whiten (safe direction, but biases long A/B series): inspect under the loupe before every session (30 s), re-run the tape test after 10 sessions, replace any tip with a chip, crack, crazing, a visible wear step, or after about 10 h of use. Keep duplicates from one print batch.

### G.5 Blinding codes and the tip box

Every tip gets a random two-letter code drawn from the alphabet without W, B, A, E, H and P, never reused, written in 3 mm letters with the 0.3 mm marker on the tang's plain −Y face (inside the pocket, invisible when installed) and sealed with one thin coat of clear varnish; no stickers (0.15 mm pocket clearance). Make two copies of every tip compared blind (at least W, B45, H, A45, P), each with its own code. Key card (tip ID, print batch, measured radius, tape-test result, date) stays with the helper or in a sealed envelope; re-code every two weeks or when a tip is identified by accident. Tip box: one slot per tip, about 11 × 5 × 14 mm deep, labelled only with the code (printed block from spool 1, or a pill organiser with cut foam); lid closed during trials; the helper swaps tips out of Michael's sight.

### G.6 The Stage-0 hand wand

One TM1 holder (the standard `paddle_with_pocket` paddle with its pocket, magnet and seam sleeve) clamped to the free end of a 0.30 × 12.7 feeler leaf whose other end is clamped in a 150 mm printed handle (150 × 22 × 16 grip, R 8 corners, plus a 28 × 30 × 16 clamp block). Both clamps hold the leaf without holes: bar with a 0.25 mm locating groove, 4 × M3 × 8 in the handle (bar 24 × 24 × 3.2), 2 × M3 × 8 in the paddle (bar 24 × 8 × 3.2). The leaf runs along Y (the handle's axis) and the paddle hangs below its free end, so the wand strokes across its own axis (X), exactly as each nail on the rig. Same leaf part number as the rig: a tip, a force and a spring rate found on the wand are the rig's.

**Leaf:** 80 mm long: 27 mm in the handle block, 38 mm free (handle face to paddle −Y face), 14 mm through the paddle root, 1 mm to trim. Stiffness k = EI / (a³/3 + a²b + ab²), a = free length + 6, b = 4, EI = 5715 N·mm²:

| Free length (face to face) | 30 mm | 35 mm | **38 mm (default)** | 40 mm | 45 mm |
|---|---|---|---|---|---|
| k at the tip | 0.27 N/mm | 0.19 N/mm | **0.155 N/mm** | 0.14 N/mm | 0.10 N/mm |

At 0.155 N/mm the tip deflects 1.9 mm at 0.3 N, 3.2 at 0.5 N, 6.5 at 1.0 N and 15.5 mm at the 2.4 N per-nail cap (leaf root stress about 600 MPa, inside hardened feeler stock). The wand has no hard stop: force comes from scale practice and the visible leaf bend; a printed stop finger under the leaf is a 20-minute addition if practice proves unreliable.

**Building it in 3 hours** (prints run unattended the evening before, §0.2):

| Time | Step |
|---|---|
| 0:00–0:20 | Remove supports, clean prints. Test-fit every tang in the paddle pocket: slides home without force, cannot enter rotated. Sand any support scar on a tang face. |
| 0:20–0:45 | File flats on 6 × 1 mm steel discs to 3.9 mm (or cut slugs); bond one flush into every tang-end notch with epoxy or gel CA. CA the 3 mm ball into H. |
| 0:45–1:35 | Edge work per §G.4: W and B45 rolling-stroke sanding 400→2000; A45 nylon blade cut, filed to R 0.3 and bonded; P nails nested, trimmed, filed to R 0.4–0.5 and bonded. |
| 1:35–2:00 | Cut the leaf to 80 mm, round its corners R 1 and deburr both ends. Clamp it in the handle (bar, 4 × M3 × 8, snug, not crushing), set 38 mm free length, clamp the paddle (bar, 2 × M3 × 8). Trim any excess leaf flush with the paddle +Y face and cover the paddle root and leaf end with one turn of electrical tape (the wand root has open slots within reach of long hair). Fit the seam sleeve, dot of gel CA at its top rim. |
| 2:00–2:30 | Calibrate: press the tip onto the kitchen scale, read force at 2, 4 and 6 mm of deflection against a ruler; trim free length until k is 0.13–0.18 N/mm. Practise hitting 0.3 and 0.5 N on the scale ten times each (people press 2–3× too hard). Breakaway per L6(b) for each tip: 4–8 N. |
| 2:30–3:00 | Tape test (L9) and cotton-ball burr test for every tip; write blinding codes and fill the key card and tip box. |

**What to test with it, in order, before any motorised part is ordered:** (1) L9 tape test and L10a forearm screen per tip; A45 joins only after L9 at 2.4 N and sharpness < 7 at 0.6 N. (2) Loaded edge: ink the edge with whiteboard marker, press on the forearm or on carbon paper over 10 mm foam at 0.3 and 0.5 N, measure the mark (about 4 mm expected at 0.3 N). (3) Wig head L8.1 static reach and L8.9, 200 strokes per tip, B45 counted per stroke sense. (4) Scalp H0: 10 strokes per tip, 30–40 mm at about 80 mm/s and 0.3–0.5 N, crown then occiput, along and across the lie; side photo of contact fraction at 0.3 and 0.5 N; blind W vs H and B45 vs H with a helper swapping coded tips; preference among B45 +X, B45 −X and W bidirectional; P vs W as the "real nail" check. Also the M-pre measurements (hair length, grain map, density, human reference scratch).

**Go / no-go:** GO to Stage 1 when the nail visibly reaches skin through Michael's hair at ≤ 0.5 N, W or B45 clearly beats H on the scalp (≥ 3 points on realism, blind), and no tip captures hair in 200 wig strokes. NO-GO: fix the tip first; if no tip reaches the skin, the engagement, leaf and paddle questions go to the top of §P.

### G.7 Hygiene and wear

FDM parts are porous: scalp-contacting printed tips are weekly consumables. Each session: 70 % IPA wipe on PETG, nylon and steel with a 1-minute flash-off (IPA on freshly scratched skin stings); soap and water for ABS P; a soft brush through the B45 V and along the P root fillet (the two sebum crevices). Weekly: pocket cleaned with a pipe cleaner and IPA (sebum changes the breakaway); TPU sleeves and pads replaced when fouled or split. Count tips in and out of the box every session; pull-test every tip weekly (a debonded keeper, H ball or P nail are the things that could be lost into the hair; one bright colour makes them visible). One tip set per person.

---

## H. ELECTRONICS

### H.1 Wiring architecture in one sentence

One certified 5 V brick feeds **one series safety loop** — fuse → NC e-stop → NO hold-to-run — and only after that loop does the 5 V split into (a) the OpenRB-150 **Terminal VIN** (which is the DYNAMIXEL bus supply when the jumper is on `VIN(DXL)`) and (b) the **holding electromagnet**. The OpenRB-150 **logic runs from USB-C**, on the laptop side of the loop, so opening the loop kills the servo and drops the magnet while the MCU keeps logging. Nothing on the laptop side can energise anything on the rail side. The hardware loop is the primary barrier; the servo's own registers are the electrical second layer; the sketch is the third, never credited alone (red line 13).

Deviations from the freeze made by the electronics lead (flagged, accepted): a read-only **rail-sense input** (10 k/10 k divider to A2) so the firmware knows the rail state; **Status Return Level 2** (every write acknowledged; level 1 would make every write look like a timeout); **Current Limit (EEPROM 38) = 450 mA** as a second, firmware-independent ceiling above the 300 mA Goal Current; the sketch is 533 lines (test-lead hooks added).

### H.2 Schematic (copied from electronics-firmware.md §1.2)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="960" height="560" font-family="Helvetica, Arial, sans-serif" font-size="12">
  <defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
  <rect x="0" y="0" width="960" height="560" fill="#fff"/>
  <text x="12" y="20" font-size="14" font-weight="bold">SP1 actuator rail (hardware safety loop) and control wiring</text>
  <!-- rail band -->
  <rect x="12" y="40" width="936" height="190" fill="#fff4f4" stroke="#c33" stroke-dasharray="4 3"/>
  <text x="20" y="56" fill="#c33" font-weight="bold">ACTUATOR RAIL — everything inside this box is dead when the loop is open</text>
  <!-- adapter -->
  <rect x="24" y="90" width="110" height="60" fill="#fff" stroke="#333"/>
  <text x="79" y="112" text-anchor="middle">5 V 4 A brick</text><text x="79" y="128" text-anchor="middle" font-size="10">Adafruit 1466, UL</text><text x="79" y="142" text-anchor="middle" font-size="10">5.5×2.1 centre +</text>
  <!-- jack adapter + fuse -->
  <rect x="160" y="100" width="70" height="40" fill="#fff" stroke="#333"/><text x="195" y="117" text-anchor="middle" font-size="10">jack→screw</text><text x="195" y="131" text-anchor="middle" font-size="10">adapter</text>
  <rect x="255" y="100" width="70" height="40" fill="#fff" stroke="#333"/><text x="290" y="117" text-anchor="middle">FUSE</text><text x="290" y="131" text-anchor="middle" font-size="10">1 A fast 5×20</text>
  <!-- e-stop -->
  <rect x="350" y="90" width="90" height="60" fill="#fff" stroke="#c33" stroke-width="2"/><text x="395" y="112" text-anchor="middle" font-weight="bold">E-STOP</text><text x="395" y="127" text-anchor="middle" font-size="10">22 mm mushroom</text><text x="395" y="141" text-anchor="middle" font-size="10">NC, latching, boxed</text>
  <!-- hold to run -->
  <rect x="465" y="90" width="100" height="60" fill="#fff" stroke="#c33" stroke-width="2"/><text x="515" y="112" text-anchor="middle" font-weight="bold">HOLD-TO-RUN</text><text x="515" y="127" text-anchor="middle" font-size="10">NO momentary, handheld</text><text x="515" y="141" text-anchor="middle" font-size="10">1.5 m lead</text>
  <!-- split node -->
  <circle cx="600" cy="120" r="4" fill="#333"/>
  <!-- OpenRB VIN -->
  <rect x="650" y="70" width="130" height="50" fill="#fff" stroke="#333"/><text x="715" y="90" text-anchor="middle">OpenRB-150</text><text x="715" y="105" text-anchor="middle" font-size="10">Terminal VIN (+ / −)</text>
  <text x="790" y="78" font-size="9">470 µF + SMAJ5.0A</text><text x="790" y="90" font-size="9">at the terminal</text>
  <!-- magnet -->
  <rect x="650" y="150" width="130" height="60" fill="#fff" stroke="#333"/><text x="715" y="170" text-anchor="middle">ELECTROMAGNET</text><text x="715" y="185" text-anchor="middle" font-size="10">P20/15 5 V 0.22 A 25 N</text><text x="715" y="199" text-anchor="middle" font-size="10">1N5819 flyback ↑ across coil</text>
  <!-- servo -->
  <rect x="820" y="100" width="118" height="60" fill="#fff" stroke="#333"/><text x="879" y="120" text-anchor="middle">XL330-M288-T</text><text x="879" y="135" text-anchor="middle" font-size="10">ID 1 elbow (ID 2 yaw, St.3)</text><text x="879" y="149" text-anchor="middle" font-size="10">DXL port, FET-switched</text>
  <!-- wires rail -->
  <line x1="134" y1="120" x2="160" y2="120" stroke="#c33" stroke-width="2"/>
  <line x1="230" y1="120" x2="255" y2="120" stroke="#c33" stroke-width="2"/>
  <line x1="325" y1="120" x2="350" y2="120" stroke="#c33" stroke-width="2"/>
  <line x1="440" y1="120" x2="465" y2="120" stroke="#c33" stroke-width="2"/>
  <line x1="565" y1="120" x2="600" y2="120" stroke="#c33" stroke-width="2"/>
  <line x1="600" y1="120" x2="600" y2="95" stroke="#c33" stroke-width="2"/><line x1="600" y1="95" x2="650" y2="95" stroke="#c33" stroke-width="2" marker-end="url(#ar)"/>
  <line x1="600" y1="120" x2="600" y2="180" stroke="#c33" stroke-width="2"/><line x1="600" y1="180" x2="650" y2="180" stroke="#c33" stroke-width="2" marker-end="url(#ar)"/>
  <line x1="780" y1="95" x2="800" y2="95" stroke="#333" stroke-width="2"/><line x1="800" y1="95" x2="800" y2="130" stroke="#333" stroke-width="2"/><line x1="800" y1="130" x2="820" y2="130" stroke="#333" stroke-width="2" marker-end="url(#ar)"/>
  <text x="790" y="170" font-size="9">3-pin TTL cable</text><text x="790" y="181" font-size="9">(GND, VDD, DATA)</text>
  <text x="90" y="170" font-size="10">22 AWG silicone, red/black, the whole rail; return (−) runs straight from the brick to the OpenRB terminal − and the magnet −</text>
  <text x="90" y="186" font-size="10">Rail-sense tap: 10 k from the split node to A2, 10 k from A2 to GND, 100 nF to GND (read-only, 2.5 V when live)</text>
  <line x1="600" y1="120" x2="600" y2="222" stroke="#888" stroke-width="1" stroke-dasharray="3 2"/><text x="606" y="225" font-size="9" fill="#555">→ A2 via divider</text>
  <!-- logic side -->
  <rect x="12" y="250" width="936" height="296" fill="#f3f7ff" stroke="#36c" stroke-dasharray="4 3"/>
  <text x="20" y="266" fill="#36c" font-weight="bold">LOGIC — powered from USB-C; stays alive when the rail is open; cannot energise the rail</text>
  <rect x="24" y="290" width="120" height="50" fill="#fff" stroke="#333"/><text x="84" y="310" text-anchor="middle">Laptop / USB</text><text x="84" y="325" text-anchor="middle" font-size="10">charger 5 V (500 mA fuse on board)</text>
  <rect x="250" y="280" width="300" height="250" fill="#fff" stroke="#333" stroke-width="1.5"/>
  <text x="400" y="300" text-anchor="middle" font-weight="bold">OpenRB-150 (SAMD21G18A)</text>
  <text x="400" y="315" text-anchor="middle" font-size="10">jumper = VIN(DXL) · DXL power FET on pin 31 (off at boot)</text>
  <text x="262" y="340" font-size="11">A0  ← SPEED pot wiper</text>
  <text x="262" y="358" font-size="11">A1  ← VARIATION pot wiper</text>
  <text x="262" y="376" font-size="11">A2  ← rail sense (divider)</text>
  <text x="262" y="394" font-size="11">D4  ← PERIODIC/HUMAN toggle (INPUT_PULLUP, closed = PERIODIC)</text>
  <text x="262" y="412" font-size="11">D5  → status LED (330 Ω) ; LED_BUILTIN (pin 32) mirrors</text>
  <text x="262" y="430" font-size="11">D2, D3, 3V3, GND → HX711 header (reserved, Stage 3)</text>
  <text x="262" y="448" font-size="11">3V3 → pot ends (+) ; GND → pot ends (−), toggle, LED, divider</text>
  <text x="262" y="466" font-size="11">Serial1 (DXL port 1) → XL330 TTL bus, 1 Mbps</text>
  <text x="262" y="484" font-size="11">USB-C → Serial (115200): commands, 1 Hz telemetry, stroke log</text>
  <text x="262" y="508" font-size="10" fill="#555">GND: logic GND and rail − are the same net at the OpenRB terminal (star point); no second return path.</text>
  <line x1="144" y1="315" x2="250" y2="315" stroke="#36c" stroke-width="2" marker-end="url(#ar)"/><text x="160" y="308" font-size="10">USB-C</text>
  <!-- pots -->
  <rect x="600" y="290" width="150" height="70" fill="#fff" stroke="#333"/><text x="675" y="310" text-anchor="middle">SPEED pot 10 kΩ</text><text x="675" y="325" text-anchor="middle" font-size="10">3V3 — wiper A0 — GND</text><text x="675" y="340" text-anchor="middle" font-size="10">tape marks 0 / 50 / 100 %</text>
  <rect x="600" y="370" width="150" height="70" fill="#fff" stroke="#333"/><text x="675" y="390" text-anchor="middle">VARIATION pot 10 kΩ</text><text x="675" y="405" text-anchor="middle" font-size="10">3V3 — wiper A1 — GND</text><text x="675" y="420" text-anchor="middle" font-size="10">tape marks 0 / 50 / 100 %</text>
  <rect x="600" y="450" width="150" height="40" fill="#fff" stroke="#333"/><text x="675" y="467" text-anchor="middle">PERIODIC/HUMAN toggle</text><text x="675" y="481" text-anchor="middle" font-size="10">SPST: D4 — GND</text>
  <rect x="780" y="290" width="150" height="40" fill="#fff" stroke="#333"/><text x="855" y="307" text-anchor="middle">Status LED</text><text x="855" y="321" text-anchor="middle" font-size="10">D5 — 330 Ω — LED — GND</text>
  <rect x="780" y="350" width="150" height="50" fill="#fff" stroke="#333" stroke-dasharray="3 2"/><text x="855" y="370" text-anchor="middle">HX711 + bar cell</text><text x="855" y="385" text-anchor="middle" font-size="10">reserved: D2 DT, D3 SCK</text>
  <line x1="550" y1="325" x2="600" y2="325" stroke="#36c" stroke-width="1.5"/><line x1="550" y1="405" x2="600" y2="405" stroke="#36c" stroke-width="1.5"/><line x1="550" y1="470" x2="600" y2="470" stroke="#36c" stroke-width="1.5"/>
  <line x1="550" y1="310" x2="780" y2="310" stroke="#36c" stroke-width="1.5" stroke-dasharray="6 3"/>
  <text x="20" y="540" font-size="10" fill="#555">Red = rail (switched 5 V). Blue = logic. The only link between the two domains is the DXL cable's GND/DATA and the rail-sense divider; the DXL VDD pin is fed from Terminal VIN through the on-board FET, never from USB (jumper VIN(DXL), bench test B3).</text>
</svg>

### H.3 Connection table (every wire)

| # | From | To | Wire / gauge | Connector / termination | Notes |
|---|---|---|---|---|---|
| 1 | Adapter 5.5 × 2.1 plug (+ centre) | Jack-to-screw adapter | adapter cord | barrel 5.5/2.1 → screw terminals | Polarity: centre positive [SRC Adafruit 1466]. Meter before first power-up (B1). |
| 2 | Jack adapter **+** | Fuse holder in | 22 AWG red silicone | screw / inline holder | 1 A fast-blow 5 × 20 (F1AL250V); spare in the kit. |
| 3 | Fuse holder out | E-stop NC terminal 1 | 22 AWG red | ring/fork crimp on the e-stop block | Boxed e-stop on the desk, weighted base. |
| 4 | E-stop NC terminal 2 | Hold-to-run cable **+** | 22 AWG red | crimp at the e-stop; 1.5 m 2-core 22 AWG cable to the handle | Second NC contact of the e-stop left unused (spare). |
| 5 | Hold-to-run microswitch COM | — | inside the handle | 4.8 mm spade on the arcade microswitch | Strain relief: cable through the printed gland + internal zip-tie anchor. |
| 6 | Hold-to-run microswitch **NO** | Rail split node (3-way Wago / screw block at the module) | 22 AWG red (return leg of the 1.5 m cable) | Wago 221-413 lever block or screw terminal | This node is the **ACTUATOR RAIL +**. |
| 7 | Rail node + | OpenRB-150 Terminal VIN **+** | 22 AWG red | removable terminal block (supplied) | 470 µF 10 V electrolytic + SMAJ5.0A TVS across + / − at the terminal. Jumper on **VIN(DXL)**. |
| 8 | Rail node + | Electromagnet lead 1 (+) | 22 AWG red (magnet's own 270 mm leads spliced, heat-shrink) | solder + heat-shrink | 1N5819 Schottky across the coil: **cathode (band) to +**, anode to −. |
| 9 | Rail node + | 10 kΩ → A2 | 26 AWG | pot/divider on the small perfboard | 10 kΩ A2 → GND, 100 nF A2 → GND. Read-only sense. |
| 10 | Jack adapter **−** | OpenRB-150 Terminal VIN **−** | 22 AWG black | terminal block | Star ground point. |
| 11 | OpenRB-150 Terminal **−** | Electromagnet lead 2 (−) | 22 AWG black | solder + heat-shrink | |
| 12 | OpenRB-150 DXL port 1 | XL330 ID 1 (either X3P socket) | ROBOTIS 3-pin TTL X3P cable (JST-EH), **340 mm or longer** (the 180 mm cable supplied with the servo is too short for the tray → hinge → beam → drop-leg run) | JST-EH 3-pin | 60 mm service loop at the hinge in clip P36; braided sleeve; zip-tie anchors at both ends. Daisy-chain port on the servo → ID 2 in Stage 3. |
| 13 | SPEED pot ends | 3V3 / GND | 26 AWG (in the 1.0 m 6-core panel cable) | Dupont to the OpenRB headers | Wiper → **A0**. |
| 14 | VARIATION pot ends | 3V3 / GND | 26 AWG | Dupont | Wiper → **A1**. |
| 15 | Toggle PERIODIC/HUMAN | **D4** / GND | 26 AWG | Dupont | INPUT_PULLUP; closed (to GND) = PERIODIC. |
| 16 | Status LED anode | **D5** via 330 Ω; cathode → GND | 26 AWG | Dupont | LED_BUILTIN (pin 32) mirrors it. |
| 17 | HX711 header | **D2** (DT), **D3** (SCK), 3V3, GND | 26 AWG | 4-pin header, unpopulated | Stage 3 load cell (40 × 12 mm bar cell slot in the wrist). |
| 18 | Laptop / USB charger | OpenRB-150 USB-C | USB-C data cable, 2 m, tie-wrapped down the monitor arm | USB-C | Logic power + serial. Board USB input fused 500 mA [SRC]. |

Only wire 12 crosses a moving joint (the fail-safe hinge): 60 mm service loop, braided sleeving, zip-tie anchors at both ends. No bare terminals anywhere on the rail; the Wago block sits inside the printed tray P3 on the adapter (fixed side of the hinge), so the electromagnet leads never cross the hinge.

### H.4 Where the electronics live

OpenRB-150, Wago rail node, rail perfboard (divider, TVS, 470 µF) and fuse holder: electronics tray P3 on the adapter's front face. Electromagnet: on the adapter's magnet arm. SPEED and VARIATION pots, PERIODIC/HUMAN toggle and status LED: control panel P37/P38 on the desk beside the e-stop, linked to the tray by the 1.0 m 6-core cable (3V3, GND, A0, A1, D4, D5), tape marks at 0/50/100 % around each pot. E-stop: the boxed TWTADE unit on its steel plate on the desk, under the free hand in the test posture. Hold-to-run: handheld housing P39/P40 on its 1.5 m cable, gland at the handle, zip-tie anchor on the carrier beam. Brick: on the floor, > 1 m from the head, cord zip-tied to the desk edge. USB-C from the tray to the laptop tie-wrapped down the arm.

### H.5 Power facts verified from the ROBOTIS e-manual, and the one thing it does not say

Verified [SRC]: three power inputs (USB-C 5 V; VIN pin 3.7–12.6 V; Terminal block / XT60 3.7–12.6 V); the jumper selects the DYNAMIXEL supply (`VIN(DXL)` or `USB(5V)`); power to the DYNAMIXEL ports is controlled by a FET that is **off whenever the board is powered on** (pin `BDPIN_DXL_PWR_EN`, 31) and Dynamixel2Arduino raises it in `begin()`, so the bus is powered only once firmware is running and any reset (including a watchdog reset) drops it; USB current is limited to 500 mA by a built-in fuse; DC current for the DYNAMIXEL ports 3,000 mA; resetting the microcontroller resets the power of any connected DYNAMIXEL. The `USB(5V)` jumper position is **forbidden** for SP1 (servo on the laptop side of the safety loop).

**[VERIFY] not stated in the manual:** whether, with the jumper on `VIN(DXL)` and Terminal VIN at 0 V, the MCU keeps running from USB-C (the MKR-style ORed design makes this likely; the schematic is a download at https://www.robotis.com/service/download.php?no=2117). Bench test **B2** settles it; both outcomes are safe: *A (expected)* MCU alive on USB, firmware sees rail = 0, goes PAUSED, re-initialises when the rail returns; *B* MCU resets with the rail, bus FET off at boot, servo limp, firmware restarts in INIT. **B3 is a hard gate:** rail open + USB connected → DXL port VDD pin meters 0 V and the servo LED stays dark; if it reads 5 V the jumper is wrong and the rig is not used until it reads 0 V.

### H.6 Fusing, polarity, strain relief, back-feed

- **Fuse 1 A fast.** Normal rail current ≈ 0.6 A (servo ≤ 0.30 A at goal current + magnet 0.22 A + board ≈ 0.05 A) → 1 A ≈ 1.5–1.7× running. A servo that has lost its limits stalls at 1.47 A → fuse opens; the brick's own OCP (≈ 4 A) is the absolute ceiling. If 1 A nuisance-trips at bring-up at 450 mA goal current, 1.25 A fast is the only permitted step up; note it on the diagram.
- **Polarity.** Centre-positive brick → keyed barrel adapter → red/black → terminal marked + / −. No series diode (it would drop the bus toward the XL330's 3.7 V floor); the SMAJ5.0A clamps reversed or spiked input; the metered polarity check is B1. XL330 operating range 3.7–6.0 V.
- **Rail voltage.** With the 5 V 4 A brick and 22 AWG rail wire the drop stays under 0.2 V at 0.6 A (addendum ruling 7). The firmware's rail-sense threshold is set so that **< 4.0 V reads as rail-dead** (torque off), closing the 3.3–3.7 V window where the servo could brown out while the magnet still holds the frame (§I.6, Appendix 1 note 6).
- **Strain relief.** Brick cord zip-tied to the desk edge; e-stop box screwed to its steel plate; the 1.5 m hold-to-run cable has a gland at the handle and a zip-tie anchor at the module; the DXL cable has its service loop at the hinge; nothing hangs from a solder joint.
- **Why the magnet must not back-feed and must not be fed from anywhere else.** The fail-safe lift is credited only because the magnet dies *with* the servo. (i) It hangs on the rail after the hold-to-run contact, never on a GPIO, a MOSFET from USB 5 V, or its own supply: any other path would hold the frame down with the nails in the hair while the servo is dead (red line 8). (ii) The coil stores a few mJ [EST]; when the loop opens that energy would spike the open contact to tens of volts and put a transient on VIN and the DXL bus; the 1N5819 recirculates it, and drop-out takes a few ms longer, irrelevant against the spring's lift time. (iii) The 470 µF holds up the rail for ≈ 4 ms, negligible, and the magnet releases below ~50 % of rated voltage anyway.

### H.7 Safety architecture: what electronics and firmware mitigate

| Hazard | Primary (hardware) | Electrical second layer (servo registers, set by firmware at INIT; EEPROM items persist) | Firmware third layer |
|---|---|---|---|
| Excessive normal force | mechanical: dead weight + leaf stops | — (normal force is not a servo quantity) | — |
| Excessive tangential force (red line 3) | 2.0 N magnetic wrist breakaway | Goal Current 300 mA ≈ 1.26 N at 84 mm; Current Limit 450 mA ≈ 1.9 N | stall trip 270 mA / 250 ms → FAULT; `cur` clamped ≤ 450 |
| Motor stall / overheating | 1 A fuse; XL330 Shutdown on overload/overheat (bits 5, 2) | Current Limit 450 mA bounds dissipation to ≈ 0.7 W [EST]; Shutdown 0x34 | stall trip < 300 ms; Hardware Error Status polled 5 Hz → FAULT; re-arm by `reset` |
| Runaway actuation | e-stop / hold-to-run cut the rail; mechanical stops at the hinge and the elbow | Min/Max Position Limit ±28° in EEPROM (the servo refuses goals outside, B6); Profile Velocity never above 180 LSB | all goals clamped to ±25° in one function (`setGoal`), bounded speeds, 3 ramp strokes, MCU WDT 1 s → reset → DXL FET off |
| Abrasion / dwell | — | — | no dwell on skin: pauses go to +25° (lifted by geometry); end-dwell ≤ 300 ms; 20-min session limit |
| Mains | certified external brick, nothing above 5 V on the rig | — | — |
| Low-voltage shorts | 1 A fuse, 22 AWG, sleeving, no bare terminals | servo OCP/OTP | — |
| Back-EMF / inductive kick | 1N5819 on the magnet; 470 µF + SMAJ5.0A at the terminal; separate USB logic supply | — | — |
| Lithium | none in SP1 | — | — |
| No / failed emergency shutoff (red line 4) | NC e-stop in series with the rail, in reach; hold-to-run in the free hand; logic on USB stays up | Bus Watchdog 100 ms stops the servo if the MCU dies | firmware reads the rail (A2) and mirrors it as PAUSED; never implements the stop |
| Hot motor near scalp | servo ≥ 75 mm from the scalp | current limits keep dissipation low; Shutdown on overheat | Present Temperature readable |
| Cannot remove quickly (red line 8) | release the button → rail dead → magnet drops → spring lifts ≥ 25 mm | servo unpowered → limp (XL330 back-drive torque small [EST]) | on FAULT: torque off + bus FET off; restart only via `reset` |
| Firmware faults (red line 13) | the rail loop does not depend on any of this | Bus Watchdog (servo-side), EEPROM limits (servo-side) | MCU WDT, limits table printed at boot, single clamp point, motion timeout, comm-loss trip |
| Non-back-drivable servo (red line 7) | spring-return lift on the hinge; leaf cap downstream | — | torque off on every stop/fault so the arm is at least limp |

What firmware **cannot** do and does not claim: bound the normal force (dead weight and leaf stops do), lift the hand on comm loss (the Bus Watchdog *stops* the servo; the hardware rail lifts), or stop a latched hold-to-run (the §M rule).

### H.8 Stack B (fallback if the OpenRB-150 or XL330 is unobtainable)

ESP32 + Waveshare "Servo Driver with ESP32" + Feetech STS3215: same rail topology at 7.4 V (STS3215-7.4 V on a 7.5 V brick, or a 12 V brick + UBEC after the hold-to-run), 12 V P20/15 magnet, 2 A fuse, 20 AWG rail. The Waveshare board feeds its logic from the servo jack, so logic dies with the rail unless the ESP32 is powered from USB (check the power path; else accept Outcome-B behaviour and log on the host). STS3215 has no Bus Watchdog and its servo power is not FET-gated through a reset, so add an INA219 rail watchdog (trip 1.2 A / 200 ms) or a logic-driven MOSFET on the servo rail. Torque Limit / Protection current (6.5 mA/LSB) replaces Goal Current (~0.1 N·m → ~300 mA at 7.4 V [EST], re-derive on the bench); position units 4096/rev are the same; only `tipSpeedToVelLsb()` re-scales; ESP32 ADC non-linearity near the rails → pot end marks at 5 %/95 %. A 55 g servo needs a new cradle P13. About a week of work; last resort.

---

## I. CONTROL LOGIC AND FIRMWARE

Source: `05-engineering/firmware/sp1_scratch/sp1_scratch.ino`, boot banner `SP1-fw-0.2`, 533 lines. Board OpenRB-150 (SAMD21G18A), library Dynamixel2Arduino ≥ 0.7, servo XL330-M288-T ID 1 in current-based position mode. **Not yet compiled with a real toolchain** (no arduino-cli where it was written); compiling it in the Arduino IDE is bring-up step B0 and the first step of the build review.

### I.1 State machine

```
            rail present, servo configured, zero sane, torque on at +25°
  INIT ───────────────────────────────────────────────────────────────▶ LIFTED_IDLE
   ▲  (no rail: wait, print every 2 s)                                     │ 1 s hold, run latch set
   │                                                                       ▼
   │  rail returns (servo was unpowered → re-write RAM registers)       RUNNING ──── stroke engine (§I.4)
   │◀──────────────────────── PAUSED ◀──── rail lost (button released / e-stop) ──┘
   │                                                                       │ 'stop' / 20-min limit: finish at +25°, torque off
   │                                                                       ▼
   │                                                               LIFTED_IDLE (torque off)
   │
   └──────── 'reset' ◀──── FAULT ◀── comm loss | over-current/stall | hardware error | motion timeout | zero out of range | config
                            (torque off + DXL power FET LOW; LED rapid flash; nothing restarts without 'reset')
```

- **INIT:** waits for the rail (A2 above the rail-dead threshold, §I.6). Then `dxl.begin(1 Mbps)` (raises the DXL FET), ping ID 1 (falls back to 57600 and migrates a factory servo to 1 Mbps), model check (1200 = XL330-M288), torque off, EEPROM table written only where it differs, RAM registers, zero-sanity check (present position within ±40° of zero with the arm free and the zero pin out, else FAULT `zero_out_of_range`), goal +25° at 60 mm/s, torque on, Bus Watchdog armed last.
- **LIFTED_IDLE:** torque on at +25° (lifted by geometry: 15.9 mm along the arm at the down-stop, 11.2 mm vertical for the centre nail, 5.7 mm for the trailing outer nail). After 1 s, if the run latch is set (default: the hold-to-run press *is* the start action; `stop` clears it, `run` sets it) → RUNNING. `goto`/`gotoraw`/`zero` are only accepted here.
- **RUNNING:** every 20 ms read Present Position and Present Current (feeds the Bus Watchdog), Hardware Error Status every 200 ms, trips, stroke engine, 1 Hz telemetry.
- **PAUSED:** rail off; servo and magnet already dead by hardware; firmware waits and re-enters INIT when the rail returns (the servo rebooted, so RAM registers are re-written).
- **FAULT:** torque off (best effort), `BDPIN_DXL_PWR_EN` LOW, LED 10 Hz, telemetry keeps printing the fault code; only `reset` leaves (→ INIT).

### I.2 XL330-M288-T register settings [SRC: e-manual control table]

| Register (addr) | Value | Unit / meaning | Why |
|---|---|---|---|
| Operating Mode (11) | **5** current-based position | | position goals with a hard current (torque) ceiling |
| Baud Rate (8) | 3 (1 Mbps) | | 50 Hz loop with three reads per tick; migrated from factory 57600 by firmware |
| Return Delay Time (9) | **0** | 2 µs/LSB | fastest turnaround |
| Status Return Level (68) | **2** | all instructions answered | every write verifiable |
| Homing Offset (20) | set by `zero` | ticks; Present = Actual + Offset | puts the pinned θ = 0° position at 2048 |
| Min Position Limit (52) | **1729** (= 2048 − 28° × 11.378) | 0.088°/LSB | −28° absolute; the servo refuses goals below |
| Max Position Limit (48) | **2367** | | +28° absolute |
| Current Limit (38) | **450** | mA (default 1750) | EEPROM ceiling ≈ 1.9 N tangential; Goal Current cannot exceed it |
| Shutdown (63) | 0x34 (default) | overload, electrical shock, overheating | factory default kept explicitly |
| Goal Current (102) | **300** (RAM, `cur` command, 100–450) | mA | ≈ 1.26 N at 84 mm by the linear curve |
| Profile Acceleration (108) | 20–60 per stroke | 214.577 rev/min²/LSB = 21.46 °/s² | 0.63–1.9 m/s² at the tip |
| Profile Velocity (112) | per stroke, **cap 180** | 0.229 rpm/LSB | 25 / 50 / 75 LSB ≈ 50 / 100 / 150 mm/s; 180 LSB = 0.36 m/s < 0.4 m/s cap |
| Goal Position (116) | per stroke, clamped ±25° (±284 ticks) | ticks | one clamp point: `setGoal()` |
| Bus Watchdog (98) | **5** = 100 ms, armed after torque on; cleared with 0 at every INIT | 20 ms/LSB | if the communication interval exceeds it the servo stops; goal registers become read-only and the register reads −1 until cleared |
| Present Position (132) / Present Current (126) / Hardware Error Status (70) | read 50 / 50 / 5 Hz | ticks / mA signed / bits 0, 2, 3, 4, 5 | telemetry, stall trip, fault trip |

**Goal current from 1.2 N at 84 mm.** Datasheet: stall 0.52 N·m at 5.0 V, 1.47 A → K_t ≈ 0.354 N·m/A (0.378 at 3.7 V, 0.345 at 6.0 V; linear to a good approximation). Required τ = 1.2 N × 0.084 m = 0.1008 N·m → I = 0.285 A → **Goal Current 300 mA** (→ 1.26 N on the same line). Ceiling: Current Limit 450 mA → 0.159 N·m → **1.90 N**, inside the 2.0 N wrist breakaway. Expected running current: three nails × ~0.1 N drag × 0.084 m = 0.025 N·m → ~70 mA, + inertia (hand ≈ 30 g at 84 mm, J ≈ 2.1 × 10⁻⁴ kg·m², α ≤ 22 rad/s² → 13 mA) + gear friction → **≈ 150 mA typical** [EST]; the 270 mA stall trip is ~1.8× that. Caveat: the gearbox needs a no-load current (50–100 mA [EST]) before torque appears, so the actual stall force at 300 mA is roughly 0.85–1.1 N; **B7 calibrates `cur` so the stalled push reads 1.2 ± 0.2 N** on a scale and the result replaces `goalCurrentMa` in the config block. Current is a secondary layer; the 2.0 N wrist breakaway bounds the worst case.

**Velocity, acceleration, timing.** ω = v / L: 50, 100, 150 mm/s at L = 84 → 0.595, 1.19, 1.79 rad/s = 25, 50, 75 LSB; cap 180 LSB. Acceleration 20–60 LSB (430–1290 °/s²) → 0.63–1.9 m/s² at the tip; the servo's trapezoidal profile does the shaping; short strokes become triangular automatically. Stroke timeout = 2 × (distance / velocity) + 600 ms; three consecutive timeouts → FAULT `motion_timeout`.

**On communication loss.** Bus Watchdog 100 ms: the XL330 **stops** (holds position under the current limit) but does not torque off by itself. (a) If the MCU hung, the SAMD21 WDT resets it within 1 s → DXL FET off at boot → servo limp. (b) If the MCU is dead (USB pulled), the servo stays stopped under ≤ 300 mA until the operator releases the hold-to-run, the normal way to end anything. (c) The normal force never came from the servo (dead weight), so a stopped servo is a resting hand at W: that is why the lift is on the rail, not in the servo. Firmware side: 5 consecutive failed reads (100 ms) → FAULT `comm_loss` → torque off + FET off.

### I.3 Zero calibration (addendum ruling 5: by the pin, never by gravity)

The arm is top-heavy (rail, mast and carriage sit above the axis), so it does **not** hang plumb. Procedure: rail on, not running (`stop`), module latched, nails in free air ≥ 25 mm above anything; torque off; insert the **3 mm zero pin** through cheek A and the cradle flange (the hole is coincident only at θ = 0°; the mast must then be plumb to the carrier beam, check with the square); type `zero`. Firmware writes Homing Offset = 0, reads the raw Present Position, writes Homing Offset = 2048 − raw, re-reads and expects 0.0° ± 0.5°. The offset lives in the servo's EEPROM, so it survives reflashes and power cycles; redo it after any hand/arm re-mount. **Remove the pin before `run` or `goto`** (a `goto` with the pin in stalls the servo against the pin; the stall trip would catch it, but do not rely on it). Sign convention: `+` is the direction that lifts toward the +25° park; check on the bench that `goto 25` raises the nails on the same side every time and negate the sign in `degToTicks()`/`presentDeg()` if the horn is mirrored. (The electronics-firmware document and the firmware README describe `zero` "with the hand hanging freely"; that wording is superseded by this pin procedure. The firmware's INIT zero-sanity check — present position within ±40° of zero — is unchanged and is checked with the pin removed.)

### I.4 Pattern engine (freeze §2)

| Symbol | Default | Freeze §2 | Serial |
|---|---|---|---|
| amplitude band (half-amplitude) | 12–25° | 12–25° (chord 33–68 mm incl. lifted portions; contact chord ≤ 37 mm) | `amp <min> <max>` |
| peak tip speed band | 50–150 mm/s × SPEED | 50–150 mm/s, SPEED pot scales | `speed <min> <max>` |
| SPEED pot | 0 / 50 / 100 % → × 0.5 / × 1.0 / × 1.5 (S1 / S2 / S3) | | `spd <%>` / `spd auto` |
| per-stroke jitter | ±25 % amp, ±25 % speed, × VARIATION | ±25 % | `jitter <%>` |
| direction asymmetry | up to 15 % × VARIATION | "randomized asymmetry" | `asym <%>` |
| end dwell | 0–300 ms × VARIATION | 0–300 ms | `dwell <ms>` |
| pause | every 4–10 strokes, 0.5–3 s at +25°, p = 1.0 | every 4–10 strokes, 0.5–3 s lifted | `pausen`, `pausems`, `pause <p>` |
| episode | every 5–20 s new sub-bands; p = 0.2 × VARIATION one slow long stroke (25°, 40 mm/s) | every 5–20 s | `episode <min> <max>`, `slow <p>` |
| VARIATION pot | 0–100 % scales all jitter, dwell, asymmetry, slow-stroke chance; at < 5 % bands collapse to their centres | 0–100 % | `var <%>` / `var auto` |
| PERIODIC | 18°, 100 mm/s × SPEED, no pauses/dwell/episodes | fixed 18°, fixed speed, no pauses | toggle, `mode`, `periodic <deg> <mm/s>` |
| strokes/s | emergent: 2·amp/ω + dwell → ≈ 1–3 /s | 1–3 /s | — |
| RNG seed | 0x5EEDC0DE | — | `seed <n>` (reproducible sessions) |

```
every 20 ms tick (RUNNING):
  read PresentPosition, PresentCurrent (feeds Bus Watchdog); HardwareError every 10th tick
  trips: hwError → FAULT ; |I| ≥ 0.9·Igoal and |Δθ| < 0.3° for ≥ 250 ms → FAULT ; 5 failed reads → FAULT
  if session > 20 min → stop (finish at +25°, torque off)
  phase MOVING : if |θ − goal| < 1.5° → endStroke() ; elif t > timeout → count, endStroke() (3 in a row → FAULT)
  phase DWELL / PAUSE : if t ≥ phaseEnd → beginStroke()

beginStroke():
  if PERIODIC: amp = 18°, tip = 100 mm/s × S, acc = 40
  else (HUMAN):
    if t > episodeEnd: newEpisode()        # sub-bands [epAmp], [epSpd] ⊂ bands; width 30–100 %; maybe one slow stroke
    if slowStrokePending: amp = 25°, tip = 40 × S, acc = 20
    else: amp = U(epAmp) · (1 + U(−.25,.25)·V) ; tip = U(epSpd) · (1 + U(−.25,.25)·V) · S · (1 ± 0.15·V·U(0,1)) ; acc = U(20,60)
    dwell = U(0, 300 ms) · V
  first 3 strokes of a run: tip × 0.5 / 0.7 / 0.9     # soft start
  clamp amp ∈ [5°, 25°], tip ∈ [20, 360] mm/s ; vel = ω(tip)/0.229 rpm, ≤ 180
  write ProfileAccel, ProfileVelocity, GoalPosition(dir·amp) ; dir = −dir

endStroke():
  n++ ; if settings code changed → print "C," line ; print "S," line
  if HUMAN and --strokesToPause == 0: strokesToPause = U(4,10); with p=pause_prob → goal +25°, PAUSE U(0.5,3 s)+0.4 s
  else DWELL(dwell)
```

**Startup:** rail on → INIT configures → torque on at +25°, 1 s hold in LIFTED_IDLE → RUNNING with the 50/70/90 % ramp over the first three strokes (soft start ≥ 500 ms met). **Shutdown** (`stop`, 20-min limit): the current stroke is abandoned for a goal of +25° at 80 mm/s, then torque off 1.5 s later. `run` after a stop re-enters INIT and then the 1 s lifted hold. **Rail loss** (button released, e-stop): hardware has already removed servo power and dropped the magnet; firmware mirrors this as PAUSED within one tick and re-initialises when the rail returns; resuming through INIT → LIFTED_IDLE → RUNNING with the ramp means **no stroke ever starts in contact** (set `AUTO_RUN_ON_RAIL = false` to require a serial `run` after each release instead). **Fault:** torque off, DXL FET LOW, LED 10 Hz, telemetry shows the fault name; only `reset` clears it; the hardware rail is what lifts the hand.

### I.5 Serial command interface (USB, 115200 8N1, newline-terminated)

| Command | Effect |
|---|---|
| `help`, `status`, `limits` | help; one-line status + full `C,` settings line; the limits table (also printed at boot) |
| `run`, `stop`, `reset` | set run latch / finish at +25° and torque off / leave FAULT → INIT |
| `zero` | zero calibration (rail on, not running, **zero pin in**) → Homing Offset in the servo |
| `goto <deg>` | LIFTED_IDLE only; clamps to ±28°; limit test ("go to +28°") |
| `gotoraw <deg>` | LIFTED_IDLE only; sends the unclamped goal; the servo must **refuse** anything beyond ±28° (prints ACCEPTED/REFUSED) |
| `hang` | stops the main loop → MCU watchdog reset in ≈ 1 s → DXL FET off → servo limp (watchdog test) |
| `mode human|periodic|auto` | override the toggle / return to it |
| `spd <0-100>|auto`, `var <0-100>|auto` | override the SPEED / VARIATION pots / return to them (0/50/100 = S1/S2/S3, V0/V50/V100) |
| `amp a b`, `speed a b`, `jitter %`, `asym %`, `dwell ms`, `pause p`, `pausen a b`, `pausems a b`, `episode a b`, `slow p`, `periodic deg mm/s` | pattern parameters, all clamped inside the limits table |
| `cur <mA>` | goal current, clamped 100–450 (Current Limit); written immediately when the servo is up |
| `seed <n>` | reseed the xorshift32 RNG (same seed + same settings code = same stroke sequence) |
| `log on|off` | per-stroke lines on/off (telemetry and state lines always print) |
| `bset <slot 1-8> per|hum|auto <spd%|-1> <var%|-1>` | define a BLIND condition slot (−1 = leave that level to the pot) |
| `blind <n>` | shuffle slots 1..n (seeded), apply the first without printing which; mode shows `BLD`, S/V show −1 or 0 in logs |
| `next` | advance to the next hidden slot (between trials) |
| `reveal` | print `R,trial i = slot k MODE Sx Vy` for every trial |
| `unblind` | clear overrides, back to pots/toggle |

**Log lines** (comma-separated, first field a letter, `t` = ms since boot): `H,t,state,mode,spd%,var%,strokes,pos_deg,mA,fault,code` 1 Hz always; `S,t,n,amp_deg,vel_lsb,tip_mm_s,dwell_ms,cur_peak_mA,cur_mean_mA,pos_end_deg,code` per stroke; `C,t,code,amp…,spd…,jit,asym,dwell,pause,ep,slow,per,seed` at boot and whenever the code changes (a log file is self-describing); `E,` episode; `Z,` pause; `T,` stroke timeout; `STATE …`; `R,` reveal. **Settings code** = `MODE-S<spd%>-V<var%>-C<goal mA>#<hash>`, e.g. `HUM-S50-V100-C300#3f1a`; the test notation `HUM S2 V100` maps directly (S1/S2/S3 = S0/S50/S100). Save a session with the IDE serial monitor or `screen -L /dev/cu.usbmodem* 115200`.

**Changing the pattern:** live, per session, with the commands above (record the code from the `C,` line on the session log); defaults in `Pattern P = { … }` in the CONFIG BLOCK (order: amp min/max, speed min/max, jitter amp, jitter speed, asym, dwell max, pause every min/max, pause prob, pause ms min/max, episode s min/max, slow-stroke prob, periodic amp, periodic speed); shape in `newEpisode()`, `beginStroke()`, `endStroke()`. Every goal goes through `setGoal()`, which clamps position to ±25°, velocity to 180 LSB and acceleration to 20–60 LSB: keep it that way, it is the single clamp point the safety case relies on. Limits (`LIMIT_*`, `CURRENT_LIMIT_MA`, `goalCurrentMa`, `PROFILE_*`, `STALL_*`, `BUS_WATCHDOG_LSB`) are in the CONFIG BLOCK and printed at boot; change them only with a matching edit to this section and a re-run of B6–B10. Stage 3 yaw: `DXL_ID_YAW` is reserved; add a second `setGoal`-style clamp for ID 2 before driving it.

### I.6 Two firmware edits required before bring-up (addendum rulings 5 and 7)

1. **Rail-dead threshold 4.0 V.** As written, `railOn = analogRead(PIN_RAIL_SENSE) > 400` (≈ 1.3 V at A2 ≈ 2.6 V on the rail). The addendum requires < 4.0 V to read as rail-dead. With the 10 k/10 k divider and the 10-bit 3.3 V ADC, 4.0 V on the rail is 2.0 V at A2 = count 620. **Change the threshold to 620** (and name it, e.g. `RAIL_ON_COUNTS = 620`, in the CONFIG BLOCK so it prints with the limits table). Verify in B1 that a live 5.0 V rail reads about 775 counts and that the state goes PAUSED when the rail is pulled down.
2. **Zero by pin.** The `zero` help text and the INIT error message say "with the hand hanging"; change them to "with the zero pin in" so the serial prompt matches §I.3. No logic change.

Assumptions to confirm at first compile: `readControlTableItem()` sets `getLastLibErrCode()` to 0 on success (used by `rd()`; if reads never flag errors, B10(b) will show it, then check the returned value against a sentinel); `getModelNumber(id)` returns 1200 for the XL330-M288-T; the SAMD21 WDT block follows Adafruit SleepyDog (if the core already configures GCLK2, remove the two `GCLK->` lines); the sign convention (`goto 25` must lift toward the park side).

### I.7 Bring-up procedure and bench tests (pass criteria)

Equipment: multimeter, kitchen scale or 0–5 N spring scale, stopwatch/phone, the servo on the bench **without the hand** for B4–B6, with the hand for B7–B9.

| # | Step / test | Procedure | Pass |
|---|---|---|---|
| B0 | Toolchain | Arduino IDE 2.x; File → Preferences → Additional boards manager URL `https://raw.githubusercontent.com/ROBOTIS-GIT/OpenRB-150/master/package_openrb_index.json` → Boards Manager → install "OpenRB-150"; Library Manager → Dynamixel2Arduino (0.7.x) by ROBOTIS. Jumper on **VIN(DXL)**. Apply the two §I.6 edits. Rail **off**, USB-C to the laptop, Sketch → Upload `sp1_scratch.ino` (if the port disappears, double-press the board's reset button and upload again). Serial Monitor 115200, Newline. | Boot banner `PROJECT SCRATCH SP1 SP1-fw-0.2` and the limits table print; `C,` line; `H,` lines at 1 Hz; `INIT: waiting for actuator rail`. |
| B1 | Polarity & rail | Brick → adapter → fuse → e-stop → button → terminal, **servo not yet plugged**. Meter the terminal: + is centre-positive 5.0 ± 0.25 V only while the button is held; 0 V with the button released; 0 V with the e-stop pressed regardless of the button. Watch the `H,` state: PAUSED/INIT with the button released. | All three readings; fuse value written on the diagram and the kit label; rail-sense reads live only with the button held. |
| B2 | Logic survives rail loss **[VERIFY]** | USB connected, button held (rail live), then release. Watch the serial monitor. | Outcome A: `H,` lines continue, state → PAUSED. Outcome B: board resets and re-prints the banner. Record which; both pass; B is noted in the session log. |
| B3 | **No USB back-feed to the bus (hard gate)** | Rail open (button released), USB connected, firmware running. Meter the DXL port VDD pin against GND; plug the servo in. | **0.0 V**; servo LED dark; `INIT` keeps waiting. Any voltage → stop, fix the jumper, repeat. |
| B4 | Servo ID / baud | Plug the XL330 (factory ID 1, 57600). Hold the button. | Serial: `servo found at 57600, migrating to 1 Mbps` (first time only), then `STATE LIFTED_IDLE` and the horn moves to +25°. Alternative: Dynamixel Wizard 2.0 to set ID 1 / 1 Mbps beforehand. ID 2 (yaw) is set the same way in Stage 3, one servo on the bus at a time. |
| B5 | Zero calibration (by pin) | Mount the arm + hand, module latched, nails in free air. `stop`, release/hold the button, torque off, **insert the 3 mm zero pin**, `zero`, **remove the pin**. Then `goto 0`, `goto 25`, `goto -25`. | `zero OK … now 0.0 deg`; at `goto 0` the pin slides freely back into its hole and the mast is plumb to the carrier beam (± 1°); `goto 25` lifts toward the park side; both directions symmetric. |
| B6 | Position limits (K2.13 / L4) | `goto 28`, `goto -28` (hand held lightly), then `gotoraw 40` and `gotoraw -40`. | Hand reaches ±28° and no further; `gotoraw` prints **REFUSED** and the horn does not move; `H,` position never exceeds ±28.5°. |
| B7 | Goal-current calibration (over-current test) | `run`; while running, block the arm with a finger/spring scale at the nail tips. Then at `goto 0`, push the horn via the scale until it stalls. | Running: FAULT `over_current` within **≤ 300 ms** of blocking; LED rapid flash; `reset` required. Stalled push on the scale = **1.2 ± 0.2 N**; otherwise adjust `cur` and record the final value in the config block. |
| B8 | E-stop (K3.5) | Running; press the e-stop. Twist to release. | Rail 0 V, servo limp, magnet drops, frame lifts ≥ 25 mm; firmware → PAUSED; on release *nothing moves* until the button is held, then INIT → 1 s at +25° → strokes. |
| B9 | Hold-to-run release | Running; release the thumb × 10. | Every time: servo limp + lift within the spring's time; resume only through the 1 s lifted hold; no stroke starts in contact (video). |
| B10 | Watchdog (K4.3) | (a) `hang` while running; (b) unplug USB while running (rail live). | (a) reset in ≈ 1 s, banner reprints, DXL LED off, servo limp (hand liftable by hand) ≤ 1 s. (b) servo **stops** within 100 ms (Bus Watchdog) and holds under ≤ 300 mA; releasing the button lifts it; re-plugging USB → INIT clears the watchdog and resumes only via the lifted hold. |
| B11 | Runaway / garbage input (K4.6) | Type garbage, `amp 90 200`, `speed 5 9999`, `cur 9999`, wiggle pots, flip the toggle mid-stroke. | All values clamp (`status` shows the clamped numbers); position stays inside ±25° nominal, ±28° absolute; tip speed ≤ 0.36 m/s; mode changes take effect at the next stroke. |
| B12 | Telemetry & reproducibility | `seed 42`, `status`, run 30 s, `stop`; repeat. | Identical `S,` amplitude/speed sequences for the same seed and code; `H,` lines every 1.0 s; the `C,` line appears whenever a parameter changes. |
| B13 | BLIND | `bset 1 per -1 -1`, `bset 2 hum -1 0`, `bset 3 hum -1 50`, `bset 4 hum -1 100`, `blind 4`, run/`next` × 3, `reveal`. | Mode prints `BLD` throughout; `reveal` lists a permutation of the four slots; the pot echo shows −1 while blind. |
| B14 | 30-min soak (L7) | Per L7, hold-to-run taped **for this bench test only** (label, remove after). | Zero faults, zero resets; XL330 case ≤ 48 °C; stroke count 1–3/s consistent with the log. |

### I.8 Test-lead requirements compliance

| Requirement | Status |
|---|---|
| 1 Hz serial echo of SPEED %, VARIATION %, MODE, stroke count, elbow position, fault code | Met (`H,` line) |
| SPEED pot active in PERIODIC | Met: PERIODIC speed = 100 mm/s × (0.5 + pot) |
| Serial "go to +28°", "hang", limits at boot | Met (`goto`, `gotoraw`, `hang`, `printLimits()`) |
| BLIND: random PER/HUM, reveal on request | Met for firmware-settable conditions (mode, SPEED %, VARIATION %). Cannot be met for tips, weights, engagement or direction (physical swaps): use the coded tip box or a helper |
| Hold-to-run lead ≥ 1.5 m | Met |
| Button "cannot be latched" | Partly met: momentary microswitch, thumb well 3 mm below a 36 mm rim, 20-min firmware limit; no cheap handheld switch is proof against a deliberately inserted wedge; a 3-position enabling pendant is out of SP1's budget; the §M rule stands |
| Fuse value on the diagram, spare in the kit | Met (1 A fast) |
| Per-stroke log line carries the settings code | Met |
| E-stop on a weighted base | Met |
| Tape marks on both pots at 0/50/100 % | procedural |

---

## J. ASSEMBLY INSTRUCTIONS

The order front-loads the bench tests: L2 runs on the bare hand, L3, L6 and L1 on the float before the arm exists, L5 as soon as the hinge and magnet are up (before the servo is even plugged in), and L4 last. Paint-pen torque marks on every screw once tightened (K2.15). Torques: M2 0.15 N·m, aluminium M3 0.3 N·m, steel M3 0.5–0.6 N·m, M4 nyloc 1 N·m, M5 into 2020 2 N·m. Inserts go in at 220–230 °C, square to the surface.

### Phase A: hand (about 5 h)

1. Print the fit-test parts first (P15, P2, P13, P34 with a leaf scrap, one paddle and one tip) and adjust hole compensation before the rest. Print everything else; weigh each float part as it comes off the printer and log it against §C.6.
2. Cut the three leaves with aviation snips: 70 / 67 / 64 mm (L, C, R). Round all four corners R 1, stone both long edges and the ends, wipe off oil. Mark each leaf's root bar-edge line with a fine marker: from the paddle end, 4 + a mm = 52.3 / 48.5 / 45.7 mm (L, C, R).
3. Set heat-set inserts in P32 (18 × M2, 3 × M3).
4. Fit each paddle (T1, T1, T2, with TM1 magnets and sleeves already in; the T2 riser paddle marked "C" goes on the centre leaf only) onto its leaf: leaf through both Y wall slots, bar on, 2 × M3 × 8 aluminium screws, 0.3 N·m. Trim the leaf end flush with the far wall, round it.
5. Lay the leaves in the tray's root slots (L and R at level 0 rooting outboard, C at level 1 over L rooting on the −Y side), align the marked lines with the root bar edges, fit the root bars P34, 2 × M2 × 6 each, 0.15 N·m. Check by eye that each paddle hangs rolled outward by its β (4–5°) and that C's leaf clears L's paddle top by about 3 mm.
6. Thread the three nylon M3 × 10 stop screws into the stop beams, backed well off.
7. **L2 (leaf rate and stop):** clamp the tray in a vise with the leaves horizontal. Press each nail on the kitchen scale against a steel rule; read force at 2 and 4 mm. Trim free length (move the leaf in the root clamp; 1 mm = 6–7 %) until k = 0.12 / 0.15 / 0.18 ± 0.01 N/mm. Then turn each stop screw down until the stop is reached at **5.0 ± 0.3 mm** of tip travel; threadlocker. **Proof each nail to 7.5 N on its stop** for 10 s (luggage scale) and recheck free height (no set > 0.2 mm). Photograph each paddle at 0 and 5 mm (roll check).
8. Cut the boot with template P35, bond its three holes to the paddles (Sil-Poxy bead at z 26–28, cure 1 h; keep that band free of CA and varnish), lay the flange over the tray underside, add P31 and the knuckle plate P30, 6 × M2 × 8. Check every paddle swings full travel with no tug from the boot (the scale reading at 2 mm must not change by more than 0.01 N with the boot fitted). Probe every gap at the plate with the 100 µm monofilament.
9. Fit the 12 × 1.5 steel keeper disc into the lid's cone (epoxy, flush), screw the lid on (6 × M2 × 6), wrap the lid-to-tray seam with 0.05 mm PTFE tape, tie the tether eyelet. Weigh the finished hand (target ≤ 60.5 g).

### Phase B: float on the bench (about 3 h)

10. Set inserts in P21 (13 × M3). Bolt the MGN9 rail to the mast against the 1 mm reference lip, middle screw first then outward, 5 × M3 × 8, 0.6 N·m, medium threadlocker. Pull the block's end seals and wipers (keep the end caps and ball retainers), flush, one drop of oil, slide the MGN9C on (never let a block off the rail end without its retainer).
11. Riser P26 on the block (4 × M3 × 6 steel, 0.5 N·m; never longer than 6 mm or the screws touch the rail). Down-stop block P23 (insert + M3 × 16 thumbscrew + jam nut), up-stop block P24 (TPU pad), shroud P22, scale strip P25, trim cleat P27 on the mast. Upper seat P28 on the riser arm through the P47 filler (2 × aluminium M3, length per the CAD: 8 or 10 mm). Bond the D61 into the recess (CA), cover with one layer of 0.05 mm tape. Weigh the carriage side (target ≤ 29.6 g).
12. **L3 (float friction):** lay the crossbar flat (rail horizontal) and pull the carriage with thread and gram weights from the up-stop, mid and down-stop positions. Pass ≤ 0.1 N. Then clamp the crossbar so the rail is vertical.
13. Seat the hand on the wrist (key peg in its slot), **knot the tether at 25 mm** and fold it into its cup. **L6(a):** fish scale on the pull clip P46 at nail height: 1.5–2.5 N (expected 1.9–2.1) in +X, −X, +Y, −Y; straight down ≥ 5 N. Tune with tape layers. **L6(b):** tips 4–8 N pull-out; proof 7.5 N normal / 6 N lateral.
14. **L1 (dead weight):** rail vertical, hand resting on the kitchen scale with the carriage mid-travel: W1 = 0.90 ± 0.05 N; trim with M3 washers under the weight cap. Make up the +30 g and +60 g slug sets on the same scale (yellow / red tape) and read W2, W3. Per-nail shares with a 10 mm block under one nail at a time: 0.8 : 1.0 : 1.2 ± 0.1.

### Phase C: elbow (about 3 h)

15. Cut the 2020 square with the mitre box (270, 104, 80 mm), deburr; tap both ends of the 270 beam M5. Carrier beam with drop legs P11, P12 (M5 end screws plus T-nuts, 2 N·m), carrier yaw plate P9 on top. Servo into the cradle P13 with the strap P14 (2 × M3 × 10 into inserts; 2 × M2 × 6 into the servo's side holes if they line up [VERIFY]); cradle on P11 (4 × M3 × 10) with G2 (P17) under it; idler housing P15 (625-2RS pressed, one dot of CA on the outer ring) on P12 with G3 (P18), screws loose in the slots.
16. Horn adapter disc P16 on the horn (the servo's own M2 screws [VERIFY supplied]), cheek A on the disc (4 × M3 × 10). Cheek B on the shoulder screw through the bearing (M4 nyloc, 1 N·m). Crossbar assembly between the cheeks (4 × M3 × 12). **Idler alignment:** servo unpowered, swing the yoke by hand through the ±32° stops; slide the idler housing in its slots until there is no tight spot, then tighten. Insert the zero pin: it must slide in with the mast plumb to the carrier beam (engineer's square). Glue the TPU bumpers on the cradle lugs.

### Phase D: frame, hinge, arm (about 3 h)

17. Adapter P1: magnet on the magnet arm (M3 rear screw, 0.5 N·m, M3 washers to set depth), PTFE thread-seal tape on its face; pulleys P2 on M3 × 16 with nyloc nuts; spring-anchor hooks checked; electronics tray P3 on its seat (4 × M3 × 10). Frame: post and spine joined with two corner brackets; knuckle P5 on the post foot (2 × M5); keeper lever P6 (keeper plate flattened, epoxied and screwed with 2 × M3 × 6 countersunk) and cord bar P7 on the post (T-nuts); frame yaw plate P8 under the spine; reset tab P10. Pin the knuckle between the adapter ears (M6 × 80, PTFE washers, nyloc snug, free rotation). Bolt the carrier to the frame at 0° (4 × M3 × 14 [verify length]).
18. Springs: hook each spring to its anchor, run its cord over the pulley to the cord bar, tie off with the frame latched (keeper on the magnet face, hold it by hand) so each spring reads 117 mm hook to hook (6.5 N). Check on the luggage scale through each cord: 6.5 ± 0.5 N latched, 3.9 ± 0.5 N at the up-stop. Fit the reset cord through P45 to the toggle P44 at the desk edge. Up-stop screw with its rubber cap set for 25°.
19. Ballast stack and adapter onto the monitor arm (4 × M4 × 50 with washers). Clamp the arm to the desk with its steel plate; set the arm so it holds height without drift (K2.14, ≤ 2 mm in 30 min).
20. Wire the rail (§H.3 rows 1–11) and the panel (rows 13–16); tray lid on with the spare fuse taped inside. **L5 (fail-safe lift), first pass:** with the rail wired to the magnet only (servo unplugged), latch the frame, hold the button, release: film at 240 fps: ≥ 25 mm in ≤ 0.5 s, stays up, re-latches with the reset cord. Repeat with +60 g. Repeat with one spring unhooked (redundancy, D11): the module must still lift. Then the deliberate float-jam test (D10): push up at the centre nail with the float on its up-stop; record the force at which the frame lifts (expected 8–11 N).
21. Route the 340 mm DXL cable: tray → down the adapter → across the hinge with a 60 mm service loop in clip P36 → along the carrier beam → down the −Y drop leg → servo; braided sleeve, zip-tie anchors at both ends. Plug the servo. Bring-up B0–B5 (§I.7). **Zero with the pin in**, not by gravity.

### Alignment (zero pin in, module latched, foam head or 7 in ball under the hand)

- Elbow axis parallel to Y: inclinometer on the carrier beam top reads 0 ± 0.5° along Y (arm head rotation screw); cheeks square to the beam (engineer's square on cheek A).
- Rail radial and plumb: inclinometer on the mast face and side reads 90 ± 0.5° (arm head tilt for pitch, rotation for roll). Recheck after every aim change (±1° for sessions).
- Axis height: apex gauge P43 on the foam-head apex, 80 mm ring level with the axis mark scribed on cheek A (H = 80 mm).
- Nails at O: plumb line from the axis mark lands on the centre edge within ±1 mm in X; axis to centre edge 84.0 ± 0.5 mm (down-stop thumbscrew, then jam nut); outer edges 3.6 ± 0.3 mm below the centre edge (0.25 mm PETG shims under a root clamp raise that nail about 0.3 mm). Final check: on the 180 mm sphere at W1, all three nails touch together (carbon paper).
- Scale strip zeroed with the carriage on the down-stop; lock.
- Remove the zero pin. Tape marks on the arm joints for CR-ALONG, CR-CROSS, OC-ALONG, OC-CROSS once the aims are found.

22. **L4 (lift-off chord)** on the R 90 form, then B6–B14 and L7–L12, then the §K checklist.

### Aim rule for every session

The nails move 28 mm **away from the hinge (+X)** as they rise in a fail-safe lift: never aim with +X pointing at the hairline with the nails within 40 mm of it. For CROSS aims turn the module so the idler side (+Y) faces forward (guard G3 between cheek B and the eyes).

---

## K. SAFETY CHECKLIST — pre-human-test, SP1 Float-Arm specific

Fill in every line with a value or N/A, date and initial. **Any unticked box or any value outside its limit blocks the human session.** K1–K4 are done once per build state (re-done after any mechanical, tip or firmware change); K5 before *every* session. Hard limits that no protocol may exceed: per-nail normal force ≤ 2.4 N at the leaf hard stop (expected 0.6–0.9 N); total scalp load ≤ 12 N; tangential ≤ 2.0 N before the wrist breaks away; tip speed ≤ 0.4 m/s; stroke ±28° absolute; nails rise ≥ 25 mm on loss of rail power; first human sessions ≤ 5 min continuous, then ≤ 10, then ≤ 20; any tuft pull is a stop-and-redesign event; no first human session without §K complete, the wig-head test (L8) passed, safety glasses on.

Build state ID: ________  Date: ________  Initials: ____  Firmware version (from boot banner): ________

### K1. Visual

| # | Check | Limit | Measured / observed | OK |
|---|---|---|---|---|
| 1.1 | Printed parts: no cracks, delamination, stringing on frame, yoke, palm, knuckle plate, paddles, guard caps, rail shroud, VESA adapter | none | | ☐ |
| 1.2 | Load-bearing parts unchanged since proof test (L6/L7; leaf stops proofed at 7.5 N) | yes | | ☐ |
| 1.3 | All skin-accessible edges radiused: knuckle plate perimeter R ≥ 3, slot edge R ≥ 1.5, guard caps R ≥ 3, palm clamshell seam taped | R ≥ 1 mm (tips ≥ 0.4 mm) | | ☐ |
| 1.4 | Tape sharpness test (L9) passed on every tip in today's set and on guard/knuckle/paddle edges | no cut through 3 layers | tips tested: ________ | ☐ |
| 1.5 | Tips seated: each TM1 tang fully home, magnet engaged, seam sleeve in place, no rock | hand pull cannot unseat; ≥ 4 N breakaway from L6 | | ☐ |
| 1.6 | Tips: correct material, no chips, no burr (loupe), no visible wear step at the edge; A45 only if its gate (L9 at 2.4 N, L10 < 7) is on record | | | ☐ |
| 1.7 | No fastener tip, wire, zip-tie tail or burr pointing toward the scalp; no screw head below the knuckle canopy | none | | ☐ |
| 1.8 | Gaps: the shared knuckle-plate slot is ≥ 4.5 mm clear of the outer paddles and 6.0 mm of the centre paddle, sealed by the bonded silicone membrane with no sliding contact and no peeled bond; guard openings ≥ 10 mm from every moving part; **no gap 0.04–3 mm anywhere within 25 mm of hair** (palm seam taped, TM1 seams sleeved, rail/carriage above the guard) | per §B.5 table, all ≥ 3 mm | | ☐ |
| 1.9 | Nothing rotates within 30 mm of hair: elbow horn and idler at |Y| ≥ 101 mm, rail and carriage above the shroud | yes | | ☐ |
| 1.10 | Hair-probe: 100 µm nylon monofilament offered to every seam/gap below the guard (slot, membrane bonds, sleeves, palm seam, wrist, tether cup) cannot be fed in or trapped | no capture | | ☐ |

### K2. Mechanical

| # | Check | Limit | Measured | OK |
|---|---|---|---|---|
| 2.1 | **Float free:** carriage slides full travel under its own weight from the up-stop to the down-stop with the rail vertical; no catch anywhere; stiction (L3) | F_f ≤ 0.1 N (≤ 10 % of W1) | F_f = ______ N | ☐ |
| 2.2 | Carriage travel between up-stop and down-stop | 24 + e mm: 26–32 mm over the e range, 28 mm at e = 4 | ______ mm | ☐ |
| 2.3 | **Down-stop set** for today's E (geometric engagement by the apex gauge); pointer reads 0 at the down-stop; thumbscrew locked (jam nut) | E = 2 / 4 / 6 mm ± 0.3 | E = ______ mm | ☐ |
| 2.4 | **Dead weight** on the kitchen scale with the carriage floating mid-travel (L1) | W1 0.9 / W2 1.2 / W3 1.5 N ± 0.05 | W = ______ N (slug: ______) | ☐ |
| 2.5 | Per-nail share (L1c): heaviest nail / lightest nail | 1.2–1.6 (unequal preload intended; design 1.5); no nail > 0.6 N at W2 | ______ / ______ / ______ N | ☐ |
| 2.6 | **Leaf stops:** each leaf reaches its hard stop at **5.0 ± 0.3 mm** of tip travel (L2); force at the stop ≤ 2.4 N (expected 0.6–0.9 N); returns fully with no set; stop structure proofed at 7.5 N per nail | 5.0 ± 0.3 mm; ≤ 2.4 N | nail L ____ mm / ____ N, C ____ / ____, R ____ / ____ | ☐ |
| 2.7 | Leaf rate (L2) | 0.1–0.25 N/mm (design 0.12 / 0.15 / 0.18 ± 0.01) | ______ N/mm each | ☐ |
| 2.8 | **Wrist breakaway force measured** (L6a) **at nail height with the P46 clip** in +X, −X, +Y, −Y | 1.5–2.5 N (design 1.9–2.1 N); straight down ≥ 5 N | ______ / ______ / ______ / ______ N; −Z ______ N | ☐ |
| 2.9 | Tether: released hand hangs **≤ 25 mm** below the carriage, stays above the head, cannot reach the face envelope from any stroke position; tether stowed in its cup when seated | ≤ 25 mm | ______ mm | ☐ |
| 2.10 | Tip breakaway (L6b), each tip in today's set | 4–8 N | ______ | ☐ |
| 2.11 | **Fail-safe lift measured** (L5): nail-tip rise from working position to up-stop on magnet drop | ≥ 25 mm, ≤ 0.5 s (expected 33 mm, ≤ 0.14 s) | ______ mm, ______ s | ☐ |
| 2.12 | Lift springs hold the frame at the up-stop with the heaviest hand + W3 slug fitted (and with +100 g); one spring alone still lifts the module; magnet re-latches at 5 V | yes | | ☐ |
| 2.13 | Firmware limit ±28° reached before any mechanical interference (bumpers at ±32°); at ±28° with the carriage at the down-stop the centre nail is ≥ 10 mm above the sphere apex plane and the trailing outer nail **≥ 9 mm** (L4e; addendum ruling 6) | centre ≥ 10 mm, outer ≥ 9 mm | centre ______ mm, outer ______ mm | ☐ |
| 2.14 | Monitor arm: clamp tight, gas spring holds the module at the set height for 30 min with no drift; arm joints taped at the aim marks | drift ≤ 2 mm | ______ mm | ☐ |
| 2.15 | Fasteners torque-marked / nyloc / threadlocked; shake test, nothing rattles; weights captured on the post under the cap (cannot fall) | | | ☐ |
| 2.16 | Moving hand mass (carriage + wrist + hand + slug) and peak tip speed | mass ≤ 160 g; speed ≤ 0.4 m/s | ______ g, ______ mm/s | ☐ |
| 2.17 | Zero calibration done with the zero pin; pin removed; `goto 0` re-admits the pin freely | yes | | ☐ |
| 2.18 | Frame yield with the float jammed on its up-stop (D10) recorded | 8–11 N total at the nails | ______ N | ☐ |

### K3. Electrical

| # | Check | Limit | Measured | OK |
|---|---|---|---|---|
| 3.1 | Adapter: UL/ETL/CE mark visible, 5 V 4 A, output metered | 4.75–5.25 V | ______ V | ☐ |
| 3.2 | **No mains in reach:** adapter and its cord on the floor/under the desk, > 1 m from the head and from the e-stop lead; nothing above 5 V DC on the rig; no lithium cells | yes | | ☐ |
| 3.3 | **Strain relief:** adapter cord, rail leads, hold-to-run lead and DXL cable anchored with a service loop at the hinge; no conductor exposed; no cable crosses the float or the hair zone | yes | | ☐ |
| 3.4 | **Rail loop** wired exactly: adapter(+) → fuse → E-STOP (NC) → HOLD-TO-RUN (NO momentary) → [OpenRB Terminal VIN, jumper VIN(DXL)] ∥ [electromagnet with 1N5819]; logic on USB only; B3 back-feed test 0 V | per §H.1 | | ☐ |
| 3.5 | **E-stop:** press with the servo running → rail reads 0 V, servo torque gone, magnet drops, frame lifts; latches; twist-release does NOT restart motion (firmware waits for the button and the 1 s lifted hold) | 0 V, lift ≥ 25 mm | ______ V | ☐ |
| 3.6 | **Hold-to-run:** release mid-stroke → 0 V on rail, lift; 10 of 10 trials; button has no latch, no tape, no tie | 10/10 | ______ | ☐ |
| 3.7 | **Fuse** in the rail at the adapter: 1 A fast (1.25 A only if 1 A nuisance-tripped, noted on the diagram); spare in the kit | value = ______ A | | ☐ |
| 3.8 | Polarity metered at the OpenRB VIN and at the magnet before first power-up of this build state | correct | | ☐ |
| 3.9 | Logic stays up (USB) when the rail is killed (B2 outcome recorded); boot banner prints the limits table (position ±28°, velocity cap, goal current); rail-dead threshold 4.0 V (620 counts) confirmed | yes | outcome A / B | ☐ |
| 3.10 | 30-min run (L7): XL330 case, magnet, adapter temperatures | ≤ 48 °C hand-touch, ≤ 43 °C within 10 mm of skin | ______ / ______ / ______ °C | ☐ |
| 3.11 | E-stop position: under the free hand without looking in the test posture; hold-to-run lead ≥ 1.5 m | yes | | ☐ |

### K4. Functional (bench, with the mannequin, no human)

| # | Check | Limit | Measured | OK |
|---|---|---|---|---|
| 4.1 | **Position limits:** `goto ±28` reaches ±28° and no further; `gotoraw ±40` is REFUSED by the servo; pot extremes never exceed ±25° | ±28° | max seen = ______° | ☐ |
| 4.2 | Velocity limit: SPEED pot at 100 % → peak tip speed on 240 fps video | ≤ 150 mm/s nominal, ≤ 0.4 m/s hard | ______ mm/s | ☐ |
| 4.3 | **Watchdog:** `hang` (or unplug USB with the rail live) → torque off within 1 s; the rail stays live but the servo is limp and the float rests at dead weight; the hand can be lifted by hand | ≤ 1 s | ______ s | ☐ |
| 4.4 | **Over-current / stall:** block the hand with the palm at mid-stroke → goal-current limit holds tangential force at ≈ 1.2 N (spring scale) and the servo does not push through; fault → torque off; re-arm required | ≤ 1.5 N | ______ N | ☐ |
| 4.5 | Start/stop only lifted: run from any position → the servo first goes to +25°, 1 s hold, then ramps; stop → finishes at +25°, torque off | yes | | ☐ |
| 4.6 | Runaway: garbage serial input, pot wiggled during run, toggle flipped mid-stroke → motion stays inside ±28°, no jump > 25° in one step, no force above cap | yes | | ☐ |
| 4.7 | Noise at the ear position (phone SPL meter, A-weighted), HUM S3 | ≤ 70 dBA hard, ≤ 60 target | ______ dBA | ☐ |
| 4.8 | Plug-pull mid-stroke × 10: lift every time, no hang-up of the frame on the up-stop, magnet re-latches when pressed down with power on | 10/10 | ______ | ☐ |

### K5. Environment and person (every session)

| # | Check | OK |
|---|---|---|
| 5.1 | Safety glasses on before the rail is powered | ☐ |
| 5.2 | Hair: tied back / clipped away from everything except the target patch; nothing longer than 15 cm hangs toward the elbow or rail; no hair products that stiffen or tangle (gel, spray) | ☐ |
| 5.3 | No jewelry, no glasses chain, no hood/hoodie strings, no lanyard, no earbuds cable | ☐ |
| 5.4 | Clear space: 0.5 m around the rig, nothing on the desk that could fall on the head, chair stable, cradle clamped | ☐ |
| 5.5 | Phone nearby, unlocked, on the desk: timer running, voice-memo ready, 240 fps ready; a second person informed where you are if no helper is present | ☐ |
| 5.6 | E-stop under the free hand; hold-to-run in the other hand; both tested once (press/release) with the rig over the mannequin before moving it over the head | ☐ |
| 5.7 | **Per-session lift check:** one hold-to-run release with the hand over the foam head: the frame lifts fully and re-latches | ☐ |
| 5.8 | Both springs and cords inspected (no kink, hooks seated); tether in its cup; slugs captured | ☐ |
| 5.9 | Axis height re-checked with the apex gauge (printed ears can creep); rail plumb ±1° | ☐ |
| 5.10 | Tips wiped with 70 % IPA ≥ 1 min ago; hand/guard lint-rolled; black cloth under the cradle for shed-hair count | ☐ |
| 5.11 | Scalp inspected (photo, flash): no existing broken skin, rash, sunburn on the target region; not within 24 h of a haircut or chemical treatment | ☐ |
| 5.12 | Settings for the session written on the Session Log *before* starting; serial echo matches | ☐ |
| 5.13 | Session timer set to the stage limit (2 / 5 / 10 / 20 min) with an audible alarm | ☐ |

Signed: ______________  Time: ______

---

## L. BENCH TESTING (non-human), in order

Run L1–L12 in this order on each new build state; L8–L12 again whenever a tip or hand part changes. Equipment: kitchen scale (0.1 g), 0–5 N spring scale, luggage scale, steel ruler and 150 mm caliper, phone (240 fps, SPL meter, inclinometer, timer), 10× loupe, IR thermometer, 100 µm nylon monofilament, 10 mm rod + 3 layers of 50 µm tape, carbon paper or whiteboard marker, the 7 in (R 89) foam ball or a hairless foam head, a real-hair training head (one trimmed to 3–5 cm, one long), a Kanekalon wig, black card/cloth, lint roller, 15 / 50 / 100 g weights with thread and a 623ZZ pulley, hygrometer, M8 slug sets pre-weighed (+30 g, +60 g), the P46 pull clip, the P43 apex gauge, the 3 mm zero pin.

**Settings notation used in every log line, form and table:**

| Variable | Code | Levels | How it is set | How it is verified |
|---|---|---|---|---|
| Tip | TIP | W, B45, B45-12, A45 (gated), E, H (control), P | TM1 magnetic swap | letter code under the tang (random code for blinded trials) |
| Dead weight (total on three nails) | WT | W1 = 0.9 N (bare float), W2 = 1.2 N (+30 g), W3 = 1.5 N (+60 g); 0.6 N via the trim hook | weight post | kitchen scale (L1); ±0.05 N |
| Speed band (peak tip speed) | SPD | S1 ≈ 50 mm/s (pot 0 %), S2 ≈ 100 (50 %), S3 ≈ 150 (100 %) | SPEED pot at tape marks | serial echo; 240 fps video (L4) |
| Variation | VAR | V0 = 0 %, V50, V100 | VARIATION pot at tape marks | serial echo |
| Stroke direction vs hair lie | DIR | ALONG (axis parallel to the local lie; a bidirectional stroke alternates with/against), CROSS (axis ⟂ lie); for 45° tips add the loaded-edge sense ALONG-W (loaded stroke moves with the lie) / ALONG-A (against) | aim: rotate the module about vertical with the monitor-arm head swivel; mount 45° tips edge-forward or edge-back | grain map (§M-pre) + tape index marks on the arm |
| Engagement | E | 2 / 4 / 6 mm **geometric engagement** (down-stop position relative to the scalp apex, set with the apex gauge; chord ≈ 26 / 37 / 46 mm); E4 default, **E6 candidate default** if the dead weight does not float at E4 | arm height (apex gauge) vs down-stop thumbscrew; scale zeroed on the down-stop | pointer reads e − W/Σk at mid-stroke with nails on the scalp (1.4 mm at E4/W2) and 0 (down-stop) at the stroke ends |
| Mode | MODE | PER (PERIODIC: fixed 18°, no pauses), HUM (HUMAN) | toggle | serial echo |
| Region | REG | CR = crown/vertex, OC = occiput | head tilt in the cradle; arm position | scalp normal at the contact point vertical (rail vertical ±5°, inclinometer on the mast) |
| Posture | POS | SEAT (seated, tabletop face cradle), PRONE (face cushion on the bed) | — | — |
| Pitch | — | 24 mm (constant, noted; addendum D2) | — | — |

**Default condition D0** = W · W2 · S2 · V100 · ALONG · E4 · HUM · CR · SEAT. **Trial** = one condition held 30–90 s followed by a §O form. **Session** = one sitting on one day, ≤ 25 min of total scalp exposure. **Washout** = ≥ 60 s with the hand lifted (hold-to-run released) between trials, ≥ 3 min break with the head out of the cradle every 5 trials. **Day gap** ≥ 20 h between sessions on the same region; skip a day if any redness persists > 60 min.

### L1. Dead-weight calibration (kitchen scale)

**Setup.** Rig over the kitchen scale, rail vertical (inclinometer ±1°), servo torque OFF (USB only, rail dead: the frame will be at the up-stop; hold it down by hand against the stop, or latch with the rail live and the hold-to-run taped **only for this bench test, label the tape, remove it after**). Lower the arm until the nails rest on the scale pan with the carriage floating mid-travel (pointer ≈ 12–15 mm).
**Procedure.** (a) Tare the scale with nothing touching. (b) Read total W with no slug, +30 g, +60 g; repeat each 3× lifting the hand off between reads. (c) **Per-nail share:** 10 mm block under one nail only (the other two in air) and read; repeat per nail. (d) Record the pointer reading at which the scale first reads > 0 while lowering slowly (float engages) and the reading at the down-stop (jumps to the arm's full weight: do not leave it there).
**Pass.** W1 = 0.90 ± 0.05 N (92 ± 5 g), W2 = 1.20 ± 0.05, W3 = 1.50 ± 0.05; three reads within ±2 g; per-nail shares ≈ 0.8 : 1.0 : 1.2 (±0.1), no nail above 0.6 N at W2 or 0.75 N at W3; the sum of per-nail reads = W ± 10 %.
**If it fails.** W1 > 0.95 N: bare floating mass too high: aluminium screws, trim cord, lighter wrist, MGN7C (§C.6). Shares outside ratio: adjust leaf free length. Sum ≠ W: a leaf is preloaded against its stop harder than its share; stop preloads must sum below W.

### L2. Leaf rate, stop and proof

**Procedure.** Hand off the rig (or carriage locked at the up-stop). Press one nail onto the kitchen scale with the ruler against the knuckle plate; read force at 2, 4 mm of leaf deflection and at the hard stop. Repeat per leaf. Push to the stop five times and re-check the free height (set). Photograph each paddle at 0 and 5 mm (roll check). Then **proof each nail to 7.5 N at the tip with the leaf on its stop, 10 s, luggage scale** (addendum ruling 1).
**Pass.** Rate 0.1–0.25 N/mm (design 0.12 / 0.15 / 0.18 ± 0.01); hard stop reached at **5.0 ± 0.3 mm**; force at the stop ≤ 2.4 N (expected 0.6–0.9 N); zero permanent set (free height within 0.2 mm); preload per leaf recorded, sum of preloads ≤ 0.3 N above W/3-shares; proof: no slip at root or paddle clamp, no crack or whitening, free height back within 0.2 mm.

### L3. Float friction (stiction)

**Procedure.** (a) Rail horizontal (rotate the frame on the bench): thread over the pulley from the carriage, add grams until the carriage first moves; F_f = m·g; three directions of start (from the up-stop, from mid, from the down-stop). (b) Rail vertical, hand on the kitchen scale: lower the arm 1 mm at a time and log scale reading vs pointer; then raise it; the hysteresis between the curves = 2·F_f.
**Pass.** F_f ≤ 0.1 N by both methods (≤ 10 % of W1); no position with F_f > 0.15 N; hysteresis loop closes with no step > 0.1 N. **Fail:** re-oil the MGN9C, check rail straightness and bolt stress; check the tether cord, trim cord and the DXL cable are not touching the carriage.

### L4. Lift-off chord on the R 90 form

**Setup.** Foam ball/head clamped so its apex is at the nominal O (apex gauge). Carbon paper (or marker ink on the tips) over the apex. Rail live, PER mode, S1.
**Procedure.** (a) Set E = 4 by arm height (apex gauge: 80 mm ring at the axis mark; pointer 0 at the ends). (b) Run 10 strokes; measure each nail's mark length and its centre offset from the mid-stroke line. (c) Repeat at E = 2 and E = 6. (d) 240 fps video from the side at ±25°: measure the visible gap between tip and surface at the stroke ends, for the centre and the trailing outer nail. (e) `goto ±28`, carriage at the down-stop: gap to the surface for the centre and the trailing outer nail.
**Pass.** Mark lengths ≈ 25 / 36 / 44 mm at E = 2 / 4 / 6 (±5 mm; geometric expectation 26 / 37 / 46); three nails all mark; mark centres within ±5 mm of mid-stroke (else the aim/tilt is off); visible gap ≥ 5 mm at ±25° on every nail (expected 11.2 centre, 5.7 trailing outer); at ±28° centre ≥ 10 mm (expected 14.9), **trailing outer nail ≥ 9 mm** (expected 9.1); no mark continuity through the stroke end (lift really happens, no scuff at reversal). Also measure peak tip speed from the video at S1/S2/S3 (frames to cross a 20 mm mark) and note the dead-weight plateau length (where the pointer leaves 0) for the E6-as-default decision.

### L5. Fail-safe lift, redundancy and float jam

**Procedure.** Rig over the foam head, hand on it at E = 4, HUM S2. Ten times each: (a) release hold-to-run, (b) press e-stop, (c) pull the adapter plug, (d) kill USB with the rail live (watchdog path: expect limp, not lift; confirm the hand can be lifted by hand at dead weight). For (a)–(c) measure on 240 fps video: time from the event to the first nail movement and the final nail-tip height above the surface (ruler in frame). Test from the stroke ends and from mid-stroke, with W3 fitted and again with +100 g. **Redundancy (D11):** unhook one spring, repeat (a) × 3. **Float jam (D10):** rail live, servo stopped, push up at the centre nail with the float held on its up-stop until the frame yields; read the luggage scale. **Magnet hold:** after the L7 run, luggage scale pulling the keeper lever foot forward with the rail live.
**Pass.** Lift ≥ 25 mm in ≤ 0.5 s, 30/30 (expected 33 mm, ≤ 0.14 s); the frame stays at the up-stop indefinitely with any slug; re-latch takes one hand on the reset cord with power on; nothing dislodged (tips, slug); (d) torque gone ≤ 1 s, hand liftable with ≤ W + 0.2 N; one spring alone lifts the module (it need not hold the up-stop with +100 g); frame yields at 8–11 N (record it); magnet pull-off ≥ 19 N warm.

### L6. Breakaway

**(a) Wrist.** Hand seated, carriage at mid-travel, spring scale hooked to the **P46 pull clip at nail height** (addendum ruling 2; at the knuckle plate the same seat lets go at 4.3–4.7 N, which is not the test): pull slowly in +X, −X, +Y, −Y until release; read the peak. Pull straight down (−Z): must NOT release below 5 N (the dead-weight path). Re-seat and repeat 3× per direction. **Pass:** 1.5–2.5 N tangential each direction (expected 1.9–2.1 N); −Z ≥ 5 N; the released hand swings on the **25 mm tether** without dropping more than 25 mm below the carriage and stays above the head; re-seats by hand and keys to the same orientation.
**(b) Tips.** Each tip in a holder, tip down, hang weights from the tip: record the pull-out force. **Pass:** 4–8 N. Then proof-load each tip per safety §3.6 (addendum ruling 1): **7.5 N normal and 6 N lateral** on the bench (hand on the leaf stop so the stop, not the leaf, carries it) without cracking, chipping or whitening (loupe after). The separate requirement that the leaf reaches its stop at ≤ 2.4 N is confirmed in L2.

### L7. 30-minute cycle (endurance, thermal, noise, firmware)

**Setup.** Foam head, E = 6, W3, HUM S3 V100 (worst case for current and heat). Phone SPL meter at the ear position (≈ 120 mm from the module). IR thermometer.
**Procedure.** Run 30 min continuous (firmware restarts at the 20-min limit: `run` again), hold-to-run taped **for this bench test only** (label, remove after). Log at 0/10/20/30 min: XL330 case, magnet and adapter temperatures, dBA (Leq over 30 s), stroke count from serial, any fault lines, pointer behaviour (sticking), gas-arm height drift. Afterwards: shake test, fastener check, loupe on the tips, re-run L1 (W must not have changed), L3 (F_f), magnet pull-off (L5).
**Pass.** Zero faults, zero resets, zero magnet drops; temperatures ≤ 48 °C hand-touch / ≤ 43 °C within 10 mm of skin (guard underside); ≤ 70 dBA (≤ 60 target); drift ≤ 2 mm; no loosening; W and F_f unchanged within tolerance; stroke count consistent with 1–3 strokes/s.

### L8. Wig-head hair-entanglement test (real-hair mannequin)

This is the hair gate (red line 12). Run on the real-hair head at both hair lengths and on the Kanekalon wig; the full set once per build state and the 20-min endurance again after any hand/tip/boot change.
**Instruments.** Black card under the head; lint roller; hygrometer (record RH; repeat L8.4 below 35 % RH if the first run was above 50 %); 240 fps phone with a side lamp and macro clip lens; 15 / 50 / 100 g tether weights.
**Baseline.** Comb the wig 20 strokes with a wide-tooth comb; count shed hairs on the card = combing baseline B (per 20 strokes). Record comb-through force with the spring scale (pre).

1. **Static reach** (wand or the rig at rest): press each tip onto the hair at 0.3, 0.5, 1.0 N (kitchen scale under the head); side photo through the pile. Pass: visible edge-to-scalp contact at ≤ 0.5 N for all tips except H at both hair lengths.
2. **Single-stroke drag** (optional, luggage-scale sled): with-/cross-/against-grain at S1, W2; drag ≤ 0.6 N per hand with-grain; against-grain ≤ 3× with-grain and not rising along the stroke.
3. **Reversal / loop test.** 50 reversals PER S2 W2 E4 ALONG, then 50 CROSS, on the real-hair head; 240 fps on 20 reversals. Count loops, knots, shed. Pass: zero loops/knots; on video every strand released before the reversal; lift visible at both ends.
4. **Tethered-strand weight test (snag-yield).** Tie one hair (or 70 µm monofilament) to the 15 g weight over the pulley so the strand lies across the stroke path at scalp level; run 20 strokes HUM S2 W2. Then 50 g, then 100 g. Pass: the 15 g weight is never lifted (snag-yield ≤ 0.15 N target); the 50 g weight is never lifted (≤ 0.5 N hard); if the 100 g weight lifts, the wrist must break away before it rises > 20 mm. Record which element yielded (leaf torsion, float, wrist).
5. **Wrap test.** Long wig draped over the running module in every orientation the head could take (hair toward the elbow, toward the rail, over the guard edge), 5 min HUM S3 V100. Inspect the elbow horn, idler, rail, carriage, hinge, tether cord, cable. Pass: zero wraps, zero strands in any gap.
6. **Gap probe (running).** At S1, offer single hairs and small (5-strand) tufts with tweezers to the membrane bonds, slot edges, TM1 seams, palm seam, guard openings, tether cup. Pass: zero captures.
7. **20-min endurance / matting.** HUM S3 V100 W3 E6 on the 3–5 cm real-hair head, 10 min ALONG then 10 min CROSS; black card under; photo of the hair before/after; comb-through force after. Count shed hairs (bulb vs broken). Pass: shed per 100 machine strokes ≤ 2× the combing baseline per 100 comb strokes (baseline per 100 = 5·B; the 20-min run is ≈ 2,400 strokes from the serial count), no mat, comb-through force ≤ 1.5× pre.
8. **Static run.** Repeat 7 for 5 min at < 35 % RH; note fly-away and hair clinging to the tips after lift-off. Record only; if hair follows the tips up by > 10 mm, add the antistatic wipe to the cleaning list.
9. **Tip-material comparison** (log for §N, not a gate): 200 strokes per tip W, B45, B45-12, E, P, H; shed count and any capture per tip; B45 family counted per stroke sense.

**Gate to any human session:** zero wraps, zero captures, zero knots in 3/5/6; 15 g never lifted in 4; shed ≤ 2× baseline in 7; all gating items of the hair-interaction §6.8 checklist scored 2 (score sheet attached to the Session Log; the hand self-scores 29/36 with no gating zero, to be re-scored on the built hand).

### L9. Tip sharpness tape test

**Procedure.** 10 mm rod wrapped with 3 layers of 50 µm polyester or PTFE tape. For each tip in the holder on the wand: press at 1.0 N and then 2.4 N (kitchen scale under the rod) and slide 50 mm along the rod axis at ≈ 50 mm/s, three passes each direction, both edge senses for the 45° tips, then across the corners. Also test the knuckle plate edge, slot edge, guard caps and paddle noses by hand at 5 N. Inspect the tape under the loupe.
**Pass.** No cut through any layer at 2.4 N for R ≥ 0.4 tips; **A45 (R 0.3) must pass at 2.4 N too or stays gated**; no cut at 5 N for structure edges. Record per tip; re-test after 10 sessions or any drop.

### L10. Forearm skin test (self)

**Procedure.** Volar forearm, hairy side. (a) **Wand:** per tip, 10 strokes, 40 mm, ≈ 80 mm/s at 0.3 / 0.6 / 1.0 N (practise the force on the kitchen scale first). Score sharpness 0–10, forced choice scratch / stroke / pressure, pleasantness 0–10, redness at 10 min. (b) **Machine on forearm:** forearm on a folded towel under the rig, E = 4, W1, PER S1, tip H then W, 30 s each with the hold-to-run in the other hand; then HUM S2 W2 30 s with W. Score the same.
**Pass.** No tip with sharpness ≥ 7 at 0.6 N goes to the scalp; no redness beyond faint transient at 10 min; machine run: no pain, no skin marks, forearm hair not pulled; stop-on-release confirmed by feel.

### L11. Back-of-hand test (self)

**Procedure.** Back of the non-button hand flat on the towel under the rig. HUM S2 W2 E4 tip W, 30 s; then S3 W3 E6, 30 s. Move the hand ±15 mm sideways and ±10 mm up/down during the run (the float and leaves must follow with no force spike you can feel); lift the hand away quickly mid-stroke (the nails must drop to the down-stop and lift at the ends, nothing chases the hand).
**Pass.** No pain, no skin marks, no force spike on head-motion simulation, no knuckle catch; comfortable at S3 W3 (if not, note it: this becomes the first-session ceiling).

### L12. Own-palm scratch test (compliance and stop)

**Procedure.** Rig running HUM S2 W2 E4 over the foam head; push the palm of the free hand up into the moving hand from below, then from the side (±X, ±Y). Expect: float rises freely, leaves deflect, the servo stalls at ≈ 1.2 N tangential (goal current) without pushing through, nothing hurts. While the palm is loaded: release hold-to-run → everything stops and lifts within 0.5 s; repeat with the e-stop; repeat the push in the wrist breakaway direction (+X at ≈ 2 N: the hand must release onto the tether, not pin the palm).
**Pass.** Yields in all directions; stall ≤ 1.5 N by feel/spring scale; stop + lift ≤ 0.5 s every time (10/10 on hold-to-run, 5/5 on e-stop); breakaway releases rather than pins.

### L. Results table (one row per test, per build state)

| Test | Build state | Date | Key measured values | Limit | Pass? | Notes / action |
|---|---|---|---|---|---|---|
| L1 dead weight | | | W1 ___ W2 ___ W3 ___ N; shares ___/___/___ | 0.9/1.2/1.5 ± 0.05; ratio 0.8:1:1.2 | ☐ | |
| L2 leaf rate / stop / proof | | | k ___/___/___ N/mm; stop at ___/___/___ mm, ___/___/___ N; proof 7.5 N ok? | 0.1–0.25; 5.0 ± 0.3 mm; ≤ 2.4 N; no set | ☐ | |
| L3 float friction | | | F_f ___ N (horizontal), ___ N (hysteresis/2) | ≤ 0.1 | ☐ | |
| L4 lift-off chord | | | chord E2 ___ E4 ___ E6 ___ mm; gap ±25° ___/___ mm; ±28° ___/___ mm; speed S1/S2/S3 ___/___/___ mm/s; plateau at E4 ___ mm | 25/36/44 ± 5; ≥ 5; ≥ 10 centre / ≥ 9 outer; ≤ 400 | ☐ | |
| L5 fail-safe lift | | | rise ___ mm; t ___ s; n pass ___/30; one-spring lift ok?; frame yield ___ N; magnet pull-off ___ N | ≥ 25; ≤ 0.5; 30/30; yes; 8–11; ≥ 19 | ☐ | |
| L6 breakaway | | | wrist at nail height ___/___/___/___ N; −Z ___ N; tips ___; proof 7.5/6 N ok? | 1.5–2.5; ≥ 5; 4–8; no damage | ☐ | |
| L7 30-min cycle | | | T ___/___/___ °C; ___ dBA; faults ___; drift ___ mm | ≤ 48/43; ≤ 70; 0; ≤ 2 | ☐ | |
| L8 wig head | | | wraps ___ captures ___ knots ___; 15 g lifted? ___; shed ___ vs baseline ___; RH ___ % | 0/0/0; no; ≤ 2× | ☐ | |
| L9 tape test | | | tips passed: ___; A45 at 2.4 N: ___ | no cut | ☐ | |
| L10 forearm | | | max sharpness @0.6 N ___ (tip ___); redness ___ | < 7; none | ☐ | |
| L11 back of hand | | | S3 W3 tolerable? ___; spikes? ___ | yes; none | ☐ | |
| L12 palm | | | stall ___ N; stop ___ s; ___/10 ___/5 | ≤ 1.5; ≤ 0.5; all | ☐ | |

---

## M. FIRST HUMAN TEST — staged protocol

### M0. Posture setup

**Primary, SEAT:** chair at the desk, tabletop face cradle on its own stand (or a padded block) so the forehead/cheeks carry the head with the neck relaxed; trunk supported by the chair back or the forearms on the desk. The monitor arm comes over the head from the side/behind. Adjust the cradle height and tilt so that **the scalp normal at the target point is vertical**: inclinometer on the mast (rail vertical ±5°), then tilt the head until the three nails, resting at W1 with the carriage floating, touch simultaneously (helper looks; alone, feel it, then photo via a mirror). CR: head flexed ≈ 30–45°; OC: head flexed ≈ 60–80°, and if that is uncomfortable seated, OC goes PRONE. **Isolate the cradle from the desk the arm clamps to** (separate stool, or the baseboard on isolation feet) if you can feel the stroke rhythm in your forehead; note "rhythm felt in forehead: y/n" on every form.
**Alternative, PRONE:** on the bed, face in the face-cradle cushion, monitor arm clamped to the nightstand (≥ 18 mm solid top) or a floor stand within 500 mm of the occiput. Gravity is then along the occipital normal (the posture the dead weight is designed for); breathing drift 5–15 mm is inside the float travel. PRONE for OC by default and for any session where SEAT discomfort is rated > 3/10 within 5 min.
**Aiming.** Make the grain map first (M-pre). Mark the target patch with two hair clips 50 mm apart along the intended axis; a helper aligns the stroke axis to the clips, or Michael does it with a hand mirror + phone camera. Tape index marks on the monitor-arm joints for CR-ALONG, CR-CROSS, OC-ALONG, OC-CROSS so a re-aim takes < 1 min. Set the axis height with the apex gauge (H = 80 mm) and E with the down-stop. Remove the clips before running. Aim rule: the lifted nails travel 28 mm toward +X; never aim with +X at the hairline with the nails within 40 mm of it; for CROSS aims the idler side (+Y) faces forward.

### M-pre. One-off measurements (Day 0, with the wand)

Michael's hair: length (cm) at CR and OC; grain map (comb test: direction of lie at CR, whorl position and sense; at OC, lie direction, usually downward); approximate density (photo-count 1 cm²) and strand diameter (caliper on a plucked strand) if easy. Human reference: if a helper is available, 30 s of real fingernail scratching at CR and OC, rated on the §O form: this anchors "10 = a real person" on the realism scale and is the gold reference for §P. If no helper: self-scratch 30 s (note it is attenuated) and the anchor is "the best the wand ever felt".

### M-rule. The free-hand hold-to-run rule

The HOLD-TO-RUN button is in one hand for the whole run; the thumb holds it, nothing else does: **never taped, tied, latched, wedged, or held by a helper**. The other hand rests on the desk/bed under the e-stop. Letting go of the button is the normal way to end *anything*: a snag, a pull, a sharp feel, a wish to reposition, a cough. Releasing costs nothing (the firmware resumes lifted after a re-latch), so **release first, think second.** Both hands stay below the knuckle-plate plane and never go near the module while the rail is live; any adjustment (tip swap, slug, aim, re-latch) is done with the e-stop pressed in, except the re-latch itself, which is done by the reset cord with the head out of the cradle (or the nails parked ≥ 15 mm clear) and the button held.

### M-stop. Stop rules (every stage)

Release hold-to-run immediately on: any hair pull you feel (not just hear), any pain or sharp/prick event, any snag or "catch", any sensation of the hand pushing rather than resting, any unexpected sound, the module touching anything but hair, any dizziness or neck pain. Then: press e-stop, lift the head out, inspect the hand and scalp before deciding anything. **Tuft pull (more than a few strands at once) = end of session, redesign item logged, no further human testing until the fix passes L8.** Pain ≥ 4/10 = end of stage; the next attempt is at the previous (lower) setting. Any skin break = end of the programme's human testing until a safety review.

### Stage table

| Stage | Preconditions | Settings | Duration | Record | GO to next stage if | NO-GO action |
|---|---|---|---|---|---|---|
| **H0, Hand wand (Day 0)** | Wand built; tips W, B45, A45, H, P tape-tested (L9) and forearm-screened (L10a); grain map done | Hand-driven, kitchen-scale practice to 0.3–0.5 N; 10 strokes per tip, 30–40 mm, ≈ 80 mm/s; CR then OC; ALONG and CROSS | ≤ 10 min total | §O form per tip; side photo of contact fraction through the hair at 0.3 and 0.5 N; wig: 200 strokes per tip, catches/pulls counted; **blind W vs H and B45 vs H** (helper or eyes-closed swap, code read after) | nail visibly reaches skin at ≤ 0.5 N in Michael's hair; W or B45 beats H on realism by ≥ 3 points blind; zero captures in 200 wig strokes per tip; uni (B45) vs bidirectional (W) preference noted | fix the tip (reach, radius, width) before any motorised build; if nothing reaches skin, the engagement/leaf/paddle question moves to the top of §P |
| **H1, Machine off, nails resting** | §K complete (all sections); L1–L12 passed; wig gate passed; glasses; e-stop pressed in; rail dead | Tip W; **dead weight 0.6 N total** (trim-spring hook calibrated to 61 ± 2 g on the scale); E4 (E6 if L4 showed no dead-weight plateau at E4); CR; SEAT | 3 × 20 s rests, lifting the head out between | Feel: "nails or pins?"; even contact of three nails (y/n); forehead pressure comfort 0–10; any pain; then **live fail-safe check**: Michael (or a helper) powers the rail with the hold-to-run with the nails resting, then releases it → hand lifts ≥ 25 mm off the head, felt and seen | three nails felt, none sharp, pain 0; lift confirmed on the head; head withdraws freely with no hair caught | re-seat tips / re-check leaf shares (L1c); if even 0.6 N feels sharp, the tip set is wrong: back to H0 |
| **H2, PERIODIC, minimum speed** | H1 passed; W1 fitted (0.9 N), trim hook removed | PER, S1, E4, CR, ALONG, **tip H first (30 s), then tip W (30 s)**; hold-to-run in hand | 2 × 30 s, 60 s washout | §O form after each; snags; hairs on the black cloth; side video if a helper is present | pain 0–1, pulling ≤ 1, zero snags; hold-to-run released at least once mid-run and the lift felt; W rated as more "edge/nail" than H (checklist C1) | if W feels like H: tip/force problem (§P-2); if pulling > 1: check DIR vs grain and E (drop to E2) |
| **H3, HUMAN mode, 1 min** | H2 passed | HUM, S1→S2 (pot at 25 %), V100, W1, E4, CR, ALONG, tip W | 60 s | full §O form; realism, pleasure, machine-ness; snags; shed count; scalp photo at 0 and 10 min | discomfort ≤ 2, pulling ≤ 2, zero snags, no redness at 10 min; nothing on the stop list triggered | if HUM at S1–S2 feels worse than PER: note it (data for §P-7); repeat once; if discomfort > 2 at W1, the force is high for this tip: check L1 shares |
| **H4, Weight steps** | H3 passed; same day or next | HUM S2 V100 E4 CR ALONG tip W; **W1 → W2 → W3**, 45 s each, 60 s washout; e-stop in between for the slug change | 3 × 45 s | §O per step; note the first weight at which "pressing" appears (C3 = no) and at which realism peaks | each step: discomfort ≤ 3, pulling ≤ 2; stop at the first weight with discomfort > 3 and record it as W_max for this tip | W_max = W1: the usable range is below the freeze range: fit the trim hook and add a 0.6 N level to §N; W3 wanted and comfortable: the matrix top stays W3 |
| **H5, Speed steps** | H4 passed | HUM V100 E4 CR ALONG tip W at the best weight from H4; **S1 → S2 → S3**, 45 s each | 3 × 45 s | §O per step; snags per 45 s at S3; any landing "tap" or buzz noted; dBA at the ear | each step: discomfort ≤ 3, pulling ≤ 2, zero snags at S3; no buzz/tap complaint ≥ 5/10 | snags at S3: cap the matrix at S2 for this tip/direction and log; buzz: check leaf-root damping and float stiction (L3) |
| **H6, 5-min session** | H5 passed; ≥ 20 h since H3 | best (tip W, weight, speed) from H4/H5; HUM V100 E4 CR ALONG | 5 min continuous; ratings called into a voice memo every 60 s (realism, pleasure, pulling, discomfort) | §O at the end plus the per-minute series; snag count; shed count; scalp photo 0/10/60 min; posture discomfort | discomfort never > 3 and not rising > 2 points over 5 min; pulling ≤ 2; snags ≤ 1; shed ≤ 5; redness gone by 60 min; "desire to continue" ≥ 5 | realism decays > 3 points by minute 5 → log as habituation (§P-3/4); try head roll ±15° in the second half; posture > 3 → PRONE next session |
| **H7, 20-min session** | H6 passed; ≥ 20 h; scalp clear next day | same as H6; invite a slow head roll ±15° every 30–60 s; one manual re-aim at 10 min (e-stop, move to a patch 40 mm away, resume) | 20 min (the firmware's 20-min limit ends the run; voice-memo ratings every 2 min) | §O at 10 and 20 min; per-2-min series; snags; shed; scalp photo 0/10/60 min and next morning; posture; what you wanted to change | no cumulative discomfort rise > 2; no tenderness next day; snags ≤ 2 with none "felt as a pull"; shed ≤ 10; no erythema beyond mild transient; willing to run the matrix | 20 min not tolerable for posture: PRONE, or cap matrix sessions at 10 min exposure; sensation-side failures go to §P, not to a protocol change |

Exposure accounting for the first days: Day 0 = H0 only. Day 1 = H1–H3 (≈ 2.5 min). Day 2 = H4–H5 (≈ 4.5 min). Day 3 = H6 (5 min). Day 4 = H7 (20 min). Day gaps may be longer; never shorter than 20 h for H3→H6→H7. The engagement E used in H1–H7 is recorded as geometric engagement; if the L4 plateau at E4 was under 20 mm with W1, run H1–H7 at E6 and note it (addendum ruling 4).

---

## N. EXPERIMENT MATRIX

### N0. Design logic

Eight factors (tip 7, WT 3, SPD 3, VAR 3, DIR 2–3, E 3, MODE 2, REG 2) are far beyond any full factorial for one tester (≈ 6,800 cells); nail pitch is a noted constant at 24 mm (addendum D2). SP1 is a research rig whose first job is to find **any** condition that reads as fingernails, then learn which knobs move that reading. The design is sequential: (1) **Screening (S):** wide, fast, un-replicated, all at D0 plus one-factor swings, looking for the first "yes" (realism ≥ 6); 45 s trials. (2) **One-factor-at-a-time (OFAT):** around the best screening condition, each factor over its full range, two replicates, order randomised within the session. (3) **Paired A/B:** the hypothesis-bearing contrasts, blinded where feasible, ABBA order, replicated across sessions. (4) **Endurance:** one 20-min run at the final best condition with the per-2-min series (habituation). **Realism rule for ordering:** the realism scale (§O Q1) is the primary outcome; pleasure (Q2) secondary; "desire to continue" (Q9) tertiary. Pulling (Q5) and discomfort (Q6) are constraints (a condition with Q5 or Q6 > 3 is excluded from "best" regardless of Q1).

### N1. Settings and gating

- A45 enters only after L9 at 2.4 N and L10 (sharpness < 7 at 0.6 N), then at W1–W2 only, never W3.
- B45, B45-12, A45, E and P are 45°-faced (unidirectional loaded edge): in bidirectional strokes their return is a back-of-blade glide. Record the loaded sense (ALONG-W / ALONG-A). W and H are symmetric. E's edge sits 4 mm lower: raise the down-stop 4 mm for E so its geometric engagement matches.
- E = 6 and S3 are allowed only after H5/H4 showed them tolerable; otherwise cap at E4 / S2 and log. If E6 became the working default in the H-stages (no dead-weight plateau at E4), treat E6 as D0's engagement and sweep E4/E8 around it.
- OC sessions are PRONE unless SEAT at 60–80° flexion was comfortable in the H-stages.
- Pitch 24 mm is constant; the Sensation Gate's ruling on it is attached to the session log.

### N2. Screening phase (sessions 5–8; 45 s trials; 60 s washout; ratings after each)

| Session | Purpose | Trials (each = D0 with the stated change) | n trials | Exposure |
|---|---|---|---|---|
| S-A (5) | Tip screen, crown | TIP ∈ {H, W, B45, B45-12, E, P} at D0 (B45/B45-12/E/P mounted ALONG-A, loaded against the lie, the human occiput primitive; on the crown use the whorl-outward sense as "with"). Order randomised by helper/script; tip codes blind. Then the two best plus H repeated in reverse order | 9 | ≈ 7 min |
| S-B (6) | Tip screen, occiput (PRONE) | same six tips at D0 with REG = OC; then the two best plus H reversed | 9 | ≈ 7 min |
| S-C (7) | Mode × variation screen | best tip from S-A/S-B at its region: PER; HUM V0; HUM V50; HUM V100; then the same four at the other region. Mode blinded by the firmware BLIND command (`bset`/`blind`/`next`/`reveal`) or a helper flipping the toggle | 8 | ≈ 6 min |
| S-D (8) | Direction × engagement screen | best tip, best mode/variation, primary region: DIR ∈ {ALONG, CROSS} × E ∈ {2, 4, 6}; for 45° tips add ALONG-W vs ALONG-A at E4 | 6–8 | ≈ 6 min |

**Screening exit:** the best condition **C\*** (highest realism with Q5, Q6 ≤ 3). If no trial reaches realism ≥ 4 in S-A/S-B, do **not** continue to S-C/S-D on the machine: run the wand on the same patch the same day at the same tips (the wand-vs-machine comparison is §P-7's data) and go to §P.

### N3. OFAT phase (sessions 9–13; 60 s trials; 60 s washout; 2 replicates each, order randomised)

| Session | Factor swept | Levels | n trials |
|---|---|---|---|
| O-1 (9) | WT | W1, W2, W3 (+ 0.6 N via trim hook if H4 said W1 was already "pressing") | 6–8 |
| O-2 (10) | SPD | S1, S2, S3 | 6 |
| O-3 (11) | E | 2, 4, 6 (or 4, 6, 8 if E6 is the working default) | 6 |
| O-4 (12) | VAR and MODE | PER, V0, V50, V100 | 8 |
| O-5 (13) | DIR (and sound) | ALONG, CROSS (+ ALONG-W vs ALONG-A for 45° tips); then C* with foam ear plugs vs without | 6–8 |

**OFAT exit:** update C* if any level beats the previous best by ≥ 1.5 points on realism averaged over its two replicates; note monotone trends (e.g. realism rising with WT up to W3 means the force window is above the freeze range → §P-6).

### N4. Paired A/B phase (sessions 14–19; 45 s per arm; ABBA within a pair; 60 s washouts; 4–5 pairs per session; order of pairs randomised per session)

| Pair | A | B | Hypothesis tested | Blinding | Region(s) |
|---|---|---|---|---|---|
| P1 | C* | C* with TIP = H | sanity: an edge beats a ball (massager-vs-scratcher) | tip code | primary |
| P2 | C* (HUM V100) | same, PER | irregularity is a large part of "fingernails" (DECISION hypothesis) | BLIND command / helper toggle | both |
| P3 | C* | same with V0 | which part of HUM matters: jitter vs episodes/pauses | BLIND / helper toggle | primary |
| P4 | W | B45 (loaded ALONG-A) | symmetric bidirectional rake vs nail-mimic 45° | tip code | both |
| P5 | B45 | B45-12 | width (hair collection vs reach) | tip code | primary |
| P6 | C* | same with TIP = P | zero-fabrication real-nail reference vs printed edge | tip code | primary |
| P7 | C* | same with TIP = E | damping / soft backing in the tip | tip code | primary |
| P8 | ALONG | CROSS | direction vs lie | none (aim is visible) | primary |
| P9 | E4 | E2 (or E6 vs E4 if E6 is the default) | engagement/chord | none | primary |
| P10 | best WT | adjacent WT | force window edge | slug swapped out of sight | primary |
| P11 (gated) | C* | same with TIP = A45 | radius 0.3 vs 0.4–0.5 | tip code | primary, W1–W2 only |

Count: 11 pairs, P2 and P4 at both regions → 13 pair-blocks × ABBA (4 arms) = 52 arms × 45 s ≈ 39 min of exposure over 6 sessions (≈ 2 pair-blocks + 1 single-block per session, ≈ 7–9 min exposure each). Each pair's forced choice ("which was more like fingernails / more pleasant") plus the two §O forms. **Win rule:** a pair is decided if the same arm wins ≥ 3 of 4 ABBA presentations on the forced choice *and* the mean realism difference is ≥ 1 point; otherwise "no difference" (itself a result: that knob does not matter at this precision).

**Blinding mechanics.** Helper present: helper swaps tips/slugs and flips the toggle behind the head while Michael's eyes are closed and the e-stop is pressed; helper records the condition; Michael rates before being told. No helper: tips carry random two-letter codes under the tang; Michael presses e-stop, closes eyes, picks the next tip from a shuffled box by the order printed by a script (`python3 -c "import random; l=['A','B','B','A']; random.shuffle(l); print(l)"`), seats it, runs, rates, then reads the code. Mode blinding without a helper uses the firmware BLIND command (`bset 1 per -1 -1`, `bset 2 hum -1 100`, `blind 2`, `next`, `reveal`).

### N5. Endurance (session 20)

C* for 20 min with the per-2-min series as in H7; one re-aim at 10 min; head roll invited. This is the habituation curve that §P-3/4 reads.

### N6. Session count, length, washout

- **Sessions:** 0 (H0) + 4 (H1–H7) + 4 (screening) + 5 (OFAT) + 6 (A/B) + 1 (endurance) = **20 nominal**; minimum 15 if S-C/S-D are folded into OFAT and A/B is cut to P1, P2, P4, P8 (the four that carry the hypothesis); maximum 25 if A45 is admitted, the second region is replicated in OFAT, or any session is repeated for a stop-rule abort.
- **Session length:** 20–35 min wall-clock, ≤ 10 min scalp exposure in S/OFAT/A/B sessions, 20 min in H7 and N5.
- **Washout:** 60 s lifted between trials; 3 min out of the cradle every 5 trials; ≥ 20 h between sessions; a rest day after any session with redness > 60 min or snags ≥ 2.
- **Order of days:** H-stages → S-A → S-B → S-C → S-D → OFAT → A/B → endurance; A/B pairs can be interleaved with OFAT days if a factor is already settled.
- **Replication:** screening unreplicated (by design); OFAT 2×; A/B 4 arms per pair; endurance 1× (2× if the first shows a clear decay).

---

## O. FEEDBACK FORM (one per trial; print; fill within 60 s of the trial while the head is still in the cradle: voice memo first, paper after)

**Session ___  Trial ___  Date ______  Time ______  Build state ______**

| Field | Value |
|---|---|
| TIP (code if blind) | ______ |
| WT (W1/W2/W3/0.6) | ______ |
| SPD (S1/S2/S3) | ______ |
| VAR (V0/V50/V100) | ______ |
| DIR (ALONG / ALONG-W / ALONG-A / CROSS) | ______ |
| E (2/4/6/8 mm, geometric) | ______ |
| MODE (PER/HUM/BLD) | ______ |
| REG (CR/OC) · POS (SEAT/PRONE) | ______ · ______ |
| Settings code from the `C,` line | ______ |
| Duration (s) | ______ |
| Snags count (felt catches) · of which pulls felt | ______ · ______ |
| Hairs shed on cloth/roller (with bulb · broken) | ______ · ______ |
| Ear plugs (y/n) · rhythm felt in forehead (y/n) | ______ · ______ |

**Rate 0–10** (0 = none/not at all, 10 = extreme/perfect; anchor Q1 on the human reference from M-pre = 10, tip H on the machine ≈ 0–2):

| # | Scale | 0 ———————————— 10 | Score |
|---|---|---|---|
| Q1 | **Scratch realism**: "this is someone's fingernails" | not at all → exactly | ___ |
| Q2 | Pleasure | none → wonderful | ___ |
| Q3 | Intensity | can barely feel it → as hard as I'd want | ___ |
| Q4 | Tingle / ASMR / shiver | none → strong | ___ |
| Q5 | Hair pulling | none → painful pull | ___ |
| Q6 | Discomfort / pain | none → stop now | ___ |
| Q7 | Perceived coverage | one line → whole region being worked | ___ |
| Q8 | Noise annoyance | silent → intolerable | ___ |
| Q9 | Desire to continue | want it off → don't stop | ___ |
| Q10 | **Machine-ness**: "I can tell it's a machine" | never → constantly | ___ |

**Massager-vs-scratcher checklist (as felt), Y / N:**

| # | As felt | Y/N |
|---|---|---|
| C1 | An edge, not a pad: I feel a line/nail, not a dome or finger pad | ___ |
| C2 | It reaches my skin (not riding on the hair) for most of each stroke | ___ |
| C3 | It is light: resting, not pressing | ___ |
| C4 | It slides across the skin; the skin does not move with it | ___ |
| C5 | Right speed: scratching, not flicking/brushing, and no buzz/vibration | ___ |
| C6 | Hair is moved near the root (I feel the follicles), not just the ends | ___ |
| C7 | Feels like several separate fingers, not one comb | ___ |
| C8 | Irregular: I cannot predict the next stroke | ___ |
| C9 | Follows my head: no force spikes when I move/breathe | ___ |
| C10 | It unloads at the ends of strokes: no dragging reversal | ___ |
| C11 | No hair caught anywhere during or after | ___ |
| C12 | Sounds like a scratch, not a motor | ___ |

**Free text:** What would make it more like a person? ______________________________________________
Anything sharp, any tap/landing, any pattern you noticed, where you wanted it to go next: ______________________________________________

**Pair trials only:** this arm vs the other arm: more like fingernails: A / B / same; more pleasant: A / B / same.

**CSV header line** (one row per trial; append to `sp1_trials.csv`):

```
session,trial,date,time,build_state,tip,tip_code,wt_N,spd,var,dir,e_mm,mode,region,posture,settings_code,duration_s,snags,pulls_felt,shed_bulb,shed_broken,earplugs,forehead_rhythm,q1_realism,q2_pleasure,q3_intensity,q4_tingle,q5_pulling,q6_discomfort,q7_coverage,q8_noise,q9_continue,q10_machine,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,pair_id,pair_arm,fc_realism,fc_pleasure,free_text
```

---

## P. ITERATION MAP — what SP1 outcomes imply for SP2

Read after the screening phase and again after the A/B phase. "Realism" = Q1 mean at the best condition.

| # | Outcome pattern (as it shows in the data) | What it means | SP2 / Stage-3 change | SP1 data that justify it |
|---|---|---|---|---|
| P-1 | **Nothing reaches skin:** C2 = N on all tips at E6 W3; realism ≤ 3 everywhere; wand side-photos show the edge riding on the pile; C6 = N | The canopy problem, not the mechanism: 8 mm edges at ≤ 0.5 N cannot part Michael's hair | Engagement first: E 8 mm (down-stop range), stiffer leaf preload, narrower/longer paddles (≥ 25 mm protrusion), narrower tip (nail-corner 4 mm at ≤ 0.4 N); if the wand also fails → hair-parting is a tip-geometry problem (SP2 tip programme before any new mechanism) | S-A/S-B contact-fraction photos; H0 side photos at 0.3/0.5 N; O-3 (E) flat; O-1 (WT) flat |
| P-2 | **Feels like a comb / sweep:** C1 = Y but C7 = N and free text says "comb"; realism 3–5; B45-12 ≤ B45 ≤ W or all equal; realism rises with WT monotonically to W3 | Line load too low for the edge radius (glide region) or three phase-locked lines read as teeth | Tip radius/width/force: R 0.3 (A45) admitted; 4 mm loaded edge (nail-corner); per-nail ≥ 0.4 N (trim the range up, cap stays 2.4 N); carrier yaw stagger 15–20° so the lines are not parallel; 4th nail; revisit the 24 mm pitch (Sensation Gate) | P4/P5/P11 pair results; O-1 monotone trend; C7 pattern |
| P-3 | **High realism only in HUMAN:** P2 shows HUM ≫ PER (≥ 2 points), V100 > V0 (P3), but the endurance curve decays > 3 points by minute 5 even in HUM | Irregularity in time works; irregularity in *place* is missing (single patch habituates) | **Stage 3 yaw servo** (XL330 ID 2 at the internal yaw joint on the lazy-Susan bearing): direction wander ±15–30° and start-point drift in the air; episodes every 5–20 s that change region; head-roll invitation stays | P2/P3 wins; N5 and H7 per-2-min series; the 10-min re-aim restores ≥ 2 points |
| P-4 | **Realism good but habituates:** realism ≥ 6 in the first 2 min of every run, then decays; manual re-aim restores it; free text "wants to move" | The contact is right; the pattern needs region change and longer episodes | Episodes/wander: yaw servo + firmware episode engine (sweeps, pauses, region changes); then SP2 full-coverage | N5 decay slope vs re-aim recovery; Q7 coverage low with Q1 high |
| P-5 | **Pulls hair:** Q5 ≥ 3 at any condition; snags cluster by DIR (ALONG-A ≫ ALONG-W) or by E (E6 ≫ E2) or by SPD (S3) | Direction, lift geometry, or boot/paddle capture | Direction: lock against-grain strokes to ≤ 25 mm (firmware amplitude by direction, needs yaw/aim knowledge); lift: lower E, add a reversal force-dip (float micro-lift via a magnet pulse or a 4th servo in SP2); boot: if shed hairs are found at the slot, redesign the membrane/paddle clearance; **any tuft pull: redesign before any further human session** | O-5 snags by DIR; O-3 by E; O-2 by SPD; L8 repeated with the hair pushed into the mechanism; shed counts with bulbs |
| P-6 | **Too weak / too strong:** realism peaks at W1 with "pressing" already at W2 (too strong) or rises monotonically to W3 and C3 = Y still (too weak) | The 0.9–1.5 N window is misplaced for this tip | Weight: add the 0.6 N trim level or extend the slug range to 2.0 N total (per-nail stays ≤ 0.75 N, cap 2.4 N); SP2: constant-force spring float (orientation-independent) and the load cell in the wrist slot for a measured force–pleasure curve | O-1 shape; H4 W_max; per-nail shares from L1c |
| P-7 | **Good on the wand, not on the machine:** H0 realism ≥ 7 for a tip, machine ≤ 4 with the same tip, same patch, same day; free text "taps", "metronome", "step in the middle" | Kinematics/stiction: landing taps, mid-stroke float reversal, fixed-duration events, servo gear ripple | Kinematics: trapezoid in-contact profile, land at ≤ 25 mm/s or plough in while moving, randomise every fixed-duration event; measure F_f again; SP2: head-centred yoke (concentric arc removes the mid-stroke float reversal) or a back-drivable gimbal FOC stroke axis (silent, impedance) | Wand-vs-machine paired ratings; L3 stiction; 240 fps of landings; C5/C9/C10; Q10 high with Q8 low |
| P-8 | **Posture intolerable:** neck/forehead discomfort > 3 within 5 min seated; sessions cut short for posture, not sensation | The rig's physics are fine; the human cannot hold the pose | PRONE as the default (nightstand/floor-stand clamp, face cushion); SP2: reclined/side-lying needs a constant-force float | H6/H7 posture field; forehead-rhythm y/n |
| P-9 | **Machine-ness high even when realism is fair:** Q10 ≥ 6 with Q1 ≥ 5; ear plugs (O-5) drop Q10 by ≥ 2 | Sound/vibration is the tell | Isolation (cradle off the arm's desk, servo muff, rubber at the VESA adapter); SP2: silent direct drive (gimbal + SimpleFOC) on the stroke axis | O-5 ear-plug pair; K4.7 dBA; forehead-rhythm y/n |
| P-10 | **PERIODIC ≈ HUMAN, both ≥ 6** | The per-stroke contact physics carries the sensation; the rank-1 variable matters less than modelled at this patch size | Machine done for SP1's question; spend on tips, regions, sessions and the full-coverage SP2; keep the pattern engine simple | P2/P3 "no difference"; endurance curve flat |
| P-11 | **Three nails read as three scratchers:** C7 = N while C1, C2 = Y; realism 4–6; free text "three things", "rake" | Hand illusion needs per-finger asynchrony/force spread | SP2 hand: per-finger phase/force (pendulum fingers or a tendon hand on the same float); carrier yaw stagger as the cheap first step; a pitch experiment (20 vs 24 mm) | C7 pattern; P4 (W vs B45) indifferent; single-nail OFAT (remove two tips) if run |
| P-12 | **Realism high only at OC (prone) and low at CR seated, or vice versa** | Region/posture confound: gravity alignment, hair lie, follicle density | Keep the winning posture; SP2 coverage design targets the winning region first; re-check rail verticality in the losing posture | S-A vs S-B; O-5 at both regions; inclinometer logs |

### P-GO. "Go to SP2 full-coverage" criteria (all must hold)

1. A condition C* exists with realism ≥ 7 and pleasure ≥ 7 on ≥ 2 separate sessions, with Q5 ≤ 2 and Q6 ≤ 2.
2. "Desire to continue" ≥ 7 at C*, and H7/N5 show either ≤ 2 points of decay over 20 min **or** decay that a manual re-aim reliably restores (≥ 2 points back within 1 min): the unmet need is *place*, which coverage solves.
3. Zero tuft pulls across all sessions; shed ≤ 10 per 20 min; no scalp finding beyond transient redness.
4. The massager-vs-scratcher checklist at C* has C1, C2, C3, C4, C6 = Y on ≥ 80 % of trials.
5. The wand does not beat the machine by more than 1 point at the same tip (otherwise fix the kinematics first, §P-7).
6. The HUM-vs-PER result is known (either direction), so SP2 knows whether to carry the pattern engine or simplify it.

### P-STOP. "Abandon this mechanism" criteria (any one is sufficient; the *contact* findings transfer regardless)

1. After the full matrix, no condition reaches realism ≥ 5 **while the wand reaches ≥ 7** with the same tips on the same patch: the stroke generator, not the contact, is wrong, and no OFAT trend points to a fix inside the SP1 envelope.
2. Nothing reaches skin (P-1) at E6/W3 on every tip **and** the wand also fails → a different hair-parting approach (tendon hand, narrower tines, two-stage part-then-scratch), not a Float-Arm revision.
3. Hair pulling Q5 ≥ 4 persists at every DIR × E × SPD combination after one boot/paddle fix cycle, or any tuft pull reproduces after one fix cycle.
4. Machine-ness Q10 ≥ 7 at all settings *with* ear plugs and the cradle isolated: the kinematic signature itself reads as a machine → SP2 is a different stroke generator (yoke or FOC), not more SP1.
5. Posture: neither SEAT nor PRONE tolerable ≥ 10 min after two attempts each: a head-worn or reclined architecture is needed, which this float cannot serve.

---

## QUICK REFERENCE CARD (print, keep at the rig)

**Settings codes:** TIP W / B45 / B45-12 / A45 (gated) / E / H (control) / P · WT W1 0.9 N (bare) / W2 1.2 N (+30 g yellow) / W3 1.5 N (+60 g red) / 0.6 N (trim hook) · SPD S1 50 (pot 0 %) / S2 100 (50 %) / S3 150 mm/s (100 %) · VAR V0 / V50 / V100 · DIR ALONG / ALONG-W / ALONG-A / CROSS · E 2 / 4 / 6 (/ 8) mm geometric, apex gauge · MODE PER / HUM / BLD · REG CR / OC · POS SEAT / PRONE. **D0** = W · W2 · S2 · V100 · ALONG · E4 · HUM · CR · SEAT. Firmware code `MODE-S<spd%>-V<var%>-C<mA>#<hash>` from the `C,` line goes on every form.

**Tip codes:** random two letters under the tang (no W, B, A, E, H, P); key card with the helper or in the envelope; count tips in and out of the box.

**Before every session (K5):** glasses on → hair clipped, nothing > 15 cm toward the module → clear 0.5 m → phone timer/voice memo/240 fps → e-stop under the free hand, button in the other, both tested over the mannequin → one lift check over the foam head → springs, cords, tether cup, slugs captured → apex gauge 80 mm ring at the axis mark, rail plumb → tips IPA-wiped ≥ 1 min ago → scalp photo → settings on the log before starting → timer with alarm at the stage limit (2 / 5 / 10 / 20 min).

**Hard limits:** ≤ 2.4 N per nail at the leaf stop (expected 0.6–0.9) · ≤ 12 N total · ≤ 2.0 N tangential (wrist lets go at ~2 N) · tip speed ≤ 0.4 m/s (cap 0.36) · ±28° absolute · nails rise ≥ 25 mm in ≤ 0.5 s on rail loss (expect 33 mm in 0.14 s) · sessions ≤ 5 → 10 → 20 min · ≤ 25 min scalp exposure per sitting · ≥ 20 h between sessions on a region.

**Stop rules:** release the button on any felt hair pull, pain or prick, snag or catch, "pushing not resting", unexpected sound, module touching anything but hair, dizziness or neck pain. Then e-stop, head out, inspect hand and scalp. Tuft pull = session over, redesign item, no human test until L8 passes again. Pain ≥ 4/10 = stage over, next attempt one setting lower. Skin break = programme pause for a safety review.

**Hold-to-run:** thumb only. Never taped, tied, latched, wedged or held by a helper. Release first, think second. Hands below the knuckle plane while the rail is live; adjustments with the e-stop pressed in.

**E-stop reset and re-latch:** twist-release the mushroom → nothing moves → head out of the cradle (or nails parked ≥ 15 mm clear) → hold the button (rail live, magnet energised, firmware INIT parks the arm at +25°) → pull the reset cord (~10 N) or press the reset tab (~11 N) until the keeper clicks onto the magnet → let the cord go slack → firmware holds 1 s lifted, then strokes. Every button release lifts the frame and needs this re-latch: that is intended.

**Firmware FAULT (LED 10 Hz):** read the `H,` fault field (`comm_loss`, `over_current`, `hw_error`, `motion_timeout`, `zero_out_of_range`, `config`); release the button; fix the cause; type `reset` → INIT. **Serial essentials:** `status`, `limits`, `run`, `stop`, `reset`, `zero` (pin in!), `goto ±28`, `spd 0|50|100`, `var 0|50|100`, `mode human|periodic`, `cur 300`, `seed 42`, `bset`/`blind n`/`next`/`reveal`.

**Fuse:** 1 A fast 5 × 20 at the adapter (1.25 A only if noted on the diagram); spare inside the tray lid. **Rail:** 5 V only after fuse → e-stop (NC) → button (NO) → OpenRB VIN (jumper VIN(DXL)) ∥ magnet. **Never** feed the magnet from anywhere else; **never** jumper USB(5V).

**After every session:** e-stop in; brick unplugged first; USB out; lint-roll hand, plate, boot, guard, cloth; count hairs (bulb / broken); tips out, IPA (soap for P), loupe; check seams and the membrane for trapped hair (a found hair is a design item); cradle pad wiped; weights off or captured; hand re-seated; cords inspected; arm parked; cables coiled with service loops; scalp photo reminders at 10 and 60 min; CSV row appended; log filed. Weekly: L3 and L1, re-oil the MGN9C, replace the membrane if cut or stretched, tape-test any tip past 10 sessions.

---

## APPENDIX 1. INTEGRATION NOTES (every resolution the integrator made; for the gates)

Precedence applied: addendum > mechanical.md > tips.md > electronics-firmware.md > test-protocols.md > freeze. Items marked **[CONFLICT]** in the text could not be resolved from the documents and are listed with both values.

1. **[CONFLICT] Module post length.** Addendum D8 rules 104 mm (calling the lead's 90 mm a typo); mechanical.md §2 (Z 92–196), §5.1, §12 and §13 all say 104 mm; the BOM cut list says 104 mm; **the frame CAD generator `cad/frame/gen_frame_stl.py` models the post as 122 mm (Z 94–216) and refers to its own `CONFLICTS.md` item C-F1.** Addendum wins on paper (104 mm) and §C.1 says 104 mm, but the CAD may have found that the spine, cord bar and knuckle sockets need 122 mm. **Resolution for the builder:** do not cut the post until `cad/frame/CONFLICTS.md` is read; cut to the length the released frame CAD uses, and tell the build reviewer which. A 500 mm bar covers either.
2. **Tip proof load.** safety §3.6 (≈ 7.5 N normal, 6 N lateral, 3× rated) vs test-protocols L6(b) (2.4 N on the leaf stop). Addendum ruling 1 resolves: L6(b) and L2 amended to proof the stop structure and each tip at 7.5 N (6 N lateral), and to confirm separately in L2 that the leaf reaches its stop at ≤ 2.4 N (expected 0.6–0.9 N). Applied in §G.4, §J step 7, §K1.2, §K2.6, §L2, §L6(b).
3. **Wrist breakaway test point.** mechanical §7.2 and addendum ruling 2: L6(a) now pulls at nail height with the P46 clip, 1.5–2.5 N (expected 1.9–2.1 N); at the knuckle plate the same seat lets go at 4.3–4.7 N and that is explicitly not the test. Applied in §C.5, §J step 13, §K2.8, §L6(a).
4. **Tether 25 mm, not 60 mm.** Addendum ruling 3 overrides freeze §1.6 and mechanical §7.3/§6.5 (which still say 60 mm in places). Applied in §B.1, §C.6, §J step 13, §K2.9, §L6(a), BOM row 2.11.
5. **Engagement definition and E6.** Addendum ruling 4: E is geometric engagement set with the apex gauge; the pointer reads e − W/Σk; E4 default, E6 candidate default if the dead weight does not float at E4. test-protocols §0 ("pointer reads E at mid-stroke") amended; E6 added to §M (H1 note), §N1, N3 O-3 and P9. Applied in §C.2, §L settings table, §L4 (plateau measurement).
6. **Rail brown-out threshold 4.0 V.** Addendum ruling 7 vs the firmware as written (`analogRead(A2) > 400` ≈ 2.6 V on the rail) and electronics-firmware.md §1.2 ("read-only, 2.5 V when live", threshold ~1.3 V). Resolved in favour of the addendum: §I.6 gives the one-line edit (threshold 620 counts = 2.0 V at A2 = 4.0 V rail) and K3.9 checks it. The build reviewer must confirm the edit is made before B1.
7. **Servo zero by pin.** Addendum ruling 5 vs electronics-firmware.md §4.2 / B5 and firmware README ("hand hanging freely"). Resolved: §I.3, B5 and §J step 21 use the 3 mm pin through cheek A and the cradle flange; the firmware help text should be reworded (§I.6 edit 2); the INIT sanity check (±40°) is unchanged.
8. **K2.13 / L4(e) at ±28°.** test-protocols asked ≥ 10 mm; mechanical §9.1 shows the trailing outer nail at 9.1 mm because of the frozen ±8 mm stagger; addendum ruling 6 amends to ≥ 9 mm for the outer nails (centre ≥ 10 mm, expected 14.9). Applied in §C.2, §K2.13, §L4.
9. **Leaf travel 5.0 mm, not 8–10 mm.** Addendum D5 vs freeze §1.7, test-protocols K2.6 and L2 (8–10 mm). Amended to 5.0 ± 0.3 mm everywhere (§B.1, §C.3, §K2.6, §L2).
10. **Carriage travel.** test-protocols K2.2 asked 25–30 mm; mechanical §6.3 gives 24 + e = 26–32 mm over the e range (28 at e = 4). Amended to 26–32 mm in §K2.2.
11. **Pitch 24 mm.** Addendum D2 vs DECISION hypothesis, freeze §1.7 and the older parts of tips.md (20 mm). Package states 24 mm everywhere, with a footnote in §A.2 and a "noted constant" line in §L settings and §N1; §P-2/P-11 keep a pitch experiment for SP2. The Sensation Gate must rule on it.
12. **MGN9C, not MGN9H.** Addendum D7 vs freeze §1.5 and test-protocols L3 fail text and the packing list ("re-oil the MGN9H"). Amended throughout (§B.1, §D.3, §L3, packing list).
13. **Two springs.** Addendum D11 vs freeze §1.3 (one spring 6–10 N). Package: two springs at 6.5 N each; single-spring redundancy added to L5 and K2.12.
14. **Servo beside the palm on a yoke with an idler.** Addendum D6 vs freeze §1.4–1.5 (servo above, arm bracket on the horn). Package describes the yoke only; the build reviewer checks the idler alignment procedure (§J step 16) and the idler's hair exposure (G3, §B.5).
15. **Lift-off clearance at ±25°.** Addendum D12: 15.9 mm along the arm for the free tip at the down-stop (11.2 mm vertical centre, 5.7 mm trailing outer), not the freeze's 19.9 mm (which is for L = 80). electronics-firmware.md §4.1 ("19.9 mm gap") corrected in §I.1.
16. **Coordinate frame.** Addendum D9: scalp sphere centre (0, 0, −86), apex Z +4; freeze §0's (0, 0, −90) superseded. Applied in the front matter and §C.1.
17. **Stage-1 yaw by the arm head swivel.** Addendum ruling 8 vs freeze §1.4(a) and test-protocols §Q6 (45° holes on the internal joint). Package: the internal joint keeps its 45° insert pattern (P8) but is used only at 0°/180° in Stage 1; aim is by the arm's head swivel and tape marks (§B.1, §B.2, §L DIR row).
18. **Proof of the leaf stop structure (7.5 N) added to L2 and K1.2**, and the deliberate float-jam test (D10, frame yield 8–11 N), the single-spring redundancy test (D11), the magnet pull-off check (≥ 19 N warm) and the per-session lift check (K5.7) added from mechanical §14, as the addendum asks. D10 itself is left for the Safety Gate (§B.6 states the residual).
19. **DXL cable length.** electronics-firmware.md row 12 says the cable "supplied with the servo"; mechanical §3.3 shows the route needs ≥ 340 mm. Resolved in favour of mechanical (BOM row 6.18); row 12 in §H.3 amended.
20. **Hold-to-run housing CAD file.** electronics-firmware.md names `cad/handheld_button.scad`; mechanical P39/P40 and the frame CAD own it. Package indexes it under the frame CAD (expected `p39_p40_handheld_button.scad`).
21. **Riser-to-seat screws.** mechanical §6.5 counts 2 × M3 × 8 aluminium (0.4 g); §12 and §13 step 11 use 2 × M3 × 10 steel through the P47 filler. Resolved per the BOM: aluminium, length (8 or 10 mm) per the released CAD (§J step 11, BOM 3.09).
22. **Screws missing from mechanical §12** (tray P3 to adapter 4 × M3; cradle to drop leg 4 × M3; P45 guide 2 × M3 with nuts; button housing 2 × M3 × 16–20) added by the BOM to table 3A; kept with [verify] tags. M3 × 14 yaw-plate length and M5 × 12/16 reach are [verify] against the CAD.
23. **Lift-off chord targets.** test-protocols L4 (25 / 36 / 44 ± 5 mm) vs mechanical §9.2 (26.2 / 37.4 / 46.1). Both kept: protocol targets with the geometric expectation in brackets (inside tolerance).
24. **Freeze §1.7 "1 mm paddles"** superseded by addendum D1 (tip lead's paddle_with_pocket); §B.1 and §F.3 describe the real paddle. **Freeze "≥ 4 mm clearance holes + TPU boot"** superseded by D4 (shared slot + bonded membrane); K1.8 amended.
25. **General-arrangement SVGs.** The task asked for mechanical.md's GA SVG blocks; mechanical.md contains no SVG (the only SVG in 05-engineering is the wiring schematic). §B.3/B.4 are integrator-drawn elevations from the §2 coordinates, labelled as such and not to be used for dimensions; the wiring SVG in §H.2 is copied verbatim from electronics-firmware.md §1.2.
26. **Firmware 20-min limit vs L7's 30-min run.** The sketch ends any run at 20 min; §L7 notes that `run` is issued again at the limit.
27. **Tip box.** mechanical P48 and tips §9 item 18 both describe a tip box; the BOM resolves to print only the tip lead's (P48 listed but normally not printed).
28. **E tip down-stop.** tips §4.5: E's edge sits 4.0 mm lower than W, so the down-stop is raised 4 mm for E to keep the geometric engagement equal; added to §G.2 and §N1 (not previously in the protocols).
29. **Mass ledger entries** (tether cord mass, screw counts) kept as mechanical §6.5 wrote them; the BOM's observation that the second riser screw pair should be aluminium is adopted. The 2 g margin stands; the scale decides (L1).
30. **BOM vs DECISION cost target** (DECISION $250–300 vs BOM $903.50 full rig): both kept in §E.1.3 with the BOM's reconciliation (named major parts $249.50).
31. **Monitor-arm head rotation.** test-protocols §Q6 asked to confirm the VESA head rotates; mechanical §3.4 confirms every arm of the specified class has a vertical swivel; the BOM row 2.01 carries [verify] for swivel range. Kept as a [verify].
32. **Safety §2.4 moving-mass limit** (≤ 30 g per element; carriage KE ≤ 50 mJ) vs test-protocols K2.16 (≤ 160 g float): reconciled in §C.6 (float ≈ 150 g at W3, KE ≈ 10 mJ at 0.36 m/s, inside the 50 mJ carriage limit; the "element" in safety §2.4 is the hand on its leaves, which is spring-bounded).
33. **Status Return Level 2, Current Limit 450 mA, rail-sense input**: electronics lead's deviations from the freeze, accepted as written (§H.1).
34. **Hinge pin washers:** mechanical §4.1 says PTFE or nylon 0.5 mm; BOM row 2.07 says nylon or PTFE; no conflict, both allowed.
35. **The Stage-3 load cell**: a 40 × 12 mm 5 kg bar cell may not exist (BOM [verify]); the wrist slot may need resizing at Stage 3; noted in §D.1 and Appendix 2.

Items the addendum left open for the build reviewer and still open here: the XL330 vendor dimensions and MGN9 hole patterns (Appendix 2); the lift-spring exact part number (box 2A); the 2 g floating-mass margin (L1 decides); the firmware has not been compiled with a real toolchain (B0 is the first build-review step, plus the two §I.6 edits).

---

## APPENDIX 2. VERIFY BEFORE ORDERING / PRINTING (every [VERIFY] and [verify] tag from the sources, collected)

**Before ordering (they change what you click):**
- Lift springs: McMaster 9654K suffix not confirmed; select by the box 2A filter and acceptance table; confirm pack size (BOM 2.13; mechanical §4.3). Or substitute via the luggage-scale test.
- Monitor arm: confirm the printed minimum load (≤ 2.0 kg, ideally ≤ 1.0 kg), head swivel ±90° and tilt ±45° on the chosen listing (BOM 2.01).
- DXL cable: whether ROBOTIS sells an X3P cable ≥ 340 mm; otherwise crimp one (BOM 6.18; mechanical §3.3).
- MGN9 rail 100 mm with MGN9C block: no confirmed listing for the 100 mm MGN9C kit (the component-landscape URL is MGN9H 150 mm) (BOM 2.05). Spare MGN9C block: confirm it ships on a retainer (2.06).
- Idler shoulder screw Ø 5 × 25, M4: no confirmed McMaster part number (BOM 2.10; mechanical §12).
- Feeler stock 0.012 × 1/2 × 12 in: no confirmed Precision Brand or McMaster part number; buy by size (BOM 2.21; mechanical §12).
- Wrist keeper discs: confirm 1.5 mm thickness (BOM 2.20). Silicone membrane: confirm 0.25 mm and about 40A (2.24). PTFE film tape: confirm 0.05 mm (3M 5490 itself is thicker) (2.26). Face cradle: needs its own stand and tilt (2.30).
- Hold-to-run button: pack size of uxcell B08HH78XMH (BOM 6.08). TVS: SA5.0A as the through-hole alternative to SMAJ5.0A (6.15). Kanekalon wig: confirm the fibre (7.04). 3D printer: bed ≥ 220 mm, direct drive (8.01). Mean Well GST25A05 as a brick alternative; Misumi tapped-end 2020 option; XL330-M077-T goal-current re-derivation if substituted. Adafruit 3872/3873 prices [est].
- Bar load cell 5 kg, 40 × 12 mm: may not exist (common 5 kg cells are about 80 mm long); the wrist slot may need resizing at Stage 3 (BOM 6.35).
- M2 assortment: OpenRB-150 mounting-hole size; whether the XL330 horn screws ship with the servo (BOM 3.08; mechanical §5.3). XL330 box contents (horn, short X3P cable) (6.17).
- M3 × 14 for the yaw plates: the 6 + 6 mm stack with a 4 mm insert may want M3 × 10 or × 12; check the CAD (BOM 3.05, §9.3). M5 × 12 / × 16 reach through the 12 mm printed nodes P5/P6/P7; check the CAD (3.13). Button housing screws M3 × 16–20 (3A). P45 reset-cord guide screws and nuts (3A).

**Before printing (vendor drawings and the parts in hand):**
- XL330 output-axis position: 10 mm from the lower body end assumed; the cradle P13 pocket is referenced to the axis, so if the dimension differs only the pocket floor moves (mechanical §2 row 10, §5.3; addendum open item).
- XL330 side mounting-hole positions for the 2 × M2 × 6 into the cradle (P13); the strap alone holds it if they do not line up (mechanical §5.3, P13).
- XL330 horn M2 hole pattern for the horn adapter disc P16 (a 10-minute reprint if wrong) (mechanical §5.3, P16).
- MGN9 rail hole pitch 20 mm with 10 mm end distance (holes at 10/30/50/70/90) on the purchased rail, before printing the P21 mast (mechanical §6.1; BOM 2.05).
- MGN9C block tapped-hole pattern 15 × 10 mm for the riser P26 (mechanical §6.2, P26; BOM 2.05).
- OpenRB-150 outline (about 66 × 25 mm) and mounting-hole size for the tray P3 (mechanical P3; BOM 3.08).
- uxcell 30 mm button: the Ø 29.6 mm deck hole in P39 against the real button (mechanical P39; BOM 6.08).
- M4 heat-set insert hole diameter (5.6 mm modelled) on the insert kit (frame CAD `sp1_frame_lib.scad`).
- Stage 3: bar load-cell hole pitch for the riser-to-seat bolting (mechanical §7.4).
- Print-test first and adjust hole compensation: P15 (625 bearing press, 0.05 mm interference target), P2 (623 press), P13 (servo pocket, after the servo arrives), P34 + a leaf scrap (groove grip), one paddle + one tip (TM1 tang fit).

**Bench tests that decide a [VERIFY]:**
- B2: whether the OpenRB-150 MCU stays up on USB with Terminal VIN at 0 V and the jumper on VIN(DXL) (electronics-firmware §1.5; both outcomes are safe; record which).
- B7: the real goal current for 1.2 N at the tip (no-load gearbox current unknown).
- L6: wrist magnet hold (D61 on a 1.5 mm keeper through 0.05 mm tape, 5.5–7.5 N estimated) and TM1 tip breakaway (4–6 N estimated).
- L1: bare floating mass against the 92 g budget (2 g margin on paper).
- L5: magnet pull-off warm (≥ 19 N) and frame yield (8–11 N).

---

## APPENDIX 3. SESSION LOG AND PACKING / CLEANING LIST (print)

```
SP1 SESSION LOG
Session # ____   Date ________   Start ______  End ______   Build state ______  Firmware ______
Stage/phase: H__ / S-__ / O-__ / A/B __ / Endurance        Helper present: y / n   Name: ______
Posture: SEAT / PRONE   Region(s): CR / OC   Cradle isolated from arm desk: y / n
K5 checklist complete (sign): ______   K1–K4 valid for this build state (date): ______
Per-session lift check done: y / n     Zero pin removed: y / n
Tips used (IDs and codes): ______________________   Tape test valid (date): ______
Weights available: W1 ___ N  W2 ___ N  W3 ___ N  (L1 date ______)   Trim hook used: y / n
Grain map ref: CR lie ______  OC lie ______   Aim marks used: ______   Apex gauge ring at axis: 80 mm y/n
Serial echo at start: SPEED ___ % VAR ___ % MODE ___  Code ______   E (geometric) ___ mm; pointer at mid-stroke ___ mm, at ends 0? y/n
RH ___ %   Room temp ___ °C   Ear plugs: y / n
Planned trial list (condition codes, order as randomised): ______________________________________
Total scalp exposure this session: ___ min (limit ___)
Stops: hold-to-run releases ___  e-stop presses ___  reason(s): ______________________________
Snags total ___   pulls felt ___   tuft pull: y / n (if y: STOP, log redesign item #____)
Shed hairs total: bulb ___  broken ___      Scalp photo 0 min ☐ 10 min ☐ 60 min ☐ next day ☐
Scalp findings (redness / tenderness / marks / none): ______________________________________
Device findings after (hair in gaps, loosening, tip wear, magnet drop, membrane bond): ________________________
Best condition this session (code): ______  Q1 ___ Q2 ___ Q9 ___
One sentence: what would make it more like a person: _________________________________________
Next session plan / changes to build state: ________________________________________________
```

**Before the session (packing in / set-up, ≈ 5 min)**
- ☐ Rig out of the folded position; monitor-arm clamp tightened; arm joints to the taped aim marks for today's REG/DIR; apex gauge check
- ☐ Face cradle clamped (SEAT) / cushion placed and arm clamped to the nightstand or stand (PRONE); cradle isolated from the arm's desk
- ☐ Adapter on the floor, > 1 m from the head; USB to the laptop/charger; OpenRB boot banner read (limits table; rail threshold)
- ☐ E-stop on its weighted base under the free hand; hold-to-run lead ≥ 1.5 m, button in the other hand; both tested over the mannequin; one lift check over the foam head
- ☐ Tip box with today's set (codes face-down for blind trials), wand, slugs (+30, +60, trim hook), hair clips, mirror, zero pin (out of the rig)
- ☐ Phone: timer, voice memo, 240 fps, SPL app, inclinometer; black cloth under the cradle; lint roller; forms and pen; §K5 signed

**After the session (cleaning and packing away, ≈ 5 min)**
- ☐ E-stop pressed; adapter unplugged **first**; USB unplugged
- ☐ Lint-roll the hand, knuckle plate, membrane, guard caps, rail shroud and the cloth; count hairs onto the Session Log (bulb vs broken)
- ☐ Tips out of the TM1 pockets; 70 % IPA wipe each tip (soap and water for P), the pockets, paddles, sleeves, knuckle plate, guard undersides; let flash off; inspect each tip edge under the loupe; retire any chipped tip
- ☐ Check every seam, the membrane bonds and the slot edges with the loupe for trapped hair; tweezers out anything found and log it (a found hair is a design item, not just debris)
- ☐ Face cradle pad wiped (or its cover to the wash); cushion cover likewise
- ☐ Weights off the post (or confirmed captured); hand re-seated on the wrist key; tether cord inspected and folded into its cup
- ☐ Gas arm folded to the parked position; cables coiled with the service loops intact; e-stop and hold-to-run coiled, not kinked
- ☐ Scalp photo at 10 and 60 min set as phone reminders; CSV row(s) appended; Session Log filed in 05-engineering/results/
- ☐ Weekly: re-run L3 (float friction) and L1 (dead weight); re-oil the MGN9C; replace the silicone membrane if cut or stretched; pipe-clean the TM1 pockets; tape-test any tip past 10 sessions; pull-test every tip

*End of SP1-PACKAGE.md.*
