# SP1 Tips, TM1 Mount and Stage-0 Hand Wand

Project SCRATCH, 05-engineering, tip lead, 2026-10-01.
Builds to: `05-engineering/DESIGN-FREEZE.md` §1.7, §1.8 and §3 (binding). Inherits: `01-foundations/tip-interface.md` (SP1-TM1, tip family, edge finishing), `01-foundations/safety-requirements.md` (red line 11, tape test, hygiene), `01-foundations/scratch-model.md` (nail geometry targets, DR1 to DR8), `01-foundations/hair-interaction.md` (H-4.3), `04-redteam/redteam-1-sensation.md` §5, `05-engineering/test-protocols.md` (L6, L8 to L12, H0, §Q5).
CAD: `05-engineering/cad/tips/` (OpenSCAD sources, `gen_tips_stl.py`, `stl/`, `README.md`). Units: mm, N, g, s unless stated. Tags: [KNOWN] literature, [EST] engineering estimate, [UNKNOWN] must be measured.

---

## 1. Scope

This document describes, as built, the SP1 scratching tips, the SP1-TM1 mount, the paddle that carries a TM1 pocket on each hand leaf, and the motorless Stage-0 hand wand. It covers DESIGN-FREEZE §1.8, the tip side of §1.7 and Stage 0 of §3. The tip set is the frozen one: W (symmetric wedge, default), B45 (45° nail-mimic plate), B45-12 (width), A45 (R 0.3 mm, gated), E (pulp-backed), H (3 mm ball control) and P (press-on nail reference). Every tip shares one tang and one pocket, so a result found on the wand transfers to the rig unchanged. Out of scope: hand clamshell, knuckle plate, float, wrist (MECH LEAD); electronics; test procedures (owned by `test-protocols.md`, referenced here). The audit of the delivered SCAD files is summarised in §10.1.

**Post-addendum changes (2026-10-01, tip lead follow-up, after `DESIGN-FREEZE-ADDENDUM-1.md`).** The mechanical lead's hand (mechanical.md §8) changed the paddle's context, and the addendum's rulings D2 to D5 are binding. In `paddle_with_pocket.scad` and `gen_tips_stl.py` I changed two things. `DRAFT_Y` went from 5 to 10, so all four paddle faces now carry the ≥ 10° of freeze §1.7 and H-4.3; the 24 mm pitch (D2) leaves room for it. I added a `RISER` parameter (D3): `RISER = 9` gives the centre paddle, whose leaf clamps 9 mm higher. Every other dimension is unchanged. The STLs were regenerated, with a new `paddle_with_pocket_riser9.stl`. The seam sleeve follows the 10° nose and is 0.56 mm wider in Y at its top. The hand now uses three paddles of two kinds. The knuckle-plate exits are one shared slot with a bonded slack membrane (D4), and leaf travel to the stop is 5.0 mm (D5). Sections changed: §1 (this note), §2.5 (sleeve size), §8 (rewritten), §9 (paddle parts table), §10.1 and new §10.9. The tips, the TM1 mount, the wand and their STLs are unchanged.

---

## 2. The TM1 mount as built

### 2.1 Dimensions

All values are from `tm1_tang_lib.scad`. The origin is the centre of the pocket-mouth plane; +Z points into the pocket.

| Feature | Value | Spec (tip-interface §5.2) | Note |
|---|---|---|---|
| Tang section | 10.0 mm (X) x 4.0 mm (Y) | 10.0 x 4.0 | |
| Tang length | 12.0 mm (z 0 to 12.0) | 12.0 | |
| Orientation key | 2.0 mm x 45° chamfer on the +X+Y corner, full length | one corner, 2 x 45° | a mirrored tip cannot enter |
| Tang end chamfer | 0.5 mm all round | not in spec | insertion lead-in, elephant-foot relief |
| Pocket section | 10.3 x 4.3 mm (0.15 mm clearance per side), matching key chamfer | 10.3 x 4.3 | |
| Pocket depth | 12.5 mm | 12.5 | tang bottoms on the magnet at 12.0 |
| Pocket mouth lead-in | 0.6 mm chamfer | not in spec | |
| Magnet recess | Ø 6.2 mm, z 11.9 to 14.0 | magnet at floor | captured by 0.85 mm ledges of the 4.3 mm pocket walls |
| Magnet | N52 6 x 2 mm disc, axial | N52 6 x 2 | dropped in at a print pause |
| Steel keeper | 6.0 x 3.9 x 1.0 mm slug (or 6 x 1 mm disc with two flats to 3.9 mm) in a through-notch at the tang end | 6 x 1 mm disc or M3 washer | a round 6 mm disc or a 7 mm M3 washer cannot fit a 4.0 mm tang |
| Shoulder | cone from the tang section at z 0 to a 14 x 9 mm (R 1 mm corners) band at z -2.5; band to z -5.5 | not in spec | band = paddle nose size, carries the seam sleeve |
| Working part | below z -5.5 | | edge of W, B45, B45-12, A45 at z -12.5 |
| Heavy-tip option | TM1-B: M3 cross-bolt, Ø 3.2 mm in the tang, Ø 3.4 mm in the holder, at z 6.0 | M3 x 6 into the floor | not used in SP1 |

Normal scratch force pushes the tip deeper and never loads the magnet. Drag (0.05 to 0.3 N per nail, scratch-model 3.5) is carried by the 12 mm deep pocket walls: at most 1.5 N x 12.5 mm = 19 N mm at the mouth, trivial for the 1.85 to 2.35 mm PETG walls of the paddle nose.

### 2.2 Magnet and keeper

The N52 6 x 2 mm disc sits in a Ø 6.2 x 2.1 mm recess that straddles the pocket floor. The pocket is only 4.3 mm wide in Y, so once the print resumes above the magnet the two pocket walls overlap the magnet rim by 0.85 mm each side and capture it mechanically; a dot of CA at the pause keeps it from jumping to the hotend. The magnet face ends up at z 11.9 to 12.0, so a fully seated tang (12.0 mm long) touches it directly with no designed air gap.

The keeper is a 6.0 x 3.9 x 1.0 mm mild-steel slug bonded flush into a notch open at the tang end and through both Y faces. The DESIGN-FREEZE wording "6 x 1 steel disc" cannot be met literally (a 6 mm disc is wider than the 4.0 mm tang), so buy 6 x 1 mm steel discs and file two flats to 3.9 mm, or cut slugs from 1 mm sheet. The slug covers 21.6 mm² of the 28.3 mm² magnet face (76 %).

### 2.3 Breakaway force calculation

The axial breakaway is the force that pulls a tip out of its pocket along the tip axis, which is the direction a hair wrap pulls as the stroke continues. Spec: 4 to 8 N (tip-interface §5.1 item 4, DESIGN-FREEZE §1.8).

F_break = F_rated x k_area x k_keeper x k_gap + F_sleeve

| Term | Value | Basis |
|---|---|---|
| F_rated, N52 6 x 2 mm on thick steel, in contact | about 8 N (0.8 kgf) | [EST], vendor ratings for 6 x 2 mm N52 discs cluster at 0.7 to 0.9 kgf; tip-interface quotes 11 N for 6 x 3 mm |
| k_area, slug covers 76 % of the face | 0.76 | computed from the slug and magnet outlines |
| k_keeper, 1 mm thick keeper saturates | about 0.7 | [EST] |
| k_gap, 0 to 0.1 mm (magnet float, print roughness) | 0.8 to 1.0 | [EST] |
| Magnet subtotal | 3.4 to 4.3 N | |
| F_sleeve, TPU sleeve gripping the band with 0.2 mm interference over 3 mm | 0.5 to 1.5 N | [EST] |
| Total | about 4 to 6 N | inside the spec, at its low end |

Loads that act to pull a tip out are tip weight (0.02 N) and stroke inertia (about 0.01 N at 2 Hz, ±30 mm), so the margin against accidental release exceeds 100 times. The breakaway only backstops bundle snags: one anagen hair pulls out at about 0.36 N [KNOWN, scratch-model §2.3], far below any magnet hold, so the primary hair protection stays geometric and the rig's wrist breaks away at 2.0 N tangential.

Tuning, measured by test-protocols L6(b) (hang weights from the tip, tip pointing down, with the sleeve fitted): below 4 N, change to an N52 6 x 3 mm magnet (set `TM1_MAG_H = 3.0`, recess 3.1 mm, about 35 % more hold [EST]); above 8 N, add one 0.1 mm layer of tape on the slug face (each 0.1 mm of gap removes roughly 15 to 20 % [EST]) or use a 5 x 2 mm magnet. Record the value per tip; mass differences are negligible but slug bonding is not.

### 2.4 Seating and release

Seat: align the key chamfer with the chamfered pocket corner (a 45° tip cannot be reversed by accident), push until the magnet pulls the last millimetre home with a click, press on the working part to confirm no rock. A tang that stops short of 12.0 mm is the wrong way round or has varnish or a support scar on a face. Release: grip the working part and pull straight along the axis with 4 to 6 N. No tool, under 10 s (tip-interface §5.1). One dot of gel CA bonds the seam sleeve's top rim to the paddle nose so the sleeve stays on the paddle.

### 2.5 Seam sleeving against hair

The cone between the tang and the band leaves a V-shaped gap between the paddle nose face (z 0) and the tip shoulder that grows from 0.15 mm at the pocket mouth to 2.5 mm at the band. That is exactly the 0.04 to 3 mm gap range forbidden near hair (DESIGN-FREEZE §1.4, test-protocols K1.8). The TPU 90A seam sleeve (`paddle_with_pocket.scad`, `PART = "sleeve"`, 0.8 mm wall) is stretched over the drafted nose with 0.2 mm interference per side and covers z +3.0 down to z -5.5, the bottom of the tip band, so the whole seam is enclosed and the hair only ever sees the sleeve's smooth outside and the tip's working part below it. The sleeve outline is 15.2 x 10.2 mm at the bottom, 15.9 x 10.9 mm at the top (post-addendum 10° nose; the 5° version was 10.3 mm at the top and does not fit the new paddles). Probe it with 100 µm monofilament (K1.10) at every tip change.

---

## 3. Tip family

Loaded edge length is the edge length in skin contact. Every edge is crowned (R 9 mm, index-nail value), so it grows with indentation δ: L = 2 x sqrt(2δ / κ), κ = 1/9 + 1/90 = 0.122 mm⁻¹; L = 4.0 mm at δ 0.25 mm, 5.7 mm at 0.5 mm, the full 8 mm at about 1.0 mm. Redteam-1 §5 estimates about 4 mm at 0.3 N, which is 0.075 N/mm, mid-window (0.05 to 0.15 N/mm). Sheet blades crowned in plan and laid at 45° act as a 12.7 mm crown. Measured on day 0 (§7.4).

| Code | Geometry | Loaded edge (at 0.3 N) | Edge radius | Width | Material | Sensory variable it isolates | Stage gate |
|---|---|---|---|---|---|---|---|
| W | symmetric wedge, two 45.7° faces (88.6° included) | about 4 mm [EST], 8 mm max | 0.4 mm | 8 mm | PETG, printed on its side | DEFAULT; a symmetric edge so both stroke senses of the bidirectional rake are identical scratches | Stage 0 wand and first human session (H0, H1) |
| B45 | 1.0 mm plate at 45°, pulp lump behind | about 4 mm [EST], 8 mm max | 0.5 mm (full half-round of the plate) | 8 mm | PETG, printed on its side | nail-like thin plate vs wedge at similar radius; stroke-sense asymmetry (plate-first +X vs edge-first -X) | Stage 0 wand; Stage 1 human sessions |
| B45-12 | as B45, 12 mm plate, lump 9 mm | about 4 mm [EST], 12 mm max (needs 2.2 mm indentation) | 0.5 mm | 12 mm | PETG, printed on its side | width: hair collection ahead of the plate and loaded length at higher force | Stage 2 matrix (after B45 is characterised) |
| A45 | 0.8 mm nylon sheet at 45° on a carrier | about 4 to 5 mm [EST] | 0.3 mm | 8 mm | nylon 6/6 (pick or sheet) on PETG | radius 0.3 vs 0.5 mm at constant geometry (vs B45) | GATED: L9 tape test at 2.4 N and L10 forearm sharpness below 7 at 0.6 N first; then W1 and W2 only, never W3 |
| E | B45 geometry: 1.0 mm nylon blade on a TPU 90A pad in a dovetail | about 4 to 5 mm [EST] | 0.5 mm | 8 mm | nylon blade, TPU 90A pad, PETG carrier | soft backing behind the edge (damping, local give) vs B45 | Stage 2, only after B45 is characterised with the leaf spring active |
| H | 3 mm steel ball on a drafted cone | contact circle about 4 mm diameter (Hertz, 0.3 N) | 1.5 mm (sphere) | 3 mm | G25 chrome-steel ball in PETG | edge vs no edge: the massager baseline that every edge tip must beat | Stage 0 control; every blind pair starts against H |
| P | trimmed press-on nail on a convex R 8.5 mm bed | about 4 mm [EST] | 0.4 to 0.5 mm with two nested nails; 0.3 mm max with one | 8 to 9 mm | ABS press-on (two nested), PETG carrier | a real nail's shape and material vs our printed W and B45 | Stage 0 with nested nails; a single-thickness P is A45-class and gated |

All edge radii are post-finishing targets verified per §6. Nothing below R 0.4 mm goes on the scalp before the A45 gate is passed (red line 11).

---

## 4. Per-tip drawings in words

Every tip is the TM1 tang (z 0 to 12.0) plus the shoulder cone and 14 x 9 mm band (z 0 to -5.5) described in §2.1. Only the working part below z -5.5 differs. X is the stroke, Y runs along the edge. Masses are for solid PETG (1.27 g/cm³) and exclude the 0.18 g steel slug.

### 4.1 W, symmetric wedge (default)

Hull of the band bottom (x ±7, y ±4.5, z -5.5) and an R 0.4 mm apex cylinder, 8 mm long in Y, centred at x 0, z -12.1: a wedge 7.0 mm tall whose faces run from the band's ±X edges to the apex at 45.7° to the scalp plane (88.6° included). Edge lowest point x 0, z -12.5. End faces taper from 9 to 8 mm. Crown: intersected with an R 9 mm cylinder along X, so the edge ends at y ±4 sit 0.94 mm higher than the centre. Plan corners hand-rounded to R 1.5 mm. Volume 1,429 mm³, 1.8 g. Convex and symmetric, so both stroke senses see the same face.

### 4.2 B45, 45° nail-mimic plate

A 1.0 mm plate rises at 45° toward +X from an edge cylinder (R 0.5 mm) at x -0.35, z -12.0 (edge lowest point z -12.5) to the band, clipped at the band plane. Its underside is the whole +X face, so the +X stroke (loaded sense, "plate-first") looks like W's face ending in a thin plate. A drafted pulp lump, the hull of the band and a 0.5 mm cylinder 3.6 mm up the plate (x 2.20, z -9.45), fills the space behind. On the -X side this leaves an open 68° V between plate and lump, 3.6 mm deep. In a -X stroke ("edge-first", plate trailing like the pulled nail of tip-interface §1.4) hair climbs the plate into that V (§10.4). Crown R 9 mm, plan corners R 1.5 mm. Volume 1,299 mm³, 1.65 g. Slot mode drops the plate and cuts the lump back to the plate's upper-face plane for a 1.0 mm nylon sheet.

### 4.3 B45-12, width variable

Identical to B45 with a 12 mm plate. The lump stays 9 mm wide, so the outer 1.5 mm at each end is a free 1.0 mm plate that is rounded in plan to R 1.5 mm. The crown raises the edge ends 2.3 mm, so at light force the loaded length equals B45's and the extra width mainly changes how much hair the 12 x 9.5 mm plate collects. The working part is clipped at the band plane, which removes 0.7 mm tall plate ends that would otherwise have pushed into the seam sleeve (fixed in this revision). Volume 1,335 mm³, mass 1.70 g.

### 4.4 A45, R 0.3 mm (gated)

A45 is a carrier in slot mode. Its lump is the B45 lump (0.4 mm cylinder at x 2.20, z -9.55) cut back by the plane of the sheet's upper face: a true 45° bonding face of 50 mm², running from the lump bottom at z -9.67 to the band plane at x 5.68. The blade is a 0.8 mm nylon sheet (a Dunlop nylon 0.88 mm pick filed flat is the cheapest source) cut to 8 x 9 mm with a convex R 9 mm free end and R 1.5 mm corners, edge filed to R 0.3 mm, then bonded with CA on the face with its top butted under the band; the edge lands at about z -12.5, the same as W. The earlier revision shifted the lump 0.8 mm in X instead, which left a 36° bonding face; that is fixed. Carrier volume 1,227 mm³, 1.56 g plus a 0.07 g blade.

### 4.5 E, pulp-backed blade

Carrier: a 3.0 mm drafted block under the band (14 to 11 mm in X, 9 mm in Y, bottom z -8.5) with a dovetail slot through Y, 5.0 mm at the mouth, 7.0 mm at the top, 2.0 mm deep. Pad (TPU 90A): a rail 4.7 / 6.7 mm wide, 1.85 mm tall (0.15 mm clearance per side) on a 10 x 10 x 6 mm block with a 45° +X face from x 5, z -8.5 to x -1, z -14.5 and a 10° rear draft; it slides in along Y. Blade: 1.0 mm nylon, 8 x 9 mm, convex R 9 mm end, R 1.5 mm corners, CA-bonded on the 45° face with 2.0 mm overhang (the `PART = "blade"` STL is a scribing template). Edge lowest point about z -16.5 after radiusing to R 0.5 mm, 4.0 mm lower than W: set the float down-stop 4.0 mm higher. Carrier 1.56 g, pad 0.60 g, blade 0.08 g.

### 4.6 H, 3 mm ball control

A cone drafted from the band down to a Ø 4.0 mm end at z -11.0. A spherical cup of R 1.55 mm centred at z -11.3 holds a 3.0 mm chrome-steel ball by CA; the ball centre is 0.3 mm below the cone end, so the cup holds 1.25 mm of the ball (less than a hemisphere, so the glue is the retention, with about 12 mm² of bond) and the ball protrudes 1.8 mm. Ball bottom z -12.8, 0.3 mm below W's edge. The tip-interface sketch had a 2 mm parallel stem; the drafted cone replaces it because H-4.3 forbids necks. Volume 1,327 mm³, mass 1.68 g plus a 0.11 g ball. `PRINTED_BALL = true` prints the ball solid if no ball is at hand.

### 4.7 P, press-on nail reference

Carrier: hull of the band and two R 1.0 mm bosses along Y at x 5.0, z -9.0 and x -0.5, z -10.5, carved to a convex R 8.5 mm bed (a size 1 to 2 nail's underside) about an axis through x -4.52, z -6.0 rising toward +X at 45°. At y 0 the bed spans z -6.9 to -10.6; at the sides it reaches z -11.3 (a patch about 7.5 mm long). The 10 mm nail sits concave side down, convex top facing +X and down, root at the top of the bed. Gel CA fills under the overhang so the unsupported overhang is 3 mm or less (redteam-2: ABS yields at the 7.2 N proof with 4 mm), and a fillet blends the root. Edge lowest point about z -14.3 (one nail) or -15.0 (two nested). Volume 1,441 mm³, 1.83 g plus 0.15 g of nail.

---

## 5. Materials and printing

### 5.1 PETG vs resin vs nylon for the edge

PETG is the printed-edge material for W, B45 and B45-12: a 1.0 mm plate scuffs and whitens rather than shattering, wear raises the radius (the safe direction), it survives 70 % IPA, and it prints a clean 1.0 mm plate from a 0.4 mm nozzle when the tip lies on its side. The side orientation matters twice: the edge cross-section is drawn by the perimeter toolpath (a continuous curve, layer lines parallel to the stroke, no 0.10 mm staircase across the edge), and drag bends the plate within each layer instead of across layer bonds. Use 0.10 mm layers, 3 perimeters, 100 % infill, one bright colour.

Standard SLA resin gives the best edge definition (0.05 mm features) but is brittle and skin-sensitising if under-cured; red line 9 bans it at the scalp. In SP1 it is only a geometry master; a tough resin can be revisited in SP2 after a drop test and the 3x proof load.

Nylon 6/6 is best for blades of 0.8 mm and thinner: ductile, polishes glossy, takes up a little water like keratin. It prints poorly, so SP1 uses stock (Dunlop nylon 0.88 and 1.0 mm picks, or 1.0 mm sheet) for the A45 and E blades and B45 slot mode. PLA is excluded from every tip and allowed only for the wand handle.

### 5.2 TPU 90A for the E pad and the seam sleeve

TPU 90A prints reliably in sections of 0.8 mm and up on a direct-drive extruder at 15 to 20 mm/s, holds a dovetail rail without tearing, tolerates sweat and short IPA wipes, and is soft enough to stretch over the paddle nose. It never forms an edge (DR8: an elastomer at the contact grabs hair at µ above 1). Note what E can and cannot test: a 10 x 10 x 6 mm pad of 90A (Young's modulus about 20 MPa [EST]) is about 120 N/mm in shear and 330 N/mm in compression, roughly a thousand times stiffer than the 0.1 to 0.25 N/mm leaf. E therefore isolates soft backing (damping of edge chatter and micro-rocking, a less "ringing" contact), not macroscopic compliance. If the experiment needs compliance in the tip, the next E is a slotted 85A pad or a 0.3 mm leaf inside the tip (§10.8).

### 5.3 Fasteners, keeper and adhesives

Thin CA for nylon-to-PETG and nail-to-nail joints, gel CA for gap filling under the P overhang and the sleeve rim, 5-minute epoxy as the alternative for the steel keepers. Nylon bonds poorly to CA unless the faying face is sanded with 240 grit and wiped with IPA. Never let adhesive squeeze out onto a working face: a cured drop at the edge is a burr.

### 5.4 Press-on nail trimming for P

Choose a full-cover ABS press-on of size 1 to 2 (8 to 9 mm wide, about 0.6 mm thick). A single nail can only be filed to R 0.3 mm (half its thickness), which is below red line 11, so for first human sessions nest two nails of the same size (they nest naturally), wick thin CA between them and clamp for 1 minute, giving about 1.2 mm. Cut the cuticle end with flush cutters so the total length is 10 mm, keeping the factory free-edge shape. File the free edge square, then roll it to a full half-round of R 0.4 to 0.5 mm (§6), round the plan corners to R 1 to 1.5 mm, sand 400 to 2000 grit. Bond on the bed with gel CA, root at the top of the bed, fill under the overhang, fillet the root. ABS crazes in IPA (safety §8), so clean P with soap and water, treat it as a weekly consumable and discard it at the first sign of crazing.

---

## 6. Edge radius control and verification

**The failure that matters** is not a slightly wrong radius but a flat with two broken corners: a 1.0 mm plate end sanded flat and only softened at the corners is two edges of R 0.1 to 0.2 mm, sharper than A45, although a caliper still reads 1.0 mm.

**Achieving the radius.** Printed on its side, W's apex comes off close to the modelled R 0.4 mm (the outer perimeter traces the arc; the bead half-width, about 0.22 mm, is smaller than the radius) and B45's plate end comes out near half-round, so sanding refines rather than creates the radius. Clean the seam and stringing first, then wrap 400 grit wet-and-dry round a flat stick and stroke along the edge (Y) while rolling the stick through the included angle: 90° for W, the full 180° over the plate end for B45, B45-12, E and P, so the end becomes one continuous half-round tangent to both faces. Repeat the rolling stroke with 600, 1000 and 2000 grit, wet, until no scratch is visible at 10x (Ra below 1 µm, DR8). PETG and ABS may get one optional 1 s pass with a lighter flame; nylon gets plastic polish instead. Round the plan-form corners to R 1.5 mm with a nail file. For A45, file the 0.8 mm sheet edge with two blended 0.3 mm chamfers before bonding, then polish.

**Verifying it.** Four checks, all cheap:

| Check | Method | Pass |
|---|---|---|
| Silhouette vs reference | 10x loupe, edge-on, back-lit on white card, beside a drill-bit shank: 0.6 mm shank = R 0.3, 0.8 mm = R 0.4, 1.0 mm = R 0.5 | edge at least as round as its target shank, one continuous arc, no flat |
| Macro photo | phone macro, edge-on, next to a ruler; fit a circle by eye or count pixels across three points | radius within 0.05 mm of target or larger; photo filed with the tip code |
| Burr | cotton ball dragged along the edge both ways, then back of the hand at about 1 N | no fibre snags, nothing catches |
| Tape test (L9) | 10 mm rod, 3 layers of 50 µm polyester or PTFE tape; tip on the wand; 1.0 N then 2.4 N on a kitchen scale; slide 50 mm at about 50 mm/s, 3 passes each way, both senses for 45° tips, then across the corners | no cut through any layer at 2.4 N; A45 must pass at 2.4 N or stays gated |

An optional fifth check gives a direct profile: press the edge 1 mm into firm modelling putty, cut the impression across with a fresh blade and view the cut face under the loupe against the drill shanks.

**Wear and re-verification.** PETG edges scuff and whiten, which raises the radius and makes the sensation milder over tens of hours; nylon polishes and stays put; ABS crazes. Inspect under the loupe before every session (30 s), re-run the tape test after 10 sessions or any drop, and replace any tip with a chip, crack, crazing, a visible wear step, or after about 10 h of use.

---

## 7. The Stage-0 hand wand

### 7.1 What it is

One TM1 holder (the standard `paddle_with_pocket` paddle with its pocket, magnet and seam sleeve) clamped to the free end of a 0.30 x 12.7 mm spring-steel feeler leaf, whose other end is clamped in a 150 mm printed handle (`hand_wand_handle.scad`: 150 x 22 x 16 mm grip with R 8 mm corners, plus a 28 x 30 x 16 mm clamp block). Both clamps hold the leaf without holes: the leaf lies on a window floor and is pressed by a printed bar with a 0.25 mm locating groove, 4 x M3 x 8 in the handle (bar 24 x 24 x 3.2 mm) and 2 x M3 x 8 in the paddle (bar 24 x 8 x 3.2 mm). The leaf runs along Y, the handle's axis, and the paddle hangs below its free end, so the wand strokes across its own axis (X), exactly as each nail on the rig is cantilevered along Y and strokes in X. The leaf is the same part number as the rig's leaves, so a tip, a force and a spring rate found on the wand are the rig's.

### 7.2 Leaf length and stiffness

The leaf is 80 mm long: 27 mm in the handle block, 38 mm free between the handle face and the paddle's -Y face, 14 mm through the paddle root, 1 mm to trim. The leaf also flexes 3 mm inside each wall slot (from the bar edge to the wall face) and the tip sits 4 mm beyond the paddle bar edge, so the stiffness at the tip is k = EI / (a³/3 + a²b + ab²) with a = free length + 6 mm, b = 4 mm, EI = 200 GPa x (12.7 x 0.3³ / 12) mm⁴ = 5,715 N mm².

| Free length (handle face to paddle) | 30 mm | 35 mm | 38 mm (default) | 40 mm | 45 mm |
|---|---|---|---|---|---|
| k at the tip | 0.27 N/mm | 0.19 N/mm | 0.155 N/mm | 0.14 N/mm | 0.10 N/mm |

At the default 0.155 N/mm, inside DESIGN-FREEZE's 0.1 to 0.25 N/mm band, the tip deflects 1.9 mm at 0.3 N, 3.2 mm at 0.5 N, 6.5 mm at 1.0 N and 15.5 mm at the 2.4 N per-nail cap. Leaf root stress at 2.4 N is about 600 MPa, well inside hardened feeler stock. The earlier SCAD comment used 3EI/L³ on the face-to-face length and gave 0.155 N/mm for 48 mm; the true value at 48 mm is 0.09 N/mm, below the freeze band, so the default is now 38 mm. The leaf bend also rolls the paddle about X by about 1.8° per mm of tip deflection (6° at 0.5 N), which shifts the contact point along the crowned edge by under 1 mm: harmless.

### 7.3 Building it in 3 hours

The prints run unattended the evening before (about 4.5 h of printer time, [EST] for a typical 0.4 mm nozzle machine): plate A in PETG at 0.20 mm (handle, two bars, the paddle with the magnet pause at 23.1 mm print height, a spare paddle), plate B in PETG at 0.10 mm (W x 2, B45 x 2, H, A45 carrier, P carrier x 2, tips on their sides or tang down per README §3), plate C in TPU 90A (two seam sleeves). Hands-on work:

| Time | Step |
|---|---|
| 0:00 to 0:20 | Remove supports, clean prints. Test-fit every tang in the paddle pocket: slides home without force, cannot enter rotated. Sand any support scar on a tang face. |
| 0:20 to 0:45 | File flats on 6 x 1 mm steel discs to 3.9 mm (or cut slugs); bond one flush into every tang-end notch with epoxy or gel CA. CA the 3 mm ball into H. |
| 0:45 to 1:35 | Edge work per §6: W and B45 rolling-stroke sanding 400 to 2000; A45 nylon blade cut, filed to R 0.3 and bonded; P nails nested, trimmed, filed to R 0.4 to 0.5 and bonded. |
| 1:35 to 2:00 | Cut the leaf to 80 mm, round its corners R 1 mm and deburr both ends. Clamp it in the handle (bar, 4 x M3 x 8, snug, not crushing), set 38 mm free length, clamp the paddle (bar, 2 x M3 x 8). Trim any excess leaf flush with the paddle +Y face and cover the paddle root and leaf end with one turn of electrical tape (the wand root has open slots and bar seams within reach of long hair). Fit the seam sleeve, dot of gel CA at its top rim. |
| 2:00 to 2:30 | Calibrate: press the tip onto the kitchen scale, read force at 2, 4 and 6 mm of deflection against a ruler; trim free length until k is 0.13 to 0.18 N/mm. Practise hitting 0.3 and 0.5 N on the scale ten times each (test-protocols: people press 2 to 3 times too hard). Breakaway per L6(b) for each tip: 4 to 8 N. |
| 2:30 to 3:00 | Tape test (L9) and cotton-ball burr test for every tip; write blinding codes (README §5) and fill the key card and tip box. |

### 7.4 What to test with it

In order, before any motorised part is ordered: (1) L9 tape test and L10a forearm screen per tip; A45 joins only after L9 at 2.4 N and sharpness below 7 at 0.6 N. (2) Loaded edge: ink the edge with whiteboard marker, press it on the forearm or on carbon paper over 10 mm foam at 0.3 and 0.5 N, measure the mark (about 4 mm expected at 0.3 N). (3) Wig head L8.1 static reach and L8.9, 200 strokes per tip, B45 counted per stroke sense. (4) Scalp H0: 10 strokes per tip, 30 to 40 mm at about 80 mm/s and 0.3 to 0.5 N, crown then occiput, along and across the lie; side photo of contact fraction at 0.3 and 0.5 N; blind W vs H and B45 vs H with a helper swapping coded tips; preference among B45 +X, B45 -X and W bidirectional; P vs W as the "real nail" check.

### 7.5 Go / no-go

From DESIGN-FREEZE §3 Stage 0 and test-protocols H0: GO to Stage 1 when the nail visibly reaches skin through Michael's hair at 0.5 N or less, W or B45 clearly beats H on the scalp (by 3 points or more on the realism scale, blind), and no tip captures hair in 200 wig strokes. NO-GO: fix the tip first (reach, radius, width), before any motorised build; if no tip reaches the skin, the engagement, leaf and paddle questions go to the top of the iteration map.

---

## 8. The paddle interface to the hand

`paddle_with_pocket.scad` is the part the mechanical lead puts at the free end of each of the three hand leaves. Since DESIGN-FREEZE-ADDENDUM-1 (D2 to D5) the hand has 24 mm nail pitch in Y, 10° draft on every paddle face, a centre paddle with a 9 mm riser, one shared knuckle-plate slot sealed by a bonded slack membrane, and 5.0 mm leaf travel to the hard stop (mechanical.md §8). There are now two paddles, built from the same file:

| STL | Setting | Qty on the SP1 hand | Where | Leaf floor | Leaf floor to W/B45 edge |
|---|---|---|---|---|---|
| `paddle_with_pocket.stl` | `RISER = 0` | 2 | outer nails L (−8, −24) and R (+8, +24); also the wand | z 31.5 | 44.0 mm |
| `paddle_with_pocket_riser9.stl` | `RISER = 9` | 1 | centre nail C (0, 0); its leaf crosses one level above L's | z 40.5 | 53.0 mm |

Geometry in the TM1 frame (z 0 = pocket mouth; z0 = 25 + `RISER`):

| Zone | Geometry |
|---|---|
| Nose, z 0 | 14 x 9 mm, R 1 mm corners, equal to the tip band so the sleeve spans the joint |
| Drafted body, z 0 to 25 | grows at 10° per side on all four faces (`DRAFT_X = DRAFT_Y = 10`), to 22.8 x 17.8 mm at z 25 (the section in the knuckle plate); no steps, no fastener heads. Identical on both paddles |
| Riser, z 25 to z0 | `RISER = 9` paddle only: straight 22.8 x 17.8 mm section, z 25 to 34 |
| Transition, z0 to z0 + 3 | to the 28 x 14 mm (R 2 mm) root block: widens in X, and narrows in Y from 17.8 to 14 mm (above the plate, inside the boot) |
| Root block, z0 + 3 to z0 + 10 | clamp window 24.2 x 8.4 x 3.5 mm deep from the top; leaf floor at z 31.5 (`RISER = 0`) or 40.5 (`RISER = 9`); leaf slots 12.9 x 1.0 mm through both Y walls; clamp bar 24 x 8 x 3.2 mm with a 12.9 x 0.25 mm groove; 2 x M3 x 8 at x ±9.5 into 2.6 mm thread-forming holes 5 mm deep (4.0 mm for heat-set inserts) |
| Pocket | `tm1_pocket()`: 10.3 x 4.3 x 12.5 mm, 0.6 mm lead-in, N52 6 x 2 recess at z 11.9 to 14.0 (print pause at 23.1 mm print height, or 32.1 mm on the riser paddle) |
| Seam sleeve | TPU 90A, z +3 to −5.5, now drawn for the 10° nose: 15.2 x 10.2 mm at the bottom, 15.9 x 10.9 mm at the top |

**How it clamps to the leaf (checked against mechanical.md §8.6).** The 0.30 x 12.7 mm leaf runs along Y over the window floor and out through both wall slots (`LEAF_THROUGH = true`); the bar's 0.25 mm groove locates it in X and, being shallower than the leaf, makes the bar press the leaf rather than the floor. No hole is drilled in the leaf, so there is no stress raiser and the free length can be trimmed at will. The screws sit 1.85 mm clear of the leaf edges with 0.8 mm of bar outboard of each hole. Screw length works out: an M3 x 8 through the 3.2 mm bar (bar underside 0.05 mm above the floor once the leaf is under it) reaches 4.75 mm into the 5 mm hole. The paddle clamp uses M3 (aluminium on the hand, 0.3 N·m, mechanical.md §8.6 and §12); the M2 screws in mechanical.md belong to the palm-side root clamp bars (P34, 2 x M2 at ±8.6 mm) and the plate and lid, not to the paddle. The draft and riser changes do not touch the clamp: window, slots, bar and screw positions are the same on both paddles, only 9 mm higher on the riser one. The leaf roots are pre-tilted on the palm side (P32: L 4.4°, C 4.7°, R 5.0°), so the paddle clamp stays square to the paddle and each paddle hangs vertical at the nominal 2.67 mm deflection.

**Knuckle plate: shared slot and membrane (ADDENDUM-1 D4).** The freeze's individual ≥ 4 mm clearance holes cannot be made: with the 17.8 mm section at z 25 they would need 26.8 mm at 24 mm pitch. The hand uses one shared slot (≥ 4.5 mm clear of L and R, 6.0 mm of C) sealed by one slack 0.25 mm Shore 40A silicone membrane bonded to each paddle at z 26 to 28 with silicone adhesive, with no sliding contact (mechanical.md §8.7). On the paddle side that needs only a clean, bondable band at z 26 to 28: no CA, varnish or slicer seam there (put the seam on an X corner). When the leaf deflects the paddle rises, the plate crosses a narrower part of the body, and the clearance to the slot edge grows.

**Gap between paddles at the knuckle plate (24 mm pitch, 10° draft), from the SCAD parameters.** Section at z 25: 9 + 2 x 25 x tan 10° = 17.82 mm, so the static gap is 24 − 17.82 = **6.18 mm** (mechanical.md: 6.2 mm). For the worst case the paddle rolls about X as its leaf bends (1.63, 1.76, 1.87° per mm for L, C, R, zero at 2.67 mm by the pre-tilt), pivoting at the root-side bar edge on the leaf floor. The plate section is 6.5 mm below the leaf floor on the outer paddles and 15.5 mm on the riser paddle. Every combination of 0 to 5.0 mm on each leaf (D5) was swept:

| Model | L–C | C–R | Rule |
|---|---|---|---|
| Section at z 25 shifted sideways by roll only (the §8.7 method, levers 6.5 / 15.5 mm) | 4.48 mm worst | 4.58 mm worst | ≥ 3 mm |
| Rigid paddle in the 1.6 mm R 90 mm plate shell: roll, rise of the paddle with the leaf, spherical plate, transition narrowing | 4.72 mm worst (L on its stop, C unloaded); 5.15 mm in normal use (±2 mm of nominal) | 5.34 mm worst | ≥ 3 mm |

Both models meet mechanical.md §8.7's ≥ 4.2 mm. Its 4.2 mm figure matches the §8.7 method with a 19.5 mm centre lever (a 13 mm level step), so it is conservative for the 9 mm riser as built. Hair-exposed gaps below the plate, same sweep: paddle bodies ≥ 5.1 mm, seam sleeves ≥ 7.6 mm (the 10° sleeve is 0.56 mm wider in Y at its top than the old one, and this is included). Tip-edge gaps are mechanical.md's (W ≥ 8.4 mm, B45-12 ≥ 4.4 mm). No gap within 25 mm of the scalp falls in the 0.04 to 3 mm band.

**What the mechanical lead must match.**

1. The pocket exactly as `tm1_pocket()` (do not re-draw it) and a 14 x 9 mm nose, so every tip and the sleeve fit both paddles.
2. Edge position: the W, B45, B45-12 and A45 edge is 12.5 mm below the pocket mouth, 37.5 mm below the knuckle plate at 25 mm protrusion, and 44.0 mm below the leaf floor (53.0 mm on the riser paddle). H is 0.3 mm lower, P 1.8 to 2.5 mm lower, E 4.0 mm lower.
3. Leaf: 0.30 x 12.7 mm feeler stock along Y; free length measured from bar edge to bar edge (add 6 mm to the face-to-face length) and the tip 4 mm beyond the paddle bar edge, as in §7.2, or the leaves come out about half as stiff as intended: the naive 3EI/L³ overstates k by 1.9 to 2.1 times at the hand's lengths. mechanical.md §8.3 applies the correction.
4. Mass per nail station on the float [EST, the scale decides, mechanical.md §6.5]: outer paddle 11.2 g solid, about 4.5 to 5.5 g at 2 perimeters and 10 % gyroid; riser paddle 15.8 g solid, about 5.7 to 6.7 g. Bar 0.7 g, 2 aluminium screws 0.4 g, magnet 0.4 g, sleeve 0.4 g, tip 1.6 to 2.2 g. mechanical.md budgets 5.0 / 6.5 g per paddle. Wand paddles are printed at 4 perimeters and 30 % (mass does not matter there).
5. Deviations from the freeze, both now ruled on in DESIGN-FREEZE-ADDENDUM-1. DESIGN-FREEZE §1.7 calls the paddles "1 mm thick", but a TM1 pocket needs a body at least 9 mm thick (14 x 9 mm nose, 2.35 mm walls around the 4.3 mm pocket); accepted as D1. The Y faces carried 5° of draft at the freeze's 20 mm pitch, because 10° there would leave 2.2 mm between neighbouring paddles, inside the forbidden 0.04 to 3 mm band. At the 24 mm pitch of D2 they carry the full 10° (D3), and the gaps above hold.
6. Attack angle lives in the tip (`POCKET_TILT = 0`), as DESIGN-FREEZE §1.8 implies; tip-interface §5.2's 35° / 45° / 55° holder variants are not used in SP1.
7. Leaf travel to the hard stop is 5.0 mm (4.5 to 5.5 mm, D5). At the stop the paddle rises 5 mm in the slot and rolls 3.8 to 4.4° past vertical. Both are inside the gaps above, and the pocket mouth is still 20 mm below the plate.
8. `ROOT_Y` stays 14 mm. mechanical.md §8.9 offers `ROOT_Y = 18` to remove the Y-narrowing transition (+0.6 g per paddle). It is not needed: the narrowing is above the plate, inside the boot, and only widens the gaps. The parameter is there if MECH wants it.

---

## 9. Tip BOM

Approximate single-unit retail prices in USD, 2026. Printed parts are costed pro rata from 1 kg spools. Items marked "test kit" are already on the test lead's list (test-protocols §Q8) and are not in the total.

| # | Item | Specification | Qty | Use | Price (USD) |
|---|---|---|---|---|---|
| 1 | PETG filament, one bright colour | 1.75 mm; about 130 g used | 130 g | all tips, carriers, paddles (hand and wand, table below), bars, handle | 3 |
| 2 | TPU 90A filament | 1.75 mm; about 10 g used | 10 g | seam sleeves x 6 (hand 3, wand 1, 2 spares), E pads x 2 | 1 (spool 29 if not owned) |
| 3 | Neodymium magnets | N52, 6 x 2 mm disc, axial | 50 pack | one per pocket | 9 |
| 4 | Neodymium magnets | N52, 6 x 3 mm disc, axial | 20 pack | breakaway tuning (§2.3) | 6 |
| 5 | Steel keeper discs | mild steel 6 x 1 mm (or 1 mm sheet 100 x 100 mm) | 50 pack | tang keepers, flats filed to 3.9 mm | 7 |
| 6 | Feeler stock | spring steel 0.30 x 12.7 x 305 mm (0.012 x 1/2 x 12 in) | 2 strips | wand leaf and spares (rig leaves on the mech BOM) | 8 |
| 7 | Press-on nails | ABS full cover, sizes 0 to 3, 100 or more | 1 box | P tips (two nested per tip) | 7 |
| 8 | Nylon picks | Dunlop nylon 0.88 mm | 12 pack | A45 blades | 5 |
| 9 | Nylon picks or sheet | Dunlop nylon 1.0 mm, or nylon 6/6 sheet 1.0 mm | 12 pack | E blades, B45 slot blades | 5 |
| 10 | Steel balls | G25 chrome steel, 3.0 mm | 100 pack | H tips | 5 |
| 11 | Screws | M3 x 8 socket or button head | 50 pack | wand bar 4, wand paddle bar 2 (the SP1 hand's 6 aluminium M3 x 8 paddle-clamp screws are on the mechanical BOM, mechanical.md §12) | 5 |
| 12 | Cyanoacrylate | thin and gel, 20 g each | 2 | blades, nails, balls, sleeve rim | 8 |
| 13 | Epoxy | 5-minute, twin syringe | 1 | keepers, P fill (alternative) | 6 |
| 14 | Abrasive paper | wet-and-dry 400, 600, 1000, 2000 grit | 1 sheet each | edge radius (§6) | 8 |
| 15 | Nail files and buffer | 180 / 240 file, 3-way buffer block | 1 set | plan corners, P trimming | 4 |
| 16 | Drill-bit set | 0.5 to 3.0 mm by 0.1 mm | 1 | radius reference shanks (0.6, 0.8, 1.0 mm) | 10 |
| 17 | Marker and varnish | 0.3 mm permanent marker, clear nail varnish | 1 each | blinding codes | 5 |
| 18 | Tip box | printed block (30 g PETG) or pill organiser with foam | 1 | coded tip storage | 1 |
| | **Total** | | | | **103** |
| | Test kit (not totalled) | 10x loupe 8, 50 µm polyester tape 6, 10 mm rod 2, kitchen scale | | L9, §6 | (16) |

**Printed paddle parts (from `cad/tips/stl/`, PETG unless stated; mechanical.md §11 T1 to T4).**

| Ref | STL | Setting | Qty SP1 hand | Qty wand | Mass each [EST] | Print |
|---|---|---|---|---|---|---|
| T1 | `paddle_with_pocket.stl` | `RISER = 0`, outer paddle | 2 (L, R) | 1 + 1 spare | 4.5 to 5.5 g (hand), about 8 g (wand) | nose up, magnet pause at 23.1 mm |
| T2 | `paddle_with_pocket_riser9.stl` | `RISER = 9`, centre paddle | 1 (C), print a spare | 0 | 5.7 to 6.7 g | nose up, magnet pause at 32.1 mm; mark "C" |
| T3 | `paddle_clamp_bar.stl` | | 3 | 1 | 0.7 g | groove up |
| T4 | `tm1_seam_sleeve.stl` (TPU 90A) | 10° nose | 3 + 2 spares | 1 | 0.4 g | standing |

Hand paddles print at 2 perimeters and 10 % gyroid, with 4 perimeters around the screw holes (mechanical.md §8.9). Wand paddles print at 4 perimeters and 30 %. Each paddle takes one N52 6 x 2 magnet (item 3) and is clamped with 2 x M3 x 8. The boot membrane and Sil-Poxy that bond to the hand paddles (D4) are on the mechanical BOM.

The tip subsystem costs about $103 with filament costed pro rata, about $132 if a TPU 90A spool has to be bought. The Stage-0 wand alone needs items 1, 3, 5, 6, 7 and 10 plus screws, glue and abrasives: about $39 cash if screws, CA, abrasives and a marker are already in the shop, against the DESIGN-FREEZE estimate of about $30.

---

## 10. Risks and open questions

### 10.1 Audit summary

Fixed in the SCAD files and mirrored in `gen_tips_stl.py`: (1) slot-mode bonding face was about 36°, now a true 45° face; (2) B45-12 plate ends rose 0.7 mm into the seam sleeve, now clipped at the band plane; (3) clamp-bar screw holes broke out of the bar ends, now bar 24 mm and screws at ±9.5 mm (paddle and wand); (4) wand stiffness table overstated k 1.75 times, now corrected with a 38 mm default; (5) "tang down" orientation made the edge a layer staircase, now W, B45 and B45-12 print on their side at 0.10 mm; (6) single press-on cannot reach R 0.4 mm, nested nails now required; (7) E edge height and down-stop advice corrected; (8) W face angle and B45-12 crown comments corrected; (9) B45 hair-behaviour comment corrected.

Resolved after the addendum: the paddle Y draft is now 10° (was 5°, held back by the 20 mm pitch; D2 and D3), and the centre paddle has a 9 mm riser (§1, §8).

Kept as deliberate deviations: steel slug instead of a round disc; breakaway estimate at the low end of the band; H drafted cone with a glued ball; E pad 10 x 10 x 6 mm (8 mm blade); attack angle in the tip; TM1-B cross-bolt; solid paddle body (freeze "1 mm" paddle, accepted as ADDENDUM-1 D1); the freeze's "8 mm loaded edge" read as width, about 4 mm loaded at 0.3 N.

### 10.2 Edge radius vs safety

R 0.4 to 0.5 mm meets red line 11 but sits at the gentle end of the window; redteam-1 §5 shows it reads as a glide at 0.2 N per nail. The freeze's answer (crowned edge loading about 4 mm at 0.3 N or more per nail) is right on paper and is the day-0 wand question. Edges end up sharper than intended through a sanded flat with broken corners, adhesive squeeze-out, or slicer wall overshoot at the apex; the silhouette check and tape test catch all three, a caliper catches none.

### 10.3 The 0.3 mm gate

A45 and a single-thickness P are the only tips below the red line: human use only after L9 at 2.4 N and L10 sharpness below 7 at 0.6 N, then at W1 and W2 only (test-protocols N1). If A45 fails, the 0.3 vs 0.5 mm question moves to SP2 with another edge material, not to a relaxed test. Open: the proof load differs between safety §3.6 (about 7.5 N normal, 6 N lateral) and test-protocols L6(b) (2.4 N); tips are built for the higher one, and the test lead should name the gate.

### 10.4 Hair interaction of the B45 family

The B45 family is direction-dependent and the rig strokes both ways, so the -X (edge-first) stroke drives hair up the plate into the 68° V between plate and lump. That is an open V, not a closed aperture, but it is a concavity within 15 mm of the contact (scratch-model DR1) and a narrowing in H-4.3 terms. A convex profile would turn B45 into W with R 0.5 mm and remove the variable B45 exists to test, so the geometry is unchanged and the risk is put to the wig: L8.9 counts captures for B45 per stroke sense, and any capture in the -X sense moves B45 to one-way use or to a filled V (set `s_lump` to 1.5 mm, opening the V to about 80° and shortening it to 1.5 mm). Which sense feels more like a nail is itself an open question the wand answers on day 0.

### 10.5 Breakaway, retention and tip loss

The magnet alone is estimated at 3.4 to 4.3 N and the rest depends on sleeve friction, which varies print to print; below 4 N on L6(b), fit 6 x 3 mm magnets. Ways to lose something into the hair: a debonded keeper (the tip falls out), H ball or P nail. Mitigations: one bright colour, count tips in and out of the box every session, pull-test every tip weekly.

### 10.6 Wear

PETG edges blunt slowly (safe direction, but it biases long A/B series): re-measure after 10 sessions and keep duplicates from one print batch. TPU sleeves and pads foul with sebum and split at corners: replace weekly or when cut.

### 10.7 Cleaning

FDM parts are porous (safety §8), so scalp-contacting printed tips are weekly consumables. Each session: 70 % IPA wipe on PETG, nylon and steel with 1 minute flash-off; soap and water for ABS P (IPA crazes it); a soft brush through the B45 V and along the P root fillet, the two sebum crevices. Weekly: pocket cleaned with a pipe cleaner and IPA (sebum changes the breakaway). One tip set per person.

### 10.8 Other open questions

1. Loaded edge length at 0.3 N [UNKNOWN]: the §7.4 ink-mark test replaces the 4 mm estimate.
2. E cannot test compliance in the tip (pad about 1,000 times stiffer than the leaf): decide after B45 whether E is a damping experiment or needs a softer design.
3. The wand has no hard stop; force comes from scale practice and the visible leaf bend (15.5 mm at 2.4 N). A printed stop finger under the leaf is a 20-minute addition if practice proves unreliable.
4. Floating mass: three paddle and tip stations at mechanical.md's print settings take about 26 to 32 g [EST] (§8 item 5). mechanical.md §6.5 budgets 27.7 g for them, with 2 g of margin on the 92 g limit, so the scale (L1) decides. If the budget is over, the first fallback on the tip side is thinner paddle walls around the pocket, not a shorter paddle.

### 10.9 Post-addendum risks (24 mm pitch, 10° draft, riser, shared slot, 5 mm travel)

1. **Two paddle kinds.** The riser paddle is 9 mm taller and must sit on C only. Fitted on L or R, its leaf floor is at the wrong level and the edge 9 mm too low. Mark "C" on its root block. Its magnet pause height differs: 32.1 mm against 23.1 mm.
2. **Old sleeves and old paddles.** A 5° paddle printed before the addendum is 4.4 mm narrower in Y at the plate and takes a 5° sleeve. Scrap the old ones: mixing them changes the gaps and the boot fit.
3. **Gap margins.** Static 6.18 mm between paddles at the plate. Worst case 4.5 to 4.7 mm with any leaf at 0 to 5 mm (§8), against the ≥ 3 mm rule. Past the stop the margin goes quickly. With travel allowed to 6 mm the worst gap is 4.6 mm; at 7 mm it is 3.9 mm (C–R, falling about 0.7 mm per extra millimetre). So L2 must confirm the stop at 5.0 ± 0.3 mm before any hair test.
4. **Membrane bond.** The D4 boot is bonded to each paddle at z 26 to 28. A PETG surface with seam zits or CA residue there bonds badly, and a peeled boot leaves a 0.04 to 3 mm gap at the plate. Keep that band clean, and inspect it with the K1.10 monofilament probe at every hand assembly.
5. **Sensation.** The 24 mm pitch is for the SENSATION GATE to assess (D2). Nothing in the tips changes with pitch, so a tip result from the wand still transfers.
