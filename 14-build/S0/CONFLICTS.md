# S0 package: conflicts with SYSTEM-SPEC-v3 and deviations on the bench

**Project SCRATCH · 14-build/S0 · S0 kit engineer · 2026-10-02**

Nothing here edits SYSTEM-SPEC-v3. Each item gives the evidence, what the S0 bench does about it, and the decision needed and from whom.

Numbers come from `cad/dish_kinematics.py`, a rigid-body pose solver on the three balls with z-lift pockets, and from the bench CAD.

---

## #1 MAJOR: the concentric dish moves the nails only 54 % as far as the block, and lands them at about 50°

**Evidence.**
- Three balls held on a sphere about the scalp centre C force the pin block to **rotate about C**.
- Points on the block move in proportion to their distance from C:
  - balls (R 157) move 157 φ;
  - nail tips (R ≈ 85) move 85 φ.
- So every distance on the scalp is **85/157 = 0.54 ×** the same distance at the dish.
- Every slope at the dish becomes atan(tan θ × 157/85) at the scalp.

**Read literally, with d measured at the dish (that is how the bench is built):**

| Quantity (bench solver, 24 headings) | Spec says | Literal dish gives |
|---|---|---|
| Contact rake on the scalp per nail, line through the centre | 17–24 mm (§4.2); S0 pass ≥ 15 mm | **10.2–10.4 mm** |
| Landing angle at the nail, relative to the scalp | ≤ 35° (C5, H-5.3) | **48–62°** |
| Clearance at the turnaround (\|d\| 16.5), reserve 2.0 / 3.5 | ≥ 5 mm | 5.4–5.8 / 3.9–4.3 mm |
| Tilt at \|d\| 16.5 | ≤ 5.5° | 6.6° |

**Read with d measured at the nail plane, as frame S defines it ("pin-block centre projected in P", §3.1):**
- The dish must be scaled in the lateral direction by 157/85.
- Rise is unchanged.
- That gives:
  - sphere to 12.9 mm;
  - inner rim at **20.1° at the dish** to 25.3 mm;
  - outer rim at 32.8° to 31.4 mm.
- With balls at R 43 (`scratchpad v2check`), the solver gives:
  - **rake 19.3–19.8 mm, landing 33–39°, clearance 4.8–5.8 mm**: the spec's intent;
  - but **dish travel ±30.5 mm, tilt 11.1°**;
  - pockets of radius ≈ 36 mm, needing balls at R ≥ 43;
  - a deck of about Ø 165;
  - only a Ø ≈ 12 central island, so a centred lift spring cannot work: it would sit 46° off vertical at the rim and foul the nail bores.
- The tendon yoke would need ±28 mm of travel, not ±17.

**What S0a does.**
- It builds the literal dish, because it is compact and buildable with a centred lift elastic.
- It states the predicted FAILs of the chord and landing pass lines in advance (`S0-guide.md` §3).
- It adds a **hand-rake comparison**: the same block, nails and force, stroked about 25 mm by hand on moving skids. Michael's blind ratings then show directly whether the short, steep dish rake costs sensation.

**Decision needed (Director, then the PAD work package), before any Stage A pad CAD.** Choose one:
- **(a)** Accept a ≈ 10 mm scalp rake. This needs the Director's ruling that C5's ≤ 35° may be read at the dish, which I do not recommend.
- **(b)** The scaled dish. This means a bigger pad (≈ Ø 165 deck), 11° tilt, and a different lift spring, such as three gravity-independent springs or a palm-line latch.
- **(c)** Drop concentric motion: a translating block on a flat or slightly curved dish. Bench solver: rake 20–21 mm, but landing angle 31–52° depending on the nail, and turnaround clearance as low as 3.4 mm.
- **(d)** Keep per-pin gating, which is what leap4-A L1/L2 do.

The S0a sensation data (dish vs hand-rake) is the main input to this choice.

## #2 Spec §4.2 lift line is internally inconsistent

- §4.2 says "lift clearance ≥ 5 mm at the worst reserve for |d| ≥ 13.7".
- But the rise at |d| = 13.7 is only +4.52 mm, so clearance there is 4.52 − reserve, which is 1.0–3.5 mm.
- The bench pass line is therefore applied **at the turnaround** (|d| = 16.5), with the design reserve.
- **PAD work package:** decide whether the outer rim must be steeper or reach farther (e.g. 55°, or top at 18 mm), so that the worst reserve (3.5) still clears 5 mm. The bench predicts 3.9–4.3 mm with N35 nails.

## #3 Balls at R 26 on the bench, not R 22 (spec M11); deck Ø 116, not "Ø 70" (leap4-A)

- Each pocket must hold the ball's full travel: 17 mm, plus a contact offset of up to 2.3 mm on the 50° rim, plus a stop wall. That makes a pocket of radius ≈ 21 mm.
- At R 22 the three pockets overlap and leave no central island for the lift elastic.
- At R 26 they leave a Ø ≈ 10 island and fit in a Ø 116 deck.
- **The PAD work package must re-place the balls** (or the dish concept, see #1).

## #4 Rim rise must be along the pad axis per ball (z-lift), not along each pocket's own radial axis

- First model: pockets revolved about the line from C to each ball home. On the rim, each ball's lift then pushes it sideways in its own pocket, by 0.16 × the rise.
- Result: 3–4° of extra tilt, and the leading nail lost about 2 mm of clearance (3.0 vs 5.4 mm).
- The bench uses: concentric sphere + rise up the pad axis as a function of the ball's lateral offset. The ceiling is the exact envelope of the ball, generated as a polyhedron.
- The **PAD work package should adopt the same construction.**

## #5 Spring nails on the bench, not syringe air nails (spec S0 table, leap4-A (e))

- **Plastic syringe stopper friction** is ≈ 0.3–2 N [est, not measured]. That is larger than the whole 0.08–0.5 N nail force at 2–13 kPa: the nail would stick and then jump.
- **A syringe will not fit** under the 75 mm follower height, with 32 mm of hair clearance and ≥ 57 mm of barrel.
- **The bench uses spring nails instead**:
  - a plunger with a spring in a short bore, set to about 0.15 N at touch-down rising to about 0.3 N at 2 mm in;
  - the force varies 2–3× over the reserve, so it is **not** constant-force;
  - the pump, relief and bleed are therefore not in S0a.
- **Constant air force on both flanks is first tested at Stage A2**, with the real Penrose pins.
- S0a still tests the cone, the force level, the dish gate, the C1 magnetic breakaway and the C2 nail profile.

## #6 Bench nail, compared with spec C4

- **Spec C4:** POM cone on a Ø 1.0 A228 shaft, 2.5° draft.
- **Bench:** one-piece resin nail:
  - the same tip (90° cone from a Ø 2.0 flat with an R 0.4 rim, to Ø 4.5 at 1.25 mm);
  - then a **constant Ø 4.5 stem** (the C2 "constant stem" option) that slides in a Ø 4.7 guide;
  - a 5 mm steel insert (paper-clip wire) at the top for the C1 magnet.
- The magnetic release is set to 0.12–0.25 N with tape shims (guide step D9).
- The nose plate is 32.4 mm above the R 85 contact plane (H-6.3 asks ≥ 32).

## #7 Lift elastic on the bench: ≈ 1.5 N, not 0.5–0.6 N

The bench elastic is about 1.5 N rather than the spec's 0.5–0.6 N, for two reasons:
- the bench block assembly weighs ≈ 55 g, and the C-arm is off-centre;
- the hand drive adds a tipping moment.

**Geometry note for the PAD work package.** A "centred" lift spring between the deck centre and the block centre runs 33° off vertical at |d| = 16.5 on the bench. It also acts as a centring spring of ≈ 0.55 T. This happens because the only free spot at the deck centre is the small island between the pockets.

## #8 Tendon layout (spec M13 / M14) does not fit the travel

- Housing stops at R 48 and yoke posts at R 30, with ±17 mm of travel, leave ≤ 1 mm between a post and its stop. There is no room for the 2 N/mm series spring at the pad (C16).
- **The ink rig uses:**
  - stops at R 60;
  - posts at R 22;
  - **series springs at the box end**, which is statically equivalent; only the dynamic filtering location differs.
- The PAD and DRIVE BOX work packages must re-layout.

## #9 Stock substitutions

| Spec says | What was found (cart-S0b) |
|---|---|
| Series spring 2 N/mm | Nearest stock part: McMaster 9654K959, **1.65 N/mm**, max 11.7 N |
| Drum motor "17HS08-1004S class 13 N·cm" | Current listing: 16 N·cm |
| Tendon "0.45 mm nylon-coated 7×7" | AFW Surflon Micro Supreme DM49-26-A (0.018 in, 26 lb), **5 m spools only**: two spools are needed for three 1.6 m tendons |
| "PTFE-lined coil 1.2 OD / 0.6 ID" | **Not found at retail.** Nearest: 2.0 mm OD stainless sheath spring, sold in 1 m pieces. The 1.6 m baseline is 4 mm bike shift housing. |
| M8P + CB1 bundle | Contains **no drivers and no heatsink**. The CB1 boots from microSD (no eMMC). |

## #10 S0b runs Klipper on the M8P + CB1, not on a Pico + VM

- The spec allows either. The M8P is the Stage A controller, so the test result transfers directly, and about $155 is not thrown away.
- A Pico variant is listed in `cart-S0b.md` as the lean option.

## #11 Landing-spread pass line (≥ 20 ms) on the ball

- On a true sphere all nails share one reserve, so there is no natural spread.
- The bench therefore mixes nail lengths: N20 + N30 + N35. That gives 1.5 mm reserve differences, about 2.2 mm of block travel between landings, ≈ 20 ms at 1.4 Hz.
- With hand drive, the bench measures the spread in **mm of travel**, from video or ink start points.
- The ms figure needs the motor drive (Stage A3).

## #12 Dish lining on the bench: wax or PTFE dry lube, not PTFE film tape (spec §4.2, M11)

- 0.13 mm PTFE film does not lie flat in a 42 mm doubly curved pocket. Strips would leave 0.13 mm steps, which the balls would click over.
- The bench pockets are therefore sanded and waxed, or sprayed with dry PTFE lube.
- The **PAD work package should check film lining on the real dish.** It may also need a sprayed or moulded low-friction surface (for example, a printed-in PTFE-filled filament).
