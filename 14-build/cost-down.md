# SP1 v3 cost-down: where the money goes and how to cut it

**Project SCRATCH · 14-build/cost-down.md · cost-down analyst · 2026-10-02**

**Inputs read:** `S0/cart-S0a.md`, `S0/cart-S0b.md`, `drivebox/parts.md`, `electronics/parts.md`, `halo/parts.md`, `pad/parts.md`, `tests/test-protocols-v3.md` §1, `12-sp1v2/SYSTEM-SPEC-v3.md` §5.4–5.5, §7, §10, §13, `13-outsourcing/diy-vs-hire.md` §1.3, `12-sp1v2/DECISION-3.md`, `01-foundations/safety-requirements.md` (§2.8, §3.10, §4, §7), `12-sp1v2/safety-ruling-dish-gate.md` §4, and `12-sp1v2/redteam-3-buildability.md` §6 (tool list).

**Price tags:**
- **[pkg]**: price cited in the package file named, checked by that package on 2026-10-02.
- **[cited]**: I checked it on 2026-10-02 (URL in §7).
- **[snippet]**: from a search-result snippet on 2026-10-02; the page itself was not opened.
- **[est]**: estimate.

Every line that is neither [pkg] nor [cited] should be read as [est].

**Tax and shipping:** Florida sales tax is taken as 6 % of goods [est]. JLC duty and DHL are listed as their own lines. Other shipping is estimated per stage.

---

## 0. Answer first

| | As designed | **Balanced** | **Lean** |
|---|---|---|---|
| Parts | $2,548 | $2,151 | $1,781 |
| Test kit (tests §1) | $234 | $208 | $143 |
| Tools no cart carries yet (soldering, calipers, meter, taps, carbon tools…) | $200 | $175 | $142 |
| JLC 40 % US duty + DHL | $150 | $134 | $103 |
| Other shipping [est] | $95 | $68 | $55 |
| FL sales tax 6 % [est] | $179 | $152 | $124 |
| **All-in, S0a → D, no printer** | **≈ $3,405** | **≈ $2,888** | **≈ $2,348** |
| Printer, if Michael has none | Bambu A1 mini $219 sale / $299 list [cited] | A1 mini $219 | used Ender-3 V2 ≈ $100 [est] |
| **All-in with a printer** | **≈ $3,624** | **≈ $3,107** | **≈ $2,448** |

**The honest current total is about $3,400, not $2,350, and not the spec's $1,360.**
- The packages double-buy about $490.
- Against that:
  - about $180 of parts are owned by no package;
  - JLC duty was left out of two packages;
  - PAD's own arithmetic is $97 low;
  - about $200 of tools sit in no cart;
  - tax and shipping were not counted.
- See §1.3 for the reconciliation.

**What the cuts do:**
- **Lean cuts ≈ $1,060**, or ≈ $1,180 with the used printer, and costs ≈ 17–29 extra hours.
- **Balanced cuts ≈ $520** and costs ≈ 7–13 extra hours.
- **Neither scenario touches** a red line, a ruling condition C1–C8, or a DECISION-3 item. Each change that needs a sign-off says so in §2.

**Five biggest savings (Lean vs as designed):**

| # | Saving | $ | Who must say yes |
|---|---|---|---|
| 0 | **Stop double-buying** (S0b and ELECTRONICS buy the same controller and supply; S0b and DRIVE BOX buy the same steppers, cable, crimps and housing; three screw kits; three scales; two helmets; two hinge pairs…) | **≈ $490** against the package sum. This is already inside the "As designed" column. | nobody: just the cart rules in §1.2 |
| 1 | **Pneumatics, cheaper equivalents:** generic Ø 3 push-fits, AliExpress XGZP sensors, PIN A on the spare uxcell 3-way from the PALM 2-pack, no interim relief spare, cheaper gauge and filters | **$146** | Michael + DRIVE BOX. Gates A1/A2 (C3 vent ≤ 100 ms) verify it. |
| 2 | **Light Penrose float instead of an Airpel E16 4-pack.** The Airpel is HALO's own mass BLOCKER (96 g); it is also orphaned (§1.4). | **$126** (incl. the smaller HALO print) | **Director + PAD/HALO** (HALO CONFLICTS #1) |
| 3 | **Used Ender-3 V2 as Michael's printer** instead of an A1 mini | **≈ $119** [est] | Michael (+4–8 h of tuning) |
| 4 | **Self-turned POM nails** instead of CNC (and the 40 % duty on them) | **$104** | Michael. PAD's own option; the C2 shadowgraph still gates. |
| 5 | **Bike shift housing instead of the out-of-stock Chamfr coil** (the spec's own R2 fallback), decided by the S0b ink rig | **$94** | Michael + DRIVE BOX, on S0b data |
| 5b | **Controller:** Manta **M5P** (+ Pi Zero 2 W in Lean) instead of M8P V2 + CB1 | **$93** (Balanced $67) | Michael + ELECTRONICS (resource remap) |

---

## 1. One rolled-up BOM by stage, de-duplicated

### 1.1 How to read it

- **One row = one purchase.** When two or more packages list the same thing, it is bought once, in the earliest stage that needs it. The "covers" note names what it replaces, for example "covers DB 1.1" (DRIVE BOX parts §1.1).
- **IDs:**

  | ID prefix | Source |
  |---|---|
  | a/b | cart-S0a |
  | A/B/C | cart-S0b in Stage S0b |
  | 1.x–6.x | drivebox/parts.md |
  | E# | electronics/parts.md |
  | HB / H | halo/parts.md |
  | PAD… | pad/parts.md |
  | K# | tests §1.1 |
  | TL | tool lists |

- **Columns.** "As designed" is each package's own choice, with one purchase per item. "Balanced" and "Lean" are the scenarios in §3. A dash means "not bought".
- **Hinge and float.** "As designed" follows HALO's default build: medium hinges and the Airpel float. Balanced and Lean use the small hinges and the light float, which is HALO's own recommended build.
- **Carries forward.** Everything bought in Stage A or later *is* the machine, so it carries to D. For S0a and S0b the table names the stage each item carries into.
- **Line by line.** The full line list, by stage and with all three scenario prices, is in §8.

**Stage totals, with shipping and tax:**

| Stage | Goods: as designed / balanced / lean | Shipping [est] | Tax 6 % | **Stage cash** | **Cumulative** |
|---|---|---|---|---|---|
| S0a | 183 / 163 / 138 | 10 / 8 / 8 | 11 / 10 / 8 | **204 / 181 / 154** | 204 / 181 / 154 |
| S0b | 453 / 356 / 241 | 20 / 15 / 12 | 27 / 21 / 14 | **500 / 392 / 268** | 704 / 573 / 422 |
| A (Cart 2 = 2a + 2b) | 1,787 / 1,572 / 1,349 | 45 / 30 / 22 | 100 / 88 / 76 | **1,932 / 1,690 / 1,447** | 2,637 / 2,263 / 1,869 |
| B (Cart 3) | 668 / 537 / 411 | 15 / 10 / 8 | 39 / 31 / 23 | **721 / 577 / 442** | 3,358 / 2,841 / 2,311 |
| C (Cart 4) | 30 / 30 / 20 | 5 | 2 / 2 / 1 | **37 / 37 / 26** | 3,394 / 2,877 / 2,337 |
| D | 10 | 0 | 1 | **11** | **3,405 / 2,888 / 2,348** |

**Stage A is 57 % of the money.** It is split into two carts in §4.

**If the build stops at a gate, this is what has been spent:**

| Stops at | As designed | Balanced | Lean |
|---|---|---|---|
| S0a gate | $204 | $181 | $154 |
| S0b gate | $704 | $573 | $422 |
| The A1 gate (Cart 2a only) | ≈ $1,670 | ≈ $1,437 | ≈ $1,232 |

### 1.2 Cart rules that remove the double-buying (≈ $490)

| Bought twice or more in the packages | Buy once as | Removed |
|---|---|---|
| **M8P + CB1, TMC2209 × 4, Mean Well 24 V, DC jack, microSD**: S0b A1–A7 *and* ELECTRONICS S0 cart #1–5 | S0b only. ELECTRONICS keeps only the fuse holder (#6), which no S0 cart had. | $214.75 |
| 3 × 17HS08 steppers, tendon cable, crimps, 4 mm housing: S0b *and* DRIVE BOX §1 (1.1, 1.4, 1.5, 1.7) | S0b | $91.07 |
| Screw kits: S0a A7, HALO B-15, HALO S0-5 M4 screws, DRIVE BOX 6.2 | one M3/M4/M5 510-pc kit (DB 6.2), bought at S0a | $21.99 |
| Heat-set inserts: DRIVE BOX 6.1 and HALO B-13 | DB 6.1 at Stage A | $9.99 |
| Helmet: S0a B1 and HALO S0-1. Tape: S0a B4 and HALO S0-4. Hinges: S0a B2 small *and* HALO S0-3 medium. | one helmet, one tape, **one** hinge pair (the size the Director picks) | $31.36 |
| Scales: S0a A6, test K2, PAD jewellery scale | S0a A6 | $28 |
| Series springs: S0b B5 and PAD | S0b B5 | $9 |
| PTFE spray: S0a A2 and PAD S0 | S0a A2 | $8 |
| Ø 3 dowels: DB 3.6 and HALO B-5 | HALO B-5 kit, bought at Stage A | $7 |
| GX12 helmet-loop connector: DB 4.2 and ELECTRONICS #13 | ELECTRONICS #13 | $7.89 |
| Clip-seat magnets: DB 4.5 Ø6 × 3 and HALO B-8 Ø6 × 3 50-pack | HALO B-8 | $8 |
| Heat-shrink: DB 4.7 and ELECTRONICS #25 | ELECTRONICS #25 | $8 |
| Halls: DB 1.12/1.13 *and* ELECTRONICS #21/#22 | DB 1.12/1.13, on the DigiKey order that already carries K1 | $10.64 |
| Head switch: HALO B-11 and ELECTRONICS #27. Pogo lanyard: HALO B-12 and ELECTRONICS #28. | one each | $9 |
| 0–15 psi gauge: DB 2.24 and K14. Spare XGZP: DB 2.8 (5th) and K13. | one each | $15 |
| Monofilament: PAD and K19. Earplugs: S0b C6 and K27. Washers: DB 4.6 and HALO B-25. | one each | $9.50 |
| **Total** | | **≈ $490** |

### 1.3 Reconciliation: package sum to honest total

| Step | $ |
|---|---|
| Package totals as written: S0a 123 + 10 printing, S0b 436, DRIVE BOX 925 (mid), ELECTRONICS 435, HALO 435 (mid), PAD 330, tests 230 | **≈ 2,920** |
| − double-buys (§1.2) | − 490 |
| + parts no package counts (§1.4): Airpel 4-pack 130.50, QEV + float relief 14, the "S0" S070 35 | + 180 |
| + 40 % US duty on the DRIVE BOX and PAD JLC orders (HALO and S0a include it; DB and PAD do not) | + 80 |
| + the diverse reliefs' real price: Generant VRV 3 psig is **$51 each** [cited], not $30 | + 20 |
| + **PAD arithmetic:** its Stage A lines sum to ≈ $352 at mid-points, but its subtotal says $255 | + 97 |
| + tools that no cart carries (RT3 §6 list: soldering kit, calipers, meter, tube cutter; DB taps and step drill; HALO saw, files, mask, insert tip; trimmer) | + 200 |
| + Stage C spares and Stage D consumables allowance [est] | + 40 |
| + choices and range picks: DB option-A housing (+25), medium hinges (+10), bigger screw kit (+6), a whole PETG spool (+12), McMaster and K&J shipping kept inside goods (+13), HALO print (+8) | + 74 |
| **Goods** | **≈ 3,130** |
| + shipping ≈ 95, tax ≈ 179 | **≈ $3,405** |

### 1.4 Orphans and conflicts found while rolling up (owners must close these before ordering)

| # | Finding | Effect | Owner |
|---|---|---|---|
| O1 | **Airpel E16D2.0N is in nobody's total.** HALO's total says "Airpel bought by PAD". PAD's file says "HALO owns the float". It is sold only as a 4-pack, $130.50 delivered [pkg HALO]. | + $130.50 | HALO + PAD; Director (CONFLICTS #1) |
| O2 | **QEV + float relief is in nobody's total.** DRIVE BOX says "(HALO)"; HALO says "(DRIVE BOX parts)". | + ≈ $14 | DRIVE BOX |
| O3 | **The first S070 is in nobody's total.** DRIVE BOX buys 1 of 2 "(1 already in S0)", but neither S0 cart has one. | + $35 | DRIVE BOX (buy both in Cart 2a) |
| O4 | **Pump deadhead.** BODENFLO's store lists the **BD-02A as 120 kPa (1.5 L) or 150 kPa (3 L)**, $16 [cited]. Spec §7.2 relies on **P1 ≤ 50 kPa and P3 ≤ 30 kPa** as the mechanical backup force cap (V12). This is not a cost item, but no pump should be bought, cheap or not, until DRIVE BOX names one with a published deadhead in range. A1 still measures it. | safety, $0 | **DRIVE BOX, before Cart 2a** |
| O5 | Clip magnet: DB 4.5 Ø6 × 3 and HALO B-10 Ø10 × 3 both claim "the 3 N umbilical clip". | pick one | DRIVE BOX + HALO |
| O6 | Hall parts differ: DRV5053 RA/VA (DB) against EA (ELECTRONICS); DRV5023 (DB) against A3144 (ELECTRONICS). | pick one | DRIVE BOX + ELECTRONICS |
| O7 | C1 breakaway magnet: Ø 3 × 2 (spec V-N2, S0a A5) against K&J D21B Ø 3.18 × 1.59 (PAD). Both are cheap. The magnet that passes A2 C1(a)(b) is the one that is bought again. | $0 | PAD |
| O8 | Hinge: S0a buys the small E6-10-101; HALO's default is the medium E6-10-301. Buy one pair, the size the float decision implies. | − $15 to − $25 | Director (with O1) |

---

## 2. Cost-down options

**Columns.** "Saved" is against the as-designed column in §1, before tax.

**OK needed:**
- **M**: Michael;
- **WP**: the named work package confirms that its design still closes;
- **Dir**: Director.

The **Check** column names the decision, red line or condition that was checked.

### 2(a) Salvage: a used 3D printer

**Market check (2026-10-02).**
- A used **Ender-3 V2** is not $50–120 in most listings:
  - eBay "for parts" V2 sold for **$70** [snippet];
  - a like-new V2 on Facebook Marketplace sold for **$150** [snippet];
  - eBay listings run from about $90 to $150+ [snippet].
- The original Ender-3, with its 8-bit board, is cheaper locally [est $60–100].
- Plan on **≈ $100** for a working V2 in SW Florida [est].

**What each part is worth to SP1:**

| Part of the printer | Use it in SP1? | Why |
|---|---|---|
| **As Michael's printer** (220 × 220 bed; prints PLA and PETG) | **YES: the best use** | It replaces the A1 mini (**$219** sale, $299 list [cited]). Saves ≈ $119. RT3 §6 asks for a ≥ 220 mm bed; the V2 meets that, the A1 mini does not. It costs 4–8 h of levelling, tuning and repairs, and is slower and louder than the A1 mini. **You cannot both print with it and strip it.** |
| **Its board (Creality 4.2.2, 4 × soldered TMC2208, STM32)** as the **SP1 box controller** | **NO** | (1) **One 24 V input feeds the logic *and* the drivers.** Spec E2/E3 and safety-requirements §4 item 1 need motor power switched by the loop while the MCU stays up, and the M8P/M5P do this with a separate motor-power (HV) input. (2) It has **3 MOSFET outputs** (hot-end, bed, fan) [cited pinout]; SP1 drives **7 loads plus the watchdog** (spec §5.5). (3) It has **2 thermistor ADCs**; SP1 needs 7 analog inputs. Closing the gaps needs a second MCU, an ADC and a MOSFET board, plus a USB-powered-logic hack that nobody has verified. That is ≈ $35 of add-ons and ≈ 8 h, to save a $53 M5P. Not worth it. |
| **Its board as the S0b Klipper bench** (V-K1, V-K2 timing) | **YES (Lean)** | Flash Klipper on the printer and host it on a **Pi Zero 2 W ($15)** [cited launch price; verify today's price]. Run the 3 pancake steppers on X/Y/Z for the timing and ink-rig tests. **This defers the controller purchase ($79) to Stage A**, so if S0 fails, it is never spent. Re-run V-K1 on the real board at A0 (≈ 30 min). The Pi Zero carries forward as the M5P's host. **Red lines 4 and 5:** for any S0b step with the deck on Michael's head and motors energised (the earplug A/B), power the board from the **Mean Well 24 V adapter through the e-stop puck and the hold-to-run lever** (bought early, Lean S0b "EST"), never from the printer's own supply. |
| Steppers (42-40 class) | NO | They are ≈ 2× the mass of the 20 mm pancakes, which threatens the **2.8 kg box cap (spec §6, binding)**, and DB02 is drawn for 20 mm bodies. The saving would only be $24–36. |
| **24 V supply (open-frame, mains)** | **NEVER** | **Red line 5** and safety-requirements §2.8: no mains inside any SP1 enclosure or on the rig; certified external adapter only. Keep the Mean Well GST60A24. |
| End-stops, wiring | marginal | SP1 homes on Hall index sensors; a Hall endstop is not a microswitch. The stepper leads are useful only if the printer is retired. |

**Verdict.** Buy one used V2 as the printer (Lean). Do not buy a second, dead printer as a parts donor: the $30–70 [snippet] buys nothing SP1 can use safely.

### 2(b) Cheaper equivalents, every line over $20

| Line (as designed) | Cheaper equivalent | Saved | Risk | OK | Check |
|---|---|---|---|---|---|
| **M8P V2 + CB1 + heatsink**, $160.49 [pkg] | **Balanced:** **Manta M5P + CB1**, $88.21 [snippet, eBay] (M5P alone $52.99 [cited West3D]), plus an ADS1115 ($5.81, 1/3 of a 3-pack [snippet]) and two logic MOSFETs ($1). **Lean:** M5P $52.99 + **Pi Zero 2 W** $15 over USB. | **$67 / $93** | **M5P facts** [cited BTT docs]: 5 driver sockets; outputs HE0, HE1, HB, FAN0, FAN1, Pi-FAN; 3 thermistor inputs; MIN1–4; **"VIN … HV (DC24–56V) Selectable"**, so ACT-24 can feed the motor rail separately, like V-E1. **Mapping:** the two NO dumps (45 mA each) go on GPIO-driven 2N7000s; the watchdog PWM goes on any GPIO (`pwm_tool` runs on any pin); 3 pressures on TH, the rest on the ADS1115 (**Klipper has `[ads1x1x]`** [cited]). **Lost:** M8P headroom. Pad-2 outputs then need a $5 MOSFET module later. **Pi Zero risk:** 512 MB for Klipper + scorer + reflexd at 280 Hz is tight; if it struggles, add a CB1 (≈ $35 [est]). | M, WP ELECTRONICS (remap §5.5, `printer.cfg`, ≈ 3–5 h) | DECISION-3 #6 ("stock 3D-printer controller board running Klipper") kept. Red lines 4/13 kept: the loop is still hardware. |
| 2 × S070 PIN valves, $70 (one orphaned) | **Lean:** PIN A = the **second valve of the uxcell 3-way 2-pack** already bought for PALM (B07XCV799G, ≈ $9.99–12.16 per 2-pack [snippet]). PIN B stays an S070 (25 Hz PWM; life). | $35 | Cheap valve on the group-change line. **C3 still gates it:** NC to the rail, vent when off, ≤ 100 ms at the gallery (A2 scope trace). If it fails, buy the S070 ($35 [cited]). | M, WP DRIVE BOX | Ruling C3 unchanged (verified, not assumed) |
| SMC push-fits, reducers, tees, plugs, $79.58 [pkg est] | generic 1/8 in × M5 push-fits ($2.33 each [cited Pneumatic Depot]) and Amazon tee / manifold packs. This is DRIVE BOX's own "lean" line. | $30 | Grip on 3.18 mm tube; leak hunting 1–2 h. A1 leak-down catches it. | M, WP DRIVE BOX | — |
| 5 × XGZP6847A at DigiKey, $30 | **AliExpress / eBay 3.3 V modules**: $0.99–5.59 [snippet], 3.3 V 0–40 kPa listing on eBay [snippet] | $15 / $18 | Clone accuracy. The U-tube manometer (K15) calibrates each one anyway (A1). 2–4 weeks' lead: order with S0b (≈ $12; the only cross-stage buy). | M | — |
| Diverse reliefs R1b/R2b (Generant), real ≈ $51 each [cited] | **Smart Products 300-series** at a 3.5 psi setpoint, ≈ $29 each [snippet] | $20 | Still a different make (spec §7.2 diversity kept). Setpoint availability [verify]. | WP DRIVE BOX | Red line 2 backups kept |
| 3 × McMaster 4277T51 (+1 interim), $27 | buy 2, no interim spare | $9 | none | M | — |
| 2 × AFW 5 m spools, $40.98 [pkg] | **1 × Beadalon 49-strand (7 × 7) 0.018 in, 30 ft** ($21.99 [pkg DB]): 9 m covers 3 × 1.8 m with two spare tendons | $19 | none (same spec T1) | M | — |
| Chamfr 304V coil housing, $87.70, **out of stock** [pkg] | **Balanced:** S0b B6 sheath spring + PTFE liner ($18.49 [pkg]). **Lean:** the 4 mm bike housing already bought at S0b (the spec's R2 fallback). | $69 / $88 | **Decided by S0b test T6 data.** The bike housing is stiffer and heavier in the umbilical; C6 (yaw torque ≤ 0.02 N·m, head share ≤ 15 g) checks it. | M, WP DRIVE BOX on S0b data | Spec R2 fallback |
| DP420 + gun + nozzles, $73.01 [pkg] | **J-B Weld 50133 plastic bonder, $6.79** [pkg HALO], **only if every node passes the 20 N pull proof** (halo.md §6.6). Fallback if a node fails: the DP420 37 mL plunger pack (no gun; ≈ $27–55 [snippet]). | $66 | Head-borne structural joints; the proof test decides. | M, WP HALO | Red line 9/10 proofs unchanged |
| CNC-turned POM nails, $60–110 + 40 % duty | **Self-turned** from Ø 4 mm POM rod in a drill with a file and the PD17 card: PAD's own option. uxcell 4 mm POM rod, 500 mm [snippet, price not shown, est $8]. | $77 + $31 duty | Land tolerance follows the stock rod (pick rods that pass the Ø 3.95 slot). **C2 shadowgraph + slip-loop 10/10 still gate every nail.** +2–4 h | M, WP PAD | Ruling C2, red lines 9 and 11 unchanged |
| Airpel E16 4-pack, $130.50 (orphan) | **Light float**: 5/8 in Penrose sleeve in a printed PA12 Ø 16 bore, ≈ $15 [pkg est]. HALO's own recommendation; it also clears HALO's **96 g mass BLOCKER**. | $116 (+ $10 of print) | It changes the float force path (spec §7.2 "total" cap, R6). HALO, PAD and Safety must re-close B2/B4. | **Dir**, WP HALO + PAD | §7.2 force caps re-verified at B2 and B4 |
| JLC DHL: 2 Stage A shipments, $45 | **one** JLC order per stage (DB SLA + PAD SLA/MJF + PD19), with HALO's batch and PAD's Stage B deck in one Stage B order | $20 (A); $0 (B, already combined) | Slightly later drums; order 2b in one go | M | — |
| Soldering kit (RT3: Pinecil + tips), $70 | a $25–30 temperature-controlled iron + insert tip [est], or **borrow** | $25 / $40 | none for perfboard and inserts | M | — |
| Real-hair heads, 2 × $35 | $29.69 each [pkg tests]. **Lean:** **one** head, run long first, then trim to 3–5 cm. | $11 / $40 | C8 re-runs B5 on the long head. Run C8 long before trimming, or keep Kanekalon as the long proxy. | M, WP TESTS | B5 hair gate unchanged |
| Halo MJF PA12 batch ($75–105 incl. duty) | — | — | **Not offered.** DECISION-3 #7 (outsourced precision printing) and head-borne strength. | — | binding |
| Apache 2800 case, $29.99 | — | — | Spec §6 is **binding** on the Apache case (the ply box is a fallback at +6 h). | — | binding |
| Mean Well GST60A24, $21.99 | — | — | Certified adapter: **red line 5**. | — | red line |
| McMaster 4277T51 3 psi reliefs; K1 SFS2 force-guided relay; TAL221 100 g load cell | — | — | Force caps, the weld check and the ruling C1(c) tether test. Keep. | — | red lines 2, 4; ruling C1 |

### 2(c) Defer or borrow the test gear

- **Defer.** The test kit is already split: Cart 2 ≈ $160, Cart 3 ≈ $70. Keep it that way. Buy nothing for B5 hair work, C6 yaw or D5 before that cart.
- **Already owned or bought earlier:**
  - pocket scale (S0a), logic analyser (S0b), safety glasses (S0a), earplugs (S0b);
  - kitchen scale, calipers, phone (owned per the tests file).
- **Lean drops or borrows:**
  - K7 macro lens: phone camera ($10);
  - K22 IR thermometer: borrow, or tape a spare thermistor on a TH input ($15);
  - K20 comb, lint roller, cloth: household ($8);
  - K24: binder clips are household ($3);
  - second wig head ($30–35).
- **Borrowable tools** (a friend, or a makerspace day pass [est]): soldering iron, multimeter, calipers, step drill, taps.
  - **Borrowing all five takes another ≈ $90 off Lean** (not counted in §3).
- **Never skip:** the TAL221 100 g + 500 g cells and the Pico/ADS1115 logger.
  - Ruling C1(c) needs ≤ 0.30 N peak and ≤ 20 ms above 0.15 N. An HX711 cannot see that (tests §1.1).

### 2(d) Design simplifications that remove parts without changing the experience

| Idea | Verdict | $ | Why |
|---|---|---|---|
| One pump instead of P1 + P3 | **No** | would save ≈ $25 | P3's own low deadhead (≤ 30 kPa) is the palm/float force-cap backup (§7.2). One pump at P1's 50 kPa removes that layer. Needs a safety re-ruling for $25. |
| One NO dump instead of RAIL DUMP + PALM DUMP | **No** | would save $8 | They vent two separate pressure circuits. Joining them couples the rail and the palm. Fail-to-free (B4, red line 8) depends on both. |
| Drop one diverse relief (R1b or R2b) | **No** | $30 | It is the per-nail and total force cap's second make (red line 2 margin, spec §7.2). |
| Fewer pressure sensors (drop S_A, S_B) | **No** | ≈ $2 with AliExpress parts | Not worth losing the C3 vent evidence. |
| Drop the 5th (spare) sensor | Balanced: keep (it covers K13) | $1–6 | — |
| **PIN A on the spare PALM-pack valve** | **Lean: yes** | $35 | See 2(b); C3 gates it. |
| NeoPixel ring → a $3–4 WS2812 clone or 3 LEDs | Lean: yes | $5.50 | Status only. |
| LED kit (S0b C2) → the ELECTRONICS #9 resistor kit bought at S0b instead, plus one LED from it or the Pico's LED | Balanced + Lean | $13 | Same parts, bought once. |
| S0b rig plywood reused as the box tray (DB 3.2 Baltic birch) | Balanced + Lean | $14 | The rig is dismantled after S0b. 1/4 in sanded ply against 6 mm birch: fine for a tray. |
| Apache foam reused for lining and baffles (DB 3.5) | Lean | $5 | DRIVE BOX's own lean note. |
| Bumpon feet (HALO B-22 pack) instead of sorbothane hemispheres (DB 3.3) | Lean | $9 | Box vibration: A5 ≤ 30 dBA checks it. |
| Household luggage strap instead of the Strapworks cam strap | Lean | $9 | Chair-back hanging only. |
| Household 250 ml and 30 ml bottles as accumulators | Lean | $14 | Volume matters, not brand. C3 needs the accumulator **rail-side**; that is unchanged. |
| Gooseneck → any clamp-on phone gooseneck | Lean | $8 | The 3 N clip still pops first (C6). |
| Custom ply box instead of the Apache | **No** | $30 | Spec §6 is binding; +6 h. |
| Home-print the HALO, pad or drum SLA/MJF parts | **No** | $150+ | DECISION-3 #7. |

### 2(e) Already in a typical household (counted at $0 in Lean)

| Item | Instead of |
|---|---|
| Spare PC or monitor IEC cord | S0b A5, $8.83 |
| micro-USB cable | E26, $3 |
| Rubber band, candle wax, superglue | S0a A10, A2, A11 |
| Marbles, binder clips, comb, lint roller, black cloth | — |
| Cable ties, report-cover PET/PP sheet | — |
| Luggage strap | — |
| Kitchen scale, drill, hacksaw, phone with 240 fps | (already assumed by the packages) |

**Often owned; ask before buying** (≈ $90 together): multimeter, soldering iron, calipers, luggage scale.

---

## 3. Three budget scenarios

| | **As designed** | **Balanced** | **Lean** |
|---|---|---|---|
| **All-in, S0a → D** (goods + test + tools + duty + shipping + tax) | **≈ $3,405** | **≈ $2,888** | **≈ $2,348** |
| + printer if none | + $219 (A1 mini, sale) → **$3,624** | + $219 → **$3,107** | + ≈ $100 (used Ender-3 V2) → **$2,448** |
| Saving against as designed | — | ≈ $517 (≈ $517 with printer) | ≈ $1,057 (≈ $1,176 with printer) |
| What is in it | every package as written, bought once; medium hinges + Airpel; M8P + CB1; SMC fittings; CNC nails; DP420; two wig heads; full test and tool kit | **M5P + CB1**; **light float + small hinges** (Director); one Beadalon spool; sheath-spring housing candidate instead of Chamfr; generic push-fits; AliExpress sensors; Smart Products reliefs; one JLC DHL per stage; household cord and USB; ply tray from the S0b rig | Balanced, plus: **used Ender as printer and as the S0b Klipper bench** (controller bought at Stage A); **Pi Zero 2 W host**; **PIN A on the spare uxcell valve**; **self-turned nails**; **J-B Weld (proof-gated)**; bike housing only; **one wig head**; trimmed test kit (no IR thermometer or macro lens); cheaper iron and meter; household straps, bottles, feet, foam |
| **What is lost** | — | M8P headroom (8 drivers, more outputs; pad-2 outputs need a $5 module later); SMC fitting quality; the Chamfr coil (only if T6 says the thin sheath spring is not enough) | Everything Balanced loses, plus: a turnkey printer (the Ender is slower, louder, needs tuning); CB1 RAM margin (Pi Zero 512 MB; fallback ≈ $35 CB1); CNC precision on the nails (hand-turned, still shadowgraph-gated); DP420 margin (J-B Weld must pass the 20 N proofs, else buy DP420); a quality valve on PIN A (C3-gated); a lighter thin housing (C6-gated); a second wig head; some test conveniences |
| **Safety, decisions, ruling** | — | **No red line, ruling condition or DECISION-3 item changed.** The light float needs the **Director** and a re-close of B2/B4 force and fail-to-free. | **Same.** Every substitution has a named existing gate that verifies it: C3 (PIN A), C2 (nails), halo §6.6 20 N (epoxy), C6 (housing), A1 (sensors, fittings). |
| **Extra hours** (on the spec's ≈ 115–175 h) | 0 | **≈ 7–13 h**: M5P remap and config 3–5; light float build 2–4; generic fittings 1–2; sensor calibration 1 | **≈ 17–29 h**: Balanced 7–13, plus Ender tune-up 4–8, Klipper on the printer for S0b 2–3, Pi Zero host set-up 1–2, nail turning 2–4, J-B Weld proofs 1, household swaps 1–2 (minus the light-float overlap) |
| **Calendar** | — | + 0–2 weeks (AliExpress) | + 1–3 weeks (AliExpress; the Ender may need parts) |

**Recommendation.**
- **Take Balanced now.** It is almost all "buy once" and "swap a part a gate already checks".
- **Add any Lean items Michael accepts:** the used printer, self-turned nails, J-B Weld, PIN A valve, one wig head and the household swaps. Each is independent.
- **Ask the Director this week** for the light-float ruling. It is the single largest decision-gated saving, and HALO needs it anyway (mass BLOCKER).

---

## 4. Per-stage spending plan: never more than one cart outstanding

**Rule:** place a cart only after the previous gate is **GO** and every box of the previous cart has arrived. Stage A is too big for one cart, so it is split at the A1 gate.

| Cart | Place it when | Contents | As designed | **Balanced** | **Lean** |
|---|---|---|---|---|---|
| **S0a** | now | dish benches, helmet, **one** hinge pair, coin bag, tape, pocket scale, the **combined** screw kit; filament. Lean: buy the used Ender here (+ ≈ $100). | $204 | $181 | $154 (+ $100 printer) |
| **S0b** | S0a GO | tendon rig, the 3 steppers, cable, crimps, housing, Mean Well, fuse; controller (Balanced) or **Pi Zero only** (Lean). Lean also: e-stop puck + lever (for the head-on earplug A/B), and the ≈ $12 of AliExpress sensors (lead time). | $500 | $392 | $268 |
| **2a** | S0b GO | **A0 + A1:** controller (Lean: M5P + drivers now), safety-loop parts, all pneumatics, the pump with a confirmed deadhead (O4), A0/A1 test items (manometer, gauge, logic dividers), the tools for A0 (iron, meter, calipers, cutter, taps) | ≈ $967 | ≈ $864 | ≈ $810 |
| **2b** | A1 GO (reliefs and deadheads measured) | **A2–A5:** one combined JLC order (DB drums + bulkhead + plug, PAD SLA/MJF + PD19) and the nails (CNC, or POM rod in Lean); drum-module hardware; K&J magnets; pad consumables; Apache case; force logger and load cells; wig head #1 | ≈ $965 | ≈ $826 | ≈ $637 |
| **3** | A GO (≥ 6/10) | HALO carbon, hardware, epoxy, float (Airpel or light), HALO + PAD-B JLC batch, umbilical, lanyard; B test kit (head #2, Kanekalon, lazy-susan) | $721 | $577 | $442 |
| **4** | B GO | spares and reprints | $37 | $37 | $26 |
| **D** | as needed | consumables | $11 | $11 | $11 |
| **Total** | | | **$3,405** | **$2,888** | **$2,348** |

**Notes on the plan:**
- **The largest single cart in Lean is ≈ $810** (2a), and only after two cheap gates have passed. In Balanced it is ≈ $864.
- **Cash at risk if S0 says NO-GO:** as designed $704, Balanced $573, Lean $422.
  - Even then, most of S0b (steppers, supply, cable, housing, logic analyser) carries into any revisited drive.
  - In Lean the controller has not been bought yet.
- **The one exception to "one cart"** is the ≈ $12 of AliExpress sensors ordered with S0b, for the lead time. If S0b fails, they are a $12 loss.
- **JLC lead time.** Cart 2b's JLC order takes ≈ 2 weeks (build + DHL). Place it the weekend A1 passes. A0/A1 bring-up does not need those parts.

---

## 5. Sign-offs this needs (all small)

| Who | Decides | For |
|---|---|---|
| **Michael** | which Lean items he accepts: used Ender, Pi Zero host, self-turned nails, J-B Weld (proof-gated), PIN A valve, one wig head, borrowing tools, household swaps | up to ≈ $540 beyond Balanced |
| **Director** | light float vs Airpel, and therefore the hinge size (O1, O8; HALO CONFLICTS #1) | $116–126 |
| **DRIVE BOX** | names a pump with a published deadhead ≤ 50 kPa (P1) and ≤ 30 kPa (P3) **before Cart 2a** (O4); generic fittings; Smart Products relief setpoint; QEV ownership (O2); the first S070 (O3); clip magnet (O5) | safety + $60–80 |
| **ELECTRONICS** | the M5P resource map (6 MOSFET outputs + 2 × 2N7000 dumps + GPIO watchdog + 3 TH + ADS1115) and the HV motor-input jumper (the V-E1 analogue); Hall part choice (O6) | $67–93 |
| **PAD** | self-turned nails acceptable under C2; C1 magnet part (O7); fix its Stage A subtotal ($255 → ≈ $352) | $104 |
| **TESTS** | one-head sequencing (long first, then trim; run C8 before trimming) | $30–35 |

---

## 6. Not recommended (each would break a binding item for little money)

| Idea | Why not |
|---|---|
| Using the Ender's open-frame supply | **Red line 5**: mains on the rig |
| The Ender board as the SP1 box controller | It cannot switch motor power separately from the logic (spec E2/E3; safety-requirements §4). Too few outputs and ADCs. |
| Cheaper pumps of unknown deadhead | Removes the §7.2 backup cap. See O4. |
| One pump; one shared dump valve; dropping a diverse relief | These are force-cap and fail-to-free layers (red lines 2, 3, 8) for $8–30 each |
| Dropping the 100 g load cell or the fast logger | Ruling **C1(c)** cannot be shown with an HX711 or a kitchen scale |
| Home-printing the halo, pad or drum precision parts | **DECISION-3 #7** |
| Custom box instead of the Apache 2800 | **Spec §6 binding** |
| Skipping the tension Halls or the comparator latch | Ruling **C4** snag reflex, red line 13 |
| Hiring out | Not cheaper (diy-vs-hire §2) |

---

## 7. Sources I checked (2026-10-02)

**Controller:**
- BTT Manta M5P features (5 sockets; HE0/HE1/HB, FAN0/FAN1/Pi-FAN; 3 thermistors; VIN/HV selectable): https://github.com/bigtreetech/docs/blob/master/docs/M5P.md [cited]
- Manta M5P $52.99, West3D: https://west3d.com/products/btt-manta-m5p-klipper-controller-board-3d-printer-control-system-using-cb1-cm4 [cited]
- Manta M5P + CB1 $88.21 (sale), eBay: https://www.ebay.com/itm/316021045855 [snippet; page blocked]
- BIQU Manta page: the M8P V2.0 board alone shows $84.38: https://biqu.equipment/products/manta-m4p-m8p [cited]
- Klipper `[ads1x1x]` (ADS1115) config: https://www.klipper3d.org/Config_Reference.html and https://github.com/Klipper3d/klipper/pull/6584 [cited]
- ADS1115 HiLetgo 3-pack $17.43: https://www.ebay.com/itm/195732344557 [snippet]
- Raspberry Pi Zero 2 W "$15": https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/ and https://www.raspberrypi.com/news/new-raspberry-pi-zero-2-w-2/ [cited; today's store price was not shown, so verify]
- Creality 4.2.2 Klipper pins (fan PA0, hot-end PA1, bed PA2, 2 thermistors, 3 endstops; V2 ships with TMC2208): https://klipper.discourse.group/t/creality-board-4-2-2-and-4-2-7-schematics/3104 and https://support.dremc.com.au/support/solutions/articles/51000421257-creality-4-2-2-4-2-7-schematics [snippet]

**Printers:**
- Used Ender-3 V2, "for parts" sold $70 and listings ≈ $90–150: https://www.ebay.com/b/Ender-3-3D-Printers/183063/bn_7115149350 [snippet]
- Ender-3 V2, Facebook Marketplace, like-new $150: https://www.facebook.com/marketplace/item/1859447097857294/ [snippet]
- Bambu A1 mini $219 sale / $299 list: https://www.tomshardware.com/3d-printing/bambu-labs-a1-mini-is-perfect-for-beginners-and-super-attractive-in-this-limited-3rd-anniversary-sale-now-26-percent-off-and-just-usd219 and https://stacksheriff.com/3d-printing/bambu-lab-pricing/ [snippet]

**Pneumatics:**
- BODENFLO BD-02A $16; **1.5 L variant 120 kPa, 3 L variant 150 kPa**: https://bodenpumpstore.com/products/12v-eccentric-diaphragm-air-pump-bodenflo [cited]
- SMC S070C-6DC-32 $35.00, 1,723 in stock: https://automationdistribution.com/s070c-6dc-32/ [cited]
- uxcell 2-position 3-way 12 V 0.2 A 2-pack (B07XCV799G), ≈ $9.99–12.16: https://www.amazon.com/uxcell-Miniature-Solenoid-Valve-Position/dp/B07XCV799G and https://www.harfington.com/products/p-1092493 [snippet]
- Generant VRV 1/4 in, 3 psig, $51.00: https://www.globaltestsupply.com/product/generant-vrv-vent-relief-valve-ss-14-port-size-3-psig [snippet]
- Smart Products relief valve ≈ $29.15: https://www.fishersci.com/shop/products/NC0623392/NC0623392 [snippet]; 300 series (0.09–20 psi; 1/8 NPT and barbs): https://smartproducts.com [snippet]
- XGZP6847A 0–40 kPa modules $0.99–5.59: https://www.aliexpress.us/item/3256805773943271.html [snippet]; 3.3 V module: https://www.ebay.com/itm/175769735852 [snippet]
- 1/8 in tube × M5 push-to-connect $2.33: https://pneumaticdepot.com/pc-1-8-m5c.html [snippet]

**Test kit and tools:**
- TAL221 100 g $14.50: https://www.sparkfun.com/mini-load-cell-100g-straight-bar-tal221.html [snippet]
- Real-hair mannequin heads, ≈ $24–30: https://www.walmart.com/c/kp/mannequin-head-human-hair [snippet]; tests §1.2 cites $29.69 for 100 % human hair
- Harbor Freight 9-function meter with audible continuity, $24.99 (coupon price $16.99 seen on an older coupon page, so verify): https://www.harborfreight.com/9-function-digital-multimeter-with-audible-continuity-59410.html and https://go.harborfreight.com/coupons/2024/04/182744-59410/ [snippet]

**Materials:**
- 3M DP420 Duo-Pak: 50 mL $52–60; 37 mL $26.94 (out of stock): https://skygeek.com/3m-021200-41528-scotch-weld-epoxy-adhesive-cp420-duopak-black-1-25-oz.html and https://www.walmart.com/ip/101632389 [snippet]
- uxcell Ø 4 mm POM rod, 500 mm (price not shown): https://www.amazon.com/uxcell-Plastic-Length-Polyoxymethylene-Engineering/dp/B07SZFCFNR [snippet; $8 est]

**All other prices** are the packages' own [pkg] citations from 2026-10-02, or [est].

---

## 8. Line-by-line BOM (de-duplicated)

**How to use it:**
- Each line is bought once, in the stage shown.
- Subtotals are goods only. Shipping and tax are in §1.1.
- Stage A is split into Carts 2a and 2b as described in §4.

#### Stage S0a

| ID | Item (what it also covers) | As designed $ | Balanced $ | Lean $ | Carries forward to |
|---|---|---|---|---|---|
| a1 | POM balls 6mm | 7 | 7 | 5.90 | A (pad domes) |
| a2 | PTFE dry lube (covers PAD S0 spray) | 7 | 7 | — | A (drums, carriage) |
| a3 | 7in ball | 10.95 | 10.95 | 10.95 | bench only |
| a4 | spring kit | 10 | 10 | 7 | bench only |
| a5 | 3x2 N52 magnets 100 (covers DB 1.14) | 11 | 11 | 11 | A (C1 trials, index magnets) |
| a6 | pocket scale (covers K2, PAD jewel scale) | 13.99 | 13.99 | 13.99 | tool, all stages |
| a7 | M3/M4/M5 SHCS kit (covers S0a A7, HALO B-15, S0-5, DB 6.2) | 15 | 15 | 15 | all stages |
| a8 | M3 set screws | 7 | 7 | 7 | S0b, A |
| a9 | safety glasses 2pk | 3.62 | 3.62 | 3.62 | B (session rule) |
| a10 | elastic cord | 3.19 | 3.19 | — | bench only |
| a11 | superglue | 3 | 3 | — | all |
| b1 | Schwinn helmet w/ dial (covers HALO S0-1) | 16.67 | 16.67 | 16.67 | B/C (dial cradle, if UltAlt skipped) |
| b2 | Southco hinges x2 (AD medium 301; BAL/LEAN small 101) | 24.96 | 14.68 | 14.68 | B (halo α hinges) |
| b3 | alu flat bar | 3.93 | 3.93 | 3.93 | test only |
| b4 | tape measure (covers HALO S0-4) | 2.99 | 2.99 | 2.99 | C fit |
| h1 | UltAlt dial 2-pack | 7.97 | 7.97 | — | B (halo cradle) |
| p0 | PAD S0 pocket: PTFE balls + wet/dry paper (+PD19 SLA AD standalone) | 25 | 15 | 15 | A (pocket finish data) |
| f1 | S0a filament | 10 | 10 | 10 | — |
| | **Goods subtotal** | **183** | **163** | **138** | |

#### Stage S0b

| ID | Item (what it also covers) | As designed $ | Balanced $ | Lean $ | Carries forward to |
|---|---|---|---|---|---|
| A1 | controller: AD M8P+CB1; BAL M5P+CB1; LEAN Pi Zero 2 W (board deferred to A) | 154.59 | 88.21 | 15 | A controller (LEAN: host for M5P) |
| A2 | TMC2209 x4 | 26.43 | 26.43 | — | A |
| A3 | CB1 heatsink | 5.90 | 5.90 | — | A |
| A4 | Mean Well GST60A24 (red line 5) | 21.99 | 21.99 | 21.99 | A (E1 supply) |
| A5 | IEC cord | 8.83 | — | — | A |
| A6 | barrel jack (covers ELEC #4) | 4.99 | 4.99 | 4.99 | A |
| A7 | microSD | 12.29 | 8 | 8 | A |
| A8 | 3 pancake steppers (covers DB 1.1) | 35.97 | 35.97 | 35.97 | A drum motors |
| E6 | inline fuse holder + T3.15A (ELEC #6, not in S0b cart) | 6 | 6 | 6 | A |
| EST | e-stop puck + 1 lever moved early (LEAN only; from Cart A) | — | — | 15.86 | A (safety loop) |
| B1 | tendon cable: AD 2x AFW 5m; BAL/LEAN 1x Beadalon 30ft (covers DB 1.4) | 40.98 | 21.99 | 21.99 | A tendons + 2 spares |
| B2 | crimp sleeves (covers DB 1.5) | 9.49 | 9.49 | 9.49 | A |
| B3 | crimper (covers DB tool) | 14.59 | 14.59 | 14.59 | tool |
| B4 | 4mm shift housing (covers DB 1.7) | 30.99 | 27 | 27 | A housing |
| B6 | thin sheath spring + PTFE liner | — | 18.49 | — | A housing candidate |
| B5 | McMaster series springs + ship (covers PAD series springs) | 20.30 | 20.30 | 20.30 | A series springs |
| C1 | logic analyser (covers ELEC tool, K8) | 12.69 | 12.69 | 12.69 | tool A0 |
| C2 | LED kit (BAL/LEAN: ELEC #9 resistor kit bought here instead) | 12.99 | — | — | A |
| C3 | Dupont jumpers | 3.99 | 3.99 | 3.99 | A |
| C3b | test hooks | 7 | 7 | 7 | tool A0 |
| C4 | marbles | 6.29 | 6.29 | — | rig only |
| C5 | 1/4 ply 2x2 (reused as box tray at A) | 8.61 | 8.61 | 8.61 | A (box tray, BAL/LEAN) |
| C6 | screws + earplugs (covers K27 earplugs) | 5 | 5 | 5 | rig only |
| T | T01-T06 printing | 3 | 3 | 3 | rig only |
| | **Goods subtotal** | **453** | **356** | **241** | |

#### Stage A

| ID | Item (what it also covers) | As designed $ | Balanced $ | Lean $ |
|---|---|---|---|---|
| 1.6 | Chamfr 304V coil housing (OOS) | 87.70 | — | — |
| 1.8 | ferrules | 6.99 | 6.99 | 5 |
| 1.9 | LM4UU | 12.99 | 12.99 | 12.99 |
| 1.10 | 4mm rods | 8 | 8 | 8 |
| 1.11 | compression springs | 7 | 7 | 7 |
| 1.12 | index Halls (covers ELEC #22) | 2.20 | 2.20 | 2.20 |
| 1.13 | tension Halls x7 (covers ELEC #21) | 6.78 | 6.78 | 6.78 |
| KJ | K&J D21B x4 + D42 x6 + ship (DB 1.14 flexure + PAD C1 + coupling) | 14.84 | 14.84 | 14.84 |
| 1.15 | isolators | 12 | 12 | 6 |
| 1.16 | 623ZZ + nickels | 8.50 | 8.50 | 8.50 |
| 2.1 | pumps x2 [deadhead VERIFY] | 36 | 36 | 36 |
| 2.2 | PIN valves: S070 x2 (one orphaned from S0); LEAN PIN A = spare uxcell from PALM 2-pack | 70 | 70 | 35 |
| 2.3 | PALM 3-way | 14 | 14 | 14 |
| 2.4 | NO dumps x2 | 16 | 16 | 16 |
| 2.5 | McMaster 4277T51 | 27 | 18 | 18 |
| 2.6 | diverse reliefs x2 | 80 | 60 | 60 |
| 2.7 | relief adapters | 24 | 24 | 17 |
| 2.8 | XGZP sensors x5 (covers K13) | 30 | 15 | 12 |
| 2.9 | inline filters | 17.62 | 17.62 | 8 |
| 2.10-15 | push-fits, reducers, tees, manifolds, bulkheads | 79.58 | 50 | 50 |
| 2.16 | PU 1/8 | 9.20 | 9.20 | 9.20 |
| 2.17 | PU 4mm | 14.20 | 14.20 | 14.20 |
| 2.18 | silicone tube | 7 | 7 | 7 |
| 2.19 | needles | 10 | 10 | 10 |
| 2.20 | Luer barbs | 8 | 8 | 8 |
| 2.21 | accumulator bottles | 19 | 19 | 5 |
| 2.22 | sorbothane | 15 | 15 | 15 |
| 2.23 | O-ring kit | 10 | 10 | 10 |
| 2.24 | 0-15 psi gauge (covers K14) | 10 | 6 | 6 |
| QEV | QEV + float relief (orphan: HALO<->DB) | 14 | 14 | 14 |
| 3.1 | Apache 2800 | 29.99 | 29.99 | 29.99 |
| 3.2 | Baltic birch (BAL/LEAN: S0b ply) | 14 | — | — |
| 3.3 | sorbothane feet | 8.95 | 8.95 | — |
| 3.4 | cam strap | 9.10 | 9.10 | — |
| 3.5 | EVA foam | 5 | 5 | — |
| 3.6 | dowels -> HALO B-5 kit bought here | 8.99 | 8.99 | 8.99 |
| 3.7 | thumb screws | 6 | 6 | 2 |
| 3.9 | M5 fender washers | 4 | 4 | 4 |
| 6.1 | M3 inserts (covers HALO B-13) | 12 | 12 | 12 |
| 6.3 | standoffs | 10 | 10 | 5 |
| 6.4 | epoxy/CA/threadlocker | 20 | 20 | 12 |
| JLC-DB | DB SLA (drums, bulkhead, plug) | 42 | 42 | 42 |
| JLC-PAD | PAD SLA 45 + MJF 27.5 (+PD19 10 in BAL/LEAN) | 72.50 | 82.50 | 82.50 |
| CNC | PAD CNC POM nails (LEAN: self-turned, rod) | 85 | 85 | 8 |
| DUTY | US duty 40% on JLC goods (not in DB/PAD totals) | 79.80 | 83.80 | 53 |
| DHL | JLC shipping (AD: 2 shipments; BAL/LEAN: 1) | 45 | 25 | 25 |
| PETG | PETG spool | 20 | 20 | 20 |
| E7 | K1 force-guided relay | 16.64 | 16.64 | 16.64 |
| E8 | safety semis | 9 | 9 | 9 |
| E9 | passives kit | 12 | 12 | 12 |
| E10 | perfboard, terminals | 9 | 9 | 9 |
| E11 | 12V buck | 3.99 | 3.99 | 3.99 |
| E12 | e-stop puck (LEAN: bought at S0b) | 14 | 14 | — |
| E13 | GX12/GX16 connectors (covers DB 4.2) | 28 | 28 | 28 |
| E14 | Omron levers x2 (LEAN: one at S0b) | 3.72 | 3.72 | 1.86 |
| E15-19 | pots, MODE, button, cables | 27 | 27 | 27 |
| E20 | Pico (tension front end) | 4 | 4 | 4 |
| E23 | NeoPixel ring | 9.50 | 9.50 | 4 |
| E24 | buzzer | 1 | 1 | 1 |
| E25 | wire, Wago, ferrules, heat-shrink (covers DB 4.7) | 32 | 32 | 32 |
| E26 | USB cable | 3 | — | — |
| CTRL | LEAN: Manta M5P board + TMC2209 4-pack (deferred from S0b) | — | — | 79.42 |
| ADS | ADS1115 3-pack (box ADC + K10) | — | 17.43 | 17.43 |
| MOS | 2 x logic MOSFET for dumps (M5P route) | — | 1 | 1 |
| K3 | luggage scale (covers DB+HALO tool) | 10 | 10 | 10 |
| K5 | feeler gauges | 4.99 | 4.99 | 4.99 |
| K7 | macro lens | 10 | 10 | — |
| K9 | Pico for logger | 4 | 4 | 4 |
| K10 | ADS1115 Adafruit (BAL/LEAN in 3-pack) | 14.95 | — | — |
| K11 | TAL221 100 g (ruling C1(c)) | 14.50 | 14.50 | 14.50 |
| K12 | TAL221 500 g | 15.50 | 15.50 | 15.50 |
| K15 | U-tube manometer | 6 | 6 | 6 |
| K19 | monofilament (covers PAD mono) | 5 | 5 | 5 |
| K21 | hygrometer | 10 | 10 | 10 |
| K22 | IR thermometer | 15 | 15 | — |
| K24 | clips, hemostat | 6 | 6 | 3 |
| K28 | dividers, breadboard | 5 | 5 | 5 |
| K16a | real-hair head #1 | 35 | 29.69 | 29.69 |
| PADmag | PAD dowels, keepers, discs | 12 | 12 | 12 |
| PADpen | Penrose 25-pack | 22.19 | 22.19 | 22.19 |
| PADptfe | PTFE tube | 8.49 | 8.49 | 8.49 |
| PADwip | silicone wiper sheet | 12 | 12 | 12 |
| PADret | return springs | 15 | 15 | 15 |
| PADpun | hollow punches | 12 | 12 | 12 |
| PADfish | braided line 0.12 | 6 | 6 | 6 |
| PADkap | Kapton | 7 | 7 | 7 |
| PADpet | PET shim + PP sheet | 6 | 6 | — |
| PAD30g | 30 G needles | 7 | 7 | 7 |
| PADlift | lift springs | 10 | 10 | 10 |
| PADm2 | M2 screws | 8 | 8 | 8 |
| PADnyl | M3 nylon | 7 | 7 | 7 |
| PADbar | barrel adjusters | 6 | 6 | 6 |
| PADfilm | PTFE film | 6 | 6 | 6 |
| PADvise | pin vise + drills | 10 | 10 | 10 |
| TL-solder | soldering iron + insert tips, solder, flux | 70 | 45 | 30 |
| TL-cal | calipers | 20 | 20 | 20 |
| TL-dmm | multimeter | 25 | 24.99 | 16.99 |
| TL-cut | tube cutter | 8 | 8 | 8 |
| TL-tap | taps + wrench | 12 | 12 | 12 |
| TL-step | step drill + hole saw | 15 | 15 | 15 |
| TL-trim | trimmer screwdriver | 4 | 4 | 4 |
| | **Goods subtotal** | **1,787** | **1,572** | **1,349** |

#### Stage B

| ID | Item (what it also covers) | As designed $ | Balanced $ | Lean $ |
|---|---|---|---|---|
| 4.1 | umbilical 4-core | 7 | 7 | 7 |
| 4.3 | knit sleeve | 15 | 15 | 15 |
| 4.4 | gooseneck hanger | 20 | 20 | 12 |
| 4.6 | washers + nut (covers HALO B-25) | 1 | 1 | 1 |
| E28 | pogo lanyard (covers HALO B-12) | 6.99 | 6.99 | 6.99 |
| HB1 | carbon tube 2-pack | 32.38 | 32.38 | 32.38 |
| HB2 | carbon flat 2-pack | 20.94 | 20.94 | 20.94 |
| HB3 | carbon rod 3mm | 7 | 7 | 7 |
| HB4 | MR63ZZ | 5.39 | 5.39 | 5.39 |
| HB6 | ball plungers | 14.50 | 14.50 | 14.50 |
| HB7 | constant-force spring | 7.57 | 7.57 | 7.57 |
| HB8 | 6x3 magnets (covers DB 4.5) | 14.59 | 14.59 | 14.59 |
| HB9 | 5mm balls | 5.99 | 5.99 | 5.99 |
| HB10 | 10x3 magnets (clip) | 9.99 | 9.99 | 9.99 |
| HB11 | D2F-01FL switch (covers ELEC #27) | 3.22 | 3.22 | 3.22 |
| HB14 | M4 inserts | 8 | 8 | 8 |
| HB17 | #10-32 nuts | 1 | 1 | 1 |
| HB18 | DP420 + gun + nozzles (LEAN: J-B Weld 50133, proof-gated) | 73.01 | 73.01 | 6.79 |
| HB21 | helmet pad kit | 6.49 | 6.49 | 6.49 |
| HB22 | Bumpon | 9.99 | 9.99 | 9.99 |
| HB23 | O-ring cord | 6 | 6 | 6 |
| HB26 | cable ties | 3.99 | 3.99 | — |
| FLOAT | AD Airpel E16 4-pack (orphan); BAL/LEAN light Penrose float | 130.50 | 15 | 15 |
| HP | HALO MJF PA12 incl 40% duty | 90 | 80 | 80 |
| HDHL | HALO JLC DHL (BAL/LEAN shared with PAD B) | 25 | 25 | 25 |
| HP3 | H19/H20 jigs | 8 | 8 | 8 |
| PADB | PAD 2nd deck + spares (rides HALO order) | 25 | 25 | 25 |
| TLH | HALO tools: files, saw, mask, insert tip, sandpaper/IPA | 46 | 46 | 36 |
| K16b | real-hair head #2 (LEAN: one head, long then trimmed) | 35 | 29.69 | — |
| K17 | Kanekalon | 4.99 | 4.99 | 4.99 |
| K20 | comb, lint roller, cloth | 8 | 8 | — |
| K23 | dowel + tape | 5 | 5 | 5 |
| K25 | lazy susan | 10 | 10 | 10 |
| | **Goods subtotal** | **668** | **537** | **411** |

#### Stage C

| ID | Item (what it also covers) | As designed $ | Balanced $ | Lean $ |
|---|---|---|---|---|
| SPARE | Cart 4 spares/reprints [est] | 30 | 30 | 20 |
| | **Goods subtotal** | **30** | **30** | **20** |

#### Stage D

| ID | Item (what it also covers) | As designed $ | Balanced $ | Lean $ |
|---|---|---|---|---|
| CONS | consumables (sleeves, cable reterminations) [est] | 10 | 10 | 10 |
| | **Goods subtotal** | **10** | **10** | **10** |
