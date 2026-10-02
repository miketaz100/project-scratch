# SP1 "PUPPET HALO": Decision analysis after the north-star amendment

**Project SCRATCH · 12-sp1v2 · Decision Analyst · 2026-10-02**
**Read:** DECISION-2 (including the NORTH STAR AMENDMENT), SYSTEM-SPEC, redteam-1/2/3 in full, scratch-model §1–3, §4.4, §7–8, safety-requirements §7 (red lines), leap2-B L3, leap3-A L2.
**Tags:** [KNOWN] = from a project file · [EST] = my arithmetic (scripts `pins.py`, `mass.py` in the session scratchpad) · [JUDG] = a judgement estimate, not a measurement.

**The question.** Michael must choose between (1) building the full design with every red-team fix, (2) simplifying first (e.g. fewer pins), or (3) running another leap round.

**The new criterion.** SP1 succeeds if a session is rated "as satisfying as being scratched well", ≥ 7/10. That rating rests on four things:
- a crisp edge reaching the scalp;
- the right force and speed;
- coverage;
- no habituation.

It must still be a scratch, not a massage, vibration or brush. Person-illusion (human-like timing, "attention", social cues) is now nice-to-have.

---

## 0. Answer first

**Recommend a precise hybrid: Option 1's must-fixes, Option 2's simplification, and no leap round.** Build a **6-pin pad** (centre pin plus a pentagon at R 18 mm) with every must-fix below, on Red Team 3's sensation-first staging.

| | Recommendation |
|---|---|
| Parts cost | **≈ $1,450–1,500**, plus ≈ $185 of tools and a printer if needed |
| Hands-on hours | **≈ 165–230 h** |
| Head-borne mass, single | **≈ 386 g** (≈ 370 g with light lines) |
| Head-borne mass, twin | **≈ 480 g** (light lines plus the spec's own mass ladder) |
| P(≥ 7/10 on-par), if a first full session is reached [JUDG] | **≈ 0.15 as drafted → ≈ 0.40 after the must-fixes** |

**The deciding fact is mass.** Under RT2's corrected model a 12-pin twin is **≥ 530 g with every lever pulled** (red line 10: ≤ 500 g); 8 pins is marginal. **Six is the largest legal twin count**, and decision 4 needs the twin addable without redesign. Six all-active pins also give as much scratch per stroke as 12 pins in 3–4-nail rows, without the hover comb.

---

## 1. Red-team attacks re-scored under the new criterion

**MUST** = required before the stage where it bites (a red line, a hair or skin hazard, a threat to crisp/right-force/scratch-not-brush/no-habituation, or a build blocker). **NICE** = improves rating or robustness; measure first. **IRRELEVANT** = person-illusion only, or moot. Safety and hair attacks are unaffected by the amendment.

### 1.1 Red Team 1 (sensation)

| # | Attack | Now | Why (one line) |
|---|---|---|---|
| 1 | Crank clock | **MUST** (narrower) | Habituation stays a requirement: per-stroke length, period, heading and lift jitter plus pauses. Fine human rubato is NICE. $0. |
| 2 | Hover comb and ghost fingers | **MUST** | 8–9 idle nails at 5 mm give ≈ 30 % of follicle drive: a *brush* component. Fewer, all-active pins dissolve it. |
| 3 | Restrictor ratchet and light-end parasitics | **MUST** | "Crisp edge at the right force" is now the core; 0.15 → 0.09 N and 55–90 % flank loss hit it directly. |
| 4 | Head-side air hiss | NICE (adopt, $10) | It mattered mainly as "pneumatic, not fingers"; still a mild irritant, and mufflers are cheap. |
| 5 | Hat lean and rocking | NICE | Comfort, not illusion. Measure at C3. Counter-mass only if felt. |
| 6 | Balanced geared axes hunting into the parietal bone | **MUST** ($0) | A rhythmic skull buzz is a vibration cue. Gear bias (free if the balancer is deferred) plus STS profile mode. |
| 7 | Stamp: common force and identical velocity | IRRELEVANT | Failed only the "hand" percept; landing jitter covers habituation. |
| 8 | Restless roaming: the H-5.5 placeholder | **MUST** ($0, one wig day) | "Won't stay where I like it" is a satisfaction failure. Wig matting test, then STAY. |
| 9 | Soft neck reads as a stylus | **MUST** | Crispness is the criterion; merged with RT2 #1. |
| 10 | Holding a 2.5 N lever for 20 minutes | **MUST by D4** ($5) | Nobody is "scratched well" while clenching. Forearm-weight armrest switch. |
| 11 | Snag-reflex false trips | **MUST** | Flinches ruin a session. Absolute or sustained criterion; hover first. |
| 12 | Substrate habituation after minute 3–5 | **MUST** | Explicitly kept by the amendment. Closed by #1, #2 and #4. |
| 13 | Synchro 25 Hz ring | NICE | Brief flutter. Adopt the free σ_t ≥ 20 ms. |
| 14 | Synchro stroke shrink | IRRELEVANT | RT1's own verdict: below acuity. |
| 15 | Omni-nail edge varies with heading | IRRELEVANT | It is axisymmetric. |

### 1.2 Red Team 2 (mechanical, hair, safety)

| # | Attack | Now | Why |
|---|---|---|---|
| 1 | Omni-nail neck in the pile: a loop former, with only 4 mm of reserve | **MUST** | S3–S4 hair capture; also the crispness fix. |
| 2 | Umbilical crosses the bail sweep | **MUST before C** | Certain; tugs and face drag. Exit along the ear axis. |
| 3 | Synchro tangential cap ≈ 10.4 N; rupture slam 60 mJ | **MUST** | Red lines 3 and 13. |
| 4 | Pad hits the hub pods past β ≈ 41–46°; twin guard 8° in firmware only | **MUST** | Pinch and closing wedge. |
| 5 | Nail–skid scissor (0.3 mm gap) | **MUST** ($0) | H-3.8. With the 6-pin field it is solved without moving the skids (§2). |
| 6 | Pad harness unrouted and unbudgeted | **MUST** | Drives the twin over 500 g (§2). |
| 7 | Retract 270–390 ms; kink plus compression ≈ 29 N | **MUST** ($10) | QEV and relief poppet at the float. |
| 8 | Third normal barrier is not a constant | **MUST** ($15) | Pump deadhead selection, diverse second reliefs, measured equilibrium. |
| 9 | Reverse pressure on rolling diaphragms or sleeves | **MUST** | Feeds #3 and sleeve life. |
| 10 | Hold-to-run contacts weld on inrush; stale outputs | **MUST** ($10) | A silent loss of red line 4. |
| 11 | Red-line-9 proof contradictions | **MUST** ($0) | Re-derived for the new stick and cap. |
| 12 | Doff with the lever held; high seats; no IMU | **MUST** (switch, posture rule) | Doff and headrest hazards; drop the IMU claim. |
| 13 | Float stiction ≈ 1.3 N | NICE | Minor patting; MGN7 rail only if the B6 trace pats. |
| 14 | Hygiene: crevices and unfiltered orifices | **MUST** (10 µm filter); rest NICE | A clogged bleed silently removes a backstop. |
| 15 | Static from PTFE in the pile | NICE | The PTFE leaves with the new stick. ESD-POM later. |
| 16 | Skids slide 18–60 m per session, unledgered | **MUST** ($0) | Matting is certain. |
| 17 | Breakaway order (plug dowels lock at 24 N) | **MUST** ($0) | Resolved by deleting the helmet plug (RT2 §11). |
| 18 | Box heat on a cushion | NICE ($5) | S1. Vents. |
| 19 | Circle tokens plough at 40° | **MUST** ($0) | Checker on before circle runs on the head. |

### 1.3 Red Team 3 (buildability)

| # | Attack | Now | Why |
|---|---|---|---|
| 1 | Overscope ×5: 270–400 h; P(D4 in 6 months) ≈ 15 % | **MUST** | Matters more now that requirements shrank. |
| 2 | Staging is a waterfall; no sensation until Stage D | **MUST** | Only the rating answers the question. |
| 3 | Cast diaphragms need degassing and moulds | **MUST** (substitute) | Bought sleeves, cots, Airpel float. |
| 4 | Machined eccentric crank | **MUST** (substitute) | XY master (frees stroke length for RT1 #1) or printed eccentrics. |
| 5 | Straight carbon cannot be bent | **MUST** | Hand-bent Al 10 × 1 (+13–23 g). |
| 6 | 20-port helmet plug | **MUST** (delete) | Confirmed by RT2, with the QEV. |
| 7 | Printed relief poppets | **MUST** (substitute) | Bought; a different type for each "b" relief. |
| 8 | Drilled Ø 0.15–0.25 mm orifices | **MUST** (substitute) | Dispensing needles. |
| 9 | Day-0 codes and supply (S070C-6DC-32; STS3032 stock; sensors from China) | **MUST** | Wrong coils or lead times stall Stage A. |
| 10 | Missing tools; honest cost ≈ $1,900 | **MUST** (budget) | Plan with real numbers. |
| 11 | Split-PTFE hover collar window | NICE | A/B against an O-ring gland at A4. |
| 12 | Capstans and balancers | NICE (adopt) | GT2 3:1 belt; defer the balancer (also helps RT1 #6). |
| 13 | Valve A/B (cheap 3-way against S070) | NICE | A cost lever of up to ≈ $28 per pin. |
| 14 | Custom enclosure | NICE (adopt) | Apache 2800 at $30. |
| 15 | 22 sensors | NICE (adopt) | 10 for Stages A–C. |
| 16 | κ-grammar, ledger, attention layer, scan | Downgraded | Defer to Stage D (§3). |
| 17 | Cast 3-chamber egg | Downgraded | Buttons or bulbs (§3). |

**Tally.** RT1: 9 MUST, 3 NICE, 3 IRRELEVANT. RT2: 16 MUST (one partial, #14), 3 NICE. RT3: 10 MUST, 7 NICE or downgraded.

The amendment removes **three RT1 attacks outright and softens two more**. It removes **none** of RT2's. It makes RT3's simplifications *more* permissible.

### 1.4 P(first good session rated ≥ 7/10 "as satisfying as a good scratch") [JUDG]

This is conditional on reaching a full-score session. It is RT1's gate method, with the gates rewritten for the new criterion.

| Gate | As drafted | After must-fixes | Reasoning |
|---|---|---|---|
| G1 Crisp edge reaches the scalp at the intended force | 0.60 | 0.75 | Neck stylus, ratchet and light-end errors are fixed. Contact fraction in his hair is still unmeasured. |
| G2 Reads as a scratch, not a brush or comb, at the right speed | 0.60 | 0.85 | The hover comb is gone; 70–130 mm/s at 1–4 Hz is already in band. |
| G3 No intrusion dominates (lever, flinches, servo buzz, hiss, hat) | 0.60 | 0.80 | Armrest switch, snag criterion, gear bias, mufflers. |
| G4 No habituation from minute 3 to 20 | 0.55 | 0.80 | Substrate jitter, stroke-length freedom, location changes. |
| G5 Stays where it is wanted; coverage and steering | 0.75 | 0.85 | Wig-set dwell limit, STAY, THERE button. |
| Product (independent) | 0.09 | 0.35 | |
| **With positive correlation** | **≈ 0.15 (0.10–0.22)** | **≈ 0.40 (0.30–0.50)** | |

**Cross-check.** RT1 gave 0.12 → 0.28–0.35 for the harder "someone's fingernails" bar. Dropping the illusion lifts the ceiling more than the floor. The drafted design's flaws (comb, soft neck, ratchet, metronome) hurt *satisfaction* too, not just the illusion.

**Unconditional, within 26 weekends** (P(reach) × P(rating)):

| Plan | P(reach) | × P(rating) | ≈ |
|---|---|---|---|
| Spec as written | 0.15 | 0.15 | **0.02** |
| Option 1 on RT3 staging | ≈ 0.38 | 0.40 | **0.15** |
| Recommended hybrid | ≈ 0.50 | 0.40 | **0.20** |

---

## 2. Pin-count trade under the new criterion

**Layouts compared** (`pins.py`, which reproduces the spec's 12-pin row figures of 100 % and 61 %):
- **4:** a "Y + centre" at R 20 (the best of three 4-pin layouts tried);
- **6:** centre + pentagon at R 18 (the best of five 6-pin layouts; minimum spacing 18 mm, field ≈ 34 mm);
- **8:** a 3 × 3 ring without its centre, at 18 mm pitch;
- **12:** the spec's 4 × 4 grid minus corners.

**How the columns are worked out.**
- **Reach per placement** is the union of R 15 mm stroke disks around the pins: the scalp touched without travel, over all headings.
- **Mass** is RT2's corrected model, calibrated to 397 g single and 575 g twin at 12 pins. It adds:
  - 7.0 g per pin (cartridge 2.3 g, block share 1.0 g, 0.62 m head harness 2.9 g, umbilical share 0.8 g);
  - RT3's Al bail (+18 g);
  - must-fix hardware (+10 g + 0.6 g per pin: QEV, float relief, head switch, mufflers, longer cartridge);
  - for the twin, pad-B fixes (+12 g + 0.6 g per pin: interlock, twin stop, QEV).
- **"Light"** means 2 mm-OD pin lines and 3 × 2 synchro lines on the head side (RT2's twin fix).
- **"Ladder"** is the spec's own §4.7 levers that break no binding decision: Ø 16 slave cylinders (−12 g for two pads), a thinned cradle and band (−10 g), and deferred balancers (−5 g).
- **Cost:** RT3's revised $1,640 at 12 pins, ≈ $43 per pin (S070 $35 + sleeve, needle, tubing, fittings, pad-B parts), + ≈ $100 must-fix hardware; the low end assumes cheap valves win the A/B.
- **Hours:** RT3's revised plan (153–215 h) + must-fixes (20–30 h), ≈ 1.5 h per pin [EST].

| | **4** | **6** | **8** | **12** |
|---|---|---|---|---|
| Active at once | 2–4; all 4 is the norm | a 3-row, or all 6 in two ranks | a 3-row, or all 8 | a 3–4 row; all 12 exceeds a sensible scratch load |
| 3-nail rake row ⟂ heading | 23 % | **100 %** | 87 % | 100 % (4-row 60 %) |
| Distinct tracks, all pins down (minimum / mean) | 3 / 3.5 | 4 / 4.7 | 3 / 6.4 | 4 / 8.6 |
| Reach per placement | 24 cm² | 29 cm² | 40 cm² | 53 cm² |
| Scratch quality [JUDG] | thin: few patterns, more travel | ≈ 12-pin: 6 edges per stroke, rows in every heading | ≈ 12-pin | best variety, *if* idle pins are parked |
| Hover-comb risk | none | low (≤ 3 idle) | low–medium | **high** (8–9 idle; needs park discipline) |
| Nail–skid clearance at the Ø 100 skid circle | ample | **≈ 10 mm, no change needed** | ≈ 6 mm (enlarge the circle) | collision (Ø 116 needed) |
| Single mass (+fixes, Al bail) | 371 g | **386 g** (369 light) | 402 g | 432 g |
| Twin, RT2 model + fixes | 511 g ✗ | 541 g ✗ | 570 g ✗ | 629 g ✗ |
| Twin + light lines | 483 g | 507 g ✗ | 531 g ✗ | 578 g ✗ |
| Twin + light + ladder | 456 g ✓ | **480 g ✓** | 504 g ✗ (marginal) | 551 g ✗ |
| S070 valves; umbilical tubes single / twin | 4; 9 / 12 | 6; 11 / 14 | 8; 13 / 16 | 12; 17 / 20 |
| Pneumatic joints (≈ 36 + 7N) | ≈ 64 | ≈ 78 | ≈ 92 | ≈ 120 |
| Parts cost incl. must-fixes | ≈ $1,350–1,400 | **≈ $1,440–1,500** | ≈ $1,510–1,570 | ≈ $1,510–1,740 |
| Hands-on hours | 163–233 | **166–236** | 169–239 | 175–245 |

**Reading the table.**

1. **Mass decides.** Every twin fails without light lines, so **light head-side lines are a must-fix whatever the pin count**. With every lever pulled, 12 pins fails by ≈ 50 g, 8 pins sits on the line (±20 g model error), and **6 pins passes with ≈ 20 g of margin**. Ledgers on this project have run low, so 8 is not safe. The spec's ladder step 4 ("twin pads at 8 pins") is not enough.
2. **Six keeps what 12 bought.** The spec chose 12 for "a 3-nail rake row ⟂ any heading 100 % of the time" (C1). The centre-plus-pentagon 6 also has that, at 100 %. What it gives up is the 4-nail row and ≈ 36 mm of in-pad "virtual drift". Under the new criterion the 4-nail row was a hand-likeness argument. The drift is replaced by physical travel and subset cycling.
3. **All-active is now allowed.** It no longer has to look like one hand, so all 6 can bite in two ranks at 0.2–0.25 N each (1.2–1.5 N in total). That is more edges per stroke than the 12-pin's 3–4-nail row, with no idle comb. That is the strongest scratch-quality argument for 6.
4. **Four is too thin:** 3-nail rows in 23 % of headings, for ≈ $90 and ≈ 3 h saved.
5. **Hours barely move with pin count;** the big savings are staging and deferrals (§3).

**Recommendation: 6 pins, centre + pentagon at R 18.**
- Pad B's parts are bought at 6.
- Pad B's pins tee onto the same 6 valves in point mirror, which is leap3-A L2's "6 valves drive 12 nails".
- The twin carries **12 nails in total**: the spec's count, on two heads of the hand.

---

## 3. Other simplifications the amendment permits

Each item below keeps the six bindings: helmet; circle, line and precessing line; portable box; air pins; puppet drive; one pad plus the second pad's parts bought.

| Item | Simplify to | Binding kept? | Notes |
|---|---|---|---|
| Virtual-hand row tables, row stepping | **Pin subsets:** all-6, the 3-row ⟂ heading, the alternate 3-row, single pins (spider P4) | yes | Large firmware saving; the subsets are also anti-habituation levers |
| κ-grammar, familiarity ledger, attention layer | **Defer to Stage D.** Ship a random phrase generator (pink-noise f, F, length, heading kicks, pauses; region schedule) plus a **safety ledger** (H-5.5 strokes per patch, ≤ 50 passes per minute, skid passes) | yes; a Director binding, *deferred* not deleted | Keep the JSON score format so later layers drop in. The attention layer is now person-illusion |
| Squeeze egg | **Three buttons on the hand controller** (THERE / MOVE ON / LIGHTER–HARDER) or RT3's bought bulbs | yes; deferred | Steering to the itch is satisfaction. The pneumatic egg was about no wires, and the controller already has two |
| Head scan | **Defer.** Manual fences by jog plus a button; grain and canopy entered by hand; curvature boost from the ellipsoid model | yes; deferred | Fences are safety, so they are set and verified at C4, not skipped |
| Travel in the first on-head stage | **Fixed pose, manually indexed:** a static halo with 5–7 detented poses. Between bouts the pad retracts on lever release and Michael re-indexes by a knob | yes | Gives location changes and a ≥ 7/10 answer before ≈ 50–65 h of travel. Powered travel follows in Stage C |
| Circle mode | In firmware from day 1. **On the head only after** the B5 circle wig run and the token checker | yes | — |
| Tip variant sets | The new cone, D-6 control and H-3 massager control only, 6 sticks each | yes | — |
| Per-pin sensors (12) | Defer (RT3) | yes | — |
| Master | **XY belt stage** (RT3 2.1) | **needs Michael's one-line OK** | Decision 2 wording says "opposite-direction cranks". The modes are identical, and stroke length becomes free per stroke. Fallback: printed eccentrics |
| Constant-support gait | Palm feed-forward only; tune from the B6 trace | yes | — |

**Not simplified:** fail-to-free, hold-to-run plus the NC e-stop, the force caps, the hair suite, and the twin provisions (split bail, right pitch bay, double drum).

---

## 4. Recommendation

### 4.1 The three options compared

| | Option 1 (12 pins, all fixes) | Option 2 alone (fewer pins, no fixes) | Option 3 (leap round) | **Hybrid (recommended)** |
|---|---|---|---|---|
| Parts | ≈ $1,510–1,740 | ≈ $1,350 | $0 now; unknown later | **≈ $1,440–1,500** |
| Hours | 175–245 | ≈ 145–205 | +2–4 weeks before any bench | **≈ 165–230** |
| Mass, single / twin | 432 / ≥ 551 g ✗ | 355 / 494 g on paper, but unrouted harness and red lines open | — | **386 (370 light) / 480 g ✓** |
| P(on-par), conditional [JUDG] | 0.40 | ≈ 0.20 (comb gone; neck, ratchet and clock remain) | unknown until bench | **0.40** |
| P(≥ 7/10 in 26 weekends) | ≈ 0.15 | not allowed: red lines 3, 8 and 13 open | ≈ 0.12–0.18 | **≈ 0.20** |

**Why not Option 1.** Its 12-pin twin is illegal, so it already hides a forced pad-B redesign, and it pays ≈ $260 for hand-like 4-nail rows the amendment dropped.

**Why not bare Option 2.** Nearly every must-fix is independent of pin count.

**Why not Option 3.** No red team says the architecture is wrong; every must-fix is cheap. The open question (does a hover-and-bite POM cone feel like a good scratch through *his* hair?) is answered by a $40 one-nail rig in a week, not by a fourth paper round.

### 4.2 Hybrid summary

- **Pad:** 6 pins, centre + pentagon at R 18.
- **Fixes:** all the MUST fixes of §1.
- **Simplifications:** the deferrals of §3.
- **Staging:** RT3's sensation-first plan.
- **Change control:** issue an ADDENDUM-3 to SYSTEM-SPEC before the Day-0 cart.
- **Michael's sign-offs:** the XY master, 6 pins on pad B, and deferring the egg, scan and κ-grammar to Stage D.

### 4.3 Staged plan in five lines

1. **S0, week 1 (≈ 10 h; ≈ $350 cart).** Long-lead parts plus a one-nail rig: rigid-shaft POM cone, sleeve pin, bought relief, S070, button. Also the coin-and-bike-helmet evening and the earplug servo test. **GO:** scratch-like in ≥ 6 of 8 headings and ≥ 6/10 on the scalp.
2. **A, 4–5 weekends (45–60 h; ≈ $550).** Safety loop (relay hold-to-run, weld check); rails with deadhead-limited pumps and diverse reliefs; XY master; 3 sleeve synchro lines (low p₀, breakers, VREF); the 6-pin block on a bench deck; sleeve-life rig with the park cycle. **GO:** V5–V8 gates, and the hand-held 6-pin pad on the crown rated ≥ 6/10.
3. **B, 4 weekends (40–55 h; ≈ $350).** Full pad (RCC, skids, Airpel float with QEV and relief, filters, mufflers); static halo with indexed poses; Apache box; wig and force gates; fixed-pose sessions of 5 → 10 minutes. **GO:** ≥ 7/10 "as good as a good scratch", zero pulls.
4. **C, 4–6 weekends (50–65 h; ≈ $200).** Hub pods with GT2 and biased STS servos; bent Al bail; ±40° stops; ear-axis umbilical with pogo lanyard; head-present switch; light lines. **GO:** C1–C8 met, single ≤ 400 g.
5. **D, 2–4 weekends (10–20 h; ≈ $50).** 20-minute sessions with the armrest switch and THERE buttons. Then the deferred layers (scan, ledger, κ-grammar, egg) one at a time as blind A/B. The twin only after a measured light-line mass check ≤ 480 g.

### 4.4 Must-fix list (condensed)

1. **Nail:** one-piece drafted POM cone on a rigid, nose-guided Ø 1 shaft. No neck, sleeve, ferrule or lean stop. Reserve ≥ 12 mm; breakaway above the nose; re-proof at 3×.
2. **Synchro:** p₀ 8–12 kPa, relief at p₀ + 4, vacuum breakers, stepper VREF limit. Sleeve test with the park cycle.
3. **Normal caps:** pump deadheads (palm ≤ 30 kPa, rail ≤ 50 kPa), diverse "b" reliefs, measured equilibrium, 10 µm filters.
4. **Fail-to-free:** float QEV and relief poppet (≤ 150 ms).
5. **Electrical:** relay or MOSFET hold-to-run with a weld check; /G AND OE; head-present switch.
6. **Geometry:** β stops ±40° (firmware ±36°), a mechanical twin stop, pad-B palm interlock; ear-axis umbilical exit; routed light harness; skid clearance ≥ 8 mm by CAD.
7. **Sensation firmware:** per-stroke length, period and heading jitter with pauses; all-active pin subsets and park the rest; spring feed-forward, 0.20 N floor, curvature boost; gear bias; snag criterion; wig-set dwell limit with STAY; skid ledger; circle token checker.
8. **Comfort:** armrest hold-to-run by D4; posture rule.
9. **Build:** RT3 bought substitutes, plug deletion, Al bail, Day-0 part codes, sensation-first staging.
