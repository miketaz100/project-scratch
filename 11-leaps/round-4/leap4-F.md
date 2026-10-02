# LEAP-4 F: The 80/20 contrarian

**Project SCRATCH · 11-leaps/round-4 · Agent F · 2026-10-02**
**Read:** LEAP4-BRIEF; 12-sp1v2/decision-analysis.md (in full), DECISION-2 (with the NORTH STAR AMENDMENT), SYSTEM-SPEC §0, §4.1–4.7, redteam-3 §0–3; scratch-model §1–3, §7–8; hair-interaction §4–6; safety-requirements §7; 05-engineering/mechanical.md §6.5 and §8, tips.md §3, §7, §9; leap3-B §0–2 and leap3-A L4. No other round-4 file was read.
**Tags:** [KNOWN] = from a project file · [EST] = my arithmetic (script `swing.py` in the session scratchpad) · [JUDG] = judgement.

**Provocation.** Under the amended goal and every binding decision, which design gives about 80 % of the baseline's expected satisfaction for 20–30 % of its hours and cost?

---

## 0. Answer first

**Partly yes.** About **75 %** of the baseline's conditional P(on-par) is reachable for **≈ 45 % of the hours** and **≈ 38 % of the parts cost**. On the number that matters for a first prototype, P(≥ 7/10 within 26 weekends), it comes out slightly *better* than the baseline (≈ 0.24 against 0.20).

The brief's 20–30 % of hours is **not** reachable without breaking a red line. The reason is that about 50 h are fixed costs that every legal head-worn design pays:
- the safety loop;
- the box;
- helmet fit;
- the hair and force test suite;
- the first sessions.

The best bet is the **SPRING RAKE**:
- six **sprung** POM cones on one block (no per-pin air);
- a **four-link swing** that lifts the whole block at every stroke end by geometry (no lift actuator in the default modes);
- the block driven from the box by **three push-pull cables** (X, Y, depth), turned by three bus servos;
- a **passive, detented halo** that Michael re-indexes by hand between bouts (no powered travel).

Pad B's parts are bought now. In the twin, each servo horn drives both pads in point mirror.

| | Baseline (6-pin hybrid) | **Spring Rake (best bet)** | Ratio |
|---|---|---|---|
| Hands-on hours | 165–230 | **75–100** | ≈ 45 % |
| Parts cost (+ tools) | $1,450–1,500 (+$185) | **≈ $520–600 (+≈ $60)** | ≈ 38 % |
| Head mass, single / twin | 386 (370) / 480 g | **≈ 260 / ≈ 350 g** | 150 g of twin margin |
| Coverage | ≈ 90 %, continuous powered drift | ≈ 85 % reachable, in manual jumps | — |
| P(≥ 7/10 \| full session) [JUDG] | ≈ 0.40 (0.30–0.50) | **≈ 0.30 (0.22–0.40)** | ≈ 75 % |
| P(reach a full session in 26 weekends) [JUDG] | ≈ 0.50 | **≈ 0.80** | — |
| **P(≥ 7/10 in 26 weekends)** | **≈ 0.20** | **≈ 0.24** | — |
| First helmet session | ≈ weekend 10–14 | **≈ weekend 6–8** | — |

---

## 1. Where the baseline's hours, dollars and P actually sit

I split the baseline's 165–230 h across its subsystems. The splits are consistent with the decision analysis's stage totals and RT3's item lists [EST]. For each subsystem, the last column names the gate it mainly serves (from decision analysis §1.4).

| Subsystem | Hours | $ | Head g | Gate it mainly serves |
|---|---|---|---|---|
| Safety loop, box electronics, core firmware | 30–40 | ≈ 300 | — | red lines (fixed cost) |
| **Pin pneumatics:** 6 cartridges, 6 valves, rails, deadhead pumps, diverse reliefs, vacuum park, filters, restrictors, 1 kHz gate scheduler, leak hunting | **45–60** | **≈ 450** | ≈ 42 (6 × 7 g) | G1 (constant force), G4 (subsets) |
| **Puppet synchro:** XY master, 3 sleeve lines, slave deck, charge/dump, reliefs, re-zero, sleeve-life rig | **25–35** | ≈ 160 | ≈ 40 | G3 (silent head) |
| Pad mechanics: RCC palm, skids, float, guards | 15–20 | ≈ 80 | ≈ 40 | G1 |
| **Powered halo travel:** hub pods, 2 servos, GT2, bail bend, carriage, tendon, stops, routing | **35–50** | ≈ 250 | ≈ 120 | G5, part of G4 |
| Tests, wig, sessions | 15–25 | ≈ 50 | — | all |

Three facts follow:
1. **Three non-binding blocks hold ≈ 60 % of the hours and cost:** per-pin air, air synchro and powered travel.
2. **The baseline's own Stage-B GO (≥ 7/10) comes from a static halo with indexed poses,** before any powered travel exists (decision analysis §4.3).
3. **G1 and G4 dominate P.** G1 depends on cone, force and hair, not on where the force comes from; G4 is mostly firmware.

---

## 2. Candidate leaps

### L1: SPRUNG CONES ON ONE BLOCK (no per-pin actuation)

**(a) Assumption broken.** That each nail needs its own actuator (air piston, valve, hover collar, bite window) to get a capped force and a lift at reversal.

**(b) Principle and sketch.**
- **Nail:** each of the six nails keeps decision-analysis must-fix #1, the one-piece drafted POM cone (90°, Ø 2 flat, rim R 0.4) on a rigid Ø 1.0 shaft. The shaft is guided in a 15 mm POM or brass bush in the block.
- **Spring:** a soft music-wire compression spring (≈ Ø 4 OD, 0.3 mm wire, ≈ 20 active coils: k ≈ 0.05–0.08 N/mm [EST]). It sits between the bush and a collar, preloaded to **0.15 N** against an extension-stop collar.
- **Layout:** centre plus pentagon at R 18, as in the baseline.
- **Force:** each nail compresses its spring by δ₀ ≈ 3 mm at nominal depth, so **F ≈ 0.15 + 0.05 × 3 = 0.30 N per nail, 1.8 N for all six** [EST]. That is inside scratch-model 3.2–3.3.
- **Force cap:** the springs have 12 mm of travel to their bottom stop. The palm skids cap how far the scalp can rise into the field (§2, L2), at ≤ 10 mm. So a nail can never bottom, and the per-nail force is bounded by geometry at **≤ 0.15 + 0.05 × 10 = 0.65 N**.
- **Total load:** six nails at that bound plus a ≤ 4 N palm float spring is ≤ 7.9 N.
- **Red lines:** 2 (a mechanical constant, ≤ 2.5 N per element) and 3 (≤ 12 N total) are met with no relief valve, pump deadhead or diverse "b" relief.
- **Lift:** all six nails lift together with the block (L2).

**(c) Baseline numbers moved.** It deletes the pin-pneumatics block: **−45–60 h, ≈ −$330** net of a lift mechanism, **−26 g single, ≈ −50 g twin**. It also deletes RT2 #3 (partly), #7, #8, #9 and #14 and RT1 #3 (the restrictor ratchet).

What is lost: per-pin subsets (all-6 / 3-row / single) and constant force across the stroke. The cost is about −0.02 on G1 and −0.06 on G4 [JUDG].

**(d) Plausibility.** The tip and finger compliance windows are 0.1–0.5 N/mm (scratch-model 3.12; criterion 9 asks for ≤ 0.5 N/mm with ≥ 5 mm travel). A soft spring therefore sits *inside* the human envelope. A finger is itself a ≈ 0.3 N/mm spring, not a constant-force source.

The catch is curvature: scalp height under the field varies with region. A Ø 90 skid circle sees a sagitta of 6.9–20 mm across R 150–60 [EST]. Powered travel would need a per-pose depth map. Fixed stations (L4) calibrate depth once per station, which is easy.

**(e) Cheapest experiment ($25, one evening).** Build a hand-held 6-nail block: printed body, POM cones, Ø 1 rod in brass tube, an assorted spring kit. Set 0.3 N per nail on the kitchen scale. A helper scrubs crown and occiput at ≈ 100 mm/s in 8 headings, blind against the H-3 ball block. **GO** if it is scratch-like in ≥ 6 of 8 headings, rated ≥ 6/10, and the cone visibly reaches skin through his hair at ≤ 0.4 N.

**(f) Replaces.** 6 S070 valves, the pin rail, vacuum park, 6 cartridges with sleeves, collars, needles and bleeds, per-pin hover-and-bite, and the 1 kHz gate scheduler.

**(g) Why it might fail.** Contact-count and force variation were real anti-habituation levers, and common-mode force modulation (L3's depth cable) may not replace them. **Fix if so:** two depth groups (centre + 2, and the other 3) on two cables (+$25, +6 h). That restores the "all-6 / half" subsets.

---

### L2: THE SWING (lift at every reversal from geometry)

**(a) Assumption broken.** That lift-at-reversal (H-5.2, gating) needs a fast actuator and timing firmware.

**(b) Principle and sketch.**
- **Suspension:** the nail block hangs from the palm's pivot plate on **four parallel, equal links with ball joints at both ends** (RC M2 ball links), **L = 17 mm**. Four S-S legs leave exactly 2 DOF, so the block translates in X and Y without rotating.
- **Bowl-cam lift:** the block rises on a sphere cap by Δz = L − √(L² − r²), where r is the radial excursion from neutral. The profile is the same in every heading, so it serves LINE, PLINE and offset CIRCLE alike.
- **Numbers on the binding 30 mm line** (amplitude 15 mm, 1.4 Hz, δ₀ = 3 mm) [EST, swing.py]:

| Quantity | Value | Rule |
|---|---|---|
| Nail contact while \|r\| < 9.6 mm | **19.3 mm of skin contact per stroke** | rake band 1–5 cm (scratch-model 3.7) |
| Plough-in / lift angle at r = 9.6 | **34.6°** | ≤ 35° (spec), ≤ 30° target (H-5.3) |
| Speed at lift | **101 mm/s = 0.77 v_peak** | H-5.3 ≥ 0.30 v_peak |
| Tip clearance above skin at the stroke ends | **6.0 mm** | H-5.2 ≥ 5 mm at zero force |
| Force profile | 0.30 N mid-stroke, falling to 0.15 N, then off | resembles the 30–70 % force dip at reversal (scratch-model 3.10) |
| Time in contact | 44 % (baseline ≈ 64 %) | — |

- **Other link lengths:** longer links give gentler profiles. L = 25 at a 38 mm line gives 23.7 mm of contact at 28°, but the line must lengthen to keep ≥ 5 mm clearance.
- **Circles:** offset circles lift once per revolution, as E3 requires (e.g. R 8 about a centre offset 7 mm: r runs 1–15 mm). The lift arc rotates with the offset heading. Circles above R ≈ 12 need the depth cable (L3) to time the lift.

**(c) Baseline numbers moved.** It removes the need for *any* fast lift actuator and is the XY guide at the same time (4 ball links, ≈ 8 g, ≈ $8): **≈ −8 h and −10 g** against crossed slides plus a timed lift.

The safety gain is larger than the hours. In the default modes, **H-5.2 and H-5.3 hold by geometry**, so a firmware timing bug cannot reverse a loaded nail (red line 13 spirit). RT2's checklist item 4 ("lift before reversal") rises from 1 to 2.

**(d) Plausibility.** It is a parallelogram mechanism with off-the-shelf ball links. The links sit inside the palm, ≥ 30 mm above the scalp (H-6.1). Ball-link play (0.1–0.2 mm) reverses only while the block is lifted, so it is unloaded and should not tick [EST].

**(e) Cheapest experiment ($15, a Saturday).** Print the palm plate and block, fit 4 ball links, and push the block along a ruler in 8 headings. Measure Δz(r) with calipers and the plough angle with 240 fps phone video on a foam head. Listen for a tick at 1.4 Hz. **GO:** clearance ≥ 5 mm, angle ≤ 35°, and no audible tick at 30 cm.

**(f) Replaces.** Hover-and-bite timing, the per-pin park vacuum and the lift-timing firmware for the default modes.

**(g) Why it might fail.**
- Contact length is tied to L and δ₀, not set freely; shorter strokes ("wiggle", 0.5–1.5 cm) need the depth cable to lift.
- The stroke must stay centred on neutral, so there is **no in-pad drift**. Short-range relocation must come from station moves.
- The time in contact drops to 44 %.
- If Michael's rating says "too gentle at the ends", lengthen L, or use the timed depth cable and treat the swing as a plain XY guide.

---

### L3: CABLE PUPPET (three push-pull lines instead of three sealed air lines)

**(a) Assumption broken.** That copying the box motion to the pad needs a sealed pneumatic replica (sleeves, charge/dump, reliefs, re-zero, leak budget).

**(b) Principle and sketch.**
- **Box:** three Feetech bus servos (STS3215 class) on 25 mm horns, so ±37° gives ±15 mm.
- **Cables:** each drives a **1.0 mm music-wire inner in a 1.5/2.5 mm PTFE liner**, about 1.8 m from box to pad. **X** and **Y** push the block through a compliant coupling (≈ 0.4 N/mm, TPU or PP) and a 3 N magnetic breakaway. **DEPTH** pulls the swing's pivot plate down against a 2–3 N up-spring, to a mechanical down-stop.
- **Fail-to-free:** the DEPTH cable's box end is held by a **12 V power-off electromagnet** (≈ $8). Power loss, the e-stop, hold-to-run release or the hardware watchdog drops the magnet, and the spring lifts the block ≥ 15 mm (red lines 8 and 13).
- **Firmware:** the path generator (LINE, PLINE default, CIRCLE; per-stroke jitter in length, period and heading; pauses; per-station depth; LIGHTER/HARDER) writes three positions at 100–200 Hz.
- **Twin:** each horn carries **two inners**, so pad B mirrors pad A in point symmetry. The scrub reactions at the helmet cancel (leap3-A L3) with no extra servos.

**(c) Baseline numbers moved.** It replaces the synchro block: **−18–26 h, ≈ −$90; head mass similar to slightly lower (≈ −10 g).** Nothing on the head is powered, hisses or turns.

**(d) Plausibility [EST].**
- **Friction:** a capstan factor of e^(0.15 × 2π) ≈ 2.6 on a 1 N drag means ≤ 3 N at the horn, far below servo torque.
- **Lost motion:** ≈ 0.5–2 mm per reversal against a 30 mm stroke, against scalp two-point acuity of 15–39 mm. The box command is scaled to the measured lost motion.
- **Head-turn drag:** three 1 mm wires have EI ≈ 3 × 9.8 × 10³ N·mm², about half of leap3-A's three bike housings (≈ 6 × 10⁴). That puts it near ≈ 0.04 N·m at ±60° yaw.
- **Drag sensing:** the 16 mN drag vector is lost; servo load readback is coarse. Snag safety rests, as RT2 insists it should, on geometry, the 0.4 N/mm coupling and the breakaway.

**Alternative: an on-helmet drive.** Three micro servos on the pad: −6 to −8 h and −$40, but +45 g per pad and 35–50 dBA at the ear plus a tick (leap3-B). G3 falls to ≈ 0.62 and P to ≈ 0.24. Keep it only as a fallback.

**(e) Cheapest experiment ($25, a weekend).** Run 1.8 m of liner and wire through two 180° loops. Drive one end by hand or with any servo at 1.4 Hz against a 1 N spring load. Read the far end on a ruler with 240 fps video. Measure the yaw drag with a luggage scale on a bike helmet. **GO:** lost motion ≤ 2 mm, no stick-slip visible in the video, yaw drag ≤ 0.05 N·m.

**(f) Replaces.** The XY belt master, 3 sleeve cylinder pairs, the slave deck, CHARGE/DUMP valves, line reliefs and breakers, line pressure sensors, re-zero firmware and the sleeve-life rig.

**(g) Why it might fail.**
- Lost motion that varies with umbilical posture could make strokes uneven when he leans back. The fix is pre-tension, or moving to a stiffer 1.2 mm inner.
- PTFE wear dust after hundreds of hours.
- A stiff umbilical bundle might be felt at the ear axis.

---

### L4: STATIONS, NOT TRAVEL (passive detented halo; the hand moves the hand)

**(a) Assumption broken.** That the first prototype needs powered travel.

**(b) Principle and sketch.**
- **Halo:** the baseline's skeleton halo geometry is kept: dial cradle, front band, hand-bent Al bail on ear-axis hubs. The hubs carry **two 6800-2RS bearings and a spring-ball detent plate** (α every 15°, −25…+100°, hard stops from the hairline fence). There are no motors.
- **Carriage:** it clamps on the bail with **β detents every 15°, ±45°**, with mechanical end stops that keep the pad edge ≥ 25 mm from the ear canal (red line 6; RT2's β ≈ 41–46° collision limit).
- **Grid:** 9 × 7 = 63 poses.
- **Moving the pad:** releasing hold-to-run drops the magnet and the pad lifts ≥ 15 mm (H-5.8). Michael moves a knob on the carriage with his free hand (≤ 3 s), then presses again.
- **Depth:** a 2-bit reed code on the detents, or a station button, tells firmware which station's stored depth to use.
- **Skids:** the palm skids sit still during scrub (only the block moves) and are lifted during moves. RT2 #16 (skids sliding 18–60 m per session) and #5 (the nail–skid scissor) mostly disappear.

**(c) Baseline numbers moved.** It deletes the powered travel block: **−35–50 h of build** (hub pods with capstans, servos and tendon), **≈ −$200, ≈ −105 g single / ≈ −125 g twin.** It also removes RT1 #6 (servo hunting into the parietal bone) and RT2 #4's firmware-only twin guard.

Coverage *reachable* stays ≈ 85 %. Coverage *realised* depends on how often he moves the pad.

**(d) Plausibility.** Decision analysis §3 already prescribes "fixed pose, manually indexed: a static halo with 5–7 detented poses … Michael re-indexes by a knob" for the first ≥ 7/10 answer. This leap makes that the prototype instead of a waypoint.

**(e) Cheapest experiment ($0–20, two evenings, once the L1 hand block exists).** This is the decisive test of whether travel is worth 35–50 h:
- **A:** the helper scratches with the 6-nail block, moving freely and drifting continuously.
- **B:** the helper may stay only on 6 marked stations and moves only when Michael taps a station on a head map.
- Ten minutes each, blind order, on two evenings.

If B rates ≥ A − 1 point, travel is not worth its hours for SP1.

**(f) Replaces.** Two STS3032 servos with GT2 capstans, the β tendon and drum, spring balancers, travel firmware, the C-stage gates and the twin's double drum.

**(g) Why it might fail.**
- **"Being scratched well" may mean "not having to do anything."** If reaching up every 1–3 minutes breaks the spell, G5 and G4 fall further than my 0.78 / 0.70.
- The wig matting test might set the H-5.5 dwell limit at under ≈ 1 minute per patch. Manual moves are then untenable, because the swing (L2) gives no in-pad drift.

**Upgrade path, keeping the head motor-free:** α travel by a **fourth cable**, a pull-pull loop onto a Ø 30 drum at the left hub, with the servo in the box: +15–20 h, +$70, +15 g. That buys continuous front-to-back drift with β still manual, P(on-par) ≈ 0.35 [JUDG].

---

### L5: THE FLOAT-ARM 3-NAIL HAND AS THE PAD (evaluated; reuse its parts, not the hand)

**(a)** The assumption broken: that SP1 needs a new pad when mechanical.md §8 already has a fully engineered one (three nails on 0.12/0.15/0.18 N/mm leaves, 24 mm pitch, TM1 breakaway tips, hair score 29/36, STLs in `cad/`).

**(b)** The hand (60.5 g [KNOWN, §6.5]) bolts under the swing in place of the cone block.

**(c)–(d)** The numbers argue against it:
- The palm is **52 × 169 mm** and sweeps ≈ 200 mm with ±15 mm of scrub. That is too long for parietal stations against RT2's 41–46° hub collision.
- W and B45 are directional in X, so the binding precessing line would drag their edges lengthwise. Fixing that needs TM1 cone tips or a yaw axis.
- Once the tips are omni, coil springs (L1) are smaller than the two-level crossed leaves.
- It gives 3 edges per stroke against 6.
- **Net:** ≈ 0 h saved, +25–30 g, P ≈ 0.22 [JUDG].

**(e)–(f)** Reuse the **Stage-0 wand and the TM1 tips (W, B45, H, P)** as S0 comparators for the cone: P is the real-nail anchor and H the massager control. Also reuse the leaf-rate formula for spring selection and the edge-finishing and tape-test procedures. That is ≈ $40 and ≈ 3 h, already designed.

**(g)** If the cone loses to W or B45 by ≥ 2 points blind, this leap reopens with directional tips on a yaw-locked line.

---

## 3. Configurations compared

Gate values are in the decision analysis's method (G1 edge, G2 scratch-not-brush, G3 no intrusion, G4 no habituation, G5 coverage and steering). Products are scaled by the analysis's correlation factor (0.35 → 0.40) [JUDG, swing.py].

| Configuration | Hours | Parts $ | Head g single / twin | G1–G5 | P(on-par \| session) | P(reach, 26 wk) | **P(≥ 7/10, 26 wk)** |
|---|---|---|---|---|---|---|---|
| Baseline hybrid | 165–230 | 1,450–1,500 | 386 / 480 | .75 .85 .80 .80 .85 | 0.40 | 0.50 | **0.20** |
| A: baseline + L1 sprung pad (keep air synchro and travel) | 125–175 | ≈ 1,120 | ≈ 360 / ≈ 430 | .73 .85 .80 .74 .85 | 0.36 | 0.58 | 0.21 |
| B: L1 + L2 + on-pad micro servos + L4 | 60–80 | ≈ 420 | ≈ 295 / ≈ 410 | .72 .85 .62 .70 .78 | 0.24 | 0.85 | 0.20 |
| **C: Spring Rake = L1 + L2 + L3 + L4** | **75–100** | **≈ 520–600** | **≈ 260 / ≈ 350** | .72 .85 .80 .70 .78 | **0.30** | **0.80** | **0.24** |
| C, crown station only ("first light") | 60–75 | ≈ 450 | ≈ 255 / — | .72 .85 .80 .62 .55 | 0.19 | 0.90 | 0.17 |
| C + α cable travel (later) | 90–120 | ≈ 600–680 | ≈ 275 / ≈ 365 | .72 .85 .80 .76 .83 | 0.35 | 0.75 | **0.26** |

**Mass build-up for C (single), in grams [EST]:**

| Part | g |
|---|---|
| Band, forehead pad, cradle, temple pads (SYSTEM-SPEC §4.7) | 66 |
| Two passive hubs | 24 |
| Al-tube bail (RT3) | 58 |
| Carriage | 10 |
| Pad: palm, guard and skids 20; swing 8; block 10; nails 4; coupling 4; cable stops 4; depth spring 4; boots and screws 6 | 60 |
| Cables on the helmet plus the umbilical's head-borne share | 21 |
| Doff handle, visor guard, miscellaneous, head switch | 20 |
| **Total** | **≈ 259** |

The twin adds a pad (60), a carriage (10) and cables (≈ 19), ≈ 350 g in total.

**Hours build-up for C [EST, with RT3's 1.5× first-timer factor]:**

| Item | h |
|---|---|
| Safety loop, box and firmware (relay hold-to-run with weld check, NC e-stop, hardware watchdog, magnet driver, servo bus, path generator) | 22–30 |
| Sprung nails | 4–6 |
| Cables and umbilical | 6–9 |
| Pad (swing, block, palm, guard, coupling, skids) | 14–18 |
| Passive halo | 15–20 |
| S0, wig and hair suite, proof loads, sessions | 14–20 |
| **Total** | **75–103** |

**Parts for C [EST]:**

| Item | $ |
|---|---|
| Box: ESP32-S3, 3 servos, bus board, adapter, e-stop, relay, watchdog, 2 magnets, case | ≈ 230 |
| Cables, including the pad-B set | ≈ 60 |
| Two pad kits | ≈ 90 |
| Helmet | ≈ 70 |
| Printing | ≈ 50 |
| Fasteners and glue | ≈ 40 |
| Load cell | ≈ 15 |
| Shipping | ≈ 40 |
| **Total** | **≈ $595** (≈ $520 with cheaper servos) |

**The fixed-cost floor.** Safety loop, box, helmet fit and tests come to ≈ 50–60 h and ≈ $300 in *every* row. That floor is why no legal configuration reaches 20–30 % of the hours. Even "crown station only" is ≈ 35 % of the hours, and it scores worse.

---

## 4. Is the baseline's extra complexity buying enough P(on-par)?

**For a first prototype, no.**

**What the extra ≈ 90–130 h and ≈ $900 buy** [JUDG]:

| Feature | Gate | Gain in P(on-par) |
|---|---|---|
| Continuous powered drift | G4, G5 | ≈ +0.05 |
| Per-pin subsets | G4 | ≈ +0.03 |
| Constant force | G1 | ≈ +0.01–0.02 |
| The synchro's drag vector | — | ≈ +0.01 |
| **Total** | | **≈ +0.10** (0.30 → 0.40) |

**What that complexity costs:** ≈ −0.30 in P(reach), because pneumatic cartridges, sealed lines and travel pods are where RT3's likeliest stopping points sit.

**Net:** unconditionally the simple machine is level or ahead (0.24 against 0.20). It gets a helmet session months earlier, with ≈ $900 less at risk.

**The asymmetry that decides it: every expensive feature except constant force grafts on later,** and the first session says which one to buy:
- "same spot" or "had to move it" → α cable travel (+15–20 h);
- "too even" → two depth groups (+6 h);
- "not crisp" → tip and force work the baseline would also need.

The feature that does not graft on, constant force from air, carries the smallest gain on the list.

**The baseline would be right in two cases:**
- Michael treats hands-free as essential, not merely nicer. Then build "C + α" from day one, which is still ≈ 50 % of the hours.
- The wig run sets a very short H-5.5 dwell limit.

Both are checked cheaply before the Day-0 cart.

---

## 5. Best bet: the SPRING RAKE (L1 + L2 + L3 + L4), with L5's tips as S0 comparators

**The case in one paragraph.** The amendment removed the human illusion and kept four things: a crisp edge, the right force and speed, coverage, and no habituation.
- **Crisp edge:** the cone that delivers it is the same in both designs.
- **Right force and speed:** springs with stops and a geometric lift deliver them with fewer failure modes than air.
- **No habituation:** this is mostly firmware: per-stroke jitter in length, period and heading, pauses, depth (force) modulation and precession. All of it survives on a three-cable drive.
- **Coverage:** the one honest loss. It becomes discrete and manual.

Spend the saved 90–130 hours on getting the answer, then buy exactly the complexity the answer asks for.

**Revised estimate if adopted:**

| | Spring Rake |
|---|---|
| Hours | **75–100 h** (+15–20 h if α travel is added later) |
| Parts | **≈ $520–600**, plus ≈ $60 of tools; pad-B parts and the second cable set included |
| Head mass | **≈ 260 g single, ≈ 350 g twin** (limit 500) |
| P(≥ 7/10 \| full session) | **≈ 0.30** (0.22–0.40); ≈ 0.35 with α travel |
| P(≥ 7/10 within 26 weekends) | **≈ 0.24**; ≈ 0.26 with α travel added after R2 |
| First helmet session | ≈ weekend 6–8 |

**Red lines.** All 13 hold. The ones the leaps change:
- **1:** nothing rotates within 30 mm of hair. The links sit in the palm, the cable inners move axially above the guard, and the hubs are at the ear axis.
- **2 and 3:** ≤ 0.65 N per nail by spring, stop and skid geometry; ≤ 7.9 N in total; tangential load goes through the 0.4 N/mm coupling and the 3 N breakaway.
- **4:** NC e-stop in series with the servos and the magnet; armrest hold-to-run.
- **7, 8 and 13:** the servos sit behind springs; the lift, force cap and reversal lift are non-firmware (spring, power-off magnet, swing geometry).
- **6:** mechanical α and β stops.
- **10:** ≤ 350 g twin; dial cradle plus the magnetic umbilical breakaway.

**Staging:**
1. **R0, one weekend, ≈ $60.** L1 (e) hand block, blind against H-3 and the P press-on nail; L2 (e) swing bench; L3 (e) cable loop; the wig matting run; the L4 (e) stations A/B with a helper. **GO:** scratch-like in ≥ 6/8 headings and ≥ 6/10; lost motion ≤ 2 mm; swing angle ≤ 35° with ≥ 5 mm clearance.
2. **R1, 3–4 weekends, ≈ $330.** Box with the full safety loop, three servos, cables, and the pad on a wig head. Hair suite (200 strokes per mode, circle only after the token check), force map on the load cell, proof loads. **GO:** zero captures, force within ±0.1 N of setpoint at each station's depth.
3. **R2, 2–3 weekends, ≈ $130.** Passive halo; crown station sessions of 5 → 10 → 20 minutes, then all stations. **GO:** ≥ 7/10 "as good as a good scratch", zero pulls.
4. **R3, only on evidence.** α cable travel, or two depth groups, chosen by what the R2 ratings name. The twin goes on when a measured single is ≤ 280 g.

**Michael's sign-offs needed:**
- replacing the puppet's air lines with cables (the puppet's *principle*, motion made off-head, is kept);
- replacing per-pin air with sprung cones;
- deferring powered travel.

None of the three is a binding decision.

**Most likely way it fails:** manual relocation proves to be the difference between "a good gadget" and "being scratched well". Run the L4 (e) A/B before the Day-0 cart. If B loses by ≥ 2 points, adopt "C + α" from the start: still ≈ 50 % of the baseline's hours, ≈ 45 % of its cost, and ≈ 0.26 unconditional.
