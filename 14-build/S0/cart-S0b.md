# Cart S0b: "Will the machine work?" (tendon ink rig, three steppers, Klipper streaming test)

**Project SCRATCH · 14-build/S0 · S0 kit engineer · prices checked 2026-10-02 · ship to Naples, FL 34102**

**Buy only after S0a is GO.** That means the scratch felt good, or the hand-rake felt good and the dish geometry goes back to the Director (see `S0-guide.md` §8).

Every part was chosen so that it is a **Stage A part bought early**, wherever that was possible. The "Carries forward" column says which Stage A item each one becomes.

**Price tags.** [cited] = price seen today on the vendor page, a store feed or the live Amazon page. [est] = estimate. [verify] = check before ordering.

## Totals

| Block | $ |
|---|---|
| A. Controller, drivers, power, motors (all Stage A parts) | **≈ $271** (≈ $262 if you own a mains cord) |
| B. Puppet drive: cable, crimps, housing, series springs (all Stage A parts) | **≈ $108** |
| C. Tools and rig-only items | **≈ $57** |
| **Parts total** | **≈ $436** (≈ $427 with your own mains cord) |
| of which carries forward into Stage A | **≈ $416 (≈ 95 %)** |
| Shipping: McMaster ground [verify], ≈ $8; BIQU [verify] | ≈ $10–20 |
| Printing (T01–T06; see `cad/README.md`) | own printer ≈ $3; service ≈ $25–40 [est] |

**Why the total is above the spec's $420 Day-0 figure (which also covered S0a).**
- About $50 is tools the spec puts in a separate $185 tool budget: logic analyser, test hooks, crimper, LED kit.
- About $20 is a second cable spool. One 5 m spool is too short for three 1.6 m tendons plus their terminations.
- Stage A's Cart 2 (≈ $520 in the spec) shrinks by the ≈ $416 bought here.

**Lean alternative: ≈ $155 less now.**
- Swap A1 and A3 (M8P + CB1, heatsink) for a **Raspberry Pi Pico ($3.95** [cited], PiShop SKU 1432), keep the 4 × TMC2209 on a breadboard, and run Klipper's host in a Linux VM on the Mac.
- It proves the same V-K1 timing.
- The cost: the Pico and the VM set-up are thrown away, and the M8P is bought at Stage A anyway.
- Recommended only if cash is tight this month.

## A. Controller and power

| # | Item | Vendor / listing | Qty | Price | Tag | Carries forward |
|---|---|---|---|---|---|---|
| A1 | **BTT Manta M8P V2.0 + CB1** (CB1 1 GB, boots from microSD; **no drivers, no heatsink** in this bundle) | BIQU, ["CB1+Manta M8P V2.0"](https://biqu.equipment/products/manta-m4p-m8p), SKU 1020000442 + 1020000405 | 1 | **$154.59** | [cited, BIQU store feed] | **Stage A controller** (spec C19). Same board, same config file (`klipper/printer.cfg`). |
| A2 | BTT **TMC2209 V1.3** stepper driver, 4-pack (3 + 1 spare) | BIQU, [btt-tmc2209-stepper-driver](https://biqu.equipment/products/btt-tmc2209-stepper-driver), SKU 1040000053 | 4 | **$26.43** (4 for) | [cited] | **Stage A drivers**, spec C20, "TMC2209 × 4" |
| A3 | CB1 heatsink | BIQU, SKU 1060000589 | 1 | **$5.90** | [cited] | Stage A |
| A4 | **Mean Well GST60A24-P1J**: 24 V 2.5 A 60 W desktop adapter (UL/CE), 5.5 × 2.1 plug | Amazon, [B013ETZUS0](https://www.amazon.com/dp/B013ETZUS0) | 1 | **$21.99** | [cited] | **Stage A supply E1** (spec C21) |
| A5 | IEC C13 mains cord for A4. **Skip if you have a spare PC or monitor cord.** | Amazon, StarTech PXT101, [B000067SLV](https://www.amazon.com/dp/B000067SLV) | 1 | $8.83 | [cited] | Stage A |
| A6 | 5.5 × 2.1 mm female barrel-jack pigtail, 2-pack | Amazon, JacobsParts, [B00QJAW9F4](https://www.amazon.com/dp/B00QJAW9F4) | 1 | **$4.99** | [cited] | Stage A (box panel jack E1) |
| A7 | microSD 32 GB for the CB1 | Amazon, Patriot LX 32 GB, [B08KSSXKYR](https://www.amazon.com/dp/B08KSSXKYR) | 1 | **$12.29** | [cited] | Stage A |
| A8 | **StepperOnline 17HS08-1004S** NEMA 17 pancake stepper (42 × 42 × 20 mm, 1.0 A; current listing says 16 N·cm) | Amazon, STEPPERONLINE store, [B00PNEQ79Q](https://www.amazon.com/dp/B00PNEQ79Q) | 3 | **$35.97** ($11.99 ea) | [cited] | **Stage A drum motors** (spec C14) |
| | **Subtotal A** | | | **≈ $271 (≈ $262 without A5)** | | |

Notes on A1 and A8, from the BTT GitHub V2.0 manual:
- The M8P V2.0 motor outputs are 4-pin 2.54 mm headers.
- Standalone STEP/DIR is set with the MS jumpers.
- The driver supply is 24 V, or 24–60 V on HV.

**The stepper's lead and connector type are [verify].** It ships with either bare leads or a detachable cable. Plan on 4-pin 2.54 mm female ends. The Dupont jumpers in C3 can bridge them.

You can buy the 8-driver bundle (M8P + CB1 + 8 × TMC2209, **$188.85** [cited]) instead of A1 + A2. It costs $7.83 more and gives 4 extra spare drivers.

## B. Puppet drive (tendon ink rig)

| # | Item | Vendor / listing | Qty | Price | Tag | Carries forward |
|---|---|---|---|---|---|---|
| B1 | **AFW Surflon Micro Supreme 7×7**, nylon-coated stainless, **0.018 in (0.46 mm)**, 26 lb, 5 m spool (AFW DM49-26-A) | Amazon, [B003NB2EQ6](https://www.amazon.com/dp/B003NB2EQ6) (5 m / 26 lb variant) | **2** | **$40.98** ($20.49 ea) | [cited] | **Stage A tendons** (spec T1: 0.45 mm coated 7×7); spool 2 = consumable spares (spec: replace at 50 sessions) |
| B2 | Mini double-barrel copper crimp sleeves, 1.0 mm ID, 100 pcs | Amazon, Hi-Seas, [B000ALE5FK](https://www.amazon.com/dp/B000ALE5FK) | 1 | **$9.49** | [cited] | Stage A terminations |
| B3 | Crimping tool for small sleeves | Amazon, iCrimp swager, [B00NJH8QXO](https://www.amazon.com/dp/B00NJH8QXO) | 1 | **$14.59** | [cited] | tool, Stage A |
| B4 | **Housing A**: 4 mm bicycle shift housing with slick liner, 10 m roll (enough for 3 × 1.6 m plus spares) | Tree Fort Bikes, [Jagwire 4 mm housing, 10 m roll](https://www.treefortbikes.com/Jagwire-4mm-L3-Derailleur-Housing-10-Yard-Roll) | 1 | ≈ $30.99 | [est] | **Stage A fallback housing** if the thin coil fails |
| B5 | Extension springs, 3/16 in OD, 0.70 in long, **9.43 lbf/in = 1.65 N/mm**, max 11.7 N, 12-pack. These are the series springs (spec C16 asks for 2 N/mm). | McMaster-Carr, [9654K959](https://www.mcmaster.com/9654K959) | 1 | **$12.30** | [cited] | **Stage A series springs** (spec §4.4) |
| B6 | Optional **housing B** (the thin housing A/B): stainless "sheath spring" 2.0 mm OD, 5 × 1 m; plus PTFE tube 0.8 ID × 1.6 OD, 1.5 m, as a liner if it fits | Amazon, [B0C85SCR7T](https://www.amazon.com/dp/B0C85SCR7T) (0.2 × 2 mm variant) + [B0BGXZL9MS](https://www.amazon.com/dp/B0BGXZL9MS) | 1 + 1 | $13.00 + $5.49 | [cited] | Stage A candidate for the spec's 1.2/0.6 coil. Only 1 m lengths: see guide test T6. |
| | **Subtotal B (without B6)** | | | **≈ $108** | | |

## C. Rig-only items and tools

| # | Item | Vendor / listing | Qty | Price | Tag | Carries forward |
|---|---|---|---|---|---|---|
| C1 | USB logic analyser, 24 MHz 8-channel (works with free PulseView) | Amazon, HiLetgo, [B077LSG5P2](https://www.amazon.com/dp/B077LSG5P2) | 1 | **$12.69** | [cited] | **tool for Stage A0** (safety-loop timing, spec A0) |
| C2 | 5 mm LED + resistor assortment (need 1 LED + one 330 Ω; the LED runs from a 3.3 V GPIO, not a 24 V fan output) | Amazon, [B07YWNHZHS](https://www.amazon.com/dp/B07YWNHZHS) | 1 | **$12.99** | [cited] | Stage A status LEDs |
| C3 | Female–female Dupont jumpers, 40 pcs, 20 cm | Amazon, [B0BRTJQGS6](https://www.amazon.com/dp/B0BRTJQGS6) | 1 | **$3.99** | [cited] | Stage A bench wiring |
| C3b | Test-hook clips for the logic analyser ("mini grabber" probes, 10 pcs), to clip onto a driver's DIR pin | Amazon, search "logic analyzer test hook clip" | 1 | ≈ $7 | [est] | tool, Stage A0 |
| C4 | Glass marbles about 16 mm, small bag (need 3). Skip if you have marbles. | Amazon, [B0DC53KT32](https://www.amazon.com/dp/B0DC53KT32) | 1 | $6.29 | [cited] | rig only |
| C5 | 1/4 in sanded plywood, 2 × 2 ft (the rig base) | Home Depot, ProWood model 109114 (in stock at South Cape Coral) | 1 | **$8.61** | [cited] | rig only |
| C6 | #6 × 1/2 in wood screws (about 20) + foam earplugs | Home Depot / household | — | ≈ $5 | [est] | — |
| — | Household: a felt-tip pen that fits a 12 mm hole (wrap tape to fit), printer paper, masking tape, phone with 240 fps slow motion, a Mac or PC on the same Wi-Fi | — | — | $0 | — | — |
| | **Subtotal C** | | | **≈ $57** | | |

Grand total of A + B + C, with A5 and without B6: **≈ $436**.

## Where to order (fewest boxes)

| Order | Items | Approx. |
|---|---|---|
| BIQU (biqu.equipment) | A1, A2, A3 | $187 + shipping [verify]. BIQU ships from China or a US warehouse; allow 1–2 weeks. **Order this first.** |
| Amazon | A4–A8, B1–B3, B6 (optional), C1–C4 | ≈ $205 (free shipping) |
| McMaster-Carr | B5 | $12.30 + ground shipping ≈ $8 [verify] |
| Tree Fort Bikes (or a local bike shop: ask for 5 m of 4 mm shift housing + 6 ferrules) | B4 | ≈ $31 [est]; a Naples bike shop may sell it by the metre |
| Home Depot | C5, C6 | pickup |

## What carries forward into Stage A, and what does not

**Carries forward (≈ $416):**
- controller, drivers, heatsink, 24 V adapter, jack, microSD, 3 motors;
- coated cable, crimps, crimper, series springs, housings;
- logic analyser, LEDs, jumpers;
- the T01 drums (reprint in SLA for Stage A).

**Rig-only (≈ $20 + printing):** plywood, marbles, screws and earplugs, plus the printed motor tables, stop blocks, rig deck and pen plate.

**If S0b fails:**
- **Klipper fails:** fallback 1 (spec §8.2) runs on the same board.
- **The tendon fails:** the motors, controller and supply still drive the Stage A bench, with lines only, or with the revisited drive.

Nothing here is wasted in any S0b outcome short of abandoning SP1.
