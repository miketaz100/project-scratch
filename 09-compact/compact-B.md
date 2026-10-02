# COMPACT B — THE FLAT DECK

**Project SCRATCH · 09-compact · 2026-10-01 · Compact team B.** Builds to COMPACT-BRIEF.md and the director's yaw amendment. Inherits DESIGN-FREEZE §1.7–1.8, ADDENDUM-1 (D1–D13), mechanical.md §6–§9 ("mech"), tips.md §2/§8, judge-2 §0 (F1–F5), redteam-1 ("RT1"), redteam-2 §1–3, §11 ("RT2"), concept-A §3–4 ("A"), team-F §2 and team-A §1 (flat single-motor mechanisms). Units mm, N, g. Heights **h** are measured from the scalp apex (freeze Z = h + 4). **[CHOICE]** = my number; **[EST]** = estimate, arithmetic shown; **[TEST]** = decided on the bench; **[FLAG]** = deviation from a frozen item or the brief, not silently made.

**One sentence.** A 181 × 98 mm open PETG tray lies on the crown on four hard-hat crown straps; inside it a Feetech STS3032 lying flat (shaft up) turns a 25 mm crank whose pin runs in a scotch-yoke slot on a U-shaped carriage that slides 50 mm along X on a 70 mm MGN7 rail; the carriage carries a 40 mm vertical MGN7 on which the three-nail hand floats on its own weight plus a clip-on constant-force spring; a 623ZZ roller on the float meets a 31° ramp fixed to the tray at each end of travel, so the hand rises 6 mm and every reversal is in the air; the contact chord is 30 mm (ramp sets for 25 and 36), 1–2.5 strokes/s.

**Headline numbers.** Height 66 mm above the apex at nominal seating, 69 mm worst case (band seated 5 mm low, hand at its up-stop). Footprint 181 × 98 at yaw 0. Mass 245 ± 15 g without the yaw axis, **280 ± 15 g with it** (over the 250 g line by ~30 g: §11 says what buys it back). Force 0.67 / 1.11 / 1.5 N, mechanical constant to ±2 % over ±5 mm of seating. Stroke servo margin 12× on torque, 1.2× on speed at 2.5 strokes/s and the 30 mm chord (trapezoid required). Band stability margin 3.4 upright at µ 0.3.

---

## 0. Three things the brief did not know, settled first

**0.1 The hand is 169 mm wide, and that is physics, not packaging [FLAG].** mech §8.3's leaves (0.30 × 12.7 feeler stock, 36–42 mm free, rooted outboard) give 0.12–0.18 N/mm **and** 180–210 N·mm/rad of torsion (D13). Torsional stiffness per unit bending stiffness scales as a²: GJ/a ÷ k = 4Ga²/(3E) = 0.51 a². Any leaf short enough to root outboard inside a 100 mm width (face-to-face ≤ 12 mm) has 10–20× less torsion at the same rate: a 0.3 N drag twists it 20–35°, the edge wanders 15–25 mm in X. Thinner/wider stock (25 × 0.127 mm, 14 mm free: k 0.19, torsion 55 N·mm/rad) still twists 14°. So the **leaf length stays ~40 mm, and the only way into 100 mm is to root the leaves inboard, which means crossings**. mech §8.2 already has one crossing (C over L, the 9 mm riser). Inboard roots need L and R to cross C and C to cross L: a cycle, unless one paddle lets a leaf pass *through* its riser. My resolution (§1.2): L and R get `RISER = 16` (level 1, floor h 52.4) and run inboard side by side over C's level-0 block (their 12.7 mm leaves are at X −14.4…−1.7 and +1.7…+14.4, 3.3 mm apart); L's riser is **necked** to a 10 × 17.8 mm post on its −X side between z 33 and 42 so C's level-0 leaf (X ±6.35) passes beside it toward −Y; C roots at Y −45.5 to −55.5. Width 86 mm (Y −55.5 to +31). L and R leaves become 0.20 mm stock at 25 / 20.5 mm free (k 0.12 / 0.18; torsion 8.7° at 0.3 N, mech's is 3.6–4.2°; edge wander 6.5 mm, still inside the 4.5 mm slot clearance at the plate because the plate is only 19 mm below the leaf). C stays 0.30 × 38.5. **This is a request to the tip lead for a `NECK` parameter in paddle_with_pocket.scad**, same class as D3's `RISER`; nothing below the knuckle plate changes, so P30/P31/P35 and all tips are reused as printed.

**0.2 The hand's own stack sets the floor at ~60 mm, not 40–50.** Paddle protrusion below the knuckle plate 37.5 mm (freeze §1.7, 25 mm to the pocket mouth + 12.5 mm pocket; H-4.5), plate 1.6, level-0 clamp 5.2, level step 12.4 (needed for C's block + 5 mm travel + 1 mm under L/R's leaves), level-1 clamp 5.2, lid 1: the lid hump is at **h 59.5** with the hand at its down-stop. The seed's 40–50 mm is reachable only with a single leaf level, which §0.1 shows cannot exist at 24 mm pitch with these paddles. Everything of mine is therefore **beside** the hand, not above it, and the deck's roof over the hand is the float arm alone (h 62–65).

**0.3 Geometric lift fixes the chord [FLAG].** Ramps at the ends of travel lift the hand only if the carriage reaches them; a shorter stroke reverses in contact (H-5.2). So with one servo and geometric lift the **contact chord is a session constant** (swappable ramp blocks: 25 / 30 / 36 mm), and firmware varies speed, profile, end-dwell, pauses, episodes, and (with the amendment) yaw. Team F and A had the same limit; concept A's arc has it too (strokes below ±21° reverse on the trailing nail). I state it rather than hide it in a speed knob.

---

## 1. Geometry

### 1.1 Layout in words

Frame: X = stroke, Y = pitch, h up from the apex; nail centroid at X 0, Y 0 (freeze origin). Scalp sphere R 90, centre (0, 0, −90).

- **Hand** (§1.2): knuckle plate 64 × 90 at h 33.5–35.1; palm tray Y −55.5…+31, X ±26; lid: central hump h 59.5 over X ±22, Y ±32 (level-1 clamps), low wings h 48 elsewhere. Keyed magnetic wrist seat (mech §7, D61) on the hump top, h 59.5–62.5.
- **Float**: MGN7 rail 40 mm vertical on the X-carriage at X +33…+40, Y −6…+1 (rail 7 wide), h 40–80?? no: h 40–66 (the rail is 40 mm: h 26? see below). Rail h 36–76 is impossible (70 limit), so the rail is **40 mm from h 30 to 70?** No. Final: rail bottom at h 28 at X +37, where the local scalp is 7.6 mm below the apex (36 mm clearance ≥ 30 ✓, static part), top at h 68; MGN7C block (10 g, seals off) travels h 34–62 on it; the float arm (3 mm PETG) runs from the block face at X +32 over the lid to the seat at X 0, h 62.5–65.5. Travel 14 mm between stops: down-stop 5 mm below nominal, up-stop 9 mm above. 623ZZ ramp roller on a stub axle on the block's −Y face at h 44, X +36.
- **X carriage**: U-frame of 2 mm PETG: +X bar (carries the vertical rail), +Y side bar at Y +33…+37, h 44–56 (1.5 mm from the palm's +Y wall, enclosed), −X slot arm at X −78 reaching from Y +37 to −28 at h 62–66 with a 6 × 32 mm slot along Y. MGN7C block on the 70 mm MGN7 X-rail at Y +37…+44, h 40–45 (rail) / 45–48 (block). Travel ±25.
- **Crank**: STS3032 shaft up, body 23.2 × 12.1 footprint centred (X −78, Y 0), h 34–57, shaft boss to 62; printed crank disc Ø 56 × 3 at h 58–61 on the horn; M3 shoulder pin with a 623ZZ (Ø 10) at r 25 running in the slot arm. Scotch yoke: x = 25 sin φ.
- **Ramps**: two PETG blocks at X −38…−28 and +28…+38 (Y −12…−3), rising 6 mm over 10 mm (31°), crest flat 4 mm, under the roller's path; swapped for 25/36 mm chord sets.
- **Tray**: 181 × 98 open PETG frame, floor ribs at h 34–36, walls 2 mm to h 60 (h 67 around the crank), window −60…+57 × −58…+34 under the hand's swept volume, closed below by a slack 0.15 mm LDPE skirt from the window rim to the knuckle-plate rim (§6). Four TPU-grommeted clips at the corners take the crown straps.
- **Band**: a hard-hat 4-point ratchet suspension (bought) with its crown-strap cross cut out: the four straps rise from the headband at the forehead, parietals and occiput to the tray corners, 60–90 mm long, lying on the hair outside the window; headband at h −46 with four pads (A's §1.4 pads, 45 × 35 × 12). Alternative: slim printed band, −20 g.

### 1.2 Side view (XZ)

<svg viewBox="-130 -60 290 150" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="5">
<defs><marker id="a" markerWidth="4" markerHeight="4" refX="2" refY="2" orient="auto"><path d="M0,0 L4,2 L0,4 z" fill="#333"/></marker></defs>
<g transform="scale(1,-1)">
<path d="M -110 -50 A 90 90 0 0 1 110 -50" fill="none" stroke="#c96" stroke-width="1.2"/>
<text transform="scale(1,-1)" x="80" y="40" fill="#c96">scalp R90</text>
<path d="M -32 33.5 A 90 90 0 0 1 32 33.5" stroke="#000" stroke-width="1.6" fill="none"/>
<rect x="-26" y="35" width="52" height="13" fill="#eee" stroke="#000" stroke-width="0.5"/>
<rect x="-22" y="48" width="44" height="11.5" fill="#ddd" stroke="#000" stroke-width="0.5"/>
<rect x="-4" y="-4" width="2" height="37.5" fill="#333"/><rect x="-12" y="-4" width="2" height="37.5" fill="#333" opacity="0.5"/><rect x="6" y="-4" width="2" height="37.5" fill="#333" opacity="0.5"/>
<rect x="33" y="28" width="7" height="40" fill="#9bd" stroke="#000" stroke-width="0.5"/>
<rect x="30" y="44" width="10" height="18" fill="#58a" stroke="#000" stroke-width="0.5"/>
<rect x="-2" y="62.5" width="34" height="3" fill="#58a"/>
<circle cx="36" cy="44" r="5" fill="none" stroke="#000" stroke-width="0.5"/>
<path d="M 28 36 L 38 42 L 42 42" fill="none" stroke="#000" stroke-width="1"/>
<path d="M -28 36 L -38 42 L -42 42" fill="none" stroke="#000" stroke-width="1"/>
<rect x="-90" y="34" width="24" height="23" fill="#fc9" stroke="#000" stroke-width="0.5"/>
<rect x="-106" y="58" width="56" height="3" fill="#999" stroke="#000" stroke-width="0.5"/>
<rect x="-82" y="62" width="8" height="4" fill="#58a"/>
<rect x="-109" y="34" width="190" height="2" fill="#bbb"/>
<rect x="-109" y="34" width="2" height="33" fill="#bbb"/><rect x="79" y="34" width="2" height="26" fill="#bbb"/>
<path d="M -109 34 L -140 -46 M 81 34 L 112 -46" stroke="#696" stroke-width="2" fill="none"/>
<rect x="-150" y="-54" width="20" height="16" fill="#9c9"/><rect x="110" y="-54" width="20" height="16" fill="#9c9"/>
<line x1="-120" y1="0" x2="-120" y2="66" stroke="#333" stroke-width="0.4" marker-end="url(#a)" marker-start="url(#a)"/>
</g>
<text x="-128" y="-30" transform="rotate(-90 -128 -30)">h 66</text>
<text x="-50" y="-58">tray h 34–67, 181 long</text>
<text x="-95" y="-10">STS3032 shaft up</text>
<text x="-108" y="-63">crank Ø56 h58–61 / slot arm h62–66</text>
<text x="34" y="-70">MGN7 40 float rail</text>
<text x="-30" y="-20">ramp 31°</text>
<text x="-24" y="-52">palm hump h59.5</text>
<text x="-150" y="52">headband h −46</text>
<text x="-90" y="-40">crown strap</text>
</svg>

Dimensions (nominal seating, hand on its down-stop, carriage at mid-travel): knuckle plate underside h 33.5; lid hump h 59.5; seat h 59.5–62.5; float arm top h 65.5; crank slot arm and pin head h 62–67; tray walls h 60 (h 67 at the crank bay); float rail top h 68 **← tallest point, 68 mm**. Worst case: band seated 5 mm low → hand +5 relative to the tray: arm top h 70.5?? No: the limit is measured from the scalp, and when the band sits low the tray is 5 mm *lower*, so the hand's absolute height is unchanged and the tray's is −5. The worst *absolute* height is the rail top at **h 68** at nominal and h 73 with the band seated 5 mm **high** (nails then float 5 mm lower on the rail, hand unchanged). Per the brief's "measured from the scalp surface at the crown" I report **68 mm nominal, 73 mm at +5 mm seating** [FLAG: +3 over 70 at the seating extreme; cut the rail to 36 mm and the up-stop to +7 to make it 69].

### 1.3 Front view (YZ), section at X +36 through the float rail

<svg viewBox="-80 -60 180 140" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="5">
<g transform="scale(1,-1)">
<path d="M -80 -45 A 90 90 0 0 1 80 -45" fill="none" stroke="#c96" stroke-width="1.2"/>
<path d="M -45 33.5 A 90 90 0 0 1 45 33.5" stroke="#000" stroke-width="1.6" fill="none"/>
<rect x="-55.5" y="35" width="86.5" height="13" fill="#eee" stroke="#000" stroke-width="0.5"/>
<rect x="-32" y="48" width="64" height="11.5" fill="#ddd" stroke="#000" stroke-width="0.5"/>
<rect x="-25" y="-7.6" width="2" height="41" fill="#333"/><rect x="-1" y="-4" width="2" height="37.5" fill="#333"/><rect x="23" y="-7.6" width="2" height="41" fill="#333"/>
<rect x="-6" y="28" width="7" height="40" fill="#9bd" stroke="#000" stroke-width="0.5"/>
<rect x="-10" y="44" width="15" height="18" fill="#58a" stroke="#000" stroke-width="0.5"/>
<rect x="33" y="44" width="4" height="12" fill="#58a"/>
<rect x="37" y="40" width="7" height="5" fill="#9bd"/><rect x="36" y="45" width="9" height="3" fill="#58a"/>
<rect x="-58" y="34" width="98" height="2" fill="#bbb"/><rect x="-58" y="34" width="2" height="26" fill="#bbb"/><rect x="38" y="34" width="2" height="26" fill="#bbb"/>
<path d="M -58 34 L -85 -46 M 40 34 L 68 -46" stroke="#696" stroke-width="2" fill="none"/>
<rect x="-95" y="-54" width="18" height="16" fill="#9c9"/><rect x="60" y="-54" width="18" height="16" fill="#9c9"/>
<line x1="-55.5" y1="25" x2="31" y2="25" stroke="#333" stroke-width="0.4"/>
<line x1="-58" y1="72" x2="40" y2="72" stroke="#333" stroke-width="0.4"/>
</g>
<text x="-40" y="-22">palm 86.5 (Y −55.5…+31)</text>
<text x="-30" y="-74">tray 98 (Y −58…+40)</text>
<text x="-55" y="-52">C leaf root wing h48</text>
<text x="-20" y="-56">L/R clamps h52–58</text>
<text x="34" y="-50">X rail+block</text>
<text x="-70" y="55">parietal pads h −46</text>
</svg>

### 1.4 Plan view

<svg viewBox="-125 -75 260 150" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="5">
<rect x="-109" y="-58" width="190" height="98" fill="none" stroke="#333" stroke-width="1"/>
<circle cx="-22" cy="0" r="80" fill="none" stroke="#c33" stroke-dasharray="3 2" stroke-width="0.6"/>
<rect x="-60" y="-58" width="117" height="92" fill="#f6f6f6" stroke="#999" stroke-width="0.4" stroke-dasharray="2 2"/>
<rect x="-26" y="-55.5" width="52" height="86.5" fill="#eee" stroke="#000" stroke-width="0.6"/>
<rect x="-51" y="-55.5" width="102" height="86.5" fill="none" stroke="#000" stroke-width="0.3" stroke-dasharray="1 1"/>
<circle cx="-8" cy="-24" r="4" fill="#333"/><circle cx="0" cy="0" r="4" fill="#333"/><circle cx="8" cy="24" r="4" fill="#333"/>
<rect x="33" y="-6" width="7" height="7" fill="#9bd" stroke="#000" stroke-width="0.4"/>
<rect x="-5" y="33" width="80" height="4" fill="#58a"/><rect x="-82" y="-28" width="8" height="65" fill="#58a"/><rect x="28" y="-6" width="12" height="42" fill="#58a"/>
<rect x="-40" y="37" width="70" height="7" fill="#9bd" stroke="#000" stroke-width="0.4"/>
<circle cx="-78" cy="0" r="28" fill="none" stroke="#000" stroke-width="0.8"/>
<rect x="-89.6" y="-6" width="23.2" height="12.1" fill="#fc9" stroke="#000" stroke-width="0.5"/>
<circle cx="-78" cy="25" r="5" fill="#fff" stroke="#000" stroke-width="0.6"/>
<rect x="-38" y="-12" width="10" height="9" fill="#999"/><rect x="28" y="-12" width="10" height="9" fill="#999"/>
<circle cx="-22" cy="0" r="2" fill="#c33"/>
<text x="-20" y="-62">window X −60…+57</text>
<text x="-108" y="-62">tray 181 × 98 (yaw 0)</text>
<text x="-105" y="48">crank Ø56, r 25, pin 623ZZ</text>
<text x="-20" y="55">X rail MGN7 70 at Y +37</text>
<text x="40" y="-30">float rail</text>
<text x="-60" y="-20">ramp</text>
<text x="-100" y="-68" fill="#c33">dashed: yaw swept circle Ø 188 (§12)</text>
<text x="-30" y="40">palm swept ±25 (dotted)</text>
</svg>

### 1.5 Mass budget by part

| Part | g | Note |
|---|---|---|
| Hand, floating: 3 paddles 16.5, tips W 5.4, TM1 magnets + sleeves 2.5, paddle bars + Al screws 3.3, leaves 4.5, root bars + M2 2.2, stops 1.1, knuckle plate 4.0, boot 2.0, tray (0.8 walls, open) 7.0, lid 3.0, lower seat + keeper 1.5 | 53 | mech §6.5 hand was 60.5; the tray/lid lose 6 g to thinner walls and no tether cup |
| Float carrier: MGN7C 10, float arm + upper seat + D61 5, roller 623ZZ + axle 1.5, CF-spring tab 0.5 | 17 | **floating mass 70 g = 0.69 N** |
| X carriage U-frame (2 mm PETG) 12, vertical MGN7 40 mm 9, slot arm 3 | 24 | |
| X guide: MGN7 70 mm 15.4 + MGN7C 10 | 25 | printed dovetail + PTFE: 8 g (−17) |
| Crank: STS3032 20.6, disc 3, pin + 623ZZ 1.5 | 25 | |
| Tray: floor ribs, walls, ramps, clips, cable channel | 30 | 2 mm PETG, 15 % gyroid |
| LDPE hair skirt, felt | 2 | |
| Band: hard-hat ratchet suspension, crown cross removed, 4 straps | 72 | printed slim band + 4 pads + ratchet: 52 |
| Chin strap, anchors, magnetic fuse | 10 | A §3.3 spec |
| On-head cable (3 × 28 AWG, 0.5 m) + boot | 6 | bus board off-head |
| Fasteners, grommets, misc | 6 | |
| **Total, no yaw** | **270** | **245 with dovetail X guide + printed band** |
| Yaw axis (§12): SCS0009 13.2, ring track 13, 3 rollers 3.3, pinion + mount 4 | 34 | |
| **Total with yaw** | **304 / 279** | over 250 by 29 at best; §11 |

**Centre of mass**: tray parts (≈ 170 g) at h 45–55, band (≈ 80 g) at h −46 → CoM at **h +20** (W2), 110 mm above the sphere centre (A: 122). The reciprocating mass is 106 g (hand 53, float 17, U-frame 24, X block 10, pin 2).
