# ELECTRONICS + FIRMWARE — parts list with live prices

**Package:** 14-build/electronics · **Prices checked:** 2026-10-02 · **Tags:** **[cited]** = price seen on the linked page that day · **[est]** = estimate (±25 %) · **[verify]** = check the exact part/price before ordering.
**Staging (SYSTEM-SPEC-v3 §10):** buy S0 now; buy Cart A only after S0 passes; Cart B only after A passes. Parts owned by other packages (steppers, pressure sensors, valves, pumps) are listed under "cross-references" with no price, so nothing is counted twice.

## S0 cart — Klipper bench test (V-K1, V-K2)

| # | Part | Exact spec / what to search | Qty | Unit $ | Line $ | Source | Tag |
|---|---|---|---|---|---|---|---|
| 1 | BTT Manta M8P **V2.0 + CB1** bundle | "BIGTREETECH Stealthy Hi-Speed Solution, option M8P V2.0+CB1" (CB1 = the Linux module that plugs into the board) | 1 | 154.59 | 154.59 | [biqu.equipment](https://biqu.equipment/products/bigtreetech-stealthy-hi-speed-solution) | [cited] — confirm in the cart whether TMC2209s are included [verify] |
| 2 | TMC2209 driver module | BIGTREETECH TMC2209 V1.3 (or V1.2); 3 for the drums + 1 spare | 4 | 7.89 | 31.56 | BIQU / Amazon (price from leap4-E, same day) | [cited] |
| 3 | 24 V power adapter | **Mean Well GST60A24-P1J** (24 V 2.5 A 60 W, UL, 2.1 mm plug, centre +) | 1 | 18.60 | 18.60 | [Jameco](https://www.jameco.com/z/GST60A24-P1J-MEAN-WELL-24-Volt-2500mA-60-Watt-3-Wire-Regulated-Switching-Desktop-Power-Adapter-2-1mm-Plug-Level-VI_2224411.html), DigiKey same price | [cited] |
| 4 | Panel DC jack | 5.5 × 2.1 mm panel-mount female, screw/solder lugs, ≥ 5 A | 1 | 2.00 | 2.00 | Amazon / DigiKey | [est] |
| 5 | microSD card for the CB1 | 32 GB, "A1"/"U3" class (SanDisk/Samsung) | 1 | 8.00 | 8.00 | any | [est] |
| 6 | Inline fuse holder + fuses | 5 × 20 mm holder, 18 AWG leads; **3.15 A slow-blow (T3.15A)** ×5 | 1 | 6.00 | 6.00 | Amazon | [est] |
| | | | | | **≈ 221** | | |

Steppers (3 × 17HS08-1004S) and their cables are in the DRIVE BOX / BOM S0 cart.

## Cart A — safety loop, sensing, controls (after S0 GO)

| # | Part | Exact spec / what to search | Qty | Unit $ | Line $ | Source | Tag |
|---|---|---|---|---|---|---|---|
| 7 | **K1 force-guided relay** | **Panasonic SFS2-DC24V** (2 Form A + 2 Form B, forcibly guided, 24 V coil 360 mW, 6 A, PCB pins) | 1 | 16.64 | 16.64 | DigiKey (1,143 in stock per search; LED version SFS2-L-DC24V is 18-week lead — do not order that one) | [cited] |
| 8 | Safety-board semiconductors | 74HC74 (DIP-14) ×1; LM393 (DIP-8) ×4; 2N7000 (TO-92) ×4; PC817 (DIP-4) ×8; 1N4007 ×2; 1N4746A (18 V zener) ×1; 1N4148 ×4; BAT54S ×2; SS14 ×10; SMAJ26A ×2 | 1 set | — | 9.00 | DigiKey / LCSC / Amazon kits | [est] |
| 9 | Safety-board passives | resistor kit (1/4 W: 100 Ω…1 MΩ); 470 µF 35 V ×2; 1 µF 50 V film ×2; 100 nF ×10; 1 nF ×2; **3296W 10 k multiturn trimpot ×8**; **4.7 Ω 5 W wire-wound ×1** | 1 set | — | 12.00 | Amazon / DigiKey | [est] |
| 10 | Perfboard + terminals | 7 × 9 cm double-sided perfboard ×2; 5.08 mm screw terminals (2-pin ×12); 2.54 mm headers; DIP sockets (8 ×4, 14 ×1) | 1 set | — | 9.00 | Amazon | [est] |
| 11 | 12 V buck converter | **XL4015 5 A** adjustable module (in 4–38 V, out 1.25–36 V), set to 12.0 V | 1 | 3.99 | 3.99 | [PartsBuilt](https://partsbuilt.com/buck-converter-xl4015-5a-dc-dc/) (Amazon multipacks ≈ $3/ea) | [cited] |
| 12 | E-stop puck | **22 mm red mushroom, latching (push-lock, twist-release), 2 × NC**, in a 1-hole box (e.g. mxuteuk HB2-ES544-BOX "2NC", TWTADE YW1B-V4E02R) | 1 | 14.00 | 14.00 | [Amazon mxuteuk 2NC](https://www.amazon.com/mxuteuk-Emergency-Button-Mushroom-Equipment/dp/B09T6MH44Y) | [verify] price; contact config 2NC [cited] |
| 13 | Aviation connectors | **GX12-4** male+female pairs ×2 (e-stop, helmet loop); **GX16-8** pair ×1 (hand controller) | — | — | 28.00 | [GX16-8 10-set $17.99](https://www.amazon.com/GX16-8-Aviation-Connector-aviation-connector/dp/B06XF62SYD); GX12-4 pack ≈ $10 | [cited] / [est] |
| 14 | Hold-to-run lever switch | **Omron V-15G2-1C25-K** (hinge lever, SPDT, Au-flash OK at 15 mA) under a printed paddle | 2 | 1.86 | 3.72 | DigiKey SW875-ND | [cited] |
| 15 | Knobs | 10 kΩ **linear (B10K)** 16 mm pots ×2 + knobs | 1 set | — | 5.00 | Amazon | [est] |
| 16 | MODE selector | **1P4T rotary switch** (1 pole 4 position, 1 deck) + knob; resistors 1 k, 3.3 k, 10 k, 33 k (1 %) | 1 | 7.00 | 7.00 | [uxcell 1P4T](https://www.amazon.com/uxcell-Position-Channel-Rotary-Selector/dp/B07JM3GWQ4) | [verify] |
| 17 | MOVED button | 12 mm momentary push button, NO | 1 | 1.00 | 1.00 | Amazon | [est] |
| 18 | Hand-controller cable | 8-core 24 AWG flexible cable, 2 m (or 8-core shielded control cable) | 1 | 8.00 | 8.00 | Amazon | [est] |
| 19 | E-stop cable | 4-core 20 AWG flexible cable, 2 m (carries the rail current through pole 2) | 1 | 6.00 | 6.00 | Amazon | [est] |
| 20 | Tension front-end MCU | **Raspberry Pi Pico (RP2040)**, Pico H if you do not want to solder headers ($5) | 1 | 4.00 | 4.00 | [Adafruit 4864](https://www.adafruit.com/product/4864) | [cited] |
| 21 | Tension Halls | **TI DRV5053EAQLPG** (analog bipolar, +45 mV/mT class, TO-92) ×3 + 1 spare | 4 | 1.16 | 4.64 | DigiKey | [cited] |
| 22 | Drum index Halls | A3144 / OH3144 unipolar switch (TO-92, open collector, 4.5–24 V) — pack of 10 | 1 | 6.00 | 6.00 | Amazon | [est] |
| 23 | Status ring | **Adafruit NeoPixel Ring 12 × 5050 RGB (1643)** | 1 | 9.50 | 9.50 | [Adafruit](https://www.adafruit.com/product/1643) / Jameco $11.85 | [cited] |
| 24 | Chime | 5 V active buzzer (continuous tone, 12 mm) | 1 | 1.00 | 1.00 | Amazon | [est] |
| 25 | Wire and terminations | silicone wire 18/20/22/26 AWG (red/black + colours), Wago 221-413 ×10, ferrules + crimper kit, heat-shrink | 1 set | — | 32.00 | Amazon | [est] |
| 26 | USB cable | USB-A to micro-USB, 0.3 m (Pico → M8P USB port) | 1 | 3.00 | 3.00 | any | [est] |
| | | | | | **≈ 203** | | |

## Cart B — helmet loop (after A GO)

| # | Part | Exact spec | Qty | Unit $ | Line $ | Source | Tag |
|---|---|---|---|---|---|---|---|
| 27 | Head-present switch | sub-miniature microswitch, NO, low force (e.g. Omron D2F-01L or ZF/Cherry DB2), ≥ 50 mA at 24 V | 2 | 2.00 | 4.00 | DigiKey / Amazon | [est] |
| 28 | Magnetic pogo lanyard | **2-pin spring-loaded magnetic pogo connector, male + female**, ≥ 1 A per pin | 1 pair | 6.99 | 6.99 | [eBay 1-pair](https://www.ebay.com/itm/166028342919) / Amazon 2-pair ≈ $12 | [cited] |
| | | | | | **≈ 11** | | |

The 4-core 26 AWG umbilical cable is in the DRIVE BOX umbilical build (SPEC §5.4: loop out, loop return, 2 spare).

## Tools this package needs (once)

| Tool | Why | $ | Tag |
|---|---|---|---|
| Digital multimeter (auto-range, continuity beep) | every bring-up step | 25 | [est] (RT3 tool list) |
| 8-channel 24 MHz USB logic analyser (Saleae-clone) + PulseView (free) | A0 gate: each loop element opens the rail ≤ 35 ms | 12 | [est] |
| Soldering iron 60 W temperature-controlled, solder, flux, solder sucker | safety board | (RT3 list) | — |
| Ceramic/plastic trimmer screwdriver | VREF and comparator trimpots | 4 | [est] |
| Phone with 240 fps slow-motion | S0 timing (LED vs pen mark) | — | — |

## Totals and comparison with SYSTEM-SPEC-v3 §13

| Cart | This package | Notes |
|---|---|---|
| S0 | ≈ $221 | M8P+CB1 bundle dominates; drivers may already be in the bundle (−$32) |
| A | ≈ $203 | |
| B | ≈ $11 | |
| **Total** | **≈ $435** (≈ $400 if the drivers come with the bundle) | spec §13 "Controller + electronics" = $340 |

The +$60–95 against the spec is wire/terminations ($32, the spec carried $20), the GX16 hand-controller connector set, the second lever switch, and the e-stop at a 2NC box price. Nothing here is optional for safety; the cheapest saving is ordering the semiconductors and passives from one distributor in one shipment (≈ −$8 shipping).

## Cross-references (bought by other packages; wired here)

| Part | Owner | Wiring in electronics.md |
|---|---|---|
| 3 × 17HS08-1004S pancake steppers | DRIVE BOX / BOM | Motor 1–3 sockets, §4 rows M1–M3 |
| 4 × XGZP6847A 0–40 kPa gauge, **3.3 V version (0.2–2.7 V out)** — e.g. XGZP6847A040KPG + 3.3 V option [verify exact order code with the seller] | DRIVE BOX | TH0–TH3, §4 rows S1–S4 |
| 2 × S070C-6DC-32, PALM 3-way, 2 × NO dumps (all 12 V) | DRIVE BOX | HE0–HE2, FAN0–FAN1 |
| P1 rail pump (12 V, any current ≤ 5 A), P3 palm pump (12 V, **≤ 0.8 A**) | DRIVE BOX | HE3, FAN3 |
| 4-core 26 AWG umbilical | DRIVE BOX | J4 helmet loop |
