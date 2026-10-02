# HALO parts list with live prices

**SP1 v3 · 14-build/halo · 2026-10-02 · prices checked today**

## How to read the tags

| Tag | Meaning |
|---|---|
| **[cited URL]** | I saw the price on that page on 2026-10-02 |
| **[snippet]** | The price came from a search result; the page itself was not opened (bot check) |
| **[est]** | Estimate |
| **[verify]** | Check before ordering |

**What is and isn't in these totals:**
- Shipping is not included unless stated.
- Parts shared with other work packages are marked **(shared)**. Buy each only once.
- The printed parts (H01–H20) are a separate line. See `cad/README.md` for files and print notes.

## Staging

| Stage | When | What |
|---|---|---|
| **S0** (Day-0 cart) | Before any CAD is trusted | The coin-test and hinge evening (spec §10 S0) |
| **B** (Cart 3) | Only after Stage A passes | Everything else for the halo |
| **C** (Cart 4) | After Stage B passes | Spares only |

The default build uses the **medium** hinge (CONFLICTS #2). If the Director adopts the light float (CONFLICTS #1), the small hinge is enough and saves $10 and 14 g.

---

## S0: coin test and tape fit (≈ $50)

| # | Part | Qty | Unit | Line | Source |
|---|---|---|---|---|---|
| S0-1 | Adult bike helmet with a dial fit system. You use its shell for the stick-bail and coin-bag test; its own dial is a spare cradle. | 1 | $12.99 | $12.99 | [cited walmart.com/ip/21052657389, 2026-10-02] |
| S0-2 | UltAlt bike helmet retention dial, 2-pack (ADJ3501, 50–62 cm; rear cradle + 2 side arms ending in tabs). This is **the** cradle for the halo; the second one is a spare. | 1 pack | $7.97 | $7.97 | [cited amazon.com/dp/B0G3WDYMLC, 2026-10-02] |
| S0-3 | Southco **E6-10-301-20** medium adjustable-torque hinge, acetal (0.8 N·m max; 4 × Ø4.5 holes on 31.8 × 25.4; M4 screws not supplied) | 2 | $12.48 | $24.96 | [cited shop.southco.com/en_us/e6-10-301-20, 2026-10-02]; Bossard out of stock |
| S0-3alt | Southco **E6-10-101-20** small (0.25 N·m; moulded studs + 4 push-on nuts supplied). Only with the light float. | 2 | $7.34 | $14.68 | [cited americas.bossard.com/products/e6-10-101-20-by-southco.html, 2026-10-02]; Southco shop $11.65; Amazon $25.00 |
| S0-4 | Soft sewing tape measure, 60 in / 150 cm | 1 | $3.69 | $3.69 | [cited amazon.com/dp/B07MT89MCW, 2026-10-02] |
| S0-5 | M4 × 10 socket screws (for the medium hinges in the coin test) | 8 | — | ≈ $4 | [est] hardware store |
| | **S0 HALO subtotal** | | | **≈ $54** | |

## Stage B: the halo (≈ $264 bought + printing ≈ $95–135)

### Carbon

| # | Part | Qty | Unit | Line | Source |
|---|---|---|---|---|---|
| B-1 | KARBXON pultruded carbon tube **8 mm OD × 6 mm ID × 1000 mm**. You need 676 mm; the second tube is spare for mistakes. | 2 | — | $32.38 (2-pack) | [cited amazon.com/dp/B09QLD99BD, 2026-10-02] |
| B-2 | KARBXON pultruded carbon flat **10 × 1 × 1000 mm**: track 371 mm + front band 2 × 290 mm | 2 | — | $20.94 (2-pack) | [cited amazon.com/dp/B09Q8FF7RR, 2026-10-02] |
| B-3 | Carbon rod Ø3 × ≥ 100 mm (float anti-rotation guide) | 1 | — | ≈ $7 | [est] [verify] any pultruded 3 mm rod pack |

### Bearings, pins, plungers, springs

| # | Part | Qty | Unit | Line | Source |
|---|---|---|---|---|---|
| B-4 | MR63ZZ ball bearing 3 × 6 × 2.5 (carriage rollers; 4 used) | 10-pack | — | $5.39 | [cited amazon.com/dp/B0H2DR1GD2, 2026-10-02] |
| B-5 | Ø3 mm stainless dowel-pin assortment (lengths 6–20: roller axles 2 × 16 + 2 × 8, trigger pins 2 × 12, spool 1 × 16, stop pins 2 × 8, node location) | 1 kit | — | $8.99 | [cited amazon.com/dp/B0DP28ZTSL, 2026-10-02] |
| B-6 | McMaster **85015A46** M4 × 0.7 stainless ball plunger, Ø2.5 ball, 4.0 N extended (one α detent, one β detent) | 2 | $7.25 | $14.50 | [cited mcmaster.com, 2026-10-02] |
| B-7 | McMaster **9293K123** constant-force spring, 0.36 lb (1.60 N), 18 in extension (float retract) | 1 | $7.57 | $7.57 | [cited mcmaster.com/products/constant-force-springs, 2026-10-02]. Coil bore assumed 8.8 mm [verify] |

### Magnets, balls, switch, lanyard

| # | Part | Qty | Unit | Line | Source |
|---|---|---|---|---|---|
| B-8 | N52 disc magnets Ø6 × 3 (spider ×3; **shared with PAD**) | 50-pack | — | $14.59 | [cited amazon.com/dp/B0GWM33Z8X, 2026-10-02] |
| B-9 | Chrome steel balls Ø5 mm, G16 (spider ×3; **shared with PAD**) | 100-pack | — | $5.99 | [cited amazon.com/dp/B0CWN7BCL7, 2026-10-02] |
| B-10 | Neodymium Ø10 × 3 disc (3 N umbilical clip) | 50-pack | — | $9.99 | [cited amazon.com/dp/B0BVY5VYQY, 2026-10-02] |
| B-11 | Omron **D2F-01FL** low-force (0.25 N) lever microswitch: the head-present switch | 2 (1 spare) | $1.61 | $3.22 | [snippet: Digi-Key; verify] |
| B-12 | 2-pin magnetic pogo connector pair: loop-wire lanyard (**ELECTRONICS owns the wiring**; HALO provides the seat in H17) | 1 pair | — | ≈ $5 | [est] [verify] pocket 13.4 × 4.9 × 5.5 |

### Fasteners

| # | Part | Qty | Unit | Line | Source |
|---|---|---|---|---|---|
| B-13 | Brass heat-set inserts **M3** (Ø4.0 holes) | 100-pack | — | $9.99 | [cited ruthex M3 × 5.7, 2026-10-02]. The CAD holes are 4 mm deep; use M3 × 4 short inserts or let the 5.7 ones stand proud 1.7 mm and face them flush [verify] |
| B-14 | Brass heat-set inserts **M4** (Ø5.6 × 6.5): 8 for the medium hinges + 2 plungers | 20-pack | — | ≈ $8 | [est] [verify] |
| B-15 | M3 stainless socket-head screw kit (lengths 6–20) + nuts | 1 kit | — | $8.99 | [cited amazon.com/dp/B0GHMM79M9, 2026-10-02]. Aluminium M3 saves ≈ 5 g [est] |
| B-16 | M4 × 10 socket screws for the medium hinges (8) | — | — | (S0-5) | |
| B-17 | #10-32 hex nuts (spider on the Airpel rod; 2) | — | — | ≈ $1 | [est] hardware store |

### Adhesive, pads, small items

| # | Part | Qty | Unit | Line | Source |
|---|---|---|---|---|---|
| B-18 | **3M Scotch-Weld DP420** black structural epoxy, 50 ml. Bail nodes, feet, stub, strip and band are head-borne structural joints. | 1 | $47.02 | $47.02 | [cited amazon.com/dp/B07FQQGP96, 2026-10-02] |
| B-19 | 50 ml 1:1/2:1 dispensing gun | 1 | — | ≈ $13 | [est] [verify] |
| B-20 | DP420 mixing nozzles | 25-pack | — | $12.99 | [cited, 2026-10-02] |
| B-18alt | **Budget option:** J-B Weld 50133 Plastic Bonder, 25 ml, **only if every node passes the 20 N pull proof** (halo.md §6.6) | 1 | $6.79 | $6.79 | [cited, 2026-10-02] |
| B-21 | Bike helmet replacement pad kit, 27 pcs (washable, hook-and-loop): temple pads (2 layers each side) + forehead foam | 1 | $6.49 | $6.49 | [cited amazon.com/dp/B0FTXTPG7G, 2026-10-02] |
| B-22 | 3M Bumpon SJ5302 (α and β stop bumpers) | 80-pack | — | $9.99 | [cited amazon.com/dp/B01ACPT2LU, 2026-10-02] |
| B-23 | NBR O-ring cord Ø3 mm, 1 m (2 hub brakes + carriage friction pad) | 1 | — | ≈ $6 | [est] [verify] |
| B-24 | PTFE tape 0.13 mm (carriage guide faces; **shared with PAD**, which buys it for the dish) | — | — | (PAD) | |
| B-25 | Steel M5 × 15 mm fender washer (umbilical clip) | 2 | — | ≈ $0.50 | [est] hardware store |
| B-26 | Cable ties 100 mm | 200-pack | — | $3.99 | [cited amazon.com/dp/B0BC1VH4XB, 2026-10-02] |
| | **Stage B HALO bought-parts subtotal (medium hinge; includes $20.58 of magnets and balls shared with PAD)** | | | **≈ $264** | |

### Float (bought by the PAD/float line in spec §13; HALO mounts it)

| # | Part | Qty | Unit | Line | Source |
|---|---|---|---|---|---|
| F-1 | Airpot **Airpel E16D2.0N**: D = double-acting, N = nose stud mount; 7/16-20 nose, 10-32 rod and ports. **≈ 96 g; see CONFLICTS #1 before buying.** | 1 | — | 4-pack **$130.50** delivered | [cited Life Sciences Trading, 2026-10-02]; eBay 4-pack $145 [cited ebay.com/itm/366660882196]. A single new unit is quote-only from Airpot [verify] |
| F-2 | Light-float alternative (proposal): 5/8 in Penrose latex drain, printed bore and piston | 1 | — | ≈ $15 | [est]. PAD already buys 1/4 in Penrose; add the 5/8 in size |

### Printing (HALO parts only)

| # | Part | Qty | Unit | Line | Source |
|---|---|---|---|---|---|
| P-1 | JLC3DP MJF PA12-HP: H01–H18 head-borne set, about 127 cm³ (medium hinge) / 106 cm³ (small) | 1 batch | "from $1/part" | ≈ $55–75 + **40 % US tariff** ≈ $75–105 | [cited jlc3dp.com PA12 page and US-tariff FAQ (2026-03-19), 2026-10-02]; batch total [est] |
| P-2 | JLC3DP shipping to Naples FL | — | — | ≈ $20–30 | [est]; DHL rate not published |
| P-3 | Tools H19 zero gauge + H20 notch jig: home PETG, or add to the batch | — | — | ≈ $8 in the batch | [est] |

### Tools HALO needs beyond the RT3 list (soldering, calipers, scales, logic analyser, tube cutter)

| # | Tool | Line | Source |
|---|---|---|---|
| T-1 | Triangular needle file (notches) + flat file | ≈ $8 | [est] |
| T-2 | Fine-tooth razor saw or junior hacksaw with a 32 tpi blade (carbon tube and strip) | ≈ $10 | [est] |
| T-3 | N95 / P2 dust mask. Cut and file carbon wet or under a damp paper towel: carbon dust is an irritant. | ≈ $10 | [est] |
| T-4 | Soldering iron with a heat-set insert tip (RT3 list already has the iron) | ≈ $8 | [est] |
| T-5 | Luggage scale 0–5 kg, 10 g resolution (hinge torque check, umbilical clip pull, cradle override) | ≈ $9 | [est] |
| T-6 | 120 and 240 grit sandpaper, isopropyl alcohol, masking tape, washable eyeliner pencil, 2 hardcover books | ≈ $10 | [est] / household |

## Totals (HALO only, before shipping)

| Option | S0 | Stage B bought | Printing | Total |
|---|---|---|---|---|
| **Default (medium hinges, Airpel bought by PAD)** | ≈ $54 | ≈ $264 | ≈ $95–135 | **≈ $415–455** |
| Light float + small hinges | ≈ $39 | ≈ $256 | ≈ $90–125 | **≈ $385–420** |

**Against spec §13:**
- Spec helmet line: **$119**.
- HALO line here: ≈ **$415–455**.

**Where the difference comes from** (not mistakes in the spec's arithmetic; those lines were simply not costed):

| Item | Cost |
|---|---|
| DP420 epoxy + gun + nozzles | ≈ $73 |
| Printing with the US tariff | ≈ $95–135 |
| Plungers | $14.50 |
| Constant-force spring | $7.57 |
| Insert and screw kits | ≈ $27 |

**Two cheaper choices that keep the design:**
- J-B Weld instead of DP420 (−$66), only if the proof tests pass.
- Printing at home in PETG and nylon instead of JLC (−$100). This needs a printer.
