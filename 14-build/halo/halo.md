# SP1 v3 HALO: detailed design and build guide

**PROJECT SCRATCH · 14-build/halo · HALO engineer · 2026-10-02**

**Binding:** SYSTEM-SPEC-v3 §11 HALO work package (§3, §4.7–4.8, §5.1 M1–M8, M15, M18, §6, §7.4–7.7), DECISION-3, the safety red lines and the H-rules.

**Built from:** leap4-C C3 (carbon polygon bail), leap4-E E4 and leap4-F L4 (hand-moved halo on friction hinges), leap3-D D1 (skeleton halo).

**Files:**
- `cad/` (OpenSCAD + STL + generator + calculator; see `cad/README.md`);
- `parts.md` (live prices);
- `CONFLICTS.md` (everything that differs from the spec, read it first).

**Tags:** [KNOWN] = sourced; [EST] = computed (`cad/halo_design.py`); [VERIFY] = check with calipers or a scale before trusting.

---

## 0. The halo on one page

The halo is the frame that holds the pad on Michael's head and lets him move it by hand between bouts. Nothing on it is powered except one switch.

```
                       Airpel float (stands 235 mm above the vertex scalp; CONFLICTS #1)
                              |
          carriage on a carbon track strip (beta, 10 deg clicks, stops)
     N-2 ____ N-1 ____ N0 ____ N+1 ____ N+2          carbon polygon bail, R 220
   N-3 /      (6 straight 8x6 carbon chords in 7 printed nodes)       \ N+3
      /  leg                                                       leg \
 right foot -- E6 friction hinge -- right hub plate  ...  left hub plate -- E6 hinge -- left foot
 (umbilical exits on the ear axis here)                  (alpha detent, alpha stops, brake)
        \_ front band: two 10x1 carbon strips over the forehead (forehead node: doff lip + switch) _/
        \_ bike-helmet dial cradle under the back of the skull (form lock, no chin strap) _/
```

| Quantity | Value | Basis |
|---|---|---|
| Head-borne mass, single pad, **default** (spec Airpel + medium hinges) | **≈ 488 g** (12 g under red line 10) | [EST] §8; CONFLICTS #1 |
| Head-borne mass, **recommended** (light float + small hinges) | **≈ 373 g** | [EST] §8 |
| Worst lean (bun pose) | 0.63 N·m default, 0.42 N·m light; cradle form lock 1–1.5 N·m | [EST] §8 |
| α (front–back) | pad α from the hairline stop (≈ −29° on the design head) to +100°, clicks every 15°, friction hold anywhere | §4.2, §9 |
| β (side–side) | ±40° hardware; set ≈ ±35° from the ears (CONFLICTS #8); clicks every 10° | §4.4, §9 |
| Hinge hold | default 2 × 0.79 N·m + brakes 0.23 + click 0.12 = 1.93 N·m against 0.73 needed (margin 2.6 new, 1.6 worn) | §7 |
| Coverage (reachable) | ≈ 82 % with β ±35°; ≈ 85 % with ±40° | [EST] §10 |
| Bail | R 220 (node centres), six 79.05 mm chords, legs to hubs at |Y| 141.5 (medium) or 124 (small) | §4.3 |
| Width | 400 mm across the shoulder nodes; 313 mm across the hub feet (278 small) | CONFLICTS #12 |
| HALO cost | ≈ $415–455 (S0 ≈ $54, Stage B ≈ $264 bought + printing ≈ $95–135) | parts.md |
| Printed parts | 26 designs, 36 pieces (incl. 2 tools), ≈ 127 cm³ PA12 head-borne | `cad/stl/_part_table.csv` |

**Three findings change the plan before anything is bought beyond S0:**
1. **The Airpel float is 96 g, not 16 g.** The helmet comes out at ≈ 488 g, twin is impossible, and the lean doubles. A light Penrose-sleeve float brings it to ≈ 373 g. *Director + PAD decision* (CONFLICTS #1).
2. **The small E6 hinges cannot hold the Airpel version.** Medium hinges are the default; brakes are added (CONFLICTS #2).
3. **The spec's "hairline + 20°" stop rule leaves the nails 4 mm in front of the hairline, and β ±40° is too close to the ear if the halo slips.** Both stops are adjustable and set on Michael's head (§9; CONFLICTS #7, #8).

---

## 1. Scope

**HALO owns:**
- carbon front band;
- forehead pad, head-present switch and doff lip (forehead node);
- dial-cradle adaptation and temple pads;
- hub plates (boss and side plate merged) with E6 friction hinges, α detent, α stops and friction brakes;
- the leg feet, including the right foot's umbilical exit on the ear axis;
- carbon polygon bail, printed nodes and track strip;
- carriage (rollers, detent, friction, β stops);
- float mount (nose plate, steady collar, anti-rotation guide, retract spring, spider = M8 ball side);
- harness clip track, umbilical exit clamp and 3 N umbilical clip;
- zero gauge;
- pad-2 provisions.

**Interfaces owned:** M1–M8 (ball side), M15, M18 (bail/boss), T4 routing on the head.

**Not HALO:**
- the pad (M8 grooves and below);
- the Airpel/QEV choice itself (spec C12);
- the umbilical build;
- the hanger;
- all electrics beyond the switch and its two wires.

---

## 2. Frames and sign conventions (read once)

**Head frame H** (spec §3.1):
- O is the skull centre, 45 mm above the ear canals; X forward, Y left, Z up.
- The ear canal is at (TRAG_X, ±72, −45) with TRAG_X = −10 on the design head.
- This is the spec table's value; the spec text says the opposite (CONFLICTS #17).

**α and β.** α is the **pad** pitch: 0 over the vertex, + toward the back. β is the pad latitude: + toward the left ear.

**Why the pad leads the bail by 5.9°.** The float cannot sit under the bail; there is no room in the radial chain. So it stands beside the bail on its **front** side. Its axis passes through O, 24 mm in front of the bail plane at the track, which is **δ = 5.9°**.
- The bail itself is at α_bail = α_pad + 5.9°.
- Every HALO number you see (detent marks, stops, the zero gauge) is pad α, so firmware and CAD can keep the spec's u(α, β) (CONFLICTS #4).

**Hub angle θ** is used in the CAD and this text for parts around the ear axis: θ is measured from straight up, + toward the back. At α_bail = 0 the leg points to θ = 0.

**Side A / side B.** Side A is the front (float, cheek, notches). Side B is the rear (strip posts, harness, carriage lip).

---

## 3. Taking your head measurements (tape fit) and what each one sets

**Time and tools:** 30 minutes. You need:
- the soft tape (parts S0-4);
- two hardcover books;
- a flat wall and a door frame;
- a pencil;
- a washable eyeliner pencil;
- a 30 cm ruler;
- a mirror;
- a helper for items 4–6 and 10 (you can do them alone with a phone on a timer against the wall, but a helper is faster and better).

**Rules:**
- Hair as it normally is.
- Head level: look at a mark on the wall at your own eye height.
- Take each number **twice** and use the average. If the two readings differ by more than 4 mm, take a third.

Enter the numbers in `cad/halo_params.scad`, TAPE FIT block, in mm.

| # | Name in the file | How to take it | What a typical man reads | What it sets in the halo |
|---|---|---|---|---|
| 1 | **HC** head circumference | Tape around the head just above the eyebrows and over the most rounded point at the back. Snug, not tight. | 560–590 | Checks that the dial cradle fits (UltAlt 500–620 mm). If HC > 600, buy the larger cradle. |
| 2 | **HL** head length | Stand with the back of your head touching the wall, heels 5 cm out. Press a book's spine flat against your brow (the bony point between the eyebrows). Helper measures wall to book, at the brow, horizontal. | 190–200 | Ellipsoid X semi-axis (HA = HL/2). Sets **R_BAIL** (§4.3: the bail must clear the pad at the bun) and the forehead-node position. |
| 3 | **HB** head breadth | Helper holds the two books flat against the sides of your head just above the ears, parallel, and measures the gap. Widest point; move up and down to find it. | 150–160 | Y semi-axis. Sets the hub-plate positions: plate face at HB/2 + 12 (temple pad) + 1 + 4 (§4.2), and therefore the hub spacing and leg length. |
| 4 | **TV** ear canal to the top of the head | Back to the door frame, head level. Book flat on the top of your head, pressed down, level; mark the frame under it. Helper marks the frame at the height of your ear-canal opening (the hole, not the flap). Measure between the marks. | 125–140 | Z semi-axis (HCZ = TV − 45). Sets where the pad sits over the crown. Changes the predicted hairline angle and coverage, not the hardware. |
| 5 | **OT** back of head to ear canal | As item 2 (back of head on the wall). Helper measures, horizontally, wall to ear-canal opening with the ruler held level. | 85–95 | The ear-canal X position (TRAG_X = −HL/2 + OT). Used by the ear-fence check (§9.3) and the cradle-arm clamp position. |
| 6 | **GH** brow above ear canal | Door frame again. Helper marks the brow height and the ear-canal height; measure between them. | 30–40 | Brow Z. Sets the band height on the forehead (centre 45 mm above the brow, spec) and the forehead node. |
| 7 | **G2H** brow to hairline | Tape laid on the skin from the brow point straight up the middle of the forehead to where the hair starts. Hair pushed back. If the hairline is fuzzy, use the first point where hair is as dense as on top. Also dot the hairline with eyeliner in the middle and 30 mm left and right; you need these dots again in §9. | 50–80 | The predicted front α stop (calculator prints it). **The real stop is set on your head in §9.** |
| 8 | **EW** ear width | Books flat against the outsides of both ears at ear-top height, lightly (don't fold the ears). Measure the gap. | 175–200 | The ear outer rim (EW/2). The calculator checks that the side plates and the boss never come down over the ears. |
| 9 | **ET** top of ear above canal | In the mirror or with the helper: ruler vertical beside the ear, from the canal opening to the top of the ear. | 25–35 | No printed part may go lower than ET − 45 + 5 behind the ear's front edge (EAR_CUT_Z). |
| 10 | **IH** occipital bump | Feel the bony bump at the back of the skull (inion); just under it is the shelf the cradle hooks under. With the door frame, measure the bump's height above (+) or below (−) the ear canal. | −10 … +10 | The cradle-arm clamp height (H15) and the "bun free ≥ 60 mm above the cradle" check (C1). |

### 3.1 What to do with the numbers

1. Type them in, then run `halo_design.py` (or ask whoever has the Python environment).
2. Read off the outputs:
   - the derived dimensions;
   - the carbon cut list;
   - the hairline α;
   - the ear distances at β 30–45°;
   - the mass and lean.
3. Run `gen_halo_stl.py`. It must print **ALL OK** before you order prints.

**If any check fails, do not "fix" the STL by hand.** Change the parameter it names, or write to the HALO/CAD owner.

**Most likely surprises:**
- **A big back of the head (HL > 200).** R_BAIL grows (+1 mm per mm of HA). Harmless.
- **A wide head (HB > 160).** The hubs move out and the helmet widens.
- **Ears that stick out (EW/2 > Y_F1 − 4).** The calculator flags it. Add a 2 mm spacer under the temple pad (TEMPLE_PAD_T 12 → 14) and regenerate.

---

## 4. Detailed design (default build; the small-hinge variant numbers are in brackets)

All dimensions are in mm, for the design head (spec §3.2 head; the TAPE FIT defaults). They scale with your numbers as described in §3.

### 4.1 Retention: band, forehead node, switch, cradle, temple pads

**Front band (bought carbon, no print).**
- Two pultruded 10 × 1 carbon strips, laid edge to edge so they act as one 20 × 1 band (spec C25; 20 × 1 is not stocked, CONFLICTS #15).
- Cut each strip **290 mm**; the calculated length is 279 mm between pocket bottoms. Trim at the pockets after the dry fit.
- The band runs from a pocket in the left hub plate, across the forehead through the forehead node, to the right hub plate.
- **Pockets in the hub plates (H01):**
  - 20.6 tall × 1.4 thick × 28 deep (X 28–56), open toward the front, centre 4 mm above O height, at |Y| 87.75.
  - Bonded with DP420 plus **one M3 × 12 cross-bolt** at X 51 through both strips (outside the α stop ring, so no nut sits under a stop block). Drill the strips Ø3.2 through the plate hole after the dry fit.
- **Forehead node (H13):**
  - Arc-shaped, its band slot on a radius R_NB = **66.0** centred at X 34.4.
  - Centred 45 mm above the brow (Z 35), inner face at X 100.4 on the midline.
  - **Bonded only. There are no bolts in the forehead node, so nothing hard sits under the forehead foam.**
- **Strain:** the band bends to R 66 at the brow, which is **0.76 % strain**; pultruded carbon breaks near 1.5 %.
  - Before bonding, bend a spare 10 × 1 offcut around a 130 mm can and leave it taped 24 h. It must spring back unmarked and uncracked.
  - If your forehead is narrower than the design head, the node radius drops and the strain rises; the calculator prints it.

**Forehead node H13 (6.4 g):**
- Band zone 42 × 24 mm, 4.4 mm thick.
- **Doff lip** on top: 34 wide (along the band), sticking out 13 mm forward, 2.5 thick, with a 6.5 mm upturned rim. Every edge has a ≥ 0.9 mm round (red line 11; sand any print edge that catches a fingernail).
- Below the band: a 28 × 13 block that holds the **head-present switch** (Omron D2F-01FL, 0.25 N, pocket 12.8 × 5.8 × 6.5, lever toward the skin). Its two wires leave through a 3 × 4 hole in the outer face.
- Two Ø3.2 guide holes at ±10.5 mm, 18.5 mm below the band centre, carry the **trigger plate H14**:
  - a 26 × 11 × 2 curved plate on two Ø3 × 12 pins, pressed into the plate and sliding in the node;
  - 1.5 mm in front of the node face;
  - a 2 mm foam pad on its skin side that stands **1–2 mm proud** of the main forehead foam.
- **How it works:**
  - On the head, band tension (≈ 5 N) pushes the trigger plate back about 1.5 mm and the switch closes (its NO contact).
  - Lift the helmet and the plate springs out on the switch lever: the loop opens, the rail is cut (spec C29, §7.7).
  - A broken wire also opens the loop.

**Forehead foam:**
- 8 mm closed-cell (helmet pad kit, hook-and-loop) on the node's inner face around the trigger plate.
- The pad kit is washable; keep a spare set (hygiene §8).

**Dial cradle (bought, adapted):**
- The UltAlt retention: a rear cradle with dial, and two side arms that end in tabs.
- The cradle hooks under the occipital shelf (form lock in pitch ≈ 1–1.5 N·m, override ≈ 10 N, spec §4.8). It is unchanged.
- Each side arm's tab is clamped in a **cradle-arm adapter H15**:
  - a printed bracket bolted with 2 × M3 × 10 to the rear lug of the hub plate (inserts at X −40 and −29, 6 mm below O);
  - it reaches back and in to a clamp plate at X −45, Z −2 (35 mm behind and 13 mm above the top of the ear), 6 mm off the scalp;
  - the tab is sandwiched under the **H15b jaw** with 2 × M3 × 10, 14 mm apart, with a strip of the helmet-pad foam for grip.
- Trim the tab with scissors or a knife if it is longer than the jaw.
- The clamp height follows OT and ET: if the tab ends up on the ear, move it up a hole by re-printing H15 with a new ET.

**Temple pads:** two layers of 6 mm helmet-pad foam (12 mm) on the inboard face of each hub plate, about 45 × 50, hook-and-loop. They resist yaw (spec) and set the hub-plate distance from the head.

### 4.2 Hubs: hub plates, hinges, feet, detent, brakes, stops

**Y stack along the ear axis**, in |Y| (the same on both sides; small-hinge values in brackets):

| From | To | What |
|---|---|---|
| 77.0 | 89.0 | scalp to temple-pad face (12 mm foam, 1 mm compressed gap) |
| 90.0 | 94.0 | **hub plate H01** (4 mm). Inboard face = temple pad; outboard face = brake track and α-detent track |
| 84.5 | 91.0 | band pocket boss on the inboard face (front, X 26–56) |
| 90.0 | 93.0 | α stop ring sectors (left only, R 30.3–47.3) |
| 94.0 | 136.9 (119.4) | **Southco E6 hinge** pin on the ear axis, 42.9 (25.4) long |
| 94.5 | 102.5 | foot bridge and α arm over the hub-plate face (0.5 mm running gap) |
| 136.9 | 141.5 (124) | foot cap, then the **bail plane** at Y_HUB 141.5 (124), where the leg axis meets the ear axis |
| 141.5 | 150 | leg socket rises from the foot (bottom 11 mm along the leg) |
| ≈ 141 | ≈ 175 | right only: carbon exit stub on the axis + exit clamp H17 |

The hub axis is 46 mm from the ear canal (red line 6 ≥ 25 ✓).

**Hub plate H01L / H01R** (22.4 / 20.5 g; small 16.3 / 14.7 g). One printed part per side; this is the spec's side plate and boss merged (CONFLICTS #3).
- **Disc** R 31.3 (26.1) × 4 mm. Nothing lower than Z −10 (= ear top + 5) behind X +5, so no part rests on the ear.
- **Boss leaf seat**, which holds the hinge leaf fixed to the plate:
  - points to θ_B = −70° (forward, 20° above horizontal);
  - the block is 8 thick, starts 2 mm out from the pin and ends at 20 mm;
  - leaf face 6.35 (5.1) mm from the pin axis;
  - **medium:** 2 × M4 heat-set inserts at 12.7 mm out, 31.8 apart along the pin;
  - **small:** 2 × Ø5.4 holes at 10.15 mm out, 15.1 apart along the pin, with Ø12 counterbores for the supplied push-on nuts (stud length ≤ 7.9 mm panel, here 4 mm).
- **Brake track:** the smooth outboard face between R 20.8 and 25.3 (16.8–21.3).
- **α detent track (left):**
  - 11 radial V-notches, 90°, 0.75 deep, 4 long, on R 28.8 (24.8);
  - notch k sits at θ = 15k + 5.9 − 40, which **puts the pad at α = 15k** for k = −3 … 7 (−45° … +105°).
- **α stop ring (left):**
  - two sectors, R 30.3–47.3 × 3 mm: front θ −104 … −44 and rear θ 44 … 96;
  - each has an arc slot (width 3.4 on R 35.3) for the stop-block screw;
  - a row of Ø3.1 pin holes every 10° on R 42.3.
- **Band pocket** (inboard, front) and **cradle-arm lug** (rear, 2 × M3 inserts), as in §4.1.

**Hinges:**
- **Default:** 2 × Southco **E6-10-301-20** (medium, acetal, adjustable, 0.8 N·m maximum).
  - 42.9 along the pin × 36.5 flat.
  - Leaves have 4 × Ø4.5 holes on 31.8 × 25.4 and take M4 × 10 screws into M4 heat-set inserts.
- **Light-float variant:** 2 × **E6-10-101-20** (small, 0.25 N·m), with moulded studs and push-on nuts.
- **Mounting:**
  - One leaf on the hub-plate seat, the other on the foot seat, the pin exactly on the ear axis. The printed seats put it there; ±0.5 mm is the target (spec M2).
  - Left and right pins are separate. The carbon bail takes up the small misalignment.

**Leaf clocking and fold range:**
- The foot leaf lies along the leg (θ = α_bail).
- The angle between the leaves runs from **51° to 176°** over the α range, never flat-past-flat and never folded tight.
- `gen_halo_stl.py` checks the leaves, the seats and the knuckle against each other every 2.5° (all clear).

**Leg feet H04L / H05R** (12.8 / 10.1 g; small 8.2 / 5.5 g):
- **Foot leaf seat** on the back side of the foot leaf.
- **Cap** over the pin end at |Y| 137.4–141.4.
- **Leg socket:** Ø8.25 bore × 14 deep, starting 11 mm along the leg from the hub point. The leg points 27.4° outboard of vertical in the bail plane: unit vector (Y 0.46, Z 0.89) (small: 0.53, 0.85).
- **Bridge:** a 6 mm-wide arc band, R 20.1–26.1, that runs over the hub-plate face from θ −45° to +45°. It carries the **brake** at θ +25°:
  - a Ø3.5 pocket holds a 4 mm plug of Ø3 NBR O-ring cord;
  - an M3 set screw in an M3 insert pushes it onto the brake track;
  - one brake per foot, adjustable 0–0.12 N·m each.
- **Left foot α arm** at θ = leg − 40°, 10 wide, from R 20.6 out to R 47.3:
  - an **M4 ball plunger** (McMaster 85015A46, 4.0 N, Ø2.5 ball) in an M4 insert at R 28.8 clicks into the detent notches (≈ 0.12 N·m click);
  - the arm's outer part drops to 0.5 mm above the stop ring and is the **stop tab**.
- **Right foot:** no α arm (spec: detent and stops on the left). It has an **Ø8.25 × 11 socket on the ear axis**, outboard, for the 30 mm carbon exit stub (§4.7).

**α stop blocks H06** (×2, 1.2 g):
- 15 (radial, R 31.3–46.3) × 14 × 6 mm.
- An M3 insert on R 35.3 takes an M3 × 10 screw from the **inboard** side of the hub plate, through the arc slot.
- Two Ø3 × 8 pin holes at ±7.5° on R 42.3: one of them always lines up with a ring hole, giving **5° steps**.
- A Bumpon (SJ5302) on the face the arm hits.
- Default positions: front block at pad α ≈ −29°, rear at +100° (set in §9).

### 4.3 Bail: carbon polygon on printed nodes

**Geometry** (bail plane; y along the ear axis, z up at α_bail = 0):

| Node | β | y | z | Part |
|---|---|---|---|---|
| N0 vertex | 0 | 0 | 220.0 | H08a + H08b (split, 2 × M3 × 12 splice = pad-2 provision M18) |
| N±1 | ±20.7 | ±77.8 | 205.8 | H07 chord node |
| N±2 | ±41.4 | ±145.5 | 165.0 | H07 chord node |
| N±3 shoulder | ±62.1 | ±194.4 | 102.9 | H09L / H09R (mirror pair) |
| hub points | — | ±141.5 (±124) | 0 | foot leg sockets |

**R_BAIL = 220.** The spec's 210 would put the float spider into the tube at the bun (CONFLICTS #5):

```
R_BAIL = ceil((HA + 86 + 25 + 3 + 4) / cos 10.35°) = ceil(216 / 0.9837) = 220
```

- 86 = spider top above the skin;
- 25 = retract;
- 3 = clearance;
- 4 = tube radius;
- 10.35° = half the chord angle; at mid-chord the tube is 3.6 mm lower than at the nodes.

**Tubes:** pultruded carbon 8 × 6. Cut list:
- **6 chords × 71.05 mm** (79.05 node to node, minus 2 × 4 mm socket bottoms);
- **2 legs × 100.8 mm** (small 109.7);
- **1 exit stub × 30 mm**;
- 676 mm of a 1000 mm tube. Buy two tubes; the second is for mistakes.

**Nodes:**
- Socket bore 8.25 (0.12 mm epoxy gap), wall 1.4, depth **14** (1.75 × tube OD), bottom 4 mm from the node centre, 0.6 mm chamfer at the mouth so the tube cannot be notched.
- Chord nodes are 2.2 g each.
- **Shoulder nodes** have the chord socket and the leg socket 110° apart. Leg direction in the node frame: (0.57, −0.82) (small 0.50, −0.87).

**Strip posts:**
- On N0 and N±1, N±2.
- 3 (lateral) × 8 (along) mm on the **rear** side, top face at 13 mm above the node centre.
- That puts the strip's inner face at R 233 with 9 mm between tube top and strip.

**Harness:** zip-tie bars on the rear side of the shoulders and of N0's half H08b.

**Stiffness:** tube EI ≈ 1.65 × 10⁷ N·mm² (leap4-C). The vertex drops ≤ 0.5 mm under 100 g (gate V-H2; test §6.6).

### 4.4 Track strip, notches, β stops

**Strip:**
- One pultruded 10 × 1 carbon strip, **371 mm** long, running β −45.5° … +45.5°.
- Bonded flat-side-down on the 5 posts with its centreline over the bail plane. It bends itself to R 233 (strain 0.21 %).
- The front edge (side A) carries the β notches. The rear edge is clear of the posts by 0.5 mm.

**Why 10 × 1 on posts and not 3 × 1 on the node crowns** (CONFLICTS #6):
- Between nodes the tube is 3.6 mm lower than at them, so the carriage must run on a smooth arc of its own.
- Notches in a 1 mm face would cut most of the strip.

**β notches:**
- 90° V, 0.75 deep (1.5 wide at the edge), **filed in the front edge with the notch jig H20** before bonding.
- Positions are measured along the strip from the centre of the N0 post, + toward the LEFT ear. The carriage's plunger sits 16 mm to the right of the carriage centre, so the table is offset:

| β | −40 | −30 | −20 | −10 | 0 | +10 | +20 | +30 | +40 |
|---|---|---|---|---|---|---|---|---|---|
| mm | −179.05 | −138.29 | −97.54 | −56.79 | **−16.03** | +24.72 | +65.47 | +106.23 | +146.98 |

Pitch 40.75 mm. These positions do not change with head size, only with R_BAIL.

**β stop blocks H11** (×2, 1.9 g):
- A split collar Ø14 × 10 clamps chord 3 (between N±2 and N±3) with an M3 × 16 pinch screw and nut.
- A 4 × 7 tower rises to 12 mm above the strip and meets the carriage cheek end. A Bumpon goes on its face.
- Slide it along the chord to set β (§9.3). The full range reaches beyond ±45°.

### 4.5 Carriage H10 (10.5 g printed + 5.6 g hardware)

**Install it with +x toward the RIGHT ear.** The cheek and float are then in front.

**Body:**
- Cheek 3.2 thick (front).
- Lip 2 thick (rear).
- Bridge 3 thick over the top, 48 long.
- The cheek and lip inner faces are 5.3 mm from the strip centre: 0.3 mm gap per side before PTFE tape. Put one layer of 0.13 mm PTFE tape on each inner face.

**Rollers:** 4 × MR63ZZ (Ø6 × 2.5, 3 mm bore).
- **Outer pair** on the strip's top face: centres at x ±20.23, 3.13 above the strip's inner face, on Ø3 × 16 pins pressed through cheek and lip, with printed spacers centring each roller.
- **Inner pair** under the strip's front margin: centres at x ±19.72, 3.85 below the strip, on Ø3 × 8 pins cantilevered from the cheek. Each roller is held by an M3 thin washer epoxied to the pin tip.
- The rear 4.5 mm under the strip is left free for the posts to pass.
- The inner rollers carry the float's outward reaction (3–5 N).

**Detent:**
- M4 ball plunger in an M4 insert in the cheek boss, at x +16, level with the strip's mid-thickness, pointing at the front edge.
- 4.0 N into a 90° notch gives ≈ 4 N hold along the track.

**Friction pad:**
- A 10 mm length of Ø3 NBR cord in a 10.4 × 3.4 slot through the bridge at x 0, pressed onto the strip's top by an M3 × 8 set screw (insert in the boss above the bridge).
- Set ≈ 5 N normal, which gives ≥ 3 N drag (spec M5).
- With the detent, about 7 N moves the carriage. That is an easy one-finger push and well above the 1.2 N weight of the moving group.

**Float nose plate:**
- 26 × 29 × 3, square to the float axis (5.9° from the cheek).
- Ø11.5 hole for the Airpel's 7/16-20 nose; the supplied nut goes underneath.
- Plate at 222.3–225.3 from O along the float axis.

**Steady collar:**
- Ø21.4 bore × 8, 18–26 mm above the plate. A loose fit: it stops the 107 mm Airpel body from levering the nose thread.
- **Never tighten anything on the Airpel body; it has a glass bore.**

**Guide lug:** Ø3.3 bore at x −15 on the float axis line, for the Ø3 carbon anti-rotation rod.

**Spring fork:** two plates at x 10.5–21 either side of the float axis, with a Ø3 pin at x 15.3, for the constant-force spring coil on the spool H10b.

**Harness zip-tie anchor** behind the lip.

### 4.6 Float mount and spider (M7, M8 ball side)

**Radial chain along the float axis at full retract** (distance from O; scalp at 98 at the bun, the worst case):

| Item | From O | Note |
|---|---|---|
| spider top | 209.4 | 3 mm under the tube's lowest point (mid-chord 212.4) |
| Airpel rod tip / rod shoulder | 209.4 | the 10-32 thread (11.4 long) goes through the spider hub (7 thick) and a 10-32 nut underneath |
| Airpel nose end | 215.8 | rod sticks out 17.8 when retracted [KNOWN] |
| supplied 7/16-20 nut | ≈ 217–222 | under the plate |
| nose plate | 222.3–225.3 | carriage |
| Airpel body | 225.3–323.2 | 20.6 OD; top is 235 mm above the vertex scalp |
| track strip inner face | 233 | |

**Working:**
- The float extends up to 50.8 mm.
- At the bun the spider sits 86 mm above the scalp with **25 mm** of retract left; on the sides it has more.

**Spider H12** (5.1 g; M8 ball side):
- Hub Ø16 × 7 with a Ø5 hole and a 10-32 nut pocket.
- Three arms, 3.2 thick, at **30°, 150° and 270°** in the pad frame. The arms stay clear of the tendon stops (90/210/330); the 270° arm passes under the bail.
- **Ø5 chrome balls** epoxied in pockets at R 55, protruding 3.0 mm.
- **N52 Ø6 × 3 magnets** flush in pockets at R 42.
- Stub arms: −x to R 15 (guide rod socket Ø3.05 × 8) and +x to R 20 (constant-force spring anchor, M2 hole).
- **PAD must match** (CONFLICTS #14): V-grooves at R 55 and steel discs Ø8 × 1 at R 42 on the same angles. Breakaway 6 ± 2 N, set by the disc gap.

**Anti-rotation:**
- A Ø3 carbon rod, 100 mm, bonded in the spider, slides in the carriage guide lug.
- It keeps the pad's x axis on the bail tangent through the whole stroke (the Airpel rod is free to turn).

**Retract spring:**
- McMaster 9293K123 constant force, **1.60 N**. The coil sits on the spool H10b on a Ø3 × 16 pin in the fork; the strip end is screwed (M2 × 6) to the spider's +x stub.
- Net retract at the vertex ≈ 0.58 N (1.60 − 0.80 pad − 0.23 piston). 25 mm takes ≈ 95 ms; B4 asks ≤ 150 ms [EST].

**QEV and float relief poppet:**
- They screw into the Airpel's **rear 10-32 port**; the palm line arrives there. These parts are DRIVE BOX's spec.
- The Airpel's side port near the nose stays open to air through a small felt plug, so the rod side breathes and stays clean.

### 4.7 Harness on the head, umbilical exit and the 3 N clip (T4, M15)

**Route from the box** (CONFLICTS #9, #10):
1. The 3 N magnetic clip beside the right ear.
2. A free loop of ≥ 450 mm.
3. The **exit clamp H17**, on the 30 mm carbon stub that sticks out along the ear axis from the right foot, |Y| ≈ 160–175.
4. Up the right leg: 2 × H16 clips, the bundle held 12 mm from the leg.
5. The zip-tie bar on the right shoulder node.
6. Along the right arc on its rear side: 3 × H16 clips at mid-chord, bundle centre 12.5 mm behind and 3.5 mm above the tube.
7. The zip-tie anchor on N0 (H08b).
8. **A free arch of about 230 mm to the carriage**, never below the bail, 60–90 mm high at its top when the carriage is at the vertex. The three coil housings are stiff enough to hold it, like bike-brake housing loops; its tightest bend must stay ≥ R 25.
9. The carriage zip-tie anchor.
10. A 150 mm service loop to the pad's deck stops.

**Length on the head ≈ 0.72 m ≈ 31 g.**

**Why the exit is on the stub, not through the boss.** The hinge knuckle occupies the ear axis between the hub plate and the foot. The bundle must turn from the leg onto the axis with a ≥ 25 mm bend radius, which puts the exit about 35 mm outboard of the hub. Turning α only twists the free loop (≤ 125°); no length changes.

**Exit clamp H17** (2.1 g):
- A sleeve bonded on the stub end, plus a C-cradle for the Ø11 bundle 12.5 mm off the axis (zip tie).
- A **pocket 13.4 × 4.9 × 5.5** for the helmet half of the 2-pin magnetic pogo lanyard. ELECTRONICS wires it; it is the shortest member of the bundle (spec §6).

**Harness clips H16** (×6, 0.7 g): snap onto the 8 mm tube (opening toward the head) and hold the bundle with a zip tie.

**3 N umbilical clip H18** (the first fuse, spec §6):
- **H18a collar** zip-tied on the knit sleeve, carrying a steel M5 × 15 fender washer.
- **H18b cup** zip-tied to the drive-box hanger. A Ø10 × 3 N52 magnet sits behind a 1.45 mm printed skin, in a shallow cone so it lets go in any direction.
- Measure the pull-off with the luggage scale. **Target 3 ± 1 N** (C6). Add tape layers on the washer to lower it; sand the skin to raise it.

### 4.8 Tools: zero gauge, notch jig, bonding template

**Zero gauge H19:**
- Snaps on the Airpel body.
- Its 60 × 50 platform is **square to the float axis**, so a phone level app lying on it reads the pad axis tilt directly.
- Used in §9.1 and to log where each detent really points on Michael's head.

**Notch jig H20:**
- A 70 mm block with a slot the strip slides in.
- An index hole takes a Ø2.5 drill shank that drops into the previous notch; a file window sits 40.75 mm further on.
- File each 90° notch with the triangular file to 0.75 mm depth, which is when its width at the edge reaches 1.5 mm. Check with calipers.

**Bonding template** `cad/bail_template.svg`, 1:1:
- node circles, tube outlines, leg lines, hub points;
- the strip arc with β ticks;
- a 100 mm check bar.

**To print it:** use tiled printing (in a PDF viewer: Poster / Tile, 100 %). Tape the sheets together on a flat board and **measure the 100 mm bar before trusting it.**

### 4.9 Pad-2 provisions kept (spec §9, M18)

**Kept:**
- The vertex node is split (H08a + H08b, 2 × M3 × 12 splice), so the half-bails can separate.
- The right exit stub takes a second bundle clamp ("bore sized for two harnesses").
- The left/right foot and hub-plate files are parametric, so a mirrored set is a re-run.

**Not possible as written:** the "second-hinge seat on the right boss" needs a different hub (CONFLICTS #13).

**Mass check:** pad 2 adds ≈ 150 g, so twin exceeds 500 g in every float option until the mass diet in CONFLICTS #11 lands.

---

## 5. Bought parts

See `parts.md`: every part with source, price and tag.

**Key items:**
- Southco E6-10-301-20 × 2 (or E6-10-101-20 × 2);
- UltAlt dial;
- KARBXON 8 × 6 tubes and 10 × 1 strips;
- MR63ZZ;
- McMaster 85015A46 plungers and the 9293K123 spring;
- N52 magnets and Ø5 balls;
- Omron D2F-01FL;
- DP420 epoxy;
- the helmet pad kit;
- heat-set inserts and screws.

**Screw lengths used:**

| Where | Screw | Qty |
|---|---|---|
| Medium hinge leaves → inserts | M4 × 10 socket | 8 |
| Small hinge | moulded studs + supplied push-on nuts | — |
| Band cross-bolt (hub plate) | M3 × 12 + nut | 2 |
| Cradle arm → hub plate | M3 × 10 | 4 |
| Cradle jaw | M3 × 10 + nut | 4 |
| α stop block (from inboard) | M3 × 10 | 2 |
| Vertex splice | M3 × 12 + nut | 2 |
| β stop pinch | M3 × 16 + nut | 2 |
| Hub brakes, carriage friction | M3 × 8 set screw (cup point) | 3 |
| Spring strip to spider | M2 × 6 + nut | 1 |
| Spider on Airpel rod | 10-32 nut (underneath) | 1 |

---

## 6. Node bonding procedure

The bail is the one structure on the helmet that hangs a load over the head, so every bond is proof-loaded.

**Work order:**
1. Cut and prepare the tubes.
2. Bond the arc on the template.
3. Bond the legs into the shoulders.
4. Bond the feet to the legs **on the assembled helmet**, so the two hinge pins end up on one axis.
5. Bond the strip.
6. Proof-test.

### 6.1 Cut

**Setup:**
- Wear the dust mask and work over a damp paper towel. Carbon dust and splinters irritate skin and lungs.
- Wrap masking tape round the tube at the cut mark; it stops splintering.

**Cut:**
- Saw slowly with the razor saw, turning the tube as you go.
- Cut 0.5 mm long, then square the end on 240-grit paper laid on a flat table, holding the tube vertical.
- Lengths: chords **71.05**, legs **100.8** (small 109.7), stub **30**. ±0.3 mm is fine.
- Break the outer edge with two strokes of the paper (0.3 mm chamfer).

**What good looks like:** square, no splits, no fibres hanging, the tube still round.

**If a split runs more than 1 mm into the tube, recut that piece.**

### 6.2 Dry fit

- Push every tube end into every socket it will go in. It should slide in by hand with no wobble you can see.
- **If tight:** run an 8.2 mm drill bit through the socket **by hand**, held in a cloth.
- **If loose (wobble > 0.3 mm):** DP420 fills it; note which one and proof-test that joint first.
- Lay everything on the template: node circles on circles, tubes on the double lines. Every node should sit on its circle within 1 mm.

### 6.3 Surface preparation

- **Tube ends:** sand the last 15 mm with 120 grit until the gloss is gone all round.
- **Sockets:** roll a strip of 120 grit round a 6 mm stick or pencil and twist it in each socket 10 times.
- Wipe both with isopropyl alcohol on a lint-free cloth. Wait 5 minutes.
- **Do not touch** the prepared surfaces.
- PA12 is a low-energy plastic: the sanding is what makes the bond, so don't skip it.

### 6.4 Bond the arc (one session, about 45 minutes)

**DP420 work life is about 20 minutes. Mix two separate nozzle-fulls:**
- one for N0 to N±2;
- one for N±2 to N±3.

**Steps:**
1. Cover the template with clear packing tape; epoxy does not stick to it.
2. Bolt the vertex halves H08a + H08b together with 2 × M3 × 12 (nut in the H08b trap). Snug, not tight.
3. Lay the nodes on their circles **rear side up**, posts pointing up.
4. Put a 1.5 mm cardboard shim under each tube so the tubes sit level with the socket centres.
5. Dispense DP420 through a mixing nozzle; throw away the first 2 cm.
6. With a toothpick, coat the inside of the socket thinly, then the tube end. Push the tube in with a quarter twist until it bottoms.
7. Wipe the squeeze-out with an IPA cloth.
8. Order: chords 1L and 1R into N0; N±1 on; chords 2; N±2; chords 3; shoulders N±3.
9. Check every node is still on its circle, the posts still point straight up, and the shoulders' leg sockets point at the hub-point circles.
10. Hold any node that wanders with a dab of modelling clay.
11. **Cure 24 h** at room temperature. Do not move it for the first 4 h.

### 6.5 Legs and feet (on the helmet: this is what makes the hinges coaxial)

1. Bond the two legs into the shoulder sockets with the arc still on the template, each leg on its dashed line. Cure 4 h.
2. Assemble the helmet (§11 steps H1–H8) on a head form (styrofoam wig head or a towel-wrapped bucket). Fit the hinges and **screw the feet onto the hinges**. Turn each foot so its leg socket points straight up (the zero gauge or a square helps).
3. Dry-fit the arc-and-legs assembly into both foot sockets. It must drop in without being forced sideways.
   - If it doesn't, sand the inside of a foot socket; never bend the carbon.
4. Bond both feet in one go. Check that:
   - the bail swings freely through the whole α range without binding;
   - the arc's centre (N0) is over the midline within 3 mm.
5. Cure 24 h on the helmet.

### 6.6 Proof (gate V-H2, hazard H9 "proof 2×")

**Coupon test (first time only):**
- Bond a 40 mm tube offcut into a spare H07, cure 24 h, and pull it apart with the luggage scale.
- It must hold **20 N for 10 s** (2× the 10 N node proof).
- **If it fails at the PA12–epoxy interface:** sand harder, flame-pass the socket (one quick pass of a butane lighter), and retest. If using J-B Weld, this test decides.

**Bail sag:**
- Rest the halo on the head form.
- Hang a 100 g bag of coins at N0. The drop must be ≤ 0.5 mm (ruler against a fixed edge).

**Bail proof:**
- With the feet held (helmet on the head form), hang **2 kg** at N0 for 1 minute.
- **Pass:** no crack, no creak, and it returns to within 0.5 mm.

**Pull test per node:** hook the luggage scale at each node in turn and pull 10 N outward and 10 N sideways. Nothing may move.

**Record each result in the build log.**

### 6.7 Strip

1. **File the notches first,** with the strip flat and the jig H20.
   - Mark the N0-post centre on the strip with a pencil line across it, near the strip's middle.
   - File notch β 0 at **16.03 mm to the right** of that line (right = the right-ear end), on the **front** edge. Use the jig for the rest at 40.75 mm pitch.
   - Deburr each notch with one light stroke of 240 grit.
2. Sand the strip's underside at the 5 post positions and the post tops (120 grit); IPA.
3. Lay the bail rear-side-up. Put DP420 on the 5 post tops.
4. Lay the strip on them with the pencil line over N0's post and the strip's front edge 0.5 mm in front of the posts' front faces. It bends itself to the arc.
5. Hold each post with a small binder clip and a scrap block. Cure 24 h.
6. Run the carriage along it by hand afterwards (§11 step K). **Pass:** no felt bump at the posts (leap4-C C3 (e)).

---

## 7. Hinge torque check

The hinge friction is what holds the pad where you put it. The torque fades with use (Southco: about −47 % by 5,000 cycles), and the adjustment screw restores it.

### 7.1 Bench check of each hinge, on arrival

1. Clamp one leaf in a vice with cloth or cardboard jaws.
2. Screw or tape a ruler to the other leaf, pointing away from the pin.
3. Hook the luggage scale 100 mm from the pin. Pull **slowly, at right angles to the ruler**, and read the force at which it starts to move.
4. Torque = kg × 9.81 × 0.1 N·m.

| Hinge | Pass | Scale reading at 100 mm |
|---|---|---|
| Medium E6-10-301-20 | 0.70–0.80 N·m | **0.71–0.82 kg** |
| Small E6-10-101-20 | 0.22–0.25 N·m | **0.22–0.26 kg** |

**If low,** turn the hinge's adjustment screw a quarter turn clockwise and repeat.

**Also test the fold range:** open the leaves flat by hand, then fold them to about 45°. It must go smoothly with no stop in between.

### 7.2 On the head form (assembled)

1. Set α at the rear (bun) detent with the Airpel and a pad, or a dummy of the same moment: **340 g at 185 mm** from the hub axis for the Airpel version, **250 g at 165 mm** for the light float.
2. Leave it 20 minutes. **Pass:** no drift you can see (< 2°).
3. **Push test:** hook the luggage scale at the carriage (≈ 240 mm from the hub axis) and pull along the bail's swing. Read the breakaway force.
   - **Pass:** at least **0.47 kg** (Airpel version; 0.33 kg light float) and at most **1.3 kg**, so one hand moves it easily and it can still be back-driven (red line 7).
4. **Brakes:**
   - start with both brake set screws just touching;
   - add quarter turns, equally on both sides, until the push test passes;
   - stop at 1.3 kg.

**The arithmetic** (`halo_design.py`):
- Need: 0.62 N·m gravity (CoM horizontal, worst case) + 0.11 N·m scrub = 0.73 N·m.
- Hold, medium hinges new: 2 × 0.79 + brakes 0.23 + click 0.12 = 1.93 N·m. Margin 2.6 new, 1.6 when worn with the brakes set.
- Small hinges, light float: margin 1.56 new; 1.10 worn. **Retighten monthly.**

### 7.3 Maintenance

- Repeat the push test **monthly**, or whenever a station "creeps".
- **If it is below the pass value:** retighten the hinge adjustment screws first, then the brakes. Log it.

---

## 8. Mass ledger by part

From `halo_design.py`; printed masses from the CAD volumes at 1.01 g/cm³ (MJF PA12). Two options are shown.

| Part | Default (Airpel, medium hinges) g | Light float, small hinges g |
|---|---|---|
| Front band, 2 × 10 × 1 carbon × 279 | 8.6 | 8.6 |
| H13 forehead node + H14 trigger + foam | 7.3 | 7.3 |
| Head-present switch + wire to the right hub | 1.5 | 1.5 |
| Dial cradle (UltAlt) [VERIFY on the kitchen scale] | 30.0 | 30.0 |
| H15 cradle arms + jaws | 7.8 | 7.8 |
| Temple pads (12 mm foam) | 1.8 | 1.8 |
| H01 hub plates L + R | 43.0 | 31.0 |
| E6 hinges × 2 with fasteners | 32.0 [est] | 18.0 |
| H04/H05 feet | 22.9 | 13.7 |
| H06 α stops + pins + M3 | 4.7 | 4.7 |
| α plunger, brake cords and set screws | 2.2 | 2.2 |
| Carbon 8 × 6 tube, 676 mm | 23.0 | 23.0 |
| Nodes H07 × 4, H08a/b, H09 × 2 | 16.3 | 16.3 |
| Track strip 10 × 1, 371 mm | 5.7 | 5.7 |
| H11 β stops + M3 | 5.3 | 5.3 |
| H16 clips × 6, H17 exit clamp + stub | 7.1 | 7.1 |
| Epoxy | 4.0 | 4.0 |
| Vertex splice and misc M3 hardware | 8.0 | 8.0 |
| H10 carriage + spool | 10.8 | 10.8 |
| Rollers, pins, plunger, cord, set screw | 5.6 | 5.6 |
| **Float** | **96.0** (Airpel E16D2.0N, catalogue) | **15.0** (proposed) |
| QEV + float relief | 8.0 [est] | 8.0 [est] |
| H12 spider + balls + magnets + nut | 9.1 | 9.1 |
| Constant-force spring + guide rod | 3.4 | 3.4 |
| Pad (PAD WP, spec) | 81.5 | 81.5 |
| Head-side harness, ≈ 0.72 m | 31.0 | 31.0 |
| Umbilical head share (spec) | 11.0 | 11.0 |
| Pogo lanyard half | 1.0 | 1.0 |
| **Total head-borne** | **≈ 488** | **≈ 373** |

**Gates:**
- **Spec:** 286 g; gate B1/C2 ≤ 320 g; red line 10 ≤ 500 g.
- The spec ledger did not include real hinge masses, cradle arms, stops, clips, epoxy or hardware, and assumed a 16 g float (CONFLICTS #11).
- Both options pass red line 10. **The default has only 12 g of margin.**

**Centre of mass and lean** (head upright, design head):

| Pose | Default lean | Light-float lean |
|---|---|---|
| α −25° | 0.23 N·m | 0.14 N·m |
| α 0° | 0.04 N·m | 0.04 N·m |
| α +45° | 0.46 N·m | 0.31 N·m |
| **α +90° (worst)** | **0.63 N·m** | **0.42 N·m** |
| β ±40° | 0.27 / 0.31 N·m | 0.13 / 0.17 N·m |

- Cradle form lock is 1–1.5 N·m: margin 1.6–2.4 (default) and 2.4–3.6 (light).
- The spec wanted ≥ 3.7. **V15 (cradle hold ≥ 1 N·m) must be measured at S0.**

**Weigh on arrival.** Weigh every printed part and the bought parts on the kitchen scale and correct the ledger. Gate B1 is the weighed total.

---

## 9. Stop-setting procedure (Stage C1): from your hairline and your ears

**Purpose:** make it mechanically impossible for any nail to reach in front of the hairline or within 25 mm of an ear canal (red line 6), even if the helmet sits 15 mm off its normal place (gate C4).

**Rules:**
- Do it with the drive box **unpowered** (pins vented, pad on its spring).
- **Never with the lever held.**
- You need:
  - the eyeliner dots from §3 item 7;
  - a helper;
  - the ruler;
  - a 35 mm-radius paper disc with a centre hole (cut from card: this is the nail reach, block ±17 mm + pentagon 18 mm);
  - a 2.5 mm hex key;
  - Bumpons.

### 9.1 Seat and zero

1. Put the helmet on as for a session: dial snug, band on its mark.
2. Clip the zero gauge H19 on the Airpel.
3. Look at the mark on the wall at eye height.
4. At the α 0 detent and β 0 notch, read the phone level on the gauge. **Write down both tilts.**
   - A few degrees is normal.
   - If either is more than 8°: the helmet is pitched or rolled on your head. Re-seat it (band lower or higher, dial tighter) and repeat.
5. Mark the band's position on the forehead with a dot. This is the "normal seat".

### 9.2 Front α stop (hairline)

1. Make a second eyeliner dot **15 mm behind** each hairline dot (midline and ±30 mm), along the scalp. These are the limit dots.
2. Loosen the front α stop block (M3 from the inboard side) and slide it fully forward.
3. Push the pad down gently by hand until the skids rest on the scalp.
4. Hold the paper disc's centre under the pad axis: look along the gauge to find it. The helper slides the disc under the pad.
5. Swing the bail forward slowly until the disc's front edge touches the **limit dot** on the midline. Check the ±30 mm dots are also behind the disc edge.
6. Hold the bail there. Slide the front stop block back until its Bumpon touches the α arm.
7. Find the ring hole that one of the block's two pins drops into, **on the safe side** (block moved back, not forward). Push the Ø3 × 8 pin in.
8. Tighten the M3 with a drop of Loctite 222. Paint-mark the screw head and the block.
9. **Check:** with the helmet pushed 15 mm forward on the head (helper pushes the band), the disc edge must still be behind the hairline dot. If not, move the block one 5° step back.

**Expect about α_pad −29° on the design head.** The calculator prints your predicted value. The spec's "+20° from the hairline" would have been −41°, which is in front of the hairline (CONFLICTS #7).

### 9.3 β stops (ears)

1. Clamp both β stop blocks on chord 3, well outboard.
2. Move the carriage to β −40 (right). Lower the pad by hand to the scalp.
3. The helper holds the paper disc under the pad axis and measures from the disc's lower edge to the ear-canal opening with the ruler, shortest straight line.
   - **It must be ≥ 40 mm** (25 mm red line + 15 mm seat slip).
   - If not, move the carriage one notch toward the top and measure again.
4. At the first notch that passes, slide the right β stop block until its Bumpon touches the carriage cheek end. Tighten the M3 pinch screw and paint-mark it.
5. Repeat on the left.
6. **Check:** push the helmet 15 mm sideways toward that ear and re-measure. It must be ≥ 25 mm.

**Expect about β ±35° on the design head** (calculator: at ±40° the reach is 32 mm seated, 17 mm slipped; CONFLICTS #8).

### 9.4 Rear α stop (cradle, bun)

1. With the carriage at β 0, swing the bail back until the rear skid is **10 mm above the cradle's top edge**, or until α_pad +100°, whichever comes first.
2. Set the rear block as in §9.2 steps 6–8.
3. **Check** that the bun stays free ≥ 60 mm above the cradle edge (C1).

### 9.5 Log and recheck

- Write the four stop angles (read the detent number nearest each), the gauge tilts and the β notch numbers in the build log.
- Recheck all stops after the first 5 sessions, then monthly, and after any knock.
- **Any screw that has moved off its paint mark: stop and reset.**

---

## 10. Coverage

**Basis:** spec §4.7 method, re-run with this halo's stops.

| Scalp region | α −29…100°, β ±35° | Note |
|---|---|---|
| Crown / vertex | 100 % | |
| Upper occiput | 100 % | |
| Bun / lower occiput | ≈ 90 % | rear stop at the cradle |
| Parietal sides | ≈ 75 % | ≈ 80 % with β ±40° if your ears allow |
| Frontal top | ≈ 75 % | front stop 15 mm behind the hairline |
| Low sides / temples | ≈ 50 % | |
| **Total** | **≈ 82 %** [EST] | ≈ 85 % at the spec's ±40° |

**Stations:**
- About 9 α detents × 7–9 β notches, minus corners: about 50–60 usable stations.
- Gate V18 checks this on your head.

---

## 11. Assembly steps for a first-timer

**Before you start:**
- Read each step to the end before doing it.
- Lay out the parts for the step on a towel.
- Tools for every step:
  - 2.5 and 3 mm hex keys;
  - small cross-head screwdriver;
  - 7 mm and 5.5 mm spanners (or pliers);
  - soldering iron with an insert tip;
  - calipers;
  - kitchen scale;
  - IPA;
  - masking tape.
- **"Snug" means:** turn until it stops, then about 1/8 turn more with the small key held at its short end. Plastic threads strip easily.

### Stage S0 (week 1): coin test, no printed parts

**S0-a. Tape fit.** Do §3 and enter the numbers.

**S0-b. Hinges on the cheap helmet.**
1. Check the hinges first (§7.1).
2. Screw one medium hinge to each side of the $13 bike helmet's shell, just above the ears: M4 × 10 with nuts and washers through 4.5 mm holes you drill in the shell.
3. Screw a 300 mm stick (a paint stirrer or a 10 mm dowel) across the two free leaves so it swings over your head like the bail.
4. Hang a coin bag on it so the moment matches §7.2: **340 g at 185 mm** for the Airpel case.
5. Watch TV for 20 minutes at α 0, 45 and 90°. Rate the lean (spec S0 gate: ≤ 3/10).
6. Re-index it with your eyes closed (must take < 3 s).

**S0-c. Cradle hold (V15).**
1. Put the UltAlt cradle on, hooked under the occipital shelf. Tighten the dial.
2. Hook the luggage scale at the front of the helmet. Pull up and back slowly; read the force at which it starts to come off (override, target ≈ 10 N).
3. Pull straight back at the top; read the force times the height above the ear (hold, target ≥ 1 N·m).
4. Write both down. **If hold < 1 N·m, stop and tell the HALO owner.**

### Stage B: build the halo (≈ 14–20 h over two weekends)

**H1. Inspect the prints.**
1. Weigh each one against the table in `cad/README.md` (±10 %).
2. Check each socket with a tube offcut (§6.2).
3. Check the Ø3 pin holes with a pin.
4. Sand any edge that a fingernail catches.

**H2. Heat-set inserts.** Iron at 220 °C with the insert tip. Push straight, let the plastic flow, and stop when the insert top is flush. Hold a flat steel ruler on it for 5 s while it cools.

| Part | Inserts |
|---|---|
| Hub plates | 2 × M3 cradle lug; medium hinge: 2 × M4 per seat |
| Feet | 2 × M4 hinge (medium); 1 × M3 brake; left foot also 1 × M4 plunger |
| α stop blocks | 1 × M3 each |
| Carriage | 1 × M4 plunger, 1 × M3 friction set screw |

**Good looks like:** flush, square, no plastic ring pushed up around it. **Crooked:** reheat and straighten within 10 s.

**H3. Temple pads.** Stick the hook-and-loop to the hub plates' inboard faces. Put two layers of 6 mm pad on each.

**H4. Band dry fit.**
1. Cut the two 10 × 1 strips to 290 mm (§6.1 method).
2. Do the 24 h bend soak on an offcut (§4.1).
3. Slide the strips into the left hub-plate pocket, through the forehead node slot (lip on top, switch block below), and into the right pocket.
4. Put the halo on your head with the cradle fitted (step H6) and look in the mirror. The node should sit on the midline, 45 mm above the brow, and the hub plates should rest on the temple pads.
5. Trim the strips so each ends at the pocket bottom. Mark the strips at the pocket mouths and at the node edges.

**H5. Band bond.**
1. Sand the strips' bond zones (pockets and node).
2. Drill the Ø3.2 cross-bolt holes through each hub plate's hole and both strips (clamp them, drill slowly).
3. DP420 in the pockets and the node slot, strips in. Fit the M3 × 12 cross-bolt with its nut, snug.
4. Strap the assembly onto the head form at the right width (a towel-wrapped bucket close to your HB works) and let it cure 24 h.

**H6. Cradle.**
1. Bolt the H15 adapters to the hub-plate lugs with M3 × 10.
2. Put the UltAlt cradle on the head form, hooked under the "shelf".
3. Lay each side-arm tab on its adapter clamp plate with a strip of pad foam, fit the H15b jaw, and do up 2 × M3 × 10 with nuts, snug.
4. Try it on your head. Tighten the dial. The halo should not rock when you nod. **The cradle must be under the bump, never on it.**

**H7. Head-present switch.**
1. Solder two 26 AWG wires (red and black, 400 mm) to the D2F-01FL's **COM and NO** tags. Heat-shrink each.
2. Put the switch in its pocket, lever toward the skin, wires out through the hole. Do not glue yet.
3. Press the two Ø3 × 12 pins into the trigger plate H14 (tight fit; tap with a hammer on a hard surface). Slide them into the node's guide holes from the skin side. Fit an M3 washer on each pin tip at the back and glue it with a drop of CA.
4. **Click test:** with the meter on beep, press the plate with one finger. It must click and beep within its first 1–2 mm of travel and release when you let go.
   - If it beeps too early or never, shift the switch 0.5 mm in its pocket with a paper shim.
   - Then glue the switch with a dot of epoxy on each side.
5. Run the wires along the band's rear face with three dots of CA glue to the right hub plate.
6. Leave 60 mm slack around the right hinge so it can swing.
7. Stick the forehead foam around the trigger plate. The trigger foam must stand **1–2 mm proud**.

**H8. Hinges.**
1. **Medium:** each hinge goes on the hub-plate seat (leaf face flat on the seat, pin on the axis mark) with 2 × M4 × 10 into the inserts, snug.
2. **Small:** studs through the seat holes; press the push-on nuts on with a 10 mm socket.
3. Then fit the foot on the other leaf the same way.
4. **Check:** the foot swings freely through the whole range and its arm passes 0.5 mm above the hub-plate face without touching.

**H9. Brakes and α detent.**
1. Push a 4 mm piece of Ø3 NBR cord into each foot's brake pocket. Screw in an M3 × 8 set screw until it just touches.
2. Left foot: screw the M4 ball plunger in from the top until its ball just touches the hub-plate face between notches, then a half turn more.
3. Swing the foot. You should feel and hear a click at every 15°.
4. **If no click:** screw the plunger in a quarter turn. **If it jams:** back out a quarter turn.

**H10. α stop blocks.**
1. Press a Ø3 × 8 pin into one of each block's pin holes.
2. Fit the blocks to the left hub plate's front and rear ring sectors with M3 × 10 from the inboard side, loosely. You set them in §9.
3. Stick Bumpons on the faces the arm will hit.

**H11. Bail.** Do §6.1–6.6 (cut, dry fit, prepare, bond the arc, legs, then feet on the helmet, then proof).

**H12. Strip and notches.** Do §6.7.

**H13. Carriage.** Hang it on the strip before the β stops go on. The strip is open at its ends, so the carriage slides on from one end.
1. Stick one layer of PTFE tape on the cheek and lip inner faces. Trim it with a knife.
2. Press the two Ø3 × 16 outer roller pins through the lip, through an MR63ZZ, and into the cheek.
   - Use a vice with soft jaws. Push slowly; support the part under the hole.
   - The rollers must spin freely.
3. Inner rollers: press a Ø3 × 8 pin into each blind hole in the cheek (pin sticking out 3.3 mm inward), slide an MR63ZZ on, and epoxy an M3 thin washer to the pin tip. Keep glue off the bearing.
4. Push the carriage onto the strip end with **+x (the plunger end) toward the RIGHT ear** and the cheek on the **front** side.
   - The outer rollers go on top, the inner rollers under the strip's front margin.
   - The rear 4.5 mm under the strip stays clear for the posts.
5. Roll it along the whole strip by hand. **Good looks like:** smooth, no bump at the posts, no side-to-side play you can feel.
   - **If tight:** sand the PTFE faces with 240 grit or remove one tape layer.
   - **If loose:** add one more tape layer.
6. Fit the M4 plunger in the cheek boss. Screw it in until each notch clicks clearly, then lock it with a drop of Loctite 222.
7. Put the 10 mm Ø3 NBR cord in the bridge slot with a 3 × 10 printed or plastic shoe on top, and the M3 × 8 set screw above. Tighten until the carriage needs a firm one-finger push between notches (≈ 7 N). Check with the luggage scale: **0.5–0.9 kg**.

**H14. β stop blocks.** Clamp an H11 on each chord 3, tower toward the front (cheek side), loosely. You set them in §9.3.

**H15. Float.**
1. Check the Airpel nose thread and the supplied nut with calipers [VERIFY] before this step.
2. Thread the nut onto the nose. Put the nose up through the plate hole from below, with the Airpel body above the plate and inside the steady collar.
3. Tighten the nut against the plate **by hand only** (≤ 60 lb·in per Airpot). Never clamp the body.
4. Screw the spider on: rod thread up through the hub, 10-32 nut in the hub's hex pocket from below. Snug.
5. Bond the Ø3 × 100 carbon guide rod into the spider's −x socket (DP420), with the rod through the carriage guide lug, so it stays parallel while curing. Cure 24 h.
6. Constant-force spring:
   - slide the coil onto the spool H10b;
   - push the Ø3 × 16 pin through the fork and spool;
   - screw the strip's end hole to the spider's +x stub (M2 × 6 + nut);
   - **pull the spider down and let go: it must snap back up.**
7. QEV and float relief: screw into the Airpel's rear 10-32 port with PTFE thread tape (DRIVE BOX parts). Put a small felt plug in the side port.

**H16. Pad on.** The PAD WP supplies the RCC ring with V-grooves and steel discs. Set the pad on the spider's three balls; the magnets pull it home.
- **Check:** with the luggage scale, it pulls off at **6 ± 2 N** (B3).

**H17. Harness and umbilical exit.**
1. Bond the 30 mm stub into the right foot's axis socket.
2. Bond the exit clamp H17 on the stub's end.
3. Snap the H16 clips onto the right leg (2) and the right chords (3, at mid-chord), saddles on the rear side.
4. Lay the bundle in, zip-tie it, and run it as §4.7.
5. Leave a 230 mm arch from N0 to the carriage. Swing the carriage from β −40 to +40: **the arch must never touch the strip, the carriage top or your hand.**
6. ELECTRONICS fits the pogo lanyard in the H17 pocket.
7. Zip-tie the H18a collar on the sleeve where the hanger's H18b cup will meet it.
8. Pull-test the clip at 3 ± 1 N.

**H18. Weigh** the complete helmet on the kitchen scale (gate B1). Write it in the log.

### Stage C: fit and finish

**C-a.** Do §9 (stops) and §7.2 (torque) on your head.

**C-b. Doff test (C7).**
- Lever released, grab the doff lip, tilt up and back.
- 10 times with eyes closed: each ≤ 3 s, the slowest ≤ 2.5 s.
- **If the cradle snags, loosen the dial one click.**

**C-c. Lean test (C3).**
- 20 minutes of TV with the pad moved every 2 minutes.
- Lean ≤ 2/10; slip ≤ 3° (phone level on the zero gauge before and after).

---

## 12. Printing notes

See `cad/README.md`:
- MJF PA12 at JLC3DP for every head-borne part;
- tolerances and fit diameters;
- which parts need one iteration (carriage, forehead node, cradle arms);
- home-FDM orientation if Michael has a printer.

**Order a second carriage and a second set of H16 clips** in the same batch; they are cheap and are the parts most likely to need a fit change.

---

## 13. Gates HALO answers for (spec §10)

| Gate | What HALO supplies | Pass |
|---|---|---|
| S0 coin test, V15 | §11 S0-b, S0-c | lean ≤ 3/10; re-index < 3 s; cradle hold ≥ 1 N·m |
| V1 | §3 tape fit | numbers entered; checks ALL OK |
| V-H1 hinge torque, leaf pattern | §7.1 | medium 0.71–0.82 kg at 100 mm |
| V-H2 bail mass and sag | §6.6 | ≤ 0.5 mm under 100 g; 2 kg proof |
| B1 / C2 mass | §8, step H18 | spec ≤ 320 g **cannot be met** (CONFLICTS #11). Proposed: ≤ 500 g red line, and the Director re-baselines B1/C2 |
| C1 fit, stops | §9 | stops set and logged; bun free ≥ 60 mm |
| C3 lean | §11 C-c | ≤ 2/10, slip ≤ 3° |
| C4 fences | §9.2 step 9, §9.3 step 6 | hairline: reach behind the hairline with a 15 mm push; ears ≥ 25 mm with a 15 mm push |
| C6 umbilical | §4.7, H17 | clip 3 ± 1 N; lanyard parts before any tube is tight |
| C7 doff | §11 C-b | ≤ 3 s, the slowest ≤ 2.5 s |

---

## 14. Open [VERIFY] items owned by HALO

| # | Item | Closed by |
|---|---|---|
| H-V1 | Medium E6-10-301-20: axis-to-face 6.35, knuckle 12.7, leaf thickness, rotation range, mass | calipers + scale on arrival (S0) |
| H-V2 | Small E6-10-101-20: axis-to-face 5.1, fold range | calipers on arrival |
| H-V3 | Airpel E16D2.0N: body length incl. nose, nut AF and thickness, side-port position, mass | calipers + scale (before ordering prints) |
| H-V4 | UltAlt cradle: mass, tab shape | scale + fit (S0) |
| H-V5 | 9293K123 coil bore (spool 8.8) and end-hole size | calipers |
| H-V6 | D2F-01FL body and hole positions | calipers; click test H7 |
| H-V7 | Pogo connector half: pocket 13.4 × 4.9 × 5.5 | ELECTRONICS part choice |
| H-V8 | Band strain 0.76 %: 24 h bend soak | step H4 |
| H-V9 | DP420 (or J-B Weld) on MJF PA12: coupon ≥ 20 N | §6.6 |
| H-V10 | Torque decay of the hinges in use; brake setting holds | §7.3 monthly log |
| H-V11 | Coverage on Michael's head (spec V18) | C-stage map |

---

*All geometry is regenerated from `cad/halo_params.scad`; numbers in this file are for the design head (spec §3.2) with the default build. Re-run `halo_design.py` after the tape fit and use its printout over these tables.*
