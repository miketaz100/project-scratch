# PROJECT SCRATCH — Hair Interaction Model and Design Rules

**Track:** 01-foundations · **Owner:** Hair-Interaction Specialist · **Date:** 2026-10-01
**Status:** Foundation document. Mechanism teams must comply with the rules in §4–§6 and self-score against the checklist in §6.5 before entering the tournament.

**Scope.** This document models the SCRATCHING ELEMENT ↔ HAIR ↔ SCALP system and derives constraints. It does not propose an overall mechanism. Every number is tagged **KNOWN** (sourced measurement), **ESTIMATED** (derived or extrapolated from sourced data, with the derivation shown), or **UNKNOWN** (needs physical testing).

**Assumed user hair (design basis).** We do not know Michael's hair. SP1 is designed for **short-to-medium, straight-to-wavy hair, 2–8 cm long, medium shaft diameter, normal density**. §1.9 analyzes sensitivity to longer, thicker, and curly hair. Every mechanism team must state which of those sensitivities their design survives and which it does not.

---

## 1. Hair as a material and a structure

### 1.1 Shaft diameter
- Fine 17–50 µm, medium 50–70 µm, coarse 70–180 µm; most adults 50–100 µm. **KNOWN** ([BrainVoyage summary of the literature](https://brainvoyage.blog/human-hair-diameter-microns); [Meyers group, UCSD, "Structure and mechanical behavior of human hair"](https://meyersgroup.ucsd.edu/papers/journals/Meyers%20434.pdf)).
- Design basis: **70 µm**. Sensitivity cases: 50 µm (fine) and 100 µm (coarse). Note that bending stiffness scales with d⁴, so a 100 µm hair is **4.2×** stiffer than a 70 µm hair and **16×** stiffer than a 50 µm hair. This is the single largest lever on how hair behaves under a scratching element.

### 1.2 Density
- Hair density on the scalp: ~124–200 hairs/cm², typical ~130–150 hairs/cm²; follicular units 65–85/cm² carrying 1–4 hairs each. **KNOWN** ([Bernstein & Rassman, follicular unit distribution, PubMed 10417585](https://pubmed.ncbi.nlm.nih.gov/10417585/)).
- Design basis: **150 hairs/cm²** → mean hair spacing ≈ 1/√150 cm ≈ **0.82 mm** between hairs (ESTIMATED from density; real spacing is clustered at follicular units ~1.2 mm apart with 1–4 hairs each).
- Consequence: any element wider than ~1 mm at scalp level is *always* pressing on several hairs; an element with a tip ≤1 mm wide can slip into inter-hair lanes.

### 1.3 Length classes and the "hair pile"
| Class | Length | Hair lies flat? | Effective pile depth over scalp (ESTIMATED) |
|---|---|---|---|
| Buzz cut | <1 cm | Stands up | 2–8 mm (hairs stand near follicle exit angle) |
| Short | 2–5 cm | Partly, directional | 5–15 mm |
| Medium | 5–15 cm | Yes, strongly directional | 10–25 mm, varies with styling |
| Long | >15 cm | Yes, can drape over device | 15–40 mm; also can hang into mechanism from any direction |

Pile depth matters because the element has to protrude at least the pile depth plus scalp-curvature tolerance to reach skin (§4.3). For the design basis (2–8 cm) assume **pile depth 5–20 mm**.

### 1.4 Stiffness and bending modulus
- Young's modulus 3–6 GPa (typically ~4 GPa; small-scale bending test gave 5.4 GPa). **KNOWN** ([ResearchGate: Tensile properties of single human hair fibers](https://www.researchgate.net/figure/Tensile-properties-of-single-human-hair-fibers_tbl1_329381307); [small-scale bending test](https://www.academia.edu/56578802/Accurate_determination_of_the_structural_elasticity_of_human_hair_by_a_small_scale_bending_test)).
- Flexural rigidity EI = E·πd⁴/64 (ESTIMATED, derived):
  - 50 µm: 1.2 × 10⁻⁹ N·m²
  - 70 µm: 4.7 × 10⁻⁹ N·m²
  - 100 µm: 2.0 × 10⁻⁸ N·m²
- Cantilever force to deflect the tip of a hair by 5 mm (F = 3EIδ/L³): 2 cm hair, 70 µm → **~9 µN**; 5 cm → **~0.6 µN**; 2 cm coarse 100 µm → **~37 µN**. (ESTIMATED.)
- **Design meaning:** a single hair resists lateral deflection with micronewtons. Even a bundle of 100 hairs under an element resists with <5 mN. Hair is *not* a mechanical obstacle to an element pushing sideways; it is only an obstacle when it is **captured and loaded in tension along its axis**, where it becomes a steel-like tether (§1.7). Every failure mode in §3 is a transition from "hair is bent" (harmless) to "hair is tensioned" (harmful).

### 1.5 Friction coefficients
| Pair | µ (dry) | Status | Source/notes |
|---|---|---|---|
| Hair–hair | 0.13 ± 0.02 dry, 0.25 ± 0.03 wet | KNOWN | [Tribology in Industry 2025 (Indian-origin hair)](https://www.tribology.rs/journals/2025/2025-2/10-1848.pdf); [Bhushan, Wei & Haddad 2005, Wear](https://www.sciencedirect.com/science/article/abs/pii/S0043164804004533) |
| Hair–polyurethane (synthetic skin) | ~0.1–0.2 | KNOWN (range) | Bhushan 2005 |
| Hair–keratin (nail) | ~0.15–0.25 | ESTIMATED | keratin-on-keratin ≈ hair–hair; nail is smoother than hair |
| Hair–polished steel | ~0.1–0.2 | ESTIMATED | polished steel vs. keratin; low adhesion |
| Hair–acetal (POM), nylon | ~0.15–0.3 | ESTIMATED | engineering plastics with keratin; comb experience |
| Hair–PETG, ABS, PLA (as-printed) | 0.3–0.5+ | ESTIMATED | layer lines act as micro-cuticle; rough |
| Hair–silicone (platinum-cure, Shore A 20–40) | 0.5–1.0+ | ESTIMATED | silicone is tacky and high-friction against keratin; hair "grabs" |
| Hair–TPU (Shore A 85–95) | 0.4–0.8 | ESTIMATED | less tacky than silicone, still high |

**Design meaning:** silicone and soft TPU are *hair-grabbing* materials. They are fine as a *compliant mount* behind a tip but should not be the surface that slides through hair. Smooth, hard, low-surface-energy materials (POM, nylon, polished steel) slide through hair best.

### 1.6 Cuticle directionality (friction anisotropy)
- Cuticle scales point root→tip. Sliding tip→root (against the grain) raises single-fiber friction by ~23% on average and can interlock scale edges; sliding root→tip shows no clear directional penalty. The effect grows with humidity and damage. **KNOWN** ([ScienceDirect, "Understanding and controlling the friction of human hair"](https://www.sciencedirect.com/science/article/pii/S0001868625001915); [Bhushan AFM directionality study](https://pubmed.ncbi.nlm.nih.gov/16675116/)).
- For our purposes the *macroscopic* hair-lie anisotropy (§2.3) dominates the microscopic cuticle anisotropy by an order of magnitude. Cuticle anisotropy matters mainly in §3.7 (hair-hair matting with repeated against-grain strokes, which lifts cuticles and velcros hairs together).

### 1.7 Tensile properties of a strand
- Tensile strength 200–260 MPa; a single hair bears ~1.5 N before breaking (coarse hairs more, fine hairs less). **KNOWN** ([ScienceDirect, "On the strength of hair across species"](https://www.sciencedirect.com/science/article/pii/S2590238519302346); [Physics World summary](https://physicsworld.com/a/thin-hairs-beat-thicker-ones-in-strength-test/)).
- Hookean (elastic) limit ~2–5% strain; yield 5–30%; break at roughly 30–50% elongation. **KNOWN** ([Meyers UCSD](https://meyersgroup.ucsd.edu/papers/journals/Meyers%20434.pdf); [Keratin stress/strain review](https://www.researchgate.net/publication/249784629_The_StressStrain_Curve_of_Keratin_Fibers_and_the_Structure_of_the_Intermediate_Filament)).
- Elastic-limit force for a 70 µm hair ≈ E·A·0.02 = 4 GPa × 3.85 × 10⁻⁹ m² × 0.02 ≈ **0.3 N**; break ≈ 0.8–1.5 N (ESTIMATED).
- **Design meaning:** the strand's breaking force (~1 N) is *higher* than the force needed to pluck a growing (anagen) hair (0.36 N, §1.8). **A caught hair will usually pluck, not snap.** The device cannot rely on the hair breaking as a fuse.

### 1.8 Follicle anchoring force and pull pain
- Slow-extraction force: **anagen ~0.36 N, telogen ~1.8 N** (telogen club hairs are counter-intuitively more firmly held in that study; other sources quote ~0.69 N (70 gf) to epilate a single hair). **KNOWN** ([J. Biomechanics, failure behavior of hair anchorage during slow extraction](https://www.sciencedirect.com/science/article/abs/pii/S0021929000002049)). The brief's "0.5–1 N" range is therefore roughly right for the *middle* of the population, but the floor is lower: **design to 0.3 N as the pluck threshold for a single anagen hair**. ~85–90% of scalp hairs are anagen.
- Pain: circumferential Aδ high-threshold mechanoreceptors wrap each follicle and fire on a single-hair pull; activation threshold measured in mice >4 mN by von Frey, and hair-pull is reported as ~10× as painful as a pinprick with very fast conduction. **KNOWN (mouse threshold; human qualitative)** ([Ghitani et al. 2017, Neuron](https://www.cell.com/neuron/fulltext/S0896-6273(17)30646-3); [Neuroscience News summary](https://neurosciencenews.com/hair-pull-pain-neuron-7327/)).
- Human perceptual thresholds (ESTIMATED from the above and everyday experience): a single hair pulled at **~0.05–0.1 N** is clearly felt as a "tug"; **~0.2–0.3 N** on a single hair is painful and may pluck; a **bundle of ~50 hairs** (standard clinical hair-pull test, 4–6 mm diameter tuft) pulled with a few newtons is uncomfortable but not injurious in healthy scalp, normally shedding ≤2 hairs ([hair pull test guidelines, JAAD 2017](https://www.sciencedirect.com/science/article/pii/S0190962216308921)).
- **The hazard is concentrated load on few hairs, not distributed load on many.** A 2 N load spread over 50 hairs is 40 mN/hair (a tug); the same 2 N on one hair plucks it.

### 1.9 Sensitivity to hair outside the design basis
| Variant | What changes | Risk delta |
|---|---|---|
| Long (>15 cm) | Hair can hang into the mechanism from any direction, including from *above* and *behind* the elements; wrap-around becomes possible on any exposed rotating part within reach of a draped strand (reach = hair length); pile depth 15–40 mm | Severe. Rules H-6.1/H-6.2 (joint exclusion) become mandatory for all joints, not just those within 30 mm of scalp |
| Coarse (100 µm) | 4× stiffer; pile is springier; less likely to be captured in sub-100 µm gaps but more likely to resist parting and to push elements up off the scalp | Moderate; element must protrude further and carry more normal force to reach scalp |
| Curly / coily | Hair does not have a single "grain"; strands cross each other and form natural loops; any reciprocating element passing through a loop can tighten it (lasso); detangling resistance ~5–10× straight hair (ESTIMATED from comb-force experience) | Severe for any element that moves *through* the pile rather than *under* it; SP1 should explicitly declare curly hair out of scope unless a with-grain-only, lift-off-every-stroke pattern is used |
| Buzz cut (<1 cm) | No pile; elements contact scalp directly; hair cannot wrap or loop; main residual risk is capture of short stiff hairs in gaps (they act like bristles and enter any gap) | Low — the easiest case; a good "first human test" configuration |
| Thinning / fine | Low pluck resistance, low pile; easy scalp access but each caught hair plucks at lower force | Low mechanically, but set force limits lower |

---

## 2. How a fingernail reaches the scalp through hair

### 2.1 The parting mechanics of a narrow blunt edge
A fingernail is a **thin, slightly convex plate with a rounded free edge** (~0.3–0.6 mm thick at the edge, edge radius ~0.1–0.3 mm, width 8–14 mm). When pressed toward the scalp at a steep angle (nail roughly 45–70° to the skin) it presents a *line contact* less than a millimetre wide. Because inter-hair spacing is ~0.8 mm (§1.2) and a single hair deflects under micronewtons (§1.4), the nail edge does not need to push a bundle aside: it finds the nearest lane, each hair it meets bends away with ~10 µN of resistance, and the nail descends to skin in a few millimetres of travel. The parting force for a nail through short/medium hair is **< 10 mN** (ESTIMATED — sum of a few dozen hairs' bending resistance), negligible compared with the 0.3–2 N normal force used in scratching.

A **ball or bulb** (radius ≥1.5 mm) fails to part hair for two reasons: (a) its contact patch spans several hairs simultaneously, so it must deflect them all at once *and* they bend around it rather than away from it, sharing load like a trampoline; (b) a sphere has no edge to "cleave" the pile — the local surface is nearly tangent to the hair it meets, so hairs get pushed down and compressed as a mat under it. The user feels a dull press through a cushion of hair rather than skin contact. The crossover radius from "parts hair" to "rides on hair" is roughly **tip radius ≈ inter-hair spacing (~0.8–1 mm)** (ESTIMATED): below it, the tip fits in the lanes; above it, it bridges them. This is the comb-tooth principle: comb teeth part hair because each tooth is narrower than the lanes it enters.

### 2.2 Why nails travel between hairs, not over them
Once the nail edge reaches skin, the hairs it bent are leaning away from it on both sides, each holding ~10 µN of restoring force. As the nail moves tangentially, hairs ahead of it are met at the **follicle exit** (the stiffest, most anchored point) and are bent aside by a short lever arm — but the force to do so is still only tens of µN because the nail edge is sliding along the skin *below* the hair's pivot. The hair springs back behind the nail within ~10–50 ms (hair's natural cantilever frequency is tens to hundreds of Hz; UNKNOWN precisely, but visibly fast). Nothing is left disturbed. This is why human scratching does not tangle hair: the moving edge is below the hair canopy, meets hairs one at a time at their stiffest point, and never loads a hair along its axis.

The key enabling conditions, which an artificial element must reproduce:
1. Contact point at skin level (not floating in the pile).
2. Leading edge narrow relative to lane spacing.
3. Leading-edge geometry that deflects hair *sideways and up*, never *down and under* the element (a down-and-under hair becomes a strand trapped between element and scalp, loaded in tension).
4. No part of the element above skin level that can catch a sprung-back hair.

### 2.3 Hair lie and stroke direction
Scalp hair has a macroscopic "grain": follicles are angled and hairs lie in streams radiating from the crown whorl toward the forehead, temples, and nape; many people have a second whorl or a cowlick at the nape or hairline. **KNOWN** ([Hair whorl, Wikipedia](https://en.wikipedia.org/wiki/Hair_whorl); [Nape whorl description](https://www.hairfinder.com/hair4/nape_whorl.htm)).

| Stroke vs. grain | What the element meets | Drag (ESTIMATED, relative) | Tangle risk |
|---|---|---|---|
| With-grain (follicle → tip direction) | Hairs already leaning away; element slides under the canopy | 1× | Lowest |
| Cross-grain (90°) | Hairs lean across the path; element lifts them over its edge one at a time | 1.5–2× | Low–moderate; hairs flip over the element and spring back |
| Against-grain | Element meets each hair tip-first and must reverse the hair's lean; hairs pile up ahead of the element as a growing wave | 3–5× rising with distance | Highest; the wave of reversed hairs becomes a mat that the element rides up onto, losing scalp contact; strands fold under the element |

The human scratcher instinctively uses short against-grain strokes (they feel good — more skin stimulation because the hairs are lifted at the follicle, which is itself a mechanoreceptor site) but **always lifts off before the wave builds**. Against-grain strokes are not forbidden; long, un-lifted against-grain strokes are.

### 2.4 Lift-off
At the end of a human stroke the fingertip rotates and the nail lifts away from the skin *through* the pile and clear of it, then comes down fresh at the start of the next stroke. Lift-off does three things:
1. Releases any hair that has been pushed ahead of the edge (the wave of §2.3 collapses back to its lie).
2. Resets any strand that has slipped under the nail before it can be loaded in tension by the reversed stroke.
3. Re-randomizes which lane the nail enters, spreading wear and sensation.

A reciprocating element that reverses *without* lift-off replaces all three benefits with their opposites (§3.4, §5.2). Lift-off is the single most important hair-safety kinematic and should be treated as a required motion primitive, not an optional refinement.

---

## 3. Entanglement and pulling failure modes

Each entry: mechanism → trigger conditions → severity → mitigations. Severity scale: **S1** nuisance (drag, noise, hair disturbance), **S2** tug (felt, unpleasant), **S3** pluck (hair loss, sharp pain), **S4** sustained pull/trap (cannot free without stopping machine; risk of multiple plucks or skin tear).

### 3.1 Wrap around a rotating shaft (capstan trap)
**Mechanism.** A strand that touches any exposed rotating surface with a non-zero wrap angle is dragged by friction. The capstan relation T_out = T_in·e^(µθ) means the holding tension multiplies by e^(2πµ) per turn: with µ = 0.15, one turn ×2.6, three turns ×17, five turns ×111; with µ = 0.25, three turns ×111. (ESTIMATED, derived.) Thus even if the initial drag on the hair is a few millinewtons, **three turns on a plastic shaft are enough to exceed the 0.3 N pluck threshold**, and the shaft then pulls the follicle with the full motor torque.
**Trigger conditions (all three required).** (a) An exposed rotating surface; (b) a hair long enough to reach it and contact it over ≥ ~90° of arc (hair length ≥ distance from scalp to shaft + ~πr/2 — for a 10 mm diameter shaft 20 mm above the scalp that is ~28 mm; buzz cuts are nearly immune, 5 cm+ hair is fully exposed); (c) rotation continuing ≥ 1 turn after first contact (a reciprocating ±90° rocker cannot build a wrap; a continuously rotating shaft can).
**Severity.** S3–S4; robot-vacuum brush rolls show each turn tightening the strand ([Narwal](https://us.narwal.com/blogs/high-tech-life/robot-vacuum-anti-tangle-technology); [US20160345792A1](https://patents.google.com/patent/US20160345792A1/en)).
**Mitigations.** (1) No continuously rotating surface exposed within hair reach (§6.1); prime movers live above a hair-shedding guard. (2) Convert rotation to oscillation (<1 turn) before it reaches hair. (3) If unavoidable: non-rotating sleeve over the shaft, a boot, or a tapered hub shroud that leads hair outward ([US 11058271](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11058271)). (4) Torque limiting is not a real mitigation: stalling below 0.3 N at r = 5 mm needs ≤ 1.5 mN·m, below any practical motor.

### 3.2 Capture in gaps and pinch points
**Mechanism.** A hair enters a gap wider than its diameter; a *changing* gap (two parts moving relative to each other) then clamps it, and the moving part drags it.
**Gap thresholds (ESTIMATED from hair diameter and bending stiffness).**
- < 40 µm: hair cannot enter. Achievable in prints only by design (press fits, overlapping lips).
- 50–200 µm: hair enters and cannot escape; a sliding/rotating gap here is a **shear trap**. Typical 3D-print clearances (0.1–0.3 mm) land squarely here — **the most dangerous band**.
- 0.2–1 mm: loosely held; a changing gap pinches, a constant gap drags (S1–S2).
- 1–3 mm: single hairs pass; bundles can jam.
- > 3 mm: open; only a loop or wrap can hold.
**Trigger conditions.** Any gap >50 µm within hair reach of the scalp whose width changes, or across which one face moves relative to the other, in the direction that can carry a hair *into* a narrowing region (the classic "V" between a rotating hub and a stationary housing).
**Severity.** S2–S4 depending on the drive force behind the pinch.
**Mitigations.** Design rule: **every gap within hair reach is either < 40 µm (sealed) or > 3 mm (open), and no changing gap is permitted** (H-4.9). Where a moving part passes a fixed part, use a compliant wiper lip (TPU) or a labyrinth with the rotating member *inside* the stationary one so the exposed seam is a stationary edge.

### 3.3 Snagging on edges and at reversal
**Mechanism.** A hair draped over a sharp or re-entrant edge of a moving element is carried along by friction (µ ≈ 0.2 against the element) and then, at a reversal or at the end of travel, is held by the edge while the element's inertia or the next stroke loads it in tension.
**Trigger.** Edge radius < ~0.3 mm, any undercut or notch, any step facing the direction of travel, layer lines of 3D prints oriented perpendicular to the stroke.
**Severity.** S1 at a single edge with low force; S3 if the snag is at the scalp end of the element and the element reverses with the hair hooked.
**Mitigations.** All element edges radiused ≥0.5 mm (≥1 mm near scalp); no re-entrant features anywhere on the element below the hair canopy; polish or vapour-smooth printed tips; orient print layers parallel to the stroke direction.

### 3.4 Loop formation during reciprocation
**Mechanism.** On the forward stroke, a strand slips under the element (it was lying across the path and was bent down rather than aside). The element reverses *without lifting*, dragging the strand back toward its root; the strand buckles into a loop ahead of the element. The next forward stroke passes *through* the loop; the following reversal pulls it tight around the element — a lasso. After two to three cycles the loop is a knot with the follicle at one end and the element at the other.
**Trigger.** Reciprocation in place without lift-off; element with any feature a loop can tighten around (a neck, a groove, a gap between two elements); more likely with cross-grain and against-grain strokes and with wavy/curly hair, which pre-loops.
**Severity.** S3–S4. This is the dominant failure mode for linear reciprocating scratchers and the reason the rule in §5.2 exists.
**Mitigations.** Lift-off at every reversal (H-5.2); smooth, neckless, tapered element profile (nothing to lasso); stroke-direction randomization so loops are never reinforced; with-grain bias.

### 3.5 Accumulation and matting with repeated strokes in one spot
**Mechanism.** Each against-grain or cross-grain pass without lift-off displaces hairs ahead of the element by a few millimetres and lifts cuticle scales (§1.6). Repeated passes in the same ~3 cm patch accumulate displaced hairs into a mat; lifted cuticles velcro adjacent hairs together ("backcombing" — hairdressers do this deliberately to create volume, and it is exactly what we must not do).
**Trigger.** > ~10–20 passes in one spot without lift-off and without a with-grain "combing" pass; dry, fine, or damaged hair; against-grain direction.
**Severity.** S1 cumulatively → S2 as the element starts riding on the mat and the mat tugs at follicles when finally cleared. A matted patch is also the seed for 3.4.
**Mitigations.** Dwell/repetition limits (H-5.5); periodic with-grain "comb-out" strokes; lift-off; wander the stroke location.

### 3.6 Static charge
**Mechanism.** Hair sits high on the triboelectric series (readily positive); PP, PE, nylon, acetal and most polymers sit lower, so sliding contact charges hair positive and the element negative. Charged hairs repel each other (fly-away) and are attracted to the element — they stand up into the mechanism and cling to the element after lift-off. **KNOWN** ([Tangram: static electricity and plastics](https://tangram.co.uk/wp-content/uploads/Plastics-Topics-Static-electricity-and-plastics.pdf); [AlphaLab triboelectric series](https://www.alphalabinc.com/triboelectric-series/)).
**Trigger.** Dry air (<40% RH), fine clean hair, insulating element materials, high stroke rates.
**Severity.** S1 directly; it raises the probability of 3.1, 3.2 and 3.4 by feeding hairs into the mechanism.
**Mitigations.** Conductive or static-dissipative tip materials (carbon-filled nylon/POM, ESD-grade acetal, stainless steel tips grounded to the frame); a grounded metal frame; humidified/lightly conditioned hair for testing; nylon is the least-bad common polymer (closest to hair on the series).

### 3.7 Hair drawn into bearings, gears and joints
**Mechanism.** Hair drawn by friction or static into a bearing or gear mesh winds around the inner race or packs the mesh. Unlike 3.1 this can happen even with reciprocating motion because the gear/bearing clearance is in the 50–200 µm trap band (§3.2).
**Trigger.** Any open bearing, gear, pivot pin, slot, or lead screw within hair reach (hair length + ~10 mm from the scalp surface in any direction the hair can hang).
**Severity.** S3–S4 plus mechanism damage.
**Mitigations.** §6.1: all joints within 30 mm of the scalp (or within hair reach for long hair) are sealed, booted, or placed above a hair-shedding guard. Treat "hair reach" as a 3-D volume the size of the hair length, not a flat distance.

### 3.8 Scissoring between two elements moving relative to each other
**Mechanism.** A strand bridging two elements that move toward or past each other is either clamped (gap closes), cut (edges pass), or pulled (one element carries it against the other).
**Trigger.** Two elements whose spacing changes during the stroke, within the hair canopy; counter-rotating or phase-shifted neighbouring elements; a moving element passing a fixed guard.
**Severity.** S3–S4.
**Mitigations.** H-5.6: within the hair canopy, neighbouring elements move *together* (rigid or near-rigid array). Relative motion between elements is permitted only above the canopy or with spacing that never drops below 3 mm.

### 3.9 Anchored-strand tension build-up
**Mechanism.** One end of a strand is in the follicle, its middle is pinned under element A (which is pressing on the scalp with 1 N), and its free length is dragged by element B or by the carriage. The pinned point acts as a fixed pulley; the strand is loaded in tension between follicle and pin with the full tangential force of B.
**Trigger.** Multiple contact points on the scalp with relative motion, or one element pressing while the carriage moves; any element whose underside can trap a strand against the scalp (flat underside, wide footprint).
**Severity.** S2–S3.
**Mitigations.** Minimize footprint pressing on hair (narrow tips); compliance in the tangential direction (§4.11) so A yields before the strand reaches 0.1 N; no tangential motion of a carriage while any element is in scalp contact *unless* the element rides freely with it.

---

## 4. Design rules for scratching elements (tip-level)

Rules are numbered H-4.x for citation by mechanism teams. "Must" rules are gating.

**H-4.1 Tip is a blade, not a ball.** The scalp-contacting feature **must** be a thin edge (nail-like): thickness at the edge 0.5–1.5 mm, width (along the edge) 3–12 mm, with the edge presented to the scalp at a steep angle (40–70° between the element face and the skin). Spherical tips > 1 mm radius ride on the pile (§2.1) and are permitted only as a deliberately-worse comparison tip in the tip experiment.

**H-4.2 Tip edge radius 0.2–0.6 mm.** Below ~0.15 mm the edge becomes an abrasive and can score the stratum corneum under 1–2 N; above ~1 mm the edge bridges hair lanes and stops reaching skin. Target **0.3 mm** for the baseline nail-like tip; provide 0.2 and 0.5 mm variants. (ESTIMATED from fingernail free-edge geometry; no literature value.)

**H-4.3 Leading-face geometry sheds hair up and out.** The element profile from scalp to root must be a continuously widening wedge or cone with **draft ≥ 10°** on every face, no steps, no necks, no grooves. Hair deflected by the leading edge must be able to slide up the face and off the top, never into a narrowing. Comb teeth, which are long tapered wedges, are the reference geometry.

**H-4.4 No re-entrant features below the hair canopy.** No undercuts, holes, slots, set-screw pockets, fastener heads, or seams within **25 mm** of the tip (design basis) or within hair length for long hair. If a tip must be replaceable (brief §11), the interface must be a smooth socket whose seam is **above the canopy** and either sealed (<40 µm) or covered by a sleeve.

**H-4.5 Element protrusion.** Tip must protrude beyond any adjacent surface (guard, carriage, neighbouring element root) by at least **pile depth + 10 mm curvature/positioning margin**: design basis **≥ 25 mm** for 2–8 cm hair; ≥ 15 mm for buzz cut; ≥ 40 mm for long hair. If the element is shorter than the pile, the carrier itself rides on the hair and the tip never reaches skin.

**H-4.6 Element spacing in arrays ≥ 8 mm centre-to-centre** at the tip, ≥ 10 mm preferred. Rationale: comb experience — fine combs (≤1 mm) grab, wide-tooth combs (≥3 mm) pass hair; a scratching element also has width and a sideways motion component, and hair bundles between two tips must be able to escape without being clamped. Human scratching uses 4–5 nails at ~12–18 mm spacing. (KNOWN comb spacing: [Jingsourcing comb types](https://jingsourcing.com/p/b49-hair-comb-brush-types/); spacing rule ESTIMATED.)

**H-4.7 Materials.**
| Material | Hair friction | Static | Printability / machinability | Verdict |
|---|---|---|---|---|
| Acetal/POM (Delrin), machined or turned | Low | Moderate (insulator) | Excellent to machine; poor to print | **Preferred tip material**; ESD grade if available |
| Nylon (PA12, PA6, CF-nylon) | Low–moderate | Lowest among polymers (nearest hair on series) | SLS/MJF prints are good, FDM is OK with drying; smooth surfaces needed | Good; CF-nylon is semi-dissipative |
| PETG / PLA / ABS (FDM) | High as printed | High | Easy | Only with polishing/vapour-smoothing; prototype-grade |
| Polished stainless steel | Low | None if grounded | Buy as pins, blanks, or guitar-pick-like stampings | Excellent for tips; must be radiused; heavier |
| TPU (85–95A) | High | Moderate | Easy | **Not** for the sliding surface; good for compliant mounts, wipers, boots |
| Silicone | Very high (tacky) | Moderate | Casting | **Forbidden as a sliding surface**; permitted as boot/seal/mount |
| Keratin-like (actual nail, horn, hard resin ~Shore D 80) | Reference | Moderate | Cast resin | Use a hard cast resin or POM as the "keratin-like" variant |

**H-4.8 Surface finish.** Ra ≤ 0.8 µm (polished plastic / 400-grit-then-buffed) on all surfaces that touch hair. Printed tips must be sanded, buffed, or vapour-smoothed; raw FDM layer lines at 0.1–0.2 mm pitch are a micro-ratchet against hair (§1.6).

**H-4.9 Gaps near scalp.** Within 25 mm of the scalp: no gap in the 40 µm–3 mm band, and **no changing gap** at all (§3.2). Push-fit tip sockets must be sleeved.

**H-4.10 Minimum radii.** Tip edge per H-4.2; all other edges ≥ 0.5 mm within the canopy, ≥ 1 mm on anything that can face the scalp. No 90° corners anywhere on the element.

**H-4.11 Compliant mounting so a caught strand yields.** Each element (or rigid group of elements) **must** mount through a compliance that limits tangential force at the tip to **≤ 0.15 N before significant deflection (≥ 3 mm)** — e.g. a flexure, a cantilever spring, a TPU living hinge, or a magnetic breakaway. Rationale: 0.15 N on a single trapped hair is a firm tug but well below the 0.3 N anagen pluck floor (§1.8); a human finger's pulp and knuckles provide exactly this compliance. This must coexist with the normal-direction force needed to scratch (0.3–2 N): the compliance is anisotropic — stiff normal, soft tangential beyond the scratch-friction load. Note the budget: scratching friction at 1 N normal × µ_skin ≈ 0.3–0.5 gives 0.3–0.5 N tangential during a normal stroke, so the compliance should be *preloaded* to ~0.3–0.5 N and yield above that (a snagged strand adds to the scratch load; the mount yields at the sum). Set the exact preload by test (§7).

**H-4.12 Antistatic.** Prefer dissipative tips (CF-nylon, ESD-POM, grounded steel). Ground the frame. Keep test hair at ≥ 40% RH or lightly conditioned.

**H-4.13 Breakaway tips.** Tips must detach (magnet, snap, or shear pin) at ≤ 3 N tangential as a last resort against a wrapped or looped strand, and the detached tip must have no cord, wire, or tether that can itself wrap hair.

---

## 5. Design rules for motion

**H-5.1 With-grain bias.** Default stroke direction is with-grain for the region being scratched (crown → forehead on top, crown → nape on the back, crown → ears on the sides, with a per-user map because whorls vary). Cross-grain is permitted. Against-grain strokes are permitted **only if short (≤ 25 mm) and followed by lift-off**. The scalp-region grain map is a required input to the control logic.

**H-5.2 Lift-off at every reversal (gating).** No element may reverse its tangential direction while in scalp contact. Minimum lift: clear the canopy — **≥ pile depth + 5 mm (≥ 15–25 mm for the design basis)** — or, where the mechanism cannot lift that far, at least **≥ 5 mm with the scalp-contact force reduced to zero** (hair that was under the tip is released once normal force is zero even if the tip is still in the pile). Lift-off should be a rotation of the tip about its trailing edge (as a finger does), so the leading edge rises first and any hair ahead of it slides off.

**H-5.3 Lift-off kinematics.** Lift before decelerating to zero tangential velocity, not after: the tip should leave the skin while still moving forward at ≥ 30% of stroke speed, so that any hair pushed ahead of the edge is overrun and released rather than reversed. Re-entry should be at the start of the next stroke with the tip already moving tangentially at a shallow angle (plough-in at ≤ 30° to the skin), not a vertical stab, which drives hair under the edge.

**H-5.4 Speed and acceleration limits.** Human scratch stroke speeds are roughly 30–150 mm/s (ESTIMATED; the sensation track owns the human model). From the hair side: tip speed is limited not by hair breakage but by (a) impulsive load on a snagged strand — a 0.3 N tug delivered in 10 ms is a pluck, delivered over 300 ms it is a tug the compliance can absorb — and (b) the compliance's ability to react. Rule: **tangential acceleration ≤ 2 m/s² while in contact**, reversals only after lift-off, and tip velocity ≤ 200 mm/s. These keep a snag event inside the compliant mount's bandwidth (verify in §7.4).

**H-5.5 Dwell and repetition limits.** No more than **8 consecutive strokes** over the same ±15 mm patch without either relocating ≥ 20 mm or executing a with-grain comb-out pass; no stationary rubbing (zero-stroke oscillation of a loaded tip) longer than 2 s. Rationale: §3.5 matting threshold.

**H-5.6 Multi-element arrays.** Elements within the canopy move as a rigid group (parallel, same phase, same direction). Permitted: a 3–5 tip "hand" that strokes, lifts, repositions. Forbidden: adjacent tips in antiphase, counter-rotating neighbours, or any two elements whose tip spacing changes while either is in contact (§3.8). If a mechanism wants independent fingers, their spacing at the tip must never fall below 3 mm and they must lift off before changing relative position.

**H-5.7 Motion patterns that comb rather than tangle.** A stroke pattern is hair-positive if every element's path through the canopy is monotonic in one direction between lift-offs, biased with-grain, and advances location with each cycle (like a slow raster). Patterns that are hair-negative: in-place circles with a loaded tip (orbital scrubbers), figure-8s without lift-off, and random dithering. Orbital/circular motion is acceptable only if the orbit radius is small (< 3 mm) *and* the tip lifts off between orbit sets, or if the "orbit" is produced by a tip that is rotating about its own axis with no exposed rotating surface (a rocking pad), not by a tip translating in a circle through the pile.

**H-5.8 Carriage motion.** A positioning carriage moving between stroke sites must do so with all elements lifted. Any element in contact while the carriage moves counts as a stroke and is subject to H-5.1–5.5.

**H-5.9 Start-up and stall.** On start-up, elements begin lifted and come down onto the scalp before any tangential motion. On a tangential-force or current-spike event (snag), the correct reflex is **lift and retract**, not stop-in-place (stopping with a loaded strand leaves it loaded) and never reverse (which tightens a loop).

---

## 6. Design rules for the machine

**H-6.1 Hair-exclusion zone.** Define the exclusion volume as everything within **30 mm** of the scalp surface for the design basis (buzz cut: 15 mm; long hair: the entire hair length plus 10 mm, in any direction a strand can hang, including upward-draped). Within it: no exposed rotating surface, no open bearing, gear, pivot, slot, lead screw, belt, cable, or pulley; no changing gaps; no 40 µm–3 mm gaps. Mechanism teams must draw this volume on their layout and list every joint inside it with its exclusion method.

**H-6.2 Joint exclusion methods (ranked).** (1) Relocate the joint above a hair-shedding guard (best); (2) convert rotation to oscillation before it enters the zone; (3) non-rotating sleeve over a rotating shaft, with the sleeve's end lip sealed to the housing (< 40 µm) or booted; (4) elastomer boot or bellows (TPU print or silicone, since it is not a sliding-through-hair surface); (5) labyrinth where the moving member is inside and the exposed seam is a stationary lip. Felt or brush seals are **not** acceptable (they are themselves hair traps).

**H-6.3 Hair-shedding guard.** A smooth, convex, drafted (≥ 15°) shell between the scalp and all mechanism, through which only the elements pass. Element pass-throughs are either sealed to the element (boot) or > 3 mm clear on all sides with the element profile such that a hair in the clearance is pushed out, not in (element widens *above* the guard, never below it). Guard underside is smooth and ≥ 1 mm radius on all edges; its standoff from the scalp is ≥ pile depth so it does not itself drag hair.

**H-6.4 Breakaway and magnetic mounts.** Tips (H-4.13) and preferably whole "hands" should detach under a defined overload (3–5 N tangential) via magnets or snap features, with no tether. A detached part must fall away from the head, so breakaway mounts should be oriented so gravity assists.

**H-6.5 Force limits derived from hair.**
- Max tangential force any single element can apply to a single caught strand before the mount yields: **0.15 N** (H-4.11).
- Max tangential force at the tip under any condition (compliance bottomed, motor stalled): **≤ 1.0 N** per element. Rationale: even bottomed-out, a single strand loaded to 1 N will pluck (anagen floor 0.36 N) — so this is a *skin*-protection limit (shear on the scalp) and a motor-sizing cap, not a hair-protection limit. Hair protection comes from H-4.11 and H-6.6, not from this cap.
- Max force before breakaway: 3–5 N.
- Normal force per element: set by the sensation track (likely 0.3–2 N); from the hair side, higher normal force increases the chance of pinning a strand under the tip (§3.9) — so narrow tips are preferred over high force for "intensity".

**H-6.6 Snag detection.** Mechanically: the compliant mount's deflection is the sensor (a simple contact or Hall switch at 3 mm deflection). Electrically: motor current rise above the stroke baseline. Response per H-5.9: lift and retract within 100 ms. This is a backstop, not a substitute for the geometry rules.

**H-6.7 Cleanability.** Shed hairs accumulate on the guard and in boots; everything inside the exclusion zone must be removable without tools for cleaning, and a "hair audit" (count of shed hairs on the guard after each session) is part of the test protocol.

### 6.8 Hair safety checklist (mechanism teams self-score; 2 = fully met, 1 = partially / with caveats, 0 = not met; any 0 on a gating item fails)
| # | Item | Gating? | Score |
|---|---|---|---|
| 1 | No exposed continuously rotating surface within the exclusion zone (H-6.1) | Yes | |
| 2 | Every joint in the exclusion zone has a named exclusion method (H-6.2) | Yes | |
| 3 | No changing gap, and no 40 µm–3 mm gap, within 25 mm of scalp (H-4.9) | Yes | |
| 4 | Elements lift off before every reversal (H-5.2) | Yes | |
| 5 | Elements within the canopy move as a rigid group (H-5.6) | Yes | |
| 6 | Tip is a radiused blade/nail with drafted root and no re-entrant features (H-4.1–4.4) | Yes | |
| 7 | Compliant mount yields at ≤ 0.15 N tangential on a snag (H-4.11) | Yes | |
| 8 | Element protrusion ≥ 25 mm beyond any adjacent surface (H-4.5) | | |
| 9 | Tip spacing ≥ 8 mm (H-4.6) | | |
| 10 | Tip and sliding surfaces are low-friction, polished, not silicone/TPU (H-4.7, 4.8) | | |
| 11 | Breakaway at 3–5 N with no tether (H-4.13, H-6.4) | | |
| 12 | Hair-shedding guard with smooth drafted pass-throughs (H-6.3) | | |
| 13 | With-grain bias and grain map in control logic (H-5.1) | | |
| 14 | Dwell/repetition limits implemented (H-5.5) | | |
| 15 | Snag reflex = lift and retract, never reverse (H-5.9) | | |
| 16 | Antistatic measures (H-4.12) | | |
| 17 | Tool-free removal of all exclusion-zone parts for cleaning (H-6.7) | | |
| 18 | Design states which hair variants (long / coarse / curly) it tolerates (§1.9) | | |
| | **Total /36** | | |

A design scoring < 28, or with any gating 0, must not proceed to human testing.

---

## 7. Bench-test method (before any human test)

### 7.1 Test heads and hair (all cheap)
1. **Real-hair wig on a foam/canvas wig head** (cosmetology training head, 100% human hair, ~$40–80). Primary article: real cuticle, friction, static. Keep one trimmed to 3–5 cm and one long.
2. **Synthetic (Kanekalon) wig** (~$15): higher friction and static than human hair, so a conservative screen for wrap and loop.
3. **Stocking-over-foam scalp with sewn-in hair wefts** (~$10/50 g) at ~1 cm pitch with a chosen grain; glue individual strands with a weak adhesive that releases at ~0.3 N to give a visible pluck count.
4. **Buzz-cut analogue**: 5–10 mm craft fur over foam, for short-stiff-hair gap capture.
5. **10 × 10 cm patches** of each for tip-level bench tests.

### 7.2 Instruments
- **5 kg load cell + HX711 + Arduino** (~$15) or a digital luggage scale: tangential drag. Mount the head on a drawer-slide sled tied to the scale.
- **0.1 g kitchen scale** under the head: normal force.
- **Single-hair tether**: one hair (or 70 µm nylon monofilament, ~0.2 N break) tied to a 15 g / 50 g / 100 g weight over a pulley; a lifted weight shows the element's capture force.
- **Phone slow-motion (240 fps)** with low side light and a $10 macro clip lens.
- **Black card or lint roller** under the head to count shed hairs per 5-minute run; baseline the wig's own shedding first.
- **Hygrometer** ($10); run static tests below 35% RH and above 50%.

### 7.3 Test sequence
1. **Static tip test (no motion).** Press each tip onto the real-hair patch at 0.5, 1, 2 N; photograph from the side; does the edge reach the stocking/scalp? (Pass: visible skin contact through the pile for all hair lengths in scope.)
2. **Single-stroke drag test.** Hand-pull the tip (or run the mechanism one stroke) with-grain, cross-grain, against-grain at 50 mm/s and 1 N normal; record drag force. Expect ~0.3–0.5 N with-grain; flag any tip whose against-grain drag exceeds 3× with-grain or rises along the stroke (wave formation).
3. **Reversal test.** Run 50 reversals in place *without* lift-off, then 50 *with* lift-off, on the real-hair head; count loops/knots and shed hairs. This test alone justifies H-5.2 and should be filmed.
4. **Wrap test.** With the long wig draped over the running mechanism in every orientation the head could take, run 5 minutes; inspect every joint. Any wrap = fail.
5. **Gap probe.** With the mechanism running, offer single hairs and small tufts into every seam and clearance with tweezers. Any capture = fail for that gap.
6. **Snag-yield test.** Tether a strand with the 50 g weight across the stroke path; run; the compliant mount should deflect and release before the weight lifts (i.e. < 0.5 N; the 0.15 N target is checked with a 15 g weight).
7. **Endurance / matting.** 20 minutes continuous on the real-hair head with the intended pattern; measure shed hairs, photograph the hair state before/after, comb-out force before/after (pull a wide-tooth comb through with the scale).
8. **Static test.** Repeat 7 at < 35% RH; observe fly-away and hair cling to the tips after lift-off.
9. **Tip-material comparison.** Same stroke, same force, swap tips (POM, nylon, polished PETG, raw PETG, steel, TPU): drag force and shed count per tip.

### 7.4 Pass criteria for proceeding to human testing
- Zero wraps, zero gap captures, zero knots in tests 3–5.
- Shed hairs in test 7 ≤ 2× the wig's hand-combing baseline.
- Snag-yield force ≤ 0.3 N measured; ≤ 0.15 N target.
- With-grain drag ≤ 0.6 N per element at 1 N normal.
- All gating checklist items at 2.

---

## 8. What remains UNKNOWN (needs physical testing)

1. **Hair friction against candidate tip materials** (POM, nylon, PETG finishes, steel, TPU) — §1.5 values are estimates; test 7.3.9.
2. **Michael's single-strand tug threshold** in newtons; the 0.05–0.1 N "felt" and 0.15 N mount-yield figures are anchored on the 0.36 N anagen pluck force, not on perception data.
3. **Crossover tip radius** between "parts hair" and "rides on hair" per hair length/density (0.8–1 mm is geometric reasoning); test 7.3.1.
4. **Hair spring-back time** after an element passes, which bounds safe re-entry timing; slow-motion in 7.3.2.
5. **Matting onset** per grain direction and hair type (H-5.5's "8 strokes" is a placeholder); test 7.3.7.
6. **Compliant-mount dynamics**: can a mount that yields at 0.15 N tangential still deliver 1–2 N normal without chatter, and does its bandwidth catch a snag at 150 mm/s; test 7.3.6 at speed.
7. **Static-charge magnitude** at real stroke rates and apartment humidity, and whether dissipative tips matter; test 7.3.8.
8. **Michael's hair**: length, diameter, density, grain map, whorl position, thinning regions. A five-minute measurement (comb to find grain; caliper a plucked strand; photo-count 1 cm²) replaces every assumption here.
9. **Curly hair** is outside the design basis and untested; §3 would need re-derivation.
10. **Whether with-grain-only strokes are sensorially sufficient** — the hair track prefers with-grain; the sensation track may want against-grain for intensity. The human test, not either foundation document, resolves this.
