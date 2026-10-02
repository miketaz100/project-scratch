# PORCUPINE — Pin Unit (PIN TEAM)

**Project SCRATCH · 10-porcupine · 2026-10-01 · Deliverable per PORCUPINE-BRIEF.md "PIN TEAM"**

Tags: `[KNOWN]` = catalogue or literature value with link · `[EST]` = computed or estimated here, verify on the bench · `[UNKNOWN]` = only a test answers it.

Interfaces assumed from the brief only (no cross-reading): the pin mounts on the INNER SHELL and rides with it; the SELECTOR pushes a pin head to park it and lifts a latch to release it; ARCHITECT owns pin pitch, count and the inner-shell standoff from the scalp. Where I need a number from them I say so and give the value I designed to.

---

## 0. Summary and the one decision that matters

The pin unit is a **two-piece music-wire pin (0.8 mm shaft + 0.38 mm neck) carrying a 6 mm mini nail cut from a press-on nail, pushed toward the scalp by a 0.02 N/mm music-wire coil spring in a PTFE-lined printed housing, held parked by a 0.3 mm feeler-steel latch leaf, and sealed at the shell exit by a double silicone wiper lip.** Per pin: 3.6 g, about $2.40 in parts at qty 36, 0.8 g moving.

The decision that matters is the spring rate. Judge-2 F1 says the strap seats to about ±3 mm and the head breathes; the brief widens that to **±5 mm of seating slop**. With a linear spring the force swing over ±5 mm is **5 mm × k regardless of preload**, so the brief's own target (0.3–0.5 N, i.e. ±0.1 N about 0.4 N) fixes **k ≤ 0.02 N/mm** `[EST, arithmetic]`. That is 6–20× softer than every leaf in 05-engineering/mechanical.md §8 (0.12–0.18 N/mm, which would swing ±0.6–0.9 N: the whole scratch window, exactly F1's complaint). A 0.02 N/mm spring that must also reach 0.7 N at park is inherently **~40 mm long** (0.7 N / 0.02 N/mm = 35 mm of compression plus solid height). That length is the price of a force reference that survives head motion, and it is the main thing I am handing the ARCHITECT and DRIVE teams as a height problem (§9).

Three variants were costed (§3): V1 coil-in-bore (picked), V2 flat leaf plunger (compact fallback), V3 buckled-strip constant force (SP2 idea, ±5 % but fatigue-risky). V1 wins on buildability: twelve identical units from one jig in an evening, all parts from K&S, McMaster, Amazon and a nail-supply shop.

---

## 1. Requirements the pin must meet (from the bound documents)

| # | Requirement | Value | Source |
|---|---|---|---|
| R1 | Scalp normal force per contact, operating | 0.3–0.5 N nominal, window 0.3–0.9 N | brief; tip-interface §2.5 |
| R2 | Force variation over ±5 mm seating | ≤ ±25 % of nominal | brief (PIN TEAM item) |
| R3 | Mechanical force cap, independent of actuators | ≤ 2.5 N per contact, ≤ 12 N total | safety red line 2, 3 |
| R4–6 | Edge R ≥ 0.4 mm (window 0.2–0.6), corners ≥ 1 mm; nail 4–8 mm wide; attack 45° (35–55°) | geometry | safety §3.5, red line 11; tip-interface §2.5, §2.3; brief |
| R7 | Protrusion beyond adjacent surface when extended | ≥ 25 mm design basis | hair H-4.5 |
| R8–9 | No 0.04–3 mm gap and no changing gap within 25 mm of scalp; faces drafted ≥ 10°, no necks/grooves below the canopy, edges ≥ 0.5 mm (≥ 1 mm facing scalp) | sealed or > 3 mm | hair H-4.9, H-6.3, H-4.3, H-4.4, H-4.10 |
| R10–11 | Tangential: ≤ 2 N hard cap, deflect/lift at ≤ 1.5 N (H-4.11's 0.15 N ideal: nobody meets it, F4); normal tip stiffness ≤ 0.5 N/mm with ≥ 5 mm travel | — | safety §2.3; hair H-4.11; scratch-model §8 crit. 9 |
| R13 | Parked state | zero contact with the head at any seating | safety §2.2; brief |
| R16 | Tip retention: positive, proof-loaded 3× (≈ 1.5 N here, 7.5 N for the latch cap) | — | safety §3.6, red line 9 |

Scratch-model §3 inputs: tangential 0.05–0.1 N steady, 0.3 N spikes (3.5); stroke 25–35 mm at 50–150 mm/s, 1–2.5 Hz (brief); scalp R 85–100 mm (3.16); edge contact 4 mm (3.11a).

---

## 2. Anatomy of the unit (V1, as picked)

Reading from the scalp outward, with the pin **extended and at nominal seating**:

```
scalp ─── nail edge (6 mm wide, R 0.4 edge, 45° attack)
          │ 1.5 mm   nail free edge beyond ferrule line
          │ 12 mm    NECK: 0.38 mm music wire, pre-bent 45°, inside a 1.0 mm PTFE sleeve
          ● 4 mm     FERRULE: 1/16" brass tube, soldered, filleted with CA (no crevice)
          │          SHAFT: 0.80 mm music wire, straight, polished
          │ 20 mm    …in hair, free
   ─ ─ ─ ─│─ ─ ─ ─   inner-shell underside (ARCHITECT: 20–25 mm above scalp)
          │ 15 mm    NOSE: drafted PETG cone, 15° draft, R 1 mm, double silicone wiper at its tip
         ╞╡          inner shell plate (2 mm)
          │ 31 mm    HOUSING: 7.0 mm bore, PTFE guide tube 2 mm OD × 1.0 ID × 25 mm, coil spring around the shaft
          ▀ 3 mm     CAP: printed head with 0.5 mm latch shoulder, the part the selector touches
          ─ latch leaf (0.3 mm feeler steel) — engaged only when parked
```

Stroke map (z = pin axial position measured from the fully-extended hard stop, positive = pushed into the housing):

| State | z (mm) | Spring force (N) | Note |
|---|---|---|---|
| Extended hard stop (no head) | 0 | 0.05 preload | nail 40 mm below shell underside |
| Nominal seating, head present | 20 | **0.45** | window centre; chosen so −5 mm gives 0.35 N |
| Seating −5 mm (head further away) | 15 | 0.35 | −22 % |
| Seating +5 mm (head closer) | 25 | 0.55 | +22 % |
| Scalp bump / flinch, worst | 30 | 0.65 | still 4× under R3 |
| **Parked (latched)** | 35 | 0.75 | nail 15 mm above nominal scalp, 10 mm above at +5 mm slop |
| Housing bottom (selector over-push) | 38 | 0.81 | solid height not reached (spring solid at z ≈ 42) |

Mechanical force constant: **F_max = 0.05 + 0.02 × 38 = 0.81 N** at the housing floor, with no actuator in the force path (the shell drive moves the pin tangentially; the selector only pushes it *away* from the head). Red line 2 by geometry; 36 pins bottomed would be 29 N but only 3–5 are ever released (≤ 4 N) `[EST]`. Normal tip stiffness is the spring, **0.02 N/mm**, 25× under criterion 9 and deliberately softer than tip-interface §5.4's "pulp-like 0.3–0.6 N/mm": head-worn, the spring is a force *reference*, not a force *feel*; the fold/release dynamics come from the stiff edge and the skin `[EST — hypothesis; T-P8 A/Bs a 0.06 N/mm spring]`.

---

## 3. Variants and the pick

| | V1 coil-in-bore (PICK) | V2 flat leaf plunger | V3 buckled-strip constant force |
|---|---|---|---|
| Spring | music-wire coil, 0.30 mm wire, 6.5 mm mean dia, 15 active coils, k ≈ 0.020 N/mm, free length ≈ 45 mm, coaxial on the pin in a 7 mm bore | 0.30 × 6 mm feeler-steel cantilever, 74 mm long, lying flat on the shell, pressing on the pin cap; k_tip = 0.020 N/mm `[EST]` | 0.10 × 4 × 40 mm feeler strip loaded as a pin-ended Euler column, Pcr = 0.41 N; post-buckled load rises only ~5 % over 10 mm `[EST]` |
| Force swing over ±5 mm | ±0.10 N (±22 %) | ±0.10 N (±22 %) plus ~5–20 % geometric stiffening at large deflection | ±0.02 N (±5 %) |
| Height above inner shell | **34 mm** (31 housing + 3 cap) | ~10 mm (leaf + cap) but leaf runs 74 mm *along* the shell; 12 leaves cross each other's pins → two leaf levels and a slot for every crossing | ~45 mm (column length) |
| Park force | 0.75 N | 0.75 N; leaf end at 35 mm slopes 40° and foreshortens 6.6 mm, so it must *slide* on a domed cap | 0.43 N |
| Max stress / life | 530 MPa shear at 0.81 N (Wahl) vs ~1000 MPa torsional endurance: infinite `[EST]` | 575 MPa static at park, ±125 MPa cyclic: infinite; edge-limited 500 MPa (RT2) matters only at park | ~780 MPa bending at 10 mm shortening `[EST]`, above sheared-feeler endurance: thousands of cycles, not infinite | 575 MPa at 35 mm static (park), ±125 MPa cyclic about nominal → infinite in bending; edge-limited ~500 MPa (RT2 §4) is a concern only at the static park value | ~780 MPa bending at midspan when shortened 10 mm `[EST]`, above the 500–600 MPa edge-limited endurance of sheared feeler stock → life counted in thousands of cycles, not infinite |
| Apartment build of 12 | one jig, ~3 h | ~6 h, leaf lanes depend on the pin layout (ARCHITECT coupling) | ~4 h, but strip-end seating is fiddly |
| Verdict | **pick** — simplest, decoupled from pin layout, honest height | fallback if the ARCHITECT cannot give 34 mm above the shell | SP2 experiment: the flattest force curve on the table |

Rejected: the mechanical §8 leaf as-is (0.12–0.18 N/mm → ±0.6–0.9 N over ±5 mm, 3–4× outside R2: this is F1); stock constant-force clock springs (smallest is Lee LCF 250 05 038S at 0.2 lb = 0.89 N `[KNOWN]`, twice the park force); magnet-cancelled zero-stiffness (tunable, but a trap for a first build); printed TPU serpentines (creep drifts the very reference they are meant to fix). Preload does not reduce the swing (it is 5 mm × k), so the only ways past ±22 % are a constant-force element (V3) or less slop (ARCHITECT: skull registration).

---

## 3b. Flexible neck vs a free ball-socket tip (Director's question)

Michael asked whether the nail should sit on a miniature ball joint with hemispherical freedom instead of a spring-centred neck. Numbers first, then the ruling.

**How much tilt is actually needed.** On an R 90 mm scalp the local normal rotates by 1 rad per 90 mm, so a 30 mm stroke sweeps **19° (±9.5°)** `[EST, geometry]`. But the brief's inner shell *follows the skull's curvature* (orbits/strokes on a spherical surface about the skull centre), so the pin axis stays normal and the stroke itself needs **0°** of tilt; what remains is the mismatch between the shell's sphere and the real head (R 85–100 crown, 100–150 parietal, scratch-model 3.16) plus seating: **±5–10°** `[EST]`. If the DRIVE team chooses a flat X/Y translation instead of a skull-centred orbit, add the ±9.5° and the pin needs ±15–20°. For a 6 mm nail, 9.5° of roll lifts one corner 1.0 mm, which the 1.6 mm of skin indentation at 0.3 N (tip-interface §2.2) mostly absorbs; a 12 mm nail lifts 2 mm and digs. **Narrow nails need little self-alignment; wide ones need a lot** — hence the 6 mm nail (§4.2).

**Does the nail stay edge-presented under drag?** Moments about the neck root (12 mm above the edge) for the 0.38 mm × 12 mm wire neck, k_ang = 17 N·mm/rad `[EST]`:

| Load | Moment | Neck pitch | Attack angle (from 45°) | Neck stress |
|---|---|---|---|---|
| Steady drag 0.05–0.1 N (3.5) | 0.6–1.2 N·mm | 2–4° | 41–43° | 110–220 MPa |
| Drag spike 0.3 N | 3.6 N·mm | 12° | 33° (momentarily below the 35° floor; glides, no bite) | 670 MPa |
| Normal 0.3–0.5 N × 3 mm edge offset | 0.9–1.5 N·mm | 3–5° (pre-bend compensates) | — | — |

So the neck holds the edge presented at steady loads and yields toward "glide" on a spike, which is the safe direction (tip-interface §2.3: shallower angle = plating, steeper = catching). Roll (about the pin axis, 13.5 N·mm/rad torsion) sees no drag moment at all because the drag acts in the stroke plane; it only sees the curvature-mismatch couple, which it is soft enough to follow at 3–5° per 0.3 N.

A **free ball** has zero restoring moment. Its edge sits 8 mm from the ball centre; a drag of 0.1 N makes 0.8 N·mm with nothing to react it, so the nail pitches until something else stops it: it **casters** — the plate trails the pivot and lies flat on the scalp (attack angle → 0°, a pad, not a scratch), and on reversal it flips through 90° and lands on the opposite corner. Cross-grain hair drag (asymmetric) rolls it onto a corner. To keep a ball within ±10° at 0.3 N drag you need ≥ 14 N·mm/rad of centring `[EST]` — which is the wire neck's stiffness. In other words **a ball socket that works is a ball socket plus a spring, and the spring is the neck**.

**Sealing.** A 3 mm ball in a printed socket is a changing gap of 50–200 µm within 15 mm of the scalp — the H-4.9 trap band exactly, and a joint that hair-interaction §3.7 says must be booted. A booted ball (TPU/silicone sleeve) is then a neck with a bearing inside it; the boot supplies 5–20 N·mm/rad `[EST]` of centring anyway, fouls with sebum (H-4.7 rates TPU/silicone "grabby"), and adds a crevice at the boot lip (safety §8). The wire neck in a bonded PTFE sleeve has **no gap and no seam below the ferrule** (§4.3).

| | Flexible neck (0.38 mm wire, 12 mm) | Sealed mini ball socket (3 mm ball, printed socket, TPU boot) |
|---|---|---|
| Passive tilt | ±10–15° at scratch loads; elastic to ~60° | hemispherical, but the boot sets the useful ±15–25° |
| Edge stays presented | yes: 4° pitch at 0.1 N, 12° (glides) at a 0.3 N spike | only with boot centring ≥ 5 N·mm/rad; a free ball casters flat at 0.1 N and flips to a corner on reversal |
| Tilt needed (±5–10°; ±15–20° if flat stroke) | covered / marginal | covered / covered |
| Hair sealing within 30 mm | sleeve bonded both ends, no gap | boot with a lip seam; socket gap is a trap if the boot tears |
| Mass | 0.05 g (neck + sleeve) | 0.3–0.5 g (ball, socket, boot) |
| Cost per pin | $0.05 | $0.40–0.80, plus a socket print per pin |
| Fatigue | 110–220 MPa at steady drag: infinite life in bending for music wire (fatigue strength ~1280 MPa `[KNOWN, MakeItFrom A228]`); 670 MPa spikes are rare events | no metal fatigue; boot creep and sebum fouling instead; socket wear in PETG |

**Recommendation: flexible neck.** It gives the ±10° the architecture needs, keeps the edge presented at the forces scratch-model §3 lists, has no gap, weighs nothing, and is one 12 mm length of K&S wire.

**The one case for a ball socket:** a **wide nail (≥ 10 mm, i.e. a full TM1 tip A) on a pin whose axis is *not* curvature-following** (flat-stroking shell, or a pin field on a rigid flat sector), where the required tilt is ±15–20° *and* corner lift must stay under ~0.5 mm. There the wire neck would need to be so thin that it buckles under 0.5 N (a 0.25 mm neck has Pcr ≈ 0.6 N at 12 mm `[EST]`), and a 4 mm ball with a thin silicone boot as the centring spring (≈ 5–8 N·mm/rad) is the better part. SP1's 6 mm nail on a skull-centred shell is not that case.

---

## 4. Detailed design, V1

### 4.1 Pin shaft

- **Material:** ASTM A228 music wire, **0.80 mm (0.031")** dia, K&S Precision Metals 36" lengths; K&S lists tensile 290–352 kpsi (2.0–2.4 GPa) for its 0.039"/0.047" wire and the same alloy family down to 0.015" `[KNOWN]` ([K&S 36" music wire range](https://ksmetals.com/collections/36-long-music-wire), [0.039" spec](https://www.zoro.com/ks-precision-metals-music-wire-0039-in-dia-36-in-l-steel-318-000-to-352-000-psi-tensile-strength-497/i/G513756385/)). McMaster carries the same as "phosphate-coated 1080 spring steel" by diameter `[KNOWN]` ([McMaster wire by diameter](https://www.mcmaster.com/products/wire/diameter~0-039/)). Why not 1.0 mm: 0.8 mm is the largest wire that fits the 1.0 mm-ID PTFE guide tube with a comfortable 0.1 mm radial clearance and still passes R10 (Pcr) with a 4× margin.
- **Length:** 60 mm (3 mm in the cap, 25 mm in the guide, 20 mm free below the nose at nominal, 12 mm overlap/ferrule allowance). Cut from one 36" length: 15 pins per stick.
- **Bending under drag** (35 mm cantilever below the guide): 0.19 N/mm → 0.5 mm at 0.1 N, 1.6 mm at 0.3 N; 60–180 MPa, infinite life `[EST]`. In series with the neck (0.36 N/mm) the tangential tip compliance is **≈ 0.12 N/mm**: 1.2 mm at 0.15 N, 3 mm at 0.37 N — hair item 7 scored 1 like every candidate (F4); the 2 N cap (R10) is met by the neck yielding at ≈ 0.75 N (§4.3).
- **Buckling under 0.5 N axial:** Euler cantilever from the guide, L = 35 mm: Pcr = π²EI/(4L²) = **20 N** `[EST]`, 25–40× over the 0.5 N service and 0.81 N cap; the neck is the weak column (3.5 N, §4.3).
- **Finish:** IPA off the oil, 2000-grit the 35 mm that passes the wiper, radius the cut end. Steel pin is groundable through the latch leaf (H-4.12).
- **Alternatives:** 1.0 mm superelastic nitinol (Kellogg's Research Labs 0.040" straight-annealed, 5 ft `[KNOWN]` [listing](https://www.amazon.com/Kelloggs-Research-Labs-Superelastic-Nitinol/dp/B00E4TE05Y), ~$35/5 ft, intermittently stocked) is as stiff as 0.7–0.8 mm steel and survives a 90° flinch without set: the shaft upgrade if bent pins recur. 1.5 mm pultruded carbon rod (flexural modulus ~130 GPa `[KNOWN]` [Goodwinds](https://goodwinds.com/composite-resources/technical-material-specifications/)) splinters at the cut and cannot be soldered or bent: rejected.

### 4.2 Nail tip (mini nail)

- **Geometry:** 6.0 mm wide × ~8 mm long plate, 0.6–0.8 mm thick, transverse curvature as cut from the press-on (R 8–10 mm), plan-form convex, **corners R 1.0 mm**, **edge radius 0.4 mm** (safety floor; tip-interface window 0.2–0.6), free edge 1.5 mm beyond the neck sleeve. Attack angle 45° set by the neck pre-bend. Contact length on an R 90 sphere at 0.3 N ≈ 4 mm `[EST, scratch-model 3.11a]`, line load 0.075–0.125 N/mm at 0.3–0.5 N: dead centre of the "##" band.
- **Stock:** press-on ABS/acrylic nails, sizes 0–3 are 10–13 mm wide `[KNOWN, tip-interface §4]`, ~0.6–0.8 mm thick `[EST]`; one nail yields one 6 mm centre strip (keeps the factory curvature). Alternative flat stock: 0.8 mm PETG or nylon sheet, or a Dunlop Tortex 0.73/0.88 mm pick (POM, the low-friction arm) `[KNOWN gauges]` ([Tortex range](https://www.jimdunlop.com/products/guitar-picks/tortex/)). Nylon for the ≤ 0.6 mm thin variant.
- **Bond:** the neck's last 4 mm hooks into a scored groove on the nail back, gel-CA bonded and over-filleted with a 1 mm bead of thick CA/UV resin: no crevice, no re-entrant feature (R9, R17). Proof: 150 g (1.5 N, 3× R1) hung from the nail, per tip (R16).
- **Finish:** file 400 → 1000 → 2000, 1 s flame pass (ABS/PETG only), cotton-ball burr test, loupe vs a 0.8 mm drill shank (R 0.4). Red/orange nails so a lost tip shows in hair.
- **Mass:** 0.10 g.

### 4.3 Flexible neck

- **Wire:** K&S music wire **0.015" (0.38 mm)**, 36" lengths `[KNOWN]`, cut to 20 mm: 12 mm flexible, 4 mm hooked into the nail, 4 mm into the ferrule.
- **Pre-bend:** 45° at 2 mm above the nail hook, over a 2 mm pin in the jig (§8), so the plate sits at 45° to the pin axis with the edge leading in the +X stroke sense. One bend only; music wire takes a cold bend of this radius without cracking `[KNOWN practice, EST margin]`; no second bend at the same spot.
- **Stiffness** (§3b table): k_ang 17 N·mm/rad bending, 13.5 N·mm/rad torsion, 0.36 N/mm at the tip `[EST]`. Buckling as a 12 mm cantilever: Pcr = π²EI/(4L²) = **3.5 N** `[EST]`, 7× the 0.5 N service axial load.
- **Plastic fuse:** M_y ≈ σ_y·I/(d/2) with σ_y ≈ 1.7 GPa → 9 N·mm → the neck takes a set at ≈ **0.75 N tangential at the edge** `[EST]`: above the 0.3 N spike, below the 2 N cap, and the bent-but-attached nail is visible and still faces forward. Replacing a neck is a 5-minute ferrule swap.
- **Sleeve:** PTFE tube **1.0 ID × 2.0 OD** ([ptfetubeshop](https://ptfetubeshop.com/en/product/ptfe-tube-1mm-x-2mm/) `[KNOWN]`), 11 mm, CA-bonded at both ends so the annulus is closed (no gap a hair can enter); it is the smooth drafted face hair meets (R9). Caveat: PTFE E ≈ 0.5 GPa gives the tube EI ≈ 370 N·mm² vs 205 for the wire, so the bonded composite neck is **1.5–2.8× stiffer** than the wire-only numbers above `[EST]`; if T-P3 shows corner contact, shorten the sleeve to 8 mm or slit it. `[UNKNOWN until T-P3]`
- **Fatigue:** 220 MPa at 0.1 N drag over ~10⁶ cycles (2.5 Hz × 20 min × 300 sessions) against ~1.3 GPa fatigue strength for A228 `[KNOWN]` ([MakeItFrom](https://www.makeitfrom.com/material-properties/ASTM-A228-SWP-A-K08500-Music-Wire)): infinite life; the pre-bend is the stress raiser — inspect at every tip change. `[EST]`
- **Ferrule:** K&S 1/16" brass tube (1.59 OD, ~0.9 ID), 4 mm: 0.8 mm shaft in one end, neck plus a 0.38 mm filler in the other, soft-soldered (acid flux, scuffed wire), then a CA/resin fillet to a 15°-drafted, crevice-free cone (H-4.3). 0.03 g.

### 4.4 Soft long-travel spring and guide

- **Spring:** music-wire compression spring, **wire 0.30 mm, mean dia 6.5 mm (OD 6.8), 15 active coils, closed-and-ground ends, free length 45 mm**: k = G d⁴ / (8 D³ n) = 79.3 GPa × 0.0081 / (8 × 274.6 × 15) = **0.0195 N/mm** `[EST]`; solid height 5.1 mm; spring index C = 21.7 (soft, must be guided — it is, on the 0.8 mm shaft inside the 7.0 mm bore). Shear at 0.81 N with Wahl factor 1.07: τ = 1.07 × 8 × 0.81 × 6.5 / (π × 0.027) = **530 MPa** `[EST]`, under the ~0.45 × 2300 ≈ 1000 MPa torsional endurance of music wire; cyclic range at ±5 mm is ±65 MPa — infinite life.
  - **Stock route:** McMaster's compression-spring filter carries 0.24" OD music-wire springs to 2" long with rates down to ~0.1 lb/in (0.0175 N/mm) `[EST — the 0.24" OD / 0.25 lb/in / 1" combination is confirmed; confirm the 0.1 lb/in × 1.75" row on mcmaster.com before ordering]` ([McMaster compression springs](https://www.mcmaster.com/products/made-to-order-compression-springs/)). Lee Spring LC stock at 0.24" OD is short and stiff (LC 038C 05 M, 64 lb/in `[KNOWN]` [Lee](https://www.leespring.com/product/compression-spring-lc038c05m-music-wire)). RS PRO 0821251, 3.45 mm OD × 34 mm, 0.06 N/mm `[KNOWN]` ([RS](https://kr.rs-online.com/web/p/compression-springs/0821251)) serves the A/B set. Order 2×, sort by measured rate.
  - **Hand-wound route (reliable, 20 min for 15):** 0.30 mm K&S music wire wound on a 6.2 mm mandrel (6 mm drill shank + tape) in a hand drill, pitch set by a 2.7 mm feeler-gauge spacer, 17 turns, cut, grind ends flat on 400-grit. Spring-back takes the 6.2 mm mandrel to ~6.5 mm mean `[EST]`. Rate scatter ±15 % — sort.
  - **Preload and A/B:** 0.05 N at the extended stop (2.5 mm of compression). For the sensation A/B (does a stiffer spring "feel more like pulp"?), a second set at **0.06 N/mm** (0.40 mm wire, 5.5 mm mean, 25 coils, or the RS part) drops into the same bore; it swings ±0.3 N over ±5 mm — the test of judge F1 by direct comparison (T-P8).
- **Guide:** PTFE tube 2.0 mm OD × 1.0 mm ID, 25 mm long, pressed into a 1.95 mm printed bore through the nose, the pin running inside it. Radial play 0.1 mm over 25 mm → angular play 0.46°, tip wander 0.3 mm `[EST]`.
- **Guide friction** `[EST]`: drag F_t at the edge, arm 35 mm below the guide centre, guide 25 mm long → end reactions 1.4 F_t each; friction 2µR with µ(PTFE/steel) ≈ 0.1 → **0.25 F_t**: 0.025 N (±6 %) at 0.1 N steady drag, 0.08 N (18 %, transient) at a 0.3 N spike. A 10 mm guide would give 0.6 F_t — that is why it is 25 mm. Wiper friction adds in §4.6.
- **Housing:** PETG, 10 OD × 48 (31 above the plate + 2 plate + 15 nose), 7.0 bore for the spring, 1.95 bore for the PTFE tube through the lower 25 mm, extended stop = the cap on the top plug; printed nose-down, 1.2 mm walls. For SP1 print all 12 housings *as* the inner-shell plate. 2.5 g.

### 4.5 Cap, latch and what the selector touches

- **Cap:** printed PETG (or a 3 mm brass bead), 3.0 mm dia × 3 mm, bonded to the shaft top; a **0.5 mm × 0.8 mm shoulder** (groove) 1 mm below its crown; the crown is a 1.5 mm radius dome. The cap is the extended-stop (it bottoms on the housing top plug at z = 0) and the park handle.
- **Latch leaf:** 0.30 × 6 × 18 mm feeler-gauge stock (same stock as mechanical §8), clamped at one end on the housing top, free end with a 2.2 mm-wide notch that drops into the cap groove when the cap is pushed to z = 35. Leaf preload 0.3 N toward engagement (its own bend, 1 mm); engagement depth 0.8 mm.
- **Holding:** 0.75 N spring vs a square shear step in a PETG cap (≈ 60 N) and the leaf in its slot (≈ 10 N before it skips) `[EST]`. Proof: hang 750 g from a parked pin — no release, no set.
- **Release:** selector lifts the leaf end 1.2 mm (≈ 0.35 N); 0.75 N on 0.8 g gives a ≈ 0.9 km/s² start and the pin covers 15 mm in **~6 ms** `[EST]`, so release must happen *onto* the scalp (the brief's momentary retraction for lift-off), not into a head gap; landing energy < 1 mJ, well under safety §2.4's 2.4 mJ.
- **Re-park:** cam/ramp pushes the cap 35 mm at ≈ 1.0 N per pin (0.75 N spring + friction), 5 N for a group of five — SELECTOR's number; the latch clicks in on its own preload.
- **Stuck latch:** a pin that will not re-park stays out at ≤ 0.81 N (annoying, not dangerous); one that releases unbidden adds a 0.45 N contact, inside R3. The latch cannot exceed the spring's mechanical constant.

### 4.6 Exit seal (the hair question)

The pin is a 0.8 mm cylinder sliding 35 mm through the nose tip. The PTFE guide's 0.1 mm clearance is squarely in H-4.9's forbidden 40 µm–3 mm band, so the guide **must not be the exposed seam**. Three options ranked:

1. **Double silicone wiper lip (picked).** Two discs of 0.5 mm, Shore 40A silicone sheet (McMaster "silicone rubber sheets, 0.5 mm, 40A" `[KNOWN]` [McMaster silicone plates](https://www.mcmaster.com/products/silicone-rubber-plates/)), 6 mm dia, punched with a 0.6 mm hole (a sharpened 0.6 mm hypodermic/0.5 mm wire in a drill), stretched over the 0.8 mm pin: zero gap, each lip ~0.3 mm wide on the pin. Stacked 2 mm apart in the nose tip under a printed 15°-drafted retainer cone, the lower disc flush with the nose's R 1 mm lip. Friction per lip: estimated **0.01–0.03 N** (silicone on polished steel, lip contact pressure from 30 % stretch) `[EST, UNKNOWN — T-P2 measures it]`; two lips 0.02–0.06 N = 4–13 % hysteresis on 0.45 N. If T-P2 reads > 0.05 N, go to a single lip or Shore 30A. Hair that is dragged to the lip meets a soft 0.3 mm edge and is wiped off the pin on the retract stroke; a hair *under* the lip rides with the pin at well under the 0.15 N tug (H-4.11) because the lip pressure on a 70 µm hair is tiny `[EST]`. The lower lip is wiped with IPA at the tip change; the discs are a weekly consumable (safety §8).
2. **Rolling diaphragm sock** (2 mm-ID, 0.25 mm-wall silicone tube bonded at ferrule and nose, rolling inside out): near-zero friction and no sliding seal — the SP2 answer if wiper friction fails T-P2; needs 20 mm of sock inside the nose.
3. **Bellows boot** (TPU vase-mode): 35 mm stroke needs ~12 convolutions and 45 mm free length — the tallest part in the unit; rejected. An open > 3 mm clearance instead of a seal would leave the spring bore open to hair and sebum; rejected for V1.

**Nose geometry (what hair sees):** 15 mm below the shell plate, 10 mm dia at the plate tapering at 15° to 4 mm at the tip, tip edge R 1 mm, all surfaces 400-grit then buffed (Ra ≤ 0.8 µm, H-4.8), printed nose-down so layer lines run around the cone (perpendicular to hair sliding up it: not ideal — sand). Nose tip stands 10 mm clear of the nominal scalp (5 mm at +5 mm slop) so it never drags hair into the lip. Spacing between adjacent noses at the ARCHITECT's pitch: ≥ 8 mm centre-to-centre at the tips is H-4.6; with 4 mm nose tips, a 24 mm pin pitch leaves 20 mm — open.

### 4.7 Hair checklist (H-6.8), pin-unit items

Items 1, 2, 3, 6, 8, 9, 10, 12, 16, 17 score 2; item 7 (0.15 N yield) scores 1 (tip compliance 0.12 N/mm, neck fuse at 0.75 N); item 11 (tether-free breakaway) scores 1 (the pin retracts in 6 ms instead of detaching; the nail bond is proof-loaded at 1.5 N). **Subtotal 22/24.**

---

## 5. Drawings (dimensions in mm; section through the pin axis, stroke direction = page X)

### 5.1 Pin unit, EXTENDED at nominal seating (z = 20) and PARKED (z = 35)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="640" height="360" font-family="monospace" font-size="10">
  <!-- scale 2 px per mm -->
  <!-- LEFT: extended -->
  <g transform="translate(60,20)">
    <text x="0" y="-6" font-weight="bold">EXTENDED, z=20 (nominal seating)</text>
    <!-- shell plate -->
    <rect x="-40" y="96" width="140" height="4" fill="#bbb" stroke="#000"/>
    <text x="-40" y="94">inner shell plate t2</text>
    <!-- housing above plate: 10 OD x 31 -->
    <rect x="20" y="34" width="20" height="62" fill="none" stroke="#000"/>
    <!-- bore 7 -->
    <rect x="23" y="36" width="14" height="60" fill="#fff" stroke="#000" stroke-dasharray="2,2"/>
    <!-- spring (coil) z=20 => compressed 20 : coil region from cap bottom to shoulder -->
    <path d="M24,80 l12,4 l-12,4 l12,4 l-12,4" fill="none" stroke="#06c" stroke-width="1.5"/>
    <path d="M24,44 l12,4 l-12,4 l12,4 l-12,4 l12,4 l-12,4 l12,4 l-12,4 l12,4" fill="none" stroke="#06c" stroke-width="1.5"/>
    <!-- cap at z=20: cap top at housing top + 20*2=40 px below -->
    <rect x="27" y="36" width="6" height="6" fill="#999" stroke="#000"/>
    <!-- actually cap sits inside bore at depth; draw plug -->
    <rect x="20" y="30" width="20" height="4" fill="#ddd" stroke="#000"/>
    <text x="44" y="34">top plug / latch leaf seat</text>
    <!-- nose below plate: 15 mm, 10->4 taper -->
    <polygon points="20,100 40,100 34,130 26,130" fill="none" stroke="#000"/>
    <!-- PTFE guide 25 mm: from plate-10 to nose tip -->
    <rect x="29" y="80" width="2" height="50" fill="#9c9" stroke="none"/>
    <text x="44" y="112">PTFE 2.0x1.0 guide, 25 long</text>
    <!-- wiper lips -->
    <rect x="27" y="126" width="6" height="1" fill="#f60"/>
    <rect x="27" y="122" width="6" height="1" fill="#f60"/>
    <text x="44" y="128">2x silicone wiper 0.5 thick</text>
    <!-- pin shaft 0.8 : from cap to ferrule, free 20 below nose -->
    <line x1="30" y1="42" x2="30" y2="170" stroke="#000" stroke-width="1.6"/>
    <!-- ferrule -->
    <rect x="28.4" y="170" width="3.2" height="8" fill="#da5" stroke="#000"/>
    <text x="44" y="178">ferrule 1/16" brass x4, CA fillet</text>
    <!-- neck 12 mm with PTFE sleeve, bent 45 at 2 above nail -->
    <line x1="30" y1="178" x2="30" y2="198" stroke="#000" stroke-width="2.4" opacity="0.4"/>
    <line x1="30" y1="178" x2="30" y2="198" stroke="#000" stroke-width="0.8"/>
    <line x1="30" y1="198" x2="36" y2="204" stroke="#000" stroke-width="0.8"/>
    <text x="44" y="196">neck 0.38 wire in PTFE 1.0x2.0 sleeve, 12 long</text>
    <!-- nail at 45 deg, 8 long -->
    <line x1="32" y1="200" x2="44" y2="212" stroke="#c00" stroke-width="2"/>
    <text x="44" y="216">nail 6 wide x 0.7, 45°, edge R0.4</text>
    <!-- scalp -->
    <path d="M-40,214 q70,-6 140,0" fill="none" stroke="#a63" stroke-width="2"/>
    <text x="-40" y="228">scalp (R 90)</text>
    <!-- dims -->
    <line x1="-20" y1="100" x2="-20" y2="214" stroke="#333" marker-end="url(#a)"/>
    <text x="-34" y="160" transform="rotate(-90 -34,160)">≈ 25 shell-to-scalp (ARCHITECT)</text>
    <line x1="60" y1="34" x2="60" y2="96" stroke="#333"/>
    <text x="62" y="68">31</text>
    <line x1="60" y1="100" x2="60" y2="130" stroke="#333"/>
    <text x="62" y="118">15 nose</text>
    <line x1="60" y1="130" x2="60" y2="212" stroke="#333"/>
    <text x="62" y="150">40 at z=0</text>
    <text x="62" y="162">(≥25 nominal, H-4.5)</text>
  </g>
  <!-- RIGHT: parked -->
  <g transform="translate(400,20)">
    <text x="0" y="-6" font-weight="bold">PARKED, z=35 (latched)</text>
    <rect x="-40" y="96" width="140" height="4" fill="#bbb" stroke="#000"/>
    <rect x="20" y="34" width="20" height="62" fill="none" stroke="#000"/>
    <rect x="23" y="36" width="14" height="60" fill="#fff" stroke="#000" stroke-dasharray="2,2"/>
    <rect x="20" y="30" width="20" height="4" fill="#ddd" stroke="#000"/>
    <!-- latch leaf engaged: from housing top across -->
    <line x1="2" y1="31" x2="30" y2="31" stroke="#06c" stroke-width="1.5"/>
    <text x="-38" y="28">latch leaf 0.3x6x18</text>
    <!-- cap now 35 mm deeper = 70 px? too deep for drawing scale: show cap at z=35 => y = 36+... cap top at 36+70-... keep schematic -->
    <rect x="27" y="40" width="6" height="6" fill="#999" stroke="#000"/>
    <text x="44" y="46">cap 3Ø, groove 0.5x0.8 (schematic)</text>
    <!-- spring compressed more -->
    <path d="M24,48 l12,3 l-12,3 l12,3 l-12,3 l12,3 l-12,3 l12,3 l-12,3 l12,3 l-12,3 l12,3 l-12,3" fill="none" stroke="#06c" stroke-width="1.5"/>
    <polygon points="20,100 40,100 34,130 26,130" fill="none" stroke="#000"/>
    <rect x="29" y="80" width="2" height="50" fill="#9c9"/>
    <rect x="27" y="126" width="6" height="1" fill="#f60"/>
    <rect x="27" y="122" width="6" height="1" fill="#f60"/>
    <!-- pin retracted: nail 15 above scalp -->
    <line x1="30" y1="46" x2="30" y2="140" stroke="#000" stroke-width="1.6"/>
    <rect x="28.4" y="140" width="3.2" height="8" fill="#da5" stroke="#000"/>
    <line x1="30" y1="148" x2="30" y2="168" stroke="#000" stroke-width="2.4" opacity="0.4"/>
    <line x1="30" y1="148" x2="30" y2="168" stroke="#000" stroke-width="0.8"/>
    <line x1="30" y1="168" x2="36" y2="174" stroke="#000" stroke-width="0.8"/>
    <line x1="32" y1="170" x2="44" y2="182" stroke="#c00" stroke-width="2"/>
    <path d="M-40,214 q70,-6 140,0" fill="none" stroke="#a63" stroke-width="2"/>
    <line x1="60" y1="182" x2="60" y2="212" stroke="#333"/>
    <text x="62" y="200">15 clear (10 at +5 slop)</text>
    <text x="-40" y="240">spring 0.75 N on the latch; F_max 0.81 N at housing floor</text>
    <text x="-40" y="252">stroke z: 0 extended stop · 20 nominal · 35 parked · 38 floor</text>
  </g>
  <text x="60" y="300">Housing 10 OD x 48 total (31 above plate + 2 plate + 15 nose). Spring 0.30 wire, 6.5 mean, 15 active, free 45, k 0.020 N/mm.</text>
  <text x="60" y="314">Pin shaft 0.80 music wire x 60. Neck 0.38 x 12 (+4 hook, +4 in ferrule). Nail 6 x 8 x 0.7 at 45°. Moving mass 0.8 g.</text>
  <text x="60" y="328">Scale: 2 px = 1 mm in the vertical stack; cap/latch shown schematically.</text>
</svg>

### 5.2 Exit seal detail (nose tip, 10× scale)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 260" width="520" height="260" font-family="monospace" font-size="10">
  <!-- 10 px per mm; pin axis at x=200 -->
  <text x="10" y="16" font-weight="bold">NOSE TIP SECTION, 10 px = 1 mm</text>
  <!-- nose cone walls: tip 4 wide at y=200, widening up at 15deg -->
  <polygon points="180,200 220,200 236,140 164,140" fill="#eee" stroke="#000"/>
  <!-- PTFE guide tube: 2.0 OD, 1.0 ID -->
  <rect x="190" y="60" width="20" height="120" fill="#cfc" stroke="#060"/>
  <rect x="195" y="60" width="10" height="120" fill="#fff" stroke="none"/>
  <text x="250" y="80">PTFE 2.0 OD x 1.0 ID (guide), ends 20 above lip</text>
  <!-- pin 0.8 -->
  <rect x="196" y="40" width="8" height="200" fill="#444"/>
  <text x="250" y="100">pin 0.80 music wire, 2000-grit</text>
  <!-- wiper discs 0.5 thick, 6 dia, hole 0.6 -> stretched -->
  <rect x="170" y="180" width="26" height="5" fill="#f90" stroke="#a50"/>
  <rect x="204" y="180" width="26" height="5" fill="#f90" stroke="#a50"/>
  <rect x="170" y="194" width="26" height="5" fill="#f90" stroke="#a50"/>
  <rect x="204" y="194" width="26" height="5" fill="#f90" stroke="#a50"/>
  <text x="250" y="186">wiper 1: silicone 0.5 t, 40A, 6 Ø, hole 0.6</text>
  <text x="250" y="200">wiper 2: same, 1.4 below; lower face flush</text>
  <!-- retainer cone ring -->
  <rect x="170" y="186" width="26" height="8" fill="#ddd" stroke="#000"/>
  <rect x="204" y="186" width="26" height="8" fill="#ddd" stroke="#000"/>
  <text x="250" y="214">printed spacer ring 0.8 t; retainer = nose tip lip</text>
  <!-- lip radius -->
  <path d="M180,200 q0,-10 10,-10" fill="none" stroke="#c00"/>
  <path d="M220,200 q0,-10 -10,-10" fill="none" stroke="#c00"/>
  <text x="20" y="206">R 1.0 lip</text>
  <!-- draft -->
  <text x="20" y="150">15° draft</text>
  <!-- dims -->
  <line x1="180" y1="222" x2="220" y2="222" stroke="#333"/>
  <text x="186" y="236">4.0 tip Ø</text>
  <line x1="164" y1="130" x2="236" y2="130" stroke="#333"/>
  <text x="170" y="126">7.2 at 15 above tip</text>
  <text x="20" y="250">Gap audit: pin–PTFE 0.1 (behind the wipers, closed); pin–wiper 0 (interference); wiper–nose 0 (clamped). No 0.04–3 mm gap exposed.</text>
</svg>

---

## 6. Mass, cost and BOM

**Per pin unit (V1):** shaft 0.19 g, neck + sleeve 0.05, ferrule 0.03, nail 0.10, cap 0.05 → **moving mass 0.42 g** (0.8 g with the spring's effective third); spring 0.32 g, PTFE guide 0.10, wipers + ring 0.06, latch leaf 0.25, housing 2.5 (as part of the shell plate: ~1.8 extra per pin) → **3.6 g per pin installed** `[EST]`. 12 pins (SP1 sector): **43 g**; 36 pins (full helmet): **130 g**.

| Item | Spec / source | Qty for 12 | Cost 12 | Qty for 36 | Cost 36 |
|---|---|---|---|---|---|
| Pin shaft | K&S music wire 0.031" (0.80 mm) × 36" `[KNOWN]` | 1 stick (15 pins) | $4 | 3 sticks | $10 |
| Neck wire | K&S music wire 0.015" (0.38 mm) × 36" | 1 stick | $3 | 1 stick | $3 |
| Ferrule | K&S 1/16" brass tube × 12" | 1 | $3 | 1 | $3 |
| Spring | hand-wound from K&S 0.012"/0.30 mm music wire (1 stick) **or** McMaster 0.24" OD music-wire spring, ≤ 0.1 lb/in, 1.75" `[EST part]` | 1 stick / 24 springs | $3 / $20 | 1 stick / 72 | $3 / $55 |
| A/B spring 0.06 N/mm | RS PRO 0821251 (3.45 OD × 34, 0.06 N/mm) or wound 0.40 mm wire | 12 | $12 | — | — |
| PTFE guide | PTFE tube 1.0 × 2.0 mm, 1 m | 1 | $8 | 1 | $8 |
| Neck sleeve | same tube | — | — | — | — |
| Wipers | silicone sheet 0.5 mm 40A, 150 × 150 mm | 1 | $8 | 1 | $8 |
| Nail | press-on nail kit (24–30 nails, ABS) | 1 kit | $6 | 2 kits | $12 |
| Latch leaf | feeler stock 0.012" × 1/2" × 12" (or 0.30 × 12.7 strip, slit to 6) | 1 | $4 | 2 | $8 |
| Housing / nose / cap / ring | PETG, ~45 g for 12 units in the shell plate print | — | $2 | — | $6 |
| Adhesives | gel CA + UV resin (shared) | — | $6 | — | $6 |
| Solder, acid flux | shared | — | $4 | — | $4 |
| **Total** | | | **$63 (≈ $5.30/pin)** | | **$71–126 (≈ $2.00–3.50/pin)** |

Nitinol shaft option: +$35 per 5 ft (18 pins). Costs are 2026 US hobby-retail `[EST ±30 %]`.

---

## 7. Making 12 identical pins in an apartment: the jig

One printed PETG fixture plate, 120 × 60 × 10 mm, seven stations; ≈ **3 h hands-on for 12 pins** after a 2 h print.

1. **Cut:** 0.9 mm groove with a 60.0 mm stop (shaft) and a 20.0 mm stop (neck); flush-cut at the stop, deburr.
2. **Neck bend:** 2.0 mm pin + 45° fence, wire inserted to its 2 mm stop, one fold; 1.5 mm pin for the 4 mm nail hook.
3. **Ferrule/solder:** V-groove holding shaft and neck coaxial with a 4 mm window; flux, ferrule, 25 W iron from below; CA/resin fillet spun to a draft. Roll on glass: wobble > 0.2 mm = reject.
4. **Nail:** 45° cradle with a 6 mm slot locating the nail strip edge-out and a 0.9 mm groove setting the 1.5 mm free edge; hook in a knife-scored groove, gel CA, resin fillet; then edge finishing (§4.2) with the pin in a clothes-peg.
5. **Spring winding** (if hand-wound): 6 mm drill shank + one turn of tape in a clamped hand drill, 2.7 mm spacer, 17 turns, grind ends; sort to 0.018–0.022 N/mm.
6. **Rate/force fixture:** step block (10/15/20/25/30/35 mm) over the kitchen scale (1 g = 0.01 N); each unit gets a card with k, F(20) and friction.
7. **Wiper punch:** 6 mm leather punch for the disc, sharpened 0.6 mm wire in a pin vise for the hole.

Tools: flush cutters, needle files, 400/1000/2000 wet paper, 25 W iron, hand drill, 10× loupe, kitchen scale, callipers.

---

## 8. Interface requests to the other teams (designed-to values)

- **ARCHITECT:** shell underside ≥ 20 mm above nominal scalp (I used 25); pitch ≥ 20 mm; print the housings as the shell plate. **Height:** 34 mm above the plate (31 + cap/latch 3) → 61 mm to the scalp before selector and outer shell, over the 60 mm target. Levers: park margin 15 → 10 mm (−5), preload 0.15 N with nominal at z = 15 (−5, same swing), 0.25 mm spring wire (−2): **24 mm at best** `[EST]`; beyond that, V2 (10 mm, couples to pin layout).
- **SELECTOR:** release = lift the latch leaf end 1.2 mm with 0.35 N; park = push the cap crown (R 1.5 dome on the pin axis) 35 mm with ≤ 1.0 N, 5 N for a group of five. Released pins reach the scalp in ~6 ms — release only over the head.
- **DRIVE:** moving mass added per released pin 0.8 g; tangential stiffness at the tip 0.12 N/mm (the nail lags the shell by 0.4–0.8 mm at 0.05–0.1 N drag — invisible); lift-off by momentary retraction is available at 6 ms extend / ≈ 40 ms selector-park.

---

## 9. Bench tests (all before any human contact; kitchen scale, ruler, wig head)

| ID | Test | Method | Pass |
|---|---|---|---|
| T-P1 | Force vs extension | housing on the step block (§7.6), tip on the kitchen scale, read at z = 10/15/20/25/30/35, up and down | 0.30–0.50 N at z = 15–25; k 0.018–0.022; hysteresis ≤ 0.04 N |
| T-P2 | Friction under drag | repeat T-P1 with a 10 g (0.1 N) and 30 g (0.3 N) side pull on the nail via thread over a pulley | hysteresis ≤ 0.06 N at 0.1 N, ≤ 0.12 N at 0.3 N; wiper-only friction (pin without spring) ≤ 0.05 N |
| T-P3 | Alignment on a 90 mm sphere | 3 units in a printed test bar at 0°, +10°, −10° to the local normal; sphere coated with whiteboard marker; press to 0.3 N and 0.5 N; measure the wiped line | line ≥ 3 mm long at every angle, no single-corner dot; neck pitch under 0.1 N drag ≤ 6° |
| T-P4 | Latch | parked pin, hang 750 g axially; then release with a 0.35 N push on the leaf | holds; releases; 50 park/release cycles with no wear step |
| T-P5 | Buckling / proof | extended pin, 1.0 N axial on the nail (100 g), then 150 g on the nail bond | no collapse, no set, no bond crack |
| T-P6 | Wig head (hair-interaction §7) | 3-pin test bar hand-stroked 200 strokes at 0.4 N through a human-hair wig, both grains, with 10 park/release cycles in the hair | 0 catches at the wiper, ≤ 2 shed hairs on the noses, no hair under a lip after retract |
| T-P7 | Fatigue | one unit cycled 10,000 times at 2 Hz on a drill-driven cam (±5 mm about z = 20 with 0.1 N side load by rubber band) | k within 5 %; neck straight; wiper intact |
| T-P8 | Spring A/B (sensation) | 0.02 vs 0.06 N/mm sets on the hand wand (tips.md §7) before the helmet exists | which feels more like a nail at 0.4 N — informs SP1 default `[UNKNOWN]` |
| T-P9 | Thermal | 20 min bench run, IR/contact thermometer on the nose | ≤ 41 °C (trivially) |

---

## 10. Risks, honestly

| Risk | Likelihood | Consequence | Mitigation |
|---|---|---|---|
| Neck + bonded PTFE sleeve is 2–3× stiffer than the wire-only calc → no self-alignment, corner contact | Medium `[UNKNOWN]` | pricking on curvature mismatch | T-P3 first; shorten/slit the sleeve; 0.012" neck wire as backup |
| Wiper friction > 0.05 N | Medium | hysteresis eats the ±22 % budget | single lip, 30A sheet, or the rolling sock (§4.6 option 2) |
| Height 34 mm above the plate refused | Medium | redesign to V2 (coupled to pin layout) | §8 levers get to 24 mm |
| Bent shaft from a flinch or doffing | Medium over months | pin drags in the guide, force error | roll-on-glass check at each session; nitinol shaft upgrade |
| Nail bond lets go in hair | Low | loose 6 mm red plate in hair | proof-load every tip; bright colour; count tips pre/post session |
| Soft 0.02 N/mm spring feels "dead" compared with pulp | Unknown | sensation miss | T-P8 A/B is cheap and early |

**What this unit cannot do:** meet the 0.15 N tangential yield (nobody can while carrying 0.3 N of scratch drag, judge F4); detach as a tether-free breakaway (it retracts instead, which is the hair-interaction §5.9 reflex); be shorter than ~24 mm above the shell plate while keeping ±25 % over ±5 mm with a linear spring.
