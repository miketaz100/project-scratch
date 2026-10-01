# SP1 Scratching Tip Interface — Tribology & Contact Specification

**Project SCRATCH · 01-foundations · Author: scratching-interface / tribology specialist · 2026-10-01**

**Scope.** The tip (artificial fingernail) is treated as its own subsystem, independent of whatever mechanism moves it. This document defines (1) the human reference, (2) the contact mechanics that set the "scratch window", (3) why existing massager tips fail, (4) the SP1 tip family, (5) the universal tip-mount standard (**SP1-TM1**) that every mechanism team must adopt, (6) multi-contact array rules, (7) materials, (8) edge finishing and wear, and (9) the test plan.

**Confidence tags used throughout:** `[KNOWN]` = literature value with citation; `[EST]` = engineering estimate derived here, mark for verification; `[UNKNOWN]` = must be found by test.

---

## 1. The human fingernail as the reference scratching tool

### 1.1 Geometry

| Parameter | Value | Tag / source |
|---|---|---|
| Nail plate thickness (fingers) | 0.25–0.60 mm, typical means 0.35–0.50 mm | `[KNOWN]` ([Tohmyoh 2023, Skin Res Technol](https://onlinelibrary.wiley.com/doi/full/10.1111/srt.13456); [nail wiki summary](https://thenailwiki.com/nail-plate/)) |
| Nail plate width (index–ring) | ~10–14 mm; width/length ratio ≈ 0.93–0.95 for fingers 2–4 in men, ~0.91 in women | `[KNOWN]` ([Fingernail Configuration, PMC4659990](https://pmc.ncbi.nlm.nih.gov/articles/PMC4659990/)) |
| Free-edge length (the part that scratches) | 1–3 mm for a "normal" short nail; up to 5 mm for grown nails | `[EST]` (grooming convention; the plate itself is ~12–15 mm long) |
| Transverse (across-finger) curvature radius | thumb 11.4 ± 1.3, index 8.9 ± 1.2, middle 8.8 ± 1.2, ring 7.3 ± 1.0, little 5.8 ± 0.9 mm (men); overall adult range ~5–13 mm | `[KNOWN]` ([Murdan 2011, Int J Cosmet Sci](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-2494.2011.00663.x)) |
| Free-edge radius after filing | ≈ half the plate thickness, i.e. **0.15–0.3 mm**, rising to ~0.4 mm on a well-worn nail; a freshly clipped, unfiled nail has a squarer edge (effective radius ~0.1 mm with two corners) | `[EST]` (edge cannot be sharper than the plate allows; filing rounds it) |
| Plan-form of free edge | gently convex ("squoval"), corners rounded ~1–2 mm | `[EST]` |

### 1.2 Mechanical properties

- Nail keratin Young's modulus by nanoindentation: top/middle/under plates **2.9 / 3.1 / 2.8 GPa**, whole-plate structural elasticity ≈ 2.9 GPa; older nanoindentation gave ~4.6 GPa `[KNOWN]` ([Tohmyoh 2023](https://pubmed.ncbi.nlm.nih.gov/37881063/); [Farren et al. humidity study](https://www.researchgate.net/publication/231922863_Microindentation_and_nanoindentation_of_human_fingernails_at_varying_relative_humidity)). Softening (urea, water) drops this to 60–70% `[KNOWN]`.
- Implication: a 0.45 mm thick, 12 mm wide nail with a 3 mm free edge is a cantilever of stiffness ≈ **30 N/mm** `[EST, computed]` — effectively rigid at scratching loads (≤1.5 N → <0.05 mm deflection). **The nail edge does not flex; the compliance comes from behind it.**

### 1.3 Pulp compliance — the hidden spring

The fingertip pulp is a nonlinear viscoelastic cushion: it is "relatively compliant at forces less than 1 N, but stiffened rapidly" beyond, with ~82% of the displacement at 5.2 N already occurring below 1 N; 2 N can displace pulp tissue >3 mm `[KNOWN]` ([Serina et al., J Biomech](https://www.sciencedirect.com/science/article/abs/pii/S0021929097000651); [Pawluk & Howe tapping model](https://www.researchgate.net/publication/10888864_Non-linear_viscoelastic_models_predict_fingertip_pulp_force-displacement_characteristics_during_voluntary_tapping)). So the effective spring behind a scratching nail is **~0.3–0.5 N/mm for the first ~2–3 mm, then hardening** `[EST]`. When a scratching finger meets a bump of scalp, force rises gently rather than spiking. This is the force-limiting behaviour SP1 must copy, and it is the single most important thing the mount (not the tip) has to provide.

### 1.4 How a person actually scratches a scalp

`[EST]` from observation and the kinematics of a curled finger: fingers curl so the nail plate meets the skin at **30–60° to the local surface**, the free edge leads (drag direction is toward the palm), and the finger pad is often in light contact just behind the nail, so the pulp both springs the nail and modulates the load. Stroke lengths 20–60 mm, speeds ~30–150 mm/s, 1–3 Hz reciprocation, forces 0.1–1.5 N per finger `[EST; the scratch-model agent owns these numbers]`.

### 1.5 What the skin "feels"

Putting 1.1–1.4 together, the stimulus is: **a narrow line contact (edge radius ~0.1–0.5 mm, contact length a few mm across the curved scalp), of high local stiffness (keratin ≫ skin), backed by a soft spring (~0.4 N/mm), dragged at modest force (0.1–1.5 N) with moderate, slightly stick-slip friction, under a wedge angle of 30–60°.** Everything in this document exists to reproduce that stimulus and nothing else.

```
          finger pad (pulp = soft spring, ~0.4 N/mm)
         ,-----.
        /       \     nail plate, E ≈ 3 GPa, t ≈ 0.45 mm
       |   ___   \_______________
        \_/   \__________________`\   <- free edge, r ≈ 0.2–0.3 mm
                 drag ->          /  \
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/    \~~~~~~~~~~   scalp (E ≈ 20–50 kPa)
   hair  |  |  | |  |  |   ,  |  |   |  |  |  |
                    attack angle 30–60°
```

---

## 2. Contact mechanics: deriving the scratch window

### 2.1 Model and inputs

Scalp skin under shallow indentation: in-vivo skin indentation gives whole-skin moduli of ~4–45 kPa by region and ~7–11 kPa complex modulus at 10 Hz; the epidermis alone is 140–600 kPa and dermis 2–80 kPa `[KNOWN]` ([Pailler-Mattei 2008 in-vivo indentation](https://www.sciencedirect.com/science/article/abs/pii/S135045330700135X); [Boyer dynamic indentation](https://pubmed.ncbi.nlm.nih.gov/19152580/); [skin mechanics review](https://www.researchgate.net/publication/307522356_Mechanical_Behaviour_of_Skin_A_Review)). The scalp sits on galea and bone, which stiffens deeper indentation. I use **E = 30 kPa, ν = 0.5 → E\* = 40 kPa** as the shallow-indentation effective modulus `[EST]`.

A nail edge is a **cylinder (line contact)** of radius R and effective contact length L. On a curved scalp a 12 mm curved edge touches over only part of its width; I take **L = 6 mm** `[EST]`. Hertz line contact: half-width b = √(4FR/(πLE\*)), peak pressure p₀ = 2F/(πbL), indentation depth ≈ b²/R.

### 2.2 Results (computed; E\* = 40 kPa, L = 6 mm) — cells: p₀ kPa / half-width b mm / depth mm

| Edge R (mm) | 0.1 N | 0.3 N | 0.5 N | 1.0 N | 1.5 N |
|---|---|---|---|---|---|
| 0.10 | 46 / 0.23 / 0.5 | 80 / 0.40 / 1.6 | 103 / 0.52 / 2.7 | 146 / 0.73 / 5.3 | 178 / 0.89 / 8.0 |
| 0.25 | 29 / 0.36 / 0.5 | 50 / 0.63 / 1.6 | 65 / 0.81 / 2.7 | 92 / 1.15 / 5.3 | 113 / 1.41 / 8.0 |
| 0.50 | 21 / 0.52 / 0.5 | 36 / 0.89 / 1.6 | 46 / 1.15 / 2.7 | 65 / 1.63 / 5.3 | 80 / 1.99 / 8.0 |
| 1.00 | 15 / 0.73 / 0.5 | 25 / 1.26 / 1.6 | 33 / 1.63 / 2.7 | 46 / 2.30 / 5.3 | 56 / 2.82 / 8.0 |
| 2.00 | 10 / 1.03 / 0.5 | 18 / 1.78 / 1.6 | 23 / 2.30 / 2.7 | 33 / 3.26 / 5.3 | 40 / 3.99 / 8.0 |

Sphere (ball) contact for comparison — p₀ kPa / contact radius a mm / depth mm:

| Ball R (mm) | 0.1 N | 0.3 N | 0.5 N | 1.0 N | 1.5 N |
|---|---|---|---|---|---|
| 1.5 (3 mm ball, control tip H) | 24 / 1.4 / 1.3 | 35 / 2.0 / 2.8 | 41 / 2.4 / 3.9 | 52 / 3.0 / 6.2 | 59 / 3.5 / 8.1 |
| 5.0 (10 mm massager ball) | 11 / 2.1 / 0.9 | 15 / 3.0 / 1.9 | 18 / 3.6 / 2.6 | 23 / 4.5 / 4.1 | 26 / 5.2 / 5.4 |
| 10.0 (20 mm bulb) | 7 / 2.7 / 0.7 | 10 / 3.8 / 1.5 | 12 / 4.5 / 2.1 | 15 / 5.7 / 3.3 | 17 / 6.6 / 4.3 |

### 2.3 The critical observation: Hertz breaks down exactly where scratching lives

Look at the depth column: for every edge radius ≤ 0.5 mm, **indentation depth exceeds the edge radius once force passes ~0.1–0.3 N.** The skin wraps around the edge; the contact is no longer "a cylinder on a half-space" but "a wedge ploughing a soft solid." Consequences:

1. The nominal p₀ values above are **lower bounds** and saturate; what the mechanoreceptors register is the **strain gradient at the edge** (set by R relative to the ~10–20 µm stratum corneum and ~100 µm epidermis `[EST]`) and the **line load F/L** (0.02–0.25 N/mm across the force range).
2. Below the wrap-around threshold the stimulus is a diffuse pressure (= stroke); above it, the skin is locally folded ahead of the edge and released behind it as the edge moves (= scratch). **The scratch sensation is the skin being ploughed and released, not pressed.** This is why radius matters far more than force.
3. The wedge angle (attack angle 30–60°) now governs the "bite": at 30° the edge glides and plates hair; at 60–90° it digs and catches. 45° is the design centre `[EST]`.

### 2.4 Pain, sharpness and abrasion ceilings

- Blunt pressure pain (1 cm² algometer): scalp/cranial PPTs are a few hundred kPa, with 800 kPa used as a safety ceiling `[KNOWN]` ([PPT review](https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S0188-95322021000200203); [headache algometry](https://thejournalofheadacheandpain.biomedcentral.com/articles/10.1186/s10194-021-01278-8)). Even the sharpest cell in the table (178 kPa) is below this — **blunt pressure pain is not the limit for a nail-like tip.**
- Sharpness is the limit. Greenspan & McGillis showed perception moves from dull pressure → sharp pressure → sharp pain as force rises, and that **force/area is not a sufficient predictor — probe size and shape matter independently** `[KNOWN]` ([Greenspan & McGillis 1991](https://pure.johnshopkins.edu/en/publications/stimulus-features-relevant-to-the-perception-of-sharpness-and-mec-6/)). Standard pinprick stimulators use a 0.25 mm diameter (≈0.12 mm radius) flat tip at 8–512 mN; "sharp" is perceived at tens of mN and pain typically around 128–512 mN on hairy skin `[KNOWN]` ([pinprick stimulator description](https://journals.physiology.org/doi/full/10.1152/jn.00774.2012); [mechanical pain thresholds](https://journals.lww.com/painrpts/fulltext/10.1097/pr9.0000000000000865~mechanical-detection-and-pain-thresholds-comparability-of)).
- Translating a point to a line `[EST]`: a 0.12 mm-radius edge must stay below ~0.1–0.2 N per mm of *actually loaded* edge to stay in "sharp pressure" rather than "sharp pain". If only a 1–2 mm corner of a square-cut blade touches (common on a curved scalp with a flat edge!), 0.3 N already concentrates to 0.15–0.3 N/mm → pricking. **This is why the tip plan-form must be curved and the corners rounded: it guarantees contact length.**
- Abrasion: repetitive sliding at high shear strips stratum corneum; blister/abrasion risk rises with friction force × cycles and with dry skin. On a sebum-rich scalp with hair, abrasion from a 0.3–0.5 mm radius polymer edge at ≤1 N is low over a 20-minute session `[EST]`; the real abrasion risks are (a) a chipped edge, (b) a burr, (c) a square corner, (d) dwell-in-place reciprocation on one spot. Mitigate by geometry and by moving the stroke, not by weakening force.

### 2.5 The scratch window (design output)

```
 line load F/L  (N per mm of loaded edge)
   0.30 |  PRICK / PAIN  . . . . . . . . . . . . . .
   0.25 |  xx xx . . . . . . . . . . . . . . . . . .
   0.20 |  xx xx xx  . . . . . . . . . . . . . . . .
   0.15 |  xx ## ## ## . . . . . . . . . . . . . . .
   0.10 |  xx ## ## ## ## ## . . . . . . . . . . . .
   0.05 |  ~~ ## ## ## ## ## ~~ ~~ . . . . . . . . .
   0.02 |  ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ . . . . . .
        +----------------------------------------------
          0.1  0.2  0.3  0.4  0.5  0.7  1.0  1.5  2.0  edge radius (mm)
   ## = crisp scratch     ~~ = stroke / glide     xx = sharp, pricking
   . = pressure/massage (skin not folded; feels like a ball)
```

`[EST]` Scratch window: **edge radius 0.2–0.6 mm, line load 0.05–0.15 N/mm**, i.e. for a 6 mm loaded edge **0.3–0.9 N normal force**, attack angle 40–50°, backed by a ~0.4 N/mm spring. Tip A (0.3 mm) sits in the middle; B (0.6 mm) at the gentle edge; the 3 mm ball (H) sits entirely in the "." region at any force — which is exactly what makes it a good control.

### 2.6 Friction: grabby vs slippery

- Dry skin against smooth solids: µ ≈ 0.2–0.5 (typically ~0.5), roughly pressure-independent; moist/wet skin: µ > 1 and strongly pressure-dependent `[KNOWN]` ([Derler & Gerhardt 2012 review](https://link.springer.com/article/10.1007/s11249-011-9854-y); [Derler 2015 hydration](https://journals.sagepub.com/doi/10.1177/1350650114527922)).
- **Sebum raises friction**: removing surface sebum dropped measured µ from ~0.9 to ~0.3 `[KNOWN]` ([Imperial bench study on sebum](https://spiral.imperial.ac.uk/server/api/core/bitstreams/540021e7-14c6-4cfb-b0cf-0fe86e9ecfda/content)). The scalp is the most sebum-rich skin on the body, so expect the high end: **µ ≈ 0.6–1.0 for keratin or rough-ish polymer on bare scalp, lower (0.3–0.5) where hair interposes** `[EST]`.
- Bulk polymer µ (against steel, as a ranking proxy): POM ≈ 0.20, PETG ≈ 0.22–0.35, nylon 6/6 ≈ 0.10–0.26 `[KNOWN]` ([filament property table](https://github.com/superjamie/lazyweb/wiki/3D-Printing-Filament-Properties); [nylon vs PETG](https://siraya.tech/blogs/news/nylon-vs-petg-material-comparison)). Against skin all polymers land in a similar 0.3–0.6 band; **surface finish and hydrophilicity dominate**. Keratin is hydrophilic and micro-ridged, so a real nail is slightly "grabbier" than a polished POM edge of the same radius `[EST]`.
- Why grabby = scratch: with µ ≈ 0.7 and a 45° wedge, the edge builds a small fold of skin ahead of it, the fold stores elastic energy and releases in micro stick-slip events at ~10–100 Hz `[EST]` — exactly the band Pacinian and Meissner-type afferents are most sensitive to. A slippery edge (µ ≈ 0.2) slides without folding: the same radius then reads as a stroke. **So friction is the second control knob after radius, and tip F (POM, polished) vs tip A (PETG, 600-grit matte) is a deliberate friction A/B at constant geometry.**

---

## 3. Why existing scalp-massager tips are not scratchers

| Device tip | Contact-mechanics diagnosis |
|---|---|
| Balls, bulbs, 8–20 mm silicone nubs | R = 4–10 mm → contact radius 3–6 mm, depth < R at all forces: the skin is never folded, only pressed. Peak pressure 10–25 kPa spread over 30–100 mm². Reads as pressure/massage ("." region) regardless of force. Also too large to pass between hairs — they ride on the hair mat. |
| "Wire spider" head massagers | Point contact (R ≈ 1 mm bead) on 0.8 mm wire of ~0.05 N/mm stiffness: the spring is so soft that line load never reaches the scratch band; the tingle is from many points simultaneously brushing hair follicles (a different, diffuse stimulus). Good hair penetration, zero bite. |
| Brushes (silicone or nylon bristle) | Hundreds of ~0.2–0.5 mm radius tips each at a few mN: individually each is in the "~~" region. Spatial summation produces "brushing", not a localized scratch; there is no single moving line the brain can track. |
| Vibrating pads | Normal-direction oscillation, no tangential ploughing: the folded-skin release event never happens. |

The common failure is **no narrow, stiff, single moving line contact with ~0.4 N/mm backing.** All four miss on at least one of {radius, stiffness, tangential drag, singularity of contact}.

---

## 4. SP1 tip family

All tips share the SP1-TM1 tang (section 5). Dimensions are of the working part. "Print" = FDM 0.4 mm nozzle unless stated. Edge radius targets are post-finishing.

| ID | Name | Working geometry | Material / fabrication | Edge finish | Sensation hypothesis | Risk |
|---|---|---|---|---|---|---|
| **A** | Nail-mimic blade (DEFAULT) | 12 mm wide, 0.8 mm thick body tapering to 0.6 mm at the edge, free-edge overhang 6 mm beyond carrier, transverse curvature R 9 mm (matches index/middle nail), plan-form convex, corners R 1.5 mm, **edge radius 0.3 mm** | PETG or nylon sheet 0.8 mm (cut + file) **or** FDM PETG printed edge-up with blade body 1.2 mm thick and a 0.6 mm chamfered edge (see §8) | File to radius, 400→1000→2000 grit, PETG optional 1 s flame pass | Crisp scratch at 0.3–0.9 N, clear skin-fold/release feel | Thin PETG can crack at the root → ductile nylon preferred if a root fillet < 1 mm |
| **B** | Soft-edge blade | As A but **edge radius 0.6 mm**, body 1.2 mm | As A | Same, stop at 0.6 mm | Still a scratch but gentler; may become a stroke below 0.5 N. Brackets the window's gentle edge | Too mild → informs force setpoint |
| **C** | Nail-corner tip | 4 mm wide × 0.8 mm blade, edge R 0.3 mm, corners R 1.0 mm (this is "one corner of a nail") | Cut from a nylon or Tortex (POM) guitar pick, 0.73–1.14 mm gauge `[KNOWN gauges]` ([pick guide](https://tonestakr.com/guides/guitar-picks-complete-guide/)) | File + 1000 grit | Most intense localized scratch per newton (line load ×3 vs A); the "scratching an itch" feel | Highest prick risk: cap at 0.4 N; must have rounded corners |
| **D** | Multi-nail rake | 3 blades of type A (10 mm wide, 0.3 mm edge) on one carrier at **20 mm pitch**, each on its own 0.4 N/mm leaf (TPU living hinge or 0.5 mm spring-steel strip), independent travel 8 mm | Carrier FDM PETG; blades = press-on nails or pick stock glued with CA | As A | Hand-like; tests whether 3 simultaneous lines "feel like a hand" vs 1 line | Hair bridging between blades; weight; one blade dominating on curved scalp if compliance uneven |
| **E** | Pulp-backed nail | Blade A bonded to a 10 × 12 × 6 mm TPU 90A pad behind it, pad bonded to the tang; blade stands 40–45° to the tang axis | Two-part: FDM TPU 90A block (or cut from a TPU sheet / shoe-sole scrap) + nylon blade, CA + mechanical pocket | As A | Closest to finger: stiff edge on a local soft cushion; should limit force spikes and give the "pad behind nail" feel | TPU creep; glue failure under shear → use a dovetail pocket not just glue |
| **F** | Low-friction POM blade | Geometry of A | **Dunlop Tortex 1.14 mm pick** (Delrin = POM) cut to plan-form, or POM sheet 1.0 mm | 2000 grit + plastic polish to gloss | Same geometry, lower µ → tests "grabby vs slippery" hypothesis in isolation | May read as a stroke → that is the information |
| **G** | Stainless blade (optional) | 12 × 0.5 mm 304 sheet, edge R 0.25 mm, transverse curvature formed over a 9 mm rod | Cut from feeler-gauge stock or a 0.5 mm stainless sheet with shears; de-burr both faces | 600 → 2000 grit; **no** burr tolerated; verify with fingertip + loupe | Maximum stiffness/thermal "cool" feel; closest to a long real nail | Highest injury risk from a burr; only after A–C are characterized |
| **H** | 3 mm ball CONTROL | 3 mm sphere on a 2 mm stem, 6 mm standoff | 3 mm steel bearing ball glued in a printed cup, or a fully printed PETG ball sanded | Smooth | Should read as pressure/stroke at any force — the massager baseline | None; it calibrates the test scale |

**Zero-fabrication shortcuts (use these first):**

- **Press-on acrylic/ABS nails**: ~10–13 mm wide for sizes 0–3 `[KNOWN]` ([press-on sizing](https://www.joyeenails.com/blogs/news/press-on-nail-size-guide)), already transversely curved, ~0.5–0.8 mm thick `[EST]`, cost cents each. Trim the free edge to 3–5 mm overhang, file to R 0.3, CA-glue to a printed carrier. These are tip A with 10 minutes of work and are the recommended way to make the first dozen.
- **Guitar picks**: nylon (Dunlop .73/.88/1.0), Tortex/Delrin = POM (.73/.88/1.14), Ultex/polyetherimide (very stiff). Thin (0.40–0.59), medium (0.60–0.79), heavy (0.80–1.49) gauges `[KNOWN]` ([pick thickness classes](https://ironageaccessories.com/blogs/iron-age-general-blog/why-are-guitar-picks-different-thicknesses)). A pick is a flat sheet with a factory-rounded edge in the exact material family we want. Tips C and F come straight from picks.
- **Acetal/PETG/nylon sheet** 0.8–1.0 mm from hobby or packaging suppliers, cut with shears and filed.

### 4.1 Tip profiles (side view through the stroke direction; not to scale)

```
A/B  nail-mimic blade           C  nail corner            E  pulp-backed
   tang                            tang                      tang
  ======\                         ======\                   ======[TPU 90A]\
         \  body 0.8-1.2 mm              \ 4 mm wide               [       ] \   blade
          \                               \                        [       ]  \
           \_  edge R 0.3 (A) / 0.6 (B)    \_ edge R 0.3           [_______]   \_ R 0.3
     ~~~~~~~~~~~~~ skin ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Front view of A (looking along the stroke):           Rake D (front view):
      ______________                                   ___      ___      ___
     /              \   width 12 mm                   /   \    /   \    /   \
    |  transverse R9  |  curved like index nail       |   |    |   |    |   |
     \______________/   corners R 1.5                 |<- 20 mm ->|<- 20 mm ->|
          edge                                       each on its own 8 mm travel leaf

H  control ball:   ======----( O )   3 mm steel ball, reads as "pressure" by design
```

---

## 5. Tip mount standard — SP1-TM1

### 5.1 Requirements

1. Tool-free swap in < 10 s, one-handed.
2. Positive orientation key: the blade can only go in one way (edge leading, correct attack angle).
3. Scratch loads (normal ≤ 1.5 N into the tip, drag ≤ 1.5 N tangential) carried by **walls, not by the retainer**.
4. Pull-out (snag) breakaway in the range **4–8 N** along the tip axis `[EST]`, adjustable; well above scratch loads, well below the ~20 N+ that would rip a bundle of hair. Primary hair safety remains geometric (no hooks, no gaps); the breakaway is a backstop.
5. Shared compliance element lives in the holder so every tip is tested against the same spring (section 5.4).
6. Printable on an FDM machine with 0.4 mm nozzle; no tolerance tighter than ±0.1 mm.

### 5.2 Geometry

```
 Tip tang (on every tip)                          Holder pocket (on every mechanism)
 ----------------------                           -----------------------------
         10.0                                       pocket 10.3 x 4.3 x 12.5 deep
   +---------------+                                  (clearance 0.15/side)
   |               | 4.0                    +-------------------------------+
   | O  steel 6x1  |   <- M3 washer or      |  N52 6x2 (or 5x2) at floor    |
   |    slug       |      6x1 steel disc    |  magnet, axial, in 6.2 pocket |
   +--\            |      epoxied in pocket |                               |
       \___________+   <- 2 x 45° chamfer   |  matching chamfer on one wall |
       keyed corner        on ONE corner    |  (orientation key)            |
   length 12.0 mm                           +-------------------------------+
   insertion axis = tip normal axis (pushing the tip into the scalp seats it deeper, never out)
```

- Tang: 10.0 × 4.0 × 12.0 mm, one corner chamfered 2 × 45° along the full length (orientation key — a mirrored tip cannot seat). Material: same as tip body, or a universal PETG tang the blade is bonded/screwed to.
- Pocket: 10.3 × 4.3 × 12.5 mm, matching chamfer. Print the pocket with the opening facing up (no supports in the pocket).
- Retention: one axially magnetized **N52 6 × 2 mm disc** in the pocket floor against a **6 × 1 mm mild-steel disc or M3 flat washer** epoxied into the tang end. A 6 × 3 N52 has ~1.1 kgf (~11 N) rated pull to a thick plate `[KNOWN]` ([6×3 N52 listing](https://suprememagnets.com/products/n52-neodymium-magnet-disc-6mm-od-x-3mm-h)); against a 1 mm steel disc with a 0.1–0.2 mm print gap the real hold is roughly half `[EST]`. Tune breakaway to 4–8 N by (a) magnet size 5×2 / 6×2 / 6×3, (b) a 0.1–0.3 mm PETG shim, (c) steel disc thickness. **Measure it with a hanging-weight test (section 9) — do not trust ratings.**
- Alternative non-breakaway: tap the pocket floor for an **M3 × 6 button-head** through the tang (M3 heat-set insert in the holder). Use for tips D and G where mass or stiffness make magnet hold marginal. Takes a hex key; no longer tool-free.
- Attack angle is set by the holder, not the tip: the pocket axis is inclined **45° to the scalp normal** in the stroke plane; make the holder with 35° / 45° / 55° variants (three cheap prints) so angle is an experimental variable without re-making tips.

### 5.3 Load path check `[EST]`

- Normal scratch force (≤1.5 N) acts along the insertion axis **into** the pocket: zero load on the magnet.
- Drag (≤1.5 N at µ≈1) acts transverse: carried by the 12 mm deep pocket walls; bending moment at the pocket mouth ≈ 1.5 N × 8 mm overhang = 12 N·mm, trivial for a 4 mm PETG wall.
- Snag: a hair wrap pulls roughly along the tip axis as the stroke continues → breakaway at 4–8 N. A pure side snag is resisted by the walls, which is why the geometry must not have hooks: the breakaway cannot protect against a side-load snag.

### 5.4 Compliance: where the spring lives

**Recommendation for SP1: spring in the holder** (one compliance, shared by all tips, tunable, measurable). Spec: linear travel **8–10 mm**, stiffness **0.3–0.6 N/mm** (pulp-like), preload adjustable 0–0.5 N, hard stop at both ends. Implementations, cheapest first:

1. Compression spring in a printed guide (e.g. 6 mm OD × 20 mm, ~0.4 N/mm — common "pen spring" territory), 8 mm printed plunger carrying the TM1 pocket. Add a 1 mm TPU bumper at the inner stop.
2. Spring-steel or PETG leaf (cantilever 40 × 10 × 0.5 mm steel ≈ 0.5 N/mm `[EST]`), the TM1 pocket at the free end. Naturally gives the nail an arc that mimics a curling finger.
3. Printed PETG flexure (serpentine), lowest cost, creeps over weeks — acceptable for SP1 if replaced.

**Alternative: compliance in the tip** (tip E). Keep the holder spring and *add* the TPU pad; if E wins, SP2 can move the spring into the tip to shrink the holder. Do not run E with the holder spring locked out until A has been characterized — otherwise you can't separate the two variables.

---

## 6. Multi-contact arrays (hand-like rake)

- Human finger pitch: hand breadth at metacarpals ≈ 85 mm (men) / 75 mm (women), 97 / 87 mm in a firefighter cohort `[KNOWN]` ([British adult data](http://personal.cityu.edu.hk/meachan/online%20anthropometry/chapter2/Ch2-29.htm); [firefighter study](https://pmc.ncbi.nlm.nih.gov/articles/PMC4681492/)); four fingers across that span gives a **centre-to-centre pitch of ~18–22 mm**, and with fingers slightly spread during scratching, 20–25 mm `[EST]`.
- **Recommendation: 3 contacts at 20 mm pitch** for SP1 (span 40 mm). Three is enough to test "does multiplicity feel like a hand" while keeping the array narrow enough that all three can contact a curved scalp. Four at 20 mm (60 mm span) is the SP2 upgrade.
- **Independent compliance is mandatory.** Scalp radius ≈ 80–100 mm `[EST]`; sagitta across a 40 mm span = 40²/(8×90) ≈ 2.2 mm, across 60 mm ≈ 5 mm, plus crown-to-temple shape variation and head motion of a few mm → **required independent travel 5–10 mm per contact**, with the same 0.3–0.6 N/mm stiffness so no single blade hogs the load.
- Cheap ways: (a) one 0.5 mm spring-steel leaf per blade, cantilevered from a common bar (hacksaw-blade stock, de-tempered or just ground); (b) one FDM TPU 95A living hinge per blade, 2 mm × 10 mm neck — simplest, test for creep; (c) compression springs in individual 6 mm bores in a common block, each with a TM1 pocket plunger — heaviest but most tunable.
- Keep blades on a single carrier ≥ 8 mm apart edge-to-edge so hair cannot bridge and be pinched between two edges on direction change.

---

## 7. Materials

| Material | Thin-edge print quality | Edge durability | Skin contact | IPA cleanability | Friction vs skin (rank) | Verdict for SP1 tips |
|---|---|---|---|---|---|---|
| PLA | Good detail, but brittle; layers delaminate at a 0.6 mm edge | Poor: chips into glassy shards, creeps at 40 °C (body heat + hand) | Fine short-term | OK | Medium | **Excluded** for blades (shard risk); OK for holders and jigs |
| PETG | Good; slightly stringy; strong layer adhesion | Good: scuffs/whitens rather than shattering; tough | Widely used for wearables; wash before use | Yes, 70–90% IPA `[KNOWN]` ([solvent table](https://filaments.ai-driven.ai/content/pla-petg-asa-tpu-solubility-solvents-chemical)) | Medium (0.22–0.35 vs steel) | **Default blade and carrier material** |
| Nylon (PA6/PA12, or pick/sheet stock) | Hard to FDM thin (warp, moisture); excellent as cut sheet | Excellent: ductile, bends not breaks, wears glossy; absorbs water and softens slightly — more nail-like | Fine | Yes | Lowest (0.10–0.26) in bulk; vs skin similar to PETG | **Best for the thinnest (0.4–0.6 mm) blades**, from picks or sheet, not printed |
| POM / acetal (Delrin, Tortex) | Not FDM-friendly (warps, poor adhesion); use sheet/picks | Excellent: hard, slick, self-lubricating | Fine | Yes | Low (0.20) — the "slippery" arm of the friction A/B | **Tip F only** |
| TPU 85A–95A | Prints fine in ≥ 1.5 mm sections; poor at thin edges | Abrades, picks up hair/sebum | Fine; sweat-tolerant `[KNOWN]` ([TPU chemical resistance](https://siraya.tech/blogs/news/tpu-filament-chemical-resistance)) | Yes, short exposure | High (grabby) | **Pulp pads and living hinges only, never the edge** |
| ABS / ASA | Decent; needs enclosure; ABS acetone-smoothable (closes the layer lines on an edge) | Good | Fine | ASA yes; ABS yes (acetone no) | Medium | Acceptable alternate to PETG; press-on nails are typically ABS |
| SLA resin (standard) | Best edge definition of any process (0.05 mm features) | Brittle like PLA; uncured resin is a skin sensitizer — must be fully post-cured | Only if fully cured and washed | Yes | Medium–high (glassy) | Good for a **master** to compare geometry; not for a 20-minute scalp session until a tough resin is used |

**Recommendation:** nylon or PETG sheet/pick stock for blades A, B, C, F (nylon for ≤0.6 mm, PETG for 0.8–1.2 mm bodies), PETG for printed carriers and holders, TPU 90A for pads and hinges, press-on ABS nails as the quick start. PLA nowhere near the scalp.

---

## 8. Edge finishing, printing, wear and failure

**Making the edge.**
- Cut sheet 2–3 mm oversize, file to plan-form, then file the edge to a half-round: for R 0.3 mm on a 0.8 mm sheet, take the face chamfers to ~0.3 mm each and blend; for R 0.6 mm on a 1.2 mm body, full round.
- Sand 400 → 1000 → 2000 wet. PETG and acrylic: an optional 1 s pass with a lighter rounds the last micro-burrs (don't dwell: bubbles and droops). Nylon and POM: do **not** flame; finish with plastic polish or a felt wheel.
- FDM-printed blades: print **edge-up** (blade standing on its root) so the edge is made of stacked perimeters, not layer steps; 0.12 mm layers; 3 perimeters; body ≥ 1.2 mm; chamfer modelled into the CAD. A 0.4 mm nozzle cannot make a clean 0.6 mm edge directly — model 1.0 mm and sand to size.
- Verify radius: a cheap radius gauge set (0.5–7 mm) covers B; for A, compare under a 10× loupe against a 0.6 mm drill shank (R 0.3), or photograph the edge end-on next to a ruler at macro and measure. Record the radius on the tip's label.
- Burr test before every first use: drag a cotton ball along the edge (burrs snag fibres), then the back of the hand at 1 N.

**How edges wear `[EST]`.** PETG: micro-scuffing that whitens and *slightly increases* radius — safe direction; the sensation gets milder over tens of hours. Nylon: polishes glossy, radius stable, slightly lower friction over time. POM: negligible wear. TPU pads: sebum/hair fouling before wear. Stainless: no wear; only risk is a burr from fabrication.

**Inspection and replacement.** Loupe + cotton-ball check before every session (30 s). Replace any blade on: visible chip, crack or crazing (whitened stress line at the root), a radius change you can see, or after ~10 h of use as a precaution `[EST]`. Tips cost cents; do not economize.

**What a broken tip looks like, and why it matters.** A 0.6–0.8 mm PETG or acrylic blade fails at the root fillet or at a layer line, leaving (a) a stub in the carrier with a jagged edge and (b) a 5–10 mm fragment with two fresh square corners and possibly a sharp spall, now loose in the hair under a moving mechanism. Mitigations: root fillet ≥ 1 mm; overhang ≤ 6–8 mm; ductile nylon for thin blades; no PLA; a bright tip colour so fragments are visible in dark hair; and the mechanism's own pre-run check must include "all tips present and intact".

---

## 9. Tip test plan

**Instrumentation (all cheap):** kitchen scale with 1 g resolution (0.01 N) for normal force calibration; a 0–5 N spring/fish scale for drag and breakaway; metronome app for stroke rate; 10× loupe; radius gauge; a labelled tip box.

**T0 — Hand wand (do this before any mechanism exists).** Print one TM1 holder with the spring, on a pen-sized handle. This turns the tip family into a hand-held instrument. Everything below runs on the wand first; the mechanism later only has to replicate what the wand proves.

**T1 — Bench, non-human.**
1. Breakaway: hang weights from each tip in the holder (tip pointing down); record pull-out force; target 4–8 N. Record per tip (mass differs).
2. Spring: press holder on the kitchen scale, read force at 2, 4, 6, 8 mm of travel (ruler); target 0.3–0.6 N/mm.
3. Wig head with a human-hair or good synthetic wig: 200 strokes per tip at 0.5 N and 1.0 N, forward and reverse. Count hair catches, hair pulled out, direction-change snags. This answers hair interaction only; foam does not answer sensation.
4. Edge check after the 200 strokes (loupe).

**T2 — Forearm and back of hand (self, sensation screen).** Volar forearm is thin-skinned hairy skin — a reasonable stand-in for sensitivity; back of hand has sparse hair. Protocol per tip: 10 strokes, 40 mm, ~80 mm/s, at 0.3 / 0.6 / 1.0 N (practice the force on the scale first; most people press 2–3× harder than they think). Score sharpness 0–10, "scratch vs stroke vs pressure" (forced 3-way), pleasantness 0–10, any after-redness at 10 min. Any tip scoring sharpness ≥ 7 at 0.6 N does not go to the scalp.

**T3 — Scalp A/B (the real test).** Method: **paired forced-choice with blinding by tip code.** Pre-label tips with random letters; a second person swaps them (or Michael swaps with eyes closed and reads the code afterward). Per pair: 20 s with tip X, 20 s with tip Y, same region (start with the crown and behind-the-ear strips), same force band (0.5 ± 0.1 N by scale practice), same stroke. Record: which felt more like a fingernail; which was more pleasant; any sharp/prick events; hair pulls. Each pair repeated in both orders. Start with H vs A — if that pair isn't an overwhelming win for A, something in the setup (force, angle, spring) is wrong before any other variable matters. Then A vs B (radius), A vs F (friction), A vs C (width), A vs E (pulp), A vs D (multiplicity). Six pairs × 2 orders × 2 regions ≈ 40 minutes per session, over several days (adaptation and scalp fatigue bias the later pairs — randomize pair order daily).

**T4 — Endurance sanity.** Winning tip, 20 minutes continuous on the wand at the preferred force. Check scalp for redness at 0, 10 and 60 minutes, and the edge under the loupe.

**What the mechanism team receives from this plan:** the winning tip ID, the force band, the attack angle, the spring stiffness and travel, the contact count and pitch, and a breakaway spec — all expressed on the TM1 interface, so any mechanism that carries a TM1 pocket inherits the result.

---

## 10. Open questions (owned by test, not analysis)

- `[UNKNOWN]` Exact force band Michael prefers (0.3–0.9 N is the model; could be lower on the crown).
- `[UNKNOWN]` Whether friction (A vs F) or radius (A vs B) is the larger sensory lever — the model says radius, but sebum effects could flip it.
- `[UNKNOWN]` Whether 3 lines at 20 mm read as "a hand" or as three separate scratchers.
- `[UNKNOWN]` Hair-mat behaviour: does a 12 mm curved edge part hair or ride on it at 45°? (T1 answers.)

Sources: [Tohmyoh 2023 nail nanoindentation](https://onlinelibrary.wiley.com/doi/full/10.1111/srt.13456) · [Fingernail Configuration, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4659990/) · [Murdan 2011 transverse curvature](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-2494.2011.00663.x) · [Serina fingertip pulp](https://www.sciencedirect.com/science/article/abs/pii/S0021929097000651) · [Pailler-Mattei in-vivo skin indentation](https://www.sciencedirect.com/science/article/abs/pii/S135045330700135X) · [Derler & Gerhardt skin tribology review](https://link.springer.com/article/10.1007/s11249-011-9854-y) · [Imperial sebum friction study](https://spiral.imperial.ac.uk/server/api/core/bitstreams/540021e7-14c6-4cfb-b0cf-0fe86e9ecfda/content) · [Greenspan & McGillis sharpness](https://pure.johnshopkins.edu/en/publications/stimulus-features-relevant-to-the-perception-of-sharpness-and-mec-6/) · [Pressure pain threshold review](https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S0188-95322021000200203) · [Hand breadth anthropometry](http://personal.cityu.edu.hk/meachan/online%20anthropometry/chapter2/Ch2-29.htm) · [Filament friction table](https://github.com/superjamie/lazyweb/wiki/3D-Printing-Filament-Properties) · [Guitar pick gauges](https://tonestakr.com/guides/guitar-picks-complete-guide/) · [Press-on nail sizing](https://www.joyeenails.com/blogs/news/press-on-nail-size-guide) · [N52 6×3 magnet](https://suprememagnets.com/products/n52-neodymium-magnet-disc-6mm-od-x-3mm-h) · [Polymer solvent/IPA table](https://filaments.ai-driven.ai/content/pla-petg-asa-tpu-solubility-solvents-chemical)
