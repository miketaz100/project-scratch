# DRIVE BOX parts list (live prices)

**Project SCRATCH · 14-build/drivebox · DRIVE BOX WP · 2026-10-02**

**Tags**
- **[cited]**: I saw the price on the vendor page on 2026-10-02.
- **[est]**: price from search snippets or a reseller on 2026-10-02.
- **[verify]**: no price found. The figure in the $ column is my estimate, and must be checked before ordering.

**Stages** follow SYSTEM-SPEC-v3 §10. Buy a stage's cart only after the previous gate has passed (**GO**):
- **S0**: the tendon ink rig (DRIVE BOX's S0 contribution).
- **A**: Cart 2, the bench puppet and the box.
- **B**: Cart 3, the umbilical and hanger.

**Owner notes**
- Items marked **(E)** are ELECTRONICS-owned. They are listed here only because they mount on DRIVE BOX parts. Do not buy them twice.
- The **Ref** column points to the drawing, schematic or CAD part in drivebox.md and cad/.

## 1. Drum module (puppet master): S0 for the rig, reused at A3

| # | Item | Part number / SKU | Vendor | Qty | Unit $ | Line $ | Tag | Ref |
|---|---|---|---|---|---|---|---|---|
| 1.1 | NEMA 17 pancake stepper. The listing now reads 16 N·cm, 1.0 A, body 21.5 mm, shaft Ø 5 × 20 mm, D-cut 16.5 mm. | **StepperOnline 17HS08-1004S** | omc-stepperonline.com (US site blocks bots; .ca shows C$11.59) | 3 | 7.99 | 23.97 | [est] US price; [cited] spec at stepperonline.ca | DB02 |
| 1.2 | Cable drum, Ø 12 pitch, double helical groove, SLA | **DB01_drum.stl** | JLC3DP SLA, 9600 or JLC Black resin | 3 (+1 spare) | ≈ 2 | ≈ 8 | [est] (price shown on upload) | DB01 |
| 1.3 | M3 × 6 cup-point grub screw + M3 hex nut (one each per drum) | from the screw kit (8.4) | — | 4 + 4 | — | — | — | DB01 |
| 1.4 | Tendon cable: 0.018 in (0.46 mm) nylon-coated stainless, 49-strand (7 × 7), 26 lb (115 N) break, 30 ft | **Beadalon JW11T-0** (Amazon B001145A5E) | Amazon / Beadaholique ($30.99 list) | 1 | 21.99 | 21.99 | [est] ($14.51–30.99 seen) | §6 |
| 1.5 | Crimp tubes #2 (ID ≈ 1.3, OD ≈ 2.0, L ≈ 1.8 mm; for 0.013–0.024 in wire) | **Beadalon #2**, Amazon B002O0DAGU (≈ 46 pc) | Amazon | 1 | 7.59 | 7.59 | [est] | §6.2 |
| 1.6 | **Housing, option A (preferred, light):** close-wound 304V Bowden spring, OD 1.35, ID 0.74 mm, 5 × 1.65 m | **Motion Dynamics 304V, 0.012 in wire, 0.053 in OD, 0.029 in ID** | Chamfr | 1 bag | 87.70 | 87.70 | [cited] **out of stock** (CONFLICTS C3) | §6 |
| 1.7 | **Housing, option B (in stock):** 4 mm PTFE-lined shift housing, plus 4 mm end caps | **Shimano OT-SP41**, by the metre; Shimano/Jagwire 4 mm end caps | CyclErie / any bike shop | 6 m + 10 caps | 5.42/m | 32.52 + ≈ 5 | [est] | §6, DB03b |
| 1.8 | Ferrule for housing A: brass tube 3/32 in OD × 0.014 in wall (ID 1.68 mm), 12 in, 3-pack | **K&S Precision Metals 8126** (BR014-3-32) | ksmetals.com / hobby shop | 1 | 6.99 | 6.99 | [est] | §6.2 |
| 1.9 | Linear ball bearing, 4 × 8 × 12 mm, 4-pack | **LM4UU**, Kozelo B0C9MR96V3 | Amazon | 1 | 12.99 | 12.99 | [est] | DB03 |
| 1.10 | Hardened rod Ø 4 × 100 mm, 2-pack | uxcell B0FKGHMMP6 | Amazon | 1 | ≈ 8 | 8 | [verify] | DB02 |
| 1.11 | Compression spring 0.5 mm wire × 5.5 OD × 42 mm (ID ≈ 4.5; ≈ 0.3 N/mm), 20 pc. Two are used on the rods: 4.5 N total at the W tick. | **uxcell B00R1ISK8I** | Amazon | 1 | ≈ 7 | 7 | [verify] | §5.3 |
| 1.12 | Index Hall switch, unipolar digital, TO-92 | **TI DRV5023AJQLPG** | Mouser 595-DRV5023AJQLPG / DigiKey | 4 | 0.55 | 2.20 | [est] | DB02 |
| 1.13 | (E) Tension Hall, linear, TO-92: RA (−11 mV/mT) for a 2.5 mm gap; VA (−90 mV/mT) for a 6.5 mm gap A/B | **TI DRV5053RAQLPG** ×4, **DRV5053VAQLPG** ×3 | Mouser / DigiKey | 7 | 0.78 / 1.22 | 6.78 | [est] | DB04 |
| 1.14 | Index and flexure magnets, N52 1/8 × 1/16 in (3.18 × 1.59 mm), 10-pack | **K&J Magnetics D21B-N52** | kjmagnetics.com | 2 | 1.68 | 3.36 | [est] | DB01, DB03 |
| 1.15 | Rubber anti-vibration mounts M4, 10 × 10 mm (module isolators) | M4 double-stud or stud/female isolator 10 × 10 | Amazon / Walmart (824886475 is $7.89 for 2) | 6 | ≈ 1–4 | ≈ 12 | [est] | §4 |
| 1.16 | Calibration pulley bearing 623ZZ (3 × 10 × 4) + 50 US nickels (5.000 g each) | generic 623ZZ 10-pack | Amazon | 1 | ≈ 6 | 6 + 2.50 | [verify] | §6.3 |
| | **Subtotal, option A housing** (spring tube) | | | | | **≈ 215** | | |
| | **Subtotal, option B housing** (SP41) | | | | | **≈ 165** | | |

**S0 note.** The spec's S0 tendon ink rig buys items 1.1, 1.4, 1.5, 1.6 *and* 1.7 (it is an A/B of the two housings), plus printed drums. At ≈ $45 the leap4-D estimate was low. The honest figure is **≈ $120 without option A, ≈ $210 with it**. If Chamfr cannot restock, run the A/B as SP41 against a 1/16 in ID PTFE tube in SP41. Everything here is reused at A3.

## 2. Pneumatics: Cart 2 (Stage A1–A2)

| # | Item | Part number / SKU | Vendor | Qty | Unit $ | Line $ | Tag | Ref |
|---|---|---|---|---|---|---|---|---|
| 2.1 | P1 rail pump and P3 palm pump: 12 V brushed diaphragm, **50 kPa max**, 1 L/min, 1.5 W | **BODENFLO BD-02A-1L** (alt: Saim 12 V 350 mmHg, Amazon B0716V496V 2-pack) | bodenpumpstore.com / Amazon | 2 | ≈ 18 | 36 | spec [cited], price [verify] | §3, C9 |
| 2.2 | PIN A and PIN B valve: 3-port NC, 12 V 0.5 W, barbs for 1/8 × 2 mm tube | **SMC S070C-6DC-32** | automationdistribution.com (factory stock 1,723) | 2 (1 already in S0) | 35.00 | 35.00 | [cited] | §3 |
| 2.3 | PALM valve: 2-position 3-way, 12 V 0.2 A, 2-pack, **max 350 mmHg (47 kPa)** | **uxcell B07XCV799G** | Amazon | 1 | ≈ 14 | 14 | [verify] | §3 |
| 2.4 | RAIL DUMP and PALM DUMP: 2-way **normally open**, 12 V 45 mA, 3 mm port | **uxcell B07X9RD6BW** (alt CJV13-A06A1, B0D5H8T2B3) | Amazon | 2 | ≈ 8 | 16 | [verify] | §3 |
| 2.5 | R1a and R2 relief: compact nylon, **fixed 3 psi (20.7 kPa)**, about 10 % over set at full flow | **McMaster-Carr 4277T51** (thread [VERIFY 1/8 NPT]) | mcmaster.com | 2 (+1 interim) | ≈ 9 | 27 | [verify] page would not load | §3, §4 |
| 2.6 | R1b and R2b relief, **different make**, preset 3.5 psi (24 kPa) | **Generant VRV**, 1/8 MNPT, factory preset 3.5 psi, Buna (alt: Smart Products 300-series relief) | generant.com: **request a quote** | 2 | ≈ 30 | 60 | [verify] (CONFLICTS C8) | §3, §4 |
| 2.7 | Relief adapter: push-in 4 mm × **1/8 NPT female**, 2-pack | uxcell a19090300ux0812 (Amazon B07Z2V59YY) | Amazon | 2 | ≈ 12 | 24 | [est] | §3 |
| 2.8 | Pressure sensor 0–40 kPa gauge, analog (S_rail, S_A, S_B, S_palm) | **CFSensor XGZP6847A040KPGPN** (check positive-only range); AliExpress modules $1–3 | DigiKey | 4 (+1) | 6.00 | 30 | [est] | §3 |
| 2.9 | 10 µm (rated 5 µm) inline filter, 4 mm push-in. P1 and P3 outlets. | **SMC ZFC050-04B** (legacy; ask SMC for the successor) | smcpneumatics.com | 2 | 8.81 | 17.62 | [est] | §3 |
| 2.10 | Push-fit male connector Ø 3.2 (1/8 in) × M5: bulkhead and plug ports | **SMC KQ2H23-M5A** | smcpneumatics.com | 6 | 2.93 | 17.58 | [est] | DB06/07 |
| 2.11 | Plug-in reducer 4 mm stem → Ø 3.2 tube | **SMC KQ2R23-04A** | smcpneumatics.com | 4 | ≈ 3 | 12 | [verify] | §3 |
| 2.12 | Union tee Ø 3.2 (line A/B sensor tees + capped pad-2 tees) and blanking plug Ø 3.2 | **SMC KQ2T23-00A**, **KQ2P-23** | smcpneumatics.com | 5 + 2 | ≈ 4 / 1.5 | 23 | [verify] | §3 |
| 2.13 | 4 mm push-fit 1-in-4-out manifold, 6-pack | VIILOCK PK-4 (Amazon B0F19D11PT) | Amazon | 1 | ≈ 10 | 10 | [verify] | §3 |
| 2.14 | 4 mm push-fit union tee, 10-pack | Metalwork 4 mm tee (Amazon B07C6RC7RS) | Amazon | 1 | ≈ 9 | 9 | [verify] | §3 |
| 2.15 | 4 mm push-fit bulkhead union (accumulator caps), 5-pack | generic PM-4 bulkhead union | Amazon | 1 | ≈ 8 | 8 | [verify] | §3 |
| 2.16 | PU tube 1/8 in OD × 0.080 in (2.03 mm) ID, 20 m: in-box 1/8 runs and the umbilical | **SMC TIUB01B-20** (yellow $5.45 at MROSupply) | smcpneumatics.com | 1 | 9.20 | 9.20 | [est] | §3, §7 |
| 2.17 | PU tube 4 × 2.5 mm, 20 m | **SMC TU0425B-20** | smcpneumatics.com | 1 | 14.20 | 14.20 | [est] | §3 |
| 2.18 | Silicone tube 2 mm ID × 4 mm OD, 1 m (sensor and valve-barb jumpers) | generic | Amazon | 1 | ≈ 7 | 7 | [verify] | §3 |
| 2.19 | Blunt Luer-lock dispensing needles, 14–27G assortment (25G line-B inlet, 23G A/B, 27G palm bleed and deadhead bleeds) | Amazon **B077WSLCHJ** | Amazon | 1 | ≈ 10 | 10 | [verify] | §3 |
| 2.20 | Male Luer-lock to 3/32 in barb (feeds the needle hubs) | Nordson Medical **MTLL220-1** class, or Qosina equivalent in small packs | Qosina / Nordson | 4 | ≈ 1 | ≈ 8 incl. small-pack premium | [verify] | §3 |
| 2.21 | Accumulators: 250 ml PET bottle (Ø 50 × 175), 12-pack; 30 ml HDPE bottle, 6-pack | Amazon **B07BNWZGTM**; **ALINK B01KA4EEY8** | Amazon | 1 + 1 | ≈ 12 / 7 | 19 | [verify] | §3 |
| 2.22 | Sorbothane sheet 1/8 in, 60 duro, 6 × 6 in or 12 × 12 in (pump pads, valve-rack pad) | Amazon B09FVHS3FN (Thorlabs 12 × 12, 70 duro, $33.99) | Amazon | 1 | ≈ 15 | 15 | [est] | §8 |
| 2.23 | Metric O-ring kit, NBR70, including 3 × 1 mm (plug face seals) | generic metric kit | Amazon | 1 | ≈ 10 | 10 | [verify] | DB07 |
| 2.24 | Test gauge 0–15 psi (0–100 kPa), 40 mm dial, 1/8 NPT back (deadhead check, independent of electronics) | generic | Amazon | 1 | ≈ 10 | 10 | [verify] | §4 |
| | **Subtotal pneumatics** (one S070 is already in S0) | | | | | **≈ 455** | | |

**Spec comparison.** SYSTEM-SPEC-v3 §13 budgeted $282. This cart is ≈ $455 because of:
- the diverse reliefs ($60 against $30);
- full-price SMC fittings;
- a fifth sensor and a test gauge.

**Lean option (−≈ $90):**
- AliExpress XGZP modules (−$22);
- generic Ø 3 mm push-fits instead of SMC Ø 3.2 (≈ −$30; check the grip on 3.18 mm tube);
- skip the dial gauge and read P1 deadhead with a spare XGZP6847A100KPG (−$5);
- skip the 5th sensor (−$6).

## 3. Case fit-out and mounts: Cart 2 (Stage A5)

| # | Item | Part number / SKU | Vendor | Qty | Unit $ | Line $ | Tag | Ref |
|---|---|---|---|---|---|---|---|---|
| 3.1 | Case, IP65, inside 302 × 229 × 135 mm (base ≈ 95, lid ≈ 30 [est]) | **Harbor Freight Apache 2800, SKU 64551** | Harbor Freight (store pickup: Naples FL) | 1 | 29.99 | 29.99 | [cited] | §2 |
| 3.2 | 6 mm (1/4 in) Baltic birch, 12 × 24 in: tray, M8P panel, electronics shelf (3 mm optional) | Woodpeckers, Amazon B01MSWYF8N (box) | Amazon / woodpeckerscrafts.com | 1 box of 3 | ≈ 14 | 14 | [est] | §2 |
| 3.3 | Sorbothane hemisphere feet, 1/2 in, adhesive, 4-pack | **Isolate It!** 0.5 in hemisphere | isolateit.com | 1 | 8.95 | 8.95 | [est] | DB-feet |
| 3.4 | Cam-buckle strap 1.5 in × 1.2 m (chair-back strap) | **Strapworks CS112L** | strapworks.com | 1 | 9.10 | 9.10 | [est] | DB09 |
| 3.5 | Closed-cell EVA foam sheet 3 mm (lid and wall lining) | generic craft EVA, 12 × 18 in | craft store | 1 | ≈ 5 | 5 | [verify] | §8 |
| 3.6 | Dowel pin Ø 3 × 12 mm stainless, pack | generic | Amazon | 1 | ≈ 7 | 7 | [verify] | DB06 |
| 3.7 | M4 × 30 knurled thumb screw (plug) | generic stainless | Amazon | 2 | ≈ 3 | 6 | [verify] | DB07 |
| 3.8 | Optional toggle latch 304 SS, 40 × 50 mm, 40 kg, 2-pack | HJGarden B09FXX532Z | Amazon | (1) | ≈ 9 | (9) | [verify] | C11 |
| 3.9 | M5 × 20 pan head + M5 fender washers + nyloc (lid hook plate) | from the kit plus a fender-washer bag | hardware store | 4 sets | — | ≈ 4 | [est] | DB09 |
| | **Subtotal case** | | | | | **≈ 84** | | |

## 4. Umbilical and hanger: Cart 3 (Stage B)

| # | Item | Part number / SKU | Vendor | Qty | Unit $ | Line $ | Tag | Ref |
|---|---|---|---|---|---|---|---|---|
| 4.1 | 4-core 26 AWG unshielded cable (loop out, return, 2 spare) | **Alpha Wire 78014** (by the foot); alt Alpha 1604 | DigiKey | 7 ft | ≈ 1/ft | 7 | [verify] OD ≤ 3.5 mm | §7 |
| 4.2 | GX12 4-pin aviation connector, panel female + cable male, 2 sets | Hxchen, Amazon **B07V554X78** | Amazon | 1 | 7.89 | 7.89 | [est] | §7 |
| 4.3 | Knit sleeve: synthetic tubular stockinette 1 in × 25 yd | **3M MS01** | Walmart / GL Medical | 1 | ≈ 15 | 15 | [est] | §7 |
| 4.4 | Gooseneck with C-clamp and 1/4-20 tip, ≈ 64 cm | AceTaken **B082HQJ1JX** | Amazon | 1 | ≈ 20 | 20 | [verify] | §7.4 |
| 4.5 | Magnet Ø 6 × 3 N52, 30-pack (clip seat) | Amazon B0CD88KWDZ | Amazon | 1 | ≈ 8 | 8 | [verify] | DB15 |
| 4.6 | M6 flat steel washer (clip armature, OD 12 × 1.6) + 1/4-20 hex nut | hardware store | — | 2 + 1 | — | 1 | [est] | DB15/16 |
| 4.7 | Heat-shrink assortment (housing-end and cable-end strain relief) | generic | Amazon | 1 | ≈ 8 | 8 | [verify] | §7 |
| | **Subtotal umbilical and hanger** (tubes and housings are in sections 1–2) | | | | | **≈ 67** | | |

## 5. Printing

| # | Item | Qty | $ | Tag |
|---|---|---|---|---|
| 5.1 | **JLC3DP SLA (9600 resin):** DB01 ×4 (≈ 22 cm³), DB06 bulkhead (108 cm³), DB07 plug (81 cm³) | 1 order | ≈ 30–45 + DHL ≈ 20 | [est] (SLA "from $0.30"; price on upload) |
| 5.2 | **PETG (home printer):** everything else. ≈ 460 cm³ solid, so ≈ 330 g at 4 perimeters and 30–40 % gyroid. | ≈ 0.35 kg | ≈ 8 of a $20 spool | [est] |
| 5.3 | *Alternative if no printer:* JLC3DP **MJF PA12** for the PETG list | 1 order | ≈ 110–150 + DHL | [est] (MJF "from $1"; ±0.3 mm) |

## 6. Fasteners and consumables

| # | Item | Part number | $ | Tag |
|---|---|---|---|---|
| 6.1 | Brass heat-set inserts M3 × 5.7 (Ø 4.0 hole), 100 pc | ruthex RX-M3x5.7, Amazon B08BCRZZS3 | ≈ 12 | [verify] |
| 6.2 | M3/M4/M5 304 SHCS assortment with nuts and washers, 510 pc | Glarks B08HHZHXTP | ≈ 15 | [verify] |
| 6.3 | M3 nylon or brass standoffs M3 × 10 and M3 × 35 kit | generic | ≈ 10 | [verify] |
| 6.4 | Epoxy (5-minute + slow 2-part), CA glue, thread-locker blue | hardware store | ≈ 20 | [est] |
| | **Subtotal** | | **≈ 57** | |

## 7. Tools this package needs (beyond the ≈ $185 RT3 kit)

| Tool | Why | $ | Tag |
|---|---|---|---|
| Beadalon Standard Crimper JTCRIMP1 | #2 crimp tubes on the tendons | 12.49–14.49 | [est] |
| M3 and M5 taps + tap wrench | tapping the SLA bulkhead and plug | ≈ 12 | [verify] |
| Step drill bit 4–20 mm + 25 mm hole saw | case wall holes (GX12, DC jack, vents) | ≈ 15 | [verify] |
| Jigsaw or coping saw, files | the 73 × 39 mm wall window and the plywood | likely owned | — |
| Luggage scale (0–10 kg) | box weight, cable stall pull, 3 N clip release | ≈ 10 | [verify] |
| Kitchen scale 0.1 g | nickels, magnet checks | likely owned | — |

## 8. Roll-up

| Section | $ (option A housing) | $ (option B housing) |
|---|---|---|
| 1 Drum module | 215 | 165 |
| 2 Pneumatics | 455 | 455 |
| 3 Case fit-out | 84 | 84 |
| 4 Umbilical and hanger | 67 | 67 |
| 5 Printing (SLA order + PETG) | ≈ 70 | ≈ 70 |
| 6 Fasteners and consumables | 57 | 57 |
| **DRIVE BOX total** | **≈ $950** | **≈ $900** |

**Against §13.** The spec's comparable lines (puppet master $102 + pneumatics $282 + box $65 + umbilical/hanger $35, plus a share of printing and fasteners) total ≈ $600. **This package is ≈ $300 over.** The difference:
- diverse reliefs and full-price SMC fittings (+≈ 150);
- the real housing price (+≈ 50–100);
- a realistic fasteners line;
- the tension-sense parts.

**Lean path (≈ −$140).** Not recommended before Stage B:
- the lean pneumatics option (−90);
- drop the optional toggle latches, the dial gauge and the 5th sensor;
- reuse case foam for the baffles.

**Staged cash for this WP.**
- S0 rig: ≈ $120–210.
- Cart 2: ≈ $560, of which ≈ $60 waits on the Generant quote.
- Cart 3: ≈ $70.
- Printing is spread across the stages.

### Sources (checked 2026-10-02)

- Harbor Freight Apache 2800, $29.99, inside 11-7/8 × 9 × 5-5/16 in, 3.96 lb shipping weight: https://www.harborfreight.com/2800-weatherproof-protective-case-medium-black-64551.html
- Apache 2800 "5 pound" user report: https://mavicpilots.com/threads/10-pound-of-stuffing-in-my-5-pound-apache-2800-flight-case.121238/
- 17HS08-1004S (16 N·cm, 21.5 mm body, shaft 20 mm, D-cut 16.5): https://www.stepperonline.ca/nema-17-bipolar-1-8deg-16ncm-22-6oz-in-1a-3-7v-42x42x20mm-4-wires-17hs08-1004s.html
- SMC S070C-6DC-32 $35.00, stock 1,723: https://automationdistribution.com/s070c-6dc-32/
- BODENFLO BD-02A (50 kPa, 1 L/min): https://www.bodenpump.com/product/bd-02a-bd-02v-brush-motor-micro-air-vacuum-pumps/
- Beadalon 49-strand 0.018 in: https://www.beadaholique.com/products/beadalon-wire-standard-bright-49-strand-018-inch-30ft
- Motion Dynamics 304V Bowden spring (Chamfr): https://chamfr.com (search "304V stainless steel medical bowden cable spring 0.053 OD")
- Shimano SP41 housing: https://store.cyclerie.net/products/shimano-sp41-derailleur-housing
- K&S brass tube 3/32: https://ksmetals.com/products/br014-3-32
- K&J D21B-N52: https://www.kjmagnetics.com/d21b-n52-neodymium-disc-magnet
- SMC KQ2H23-M5A: https://www.smcpneumatics.com/KQ2H23-M5A.html ; TIUB01B-20: https://www.smcpneumatics.com/TIUB01B-20.html ; ZFC050-04B: https://www.smcpneumatics.com/ZFC050-04B.html
- XGZP6847A040KPGPN: https://www.digikey.com/en/products/detail/cfsensor/XGZP6847A040KPGPN/22530817
- Generant relief valves: https://www.generant.com ; Smart Products: https://www.smartproducts.com
- McMaster nylon relief valves (4277T51): https://www.mcmaster.com/4277T51
- Isolate It! hemispheres: https://isolateit.com/collections/hemispheres-bumpers ; Strapworks CS112L: https://www.strapworks.com/Metal_Cam_Straps_p/cs112l.htm
- Alpha Wire 78014: https://www.digikey.com/en/products/detail/alpha-wire/78014-SL199/4989207
- JLC3DP design guideline and tolerances: https://jlc3dp.com/help/article/3d-printing-design-guideline
- BTT Manta M8P V2.0 (170 × 102.7 mm): https://global.bttwiki.com/M8P-V2_0.html
