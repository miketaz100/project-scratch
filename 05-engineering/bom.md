# SP1 Float-Arm: Bill of Materials (BOM agent)

**Project SCRATCH · 05-engineering · 2026-10-01 · BOM agent.** The consolidated list Michael orders from: one apartment build, US delivery. Builds to DESIGN-FREEZE.md as amended by DESIGN-FREEZE-ADDENDUM-1.md (cited "ADD-1"), mechanical.md ("mech"), tips.md ("tips"), electronics-firmware.md ("EF"), test-protocols.md ("TP"), 03-tournament/DECISION.md and 01-foundations/component-landscape.md ("CL"). ADD-1 rulings applied: tether 25 mm, MGN9C block, two lift springs, one bonded silicone membrane, 24 mm nail pitch (no BOM effect beyond the parts below), 7.5 N leaf proof (luggage scale), servo zero by pin.

**Price tags.** Every price is USD, before tax and shipping, as of October 2026. **[cited]** is taken from a project document (named in the Source column). **[est]** is the BOM agent's estimate; treat it as ±30 %. **[verify]** marks a part number, size or listing that must be confirmed before you pay. Web lookups were blocked in this session, so no [est] price was checked against a live cart. Where I was not sure that a SKU exists I give a search string instead.

## 0. How to use this BOM

**Stage codes used in every table.** **S0** is the Stage-0 hand wand (tips §7). **S1** is the Stage-1 rig (freeze §3). **S3** is the gated Stage-3 upgrades (yaw servo, load cell). **BK** is the bench and test kit (TP §L, §Q8). **T** is tools you keep. Rows marked *optional* are listed for completeness and left out of every total. Rows marked *can wait* are in the totals but can be bought later (list in 0.4).

### 0.1 Order groups (carts)

| Order | When | What | Cash (USD) |
|---|---|---|---|
| Cart A, Stage 0 | now | Every S0 row (tips §5 rows except items 4 and 9, PETG spool 1, TPU spool), the BK rows marked "buy with S0" (short real-hair head and clamp, loupe, polyester tape, 10 mm rod, carbon paper, cleaning consumables) and the T rows marked "buy with S0" (kitchen scale 0.1 g, calipers, hex keys, aviation snips, cutters set). Plus a printer or print service if you have neither (row 8.01) | $282.00 (S0 $141.00 + BK $70.00 + T $71.00) |
| Gate | after the Stage-0 build | Stage 0 GO (tips §7.5): the nail reaches skin through your hair at 0.5 N or less, W or B45 beats H by 3 points or more blind, no hair capture in 200 wig strokes. tips §7.4 says to run these tests before any motorised part is ordered | none |
| Cart B, Stage 1 | the day after GO; all carts the same day (CL §10) | Every S1 row, split by vendor in §10. Place the Robotis order first (longest lead time). Then the rest of the bench kit (needed before L1 to L12) and the rest of the tools (soldering iron and insert tip, multimeter, luggage scale, M5 tap, mitre box and saw) | $762.50 (S1) + $170.00 (rest of BK) + $156.00 (rest of T) |
| Cart C, Stage 3 | only if Stage 2 feedback earns it (freeze §3) | Lazy-Susan bearing and load-cell kit. The second XL330 is counted in S3 but I recommend adding it to the Stage-1 Robotis cart: it is the spare for the single most critical part and saves a second shipment | $43.49 |

### 0.2 What to buy first for Stage 0

The wand needs tips items 1, 3, 5, 6, 7 and 10 plus screws, glue and abrasives (tips §9). In this BOM that means rows 5.03, 5.05 to 5.08, 5.10 to 5.17, PETG spool 1 (row 4.01) and the TPU spool (row 4.03, for the seam sleeve on the wand paddle). Print plate A (handle, bars, paddle with the magnet pause at 23.1 mm print height, spare paddle), plate B (tips at 0.10 mm on their sides) and plate C (TPU sleeves) the evening before (tips §7.3). The day-0 tests also need the kitchen scale (practice 0.3 and 0.5 N), the loupe, the 50 µm tape on the 10 mm rod (L9), carbon paper for the loaded-edge mark (tips §7.4), and the short real-hair head on its clamp (L8.1 static reach, L8.9 200 strokes per tip).

### 0.3 What can wait for Stage 3

Rows 6.33 to 6.35: second XL330 (yaw, ID 2), lazy-Susan bearing (mech §5.4: the yaw servo needs a bearing under the plates), 5 kg bar load cell with HX711 (freeze §1.9, mech §7.4). The 40 × 12 mm wrist slot is bridged by the printed filler P47 until then. Total $43.49, inside the freeze's +$27 to $45.

### 0.4 What can wait inside Stage 1 (in the totals, skip in a lean first order)

| Row | Item | Line (USD) | Skip it when |
|---|---|---|---|
| 2.02 | Ballast plates | $45.00 | your arm's printed minimum load is 1.0 kg or less (a light arm) |
| 2.06 | Spare MGN9C block | $8.00 | you accept a few days' downtime if a block loses balls |
| 2.28 | Isolation feet | $10.00 | the face cradle stands on its own stool or table (preferred, mech §10.2) |
| 2.31 | Face cradle cushion (PRONE) | $20.00 | until the first OC (occiput) sessions or neck discomfort in SEAT |
| 5.04 | Tip item 4: Neodymium magnets | $6.00 | L6(b) reads 4 N or more on every tip with the 6 × 2 mm magnets |
| 5.09 | Tip item 9: Nylon picks or sheet | $5.00 | until the Stage-2 E tip and B45 slot mode |
| | **Total that can wait** | **$94.00** | |

### 0.5 Check before ordering

All [verify] items are listed in §9.4. Three of them change what you click: the spring part number (box 2A), the monitor arm's minimum load (row 2.01), and whether a 340 mm X3P cable exists (row 6.18). Print-test P15, P2, P13 and P34 with a leaf scrap before the rest (mech §11). The XL330 cradle P13 and the horn disc P16 depend on XL330 drawing dimensions marked [VERIFY] in mech §5.3, so print those only after the servo has arrived.

## 1. Totals by group and by stage

### 1.1 Group × stage (USD, optional rows excluded, shipping excluded)

| Group | S0 wand | S1 rig | S3 upgrades | BK bench kit | T tools | Total |
|---|---|---|---|---|---|---|
| 2 Structural and mechanical | $0.00 | $359.42 | $0.00 | $0.00 | $0.00 | $359.42 |
| 3 Fasteners and inserts | $0.00 | $110.00 | $0.00 | $0.00 | $0.00 | $110.00 |
| 4 Printing (filament) | $54.00 | $25.00 | $0.00 | $0.00 | $0.00 | $79.00 |
| 5 Tips (tips.md §9) | $87.00 | $11.00 | $0.00 | $0.00 | $0.00 | $98.00 |
| 6 Electronics | $0.00 | $257.08 | $43.49 | $0.00 | $0.00 | $300.57 |
| 7 Bench and test kit | $0.00 | $0.00 | $0.00 | $240.00 | $0.00 | $240.00 |
| 8 Tools (printer excluded) | $0.00 | $0.00 | $0.00 | $0.00 | $227.00 | $227.00 |
| **Total** | **$141.00** | **$762.50** | **$43.49** | **$240.00** | **$227.00** | **$1,413.99** |

Not in the table: optional rows $89.95; estimated shipping $33.00 for the vendors that charge it (Adafruit, Robotis, McMaster, K&J; §10); a 3D printer if you have none (about $300 to $400 [est], or $150 to $250 [est] at a print service for 1.1 kg of PETG). Grand total with shipping, without the printer: **$1,446.99**.

### 1.2 Against the DECISION and freeze targets

| Budget line | Target (document) | This BOM (cash from an empty shop) | Comment |
|---|---|---|---|
| Stage 0 wand | about $30 (freeze §3); about $39 cash if screws, CA, abrasives and a marker are already in the shop (tips §9) | $141.00 S0, plus $70.00 of bench kit and $71.00 of tools bought with it | S0 includes two whole filament spools ($54.00) and full packs of every tip consumable. The wand's marginal parts cost is the tips figure, about $39 |
| Rig (Stage 0 + Stage 1 parts, no bench kit, no tools) | $250 to $300 (DECISION §Why it won, item 6); about $250 (freeze §3 Stage 1) | **$903.50**; lean first order $809.50 (0.4 skipped) | About 3.0 to 3.6 times the target in cash. The named major parts (arm, extrusion and brackets, rail, springs, bearings, magnets, brick, e-stop, button, OpenRB-150, XL330, feeler stock, PETG spool 2) add up to **$249.50**, which is inside the target: the target covers the major parts only. The gap is three things. First, small parts, packs, consumables and spares: $393.00. Second, the face cradle, cushion, isolation feet and ballast: $120.00. Third, the tip set with its filament: $141.00. DECISION does not itemise any of these |
| Stage 3 | +$27 to $45 (freeze §3) | $43.49 | Inside the target |
| Test gear | $45 to $70 (CL indicative budget, test gear) | $240.00 | TP §Q8 asks for two real-hair heads, a wig, IR thermometer, hygrometer, weights and more than CL's list |
| Tools | $150 to $190 from nothing (CL §8) | $227.00 (printer excluded) | Adds the luggage scale, M5 tap, mitre box, snips, stone and polish that mech §12 needs |

**Where to cut if the cash matters.** Already-owned stock decides most of the gap. A screw assortment, heat-set inserts, CA, epoxy, wire and an electronics component kit already on the shelf remove about $90 to $130. Buying a light arm instead of ballast removes $45. A starter electronics component kit (about $15 to $20 [est]) can replace rows 6.19 to 6.23 and the Dupont kit ($40.00 together). Do not cut the spare springs, the spare fuse, the 340 mm DXL cable with its hinge service loop, or anything on the actuator rail: these are safety items (TP K3, mech §4.8).

## 2. Structural and mechanical

**Monitor arm rating needed (mech §3.1 to §3.2).** Moving module 733 g plus fixed adapter parts about 260 g gives 1.0 to 1.1 kg at the VESA plate, with the CoG 49 mm in front of the hinge. The arm must hold this at 350 to 500 mm reach without creeping up. A gas arm below its minimum load creeps (RT2 §4), so ballast to the arm's printed minimum plus 10 %: for a 2 to 9 kg arm, 2.2 kg − 1.1 kg = 1.1 kg of ballast (5 plates). For a 1 to 6.5 kg arm, none. Clamp moment at 450 mm reach with 2.1 kg is 9.3 N·m plus the arm's own 5 to 7 N·m. The desk must be solid, 18 mm or more, and not glass. Pass test: 2 mm drift or less in 30 min (TP K2.14).

| # | Item | Qty | Spec | Unit price (USD) | Line total (USD) | Source | Substitute | Needed by | Stage |
|---|---|---|---|---|---|---|---|---|---|
| 2.01 | Monitor arm | 1 pc | Single gas-spring arm, VESA 75 and 100. Load range minimum 2.0 kg or less. Reach 400 mm or more. VESA centre reachable 300 to 650 mm above the desk. Head tilt ±45° or more, head swivel ±90° or more, lockable rotation. Desk clamp 10 to 85 mm with its steel reinforcement plate. Payload: 1.0 to 1.1 kg module plus adapter, 2.1 to 2.2 kg with ballast. Clamp moment about 9.3 N·m plus the arm's own 5 to 7 N·m, about a third of a 2 to 9 kg arm's design moment | $36.00 [cited] [verify] | $36.00 | HUANUO or VIVO class, about $36 (CL §5.4, https://www.cuttles.io/monitors/arms/clamp). Search: "single monitor arm gas spring VESA 75 4.4 lbs minimum" [verify the printed minimum load and the swivel range on the listing] | Light arm (1 to 6.5 kg range, minimum 1.0 kg or less): needs no ballast, saves row 2.02. A mic boom arm is not acceptable (not stiff enough for 1.1 kg) | mech §3.1, §3.2, §3.4; ADD-1 ruling 8 (Stage 1 yaw by the arm head swivel) | S1 |
| 2.02 | Ballast plates | 5 pcs | 3.0 mm (0.119 in) mild steel, 100 × 100 mm, 4 holes Ø 4.5 mm on a 75 × 75 mm square, 235 g each. Five plates give 1.18 kg in a 15 mm stack, clamped between the arm VESA plate and the adapter, never on the hinged module. Remove plates until the arm holds height (K2.14) | $9.00 [est] | $45.00 | SendCutSend laser cut (CL §5.3 gives about a $29 minimum order [cited]); upload a 100 × 100 mm square with 4 holes | Steel VESA extension plates (Amazon, weigh them) or 1/8 in steel flat bar cut and drilled. Not needed with a light arm | mech §3.2, §12 | S1, can wait |
| 2.03 | 2020 aluminium extrusion | 1 pack (4 × 500 mm) | 2020 European profile, 6 mm slot. Cut 270 mm (elbow-carrier beam), 104 mm (post; ADD-1 D8 says 90 mm, see §9.3) and 80 mm (spine) from one bar: 454 mm plus 3 kerfs fits a 500 mm bar, three bars spare. Tap both carrier-beam ends M5 | $28.00 [cited] | $28.00 | CL §5.1, about $25 to $30 (unverified in CL). Search: "2020 aluminum extrusion 500mm 4 pack" | Misumi HFS5-2020 cut to length with tapped ends [verify option] | mech §5.1, §5.2, §12; ADD-1 D8 | S1 |
| 2.04 | 2020 corner bracket kit | 1 kit (about 40 sets) | Corner brackets with M5 drop-in T-nuts and M5 × 10 mm screws. The rig uses 2 brackets, about 20 T-nuts and 22 screws (§3) | $15.00 [cited] | $15.00 | CL §5.1, $10 to $18, https://www.amazon.com/Aluminum-Extrusion-Connectors-Hardware-Accessories/dp/B0FF9ZBTZJ | Any 2020 kit with drop-in (hammer) M5 T-nuts; these fit both T-slot and V-slot 2020 | mech §5.1, §12, §13 step 17 | S1 |
| 2.05 | MGN9 rail 100 mm with MGN9C block | 1 kit | MGN9 miniature rail, 100 mm long, 9 mm wide, 6.5 mm tall; M3 counterbored holes at 20 mm pitch, 10 mm end distance (holes at 10/30/50/70/90 mm) [verify on the part]. MGN9C short block, 16 g, M3 tapped holes on 15 × 10 mm [verify]. Pull both end seals and wipers, keep the end caps, oil one drop | $12.00 [cited] [verify] | $12.00 | mech §12 and CL §4 (about $12; the CL link https://www.amazon.com/Miniature-Length-Linear-Sliding-Printer/dp/B08HK19M83 is the MGN9H 150 mm listing, not this part). Search: "MGN9C 100mm linear rail" | MGN9H block on the same rail (+10 g; ADD-1 D7 allows it only if the scale shows margin). Never cut a longer hardened rail | mech §6.1, §6.2, §6.5; ADD-1 D7 | S1 |
| 2.06 | Spare MGN9C block | 1 pc | MGN9C block on its plastic retainer, for the same rail. Slide on with the retainer butted to the rail end; a block that loses balls is scrap | $8.00 [est] [verify] | $8.00 | Search: "MGN9C carriage block" [verify it ships on a retainer] | A second rail kit (about $12) | mech §12 (+1 block spare) | S1, can wait |
| 2.07 | Hinge pin set | 1 set | M6 × 80 mm socket-head screw, partially threaded (smooth shank in the Ø 6.3 mm bores), 1 M6 nyloc nut, 2 M6 nylon or PTFE washers about 0.5 mm | $4.00 [est] | $4.00 | Hardware store metric drawer | Amazon M6 × 80 socket head and nylon washers | mech §4.1, §12 | S1 |
| 2.08 | 623ZZ bearings | 1 pack of 10 | 3 × 10 × 4 mm shielded. 2 used in the pulley sheaves P2 on M3 × 16 mm; 1 more is the L8.4 bench pulley (§7) | $7.00 [cited] | $7.00 | CL §4, about $7 per 10 (unverified in CL). Search: "623ZZ bearing 10 pack" | F623ZZ flanged, about $8 per 10 (CL §4) | mech §4.3, §11 P2, §12; ADD-1 D11 | S1 |
| 2.09 | 625-2RS bearing | 1 pack of 10 | 5 × 16 × 5 mm sealed. 1 used in the idler housing P15 (press fit, dot of CA on the outer ring) | $8.00 [est] | $8.00 | Search: "625-2RS bearing 10 pack" | 625ZZ | mech §5.2, §11 P15, §12 | S1 |
| 2.10 | Idler shoulder screw | 2 pcs (1 + 1 spare) | Ø 5 mm × 25 mm shoulder, M4 × 6 mm thread, alloy steel. Its M4 nyloc nut is in §3 | $3.00 [est] [verify] | $6.00 | McMaster metric alloy-steel shoulder screws [verify part number]. Search: "shoulder screw 5 mm shoulder diameter 25 mm shoulder length M4" | Amazon shoulder-bolt assortment with a 5 mm shoulder, or Misumi | mech §5.2, §12 | S1 |
| 2.11 | Dyneema cord | 1 spool (3 m needed) | 1.0 mm braided UHMWPE, about 45 kg (100 lb) break. Uses: 2 hinge cords, the reset cord, and the wrist tether tied as a 25 mm loop (ADD-1 ruling 3, not 60 mm) | $12.00 [est] | $12.00 | Search: "1mm braided UHMWPE line 100 lb" (kite or fishing line) | Braided PE fishing line 80 to 100 lb, doubled if thinner than 0.8 mm | mech §4.3, §4.7, §7.3, §12; ADD-1 ruling 3 and D11 | S1 |
| 2.12 | Trim cord | 1 roll | 0.5 mm clear elastic beading cord (Stretch Magic type), 120 mm loop | $5.00 [est] | $5.00 | Craft store or Amazon | Any 0.5 mm clear elastic cord | mech §6.7, §12 | S1 |
| 2.13 | Hinge lift springs (pinned in box 2A) | 4 pcs (2 + 2 spare), sold as a pack | Extension spring, music wire, zinc plated, machine loop ends. OD 3/8 in (9.5 mm), wire 0.031 in (0.8 mm), length inside hooks 2.50 in (64 mm), rate 0.54 lbf/in (0.095 N/mm; accept 0.45 to 0.66 lbf/in), initial tension 0.22 to 0.45 lbf (1.0 to 2.0 N), max extended length 5.0 in (127 mm) or more, max load 2.2 lbf (10 N) or more. Working 117 mm hook to hook at 6.5 N each; 90 mm and 3.9 N at the 25° up-stop | $10.00 [est] [verify] | $10.00 | McMaster-Carr Precision Extension Springs, family 9654K, part number 9654K___ [verify]: filter https://www.mcmaster.com/9654K/ per box 2A | Amazon or hardware-store 3/8 in OD extension spring, accepted only by the luggage-scale test (6.5 ± 0.5 N at 117 mm, 3.9 ± 0.5 N at 90 mm) | mech §4.3, §4.8, §12, §14; ADD-1 D11 and open item 2 | S1 |
| 2.14 | Spring fallback assortment | 1 assortment | Extension spring assortment; only springs passing the §4.3 bench test are used | $10.00 [cited] | ($10.00) | CL §4, Amazon 200-pc about $10 (unverified in CL) | Hardware-store single extension springs 3/8 in OD | mech §4.3 (Amazon fallback) | S1, optional (not in totals) |
| 2.15 | Holding electromagnet | 1 pc | Adafruit 3872, P20/15, 5 V DC, 0.22 A, 25 N (2.5 kg) on thick steel, Ø 20 × 15 mm, M3 rear thread, 270 mm leads. Wired only on the rail after the hold-to-run (EF §1.6) | $5.95 [est] | $5.95 | https://www.adafruit.com/product/3872 (EF §1.4) | Adafruit 3873 P25/20 (row 2.16) | freeze §1.3; mech §4.4; EF §1.4, §1.6 | S1 |
| 2.16 | Fallback electromagnet | 1 pc | Adafruit 3873, P25/20, 5 V, 50 N. Fit only if the frame unlatches in a run (K4.8, L7); needs a Ø 25 mm seat on the magnet arm | $7.95 [est] | ($7.95) | https://www.adafruit.com/product/3873 (EF §1.4) | Generic 5 V P25/20 module, measured on the luggage scale | mech §4.4; EF §1.4 | S1, optional (not in totals) |
| 2.17 | Keeper plate stock | 1 bar | Mild steel flat bar 1/8 × 1 in (3.2 × 25.4 mm), 12 to 36 in long. Cut one 25 × 25 × 3 mm keeper and flatten it on 400 grit on glass | $8.00 [est] | $8.00 | Hardware store (plain steel flat bar) | Add a 25 × 25 mm square to the SendCutSend ballast order | mech §4.4, §11 P6, §12 | S1 |
| 2.18 | PTFE thread-seal tape | 1 roll | 0.075 mm PTFE tape, one layer on the electromagnet face (stops residual hold) | $2.00 [est] | $2.00 | Hardware store plumbing aisle | Any PTFE plumber's tape | mech §4.4, §12 | S1 |
| 2.19 | Wrist magnet K&J D61 | 3 pcs (1 + 2 spare, one for stack tuning) | 3/8 × 1/16 in N42 disc, 9.4 N rated pull on thick steel, 0.9 g | $0.49 [cited] | $1.47 | https://www.kjmagnetics.com/d61-neodymium-disc-magnet (CL §3) | Amazon 3/8 × 1/16 in N42 discs (no rated pull: measure in L6) | mech §6.5, §7.1, §7.2, §12 | S1 |
| 2.20 | Wrist keeper discs | 2 pcs (buy a pack) | Mild steel disc 12 mm × 1.5 mm, bonded flush in the palm-lid cone | $7.00 [est] [verify] | $7.00 | Search: "12mm x 1.5mm steel disc" [verify thickness on the listing] | Cut from 16 ga (1.5 mm) mild steel sheet; last resort a DIN 125 M6 washer (12 × 1.6 mm), lower pull, re-tune in L6 | mech §6.5, §7.1, §12 | S1 |
| 2.21 | Feeler stock, rig leaves | 2 strips (1 used, 1 spare) | Spring steel 0.30 × 12.7 × 305 mm (0.012 × 1/2 × 12 in). Leaves cut 70 / 67 / 64 mm, corners R 1 mm, edges stoned | $4.00 [cited] [verify] | $8.00 | Precision Brand feeler stock or McMaster feeler-gauge stock [verify part number]; price pro rata from tips §9 ($8 per 2 strips). Search: "feeler stock .012 x 1/2 x 12" | Same size cut from a Precision Brand 0.012 × 1/2 in coil. Width must be 12.7 mm | mech §8.3, §8.6, §12; tips §7, §9 item 6 | S1 |
| 2.22 | M8 slug washers | 20 pcs | DIN 9021 M8 large washer, 8.4 × 24 × 2 mm, about 6.2 g each. Sets: +30 g (5, yellow tape), +60 g (10, red tape); the post holds 16 (100 g) | $0.30 [est] | $6.00 | Hardware store metric drawer | 5/16 in USS fender washers, trimmed to 30.0 / 60.0 ± 0.5 g on the scale | mech §6.6, §12 | S1 |
| 2.23 | Zero pin | 1 pc | Ø 3 mm steel, 30 mm: use the shank of the 3.0 mm bit from the tips drill set (row 5.16) | $0.00 [est] | $0.00 | No purchase | 3 mm dowel pin pack, about $6 | mech §5.3, §13 step 21; ADD-1 ruling 5 | S1 |
| 2.24 | Silicone membrane sheet | 1 sheet (makes 4 boots) | Silicone sheet 0.25 mm, Shore 40A, about 150 × 150 mm, cut with template P35 and bonded slack to each paddle (one shared slot, ADD-1 D4) | $10.00 [est] [verify] | $10.00 | Search: "0.25mm silicone rubber sheet" [verify thickness and hardness on the listing] | 0.2 to 0.3 mm silicone sheet, 30A to 50A | mech §8.7, §12; ADD-1 D4 | S1 |
| 2.25 | Silicone adhesive | 1 tube | Smooth-On Sil-Poxy, 2 mm bead at paddle z 26 to 28 mm, 1 h cure | $14.00 [est] | $14.00 | Search: "Smooth-On Sil-Poxy" | Another RTV adhesive rated for silicone rubber | mech §8.7, §12, §13 step 8 | S1 |
| 2.26 | PTFE film tape 0.05 mm | 1 roll | 0.05 mm PTFE film tape, adhesive backed (3M 5490 class): palm-seam band and one layer over the D61 | $10.00 [est] [verify] | $10.00 | Search: "PTFE film tape 0.05mm" [verify thickness; 3M 5490 itself is thicker] | Any thin PTFE film tape; each extra 0.05 mm layer cuts the wrist hold about 10 % (re-tune L6) | mech §7.1, §8.6, §12 | S1 |
| 2.27 | Rubber bumpers | 1 assortment | Self-adhesive rubber bumpers Ø 10 × 6 mm: 1 up-stop cap (glued), 4 control-panel feet, spares | $6.00 [est] | $6.00 | Search: "self adhesive rubber bumper feet assortment" | Any Ø 10 mm bumper | mech §4.6, §11 P38, §12 | S1 |
| 2.28 | Isolation feet | 4 pcs | Rubber or Sorbothane feet Ø 30 × 15 mm in printed cups P41. Needed only if the face cradle shares the arm's desk | $2.50 [est] | $10.00 | Search: "rubber feet 30mm x 15mm" or "Sorbothane hemisphere 1.25 in" | A separate stool or small table for the cradle (preferred, costs nothing) | mech §10.2, §12; TP §Q7 | S1, can wait |
| 2.29 | Baseboard | 1 pc | 18 mm plywood 350 × 300 mm, only if the cradle shares the desk | $12.00 [est] | ($12.00) | Hardware store project panel | Any 15 to 20 mm board | mech §10.2, §12 | S1, optional (not in totals) |
| 2.30 | Face cradle (SEAT) | 1 pc | Tabletop massage face cradle, horseshoe pad about 280 × 220 mm, adjustable tilt, on its own stand. Forehead load about 15 N over 60 cm² | $45.00 [est] [verify] | $45.00 | Search: "tabletop massage face cradle adjustable" [verify the listing has a stand and tilt] | A massage-chair face-cradle attachment on a separate stool | mech §10.1; TP §M0 | S1 |
| 2.31 | Face cradle cushion (PRONE) | 1 pc | Horseshoe foam face cushion about 300 × 250 × 100 mm, for OC sessions and as the neck-discomfort fallback | $20.00 [est] | $20.00 | Search: "face down pillow massage face cushion" | Folded towels in a U (first OC trials only) | mech §10.1; TP §M0 | S1, can wait |
| 2.32 | Light machine oil | 1 bottle | Sewing-machine oil, one drop on the MGN9C block; weekly re-oil | $4.00 [est] | $4.00 | Hardware store | Any light machine oil | mech §6.2, §12; TP packing list | S1 |
| 2.33 | Medium threadlocker | 1 tube | Loctite 243 class (rail screws, leaf stops) | $6.00 [cited] | $6.00 | CL §8 ($6) | Any blue medium-strength threadlocker | mech §6.1, §8.4, §12 | S1 |

Section 2 subtotal in the totals: **$359.42**; optional rows (in brackets) add $29.95.

### Box 2A. Lift spring, pinned (mech §4.3, ADD-1 D11 and open item 2)

**Order this:** McMaster-Carr Precision Extension Spring, catalogue family **9654K** (zinc-plated music wire, machine loops), **part number 9654K___ [verify]**. I could not reach mcmaster.com from this session, and I am not confident of the exact suffix, so I do not give one. Open https://www.mcmaster.com/9654K/ and filter in this order: material music wire, OD 3/8 in, wire diameter 0.031 in, length 2-1/2 in. Take the row whose rate is nearest 0.54 lbf/in. Then check it against every line of the table below, and write the full part number on the order. Buy 4 (two in use, two spares; mech §4.3). McMaster usually sells these in small packs [verify pack size].

| Parameter | Order value | Acceptance window | Basis |
|---|---|---|---|
| Outside diameter | 0.375 in (9.5 mm) | 0.36 to 0.39 in | spring channels on the P1 rear face (mech §3.3) |
| Wire | 0.031 in (0.8 mm) music wire, zinc plated | 0.029 to 0.035 in | mech §4.3 |
| Length inside hooks (free) | 2.50 in (64 mm) | ≤ 2.50 in; a shorter spring is fine (the cord takes up the difference) | geometry: L0 + (6.5 N − IT)/k ≤ 117 mm, anchor at Z 30 mm to pulley at Z 148 mm (mech §4.3) |
| Rate | 0.54 lbf/in (0.095 N/mm) | 0.45 to 0.66 lbf/in (0.078 to 0.116 N/mm) | the cord shortens 26.8 mm at the 25° up-stop; force there must be 3.9 ± 0.5 N: k = (6.5 − F_up)/26.8 mm |
| Initial tension | 0.34 lbf (1.5 N) | 0.22 to 0.45 lbf (1.0 to 2.0 N) | mech §4.3 |
| Working extension, force | 53 mm (117 mm hook to hook), 1.5 + 0.095 × 53 = **6.5 N** each | 6.5 ± 0.5 N | ADD-1 D11 (13 N total, 0.832 N·m on the 64 mm lever) |
| At the 25° up-stop | 26.2 mm extension (90 mm hook to hook), 1.5 + 0.095 × 26.2 = **4.0 N** (mech table: 3.9 N) | 3.9 ± 0.5 N | holds the frame up with any slug (net +0.13 N·m with +100 g) |
| Maximum extended length | 5.0 in (127 mm) or more | ≥ 125 mm (117 mm working + 8 mm margin), no set | mech §4.3 |
| Maximum load | 2.2 lbf (10 N) or more | ≥ 10 N | mech §4.3 |

Check that a row with these numbers is physically plausible, so you can trust the filter. Use k = G d⁴ / (8 D³ Nₐ) with G = 11.5 × 10⁶ psi, d = 0.031 in and mean diameter D = 0.344 in (spring index 11.1). A rate of 0.54 lbf/in then needs about 60 active coils. That is a 1.9 in body plus two machine loops of about 0.3 in each, so about 2.5 in long, which matches the spec. The Wahl-corrected shear stress is about 48 ksi at 6.5 N and about 75 ksi at 10 N, comfortably below the roughly 135 ksi body limit typical for music wire of this size [est].

**Amazon or hardware-store substitute.** Search "3/8 inch OD extension spring 2.5 inch 0.031 wire". You can also buy the 200-piece assortment (row 2.14, optional) or hardware-store single 3/8 in OD extension springs. Either way, use a spring only if it passes the binding bench test from mech §4.3 and §14. Measure on the luggage scale through the cord after tie-off: 6.5 ± 0.5 N at 117 mm hook to hook and 3.9 ± 0.5 N at 90 mm. Two springs must pass, and the L5 single-spring redundancy check (ADD-1 D11) must still lift the module. The 117 mm and 90 mm figures are for the design spring. For a substitute with a different free length, tie the cord off where the spring reads 6.5 N with the frame latched. Then check 3.9 ± 0.5 N with the frame on its up-stop (the cord is 26.8 mm shorter there). The hook-to-hook length at 6.5 N must be 117 mm or less, or the spring will not fit between the anchor and the pulley.

## 3. Fasteners and inserts

| # | Item | Qty | Spec | Unit price (USD) | Line total (USD) | Source | Substitute | Needed by | Stage |
|---|---|---|---|---|---|---|---|---|---|
| 3.01 | Heat-set inserts M3 | 1 pack of 100 | Brass M3, 4 mm long, for a 4.0 mm printed hole. 55 used (table 3B) | $9.00 [cited] | $9.00 | CL §5.1, $8 to $10 per 100 | One insert assortment kit M2 to M5 (about $15 [est]) replaces rows 3.01 to 3.03 | mech §11, §12, §13 step 3 | S1 |
| 3.02 | Heat-set inserts M2 | 1 pack of 50 | Brass M2, 3 mm long, for a 3.2 mm hole. 18 used (palm tray P32) | $7.00 [est] | $7.00 | Search: "M2 heat set insert 3mm" | Same kit | mech §11 P32, §12 | S1 |
| 3.03 | Heat-set inserts M4 | 1 small pack | Brass M4, 6 mm long. 1 used (up-stop boss in P1) | $6.00 [est] | $6.00 | Search: "M4 heat set insert" | Same kit | mech §4.6, §11 P1 | S1 |
| 3.04 | Metric screw and nut assortment | 1 kit (about 1000 pcs, M3/M4/M5) | Socket-head M3 × 6/8/10/12/16/20, M4 and M5 sizes, hex nuts, flat washers. Covers M3 × 6 (4), M3 × 10 (20), M3 × 12 (4), M3 × 16 to 20 (4), M3 hex jam nuts (3), M3 washers (30, also the 0.12 g weight trims) | $20.00 [cited] | $20.00 | CL §5.1, $15 to $25 | Each M3 length bought separately in 10 or 25 packs | mech §12; table 3A | S1 |
| 3.05 | M3 × 14 socket head | 1 pack of 10 | Steel, 4 used (yaw plates P8 to P9). Rarely in assortments. Check the stack in the CAD: 6 + 6 mm plates may want M3 × 10 or × 12 | $5.00 [est] [verify] | $5.00 | Search: "M3 x 14 socket head cap screw" | McMaster metric socket head M3 × 14 | mech §5.4, §12 | S1 |
| 3.06 | M3 × 6 flat-head (countersunk) | 1 pack of 10 | Steel, 2 used (keeper plate on the keeper lever P6, with epoxy) | $5.00 [est] | $5.00 | Search: "M3 x 6 flat head countersunk" | Epoxy alone plus a button head | mech §11 P6, §12 | S1 |
| 3.07 | Nyloc nut assortment | 1 assortment | M3 (2, pulleys), M4 (1, shoulder screw), M6 (1 hinge spare) | $8.00 [est] | $8.00 | Search: "nylon insert lock nut assortment M3 M4 M5 M6" | Hardware-store singles | mech §4.1, §5.2, §12 | S1 |
| 3.08 | M2 socket-head assortment | 1 kit | M2 × 6 (14: root bars 6, palm lid 6, servo side holes 2), M2 × 8 (10: knuckle plate 6, OpenRB-150 mount 4 [verify hole size]), spares for the XL330 horn screws [verify they ship with the servo] | $9.00 [est] [verify] | $9.00 | Search: "M2 socket head screw assortment" | Hardware-store singles | mech §5.3, §8.6, §8.7, §12; EF §1.4 | S1 |
| 3.09 | Aluminium M3 screw assortment | 1 kit (6/8/10 mm) | Aluminium socket head: 8 × M3 × 8 (6 paddle clamps, 2 riser to seat), 2 × M3 × 10 if the riser-to-seat pair passes the P47 filler (§9.3), 4 × M3 × 6 for the §6.5 mass fallback. Snug only, 0.3 N·m | $9.00 [est] | $9.00 | Search: "aluminum M3 socket head screw assortment" | Nylon M3 for the riser-to-seat pair only | mech §6.5, §8.6, §12 | S1 |
| 3.10 | Nylon M3 screw assortment | 1 kit | Nylon M3 × 10 (3 leaf stops), nylon M3 × 8 (1 weight-cap screw; P29 has its own finger knurl) | $8.00 [est] | $8.00 | Search: "nylon M3 screw assortment" | Nylon M3 thumbscrews | mech §6.6, §8.4, §12 | S1 |
| 3.11 | Knurled M3 × 16 thumbscrews | 1 pack of 10 | Stainless knurled-head M3 × 16, 3 used (down-stop with jam nut, trim cleat, scale lock) | $8.00 [est] | $8.00 | Search: "M3 x 16 knurled thumb screw" | Socket-head M3 × 16 plus a printed knob | mech §6.3, §6.4, §6.7, §12 | S1 |
| 3.12 | M4 screws for VESA, ballast, up-stop | 1 lot | 4 × M4 × 50 socket head with 4 washers (VESA plate plus 15 mm ballast stack), 1 × M4 × 25 (up-stop). With no ballast use M4 × 16 to 20 (often supplied with the arm) | $5.00 [est] | $5.00 | Hardware store metric drawer | Amazon singles | mech §3.2, §4.6, §12 | S1 |
| 3.13 | M5 × 12 and M5 × 16 socket head | 10 of each | Steel, for printed nodes the kit's M5 × 10 may not reach through (keeper lever P6 and cord bar P7 are 12 mm parts) [verify against the CAD] | $6.00 [est] [verify] | $6.00 | Hardware store or Amazon | Longer screws if the bracket kit has them | mech §11 P5 to P12 (BOM addition) | S1 |
| 3.14 | Wood screws #4 × 1/2 in | 8 pcs | For the 4 foot cups P41 on the baseboard (2 each) | $3.00 [est] | ($3.00) | Hardware store | M3 × 12 wood screws | mech §10.2, §12 | S1, optional (not in totals) |
| 3.15 | Zip ties | 1 pack (100) | 100 mm and 200 mm. Cable anchors at the hinge, carrier beam and handle; P36 clip slots | $5.00 [est] | $5.00 | Search: "zip ties assorted" | Hook-and-loop ties | EF §1.3, §1.6; mech §3.3 | S1 |

Section 3 subtotal in the totals: **$110.00**; optional rows (in brackets) add $3.00.

### 3A. Every fastener, summed across mech §11, §12, tips and EF

| Size | Count used | Where (mech unless stated) | Bought in row |
|---|---|---|---|
| M2 × 6 socket head | 14 | root clamp bars 6, palm lid 6 (§8.6), XL330 side holes 2 (§5.3) | 3.08 |
| M2 × 8 socket head | 10 | knuckle plate 6 (§8.7), OpenRB-150 to tray bosses 4 (BOM addition, [verify] hole size) | 3.08 |
| M2 horn screws | 4 | P16 horn disc to XL330 horn: the servo's own screws (§5.3) [verify supplied] | XL330 box; spares 3.08 |
| M3 × 6 socket head, steel | 4 | riser P26 to MGN9C block (§6.2; never longer than 6 mm) | 3.04 |
| M3 × 6 socket head, aluminium | 4 | §6.5 mass fallback for the 4 carriage screws | 3.09 |
| M3 × 6 flat head | 2 | keeper plate on P6 | 3.06 |
| M3 × 8 socket head, steel | 28 | rail 5, mast parts 8, magnet rear 1, tray lid and panel lid 6 (§12); wand handle bar 4, wand paddle bar 2, spare wand paddle 2 (tips §7.1) | 5.11 (50-pack) |
| M3 × 8 socket head, aluminium | 8 | paddle clamp bars 6 (§8.6), riser arm to upper seat 2 (§6.5) | 3.09 |
| M3 × 10 socket head, steel | 20 | cheek A 4, servo strap 2, idler housing 2, P47 filler 2 (§12); plus BOM additions not in §12: tray P3 to adapter P1 4, servo cradle P13 to drop leg P11 4, reset-cord guide P45 2 with nuts [verify] | 3.04 |
| M3 × 10 nylon | 3 | leaf stop screws (§8.4) | 3.10 |
| M3 × 8 nylon | 1 | weight cap P29 (§6.6) | 3.10 |
| M3 × 12 socket head | 4 | crossbar to cheeks (§6.1) | 3.04 |
| M3 × 14 socket head | 4 | yaw plates P9 to P8 (§5.4) [verify length] | 3.05 |
| M3 × 16 socket head | 4 | pulley axles 2 (§3.3), hold-to-run housing P39 to P40 2 (BOM addition, M3 × 16 to 20 [verify]) | 3.04 |
| M3 × 16 knurled thumbscrew | 3 | down-stop, trim cleat, scale lock (§6.3, §6.4, §6.7) | 3.11 |
| M3 nyloc nut | 2 | pulley axles | 3.07 |
| M3 hex nut | 3 + 2 | jam nuts on the thumbscrews; P45 guide nuts | 3.04 |
| M3 washer | 30 | magnet depth shims (0.5 mm each = 0.6 mm at the nails), weight trims (0.12 g each) | 3.04 |
| M4 × 50 socket head + washer | 4 + 4 | VESA plate plus ballast stack (§3.2) | 3.12 |
| M4 × 25 socket head | 1 | up-stop with rubber cap (§4.6) | 3.12 |
| M4 nyloc nut | 1 | shoulder screw (§5.2) | 3.07 |
| Shoulder screw Ø 5 × 25 mm, M4 | 1 (+1) | idler (§5.2) | 2.10 |
| M5 × 10 socket head | 22 | 2020 end taps 2, T-nut joints 20 (§12) | 2.04 kit |
| M5 drop-in T-nut | 20 | drop legs 4, keeper lever 2, cord bar 2, yaw plates 4, corner brackets 4, hinge knuckle 2, spare 2 | 2.04 kit |
| M5 × 12 / × 16 | as needed | printed nodes thicker than M5 × 10 reaches [verify against CAD] | 3.13 |
| 2020 corner bracket | 2 | post to spine (§13 step 17) | 2.04 kit |
| M6 × 80 socket head + nyloc + 2 nylon washers | 1 set | hinge pin (§4.1) | 2.07 |
| #4 × 1/2 in wood screw | 8 | foot cups P41 on the baseboard (only with the baseboard) | 3.14 (optional) |

### 3B. Heat-set inserts by size (mech §11, brass; M3: 4.0 mm hole, 4 mm long; M2: 3.2 mm hole, 3 mm long)

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

Paddles and the wand use 2.6 mm thread-forming holes for their M3 × 8 clamp screws (tips §8). Inserts are optional there (4.0 mm hole), and every insert needed beyond 55 M3 is covered by the 100-pack.

**Fastener kit alternative.** One 1000-piece M3/M4/M5 socket-head assortment (row 3.04) plus one M2 assortment (row 3.08) and one M2 to M5 insert kit covers about 90 % of the counts above. Buy separately in any case: M3 × 14, aluminium and nylon M3, knurled thumbscrews, M3 × 6 flat heads, nylocs, M4 × 50, M4 × 25, M6 × 80 and the shoulder screw. Most assortments do not contain them.

## 4. Printing

| Material | Need from the documents | With 30 % waste | Buy | Notes |
|---|---|---|---|---|
| PETG | 900 g (mech §11, 60 pieces) + 120 g (tips §9 item 1: tips, carriers, paddles, bars, handle) + 30 g (tip box, tips §9 item 18) = 1,050 g | 1,365 g | 2 × 1 kg spools (rows 4.01, 4.02) | leaves about 635 g for the [VERIFY] reprints (P13, P16) and the fit tests |
| TPU 90A | 20 g (mech §11: pads, bumpers) + 10 g (tips §9 item 2: seam sleeves × 4, E pads × 2) = 30 g | 39 g | 1 small spool (row 4.03) | 90A, not 95A, for the sleeves |
| Resin | none | none | none | tips §5.1: standard SLA resin is banned at the scalp (red line 9). In SP1 it is at most an optional geometry master |
| PLA | none required | none | none | allowed only for the wand handle (tips §5.1); never near skin |

| # | Item | Qty | Spec | Unit price (USD) | Line total (USD) | Source | Substitute | Needed by | Stage |
|---|---|---|---|---|---|---|---|---|---|
| 4.01 | PETG filament, spool 1 (bright colour) | 1 kg | 1.75 mm, orange or yellow: tips must be one bright colour (visible in dark hair, identical across tips for blinding). Stage 0 uses about 150 g (tips, paddles, bars, wand, tip box); the rest goes to the hand and float parts | $25.00 [cited] | $25.00 | Pro rata $25 per kg from tips §9 item 1. Search: "PETG 1.75 1kg orange" | Any PETG; never PLA near skin (tips §5.1, mech §11) | tips §5.1, §9 items 1 and 18; mech §11; CL §5.2 | S0 |
| 4.02 | PETG filament, spool 2 | 1 kg | 1.75 mm, any colour: frame nodes, adapter, yoke, guards, boxes | $25.00 [cited] | $25.00 | Pro rata from tips §9 | Same | mech §11 (0.9 kg PETG) | S1 |
| 4.03 | TPU 90A filament | 1 small spool | 1.75 mm, Shore 90A (for example Polymaker PolyFlex TPU90): seam sleeves (4 plus spares), E pads, servo-stop bumpers, up-stop pad, wedge pads. 30 g used | $29.00 [cited] | $29.00 | tips §9 item 2 ($29 if not owned) | TPU 95A for bumpers and pads only; the sleeves need 90A to stretch over the nose | tips §5.2, §9 item 2; mech §11 (20 g TPU) | S0 |

Section 4 subtotal in the totals: **$79.00**.

**Nozzle, bed and process notes.** Use a 0.4 mm nozzle (brass is fine: no abrasive filaments). The bed must be 220 × 220 mm or larger, because the P21 crossbar lies 196 × 108 mm on the bed (mech §11) and does not fit a 180 mm bed. P32 and P33 are 169 mm long. For PETG use a textured PEI sheet, or glue stick as a release layer on smooth PEI; PETG can tear a smooth sheet. TPU 90A needs a direct-drive extruder at 15 to 20 mm/s (tips §5.2).

Tips: print W, B45 and B45-12 on their sides at 0.10 mm layers, 3 perimeters, 100 % infill, all in one bright colour (tips §5.1 and README §3). Paddles: pause at 23.1 mm print height for the N52 magnet, with a dot of CA so it cannot jump to the nozzle (tips §2.2). Knuckle plate P30: print the underside as the top surface at 0.12 mm with ironing, then sand 400 and buff (mech §11). Float parts P26 to P34: 2 to 4 perimeters with the low infill listed in mech §11, and weigh every part as it comes off against the 92 g budget (mech §6.5, §13 step 1).

Heat-set inserts go in at 220 to 230 °C, square to the surface (mech §13 step 3). Dry PETG and TPU if they string. Never print a scalp part in PLA.

## 5. Tips (tips.md §9, verbatim totals)

tips §9 reads: "The tip subsystem costs about **$103** with filament costed pro rata, about **$132** if a TPU 90A spool has to be bought. The Stage-0 wand alone needs items 1, 3, 5, 6, 7 and 10 plus screws, glue and abrasives: about **$39** cash if screws, CA, abrasives and a marker are already in the shop, against the DESIGN-FREEZE estimate of about $30." Its test kit (10× loupe $8, 50 µm polyester tape $6, 10 mm rod $2, kitchen scale) is not in that total; in this BOM it sits in §7 and §8.

In this BOM, tips items 1, 2 and 18 are bought as whole spools in §4, so they carry $0 here; the other 15 items total $98, as in tips §9. Items 11, 12, 13 and 16 also serve the rig: the M3 × 8 pack covers the 20 rig steel M3 × 8, the CA and epoxy cover the mech keeper bonds, and the 3.0 mm drill shank is the servo zero pin. They are not bought twice. The rig leaves are on row 2.21, not here.

| # | Item | Qty | Spec | Unit price (USD) | Line total (USD) | Source | Substitute | Needed by | Stage |
|---|---|---|---|---|---|---|---|---|---|
| 5.01 | Tip item 1: PETG filament, one bright colour | 120 g | 1.75 mm; about 120 g used | $0.00 [cited] | $0.00 | tips §9 item 1 ($3); bought as §4 spool 1, $0 here | see §4 | tips §9 item 1: all tips, carriers, paddles, bars, handle | S0 |
| 5.02 | Tip item 2: TPU 90A filament | 10 g | 1.75 mm; about 10 g used | $0.00 [cited] | $0.00 | tips §9 item 2 ($1); bought as §4 TPU spool, $0 here | see §4 | tips §9 item 2: seam sleeves x 4, E pads x 2 | S0 |
| 5.03 | Tip item 3: Neodymium magnets | 50 pack | N52, 6 x 2 mm disc, axial | $9.00 [cited] | $9.00 | tips §9 item 3 ($9) | 6 × 2 mm N52 discs from any magnet seller | tips §9 item 3: one per pocket | S0 |
| 5.04 | Tip item 4: Neodymium magnets | 20 pack | N52, 6 x 3 mm disc, axial | $6.00 [cited] | $6.00 | tips §9 item 4 ($6) | one 0.1 mm tape layer on the slug for the opposite case (tips §2.3) | tips §9 item 4: breakaway tuning (§2.3) | S1, can wait |
| 5.05 | Tip item 5: Steel keeper discs | 50 pack | mild steel 6 x 1 mm (or 1 mm sheet 100 x 100 mm) | $7.00 [cited] | $7.00 | tips §9 item 5 ($7) | 6.0 × 3.9 × 1.0 mm slugs cut from 1 mm mild steel sheet | tips §9 item 5: tang keepers, flats filed to 3.9 mm | S0 |
| 5.06 | Tip item 6: Feeler stock | 2 strips | spring steel 0.30 x 12.7 x 305 mm (0.012 x 1/2 x 12 in) | $8.00 [cited] | $8.00 | tips §9 item 6 ($8) | see row 2.21 | tips §9 item 6: wand leaf and spares (rig leaves on the mech BOM) | S0 |
| 5.07 | Tip item 7: Press-on nails | 1 box | ABS full cover, sizes 0 to 3, 100 or more | $7.00 [cited] | $7.00 | tips §9 item 7 ($7) | single nail only after the A45 gate | tips §9 item 7: P tips (two nested per tip) | S0 |
| 5.08 | Tip item 8: Nylon picks | 12 pack | Dunlop nylon 0.88 mm | $5.00 [cited] | $5.00 | tips §9 item 8 ($5) | 0.8 mm nylon 6/6 sheet | tips §9 item 8: A45 blades | S0 |
| 5.09 | Tip item 9: Nylon picks or sheet | 12 pack | Dunlop nylon 1.0 mm, or nylon 6/6 sheet 1.0 mm | $5.00 [cited] | $5.00 | tips §9 item 9 ($5) | 1.0 mm nylon 6/6 sheet | tips §9 item 9: E blades, B45 slot blades | S1, can wait |
| 5.10 | Tip item 10: Steel balls | 100 pack | G25 chrome steel, 3.0 mm | $5.00 [cited] | $5.00 | tips §9 item 10 ($5) | PRINTED_BALL = true (tips §4.6) | tips §9 item 10: H tips | S0 |
| 5.11 | Tip item 11: Screws | 50 pack | M3 x 8 socket or button head | $5.00 [cited] | $5.00 | tips §9 item 11 ($5) | button head M3 × 8 | tips §9 item 11: wand bar 4, paddle bars 2 each; BOM: also the 20 rig M3 × 8 steel screws | S0 |
| 5.12 | Tip item 12: Cyanoacrylate | 2 | thin and gel, 20 g each | $8.00 [cited] | $8.00 | tips §9 item 12 ($8) | any thin and gel CA | tips §9 item 12: blades, nails, balls, sleeve rim; BOM: also the mech gel CA | S0 |
| 5.13 | Tip item 13: Epoxy | 1 | 5-minute, twin syringe | $6.00 [cited] | $6.00 | tips §9 item 13 ($6) | gel CA | tips §9 item 13: keepers, P fill (alternative); BOM: also the keeper plate and wrist disc | S0 |
| 5.14 | Tip item 14: Abrasive paper | 1 sheet each | wet-and-dry 400, 600, 1000, 2000 grit | $8.00 [cited] | $8.00 | tips §9 item 14 ($8) | automotive wet-and-dry | tips §9 item 14: edge radius (§6) | S0 |
| 5.15 | Tip item 15: Nail files and buffer | 1 set | 180 / 240 file, 3-way buffer block | $4.00 [cited] | $4.00 | tips §9 item 15 ($4) | drugstore nail kit | tips §9 item 15: plan corners, P trimming | S0 |
| 5.16 | Tip item 16: Drill-bit set | 1 | 0.5 to 3.0 mm by 0.1 mm | $10.00 [cited] | $10.00 | tips §9 item 16 ($10) | loose 0.6, 0.8, 1.0 and 3.0 mm bits | tips §9 item 16: radius reference shanks (0.6, 0.8, 1.0 mm); BOM: the 3.0 mm shank is the servo zero pin | S0 |
| 5.17 | Tip item 17: Marker and varnish | 1 each | 0.3 mm permanent marker, clear nail varnish | $5.00 [cited] | $5.00 | tips §9 item 17 ($5) | none: no stickers (tips README §5) | tips §9 item 17: blinding codes | S0 |
| 5.18 | Tip item 18: Tip box | 1 | printed block (30 g PETG) or pill organiser with foam | $0.00 [cited] | $0.00 | tips §9 item 18 ($1); printed from §4 spool 1, $0 here | pill organiser with cut foam | tips §9 item 18: coded tip storage | S0 |

Section 5 subtotal in the totals: **$98.00**.

**Blinding-code labels (TP §Q5, tips README §5).** No stickers or printed labels: the pocket has only 0.15 mm of clearance per side. Write a random two-letter code on the tang's plain −Y face with the 0.3 mm permanent marker, then one thin coat of clear nail varnish (row 5.17). Draw the letters from an alphabet without W, B, A, E, H and P, and never reuse a code. Make two copies of every tip compared blind (at least W, B45, H, A45, P), each with its own code; the filament for them is inside the 120 g. The key card (tip ID, print batch, measured radius, tape-test result, date) stays with the helper or in a sealed envelope.

**Tip box.** Print it (30 g PETG, row 5.18 at $0 because it comes from spool 1) with one slot per tip, about 11 × 5 × 14 mm deep, each labelled only with its code. A pill organiser with a cut foam insert also works. Do not also print mech P48: it is listed only for the case where the tip lead supplies no box, and tips §9 supplies one.

## 6. Electronics

Every row of EF §1.4 appears below, in its order, plus the wire, heat-shrink, Wago, Dupont, perfboard, USB-C, fuse and spare-fuse lines. The electromagnet is priced once, in §2 (row 2.15). Fuse rule (EF §1.6): 1 A fast-blow, 5 × 20 mm, F1AL250V, in the rail at the adapter. Running current is about 0.6 A; a stalled XL330 at 1.47 A opens it. If 1 A nuisance-trips at bring-up, 1.25 A fast is the only permitted step up. One spare fuse lives in the kit (TP K3.7, §Q4).

| # | Item | Qty | Spec | Unit price (USD) | Line total (USD) | Source | Substitute | Needed by | Stage |
|---|---|---|---|---|---|---|---|---|---|
| 6.01 | 5 V 4 A power adapter | 1 pc | Adafruit 1466: 5 V 4 A, UL-listed, 100 to 240 V in, 5.5 × 2.1 mm centre-positive, 20 W. ADD-1 ruling 7: this brick plus 22 AWG rail wire keeps the drop under 0.2 V at 0.6 A | $14.95 [est] | $14.95 | https://www.adafruit.com/product/1466 (EF §1.4; CL §6.3 gives about $15 to $24 [cited]) | Same part at Jameco https://www.jameco.com/z/1466-Adafruit-Industries-5V-4A-4000Ma-Switching-Power-Supply-UL-Listed_2505471.html, or a Mean Well GST25A05 5 V 4 A UL brick [verify] | EF §1.1, §1.4, §1.6; ADD-1 ruling 7; TP K3.1 | S1 |
| 6.02 | DC jack to screw-terminal adapter | 1 pc | 5.5 × 2.1 mm female jack to 2-pin screw terminal | $2.00 [est] | $2.00 | Adafruit 368 (EF §1.4) | Generic Amazon pack | EF §1.3 row 1, §1.4 | S1 |
| 6.03 | Fuses 1 A fast-blow 5 × 20 mm | 1 pack of 10 | F1AL250V glass: one fitted, one spare taped inside the tray lid (TP K3.7, §Q4). Running current about 0.6 A; a stalled XL330 (1.47 A) opens it | $5.00 [est] | $5.00 | Search: "F1AL250V 5x20 fuse" | Bussmann GMA-1A | EF §1.3 row 2, §1.6; TP K3.7, §Q4 | S1 |
| 6.04 | Inline fuse holder | 1 pc (pack) | Screw-type inline holder for 5 × 20 mm fuses, 18 AWG leads | $7.00 [est] | $7.00 | https://www.amazon.com/uxcell-Inline-Screw-Holder-Gauge/dp/B07SM5KYZ7 (EF §1.4) | Panel 5 × 20 holder in the tray | EF §1.4, §1.6 | S1 |
| 6.05 | Fuses 1.25 A fast 5 × 20 mm | 1 pack | Only permitted step up if 1 A nuisance-trips at bring-up; note it on the diagram | $5.00 [est] | ($5.00) | Search: "1.25A fast blow 5x20" | None (never higher) | EF §1.6 | S1, optional (not in totals) |
| 6.06 | E-stop, boxed | 1 pc | 22 mm NC mushroom, latching (push-lock, twist-release), 10 A, boxed for desk use; second NC contact unused | $14.00 [cited] | $14.00 | https://www.amazon.com/TWTADE-Mushroom-Emergency-Warranty-YW1B-V4E02R-BOX/dp/B07NNZB41H (EF §1.4; CL §6.3, $8 to $14) | APIELE 1NC LA139A-ES542 panel mount https://www.amazon.com/APIELE-Emergency-Stop-Button-Switch/dp/B0F2F8TYMY in a printed box | EF §1.3 rows 3 to 4, §1.4; TP K3.5, §Q4 | S1 |
| 6.07 | E-stop weighted base | 1 plate | Steel plate about 100 × 100 × 3 mm or heavier; screw the e-stop box to it | $9.00 [est] | $9.00 | A 6th plate in the SendCutSend ballast order | Steel mending plate or any 0.5 kg steel object | EF §1.6, §7; TP §Q4 | S1 |
| 6.08 | Hold-to-run button | 1 pc (pack) | uxcell 30 mm momentary arcade push button, N.O. microswitch, 3 A 250 V, snap-in. Housing P39 deck hole Ø 29.6 mm [verify against the button] | $8.00 [est] [verify] | $8.00 | https://www.amazon.com/uxcell-Mounting-Momentary-Button-Switch/dp/B08HH78XMH (EF §1.4) [verify pack size] | Philmore 30-825 (row 6.11) | EF §1.4, §7; mech §11 P39 | S1 |
| 6.09 | Hold-to-run cable | 1 spool (1.5 m used) | 2-core 22 AWG stranded, 1.5 m, through the printed gland and zip-tie anchor | $9.00 [est] | $9.00 | Search: "22 AWG 2 conductor stranded wire 25 ft" | Two 22 AWG silicone wires twisted and sleeved | EF §1.3 row 4, §7; TP §Q4 | S1 |
| 6.10 | Hold-to-run housing | 1 set | Printed PETG handle Ø 36 × 110 mm (P39, P40), button face 3 mm below the rim; screws in §3 | $0.00 [cited] | $0.00 | Printed (§4) | Row 6.11 | EF §1.4; mech §11 P39, P40 | S1 |
| 6.11 | Hold-to-run, bought alternative | 1 pc | Philmore 30-825 hand-held momentary N.O. SPST, 3 A 125 V, die-cast body; extend its cord to 1.5 m | $10.00 [est] | ($10.00) | https://www.amazon.com/Hand-Held-Button-Switch-30-825/dp/B00T6RCGNC (EF §1.4) | Printed housing | EF §1.4 | S1, optional (not in totals) |
| 6.12 | Electromagnet | see row 2.15 | Adafruit 3872 P20/15, listed and priced in §2 | $0.00 [est] | $0.00 | Row 2.15 | Row 2.16 | EF §1.4 | S1 |
| 6.13 | Flyback diode | 1 pack | 1N5819 Schottky 40 V 1 A across the coil, band to + | $5.00 [est] | $5.00 | Any distributor (EF §1.4) | 1N5817 or 1N5822 | EF §1.3 row 8, §1.6 | S1 |
| 6.14 | Bulk capacitor | 1 pack | 470 µF electrolytic, 10 V or higher, at the OpenRB terminal | $5.00 [est] | $5.00 | Any distributor (EF §1.4) | 470 to 1000 µF, 16 V | EF §1.3 row 7, §1.6 | S1 |
| 6.15 | TVS diode | 1 pack | SMAJ5.0A (SMD, DO-214AC) across + and − at the terminal; solder onto perfboard pads | $6.00 [est] [verify] | $6.00 | Any distributor (EF §1.4) | Through-hole SA5.0A (DO-15) [verify] | EF §1.3 row 7, §1.6 | S1 |
| 6.16 | OpenRB-150 controller | 1 pc | SAMD21G18A, 4 DXL TTL ports, FET-switched DXL power, USB-C, terminal block supplied. Jumper on VIN(DXL), never USB(5V). Tray pocket about 66 × 25 mm [verify outline] | $28.64 [cited] | $28.64 | https://www.robotis.us/openrb-150/ (CL §6.1, $24.90 to $28.64); manual https://emanual.robotis.com/docs/en/parts/controller/openrb-150/ | See §9 | EF §1, §2; mech §11 P3 | S1 |
| 6.17 | Dynamixel XL330-M288-T (elbow) | 1 pc | 5 V (3.7 to 6.0 V), 0.52 N·m stall at 1.47 A, 18 g, 4096 ticks per rev, protocol 2.0, ID 1. Ships with a horn and a short X3P cable [verify contents] | $27.49 [cited] | $27.49 | https://www.robotis.us/dynamixel-xl330-m288-t/ (CL §1.2) | See §9 | EF §1.4, §4; mech §5.3 | S1 |
| 6.18 | DXL cable 340 mm or longer | 1 pc (pack) | ROBOTIS X3P cable (JST-EH 3-pin, 2.5 mm pitch), 340 mm or longer: the tray-to-servo run is about 330 mm including the 60 mm service loop at the hinge; the stock 180 mm cable is too short | $8.00 [est] [verify] | $8.00 | Search robotis.us: "Robot Cable-X3P" [verify a 340 mm or longer length exists] | Make one with JST-EH 3-pin housings and crimps (22 to 26 AWG) and a crimper (row 8.19) | mech §3.3; EF §1.3 row 12 | S1 |
| 6.19 | Potentiometers 10 kΩ linear with knobs | 1 pack | 2 used (SPEED, VARIATION), 7 mm bushing for the Ø 7.2 mm panel holes; tape marks at 0/50/100 % | $8.00 [est] | $8.00 | CL §6.3 ($1 to $2 each). Search: "B10K potentiometer with knob" | Alpha 9 mm pots | EF §1.2, §1.3 rows 13 to 14; mech §11 P37 | S1 |
| 6.20 | Toggle switch | 1 pack | SPST (or SPDT used as SPST), 6 mm bushing for the Ø 6.2 mm hole: PERIODIC/HUMAN on D4 | $7.00 [est] | $7.00 | Search: "mini toggle switch 6mm" | Any panel toggle with a 6 mm bushing | EF §1.3 row 15; mech §11 P37 | S1 |
| 6.21 | Status LED | 1 pack | 5 mm LED for the Ø 5.2 mm hole, on D5 | $5.00 [est] | $5.00 | Search: "5mm LED assortment" | Any 5 mm LED | EF §1.3 row 16 | S1 |
| 6.22 | Resistor assortment | 1 kit | 1/4 W: 330 Ω (LED), 2 × 10 kΩ (rail-sense divider to A2) | $7.00 [est] | $7.00 | Search: "resistor kit 1/4W" | Singles | EF §1.2, §1.3 rows 9, 16 | S1 |
| 6.23 | Ceramic capacitors 100 nF | 1 pack | 100 nF from A2 to GND (divider filter) | $5.00 [est] | $5.00 | Search: "100nF ceramic capacitor" | Capacitor assortment | EF §1.3 row 9 | S1 |
| 6.24 | 22 AWG silicone wire | 1 kit (6 colours) | Rail wiring, red and black, the whole rail | $12.00 [cited] | $12.00 | CL §6.3 (about $12) | PVC hook-up wire 22 AWG | EF §1.3 rows 2 to 11; ADD-1 ruling 7 | S1 |
| 6.25 | 6-core 26 AWG cable | 1 length (1.0 m used) | Control panel P37 to tray: 3V3, GND, A0, A1, D4, D5 | $9.00 [est] | $9.00 | Search: "6 conductor 26 AWG cable" | Ribbon cable with Dupont ends | mech §3.3; EF §1.3 rows 13 to 16 | S1 |
| 6.26 | Heat-shrink assortment | 1 kit | Magnet lead splices and terminations | $6.00 [cited] | $6.00 | CL §6.3 (about $6) | Any assortment | EF §1.3 rows 8, 11 | S1 |
| 6.27 | Braided sleeving | 2 m | 6 mm expandable PET sleeve on the DXL cable across the hinge | $7.00 [est] | $7.00 | Search: "braided cable sleeve 6mm" | Spiral wrap | EF §1.3 (wire crossing a moving joint) | S1 |
| 6.28 | Wago 221-413 lever connectors | 1 pack | 3-way lever splice for the rail + node (and a − node), inside a printed cover | $9.00 [est] | $9.00 | Search: "Wago 221-413" | Screw terminal block | EF §1.3 row 6; mech §11 P3 | S1 |
| 6.29 | Dupont kit | 1 kit | Housings, crimp pins and jumpers: pots, toggle, LED, HX711 header | $8.00 [cited] | $8.00 | CL §6.3 (about $8) | Pre-crimped female jumper wires | EF §1.3 rows 13 to 17 | S1 |
| 6.30 | Perfboard | 1 pack | Rail board 30 × 20 mm (divider, TVS, 470 µF) plus spares | $7.00 [est] | $7.00 | Search: "perfboard prototype board" | Stripboard | EF §1.3 row 9; mech §3.3 | S1 |
| 6.31 | USB-C cable | 1 pc | Data-capable USB-C, 2 m: OpenRB logic power and serial; tie-wrapped down the arm | $8.00 [est] | $8.00 | Search: "USB C data cable 2m" | Any data USB-C (not charge-only) | EF §1.3 row 18; mech §3.3 | S1 |
| 6.32 | Insulated crimp terminals | 1 assortment | Fork terminals (e-stop block), 4.8 mm female spades (microswitch) | $10.00 [est] | $10.00 | Search: "insulated crimp terminal assortment" | Solder and heat-shrink | EF §1.3 rows 3 to 5 | S1 |
| 6.33 | Dynamixel XL330-M288-T (spare, Stage 3 yaw) | 1 pc | Second servo, ID 2. Recommended in the Stage 1 Robotis cart: it covers the elbow servo as a single point of failure and becomes the Stage 3 yaw servo | $27.49 [cited] | $27.49 | https://www.robotis.us/dynamixel-xl330-m288-t/ (CL §1.2) | XL330-M077-T (§9) | freeze §3 Stage 3; EF §1.3 row 12 | S3 |
| 6.34 | Lazy-Susan bearing ring | 1 pc | About 100 mm ring under the yaw plates, for the Stage 3 yaw servo (a 270 mm, 0.5 kg carrier on one horn repeats the RT2 §4 side-load problem) | $6.00 [est] | $6.00 | Search: "lazy susan bearing 4 inch" | Printed thrust ring with 6 mm balls | mech §5.4, §15.1 item 12 | S3 |
| 6.35 | Bar load cell 5 kg with HX711 | 1 kit | 5 kg bar cell for the 40 × 12 mm wrist slot (a 1 kg cell is destroyed by a 20 N push) [verify that a 40 mm long 5 kg cell exists: common 5 kg cells are about 80 mm long]; HX711 on D2/D3 | $10.00 [cited] [verify] | $10.00 | CL §7 ($8 to $12 kit); HX711 alone $4.95 https://www.sparkfun.com/products/13879 | SparkFun HX711 plus a separate cell | freeze §1.9, §3; mech §7.4; EF §1.3 row 17 | S3 |

Section 6 subtotal in the totals: **$300.57**; optional rows (in brackets) add $15.00.

**Safety-critical: do not substitute casually.** The brick must be UL-listed, 5 V regulated (no LiPo, no unregulated wall wart). The e-stop must be NC and latching. The hold-to-run must be momentary NO. The electromagnet must hang on the rail after the hold-to-run and nowhere else (EF §1.6). The OpenRB jumper must be on VIN(DXL): bench test B3 is a hard gate.

## 7. Bench and test kit (TP §Q8 and §L)

TP §Q8 asks for: real-hair training heads (one trimmed 3 to 5 cm, one long), a Kanekalon wig, a 180 mm sphere or hairless foam head, 100 µm monofilament, 50 µm tape, 15/50/100 g tether weights and a pulley, carbon paper, foam ear plugs, black cloth, a lint roller, an IR thermometer, a hygrometer, a loupe, hair clips and a hand mirror. TP §L adds a 0 to 5 N scale, a steel ruler, the phone (240 fps, SPL meter, inclinometer and timer apps, all free) and the kitchen scale (row 8.06). K5.1 adds safety glasses. The packing list adds IPA, tweezers and a comb.

| # | Item | Qty | Spec | Unit price (USD) | Line total (USD) | Source | Substitute | Needed by | Stage |
|---|---|---|---|---|---|---|---|---|---|
| 7.01 | Real-hair training head, short | 1 pc | Cosmetology mannequin head, 100 % human hair; trim it to 3 to 5 cm yourself | $32.00 [cited] | $32.00 | CL §7, $28 to $36 (https://www.amazon.com/wig-heads/s?k=wig+heads) | Human-hair wig on the foam head | TP §L8, §Q8; tips §7.4 (Stage 0 wig tests L8.1, L8.9) | BK, buy with S0 |
| 7.02 | Real-hair training head, long | 1 pc | Same, left long | $32.00 [cited] | $32.00 | CL §7 | Human-hair wig, $65 to $100 (CL §7) | TP §L8, §Q8 | BK |
| 7.03 | Mannequin table clamp | 1 pc | Table clamp for the training heads | $8.00 [cited] | $8.00 | CL §7 (about $8) | C-clamp and a dowel | TP §L8 | BK, buy with S0 |
| 7.04 | Kanekalon synthetic wig | 1 pc | Long synthetic wig in Kanekalon fibre: the conservative wrap screen | $18.00 [est] [verify] | $18.00 | Search: "Kanekalon synthetic wig long" [verify the fibre on the listing] | Any long synthetic wig | TP §L8, §Q8 | BK |
| 7.05 | Styrofoam ball 7 in | 1 pc | 178 mm diameter (R 89 mm, within 1.2 % of the R 90 mm form) for L1, L4 and the apex gauge | $7.00 [est] | $7.00 | Craft store | 180 mm foam sphere | TP §L, §L4, §Q8; mech §10.3, §13 | BK |
| 7.06 | Foam wig head | 1 pc | Hairless styrofoam head for fit checks and the L5 rig-over-head tests | $7.00 [cited] | $7.00 | CL §7 ($5 to $8) | The 7 in ball | TP §L, §L5, §Q8 | BK |
| 7.07 | Nylon monofilament 100 µm | 1 spool | 0.10 mm nylon (about 2 lb test) for the hair probe of every seam (K1.10, L8.6) | $5.00 [est] | $5.00 | Search: "0.10mm nylon monofilament" | Fly-fishing tippet 6X to 7X | TP K1.10, §L, §Q8 | BK |
| 7.08 | Polyester film tape 50 µm | 1 roll | 50 µm (2 mil) polyester or PTFE tape, 3 layers on the rod (L9 tape test) | $6.00 [cited] | $6.00 | tips §9 test kit ($6) | 3M 850-type polyester tape | TP §L9, §Q8; tips §6 | BK, buy with S0 |
| 7.09 | Rod 10 mm | 1 pc | 10 mm steel rod or 3/8 in dowel, about 150 mm | $2.00 [cited] | $2.00 | tips §9 test kit ($2) | Any 10 mm rod | TP §L9; tips §6 | BK, buy with S0 |
| 7.10 | Calibration weight set | 1 set (1 to 100 g) | Gives the 15 / 50 / 100 g tether weights (L8.4), gram weights for L3 and a scale check | $12.00 [est] | $12.00 | Search: "calibration weight set 1g 100g" | Fishing sinkers trimmed on the kitchen scale | TP §L3, §L8.4, §Q8 | BK |
| 7.11 | Pulley for tether weights | 1 pc | Spare 623ZZ from row 2.08 on an M3 screw clamped to the table edge | $0.00 [est] | $0.00 | No purchase | Smooth rod edge (TP §L) | TP §L8.4, §Q8 | BK |
| 7.12 | Carbon paper | 1 pack | Lift-off chord marks (L4) and the day-0 loaded-edge marks (tips §7.4) | $5.00 [est] | $5.00 | Office supply | Whiteboard-marker ink on the tips | TP §L4, §Q8; tips §7.4 | BK, buy with S0 |
| 7.13 | Foam ear plugs | 1 pack | For the O-5 sound condition | $5.00 [est] | $5.00 | Pharmacy | Any foam plugs | TP §N3 O-5, §Q8 | BK |
| 7.14 | Black cloth and card | 1 set | About 0.5 m black felt under the cradle and black card under the wig head (shed counts) | $6.00 [est] | $6.00 | Craft store | A black T-shirt | TP §L8, §Q8, packing list | BK |
| 7.15 | Lint roller | 1 pc | Hand, knuckle plate and cloth after every session | $4.00 [est] | $4.00 | Any store | Tape | TP §L8, §Q8, packing list | BK |
| 7.16 | IR thermometer | 1 pc | Non-contact; servo, magnet and adapter temperatures in L7 (pass ≤ 48 °C touch, ≤ 43 °C within 10 mm of skin) | $18.00 [est] | $18.00 | Search: "infrared thermometer gun" | Thermocouple on the multimeter | TP §L7, §Q8 | BK |
| 7.17 | Hygrometer | 1 pc | Digital thermo-hygrometer: RH for L8 (repeat L8.4 below 35 % RH) | $9.00 [est] | $9.00 | Search: "digital hygrometer" | Phone weather app (less accurate) | TP §L8, §Q8, session log | BK |
| 7.18 | 10× loupe | 1 pc | Edge silhouette checks and seam inspection | $8.00 [cited] | $8.00 | tips §9 test kit ($8) | Phone macro lens | TP §L9, §Q8; tips §6 | BK, buy with S0 |
| 7.19 | Hair clips | 1 pack | Target-patch marks 50 mm apart; hair clipped back (K5.2) | $5.00 [est] | $5.00 | Drugstore | Bobby pins | TP §M0, K5.2, §Q8 | BK |
| 7.20 | Hand mirror | 1 pc | Self-aiming with the phone camera | $5.00 [est] | $5.00 | Any store | Phone front camera | TP §M0, §Q8 | BK |
| 7.21 | Safety glasses | 1 pc | On before the rail is powered, every session | $8.00 [est] | $8.00 | Hardware store | Any ANSI Z87.1 glasses | TP K5.1, §0 | BK |
| 7.22 | Spring scale 0 to 5 N | 1 pc | 0 to 500 g pull scale, 5 g divisions: L6(a) wrist breakaway at nail height (1.9 to 2.1 N expected, ADD-1 ruling 2) | $12.00 [est] | $12.00 | Search: "spring scale 500g" | Luggage scale (row 8.07; 0.1 N resolution, coarse for L6) | TP §L, §L6; ADD-1 ruling 2 | BK |
| 7.23 | Steel ruler 150 mm | 1 pc | Leaf deflection (L2), lift height in the video frame (L5) | $5.00 [est] | $5.00 | Any store | Caliper depth rod | TP §L, §L2, §L5 | BK |
| 7.24 | Phone macro clip lens | 1 pc | Edge photos (tips §6) and 240 fps side video (L8) | $10.00 [est] | ($10.00) | Search: "phone macro clip lens" | Loupe held to the phone | TP §L8; tips §6 | BK, optional (not in totals) |
| 7.25 | Wide-tooth comb and fine tweezers | 1 each | Combing baseline (L8), removing trapped hairs (packing list) | $8.00 [est] | $8.00 | Drugstore | Any | TP §L8, packing list | BK |
| 7.26 | Cleaning consumables | 1 lot | 70 % isopropyl alcohol 16 oz, pipe cleaners (weekly pocket clean), cotton balls (burr test) | $9.00 [est] | $9.00 | Pharmacy | Alcohol wipes | TP packing list; tips §6, §10.7 | BK, buy with S0 |
| 7.27 | Paint pen | 1 pc | Torque marks on every tightened screw (K2.15) | $4.00 [est] | $4.00 | Hardware store | Nail varnish | TP K2.15; mech §13 | BK |

Section 7 subtotal in the totals: **$240.00**; optional rows (in brackets) add $10.00.

## 8. Tools Michael needs

Buy only what you do not own. The tip-finishing grits (wet-and-dry 400, 600, 1000, 2000), the nail files 180/240 with buffer, and the 0.5 to 3.0 mm drill set for the radius reference shanks are tips §6 items. They are bought in §5 (rows 5.14 to 5.16) and not repeated here.

| # | Item | Qty | Spec | Unit price (USD) | Line total (USD) | Source | Substitute | Needed by | Stage |
|---|---|---|---|---|---|---|---|---|---|
| 8.01 | 3D printer (if not owned) | 1 pc | Bed 220 × 220 mm or larger (the P21 crossbar footprint is 196 × 108 mm and does not fit a 180 mm bed), direct drive for TPU 90A, hotend 250 °C or more for PETG, textured PEI sheet. Example class: Bambu Lab A1 (256 mm bed), about $300 to $400 [est]. Not in the totals | $0.00 [est] | $0.00 | CL §5.2 (its A1 mini at $199 to $249 is too small for P21) | Print service: JLC3DP $8 to $25 per 100 g part plus $8 to $15 shipping (CL §5.2), about $150 to $250 for 1.1 kg [est], 2 to 3 weeks. Library makerspaces are often PLA-only (not allowed here) | mech §11; tips §5; CL §5.2 | T, buy with S0 |
| 8.02 | Soldering iron | 1 pc | Pinecil V2 USB-C (plus a 65 W USB-C PD charger if none) | $30.00 [cited] | $30.00 | CL §8, $26 to $42 (https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/) | Any temperature-controlled iron | EF §1.3; mech §13 step 3 | T |
| 8.03 | Heat-set insert tip | 1 set | Pinecil/TS100 compatible, M2 and M3 sizes; 220 to 230 °C | $10.00 [cited] | $10.00 | CL §8, $7 to $15 | An old conical tip and a steady hand | mech §11, §13 step 3 | T |
| 8.04 | Solder and flux | 1 lot | 63/37, 0.6 mm, plus a flux pen | $10.00 [cited] | $10.00 | CL §8 ($10) | Any rosin-core 63/37 | EF §1.3 | T |
| 8.05 | Digital calipers 150 mm | 1 pc | Leaf lengths, tang fit, insert holes, slug stack | $15.00 [cited] | $15.00 | CL §8, $8 to $20 | Steel rule (coarse) | TP §L; mech §13; tips §7 | T, buy with S0 |
| 8.06 | Kitchen scale 0.1 g | 1 pc | 0.1 g resolution, 500 g max: W1 0.90 N = 92 ± 5 g, per-nail shares, slug sets, leaf rate at 2/4/6 mm, wand force practice at 0.3 and 0.5 N. Loads above 500 g go on the luggage scale | $12.00 [cited] | $12.00 | CL §7, $10 to $15 | 1 g / 5 kg kitchen scale (the TP §L minimum) | TP §L1, §L2; mech §6.5, §13; tips §7.3 | T, buy with S0 |
| 8.07 | Luggage scale | 1 pc | Digital hanging scale (G-Force 110 lb), 10 g resolution: springs 6.5 / 3.9 N, magnet pull-off ≥ 19 N, 7.5 N leaf proof, frame yield 8 to 11 N | $12.00 [cited] | $12.00 | CL §7, https://www.walmart.com/ip/G-force-Digital-Hanging-Luggage-Scale-110-lbs-Max/40900467 | Spring scale | mech §4.3, §14; TP §L | T |
| 8.08 | Multimeter | 1 pc | Polarity and rail 0 V checks (B1, B3), brick 4.75 to 5.25 V | $20.00 [cited] | $20.00 | CL §8, $15 to $23 (AstroAI) | Any DMM | EF §6; TP K3.1, K3.8 | T |
| 8.09 | Metric hex keys, ball end | 1 set | 1.5 mm (M2), 2.5 mm (M3), 3 mm (M4), 4 mm (M5), 5 mm (M6) | $10.00 [cited] | $10.00 | CL §8, $8 to $12 | Hex bit set | mech §13 | T, buy with S0 |
| 8.10 | M5 tap and tap handle | 1 set | M5 × 0.8 tap for the two carrier-beam ends (drop legs P11, P12). M2 and M3 taps are not needed: every M2/M3 thread is a heat-set insert or the paddle's 2.6 mm thread-forming hole | $10.00 [est] | $10.00 | Hardware store | Misumi extrusion with tapped ends [verify] | mech §5.2, §13 step 15 | T |
| 8.11 | Drill bits 1/4 in and 5.0 mm | 1 each | 1/4 in (6.35 mm) to open the Ø 6.3 mm hinge bores (P1, P5); 5.0 mm for the cheek B shoulder bore (P20); turn by hand in the tap handle or a drill | $6.00 [est] | $6.00 | Hardware store | 6.3 mm and 5.0 mm reamers | mech §11 P1, P5, P20; §12 tools | T |
| 8.12 | Mitre box and hacksaw | 1 set | 32 tpi blade for aluminium; cut the 2020 square and deburr | $18.00 [est] | $18.00 | Hardware store | A hardware-store cutting service | mech §5.1, §12 tools | T |
| 8.13 | Deburring tool and needle files | 1 each | Extrusion ends, printed bores | $18.00 [cited] | $18.00 | CL §8 ($8 + $10) | Utility knife | mech §5.1 | T |
| 8.14 | Sandpaper 220 and 400 | 1 pack | Printed parts; keeper, seat and mast faces flattened on glass. Tip grits 400 to 2000 are row 5.14 | $6.00 [cited] | $6.00 | CL §8 ($6) | Wet-and-dry from row 5.14 | mech §11 P6, P28, P30; tips §6 | T |
| 8.15 | Plastic polish | 1 bottle | Buff the knuckle plate to Ra ≤ 0.8 µm after 400 grit; polish nylon blades | $8.00 [est] | $8.00 | Search: "plastic polish" | Fine toothpaste | mech §8.7, §11 P30; tips §5.1, §6 | T |
| 8.16 | Aviation snips | 1 pc | Cut 0.30 mm feeler-stock leaves (wand and rig) | $12.00 [est] | $12.00 | Hardware store | Heavy scissors (dull quickly) | mech §8.6, §12 tools; tips §7.3 | T, buy with S0 |
| 8.17 | Fine stone | 1 pc | Stone the long edges and ends of the leaves (RT2 H4) | $8.00 [est] | $8.00 | Search: "pocket sharpening stone fine" | 1000-grit diamond file | mech §8.6, §12 tools | T |
| 8.18 | Flush cutters, wire stripper, small screwdrivers | 1 each | Support removal and electronics | $22.00 [cited] | $22.00 | CL §8 ($6 + $8 + $8) | Multi-tool | EF §1.3; tips §7.3 | T, buy with S0 |
| 8.19 | Crimp tool | 1 pc | Dupont pins and insulated terminals (and JST-EH if you make the DXL cable) | $20.00 [est] | ($20.00) | Search: "dupont crimping tool" | Pre-crimped jumpers plus solder | EF §1.3 | T, optional (not in totals) |
| 8.20 | Helping hands | 1 pc | Holding leads while soldering | $12.00 [cited] | ($12.00) | CL §8 ($12) | Blu-tack on the desk | EF §1.3 | T, optional (not in totals) |

Section 8 subtotal in the totals: **$227.00**; optional rows (in brackets) add $32.00.

## 9. Substitutes and single points of failure

### 9.1 If a critical part is out of stock

| Part | Why it matters | First substitute | Second substitute | What changes |
|---|---|---|---|---|
| XL330-M288-T | only actuator; current-based position control is the electronic clutch (EF §4.3) | Same part from Trossen Robotics or the ROBOTIS Amazon store (CL §10). Buy two in Stage 1 (row 6.33) | XL330-M077-T (same body, 0.22 N·m, 258 rpm; CL §1.2, about $27 [cited, unverified in CL]) | M077: re-derive goal current and the velocity scale (EF §4.2 to §4.4) [verify]; 0.22 N·m is still twice the 0.1 N·m the 1.2 N cap needs. No mechanical change |
| OpenRB-150 | FET-switched DXL power on VIN(DXL), logic on USB, Arduino sketch (EF §1.5) | Same part from Trossen, RobotShop or the ROBOTIS Amazon store; wait for stock rather than redesign | Stack B (EF §2): Waveshare Servo Driver with ESP32 ($14.97 to $15.99, CL §6.1) + Feetech STS3215 7.4 V ($14 to $20, CL §1.2) | Stack B is a redesign: 7.4 V rail, 12 V or 7.4 V magnet, 2 A fuse, 20 AWG, no servo bus watchdog (add an INA219 rail trip), a firmware port, and a 55 g servo needing a new cradle P13. About a week of work; last resort |
| MGN9 rail / MGN9C block | the float: N = W for any µ (DECISION item 5); 92 g budget | MGN9H block on the 100 mm rail (+10 g; ADD-1 D7 allows it only if the scale shows margin, then use the trim cord, mech §6.5 step 2) | MGN7C on an MGN7 rail (−6 g, mech §6.5 step 3); or genuine HIWIN MGN9C from Misumi [est $40 to $60] | MGN7: new hole pattern; reprint the P21 mast (insert spacing, reference lip) and the P26 riser. Never cut a hardened rail, never let a block run off the rail without its retainer |
| Electromagnet P20/15 (Adafruit 3872) | holds the frame down; loss of power must lift the nails ≥ 25 mm (freeze §1.3) | Adafruit 3873 P25/20, 50 N (row 2.16, optional; mech §4.4) | Generic 5 V P20/15 or P25/20 holding-magnet module, ≤ 0.3 A at 5 V, M3 rear thread [est $7], pull-off measured ≥ 19 N warm (mech §14) | P25/20: Ø 25 mm seat on the P1 magnet arm. Never a 12 V magnet on the 5 V rail; never fed from anywhere but the rail (EF §1.6) |
| Lift springs | two in parallel; one alone must still lift (L5) | Box 2A substitute route with the luggage-scale acceptance test | Lee Spring or Century Spring stock extension springs with the box 2A numbers (search "extension spring 0.375 OD 0.031 wire 2.5 length") [verify] | none if the box 2A numbers are met |
| 5 V 4 A brick | the rail supply; UL listing is a K3.1 item | Jameco 1466 (same part, EF §1.4) | Mean Well GST25A05 5 V 4 A UL desktop adapter [verify] | barrel size must be 5.5 × 2.1 mm centre-positive or the jack adapter changes |
| K&J D61 | sets the 2.0 N wrist breakaway (mech §7.2) | Amazon 3/8 × 1/16 in N42 discs | Two D41 (1/4 × 1/16 in) stacked [est] | Re-tune with tape layers in L6(a) at nail height |
| Feeler stock 0.30 × 12.7 mm | leaf rates 0.12 / 0.15 / 0.18 N/mm (mech §8.3) | McMaster feeler-gauge stock [verify] | Precision Brand 0.012 × 1/2 in coil | ±0.005 mm thickness = ±5 % rate; trim free length in L2 |
| TPU 90A | seam sleeves must stretch over the nose | Other 90A brands (for example Polymaker PolyFlex TPU90) | Print service TPU (CL §5.2) | 95A only for bumpers and pads |

### 9.2 Spares already in this BOM

Springs (2 spare), fuse (9 spare), MGN9C block (1), shoulder screw (1), D61 (2), membrane sheet (3 more boots), feeler stock (1 rig strip plus 1 wand strip), 6 × 2 mm magnets (47 spare), 623ZZ (8 spare), 625-2RS (9 spare), inserts (45 M3, 32 M2), and the second XL330 (row 6.33).

### 9.3 Document conflicts found while building the BOM (for the integrator)

1. **Post length.** ADD-1 D8 says a 90 mm post; mech §2 (Z 92 to 196 mm), §5.1 and §12 say 104 mm. One 500 mm bar covers either, so the BOM is unaffected, but the CAD and cut list must agree.
2. **Riser-to-seat screws.** mech §6.5 counts 2 × M3 × 8 aluminium (0.4 g); mech §12 and §13 step 11 use 2 × M3 × 10 steel through the P47 filler. The BOM buys aluminium M3 × 8 and × 10 (row 3.09); use aluminium to protect the 2 g mass margin.
3. **Screws missing from mech §12.** P1 tray seat (4 × M3), P11 to P13 cradle flange (4 × M3), P45 reset-cord guide (2 × M3, no insert listed) and P39 to P40 button housing (2 × M3 × 16 to 20). All are added to table 3A.
4. **M3 × 14 in the yaw joint.** Two 6 mm plates with a 4 mm insert suggest M3 × 10 to 12. Confirm in the CAD.
5. **M5 × 10 reach** into T-nuts through 12 mm printed nodes (P6, P7, P5). M5 × 12 and × 16 are added (row 3.13). Confirm in the CAD.
6. **Printer bed.** CL §5.2 suggests the Bambu A1 mini (180 mm bed), but P21 needs 196 × 108 mm. Specify a bed of 220 mm or more in the package.

### 9.4 All [verify] items

- Row 2.01, Monitor arm: confirm the printed minimum load (≤ 2.0 kg, ideally ≤ 1.0 kg), head swivel ±90° and tilt ±45° on the chosen listing.
- Row 2.05, MGN9 rail 100 mm with MGN9C block: no confirmed listing for the 100 mm MGN9C kit (the cited URL is MGN9H 150 mm); confirm the rail hole pitch (20 mm, 10 mm ends) and the block's 15 × 10 mm M3 pattern on arrival, before printing P21 and P26.
- Row 2.06, Spare MGN9C block: confirm it ships on a retainer.
- Row 2.10, Idler shoulder screw: no confirmed McMaster part number for Ø 5 × 25 mm, M4 thread.
- Row 2.13, Hinge lift springs (pinned in box 2A): McMaster 9654K suffix not confirmed; select by the box 2A filter and acceptance table; confirm pack size.
- Row 2.20, Wrist keeper discs: confirm 1.5 mm thickness on the listing.
- Row 2.21, Feeler stock, rig leaves: no confirmed Precision Brand or McMaster part number; buy by size 0.012 × 1/2 × 12 in.
- Row 2.24, Silicone membrane sheet: confirm 0.25 mm thickness and about 40A hardness on the listing.
- Row 2.26, PTFE film tape 0.05 mm: confirm 0.05 mm (3M 5490 is thicker).
- Row 2.30, Face cradle (SEAT): no confirmed product; needs its own stand and tilt.
- Row 3.05, M3 × 14 socket head: length may be wrong for the yaw stack (§9.3 item 4).
- Row 3.08, M2 socket-head assortment: OpenRB-150 mounting-hole size; whether XL330 horn screws ship with the servo.
- Row 3.13, M5 × 12 and M5 × 16 socket head: lengths against the CAD nodes.
- Row 6.08, Hold-to-run button: pack size of B08HH78XMH; the Ø 29.6 mm deck hole in P39 against the real button.
- Row 6.15, TVS diode: SA5.0A as the through-hole alternative to SMAJ5.0A.
- Row 6.18, DXL cable 340 mm or longer: whether ROBOTIS sells an X3P cable of 340 mm or more; otherwise crimp one.
- Row 6.35, Bar load cell 5 kg with HX711: a 40 × 12 mm, 5 kg bar cell may not exist (common 5 kg cells are about 80 mm long); the wrist slot may need resizing at Stage 3.
- Row 7.04, Kanekalon synthetic wig: confirm the fibre on the listing.
- Row 8.01, 3D printer (if not owned): model and price; bed 220 mm or more, direct drive.
- Also: Mean Well GST25A05 as a brick alternative; Misumi tapped-end option for 2020; XL330-M077-T goal-current re-derivation; OpenRB-150 outline (66 × 25 mm) for tray P3; Adafruit 3872 and 3873 prices ([est] $5.95 and $7.95).

## 10. Order checklist by vendor

| Vendor | S0 | S1 | S3 | BK | T | Subtotal | Shipping [est] | With shipping | Lead time (CL §10) |
|---|---|---|---|---|---|---|---|---|---|
| Amazon | $87.00 | $538.00 | $16.00 | $210.00 | $181.00 | $1,032.00 | $0.00 | $1,032.00 | 1 to 2 days (Prime) |
| Adafruit | $0.00 | $22.90 | $0.00 | $0.00 | $0.00 | $22.90 | $10.00 | $32.90 | ships same or next business day, 2 to 5 days |
| Robotis US | $0.00 | $64.13 | $27.49 | $0.00 | $0.00 | $91.62 | $10.00 | $101.62 | 2 to 5 days; order first |
| McMaster-Carr | $0.00 | $16.00 | $0.00 | $0.00 | $0.00 | $16.00 | $8.00 | $24.00 | same or next day ground, no minimum |
| K&J Magnetics | $0.00 | $1.47 | $0.00 | $0.00 | $0.00 | $1.47 | $5.00 | $6.47 | 1 to 3 days |
| SendCutSend | $0.00 | $54.00 | $0.00 | $0.00 | $0.00 | $54.00 | $0.00 | $54.00 | 2 to 5 days [est] |
| Filament supplier | $54.00 | $25.00 | $0.00 | $0.00 | $0.00 | $79.00 | $0.00 | $79.00 | 1 to 2 days if bought on Amazon |
| Hardware store | $0.00 | $41.00 | $0.00 | $30.00 | $46.00 | $117.00 | $0.00 | $117.00 | same day |
| **All vendors** | **$141.00** | **$762.50** | **$43.49** | **$240.00** | **$227.00** | **$1,413.99** | **$33.00** | **$1,446.99** | |

Shipping estimates assume one order per vendor and no free-shipping threshold; Amazon is assumed Prime. The SendCutSend minimum order (about $29, CL §5.3) is met by the 6 plates.

### Amazon ($1,032.00)

**Stage 0 wand**

- ☐ Tip item 3: Neodymium magnets, 50 pack, $9.00, row 5.03
- ☐ Tip item 5: Steel keeper discs, 50 pack, $7.00, row 5.05
- ☐ Tip item 6: Feeler stock, 2 strips, $8.00, row 5.06
- ☐ Tip item 7: Press-on nails, 1 box, $7.00, row 5.07
- ☐ Tip item 8: Nylon picks, 12 pack, $5.00, row 5.08
- ☐ Tip item 10: Steel balls, 100 pack, $5.00, row 5.10
- ☐ Tip item 11: Screws, 50 pack, $5.00, row 5.11
- ☐ Tip item 12: Cyanoacrylate, 2, $8.00, row 5.12
- ☐ Tip item 13: Epoxy, 1, $6.00, row 5.13
- ☐ Tip item 14: Abrasive paper, 1 sheet each, $8.00, row 5.14
- ☐ Tip item 15: Nail files and buffer, 1 set, $4.00, row 5.15
- ☐ Tip item 16: Drill-bit set, 1, $10.00, row 5.16
- ☐ Tip item 17: Marker and varnish, 1 each, $5.00, row 5.17

**Stage 1 rig**

- ☐ Monitor arm, 1 pc, $36.00, row 2.01
- ☐ 2020 aluminium extrusion, 1 pack (4 × 500 mm), $28.00, row 2.03
- ☐ 2020 corner bracket kit, 1 kit (about 40 sets), $15.00, row 2.04
- ☐ MGN9 rail 100 mm with MGN9C block, 1 kit, $12.00, row 2.05
- ☐ Spare MGN9C block, 1 pc, $8.00, row 2.06 (can wait)
- ☐ 623ZZ bearings, 1 pack of 10, $7.00, row 2.08
- ☐ 625-2RS bearing, 1 pack of 10, $8.00, row 2.09
- ☐ Dyneema cord, 1 spool (3 m needed), $12.00, row 2.11
- ☐ Trim cord, 1 roll, $5.00, row 2.12
- ☐ Spring fallback assortment, 1 assortment, $10.00, row 2.14 (optional, not in totals)
- ☐ Wrist keeper discs, 2 pcs (buy a pack), $7.00, row 2.20
- ☐ Feeler stock, rig leaves, 2 strips (1 used, 1 spare), $8.00, row 2.21
- ☐ Silicone membrane sheet, 1 sheet (makes 4 boots), $10.00, row 2.24
- ☐ Silicone adhesive, 1 tube, $14.00, row 2.25
- ☐ PTFE film tape 0.05 mm, 1 roll, $10.00, row 2.26
- ☐ Rubber bumpers, 1 assortment, $6.00, row 2.27
- ☐ Isolation feet, 4 pcs, $10.00, row 2.28 (can wait)
- ☐ Face cradle (SEAT), 1 pc, $45.00, row 2.30
- ☐ Face cradle cushion (PRONE), 1 pc, $20.00, row 2.31 (can wait)
- ☐ Heat-set inserts M3, 1 pack of 100, $9.00, row 3.01
- ☐ Heat-set inserts M2, 1 pack of 50, $7.00, row 3.02
- ☐ Heat-set inserts M4, 1 small pack, $6.00, row 3.03
- ☐ Metric screw and nut assortment, 1 kit (about 1000 pcs, M3/M4/M5), $20.00, row 3.04
- ☐ M3 × 14 socket head, 1 pack of 10, $5.00, row 3.05
- ☐ M3 × 6 flat-head (countersunk), 1 pack of 10, $5.00, row 3.06
- ☐ Nyloc nut assortment, 1 assortment, $8.00, row 3.07
- ☐ M2 socket-head assortment, 1 kit, $9.00, row 3.08
- ☐ Aluminium M3 screw assortment, 1 kit (6/8/10 mm), $9.00, row 3.09
- ☐ Nylon M3 screw assortment, 1 kit, $8.00, row 3.10
- ☐ Knurled M3 × 16 thumbscrews, 1 pack of 10, $8.00, row 3.11
- ☐ Zip ties, 1 pack (100), $5.00, row 3.15
- ☐ Tip item 4: Neodymium magnets, 20 pack, $6.00, row 5.04 (can wait)
- ☐ Tip item 9: Nylon picks or sheet, 12 pack, $5.00, row 5.09 (can wait)
- ☐ Fuses 1 A fast-blow 5 × 20 mm, 1 pack of 10, $5.00, row 6.03
- ☐ Inline fuse holder, 1 pc (pack), $7.00, row 6.04
- ☐ Fuses 1.25 A fast 5 × 20 mm, 1 pack, $5.00, row 6.05 (optional, not in totals)
- ☐ E-stop, boxed, 1 pc, $14.00, row 6.06
- ☐ Hold-to-run button, 1 pc (pack), $8.00, row 6.08
- ☐ Hold-to-run cable, 1 spool (1.5 m used), $9.00, row 6.09
- ☐ Hold-to-run, bought alternative, 1 pc, $10.00, row 6.11 (optional, not in totals)
- ☐ Flyback diode, 1 pack, $5.00, row 6.13
- ☐ Bulk capacitor, 1 pack, $5.00, row 6.14
- ☐ TVS diode, 1 pack, $6.00, row 6.15
- ☐ Potentiometers 10 kΩ linear with knobs, 1 pack, $8.00, row 6.19
- ☐ Toggle switch, 1 pack, $7.00, row 6.20
- ☐ Status LED, 1 pack, $5.00, row 6.21
- ☐ Resistor assortment, 1 kit, $7.00, row 6.22
- ☐ Ceramic capacitors 100 nF, 1 pack, $5.00, row 6.23
- ☐ 22 AWG silicone wire, 1 kit (6 colours), $12.00, row 6.24
- ☐ 6-core 26 AWG cable, 1 length (1.0 m used), $9.00, row 6.25
- ☐ Heat-shrink assortment, 1 kit, $6.00, row 6.26
- ☐ Braided sleeving, 2 m, $7.00, row 6.27
- ☐ Wago 221-413 lever connectors, 1 pack, $9.00, row 6.28
- ☐ Dupont kit, 1 kit, $8.00, row 6.29
- ☐ Perfboard, 1 pack, $7.00, row 6.30
- ☐ USB-C cable, 1 pc, $8.00, row 6.31
- ☐ Insulated crimp terminals, 1 assortment, $10.00, row 6.32

**Stage 3 upgrades**

- ☐ Lazy-Susan bearing ring, 1 pc, $6.00, row 6.34
- ☐ Bar load cell 5 kg with HX711, 1 kit, $10.00, row 6.35

**Bench and test kit**

- ☐ Real-hair training head, short, 1 pc, $32.00, row 7.01
- ☐ Real-hair training head, long, 1 pc, $32.00, row 7.02
- ☐ Mannequin table clamp, 1 pc, $8.00, row 7.03
- ☐ Kanekalon synthetic wig, 1 pc, $18.00, row 7.04
- ☐ Foam wig head, 1 pc, $7.00, row 7.06
- ☐ Nylon monofilament 100 µm, 1 spool, $5.00, row 7.07
- ☐ Polyester film tape 50 µm, 1 roll, $6.00, row 7.08
- ☐ Calibration weight set, 1 set (1 to 100 g), $12.00, row 7.10
- ☐ Carbon paper, 1 pack, $5.00, row 7.12
- ☐ Foam ear plugs, 1 pack, $5.00, row 7.13
- ☐ Black cloth and card, 1 set, $6.00, row 7.14
- ☐ Lint roller, 1 pc, $4.00, row 7.15
- ☐ IR thermometer, 1 pc, $18.00, row 7.16
- ☐ Hygrometer, 1 pc, $9.00, row 7.17
- ☐ 10× loupe, 1 pc, $8.00, row 7.18
- ☐ Hair clips, 1 pack, $5.00, row 7.19
- ☐ Hand mirror, 1 pc, $5.00, row 7.20
- ☐ Spring scale 0 to 5 N, 1 pc, $12.00, row 7.22
- ☐ Steel ruler 150 mm, 1 pc, $5.00, row 7.23
- ☐ Phone macro clip lens, 1 pc, $10.00, row 7.24 (optional, not in totals)
- ☐ Wide-tooth comb and fine tweezers, 1 each, $8.00, row 7.25

**Tools**

- ☐ Soldering iron, 1 pc, $30.00, row 8.02
- ☐ Heat-set insert tip, 1 set, $10.00, row 8.03
- ☐ Solder and flux, 1 lot, $10.00, row 8.04
- ☐ Digital calipers 150 mm, 1 pc, $15.00, row 8.05
- ☐ Kitchen scale 0.1 g, 1 pc, $12.00, row 8.06
- ☐ Luggage scale, 1 pc, $12.00, row 8.07
- ☐ Multimeter, 1 pc, $20.00, row 8.08
- ☐ Metric hex keys, ball end, 1 set, $10.00, row 8.09
- ☐ Deburring tool and needle files, 1 each, $18.00, row 8.13
- ☐ Sandpaper 220 and 400, 1 pack, $6.00, row 8.14
- ☐ Plastic polish, 1 bottle, $8.00, row 8.15
- ☐ Fine stone, 1 pc, $8.00, row 8.17
- ☐ Flush cutters, wire stripper, small screwdrivers, 1 each, $22.00, row 8.18
- ☐ Crimp tool, 1 pc, $20.00, row 8.19 (optional, not in totals)
- ☐ Helping hands, 1 pc, $12.00, row 8.20 (optional, not in totals)

### Adafruit ($22.90)

**Stage 1 rig**

- ☐ Holding electromagnet, 1 pc, $5.95, row 2.15
- ☐ Fallback electromagnet, 1 pc, $7.95, row 2.16 (optional, not in totals)
- ☐ 5 V 4 A power adapter, 1 pc, $14.95, row 6.01
- ☐ DC jack to screw-terminal adapter, 1 pc, $2.00, row 6.02

### Robotis US ($91.62)

**Stage 1 rig**

- ☐ OpenRB-150 controller, 1 pc, $28.64, row 6.16
- ☐ Dynamixel XL330-M288-T (elbow), 1 pc, $27.49, row 6.17
- ☐ DXL cable 340 mm or longer, 1 pc (pack), $8.00, row 6.18

**Stage 3 upgrades**

- ☐ Dynamixel XL330-M288-T (spare, Stage 3 yaw), 1 pc, $27.49, row 6.33

### McMaster-Carr ($16.00)

**Stage 1 rig**

- ☐ Idler shoulder screw, 2 pcs (1 + 1 spare), $6.00, row 2.10
- ☐ Hinge lift springs (pinned in box 2A), 4 pcs (2 + 2 spare), sold as a pack, $10.00, row 2.13

### K&J Magnetics ($1.47)

**Stage 1 rig**

- ☐ Wrist magnet K&J D61, 3 pcs (1 + 2 spare, one for stack tuning), $1.47, row 2.19

### SendCutSend ($54.00)

**Stage 1 rig**

- ☐ Ballast plates, 5 pcs, $45.00, row 2.02 (can wait)
- ☐ E-stop weighted base, 1 plate, $9.00, row 6.07

### Filament supplier ($79.00)

**Stage 0 wand**

- ☐ PETG filament, spool 1 (bright colour), 1 kg, $25.00, row 4.01
- ☐ TPU 90A filament, 1 small spool, $29.00, row 4.03

**Stage 1 rig**

- ☐ PETG filament, spool 2, 1 kg, $25.00, row 4.02

### Hardware store ($117.00)

**Stage 1 rig**

- ☐ Hinge pin set, 1 set, $4.00, row 2.07
- ☐ Keeper plate stock, 1 bar, $8.00, row 2.17
- ☐ PTFE thread-seal tape, 1 roll, $2.00, row 2.18
- ☐ M8 slug washers, 20 pcs, $6.00, row 2.22
- ☐ Baseboard, 1 pc, $12.00, row 2.29 (optional, not in totals)
- ☐ Light machine oil, 1 bottle, $4.00, row 2.32
- ☐ Medium threadlocker, 1 tube, $6.00, row 2.33
- ☐ M4 screws for VESA, ballast, up-stop, 1 lot, $5.00, row 3.12
- ☐ M5 × 12 and M5 × 16 socket head, 10 of each, $6.00, row 3.13
- ☐ Wood screws #4 × 1/2 in, 8 pcs, $3.00, row 3.14 (optional, not in totals)

**Bench and test kit**

- ☐ Styrofoam ball 7 in, 1 pc, $7.00, row 7.05
- ☐ Rod 10 mm, 1 pc, $2.00, row 7.09
- ☐ Safety glasses, 1 pc, $8.00, row 7.21
- ☐ Cleaning consumables, 1 lot, $9.00, row 7.26
- ☐ Paint pen, 1 pc, $4.00, row 7.27

**Tools**

- ☐ M5 tap and tap handle, 1 set, $10.00, row 8.10
- ☐ Drill bits 1/4 in and 5.0 mm, 1 each, $6.00, row 8.11
- ☐ Mitre box and hacksaw, 1 set, $18.00, row 8.12
- ☐ Aviation snips, 1 pc, $12.00, row 8.16

**No purchase needed:** zero pin (3.0 mm drill shank), tether-weight pulley (spare 623ZZ), hold-to-run housing and tip box (printed), phone apps (240 fps, SPL meter, inclinometer, timer).
