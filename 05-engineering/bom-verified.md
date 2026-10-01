# SP1 Float-Arm: Bill of Materials, verified against live vendor pages

**Project SCRATCH · 05-engineering · 2026-10-01 · BOM verifier.** Every line of `bom.md` was checked against a live product page on 2026-10-01 (US, pre-tax). Prices are what the page showed that day; Amazon prices are the non-Prime one-time price unless marked "Prime". `bom.md` is unchanged; this file replaces its prices, part numbers and availability and keeps its row numbers, groups, stages and the three totals.

**Status codes.** **CONFIRMED** = the listed part exists at about the listed price and the spec matches. **CHANGED** = the part exists but the price, pack, part number or spec differs; the recommended purchase is given. **UNAVAILABLE** = the listed part does not exist or is out of stock; the best substitute is given. Rows marked *optional* in bom.md stay out of every total. "Hardware store" rows have no live page; they carry the bom.md estimate and an Amazon reference price where one was found.

**Headline.** Totals rise from **$1,413.99 to $1,703.84** (+20.5 %, shipping excluded). 103 lines changed, 4 unavailable, 34 confirmed (of 141 priced lines). Two parts are the schedule risk: the **XL330-M288-T is back-ordered 2 months at robotis.us** (buy from the ROBOTIS Korea store or accept the lead time), and the **McMaster 9654K spring in box 2A does not exist** at 3/8 in OD × 0.031 in × 2.5 in (a 5/16 in OD McMaster spring that meets the force window is pinned below). Six spec mismatches against mechanical.md / electronics-firmware.md are listed in §11; the XL330 cradle (P13) and the arcade-button deck hole (P39) must change before printing.

## 0. How to use this BOM

Stage codes, carts and gates are as in bom.md §0. The order groups now read:

| Order | When | What | Cash (USD, verified) |
|---|---|---|---|
| Cart A, Stage 0 | now (Day-0 list in §13) | every S0 row, the BK rows "buy with S0", the T rows "buy with S0" | **$374.90** (S0 $161.66 + BK $80.95 + T $132.29) |
| Cart B, Stage 1 | the day after GO; **place the ROBOTIS order first, the day the design is frozen, because of the 2-month XL330 lead time** | every S1 row by vendor (§12), the rest of BK, the rest of T | $928.75 (S1) + $228.39 (rest of BK) + $124.53 (rest of T) |
| Cart C, Stage 3 | only if Stage 2 earns it | second XL330 (recommend adding it to the Stage-1 ROBOTIS order), lazy-Susan ring, load cell | $47.27 |

Rows that can wait inside Stage 1 (bom.md §0.4) now total **$119.42** (2.02 $45.00, 2.06 $13.99, 2.28 $15.49, 2.31 $19.86, 5.04 $14.59, 5.09 $10.49). Lean first rig order: $1,090.41 − $119.42 = **$970.99**.

## 1. Totals by group and by stage

### 1.1 Group × stage (USD, optional rows excluded, shipping excluded)

| Group | S0 wand | S1 rig | S3 upgrades | BK bench kit | T tools | Total (verified) | bom.md total |
|---|---|---|---|---|---|---|---|
| 2 Structural and mechanical | $0.00 | $463.13 | $0.00 | $0.00 | $0.00 | **$463.13** | $359.42 |
| 3 Fasteners and inserts | $0.00 | $129.56 | $0.00 | $0.00 | $0.00 | **$129.56** | $110.00 |
| 4 Printing (filament) | $54.28 | $15.29 | $0.00 | $0.00 | $0.00 | **$69.57** | $79.00 |
| 5 Tips (tips.md §9) | $107.38 | $25.08 | $0.00 | $0.00 | $0.00 | **$132.46** | $98.00 |
| 6 Electronics | $0.00 | $295.69 | $47.27 | $0.00 | $0.00 | **$342.96** | $300.57 |
| 7 Bench and test kit | $0.00 | $0.00 | $0.00 | $309.34 | $0.00 | **$309.34** | $240.00 |
| 8 Tools (printer excluded) | $0.00 | $0.00 | $0.00 | $0.00 | $256.82 | **$256.82** | $227.00 |
| **Total** | **$161.66** | **$928.75** | **$47.27** | **$309.34** | **$256.82** | **$1,703.84** | $1,413.99 |

Optional rows (not in the table): 2.14 $10.00 [est], 2.16 $9.95, 2.29 $12.00 [est], 3.14 $3.00 [est], 6.05 $6.99, 6.11 $19.97, 7.24 $25.99, 8.19 $22.29, 8.20 $20.99 = $131.18. Shipping estimate for the vendors that charge it (§12): about **$48**. Grand total with shipping, without the printer: **$1,751.84** (bom.md: $1,446.99). A printer, if needed: Bambu Lab A1 $299 to $349 (256 mm bed, direct drive; confirmed in §8).

### 1.2 Where the +$289.85 comes from

| Cause | Δ (USD) | Rows |
|---|---|---|
| Sil-Poxy is $45 on Amazon ($31 to $35 at specialist shops), not $14 | +$31 | 2.25 |
| Feeler stock sells only as a box of 12 blades ($28.49), covering 2.21 and 5.06 | +$12 | 2.21, 5.06 |
| Bench kit items priced from live pages (wig $36, foam ball 2-pack $17, foam head $15, safety glasses $15, ruler $12, loupe $13) | +$69 | §7 |
| Electronics kits are bigger than estimated (Dupont kit $15, 6-core cable $20, splice-able X3P 10-pack $22) | +$42 | 6.18, 6.25, 6.29 |
| Mechanical consumables (PTFE film tape $24, bumpers $13, Stretch Magic $12, oil $10, Loctite $10) | +$36 | 2.12, 2.26, 2.27, 2.32, 2.33 |
| Tools: calipers $27, insert tips $18, solder+flux $19, stone $20, cutters/stripper/drivers $27 | +$30 | §8 |
| Savings: PETG $15.29/kg not $25, monitor arm bundle, bracket kit $8.99, luggage scale $5.79, mitre box $8.99, deburring kit $8.99 | −$55 | 4.01, 4.02, 2.04, 8.07, 8.12, 8.13 |

### 1.3 Against the DECISION and freeze targets

| Budget line | Target | Verified | Comment |
|---|---|---|---|
| Stage 0 wand | about $30 (freeze §3); about $39 cash (tips §9) | $161.66 S0 (+$80.95 BK, +$132.29 T bought with it) | Still dominated by whole spools ($54.28) and full packs; the wand's marginal cost is unchanged at about $40 |
| Rig (S0 + S1, no bench kit, no tools) | $250 to $300 | **$1,090.41**; lean $970.99 | The named major parts (arm $39.99, extrusion + brackets $34.98, rail $9.99, springs $13.19, bearings $16.88, magnets $8.97, brick $14.95, e-stop $15.99, button $9.99, OpenRB $28.64, XL330 $27.49, feeler stock $28.49, PETG $15.29) are **$264.84**, inside the target. The rest is packs, consumables, cradle, ballast and tips, as bom.md §1.2 explains |
| Stage 3 | +$27 to $45 | $47.27 | $2 over, from the lazy-Susan ring ($12.99) |
| Test gear | $45 to $70 (CL) | $309.34 | Two real-hair heads ($63.88), a Kanekalon wig ($35.99) and instruments are most of it |
| Tools | $150 to $190 | $256.82 | Calipers, insert tips, solder and the diamond stones are the overrun |

## 2. Structural and mechanical

| # | Item | Qty | Status | Verified product, URL, price, stock (2026-10-01) | Line (USD) | Stage |
|---|---|---|---|---|---|---|
| 2.01 | Monitor arm | 1 | **CHANGED** (price, tilt spec) | HUANUO Single Monitor Mount 13–32 in gas spring, VESA 75/100, **4.4–19.8 lb (2.0–9.0 kg)**, tilt **−50°/+30°**, swivel ±90°, rotation 360°, lift to 39.6 cm, C-clamp or grommet. https://www.amazon.com/dp/B0CTJYYSML — $39.99 Prime / $49.99 list (white; black variant $35.99 Prime), in stock, delivery Oct 6. Reach is not on the listing; HUANUO's standard single arm is quoted at 17.3 in (440 mm) max extension (search result), inside the 350–500 mm need. Minimum load 2.0 kg: **ballast (row 2.02) is required** with this arm, 1.1 kg per bom.md §2 | $39.99 | S1 |
| 2.02 | Ballast plates | 5 | **CHANGED** (minimum order) | SendCutSend, mild steel 0.119 in, upload a 100 × 100 mm square with 4 × Ø4.5 holes on 75 mm. https://sendcutsend.com/materials/laser-cut-steel/ — **minimum order is now $39** (bom.md cited $29), free 3–5 day shipping on most orders, min part 1 × 1.5 in. Price needs the upload; $45 for 5 plates (+ row 6.07 plate + row 2.20 discs) remains an estimate inside the $39 minimum | $45.00 [est] | S1, can wait |
| 2.03 | 2020 aluminium extrusion | 1 pack (4 × 500 mm) | **CHANGED** (price) | SeekLiny 4-pack 2020 T-slot 500 mm black. https://www.amazon.com/dp/B0DY7GX9YL — $25.99, in stock, delivery Oct 6 | $25.99 | S1 |
| 2.04 | 2020 corner bracket kit | 1 kit | **CHANGED** (part: the cited kit has sliding T-nuts and ships Oct 20–Nov 2) | The bom.md link (TOHIRA B0FF9ZBTZJ) is $27.99 for 40 sets / $15.99 for 20 sets, contains **sliding** (end-insert) T-nuts, and quotes delivery **Oct 20 – Nov 2**. Buy instead: CLAHJQX 20 sets 2020 corner bracket kit with **M5 drop-in T-nuts** and bolts, $8.99, 12 left, delivery Oct 3–6 (first result at https://www.amazon.com/s?k=2020+drop+in+t+nuts+M5+corner+bracket+kit). Covers 2 brackets and about 20 T-nuts; M5 × 12 screws from row 3.13 cover the 22 screws | $8.99 | S1 |
| 2.05 | MGN9 rail 100 mm with MGN9C block | 1 | **CHANGED** (price; hole pitch to measure) | uxcell MGN9 100 mm linear guide rail with MGN9C carriage block, black, $9.99, delivery Oct 8 (listing surfaced on https://www.amazon.com/dp/B0FM82NXTG "customers also viewed"; search "uxcell MGN9 100mm MGN9C"). HIWIN datasheet (https://hiwin.co.uk/wp-content/uploads/2017/05/CRD-Hiwin-Linear-guides-MG-series.pdf, table 2-4-13): MGN9C block W 20, L 28.9, **B 15 × C 10 mm, M3 × 3 mm deep**, H 10, H1 2, weight 0.016 kg; rail WR 9, HR 6.5, **P 20 mm, E 7.5 mm**, Ø6 counterbore 3.5 deep, Ø3.5 through, M3 × 8 bolts, 0.38 kg/m. **E = 7.5 does not divide a 100 mm rail evenly** (100 − 4 × 20 = 20 → generic 100 mm rails are usually drilled at 10/30/50/70/90, but some are 5/25/45/65/85/…): measure the first hole before printing P21 (see §11) | $9.99 | S1 |
| 2.06 | Spare MGN9C block | 1 | **CHANGED** (price) | ReliaBot MGN9C carriage block, shipped on a plastic retainer rail with 2 spare balls. https://www.amazon.com/dp/B0FM82NXTG (size MGN9C) — $13.99, delivery Oct 18 – Nov 4 (slow; fine for a spare) | $13.99 | S1, can wait |
| 2.07 | Hinge pin set | 1 set | **CHANGED** (price) | M6 × 80 socket head 304 SS, 20 pcs, https://www.amazon.com/dp/B0H38WY4PJ — $8.81 (DIN 912 M6 × 80 is partially threaded, 24 mm thread: check the listing photo). M6 nyloc from row 3.07. 2 nylon M6 washers: hardware store, about $1 [est] | $9.81 | S1 |
| 2.08 | 623ZZ bearings | 10 | **CONFIRMED** | uxcell 10 pcs 623ZZ 3 × 10 × 4, chrome steel ABEC3. https://www.amazon.com/dp/B0D54JLX1Z — $6.89, delivery Oct 3. (Avoid B0CVV2MSNX, $47.76 from an overseas seller) | $6.89 | S1 |
| 2.09 | 625-2RS bearing | 10 | **CHANGED** (price) | FUSHI 625-2RS 5 × 16 × 5, 10 pcs. https://www.amazon.com/dp/B0815B5D5W — $9.99, 6 left, delivery Oct 6 | $9.99 | S1 |
| 2.10 | Idler shoulder screw | 2 (+2) | **CHANGED** (part: stainless, Amazon) | 4 pcs 304 SS hex-socket shoulder bolt, 5 mm shoulder × 25 mm, M4 thread. https://www.amazon.com/dp/B0BVZD6YHP — $7.99, delivery Oct 3. (uxcell 5 pcs B077GXTHWN $9.99 ships Oct 13–23.) McMaster lists 24 products for shoulder 5 mm × 25 mm × M4 (alloy-steel 92981A series) but the pane shows no part numbers without a cart; stainless is fine for a 1 N·m idler | $7.99 | S1 |
| 2.11 | Dyneema cord | 1 spool | **CHANGED** (price; 350 lb line) | 9KM DWLIFE UHMWPE braided cord 1.0 mm, 100 ft, 350 lb. https://www.amazon.com/dp/B0BRXHX44X — $13.99, 8 left. Stronger than the 100 lb spec; same diameter | $13.99 | S1 |
| 2.12 | Trim cord | 1 roll | **CHANGED** (price) | Stretch Magic elastic cord (first result for "Stretch Magic 0.5mm"), https://www.amazon.com/dp/B004P9C5AK — $11.98. Confirm the 0.5 mm size on the variant selector | $11.98 | S1 |
| 2.13 | Hinge lift springs (box 2A) | 4 (pack of 12) | **CHANGED** (part number: box 2A's spring does not exist) | **McMaster-Carr 9654K123**, extension spring, spring steel, loop ends: **length 2.442 in, OD 0.313 in, wire 0.029 in, rate 0.64 lbf/in (0.112 N/mm), minimum load 0.44 lb (1.96 N), maximum load 2.61 lb (11.6 N), extended length at max load 5.86 in (149 mm), pack of 12, $13.19** (table read from https://www.mcmaster.com/products/extension-springs/od~0-313/ on 2026-10-01). McMaster has **no** 3/8 in OD × 0.031 in spring between 1.5 in and 4.438 in long (the 3/8 × 0.031 rows are 0.938/1.188/1.438/1.5 in at 1.2–3.1 lbf/in and 4.438/11 in at 0.27/0.10 lbf/in; the only 2.5 in 3/8 OD spring, 94135K691, is 0.97 lbf/in). Check against box 2A: rate inside 0.45–0.66 ✓; initial tension 1.96 N inside 1.0–2.0 ✓; free length 62 mm ≤ 64 ✓; max extension 149 mm ≥ 125 ✓; max load 11.6 N ≥ 10 ✓; 6.5 N at 62 + (6.5 − 1.96)/0.112 = **102.5 mm hook-to-hook** (≤ 117 ✓; tie the cord off 14.5 mm longer than the design figure); at the up-stop, 26.8 mm shorter, **3.5 N** (window 3.4–4.4 ✓, at the low edge). OD is 7.9 mm, not 9.5: the P1 spring channels get 1.6 mm of side slack (see §11, item 5). Bench test per mech §4.3 is still binding | $13.19 | S1 |
| 2.14 | Spring fallback assortment | 1 | not checked (optional) | bom.md estimate stands ($10 [est]); the Amazon search for 3/8 in OD springs returns Grainger "Ext Spring Utility 2-1/2 OAL 3/8 OD PK6" at $15.25 but it is 0.048 in wire, 5.59 lbf/in: unusable. Row 2.13 makes this row unnecessary | ($10.00) | optional |
| 2.15 | Holding electromagnet | 1 | **CHANGED** (price) | Adafruit 3872, 5 V electromagnet 2.5 kg (5.5 lb) holding, P20/15, 0.22 A at 5 V, Ø20 × 15 mm, centre Ø8 mm, 270 mm leads, 22.7 g. https://www.adafruit.com/product/3872 — **$7.50**, in stock. Spec matches mech §4.4 | $7.50 | S1 |
| 2.16 | Fallback electromagnet | 1 | **CHANGED** (price, optional) | Adafruit 3873, 5 kg P25/20, 0.3 A, Ø25 × 20 mm. https://www.adafruit.com/product/3873 — $9.95, in stock | ($9.95) | optional |
| 2.17 | Keeper plate stock | 1 bar | **CONFIRMED** (store item) | Hardware-store 1/8 × 1 in plain steel flat bar, about $8 [est]. Online fallback: 1018 steel bar 1/8 × 1 × 12 in https://www.amazon.com/dp/B000H9NB4G $29.85 (too dear; or add a 25 × 25 mm square to the SendCutSend order) | $8.00 [est] | S1 |
| 2.18 | PTFE thread-seal tape | 1 roll | **CHANGED** (price, 4-roll pack) | 4 rolls 1/2 in × 520 in PTFE tape, https://www.amazon.com/dp/B091913Z7F — $3.99 | $3.99 | S1 |
| 2.19 | Wrist magnet K&J D61 | 3 | **CONFIRMED** | K&J D61, 3/8 × 1/16 in N42 disc, **pull force 2.12 lb (9.4 N) on a steel plate**, 0.85 g, Ni-Cu-Ni, 80 °C. https://www.kjmagnetics.com/d61-neodymium-disc-magnet — $0.49 each, in stock, same-day shipping | $1.47 | S1 |
| 2.20 | Wrist keeper discs 12 × 1.5 mm | 2 | **UNAVAILABLE** (no mild-steel 12 × 1.5 disc listing; Amazon "12 mm x 1.5 mm" results are magnets) | Substitute 1: add 2 × Ø12 mm discs in 0.060 in (1.5 mm) mild steel to the SendCutSend ballast order (SendCutSend's minimum part is 1 × 1.5 in, so draw them as a 1 × 1.5 in tab with two Ø12 circles scored, or as a 25 × 40 mm plate and cut). Substitute 2 (bom.md's own): DIN 125 M6 washer 12 × 1.6 mm, lower pull, re-tune in L6 | $2.00 [est] | S1 |
| 2.21 | Feeler stock, rig leaves | 2 strips | **CHANGED** (sold as a box of 12 blades; covers row 5.06) | **Precision Brand 19425**, feeler gauge blades 0.012 × 1/2 × 12 in, C1095 spring steel, RC 48–62, **pack of 12**. Zoro https://www.zoro.com/precision-brand-feeler-gauge-00120x12-l-pk12-19425/i/G2048103/ — **$28.49** (Walmart $42.56, Amazon Precision Brand listings $36.97–39.58). One box = 4 strips for 2.21 + 5.06 plus 8 spares. McMaster blocks the page; the Precision Brand part is the same C1095 stock | $28.49 | S1 |
| 2.22 | M8 slug washers | 20 (pack of 25) | **CHANGED** (price) | M8 fender washers 8 × 24 mm, 25 pcs, https://www.amazon.com/dp/B08C34R45G — $8.61 (hardware-store singles at $0.30 remain cheaper) | $8.61 | S1 |
| 2.23 | Zero pin | 1 | **CONFIRMED** | No purchase (3.0 mm shank from row 5.16) | $0.00 | S1 |
| 2.24 | Silicone membrane sheet | 1 sheet | **CHANGED** (thickness 0.3 mm, not 0.25) | Transparent silicone film 500 × 500 mm, offered in 0.2 / 0.3 / 0.5 / 0.8 mm. https://www.amazon.com/dp/B0FSZJ5C4L — $9.90, in stock. 0.25 mm is not offered; **buy 0.3 mm** (inside bom.md's 0.2–0.3 window). Hardness is not stated (translucent silicone film is typically 40–50A) | $9.90 | S1 |
| 2.25 | Silicone adhesive | 1 tube | **CHANGED** (price) | Smooth-On Sil-Poxy 3 oz. Amazon https://www.amazon.com/dp/B00IZNNIU8 — $44.97; cheaper direct: Sculpt.com $34.99, Douglas & Sturgess $34.45, Lawnpartsman $30.72 (search results). Amazon price used for one-cart ordering | $44.97 | S1 |
| 2.26 | PTFE film tape 0.05 mm | 1 roll | **CHANGED** (price; listing churn) | 0.05 mm × 13 mm × 10 m adhesive PTFE film tape (YATOKESS) was $24.00 in search; its ASIN B0D2HPDQ98 now returns "page not found". Search https://www.amazon.com/s?k=0.05mm+PTFE+film+tape+adhesive for the current listing; fallback CGPTFE 0.08 mm × 13 mm × 36 yd https://www.amazon.com/dp/B0CXXMS3SX $31.89 (each extra 0.05 mm layer cuts the wrist hold about 10 %, re-tune L6). This roll also serves the L9 tape test (row 7.08) | $24.00 | S1 |
| 2.27 | Rubber bumpers | 1 pack | **CHANGED** (price) | 10 mm (3/8 in) silicone self-adhesive bumper pads, https://www.amazon.com/dp/B07CPQDWWK — $12.87 | $12.87 | S1 |
| 2.28 | Isolation feet | 4 (pack of 24) | **CHANGED** (price) | DTGN rubber vibration damping pads 30 mm OD × 15 mm thick, 24 pcs, https://www.amazon.com/dp/B0HBBWS755 — $15.49 | $15.49 | S1, can wait |
| 2.29 | Baseboard | 1 | not checked (optional) | Hardware store project panel, $12 [est] | ($12.00) | optional |
| 2.30 | Face cradle (SEAT) | 1 | **CONFIRMED** (price lower) | Udefineit Face Down Tabletop Massage Kit, adjustable face cradle with hand-rest pad, 2 in height adjustment, 180° tilt, clamps to a desk or mattress edge. https://www.amazon.com/dp/B0FCLM8T38 — $38.63 Prime / $45.99 regular, in stock, delivery Oct 6. Note: it hangs off the desk edge rather than standing on its own base, so put it on a separate stool or table edge (mech §10.2 preferred) rather than the arm's desk. EBANKU B09B22DTZK is "currently unavailable" | $38.63 | S1 |
| 2.31 | Face cradle cushion (PRONE) | 1 | **CONFIRMED** | xiaomubiao face-down pillow for massage table, https://www.amazon.com/dp/B0DJ5GVGCL — $19.86 | $19.86 | S1, can wait |
| 2.32 | Light machine oil | 1 | **CHANGED** (price) | Sewing machine oil 4 fl oz with zoom-spout, https://www.amazon.com/dp/B0BV4G9R1S — $9.95 (hardware-store bottle about $4) | $9.95 | S1 |
| 2.33 | Medium threadlocker | 1 | **CHANGED** (price) | Loctite 243 blue, https://www.amazon.com/dp/B004L439FE — $9.61 | $9.61 | S1 |

Section 2 subtotal in the totals: **$463.13** (bom.md $359.42); optional rows add $31.95.

### Box 2A, resolved: lift spring order

**Order:** McMaster-Carr **9654K123**, 1 pack of 12, $13.19 (table above). It replaces the "9654K___" placeholder. The box-2A geometry (3/8 in OD, 0.031 in wire, 2.5 in) has no McMaster stock part; every 3/8 OD spring McMaster stocks at ≤ 2.6 in is 0.96 lbf/in or stiffer, which fails the up-stop check (3.9 ± 0.5 N at 26.8 mm less extension) because the spring goes slack. 9654K123 passes every row of the box-2A table except OD, where it is 7.9 mm instead of 9.5 mm (clearance, not interference: §11 item 5). Tie-off rule from mech §4.3 applies: with the frame latched, tie the cord where the luggage scale reads 6.5 ± 0.5 N through the cord (expected 102.5 mm hook-to-hook), then confirm 3.9 ± 0.5 N on the up-stop (expected 3.5 N; if it reads under 3.4 N, shorten the cord 2 mm and re-check the 6.5 N point, which then becomes 6.7 N, still in window). Two must pass; the L5 single-spring lift still applies. Ten spares remain in the pack.

## 3. Fasteners and inserts

| # | Item | Qty | Status | Verified product, URL, price, stock | Line (USD) | Stage |
|---|---|---|---|---|---|---|
| 3.01 | Heat-set inserts M3 | 100 | **CHANGED** (price) | CANIPHA 100 pcs M3 brass heat-set inserts, https://www.amazon.com/dp/B0CH32W3W5 — $6.99, 12 left. Confirm the M3 × 4 mm (OD 5 mm) size on the listing; HXYBHSD "M3 x 4mm x 5mm" 100 pcs is $13.98 if not | $6.99 | S1 |
| 3.02 | Heat-set inserts M2 | 50 | **CHANGED** (price) | uxcell 50 pcs M2 × 3 mm H × 3 mm OD brass inserts (with iron tip), https://www.amazon.com/dp/B0FQ5W844D — $5.26 | $5.26 | S1 |
| 3.03 | Heat-set inserts M4 | 100 | **CHANGED** (pack) | 100 pcs M4 × 6 × 6 mm brass inserts, https://www.amazon.com/dp/B0FM3XZZ56 — $6.49 | $6.49 | S1 |
| 3.04 | Metric screw and nut assortment | 1 kit | **CHANGED** (price) | 1220 pcs M3/M4/M5/M6 hex socket head screws, nuts, washers kit, https://www.amazon.com/dp/B0FG2964F5 — $22.99 (405 pcs M3–M5 kit B0D5CRDXLH $6.99 if cash matters; it lacks M3 × 16/20) | $22.99 | S1 |
| 3.05 | M3 × 14 socket head | 60 | **CHANGED** (price) | 60 pcs M3 × 14 12.9 black, https://www.amazon.com/dp/B0DJR1J2FN — $7.12 (bom.md §9.3 item 4: confirm the yaw stack really needs 14 mm) | $7.12 | S1 |
| 3.06 | M3 × 6 flat head | 100 | **CONFIRMED** | Hordion 100 pcs M3 × 6 flat-head socket, 304, https://www.amazon.com/dp/B0GD5LZ5LW — $4.99 | $4.99 | S1 |
| 3.07 | Nyloc nut assortment | 140 | **CHANGED** (price) | 140 pcs M3–M12 nylon-insert lock nuts, https://www.amazon.com/dp/B0DP8VTVW3 — $6.59 | $6.59 | S1 |
| 3.08 | M2 socket-head assortment | 1260 | **CHANGED** (price; horn screws confirmed in the servo box) | 1260 pcs M2 × 4/6/8/10/12/16/20 socket head kit, https://www.amazon.com/dp/B0FG2CC91J — $9.99. The XL330 ships with 6 × PHS M2 × 6 (horn) and 10 × PHS M2 × 8 (frame) tapping screws (robotis.us package contents), so horn spares are not needed. OpenRB-150 mounting holes: four corner holes visible in the e-manual pinout image (MKR form factor, 25 × 66 mm); diameter not published, measure before printing P3 | $9.99 | S1 |
| 3.09 | Aluminium M3 screws | 20 | **CHANGED** (no assortment exists; single length) | 20 pcs M3 × 10 7075 aluminium socket head, https://www.amazon.com/dp/B0C77QYGDN — $11.49; search the same store for M3 × 8 (the 8 paddle/riser screws). The ×6 mass fallback can use nylon M3 × 6 from row 3.10 | $11.49 | S1 |
| 3.10 | Nylon M3 screws | 350 | **CHANGED** (price) | 350 pcs M3 nylon Phillips screws, nuts, washers, https://www.amazon.com/dp/B0FPFTQD34 — $9.99 | $9.99 | S1 |
| 3.11 | Knurled M3 × 16 thumbscrews | 10 | **CONFIRMED** | MECCANIXITY 10 pcs M3 × 16 knurled thumb screws 304, https://www.amazon.com/dp/B0FGJB2P9T — $7.69 | $7.69 | S1 |
| 3.12 | M4 × 50 (VESA + ballast), M4 × 25 | 30 | **CHANGED** (price) | 30 pcs M4 × 50 12.9 black, https://www.amazon.com/dp/B0DYSH7JCZ — $7.99; M4 × 25 from row 3.04 | $7.99 | S1 |
| 3.13 | M5 × 12 and M5 × 16 | 50 | **CHANGED** (price) | M5 × 12 socket head 304, 50 pcs, https://www.amazon.com/dp/B07CJFPBCC — $8.69; M5 × 16 from row 3.04 (kit has M5 to 20 mm). Also covers the 22 × M5 × 10 the bracket kit may lack | $8.69 | S1 |
| 3.14 | Wood screws #4 × 1/2 | 8 | not checked (optional) | Hardware store, $3 [est] | ($3.00) | optional |
| 3.15 | Zip ties | 700 | **CHANGED** (price, pack) | 700 pcs assorted 4–12 in, https://www.amazon.com/dp/B08TBM621K — $13.29 | $13.29 | S1 |

Section 3 subtotal in the totals: **$129.56** (bom.md $110.00). Tables 3A and 3B of bom.md are unchanged except: the four horn screws are the servo's own PHS M2 × 6 (confirmed), and **M2 × 8 must never be used in the horn** (ROBOTIS drawing: a 3 mm plate on the horn takes M2 × 6; M2 × 8 bottoms into the gearbox, e-manual image x330_horn_screw.png).

## 4. Printing

| # | Item | Qty | Status | Verified product, URL, price, stock | Line (USD) | Stage |
|---|---|---|---|---|---|---|
| 4.01 | PETG spool 1, bright colour | 1 kg | **CHANGED** (price down) | ELEGOO PETG 1.75 mm orange 1 kg, https://www.amazon.com/dp/B0D421691S — $15.29, in stock, delivery Oct 2–6 | $15.29 | S0 |
| 4.02 | PETG spool 2 | 1 kg | **CHANGED** (price down) | Same listing, any colour, $15.29 | $15.29 | S1 |
| 4.03 | TPU 90A | 0.75 kg | **CHANGED** (price, spool is 750 g) | Polymaker PolyFlex TPU90 1.75 mm 0.75 kg black, https://www.amazon.com/dp/B09KKXZCBR — $38.99 one-time ($37.04 Subscribe & Save), in stock; $39.99 at shop.polymaker.com | $38.99 | S0 |

Section 4 subtotal: **$69.57** (bom.md $79.00). Printer, if none: Bambu Lab A1 standalone **$299–$349** (256 × 256 × 256 mm, direct drive, prints TPU; https://printpick.dev/printers/bambu-lab-a1 and 3dpros.com), not in the totals.

## 5. Tips (tips.md §9)

| # | Item | Qty | Status | Verified product, URL, price, stock | Line (USD) | Stage |
|---|---|---|---|---|---|---|
| 5.01 | Tip item 1: PETG | 120 g | **CONFIRMED** | From spool 4.01 | $0.00 | S0 |
| 5.02 | Tip item 2: TPU 90A | 10 g | **CONFIRMED** | From spool 4.03 | $0.00 | S0 |
| 5.03 | Tip item 3: N52 6 × 2 mm | 50 | **CHANGED** (price) | 50 pcs N52 6 × 2 mm discs, https://www.amazon.com/dp/B0F4KS6KV3 — $13.75 (The Magnet Baron 50 pcs $17.99, 1.57 lb pull each, is the pull-rated alternative) | $13.75 | S0 |
| 5.04 | Tip item 4: N52 6 × 3 mm | 50 | **CHANGED** (price, 50-pack) | N52 6 × 3 mm, 50 pcs, https://www.amazon.com/dp/B0GWM33Z8X — $14.59 | $14.59 | S1, can wait |
| 5.05 | Tip item 5: steel keeper discs 6 × 1 mm | 50 | **UNAVAILABLE** (every 6 × 1 mm disc listing is 304 stainless, which is non-magnetic) | Substitute: 1 mm (19–20 gauge) mild/weldable steel sheet from the hardware store, about $8 [est], cut 6.0 × 3.9 × 1.0 mm slugs as tips §9 allows; test the sheet with a magnet at the store. (The uxcell 6 mm × 1 mm 304 discs at https://www.amazon.com/dp/B0DM5T4699, $6.09, will not hold a magnet) | $8.00 [est] | S0 |
| 5.06 | Tip item 6: feeler stock | 2 strips | **CHANGED** (bought in row 2.21's box of 12) | Precision Brand 19425, see 2.21 | $0.00 | S0 |
| 5.07 | Tip item 7: press-on nails | 1 box | **UNAVAILABLE** (B0CQF1NC93 "currently unavailable") | Substitute: Teenitor 600 pcs clear coffin nail tips, full cover, 10 sizes, https://www.amazon.com/dp/B09WTTGMSX — $9.99 (ABS; sizes 0–3 included) | $9.99 | S0 |
| 5.08 | Tip item 8: Dunlop nylon 0.88 | 12 | **CONFIRMED** | Jim Dunlop nylon standard .88 mm 12-pack, https://www.amazon.com/dp/B003B067YE — $5.76 | $5.76 | S0 |
| 5.09 | Tip item 9: Dunlop nylon 1.0 | 12 | **CHANGED** (price) | Jim Dunlop nylon 1.0 mm 12-pack, https://www.amazon.com/dp/B0D6X2CPFK — $10.49 | $10.49 | S1, can wait |
| 5.10 | Tip item 10: steel balls 3 mm G25 | 100 | **CONFIRMED** | uxcell 3 mm chrome steel bearing balls G25, 100 pcs, https://www.amazon.com/dp/B07Q4B5ZXL — $5.19 | $5.19 | S0 |
| 5.11 | Tip item 11: M3 × 8 screws | 50 | **CHANGED** (price) | Fullerkreg M3 × 8 socket head, https://www.amazon.com/dp/B07CJ9BRCK — $7.39 (confirm the 50-count variant) | $7.39 | S0 |
| 5.12 | Tip item 12: CA thin and gel | 2 | **CHANGED** (price) | Thin CA 1.75 oz kit, https://www.amazon.com/dp/B0DT14TGDY — $8.99; gel CA from the hardware store about $5 [est] (Starbond thin EM-02 is $14.79 if a named brand is wanted) | $13.99 | S0 |
| 5.13 | Tip item 13: epoxy | 1 | **CHANGED** (price) | BAZIC quick-set epoxy syringes 0.2 oz, 2-pack, https://www.amazon.com/dp/B08GWV8J5S — $7.49 | $7.49 | S0 |
| 5.14 | Tip item 14: wet-and-dry 400–2000 | 1 set | **CHANGED** (price) | Wet/dry sandpaper assortment 9 × 3.6 in, https://www.amazon.com/dp/B0FKMDYGHJ — $5.99 (confirm 400/600/1000/2000 are in the assortment; the 1000–5000 set B0F94G5CPD is $9.99) | $5.99 | S0 |
| 5.15 | Tip item 15: nail files and buffer | 1 set | **CONFIRMED** | 6-pc nail file and buffer set, https://www.amazon.com/dp/B0CFQBS5B7 — $4.99 | $4.99 | S0 |
| 5.16 | Tip item 16: drill-bit set 0.5–3.0 mm | 1 | **CONFIRMED** | Dianrui 60-pc micro drill bit set 0.3–3.5 mm with pin vise, https://www.amazon.com/dp/B0B4JZ73QX — $9.99 (includes the 3.0 mm shank for the zero pin) | $9.99 | S0 |
| 5.17 | Tip item 17: marker and varnish | 1 each | **CHANGED** (price) | Mr. Pen 0.3 mm micro fine point pens, 12-pack, https://www.amazon.com/dp/B0CZSGQ8K1 — $11.85; clear nail varnish, drugstore, about $3 [est] | $14.85 | S0 |
| 5.18 | Tip item 18: tip box | 1 | **CONFIRMED** | Printed from spool 4.01 | $0.00 | S0 |

Section 5 subtotal: **$132.46** (bom.md $98.00).

## 6. Electronics

| # | Item | Qty | Status | Verified product, URL, price, stock | Line (USD) | Stage |
|---|---|---|---|---|---|---|
| 6.01 | 5 V 4 A power adapter | 1 | **CONFIRMED** | Adafruit 1466, 5 V 4 A UL-listed, 110–220 V in, 5.5/2.1 mm centre-positive. https://www.adafruit.com/product/1466 — $14.95, in stock. Mean Well GST25A05-P1J is $13.70 at Digi-Key as the alternate | $14.95 | S1 |
| 6.02 | DC jack to screw terminal | 1 | **CONFIRMED** | Adafruit 368, https://www.adafruit.com/product/368 — $2.00, in stock | $2.00 | S1 |
| 6.03 | Fuses 1 A fast 5 × 20 | 20 | **CHANGED** (pack of 20) | BOJACK F1AL250V glass fuses, 20 pcs, https://www.amazon.com/dp/B07S96VTJR — $5.99 | $5.99 | S1 |
| 6.04 | Inline fuse holder | 5 | **CONFIRMED** | uxcell inline screw-type 5 × 20 holder, 18 AWG, 5 pcs, https://www.amazon.com/dp/B07SM5KYZ7 — $6.29, 4 left | $6.29 | S1 |
| 6.05 | Fuses 1.25 A fast | 20 | **CHANGED** (price, optional) | BOJACK F1.25AL250V 20 pcs, https://www.amazon.com/dp/B07WBZ7TNP — $6.99 | ($6.99) | optional |
| 6.06 | E-stop, boxed | 1 | **CHANGED** (price) | TWTADE YW1B-V4E02R-BOX, 22 mm, 2NC, latching, 10 A 600 V, boxed station 77 × 72 × 97 mm, 170 g. https://www.amazon.com/dp/B07NNZB41H — $15.99 (white with box, 2NC), **6 left**, delivery Oct 4–6. APIELE 1NC panel-mount LA139A-ES542 https://www.amazon.com/dp/B0F2F8TYMY $9.99 in stock is the fallback | $15.99 | S1 |
| 6.07 | E-stop weighted base | 1 plate | **CONFIRMED** (vendor; price est) | 6th plate in the SendCutSend order, $9 [est] | $9.00 [est] | S1 |
| 6.08 | Hold-to-run button | 1 (pack of 6) | **CHANGED** (price; deck hole, see §11) | uxcell 30 mm mounting-hole momentary arcade push button, NO microswitch, snap-in, **mounting hole 30 mm, overall 33 mm Ø × 26 mm tall**, 10 A rating on the listing. The bom.md ASIN B08HH78XMH now resolves to the colour family at https://www.amazon.com/dp/B07YJZFJV1: black 6 pcs **$9.99**, red 10 pcs $13.19 (1 left), yellow 10 pcs $11.08 | $9.99 | S1 |
| 6.09 | Hold-to-run cable | 1.5 m | **CHANGED** (covered by row 6.24) | Two 22 AWG silicone wires from the 6.24 kit, twisted and sleeved (bom.md's own substitute); a separate 2-core spool is unnecessary | $0.00 | S1 |
| 6.10 | Hold-to-run housing | 1 | **CONFIRMED** | Printed | $0.00 | S1 |
| 6.11 | Philmore 30-825 (optional) | 1 | **CHANGED** (price) | https://www.amazon.com/dp/B00T6RCGNC — $19.97 in stock (Vetco $6.79 + shipping) | ($19.97) | optional |
| 6.12 | Electromagnet | — | **CONFIRMED** | Row 2.15 | $0.00 | S1 |
| 6.13 | Flyback diode 1N5819 | 50 | **CHANGED** (price) | 50 pcs 1N5819, https://www.amazon.com/dp/B0H2Q1W52D — $5.99 | $5.99 | S1 |
| 6.14 | Bulk capacitor 470 µF | 1 pack | **CHANGED** (price) | 470 µF 16 V 8 × 12 mm electrolytic pack, https://www.amazon.com/dp/B0CMQCQMH5 — $5.99 | $5.99 | S1 |
| 6.15 | TVS diode SMAJ5.0A | 50 | **CHANGED** (price) | Chanzon 50 pcs SMAJ5.0A 400 W SMA, https://www.amazon.com/dp/B079KKK1GT — $6.99 | $6.99 | S1 |
| 6.16 | OpenRB-150 | 1 | **CONFIRMED** (stock flickers) | ROBOTIS America https://robotis.us/products/openrb-150 — $28.64, SKU 902-0183-000, "Add to cart" shown at 18:30 ET with no lead-time banner (an earlier fetch the same day said "sold out"): **order it the day you see it in stock**. ROBOTIS Korea https://en.robotis.com/shop_en/item.php?it_id=902-0183-000 $24.90 in stock, DHL from Korea. Board 25 × 66 mm (e-manual spec, matches P3); DXL ports JST EHR-03 / B3B-EH-A; VIN 3.7–12.6 V | $28.64 | S1 |
| 6.17 | DYNAMIXEL XL330-M288-T | 1 | **CHANGED** (availability: **2-month lead time at robotis.us**) | https://robotis.us/products/dynamixel-xl330-m288-t — $27.49, banner "estimated lead time of 2 months", SKU 902-0163-000. In stock now: **ROBOTIS Korea** https://en.robotis.com/shop_en/item.php?it_id=902-0163-000 — $23.90, ships within 3 working days by DHL from Korea (shipping and duty not shown; typically $30–40 and 3–7 days). eBay listings $57–59. Amazon has no listing. Box contents confirmed: servo, Robot Cable-X3P 180 mm, 6 × PHS M2 × 6 (horn), 10 × PHS M2 × 8 (frame). Spec confirmed: 0.52 N·m at 5 V / 1.47 A, 103 rpm, 20 × 34 × 26 mm, 18 g, 4096 steps. Fallback in stock at robotis.us: XL330-M077-T $27.49 (0.215 N·m, 383 rpm; bom.md §9.1 firmware re-derivation) | $27.49 | S1 |
| 6.18 | DXL cable 340 mm or longer | 1 | **UNAVAILABLE** (ROBOTIS sells X3P only in 100/180/240 mm; robotis.us lists 180 mm only) | Substitute: **Robot Cable-X3P 180 mm (10 pcs)** https://robotis.us/search?q=X3P — $21.85 in stock (convertible version $17.83); solder-splice two cables with heat-shrink to 360 mm inside the braided sleeve (row 6.27). Zero-cost route: the two servos (6.17 + 6.33) each ship with a 180 mm X3P, splice those. Crimping your own needs JST EH 2.5 mm housings and the SN-28B crimper (row 8.19, $22.29) | $21.85 | S1 |
| 6.19 | Potentiometers 10 kΩ with knobs | 3 | **CHANGED** (price) | TWTADE 3 pcs WH148 B10K with knobs, nuts, washers, https://www.amazon.com/dp/B082FCRQS2 — $9.99 (7 mm bushing: confirm on the listing) | $9.99 | S1 |
| 6.20 | Toggle switch | 10 | **CONFIRMED** | Taiss 10 pcs SPST mini toggle MTS-101, 6 mm bushing, https://www.amazon.com/dp/B0799LBFNY — $6.99 | $6.99 | S1 |
| 6.21 | Status LED | 300 | **CHANGED** (price) | 300 pcs 3 mm and 5 mm LED assortment, https://www.amazon.com/dp/B0F38LJDJB — $7.99 | $7.99 | S1 |
| 6.22 | Resistor assortment | 1000 | **CHANGED** (price) | BOJACK 1000 pcs 25 values 1/4 W, https://www.amazon.com/dp/B08FD1XVL6 — $9.99 | $9.99 | S1 |
| 6.23 | Ceramic 100 nF | 100 | **CONFIRMED** | 100 pcs 100 nF (104) ceramic, https://www.amazon.com/dp/B0H6MJXNKM — $5.49 | $5.49 | S1 |
| 6.24 | 22 AWG silicone wire kit | 6 × 13 ft | **CHANGED** (price) | 22 AWG silicone wire kit, 6 colours × 13 ft, tinned copper, https://www.amazon.com/dp/B0C7T9KYND — $10.76 (also feeds row 6.09) | $10.76 | S1 |
| 6.25 | 6-core 26 AWG cable | 1 m | **CHANGED** (gauge: 22 AWG 6-conductor is what sells cheaply) | 22 AWG 6-conductor shielded UL2464, 25 ft, https://www.amazon.com/dp/B0D9JVVGV5 — $19.99 (26 AWG 6-conductor is $58.98 for a spool). Ribbon cable with Dupont ends from row 6.29 is the cheaper alternative | $19.99 | S1 |
| 6.26 | Heat-shrink assortment | 580 | **CHANGED** (price) | Ginsco 580 pcs 2:1, https://www.amazon.com/dp/B01MFA3OFA — $7.99 | $7.99 | S1 |
| 6.27 | Braided sleeving 6 mm | 25 ft | **CHANGED** (price) | PET expandable braided sleeve 1/4 in, 25 ft, https://www.amazon.com/dp/B0F8Q54B8J — $9.19 | $9.19 | S1 |
| 6.28 | Wago 221-413 | 10 | **CONFIRMED** | WAGO 221-413, "Small Bag" (10 pcs) variant on https://www.amazon.com/dp/B07W7W91FX — $7.99 (box of 50 $24.45), in stock | $7.99 | S1 |
| 6.29 | Dupont kit | 1550 | **CHANGED** (price) | IWISS 1550 pcs 2.54 mm Dupont connector kit (headers, jumpers, crimp pins), https://www.amazon.com/dp/B08X6C7PZM — $15.49. Pre-crimped alternative: ELEGOO 120 pcs jumper set $6.98 | $15.49 | S1 |
| 6.30 | Perfboard | 54 | **CHANGED** (price) | 54 pcs double-sided perfboard kit 5 sizes, https://www.amazon.com/dp/B0G4QTPVZ8 — $8.99 | $8.99 | S1 |
| 6.31 | USB-C cable | 1 | **CHANGED** (length 1 m) | LDLrui USB-C to USB-A 3.1 Gen 2 data cable 3 ft, https://www.amazon.com/dp/B08NXJKNNL — $5.99; a 2 m data cable is about $13 (B0FNCDVPJN $13.83) if the laptop cannot sit within 1 m of the arm | $5.99 | S1 |
| 6.32 | Insulated crimp terminals | 280 | **CONFIRMED** | Feggizuli 280 pcs spade/fork connector kit 2.8/4.8/6.3 mm, https://www.amazon.com/dp/B0B4H54KPS — $7.69 | $7.69 | S1 |
| 6.33 | XL330-M288-T spare / yaw | 1 | **CHANGED** (availability, as 6.17) | Same part, same sources; add to the Stage-1 ROBOTIS order | $27.49 | S3 |
| 6.34 | Lazy-Susan bearing ring | 1 | **CHANGED** (price) | Aluminium alloy turntable bearing (about 4 in), https://www.amazon.com/dp/B08CSMYXFV — $12.99 | $12.99 | S3 |
| 6.35 | Bar load cell 5 kg with HX711 | 1 kit | **CHANGED** (price; **size mismatch, §11**) | NOYITO 5 kg load cell + HX711 combo, https://www.amazon.com/dp/B07BGS58TL (5 kg option) — $6.79 (Degraw B075317R45 is unavailable). Every 5 kg bar cell found is **75–80 mm long × 12.7 mm square**, holes M4/M5 at 15 mm spacing; no 40 mm-long 5 kg cell exists | $6.79 | S3 |

Section 6 subtotal: **$342.96** (bom.md $300.57); optional rows add $26.96.

## 7. Bench and test kit

| # | Item | Qty | Status | Verified product, URL, price, stock | Line (USD) | Stage |
|---|---|---|---|---|---|---|
| 7.01 | Real-hair training head, short | 1 | **CHANGED** (price down; clamp included) | 16–18 in 100 % real hair mannequin head with clamp holder, https://www.amazon.com/dp/B077DBY6XZ — $25.99 (YODIDI 16 in with table clamp B0F1CJJDJX $25.99). HAIREALM B01HO3LVX0 (bom.md) is "currently unavailable" | $25.99 | BK, buy with S0 |
| 7.02 | Real-hair training head, long | 1 | **CHANGED** (price) | Opini 22–24 in 100 % real human hair mannequin head, $37.89, seen in Amazon's "consider these available items" panel (ASIN not captured; search "Opini mannequin head 22-24"). Search alternative: SOPHIRE 20–22 in https://www.amazon.com/dp/B07VNDHN8Y | $37.89 | BK |
| 7.03 | Mannequin table clamp | 1 | **CHANGED** (included with 7.01) | Clamp ships with row 7.01 | $0.00 | BK, buy with S0 |
| 7.04 | Kanekalon synthetic wig | 1 | **CHANGED** (price) | Aimole 24 in long straight Kanekalon premium synthetic wig, https://www.amazon.com/dp/B07H96W6S7 — $35.99, **1 left**; listing text says "100 % Japanese premium synthetic fiber" (Kanekalon is the Kaneka fibre; the title names it). Alternatives $38–49 under https://www.amazon.com/s?k=kanekalon+synthetic+wig+long+straight | $35.99 | BK |
| 7.05 | Styrofoam ball 7 in | 1 (2-pack) | **CHANGED** (price) | Crafare 2-pack 7 in foam balls, https://www.amazon.com/dp/B0CN4372B1 — $16.99 (Homeford 7-3/4 in single $11.26 is R 98 mm, outside the 1.2 % window) | $16.99 | BK |
| 7.06 | Foam wig head | 1 | **CHANGED** (price) | SHANY styrofoam model head, https://www.amazon.com/dp/B0CL5LZ22X — $14.99 | $14.99 | BK |
| 7.07 | Nylon monofilament 100 µm | 1 spool | **CHANGED** (price) | SF ultra-smooth mono fishing line, choose 2 lb (0.10 mm), https://www.amazon.com/dp/B0CDGLRS7Q — $6.99 | $6.99 | BK |
| 7.08 | Polyester film tape 50 µm | 1 roll | **CHANGED** (covered by row 2.26) | 3M 850 polyester tape is $43.98+ on Amazon; the 0.05 mm PTFE film tape in row 2.26 is the same thickness and serves the L9 three-layer test | $0.00 | BK, buy with S0 |
| 7.09 | Rod 10 mm | 1 | **CONFIRMED** (store) | Hardware store 10 mm rod or 3/8 in dowel, $2 [est] | $2.00 [est] | BK, buy with S0 |
| 7.10 | Calibration weight set | 1 | **CHANGED** (price down) | 7-pc calibration weights 1–100 g (210 g total), https://www.amazon.com/dp/B08SQ2WTNY — $6.99 | $6.99 | BK |
| 7.11 | Pulley for tether weights | 1 | **CONFIRMED** | Spare 623ZZ from 2.08 | $0.00 | BK |
| 7.12 | Carbon paper | 30 | **CHANGED** (price down) | PSLER 30 sheets A4 carbon paper, https://www.amazon.com/dp/B09M8R4CMW — $3.99 | $3.99 | BK, buy with S0 |
| 7.13 | Foam ear plugs | 100 pr | **CHANGED** (price) | AZEN 100 pairs NRR 32, https://www.amazon.com/dp/B0CD1BGHDS — $8.99 | $8.99 | BK |
| 7.14 | Black cloth and card | 1 | **CHANGED** (price) | Black felt sheet 36 × 36 in, https://www.amazon.com/dp/B0G48NF6DX — $7.99 | $7.99 | BK |
| 7.15 | Lint roller | 1 | **CHANGED** (price) | Swihauk 600-sheet lint rollers, https://www.amazon.com/dp/B0FBRSP575 — $9.99 | $9.99 | BK |
| 7.16 | IR thermometer | 1 | **CONFIRMED** | Etekcity 774 infrared thermometer, https://www.amazon.com/dp/B0B71HFH9K — $18.99 | $18.99 | BK |
| 7.17 | Hygrometer | 1 | **CONFIRMED** | TempPro digital hygrometer thermometer, https://www.amazon.com/dp/B07WCR5Y4B — $9.99 | $9.99 | BK |
| 7.18 | 10× loupe | 1 | **CHANGED** (price) | 10× Hastings triplet jewelers loupe 16 mm, https://www.amazon.com/dp/B0DWXDKXMT — $12.99 | $12.99 | BK, buy with S0 |
| 7.19 | Hair clips | 1 pack | **CHANGED** (price) | AIMIKE sectioning clips, https://www.amazon.com/dp/B08NC7BR92 — $6.99 | $6.99 | BK |
| 7.20 | Hand mirror | 1 | **CONFIRMED** | OMIRO 9.3 × 6.6 in hand mirror, https://www.amazon.com/dp/B08P5CF97D — $5.69 | $5.69 | BK |
| 7.21 | Safety glasses | 1 | **CHANGED** (price) | TICONN clear ANSI Z87.1 safety glasses, https://www.amazon.com/dp/B0BGSFQJF6 — $14.95 | $14.95 | BK |
| 7.22 | Spring scale 0–5 N | 1 | **CHANGED** (price down) | Eisco Labs tubular spring scale 5 N / 500 g, https://www.amazon.com/dp/B00VKK0Y50 — $9.99 | $9.99 | BK |
| 7.23 | Steel ruler 150 mm | 1 | **CHANGED** (price) | PEC Tools 6 in / 150 mm rigid rule, https://www.amazon.com/dp/B0FM3KFSF6 — $11.99 | $11.99 | BK |
| 7.24 | Phone macro clip lens | 1 | **CHANGED** (price, optional) | Xenvo Pro lens kit, https://www.amazon.com/dp/B01A6D2JVI — $25.99 | ($25.99) | optional |
| 7.25 | Comb and tweezers | 1 each | **CHANGED** (price) | HengTianMei 7-pc precision tweezers, https://www.amazon.com/dp/B08SJZY627 — $7.99; wide-tooth comb, drugstore, $3 [est] | $10.99 | BK |
| 7.26 | Cleaning consumables | 1 lot | **CHANGED** (price) | Dealmed 70 % isopropyl alcohol 16 oz, https://www.amazon.com/dp/B07GDR6PY8 — $9.99; pipe cleaners and cotton balls, drugstore, $4 [est] | $13.99 | BK, buy with S0 |
| 7.27 | Paint pen | 1 | **CHANGED** (12-pack online; a single pen is about $4 at a hardware store) | Overseas black oil-based fine-tip paint markers, 12, https://www.amazon.com/dp/B0GH6T8HQD — $13.99 | $13.99 | BK |

Section 7 subtotal: **$309.34** (bom.md $240.00); optional adds $25.99. "Buy with S0" rows: 7.01, 7.03, 7.08, 7.09, 7.12, 7.18, 7.26 = **$80.95**.

## 8. Tools

| # | Item | Qty | Status | Verified product, URL, price, stock | Line (USD) | Stage |
|---|---|---|---|---|---|---|
| 8.01 | 3D printer (if not owned) | 1 | **CONFIRMED** (range; not in totals) | Bambu Lab A1 standalone $299–$349 (256 mm bed, direct drive, TPU); the A1 mini (180 mm) stays excluded for P21 | $0.00 | T |
| 8.02 | Soldering iron | 1 | **CHANGED** (price; lead time) | PINECIL V2, https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/ — $25.99 community price ($35.99 retail), in stock; Pine64 ships from Hong Kong, allow 1–3 weeks and about $9 shipping. Plus a 65 W USB-C PD charger if none | $25.99 | T |
| 8.03 | Heat-set insert tip | 1 set | **CHANGED** (price) | Heat-set insert tool tips with inserts M2–M8 (TS100/Pinecil C-type), https://www.amazon.com/dp/B0DN638LJB — $18.04 | $18.04 | T |
| 8.04 | Solder and flux | 1 lot | **CHANGED** (price) | MAIYUM 63/37 0.6 mm 50 g, https://www.amazon.com/dp/B075WBDYZZ — $8.99; no-clean rosin flux pens, 3 pcs, https://www.amazon.com/dp/B0953NGKXR — $9.99 | $18.98 | T |
| 8.05 | Digital calipers 150 mm | 1 | **CHANGED** (price) | Stainless digital caliper 6 in, https://www.amazon.com/dp/B087N5N45G — $26.99 | $26.99 | T, buy with S0 |
| 8.06 | Kitchen scale 0.1 g | 1 | **CHANGED** (price down; 0.01 g) | MAXUS digital pocket scale 500 g × 0.01 g with tray, https://www.amazon.com/dp/B07DJBDL6L — $9.99 | $9.99 | T, buy with S0 |
| 8.07 | Luggage scale | 1 | **CHANGED** (price down) | Digital luggage scale 110 lb, backlit, https://www.amazon.com/dp/B0GLHJ4746 — $5.79 (the Walmart G-Force page is behind a bot check) | $5.79 | T |
| 8.08 | Multimeter | 1 | **CONFIRMED** | AstroAI digital multimeter, https://www.amazon.com/dp/B08DHHJPS1 — $18.99 | $18.99 | T |
| 8.09 | Metric ball-end hex keys | 1 set | **CONFIRMED** | AMTOVL 9-pc metric ball-end 1.5–10 mm, https://www.amazon.com/dp/B0CJBRYQF3 — $9.99 | $9.99 | T, buy with S0 |
| 8.10 | M5 tap and tap handle | 1 set | **CHANGED** (price; kit includes handle and M3–M8 taps) | KOOTANS ratchet T-handle tap wrench + 5 taps M3/M4/M5/M6/M8, https://www.amazon.com/dp/B08JB2YQWH — $11.78 | $11.78 | T |
| 8.11 | Drill bits 1/4 in and 5.0 mm | 1 each | **CHANGED** (price) | uxcell 5 mm HSS hex-shank bits, 5 pcs, https://www.amazon.com/dp/B09YV1GC5C — $9.99; 1/4 in jobber bit, hardware store, $4 [est] | $13.99 | T |
| 8.12 | Mitre box and hacksaw | 1 set | **CHANGED** (price down) | HAUTMEC 6 in mini hacksaw with mitre box, bi-metal blade, https://www.amazon.com/dp/B07CSK7TCD — $8.99 | $8.99 | T |
| 8.13 | Deburring tool and needle files | 1 set | **CHANGED** (price down) | VASTOOLS deburring tool kit with 6 needle files, https://www.amazon.com/dp/B0CSG6QN5X — $8.99 | $8.99 | T |
| 8.14 | Sandpaper 220 and 400 | 1 pack | **CONFIRMED** | Wet/dry assortment, https://www.amazon.com/dp/B0FKMDYGHJ — $5.99 (same pack as 5.14 if it covers 220) | $5.99 | T |
| 8.15 | Plastic polish | 1 | **CHANGED** (price) | Novus plastic polish, https://www.amazon.com/dp/B000RT6RUG — $11.99 | $11.99 | T |
| 8.16 | Aviation snips | 1 | **CHANGED** (price) | HURRICANE 10 in straight-cut aviation snips, https://www.amazon.com/dp/B07GDDF5JB — $13.39 | $13.39 | T, buy with S0 |
| 8.17 | Fine stone | 1 | **CHANGED** (price; diamond cards) | Honoson 3-pc credit-card diamond stones 300/600/1000, https://www.amazon.com/dp/B092SCSFL6 — $19.99 (a hardware-store pocket stone is about $8) | $19.99 | T |
| 8.18 | Flush cutters, wire stripper, screwdrivers | 1 each | **CHANGED** (price) | Micro flush cutters 2-pack, https://www.amazon.com/dp/B0F3DF92MP — $4.96; IRWIN Vise-Grip 8 in stripper 10–22 AWG, https://www.amazon.com/dp/B000JNNWQ2 — $13.99; precision screwdriver set, $8 [est] | $26.95 | T, buy with S0 |
| 8.19 | Crimp tool | 1 | **CHANGED** (price, optional) | iCrimp SN-28B, https://www.amazon.com/dp/B00OMM4YUY — $22.29 (needed only if you crimp the DXL cable instead of splicing) | ($22.29) | optional |
| 8.20 | Helping hands | 1 | **CHANGED** (price, optional) | Kaisiking helping hands with magnifier, https://www.amazon.com/dp/B0D8W2BSXJ — $20.99 | ($20.99) | optional |

Section 8 subtotal: **$256.82** (bom.md $227.00); optional adds $43.28. "Buy with S0" rows: 8.05, 8.06, 8.09, 8.16, 8.18 = **$132.29** (bom.md's $71 assumed cheaper calipers and cutters).

## 9. Substitutes and single points of failure (updates to bom.md §9)

| Part | Finding | Action |
|---|---|---|
| XL330-M288-T | robotis.us: 2-month lead. ROBOTIS Korea: in stock, $23.90, DHL. XL330-M077-T: in stock at robotis.us | Order 2 from Korea now, or 2 from robotis.us on back-order plus 1 M077 as the bridge servo if Stage 1 cannot wait 2 months |
| OpenRB-150 | robotis.us flickered sold-out → add-to-cart within one day; Korea $24.90 in stock | Order on sight; no Stack-B redesign needed |
| Lift springs | Box 2A part does not exist; 9654K123 (5/16 OD) pinned | Widen nothing: the P1 channel can stay 9.5 mm (slack) or be narrowed to 8.5 mm in the next CAD pass |
| Feeler stock | Only sold as a 12-blade box | One box covers wand and rig leaves with 8 spares |
| 340 mm DXL cable | Does not exist | Splice two 180 mm X3P cables (the servos ship with them) |
| 12 × 1.5 steel discs, 6 × 1 steel discs | Not sold as mild steel in small packs | SendCutSend add-on and hardware-store 1 mm sheet |
| 5 kg load cell | 80 mm long, not 40 | Stage-3 wrist slot must be re-drawn (§11) |

## 10. All bom.md [verify] items, resolved

| bom.md item | Result |
|---|---|
| 2.01 arm minimum load, swivel, tilt | 2.0 kg minimum (ballast needed); swivel ±90° ✓; tilt −50°/+30° (not ±45°) |
| 2.05 rail pitch, block pattern | HIWIN: block 15 × 10 mm M3 ✓; rail P 20, E 7.5; 100 mm rail end distance must be measured |
| 2.06 spare block on a retainer | ✓ (ReliaBot ships it on a plastic rail with spare balls) |
| 2.10 McMaster shoulder-screw number | Not readable without a cart; Amazon 304 SS 5 × 25 M4 used |
| 2.13 spring suffix, pack | 9654K123, pack of 12 |
| 2.20 disc thickness | No stock part; SendCutSend or M6 washer |
| 2.21 feeler part number | Precision Brand 19425 (12 × 0.012 × 1/2 × 12 in, C1095) |
| 2.24 silicone thickness/hardness | 0.3 mm available (0.25 is not); hardness unstated |
| 2.26 0.05 mm PTFE | Exists (10 m × 13 mm, about $24); listing churns |
| 2.30 face cradle | Udefineit tabletop kit, tilt and height adjustable, desk-edge mount |
| 3.05 M3 × 14 | Available; length still to confirm in CAD |
| 3.08 OpenRB hole size; XL330 horn screws | Holes visible, diameter unpublished; horn screws ship with the servo (M2 × 6, M2 × 8) |
| 3.13 M5 lengths | Available |
| 6.08 button pack, deck hole | 6-pack; hole is 30 mm, P39 says 29.6 (§11) |
| 6.15 SA5.0A through-hole alternative | Not checked; SMAJ5.0A is cheap and in stock |
| 6.18 340 mm X3P | Does not exist |
| 6.35 40 mm 5 kg cell | Does not exist; cells are 75–80 mm |
| 7.04 Kanekalon fibre | Named in the listing title; body says "Japanese premium synthetic fiber" |
| 8.01 printer | Bambu A1 $299–349, 256 mm bed, direct drive |
| Mean Well GST25A05 | $13.70 Digi-Key, in stock |
| Misumi tapped-end 2020 | Not checked; the M5 tap kit (8.10) is cheaper |
| OpenRB-150 outline | 25 × 66 mm ✓ |
| Adafruit 3872/3873 prices | $7.50 / $9.95 |

## 11. Spec mismatches found (correct the CAD before printing)

1. **XL330 side mounting holes do not exist (mech §5.3, P13).** The ROBOTIS X330 drawing (ROBOTIS XL330.pdf, sheet "X330", 28-May-20; the e-manual download link https://www.robotis.com/service/download.php?no=1986 currently returns 404, a rendered copy is in this session's scratchpad as `xl330_drawing.pdf.png`) shows **no holes on the 23 × 34 mm side faces**; those faces carry the two JST connectors, at about **13–24 mm below the horn-end face**, each protruding about 1 mm. The frame holes are **4 × Ø1.6 mm, 3.5 mm deep, on a 16 × 30 mm rectangle on the horn face** (Detail A) and **4 × Ø1.6 mm, 4.5 mm deep, on the same 16 × 30 mm rectangle on the back face** (Detail B), both for the supplied PHS M2 × 8 tapping screws. P13's "2 × Ø2.2 for M2 into the servo" side holes must go; locate the cradle instead with 2 or 4 of the back-face holes through the strap P14 (strap 3.5 mm thick with M2 × 8 gives 4.5 mm engagement, exactly the hole depth) and cut a window in one 23 × 34 side wall of the pocket for the connector and cable from Z ≈ 13 to 24 mm below the horn face.
2. **XL330 output axis is 9.5 mm from the horn-end face, not 10 mm** (same drawing: body 20 × 34 × 23 mm plus a 3 mm horn, overall 26 mm; axis 9.5 mm from the end, centred in the 20 mm width). mech §5.3 assumed 10 mm; the P13 pocket floor and the elbow-axis reference move 0.5 mm. Body 20 × 34 × 23 and overall 26 mm match mech.
3. **XL330 horn pattern (P16):** horn Ø16 mm, 3 mm thick, **4 × Ø1.6 mm holes, 3.0 mm deep max, on P.C.D. Ø12 mm**, at 90° spacing with one hole on the body's long axis, for M2 tapping screws (PHS M2 × 6 supplied). P16's "4 holes for the horn's M2 pattern" becomes 4 × Ø2.2 through-holes on Ø12 mm; the disc must be ≤ 3 mm thick where the M2 × 6 passes (3 mm plate + 3 mm engagement), and M2 × 8 is prohibited in the horn. The centre relief Ø6 clears the horn's centre screw ✓.
4. **Arcade-button deck hole (P39):** the uxcell button needs a **30 mm mounting hole** (listing: "30mm Mounting Hole", body 33 mm max diameter, 26 mm tall). P39 specifies Ø29.6. Print Ø30.2 and ream to 30.0 for the snap-in collar; the 2.0 mm deck is inside the usual 1–4 mm panel range.
5. **Lift spring OD 7.9 mm, not 9.5 mm** (row 2.13). The P1 rear-face spring channels sized for 0.36–0.39 in will hold a 5/16 in spring with 1.6 mm side slack; either accept (the cord keeps it taut) or narrow the channels to 8.5 mm in the next P1 revision. Free length 62 mm and working hook-to-hook 102.5 mm fit the Z 30 → Z 148 span.
6. **Stage-3 load cell is 75–80 mm long** (every 5 kg bar cell listed: 80 × 12.7 × 12.7 mm, M4/M5 holes at 15 mm spacing on each end), not 40 × 12 mm as mech §7.4 assumes for the wrist slot. The 41 × 13 × 8 mm pocket must become about 82 × 14 × 14 mm, or the cell moves to the riser arm. No CAD change at Stage 1 (P47 filler stays).
7. **MGN9 rail end distance:** HIWIN standard E = 7.5 mm with P = 20 mm, which does not tile a 100 mm rail; generic 100 mm rails are usually 10/30/50/70/90 but not always. Measure the first hole from each end before printing P21 (mech §6.1 already marks this [VERIFY]). Block 15 × 10 mm M3, 3 mm thread depth ✓; rail 9 × 6.5 mm ✓.
8. **Monitor arm tilt is −50°/+30°, not ±45°** (row 2.01). Only Stage-1 head-swivel yaw (±90° ✓) is required by ADD-1 ruling 8; if the +45° tilt is needed for SEAT posture, note it as a limitation of this arm.
9. **OpenRB-150 mounting holes:** four corner holes are visible in the e-manual pinout image (25 × 66 mm board) but their diameter and positions are not published and the drawing downloads (no=2118–2121) return 404. P3's four Ø2.5 bosses are plausible for M2; measure on arrival.

## 12. Order list by vendor (one cart each)

| Vendor | Items (qty) | Subtotal | Shipping | Lead time to a US apartment |
|---|---|---|---|---|
| **ROBOTIS America** (robotis.us) | OpenRB-150 ×1 ($28.64); Robot Cable-X3P 180 mm 10-pack ×1 ($21.85); XL330-M288-T ×2 ($54.98, **2-month lead**) | $105.47 | calculated at checkout (about $10) | OpenRB and cable 2–5 days; XL330 about 2 months. **Alternative:** ROBOTIS Korea en.robotis.com for the two XL330 ($47.80) by DHL from Korea (about $30–40 shipping plus any duty, 3–7 days) |
| **Adafruit** | 3872 electromagnet ×1 ($7.50); 1466 brick ×1 ($14.95); 368 jack ×1 ($2.00) | $24.45 | about $10 | ships same or next business day, 2–5 days |
| **McMaster-Carr** | 9654K123 spring, 1 pack of 12 ($13.19) | $13.19 | about $8 | next-day ground, no minimum |
| **K&J Magnetics** | D61 ×3 ($1.47) | $1.47 | about $5 | 1–3 days, same-day shipping |
| **Zoro** | Precision Brand 19425 ×1 ($28.49) | $28.49 | about $6 (free over $50) | 2–5 days |
| **SendCutSend** | 6 × 100 × 100 × 3 mm plates (5 ballast + e-stop base) and 2 × Ø12 × 1.5 mm discs; one upload | $56.00 [est] | free over $39 | 2–5 days after upload |
| **Pine64** | PINECIL V2 ×1 ($25.99) | $25.99 | about $9 | 1–3 weeks from Hong Kong (or Amazon Pinecil about $39, 2 days) |
| **Hardware store / drugstore** | 1/8 × 1 in steel bar; 1 mm steel sheet; 10 mm rod; nylon M6 washers; 1/4 in bit; gel CA; clear varnish; comb; pipe cleaners; precision screwdrivers | about $46 [est] | — | same day |
| **Amazon** | everything else, 95 lines: S0 $153.66, S1 $719.17, S3 $19.78, BK $307.34, T $230.83 | $1,430.78 | $0 (Prime, or over $35 per order) | 1–5 days; two slow lines noted (2.06 spare block Oct 18 – Nov 4; TOHIRA kit avoided) |
| **All vendors** | | **$1,703.84** (+ about $28 of in-store items already inside the line totals as [est]) | **about $48** | |

Amazon cart by stage, for copy-paste (ASINs): **S0** B0D421691S, B09KKXZCBR, B0F4KS6KV3, B09WTTGMSX, B003B067YE, B07Q4B5ZXL, B07CJ9BRCK, B0DT14TGDY, B08GWV8J5S, B0FKMDYGHJ, B0CFQBS5B7, B0B4JZ73QX, B0CZSGQ8K1. **S1** B0CTJYYSML, B0DY7GX9YL, (CLAHJQX bracket kit), (uxcell MGN9 100 mm + MGN9C), B0FM82NXTG, B0H38WY4PJ, B0D54JLX1Z, B0815B5D5W, B0BVZD6YHP, B0BRXHX44X, B004P9C5AK, B091913Z7F, B08C34R45G, B0FSZJ5C4L, B00IZNNIU8, (0.05 mm PTFE tape), B07CPQDWWK, B0HBBWS755, B0FCLM8T38, B0DJ5GVGCL, B0BV4G9R1S, B004L439FE, B0CH32W3W5, B0FQ5W844D, B0FM3XZZ56, B0FG2964F5, B0DJR1J2FN, B0GD5LZ5LW, B0DP8VTVW3, B0FG2CC91J, B0C77QYGDN, B0FPFTQD34, B0FGJB2P9T, B0DYSH7JCZ, B07CJFPBCC, B08TBM621K, B0D421691S, B0GWM33Z8X, B0D6X2CPFK, B07S96VTJR, B07SM5KYZ7, B07NNZB41H, B07YJZFJV1 (black 6), B0H2Q1W52D, B0CMQCQMH5, B079KKK1GT, B082FCRQS2, B0799LBFNY, B0F38LJDJB, B08FD1XVL6, B0H6MJXNKM, B0C7T9KYND, B0D9JVVGV5, B01MFA3OFA, B0F8Q54B8J, B07W7W91FX (small bag), B08X6C7PZM, B0G4QTPVZ8, B08NXJKNNL, B0B4H54KPS. **S3** B08CSMYXFV, B07BGS58TL. **BK** B077DBY6XZ, B07VNDHN8Y, B07H96W6S7, B0CN4372B1, B0CL5LZ22X, B0CDGLRS7Q, B08SQ2WTNY, B09M8R4CMW, B0CD1BGHDS, B0G48NF6DX, B0FBRSP575, B0B71HFH9K, B07WCR5Y4B, B0DWXDKXMT, B08NC7BR92, B08P5CF97D, B0BGSFQJF6, B00VKK0Y50, B0FM3KFSF6, B08SJZY627, B07GDR6PY8, B0GH6T8HQD. **T** B0DN638LJB, B075WBDYZZ, B0953NGKXR, B087N5N45G, B07DJBDL6L, B0GLHJ4746, B08DHHJPS1, B0CJBRYQF3, B08JB2YQWH, B09YV1GC5C, B07CSK7TCD, B0CSG6QN5X, B000RT6RUG, B07GDDF5JB, B092SCSFL6, B0F3DF92MP, B000JNNWQ2.

## 13. Day-0 order (so the Stage-0 wand and print tests start within a week)

Place these on day 0; everything is in stock with 1–5 day delivery except where noted.

| Order | Lines | Cash | Why on day 0 |
|---|---|---|---|
| **Amazon, Day-0 cart** | 4.01 PETG orange, 4.03 TPU90, 5.03 N52 6 × 2, 5.07 nail tips, 5.08 picks 0.88, 5.10 balls, 5.11 M3 × 8, 5.12 CA, 5.13 epoxy, 5.14 wet-dry, 5.15 files, 5.16 drill set, 5.17 markers; 7.01 real-hair head with clamp, 7.12 carbon paper, 7.18 loupe, 7.26 IPA; 8.05 calipers, 8.06 scale, 8.09 hex keys, 8.16 snips, 8.18 cutters and stripper; **plus the print-test parts** 2.05 rail + MGN9C ($9.99; mech §11 says print-test P15/P2/P13/P34 with a leaf scrap, and P21/P26 need the real rail and block to measure), 2.08 623ZZ, 2.09 625-2RS (2.15 is Adafruit, below) | about $370 (S0 $153.66 + BK $56.96 + T $132.29 + rail and bearings $26.87) | wand printed and tested by day 3–4; rail in hand for P21/P26 hole measurement |
| **Zoro** | 2.21 feeler stock box (covers 5.06 wand leaves) | $28.49 + ~$6 | the wand leaf is cut from it; 2–5 days |
| **Hardware store, day 0** | 1 mm steel sheet (5.05 keepers), 10 mm rod (7.09), gel CA, clear varnish, comb | about $20 | same day |
| **ROBOTIS, day 0, before the Stage-0 gate** (deviation from tips §7.4, justified by the 2-month lead) | 2 × XL330-M288-T (robotis.us back-order $54.98, or ROBOTIS Korea $47.80 + DHL), OpenRB-150 $28.64, X3P 10-pack $21.85 | $105.47 + shipping | if the Stage-0 gate fails, the OpenRB and cables are returnable/resellable and the servos are the only sunk cost; waiting for GO adds 2 months to Stage 1 |
| **Adafruit, day 0** | 2.15 electromagnet, 6.01 brick, 6.02 jack | $24.45 + ~$10 | magnet is needed for the P6/P1 fit prints; ships same day |
| **McMaster, day 0** | 2.13 springs 9654K123 | $13.19 + ~$8 | needed for the first hinge test print (P1/P2 sheaves); next-day |
| **SendCutSend, day 0 if the arm will be the HUANUO 2.0 kg-minimum model** | 2.02 plates, 6.07 base, 2.20 discs | about $56 | 2–5 days after upload; needed before the arm carries the module |

Everything else in Stage 1 (the rest of §2, §3, §6, bench kit, tools) is placed the day after the Stage-0 GO as bom.md §0.1 directs; all of it showed 1–6 day Amazon delivery on 2026-10-01 except the spare MGN9C block (Oct 18 – Nov 4, can wait).

## 14. Method and limits

Prices were read on 2026-10-01 from the vendor pages linked in each row (Adafruit, K&J, ROBOTIS America and Korea, McMaster-Carr product tables, Zoro, Pine64, Digi-Key, HIWIN datasheet, ROBOTIS e-manual and drawing) and from Amazon product pages opened in a browser pane; Amazon search-result prices were used where a single product page was not opened (rows marked with a search URL). Amazon prices move daily and several items showed low stock ("1 left", "6 left"). McMaster's site rendered its spring tables but not its feeler-gauge or shoulder-screw tables, so those two rows use Precision Brand (Zoro) and Amazon parts. The ROBOTIS drawing downloads (XL330 no=1985–1987, OpenRB-150 no=2117–2121) returned 404 on the day; the XL330 dimensions come from a rendered copy of the same ROBOTIS X330 sheet (28-May-20) and the e-manual images x330_horn_screw.png and xl330_assembly_integrated.png. Walmart's page (luggage scale) is behind a bot check. SendCutSend prices need a CAD upload and remain estimates.
