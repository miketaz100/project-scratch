# RED TEAM 3: Buildability, cost and "will he finish it" (SP1 PUPPET HALO)

**Target:** 12-sp1v2/SYSTEM-SPEC.md (design freeze v2), against DECISION-2.md. **Date:** 2026-10-02.
**Read:** DECISION-2, SYSTEM-SPEC (all of it), 04-redteam/redteam-3-simplicity.md, 05-engineering/bom-verified.md, servo-alternatives.md, 01-foundations/component-landscape.md, RESUME.md.
**Stance:** adversarial. My job is to show that the frozen design is too big, too costly or too fragile for one person in an apartment, and to propose simplifications that keep every binding decision:

- a head-worn helmet;
- PLINE, LINE and CIRCLE modes;
- a portable drive box;
- one pad built, with the second pad's parts bought;
- air pins;
- the puppet drive (a master in the box, three sealed lines, a follower on the pad).

Prices were checked live on 2026-10-02 where a source is named. Anything else is marked [est] or [VERIFY].

---

## 0. Verdict in one paragraph

The spec is a good machine. As a build plan it is wrong for a single amateur, and wrong by about 5×. Here is what it contains:

- **About 80 printed designs (about 160 pieces).**
- **About 22 cast silicone parts**, with 0.4 mm walls, that need vacuum degassing and resin-quality moulds. Neither the degassing kit nor the moulds are in the BOM or the tool list.
- **About 120 pneumatic joints** and **about 250 solder joints.**
- **Machined eccentric bushings**, with no source for the machining.
- **A carbon "arc" bought as straight tube**, which cannot be bent.
- **A custom 20-port magnetic face-seal connector.**
- **A 1 kHz pneumatic gate scheduler** with a grammar, a ledger and a head scan.

Its staging says "weeks 1–3, 3–5, 5–7". The honest figure is **270–400 hands-on hours, or 25–35 weekends**. The first time Michael's scalp feels anything is Stage D, after about 95 % of the money and hours are spent.

The earlier red team gave the much smaller Float-Arm a 10–15 % chance of being finished in three weekends. This design, as written, has about a **10–15 % chance of reaching a full Stage D session within six months**.

The fix keeps every binding decision and changes how each one is built:

1. **Buy instead of cast or machine:** an XY belt master instead of the double-crank synthesiser; bought rolling sleeves (latex or nitrile) instead of cast diaphragms; bought fixed relief valves; dispensing needles as restrictors; a bought hard case; bought squeeze bulbs.
2. **Delete the helmet-side 20-port plug.**
3. **Hand-bend an aluminium bail.**
4. **Defer the spring balancers, 12 of the 22 pressure sensors and the score layers.**
5. **Restage the build so a sensation data point arrives in weekend 4, and a fixed-pose helmet session around weekend 8–10.**

That plan costs **about $1,410–1,640** in parts, against an honest **≈ $1,900** for the spec as written. It roughly triples the chance that he reaches the hypothesis.

---

## 1. Parts count, skills, tools, hours and the honest probability

### 1.1 Inventory, spec as written (counted from §2, §4, §5, §9, §13)

| Category | Count | Notes |
|---|---|---|
| Bought line items | ≈ 130–150 | 12 S070 valves, 8 utility/dump valves, 3 pumps, 22 (+4) sensors, 3 MCP3208, 3 TMC/TPIC chips, 2 steppers, 3 servos, bearings, magnets, carbon, PU tubing in 2 sizes, fittings |
| Printed designs | ≈ 80 (≈ 160 pieces) | Halo ≈ 30. Pad ≈ 20 designs × 12 pin cartridges. Box ≈ 20. Controller, egg and puck ≈ 6. Bench fixtures ≈ 8 (bail stand at R 210, wig sled, pen holders). |
| Cast silicone parts | ≈ 22 + moulds | 12 pin diaphragms (Ø 7, 0.4 mm wall, 24 mm stroke), 6 synchro (Ø 20, 34 mm stroke), 1 float (50 mm stroke), the 3-chamber egg, plus the pad-B set |
| Precision fits he cannot easily hit | 6 | r₁ = r₂ = 7.50 ± 0.05 mm machined eccentrics; a 0.08 ± 0.015 N split-PTFE hover collar ×12; Ø 0.15–0.25 mm restrictors and bleeds ×24; ±1 kPa printed relief poppets ×6; a 20-port gasket face seal sealing ≤ 0.2 kPa/min at 12 N; bail radius R 210 |
| Pneumatic joints | ≈ 120 | Each one is a leak to hunt. The synchro budget is ≤ 0.2–0.5 kPa/min per line, through two connectors. |
| Solder joints | ≈ 250–300 on perfboard | 22 sensors × 3, 20 valve channels, 2 TMC2209, safety loop, bucks, bus buffer |
| Firmware features | ≈ 25 | 1 kHz gate scheduler with analytic path prediction, per-pin latency calibration, three PIDs, two stepper phase generators, servo bus, κ-grammar, ledger, egg attention layer, head scan, registration, blind A/B, SD logging, fault tree |
| Distinct skills | **≈ 14** | FDM printing (PETG, TPU, inserts); **silicone casting with degassing**; **resin mould making**; **machining or outsourcing turned parts**; pneumatic plumbing and leak hunting; relief calibration; tendon and capstan rigging; zero-length spring balancing; **bending a 690 mm arc**; perfboard soldering at scale; TMC2209 UART configuration; Feetech bus servos; real-time ESP32-S3 firmware bring-up; measurement (ink traces, 240 fps, SPL, load cell) |
| Tools missing from the spec | 5 | vacuum chamber + pump for degassing (≈ $90–150); a resin printer or SLA mould service (≈ $40–60 a batch); an oscilloscope or logic analyser (A0 demands "1 ms, scope"); a tube bender or form; a lathe or a CNC service for the eccentrics |

The earlier red team counted about 11 skills and about 30 printed designs for the Float-Arm and called it a 20–25 % proposition. This design has more than double the printed work, adds casting and pneumatics, and keeps every firmware layer.

### 1.2 Hours and P(stage finished in 4 weekends)

Assumptions: about 11 focused hours per weekend (two 5–6 h days), so 4 weekends ≈ 45 h. Print time runs overnight and is not counted. A 1.5× first-timer factor is applied to my estimates.

| Stage (spec) | What it actually contains | Hands-on hours | P(done in 4 weekends) | Median |
|---|---|---|---|---|
| **A**, drive box ("weeks 1–3") | Safety loop; 3 pumps, 3 accumulators, 6 printed reliefs; 22 sensors; master synthesiser (2 stages, 6 eccentrics, Oldham); 6 cast Ø 20 cylinders; slave deck with bell cranks and a parallelogram; 12 valves; **12 real pin cartridges** (casting, collars, restrictors); enclosure; firmware bring-up | **130–180** | **≈ 3 %** | 12–16 weekends |
| **B**, pad on a wig head ("weeks 3–5") | Pad finish, radial float (a cast 50 mm diaphragm), RCC struts, **bench bail at R 210 + carriage** (halo parts), load-cell sled, 8 gates | 50–80 | ≈ 15 % | 6–8 |
| **C**, halo with travel ("weeks 5–7") | Hub pods ×2 (bearings, capstan, drum, balancer, cartridge bays), bail bend + splice, tendon in a PTFE guide, umbilical (17 tubes), 20-port plugs ×2, hanger, cradle fit, 8 gates | 70–110 | ≈ 8 % | 8–10 |
| **D**, human (D1–D4) | Checklist, sessions, egg, scan | 10–20 | ≈ 75 % | 2 |

**P(reaching D4 within 26 weekends) ≈ 15 %. P(ever) ≈ 30 %.**

The three likeliest places to stop:

1. **The first diaphragm casting session.** A 0.4 mm top-hat in a 7 mm bore, with an FDM mould, bubbles and tearing on demould: the scrap rate is near 100 % for a beginner. Twelve are needed before A4 can run.
2. **Weekend 8 or so, with the box still half-plumbed** and no sensation data at all.
3. **The bail.** The carbon arrives straight.

---

## 2. Custom, hard-to-source and precision parts, with bought substitutes

| # | Spec item | Problem | Substitute (real part, price, stock as checked) | Binding decision kept? |
|---|---|---|---|---|
| 2.1 | **Two-stage parallel-crank master**: 6 eccentrics, 2 stage plates, POM Oldham, "machined" r₁ = r₂ = 7.50 ± 0.05 | No lathe and no machining source. The Oldham is a novice-hostile print. Stroke length is fixed at 30 mm (r₁ + r₂), so per-stroke **length jitter is impossible**. | **XY belt stage**: two stacked MGN12 rails (≈ $12–15 each [est]), GT2 belts and 20T pulleys (≈ $12), two **StepperOnline 17HS08-1004S** pancake NEMA 17s (**$7.99** each), the same TMC2209s. The path is pure software: circle, line, precessing line, a free stroke length per stroke, heading jumps without a 150 ms motor-B reversal. Load ≤ 5 N and a ≈ 1.2 m/s² peak are trivial for this stage. Phase lock is still exact by step count. 3 (twin: 6) master cylinders ride the top plate, which translates without rotating by construction. | **Yes.** It is still a master synthesiser in the box. Note: if the crank is kept, the ±0.05 mm is over-specified. An r mismatch Δr only makes the line an ellipse of half-width Δr, so ±0.2 mm meets the 0.5 mm bow pass line; printed eccentrics with press-fit bearings, trimmed by ink trace, would do. |
| 2.2 | **Cast silicone rolling diaphragms**: 6 synchro (Ø 20) and 12 pins (Ø 7, 0.4 mm wall) | Needs degassing and resin moulds (not in the BOM); about 22 castings; V4 open; R2 rated P = 0.30 for life alone | **Synchro:** printed Ø 20 bore + POM piston + a **nitrile finger cot as the rolling sleeve**, clamped by an O-ring at the flange (≈ $8 per 100) [VERIFY flat width for Ø 20]. **Pins:** **Graham-Field 3953.25 latex Penrose drain, 1/4 in × 18 in, pack of 25** (Amazon B00YXKSJ7E) [VERIFY wall ≈ 0.2–0.3 mm], tied off and inverted over the piston as a top-hat sleeve. Both are consumables, replaced in under 2 minutes. Gate: a drill-driven 10⁵-cycle rig (spec R2) at Stage A. Cast only if life is under 10⁴ cycles. A fabric-reinforced moulded diaphragm (Alibaba-class, custom size) is the SP2 route, not SP1. | Yes (air pins, sealed synchro) |
| 2.3 | **Radial float**: Ø 20 × 50 mm cast diaphragm + 0.3 mm bleed | A 50 mm-stroke top-hat is the hardest casting in the spec | **Airpot Airpel E16D2.0N** (graphite piston in a glass bore, ≈ 16 mm, 2 in stroke) [VERIFY bore and stroke code]: eBay new or open box **$32–50**, Radwell new ≈ $100–150. Its clearance leak (Airpot: "will slowly leak air… no true seals") *is* the float bleed, so it adds a fail-to-free path for free. At 20.7 kPa it gives 4.1 N plus 0.9 N of pad weight = 5.0 N, under red line 3 (≤ 12 N; the spec's own cap is 7.2 N). [VERIFY mass ≤ 25 g; budget 12 g, ladder applies.] Airpel is **not** suitable for the sealed synchro: my laminar estimate for a 12.7 µm clearance gives a decay τ of only ≈ 2–3 s per line. | Yes |
| 2.4 | **Printed relief poppets** R1a/R1b/R2/R2b + 3 synchro, ±1 kPa | Calibration is iterative; V9 is open; relief is a red-line part | **McMaster-Carr 4277T51**, compact nylon pressure-relief valve for air, 1/8 NPT, **fixed 3 psi = 20.7 kPa** (also sold in 0.5/1/1.5/6/10 psi) [VERIFY price ≈ $6–10 each, tolerance]. Setpoints move: pin cap 20.7 kPa → **0.80 N** (operating rail 2–13 kPa still fits); palm R2 = R2b = 20.7 kPa (two independent valves); synchro p₀ drops from 20 to **12 kPa** with relief at 20.7 kPa (stiffness falls ≈ 7 % with absolute pressure; same 8.7 kPa headroom, so the tangential cap is unchanged). | Yes |
| 2.5 | **Ø 0.20–0.25 mm restrictors, Ø 0.15 mm bleeds** ×24 | Drilling 0.15–0.25 mm holes in PETG is not repeatable | **Blunt Luer-lock dispensing needles**: 27G (ID ≈ 0.20 mm; CELLINK sells 27G at 0.20 mm ID, 50 per box) and 30G. Mixed packs on Amazon (B077WSLCHJ, 100 pcs to 27G) [VERIFY price ≈ $10]. Resistance is tuned by cut length (laminar flow), and they are replaceable. | Yes |
| 2.6 | **Split-PTFE hover collar, 0.08 ± 0.015 N** ×12 | The tightest force window in the machine; humidity-sensitive (R3) | **Ø 1 × 1 mm silicone O-ring** in a printed gland on the Ø 1.0 shaft, squeeze set by a cap shim (O-ring kit ≈ $10) [VERIFY window on the A4 rig]. Keep PTFE as the A/B. | Yes |
| 2.7 | **Carbon 10 × 8 "arc", R 210**, budgeted as "2 × 1 m" straight tube | **Straight carbon cannot be bent.** A custom curved carbon tube is a composites order. | **6061/6063 aluminium tube, 10 × 1 mm**, hand-bent over a plywood or printed form with an internal bending spring (strain r/R = 2.4 %: safe). Same EI class as the carbon (≈ 2 × 10⁷ vs ≈ 3 × 10⁷ N·mm²). **+13–23 g**, which uses part of the 48 g reserve. Carbon is an SP2 upgrade. | Yes |
| 2.8 | **20-port magnetic face-seal plug at the helmet**, 12 ± 3 N | Custom precision part; V14 and R9 (P 0.25). **The breakaway chain is mis-ordered:** the plug releases at 12 ± 3 N but the cradle sheds at ≈ 10 N, so the plug often never fires first. | **Delete the helmet-end plug.** Keep a latched block at the box only, where draw latches give ≥ 40 N of gasket clamp, so it seals easily. At the helmet, the rail-cut job moves to a **2-pin magnetic pogo breakaway on the loop wire**, with the tubes running continuously to the pad. Every line still vents, because de-energised valves in the box vent them. The 3 N hanger clip stays as fuse 1 and the cradle as fuse 2. **For RT2 to confirm.** | Yes (one umbilical) |
| 2.9 | **Zero-length spring balancers and 3:1 Dyneema capstans** | Tensioning and zeroing are fiddly; the tendon can creep | **GT2 closed-loop belt 3:1** (16T → 48T) inside the sealed pod. **Defer the balancer.** At 3:1 the worst gravity torque at the servo is 0.24/3 = 0.08 N·m, under the STS3032's 0.15 N·m rating. Add the balancer only if the C2 unpowered hold or the servo temperature fails. | Yes |
| 2.10 | **Feetech STS3032 ×3** at $33 | Thin US stock. Now **≈ $40** (AIFitLab in stock; the C001 variant back-ordered; Babsco $32.99 with 1 unit on 10-01) | Buy all 3 on Day 0 (pad B's α_R is binding). Add a **Seeed XIAO bus servo board, $5.99 US**. Fallback: XL330 via the spec's adapter B (2-month lead). | Yes |
| 2.11 | **SMC S070 ×12** at $32 | Price and code: **S070C-SDG-32 is the 5 VDC coil.** The 12 V part is **S070C-6DC-32** (12 VDC, barb Ø 3.18/Ø 2, 0.5 W, not 0.35 W), **$35.00** at Automation Distribution, **1,723 in factory stock**. Not back-ordered. | Day 0: buy **4** S070C-6DC-32 ($140) and a **uxcell 2-position 3-way 12 V mini valve 2-pack** (B07XCV799G, 0.2 A) ×2 [VERIFY price ≈ $12–15]. A/B on latency scatter, noise and life at Stage A. Buy the remaining 8 of the winner. Cheap valves would save ≈ $280. | Yes |
| 2.12 | **XGZP6847A ×26** at $3 | **Amazon US shows no offers.** Third-party sellers list $3.80–7.15, mostly shipped from China (2–4 weeks: the bom-verified back-order lesson) | Order on Day 0 from an AliExpress or LCSC-class seller. Cut to **10** for Stages A–C (rail, vac, palm, 3 synchro, 3 egg, 1 roving pin sensor on a tee). The 12 per-pin sensors and the head scan come after D2. | Yes (the scan is deferred, not dropped) |
| 2.13 | **Custom ply/PETG enclosure, 300 × 220 × 110** | 6–8 h of fabrication, and noise sealing | **Harbor Freight Apache 2800**, **$29.99**, interior **11-7/8 × 9 × 5-5/16 in (302 × 229 × 135 mm)**, pick-and-pull foam, latches, handle, IP65. Bolt the hook plate to the lid side. | Yes (portable box) |
| 2.14 | **Cast 3-chamber silicone egg** | Another mould | Three bought rubber squeeze bulbs (sphygmomanometer or ear-syringe type, ≈ $3–5 each), nubbed and taped into a printed grip | Yes (egg kept) |
| 2.15 | **Bike dial cradle** "harvested" from a $20 helmet | Fine. Also sold bare. | **UltAlt 2-pack bike helmet retention dial** (Amazon B0G3WDYMLC; 50–62 cm). Buy it plus one $20 helmet for the Day-0 coin evening. | Yes |
| 2.16 | **Vacuum pump** (P2, KPM27C class) | KPM27C pricing is all over the place ($8 resellers, $60 eBay) | **Kamoer KVP04** brushless 12 V vacuum pump, 40 kPa, 1.1 L/min, PWM (Amazon B096KFKR2J) [VERIFY ≈ $25–35]. Brushless is quieter and longer-lived. | Yes |
| 2.17 | **Pin and synchro barbs** printed, PU 3 × 2 | Printed barbs leak | Standardise on **1/8 in OD × 2 mm ID PU** (it matches the S070 barb Ø 3.18/Ø 2), with Luer barbs where the needles sit, and **4 mm OD push-to-connect** for the synchro, palm and in-box rails. Buy tees and 5-way manifolds; print none. | Yes |

---

## 3. The $1,240: where it goes and what can be cut

### 3.1 Where it goes (spec §13)

| Group | $ | Share | Biggest line |
|---|---|---|---|
| Drive box | 631 | 51 % | 12 × S070 = $384 (31 % of everything) |
| Helmet | 170 | 14 % | 2 × STS3032 = $66 |
| Electronics | 136 | 11 % | adapter, chips, e-stop |
| Second-pad parts | 104 | 8 % | STS3032, sensors, valves |
| Pad | 74 | 6 % | silicone kit, wire, PTFE |
| Printing | 70 | 6 % | PETG, TPU |
| Umbilical + hanger | 55 | 4 % | PU tubing |

**Excluded from the $1,240:** tools, the printer and the bench kit. In the Float-Arm BOM those were **$257 (tools) and $309 (bench kit)**, plus **$299–349** for a Bambu A1 if he has none.

### 3.2 Honest re-cost of the spec as written

The bom-verified lesson is that live prices plus pack sizes added **+20.5 %** (estimated $1,414 → verified $1,704), and fasteners alone came to $130.

| Adjustment | Δ $ |
|---|---|
| S070C-6DC-32 at $35, not $32 (×12) | +36 |
| STS3032 at ≈ $40, not $33 (×3) | +21 |
| XGZP6847A at ≈ $5 delivered, not $3 (×26) | +52 |
| Pumps realistic ($15 each), not $18 for three | +27 |
| Pack and consumable uplift (20 %) on the remaining ≈ $710 | +142 |
| **Missing:** degassing chamber + pump (120), SLA moulds (50), CNC eccentrics (60), Sil-Poxy (40), scope or logic analyser (25), bending form and spring (25) | +320 |
| Shipping across about 8 vendors | +60 |
| **Spec as written, honest** | **≈ $1,900** (before tools, bench kit and printer) |

### 3.3 Revised plan (all substitutions from §2)

| Group | $ | Notes |
|---|---|---|
| Drive box | ≈ 826 | 12 S070 $420; 8 utility/NO valves $48; pumps $45; 10 sensors $50; McMaster reliefs $48 [VERIFY]; needles, duckbills, O-rings $30; push-fit fittings and manifolds $40; XY master $70; finger-cot cylinders $15; Apache 2800 $30 + foam and hook $30 |
| Electronics | ≈ 175 | spec $136 + 20 %, + a $15 logic analyser |
| Helmet | ≈ 198 | 2 × STS3032 $80, bus board $6, Al tube $15, GT2 3:1 $15, rest as spec |
| Pad | ≈ 80 | Penrose sleeves replace the silicone kit |
| Umbilical + hanger | ≈ 55 | helmet plug deleted; 1/8 in PU |
| Printing, fasteners, glues | ≈ 130 | realistic packs |
| Second-pad parts (binding, bought Day 0) | ≈ 120 | STS3032 $40, 4 sensors, MCP3208 + TPIC, tees, PALM B + 4 NO valves, balls and magnets. The pad-B sleeves and needles come from the shared packs. |
| Shipping | ≈ 60 | |
| **Total** | **≈ $1,640** | **≈ $1,410** if the cheap 3-way valves win the Stage A A/B (4 S070 kept) |

**Cuts that break no binding decision, in order of dollars:**

1. Valve A/B (−$280).
2. Defer the 12 per-pin sensors, their tees and the 3rd MCP3208 (−$75).
3. No casting kit, degassing or SLA moulds (−$200 against the honest figure).
4. No machining (−$60).
5. Bought case (−$0, but 6–8 h).
6. Helmet plug deleted (−$10, about 10 h, removes R9).

The **$1,200 target is not reachable honestly with 12 S070s.** It is roughly reachable (≈ $1,250) if the cheap valves win the A/B *and* the Float-Arm Day-0 cart (if it was placed) supplies the e-stop, PETG, Dyneema, magnets, fasteners and tools.

**Staged cash:**

| Cart | When | About |
|---|---|---|
| Day 0 | S0 + Stage A + long-lead items + pad-B binding parts | $700 |
| Cart 2 | after gate A | $450 |
| Cart 3 | after gate B | $300 |
| Cart 4 | after gate C | $100 |

If gate A fails, the exposure is about $700, and most of it (valves, pumps, sensors, ESP32, steppers) is reusable.

---

## 4. Staging: is A → D coherent?

No, for five reasons.

1. **The stages are not separable by work package.**
   - A3 needs "the real slave block on the pad deck" and A4 needs "pins of the real design", so the PAD WP must be finished inside Stage A.
   - Stage B needs "the real carriage + float + pad on a bench bail segment at R 210", so HALO parts (and a bent arc) come before Stage C.
   - The stages are really one waterfall.
2. **No sensation data until Stage D**, after about 95 % of the money and hours. The cue-card evening (§14) is the only early data, and it involves no air pin. Spec risk R10 ("dabby or pad-like", P 0.30) is retired at B7 on the forearm, and only after all 12 pins, the float and the bench bail exist.
3. **The weeks are fiction.** The spec has 7 weeks to D1; my estimate is 25–35 weekends.
4. **Gates pile instrumentation in front of sensation.** A5 needs SPL, mass and orientation tests on a finished box before any pad exists.
5. **Fallbacks are expensive and late.** If A2/A3 fail on stick-slip, the fallback reopens the halo mass budget, and that is discovered only after the master and box are built.

**Rewritten plan principle:** each stage ends with a sensation data point, and the next cart is bought only when that stage's gate passes. The full plan is in §8.

---

## 5. The 24 [VERIFY] items: which block what

| Blocks | Items | Action |
|---|---|---|
| **Day-0 order** | **V2** S070 code: **closed here** (S070C-6DC-32, 12 VDC, barb Ø 3.18/Ø 2, 0.5 W, $35, in stock). **V11** sensor ranges: pick 0–40 kPa gauge, −40–0 kPa, 0–100 kPa now; long lead. **V20** PS1: buy an adjustable NC pressure switch. **V24** prices: §3 here. **V3** STS3032 stock (buy now). | Order Day 0 |
| **Helmet purchase and all HALO CAD** | **V1** head dimensions / tape fit; **V15** cradle override ≈ 10 N and ≥ 1 N·m pitch hold | $0 tape fit + $20 bike-helmet and coin evening, **Day 0–7** |
| **Cart 2 (pad geometry, cylinder size, 8 more valves)** | **V5** synchro stiffness, leak, lag; **V4** sleeve/diaphragm life; V9 (closed by the bought reliefs) | Stage A gate |
| **Pin cartridge ×12 (do not print 12 until)** | **V6** descent and restrictor; **V7** hover collar window; **V8** bleed; **V12** pump stall (sets red line 2's backup: 53 kPa → 2.04 N) | Stage A, one-pin and four-pin rig |
| **Hub motor choice (cart 3)** | **V16** bone-path servo noise; V3 mounting | Bring a C5-style earplug test forward to S0 with one STS3032 held to the skull 64 mm from the canal |
| **Stage gates only (not ordering)** | V10, V13, V14 (gone if the helmet plug is deleted), V17, V18, V19, V21, V22, V23 | as spec |

**Six items block money:** V2, V3, V11, V20 now; V1/V15 for the helmet; V5/V4/V6/V7 for the pad. V5 is the single item the whole puppet rests on, and it can be closed in Stage A's first two weekends for about $150.

---

## 6. What Michael must own, and what he can outsource

**Own (assume an empty shop):**

| Item | Approx. $ | Why |
|---|---|---|
| FDM printer, **≥ 220–256 mm bed**, direct drive (Bambu A1, $299–349) | 0–349 | ~80 designs and iteration; TPU. The A1 mini (180 mm) is enough **only if** the front band is the spec's aluminium strip and the bench bail stand is printed in segments. Buy the A1. |
| Pinecil V2 + insert tips, solder, flux | ≈ 70 | |
| Calipers, multimeter, 0.01 g scale, luggage scale | ≈ 60 | |
| **Logic analyser** (8-channel USB, ≈ $15) or a DSO kit | 15–40 | A0's 1 ms timing |
| **PU tube cutter** (≈ $8) + soapy leak spray | 10 | Push-fits leak on ragged cuts |
| Hacksaw, deburr, needle files, plywood or printed bending form + Ø 8 internal bending spring | ≈ 30 | Bail |
| Phone at 240 fps; SPL app | 0 | |

**No longer needed after §2:** vacuum degassing kit, resin printer, lathe.

**Outsource (parts made to order, not the build; this respects his 2026-10-01 "self-build" decision):**

- **JLCPCB carrier board** for the ESP32-S3, 3 sensor ADCs, 3 TPIC6B595, 2 TMC2209 sockets and the safety loop: about $20 + shipping, 1–2 weeks. It turns about 300 perfboard joints into about 120 through-hole joints and removes most wiring faults. The ELECTRONICS WP should produce the KiCad file.
- **JLC3DP MJF PA12** for the head-borne parts (hub pods, rear node, carriage) **after Stage C geometry freezes**: lighter and stronger than PETG, about $10–30 a part, 7–10 days.
- **SendCutSend** aluminium for the master base plate, the carriage plate and the box hook plate ($39 minimum).
- The eccentric bushings, only if the crank master is kept.

---

## 7. Cut / keep / substitute table

| Item (spec) | Decision | Replacement or gate |
|---|---|---|
| Helmet: bike dial cradle, front band, temple pads | **KEEP** | buy the dial (B0G3WDYMLC) + a $20 helmet; fit on Day 0–7 (V1, V15) |
| PLINE / LINE / CIRCLE in firmware | **KEEP** | generated by the XY master |
| Two-stage parallel-crank synthesiser, eccentrics, Oldham | **SUBSTITUTE** | XY belt stage, 2 × 17HS08-1004S, MGN12, GT2 |
| 3 sealed synchro lines, Ø 20, bell cranks, PP parallelogram | **KEEP** | p₀ 12 kPa with 3 psi reliefs |
| Cast synchro diaphragms | **SUBSTITUTE** | nitrile finger-cot sleeves; cast only if life < 10⁴ |
| Cast pin diaphragms | **SUBSTITUTE** | latex Penrose 1/4 in sleeves (Graham-Field 3953.25) |
| Cast float diaphragm | **SUBSTITUTE** | Airpel E16D2.0N (its leak is the bleed) |
| Printed relief poppets | **SUBSTITUTE** | McMaster 4277T51, 3 psi, ×6–7 |
| Drilled restrictors and bleeds | **SUBSTITUTE** | 27G / 30G Luer dispensing needles |
| Split-PTFE hover collar | **SUBSTITUTE (A/B)** | Ø 1 × 1 O-ring gland; PTFE as the alternative |
| 12 × S070 | **STAGE** | 4 S070C-6DC-32 + 4 cheap 3-way, A/B, then 8 of the winner |
| 22 + 4 pressure sensors | **CUT TO 10 + 4** (pad B, binding) | per-pin sensors after D2 |
| Head scan (pneumatic ToF) | **DEFER** | manual fences by jog + squeeze until D3; scan firmware after D2 |
| κ-grammar, ledger, attention layer | **DEFER past D2** | D1–D2 run from serial commands; the D2 → D4 score format is unchanged |
| Squeeze egg (3 chambers) | **KEEP, SUBSTITUTE** | 3 bought bulbs; light / hold / double gestures only |
| Hold-to-run, NC e-stop puck, watchdog, PS1 | **KEEP** | PS1 bought (adjustable NC pressure switch) |
| Fail-to-free spring lift, R2 + R2b | **KEEP** | the Airpel leak adds a vent path |
| 20-port magnetic plug at the helmet | **CUT** (RT2 to confirm) | magnetic 2-pin loop-wire breakaway; latched block at the box only. The chain was mis-ordered (12 N plug > 10 N cradle). |
| Carbon 10 × 8 bail "arc" | **SUBSTITUTE** | Al 10 × 1 tube, hand-bent; carbon in SP2 |
| Split bail, right pitch bay, double drum (twin provisions) | **KEEP** | |
| Dyneema 3:1 capstan | **SUBSTITUTE** | GT2 3:1 belt in the pod |
| Zero-length spring balancers | **DEFER** | add if the C2 unpowered hold or temperature fails |
| STS3032 ×3 (incl. pad B) | **KEEP, buy Day 0** | ≈ $40 each; Seeed XIAO bus board $5.99 |
| Custom enclosure | **SUBSTITUTE** | Apache 2800 ($29.99, 302 × 229 × 135 mm inside) |
| Perfboard electronics | **SUBSTITUTE** | JLCPCB carrier board |
| Second-pad parts | **KEEP (binding)**, trim to long-lead and specific items | pad-B consumables from the shared packs |
| RCC palm, 3 POM dome skids | **KEEP** | |
| Bench bail at R 210 for Stage B | **CUT** | Stage B uses the static halo (§8) |
| 12 pins, 18 mm pitch | **KEEP** | built as a 4-pin row first |

---

## 8. Revised stage plan with go/no-go gates

Assumes 11 h per weekend. **Every stage ends with a sensation data point.** The next cart is bought only on GO.

| Stage | Build | Hours / cash | Sensation data point | GO (to buy the next cart) | NO-GO |
|---|---|---|---|---|---|
| **S0: Day 0–7** | Tape fit (V1). $20 bike helmet + dial + coin bag, 20 min of TV (V15, C3 preview). Cue-card evening. One STS3032 held to the skull with earplugs (V16 preview). **One air nail on a stick:** pump + 3 psi relief + bleed + one S070 + one Penrose-sleeve pin + an omni-nail, fired by a button. Day-0 cart placed. | 8–10 h / ≈ $700 cart | Forearm and scalp: "nail or pad?" in 8 headings; hover-and-bite vs press-and-hold | Omni-nail reads nail-like in ≥ 6/8; the cradle holds the coin bag with lean ≤ 3/10 | Fix the tip and landing first; buy nothing else |
| **A: bench puppet, 4 weekends** | Safety loop (A0) on the carrier board. Rail and palm with bought reliefs (A1). XY master. **3 finger-cot synchro lines** to a follower block on a bench deck (A2–A3 ink traces). **A 4-pin row** on 4 S070 + 4 cheap valves, needle restrictors, O-ring hover (A4). 10⁵-cycle sleeve rig. Box parts loose on a board; no enclosure yet. | 40–55 h / — | 4-pin PLINE row on the forearm, then the crown, frame resting on its skids and held lightly; blind PLINE vs LINE vs CIRCLE | Bow ≤ 0.5 mm, shrink ≤ 1 mm at 0.5 N, leak ≤ 0.5 kPa/min (V5); descent 50 ± 10 mm/s, latency ±5 ms (V6–V8); sleeve life ≥ 10⁴; **4-pin row rated nail-like ≥ 6/10 and "machine" ≤ 4/10** | Copy fails → Ø 24 + higher p₀ (spec fallback). Sensation fails → tip and window A/B; do **not** build 12 pins or the halo |
| **B: full pad on a static halo, 4 weekends** | Pin block to 12 pins; deck, bell cranks, RCC palm, skids; Airpel float, fail-to-free (B4). **Static halo:** dial cradle + Al front band + pod *blanks* on M1, with a printed bridge holding the float at 3 poses (vertex, upper occiput, parietal). Remaining 8 valves (the A/B winner). Apache box. | 45–60 h / ≈ $450 | **The hypothesis minus travel:** 2 → 5 → 10 min sessions at 3 fixed poses on the head (D1–D3-lite, after the B2–B5 force and wig gates) | All spec B1–B5 force, proof, fail-to-free and wig gates; **"feels like fingernails" ≥ 6/10, "machine" ≤ 4/10, wants it again** | < 5/10: do not build travel; fix the pad (tips, windows, jitter, force). Hair fails → still-dome fallback |
| **C: travel, 4–6 weekends** | Hub pods with GT2 3:1 + STS3032; bent Al bail + splice; carriage, β tendon; umbilical (box-end latched block, loop-wire breakaway, 3 N clip, hanger); servo zero jig | 50–70 h / ≈ $300 | Drift 20–50 mm/s with the pad scrubbing; "does the hat move?" | C1–C8 as spec (mass ≤ 400 g incl. Al bail; bone-path test; doff ≤ 3 s; umbilical torques) | Mass or lean fails → mass ladder, or bring the twin forward; noise fails → gimbal cartridge |
| **D: sessions, 2–4 weekends, then ongoing** | Egg behaviours; 20 min scores; then the deferred layers in order: per-pin sensors + scan → ledger → κ-grammar → D5 matrix | 10–20 h / ≈ $100 | Spec D1–D5 | Spec go/no-go D | — |

**Probabilities, revised plan:**

| Stage | P(done in 4 weekends) | P(done in 6 weekends) |
|---|---|---|
| A | ≈ 40 % | ≈ 70 % |
| B | ≈ 35 % | ≈ 65 % |
| C | ≈ 25 % | ≈ 55 % |

- **P(fixed-pose sensation verdict within 12 weekends) ≈ 45 %**, against ≈ 0 % for the spec.
- **P(D4 within 26 weekends) ≈ 40–45 %**, against ≈ 15 %.
- Exposure at each NO-GO: S0 ≈ $40 of consumables; A ≈ $700, mostly reusable; B ≈ $1,150.

**Twin provisions are unaffected:**

- The XY master's top plate carries 6 cylinder mounts.
- Pad B's parts are bought on Day 0.
- The split bail, right pitch bay and double drum are built in Stage C exactly as in §9.1.

---

### Sources (checked 2026-10-02)

- SMC S070C-6DC-32, $35, factory stock 1,723, 12 VDC, 0.5 W: [automationdistribution.com](https://automationdistribution.com/s070c-6dc-32/). S070 coil codes (6 = 12 VDC, S = 5 VDC; "32" = barb Ø 3.18/Ø 2): [SMC S070 catalogue](https://ca01.smcworld.com/catalog/Clean-en/mpv/cat02-23-dc-s070_en/data/cat02-23-dc-s070_en.pdf); S070C-SDG-32 pricing $31–52: [Automation Distribution](https://automationdistribution.com/smc-s070c-sdg-32-pack-of-1/), [smcpneumatics.com](https://www.smcpneumatics.com/S070C-SDG-32.html)
- Airpel leak and clearance: [Airpot FAQ](https://www.airpot.com/faqs/), [piston leak](https://www.airpot.com/piston-leak-and-dimensional-stability/); E16 listings: [mmbt.us E16D1.5N](https://mmbt.us/products/airpel-airpot-e-16d1-5-n-e16d1-5n-e-16-d-1-5-n-anti-stiction-air-cylinder), [Radwell E16D2.0U](https://www.radwell.com/en-US/Buy/AIRPOT/AIRPEL/E16D2.0U), [eBay E16D2.0N](https://www.ebay.com/itm/366471073326)
- McMaster compact nylon relief valves 4277T51/52 (0.5–10 psi fixed): [mcmaster.com](https://www.mcmaster.com/products/nylon-relief-valves/)
- Bellofram small-bore diaphragm cylinders ($75–115 class): [Marsh Bellofram](https://www.marshbellofram.com/bellofram-pcd/products/small-bore-diaphragm-air-cylinders/)
- Dispensing needles 27G (0.20 mm ID): [CELLINK](https://www.cellink.com/product/sterile-standard-blunt-needles-27g-50-pieces/), [Amazon assortment](https://www.amazon.com/Syringe-Dispensing-Needles-Blunt-Length/dp/B077WSLCHJ)
- Penrose 1/4 in pack of 25: [Amazon Graham-Field 3953.25](https://www.amazon.com/GF-Health-3953-25-Drainage-Diameter/dp/B00YXKSJ7E)
- STS3032: [AIFitLab](https://aifitlab.com/products/feetech-sts3032-servo-motor); servo-alternatives.md §2
- XGZP6847A: [Amazon (no offers)](https://www.amazon.com/XGZP6847A-Electronic-Transmitter-Component-Performance/dp/B0F48XPH9D)
- 3-way 12 V mini valves: [uxcell 2-pack B07XCV799G](https://www.amazon.com/uxcell-Miniature-Solenoid-Valve-Position/dp/B07XCV799G)
- Kamoer KVP04: [Amazon](https://www.amazon.com/Vacuum-Negative-Pressure-Diaphragm-12V%EF%BC%8C320MA%EF%BC%8C%E2%89%A51-1L/dp/B096KFKR2J)
- 17HS08-1004S $7.99: [StepperOnline](https://www.omc-stepperonline.com/nema-17-bipolar-18deg-13ncm-184ozin-1a-35v-42x42x20mm-4-wires-17hs08-1004s.html)
- Apache 2800 $29.99: [Harbor Freight](https://www.harborfreight.com/2800-weatherproof-protective-case-medium-black-64551.html)
- Helmet dial: [UltAlt 2-pack](https://www.amazon.com/UltAlt-Retention-Replacement-Adjustable-Skateboard/dp/B0G3WDYMLC)
