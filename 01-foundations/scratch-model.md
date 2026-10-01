# PROJECT SCRATCH — Human Scalp-Scratch Engineering Model (SCRATCH-MODEL v1)

Author: Sensory-Biomechanics Lead. Date: 2026-10-01.
Status: specification baseline for all mechanism-design teams. No mechanisms are proposed here.

Reading guide: every number carries one of three labels.
- KNOWN: measured in peer-reviewed literature (URL given), applied to the scalp with little extrapolation.
- ESTIMATED: derived from physics/anatomy or extrapolated from a related body site; the derivation is shown.
- UNKNOWN: no usable data; value is informed judgment and is flagged as a test variable in section 9.

Caution that applies throughout: there is no published biomechanical study of one person scratching another person's hair-covered scalp. The closest measured data are (a) self-scratching of the forearm with an instrumented tablet, (b) investigator brush-scratching of forearm/back/ankle itch, and (c) microneurography of hairy forearm skin. Scalp-specific values are therefore mostly ESTIMATED. The prototype must be a research rig precisely because of this.

---

## 1. Phenomenology: what the sensation is

### 1.1 Definition
The target sensation is the experience of several fingernail free-edges being drawn, lightly and semi-irregularly, across the scalp through the hair canopy by another person. Subjectively it has five components, listed with the receptor story in section 2:

| # | Component | Subjective quality | Carried by |
|---|-----------|-------------------|------------|
| A | Hair-canopy sweep | "fizzy", diffuse, spreading, pleasant; largest contributor to the shiver/tingle | mass deflection of hundreds of hair shafts per stroke, each loading its follicle's lanceolate endings and the C-tactile/C-LTMR afferents coupled to follicles |
| B | Nail-edge skin contact | "sharp", focal, satisfying, "reaching the itch"; the thing that makes it a scratch rather than a stroke | thin stiff moving line contact at ~100–300 kPa local pressure, well under pain, activating field/hair units and probably a mild Aδ/nociceptor counter-stimulus |
| C | Multi-point irregular rhythm | "alive", unpredictable, attention-capturing; prevents fade-out | 3–5 contacts at ~20 mm pitch moving with phase/force jitter, 1–4 Hz reciprocation, pauses and region jumps |
| D | Sound | dry hiss from nail-on-hair conducted through the skull; part of the ASMR context | broadband contact noise (0.15–8 kHz) and bone conduction |
| E | Context | warmth of the hand/palm, weight of a resting hand, social attribution ("someone is doing this to me") | thermal, SA pressure, cognition |

### 1.2 Sharp distinctions from neighbouring sensations

| Property | SCRATCH (target) | Massage / kneading | Vibration | Brushing | Light stroking / caress |
|---|---|---|---|---|---|
| Contact element | hard keratin edge, radius ~0.1–0.3 mm, ~3–6 mm long line | soft pad ≥ 10 mm, or knuckle | pad/plate | 20–200 bristles, 0.1–0.5 mm, pitch 1–5 mm | soft fingertip pulp, 10–15 mm patch |
| Normal force per contact | 0.1–0.5 N | 5–40 N | 1–10 N | 0.01–0.05 N per bristle, 1–5 N total | 0.05–0.3 N |
| Local pressure | 50–300 kPa (line) | 20–100 kPa (but deep) | n/a | low | 2–20 kPa |
| Scalp translation over skull | < 1 mm | 5–15 mm (scalp slides on loose areolar layer) | 0 | 0–2 mm | 0–2 mm |
| Tangential travel per cycle | 10–50 mm sliding on skin | 0–10 mm, skin moves with hand (no slip) | 0 | 50–200 mm, mostly on hair | 50–300 mm |
| Velocity | 3–20 cm/s | 1–5 cm/s | 0 (oscillatory 20–200 Hz) | 10–40 cm/s | 1–10 cm/s |
| Dominant frequency | 1–4 Hz reciprocation | 0.2–1 Hz | 20–250 Hz | 0.5–2 Hz | 0.1–0.5 Hz |
| Hair interaction | parts the canopy, deflects shafts near root, nail reaches skin | compresses canopy, moves scalp | shakes canopy | combs canopy, mostly tip of shafts | glides over canopy |
| Receptor emphasis | hair-follicle Aβ + C-LTMR/CT, field units, mild Aδ | SA2/Ruffini, deep pressure, muscle afferents | Pacinian (FA2) | hair units (tip deflection), Pacinian from bristle flicker | CT, SA1 |
| Habituation | slow if pattern is irregular | moderate | fast (Pacinian adapts in < 1 s) | fast (regular) | moderate |

The two signatures that are unique to scratching and absent from every neighbour are: (1) a stiff, narrow edge that reaches the skin surface through the hair, and (2) hair deflection close to the root (first 2–5 mm above the skin) rather than at the free tips. A device that produces either but not both will read as a brush (deflects hair tips only) or as a probe/massager (touches skin with a blunt pad).

### 1.3 Ranking of components by expected contribution to pleasure (judgment, with reasoning)

1. A — hair-canopy sweep near the root. Reasoning: the scalp has 150–250 terminal hairs/cm² (KNOWN), each follicle is wrapped by lanceolate Aβ endings and is now shown to be coupled to C-tactile afferents in humans (KNOWN, forearm). A single 4-nail stroke deflects ~1,000–4,000 hairs (section 3.14). No other body site concentrates follicle afferents like this; this is why head scratching feels different from back scratching. The "tingle"/ASMR spread is most parsimoniously a mass C-LTMR event.
2. B — focal nail-edge skin contact. Reasoning: scratching pleasure in the itch literature is produced by brush/nail stimulation at 0.1–0.3 N that is "mildly painful" and inhibits itch neurons spinally (KNOWN); subjects rate scratching as pleasurable even without itch (lower, but present). The sharp edge is the difference between "scratch" and "pet". Remove it (use a pad) and the result is a stroke.
3. C — irregular multi-point rhythm. Reasoning: hair units and field units are rapidly adapting; they fire during movement only. Predictable stimuli are centrally down-weighted (the same mechanism that abolishes self-tickle). Regular machine motion is the most likely failure mode for SP1 even with perfect contact physics.
4. D — sound. Reasoning: scratch noise is a known ASMR trigger and is unavoidable with real nails on hair; it is probably a minor-but-real contributor, cheap to get right, and is testable with ear plugs.
5. E — thermal/social context. Reasoning: present in human scratching but not reproducible or necessary; likely a modulator rather than a carrier.

---

## 2. Receptor-level mechanism

### 2.1 Receptor classes present in scalp skin and what each needs

| Afferent / end organ | Present on scalp? | Adequate stimulus | Tuning | Role in scratch |
|---|---|---|---|---|
| Hair units (Aβ, rapidly adapting, lanceolate palisades around follicles) | yes, every terminal follicle; lanceolate endings confirmed in human scalp by 3D EM (KNOWN) | movement of hair shafts; fire only during hair motion, not during held deflection; firing rate rises with deflection velocity | each unit innervates ~25 follicles (range 15–52) on forearm (KNOWN); receptive fields large | primary carrier of component A; any stroke that moves shafts near the root lights up dozens of units |
| C-tactile (CT) / C-LTMR, lanceolate endings | yes (hairy skin only; scalp not recorded directly but face/forearm/arm are) | gentle stroking; optimal 1–10 cm/s with peak ~3 cm/s (KNOWN); respond to deflection of single hairs; threshold as low as 0.04–0.4 mN (KNOWN) | slow conduction (< 2 m/s); pleasantness ratings track CT firing | "pleasant/affective" channel; also drives the delayed, spreading tingle; argues for a slow-stroke mode within the pattern set |
| Field units (Aβ RA) | yes | light skin contact, moving edges; many small hot-spots over a large field | fast-adapting | respond to the nail edge sliding on skin (component B) |
| SA1 (Merkel) | yes, lower density than glabrous skin | sustained indentation, edges, curvature | slowly adapting, ~2–30 Hz | encode the nail's sharpness/edge and the dwell/pause phases |
| SA2 (Ruffini) | yes | skin stretch | slow | mostly massage/stretch; minor in scratch (scalp barely displaced) |
| Pacinian (FA2) | yes, sparse | 100–300 Hz vibration, remote taps | very fast adapting | picks up nail-on-hair micro-stick-slip (the "fizz") and sound-band vibration; not the goal and will dominate if the device vibrates |
| Aδ mechano-nociceptors / "scratch" fibres | yes | sharp edge, > ~0.5–1 N on a sub-mm edge | | contribute the mild counter-irritation that makes scratching satisfying; must stay well below pain |
| Pruriceptors | yes | itch mediators | | scratching inhibits spinal itch neurons via glycine/GABA; pleasure correlates with itch intensity |

Innervation density context (KNOWN, Corniani & Saal 2020): neck+scalp hairy skin ~17 Aβ units/cm², the densest hairy-skin region of the body apart from the face (forehead ~48/cm²), versus ~9/cm² on trunk/back. Each hair unit covers ~25 follicles. CT fibres are not counted in that estimate but are abundant in hairy skin.

### 2.2 What this implies for stimulus design

- Velocity. Two optima coexist: CT pleasantness at 1–10 cm/s (peak ~3 cm/s) and hair-unit drive that increases with velocity, with self-scratching naturally landing at 11–18 cm/s on the forearm (KNOWN). A head scratch therefore should span roughly 3–15 cm/s, with the slow end for "pleasant/tingle" phases and the fast end for "satisfying scratch" phases. Below ~1 cm/s both channels go quiet; above ~30 cm/s CT drops off and the stimulus reads as brushing/flicking.
- Force. Receptors saturate long before pain. CT thresholds are < 1 mN; hair units respond to sub-mN hair bending. The 0.1–0.3 N investigator-brush force used in pleasantness fMRI studies, and the 0.36 N "low" self-scratch force, define the useful floor. The ceiling is set by comfort/abrasion (section 3.17), not by receptor need. Pleasure does not scale with force above ~0.5 N per contact; it scales with reaching the skin and with pattern.
- Spatial pattern. Hair units and field units have large receptive fields (cm-scale) with many hot-spots; they do not need fine spatial precision. What they need is movement across many follicles, which argues for several contacts moving in parallel rather than one precise one, and for strokes that cross the hair lie (more follicles deflected per mm of travel than strokes along the lie).
- Temporal pattern. Every FA class is silent during a held contact. SA1 and central mechanisms habituate within seconds to a stationary or periodic stimulus. The stimulus must keep moving and must keep changing something (direction, speed, phase, location, force) on a 2–10 s timescale.

### 2.3 How a nail dragging through hair deflects hair shafts (physics)

Model a scalp hair as a cantilever anchored in the follicle, exiting the skin at 10–60° (KNOWN), diameter d = 50–100 µm (KNOWN), Young's modulus E ≈ 2–5 GPa (KNOWN, tension; bending modulus comparable).

Bending stiffness: EI = E·π·d⁴/64. For d = 70 µm, E = 3 GPa: I = 1.18 × 10⁻¹⁸ m⁴, EI ≈ 3.5 × 10⁻⁹ N·m². (ESTIMATED)

Force to deflect the tip of the free length L by δ (small deflection): F = 3·EI·δ / L³.
- Nail engages 5 mm above skin, pushes 2 mm sideways: F ≈ 0.17 mN per hair.
- Nail engages 2 mm above skin, pushes 2 mm: F ≈ 2.6 mN per hair.
- Nail engages 10 mm above skin (riding on the canopy, brush-like): F ≈ 0.02 mN per hair.

Bending moment delivered to the follicle: M = F·L ≈ 0.8–5 × 10⁻⁶ N·m in the near-root cases, which is what the lanceolate palisade senses. The key point for engineers: the sensory drive per hair scales as 1/L². Engaging hair within 2–5 mm of the skin gives 4–25× more follicle stimulus per hair than engaging it 10 mm up. This is the mechanical reason that a nail (which reaches the skin) and a brush (which does not) feel different even when both move the same hairs.

Hair-count per stroke: with 200 hairs/cm² and a nail edge of effective length 5 mm sweeping a 1 mm-wide band per mm of travel, the nail meets ~10 hairs per mm advanced (0.05 cm² × 200). A 50 mm stroke by one nail deflects ~500 hairs; four nails ~2,000 hairs; at 10 cm/s that is ~4,000 hair-deflection events per second across ~40 hair units (4 cm² × 17 units/cm² × overlap). Hairs are released behind the nail and spring back (they are elastic, damped by neighbours), producing a second, smaller deflection event. (ESTIMATED)

Forces compared with hair safety: per-hair bending loads of 0.1–3 mN are 100–3,000× below the 0.36 N anagen extraction force (KNOWN, pig skin in vitro) and ~300× below the ~1 N single-fibre breaking force (KNOWN). Bending does not pull hair out. Hair is pulled out or broken only when a shaft is captured and loaded in tension (wrapped, pinched, or wedged). This is the whole story of section 6.

---

## 3. Quantitative parameter envelope

Convention: "per contact" means per nail. Where a literature value comes from the forearm or from self-scratching it is marked and the extrapolation stated.

| # | Variable | Best estimate | Plausible range | Label | Basis |
|---|---|---|---|---|---|
| 3.1 | Fingers in contact | 4 (index–little, one hand) | 1–5 one hand; 6–10 two hands | ESTIMATED | Anatomy/observation; thumb usually anchors or opposes; two-handed "shampoo" scratching uses 8–10 |
| 3.2 | Normal force per nail | 0.15–0.3 N | 0.05–0.6 N | ESTIMATED | Investigator brush-scratch for pleasantness 0.1–0.3 N (KNOWN); self-scratch forearm total force low/med/high = 0.36 ± 0.23 / 0.66 ± 0.29 / 1.56 ± 0.58 N (KNOWN) divided over the 2–4 fingers used; scratching someone else is gentler than self-scratching an itch |
| 3.3 | Total normal force (all contacts) | 0.6–1.2 N | 0.2–2.5 N | ESTIMATED | 4 × per-nail; upper end matches "high" self-scratch 1.56 N; add 0–3 N of resting palm/finger-pulp weight that is not scratch load |
| 3.4 | Effective friction coefficient, nail edge through hair to skin | 0.35 | 0.25–0.7 | ESTIMATED | Dry skin on smooth probe ~0.46 ± 0.15, head-with-hair on helmet liner 0.27 dynamic / 0.32 static (KNOWN); a nail edge that catches skin micro-relief or hair bundles plows, pushing the instantaneous ratio toward 0.7–1.0 |
| 3.5 | Tangential force per nail | 0.05–0.1 N (steady), spikes to 0.3 N | 0.02–0.4 N | ESTIMATED | μ × normal force plus hair-bundle plowing |
| 3.6 | Stroke velocity | 8 cm/s | 2–20 cm/s; slow mode 2–5 cm/s, brisk mode 10–20 cm/s | ESTIMATED | Self-scratch 11–18 cm/s (KNOWN, forearm); CT optimum 1–10 cm/s peak ~3 (KNOWN); social stroking targets ~3 cm/s (KNOWN) |
| 3.7 | Stroke length | 3 cm (rake), 10 cm (sweep) | rake 1–5 cm; sweep 6–15 cm; wiggle 0.5–1.5 cm | ESTIMATED | Head dimensions (crown-to-nape arc ~20 cm, ear-to-ear over crown ~35 cm) and hand reach |
| 3.8 | Reciprocation frequency | 2 Hz | 1–4 Hz | KNOWN (itch literature validated 1–5 Hz as "scratch-like"); scalp application ESTIMATED | Mouse scratch bouts are 6 Hz peak and must NOT be used as a human reference |
| 3.9 | Contact dwell (time nail stays in skin contact per stroke) | 150–400 ms | 50 ms–3 s | ESTIMATED | Stroke length / velocity; pauses of 0.5–3 s with nails resting occur between bouts |
| 3.10 | Direction-reversal timing | reversal in 50–120 ms with momentary force drop of 30–70% | 30–250 ms | ESTIMATED | Hand kinematics; the force dip at reversal is what lets a hair slide off the nail (section 6) |
| 3.11a | Nail edge: effective contact length on scalp | 4 mm | 2–8 mm | ESTIMATED | Nail transverse curvature radius index/middle 8.8–8.9 mm men, 7.3–7.4 mm women (KNOWN) against scalp radius 80–100 mm → only the central arc touches; scalp compliance adds length |
| 3.11b | Nail edge radius (free-edge rounding) | 0.15 mm | 0.05–0.4 mm | ESTIMATED | Nail thickness 0.4–0.6 mm (KNOWN); filed edge is a half-round to a slightly bevelled profile |
| 3.11c | Nail stiffness | E ≈ 2–4 GPa dry, falls to 0.2–0.5 GPa at 100% RH; plate thickness 0.43–0.6 mm | | KNOWN | Nanoindentation 2.8–3.1 GPa; tensile 2–4 GPa; humidity sensitivity large. The free edge is a short stiff cantilever (free length 1–4 mm): bending stiffness ≈ 3·E·(w·t³/12)/L³; for w = 10 mm, t = 0.5 mm, L = 2 mm, E = 3 GPa → ~0.1 N/µm, i.e. effectively rigid. The nail is NOT the compliance in the system |
| 3.11d | Contact area per nail | 1–3 mm² | 0.5–6 mm² | ESTIMATED | length 2–8 mm × width 0.2–0.6 mm (edge + a sliver of plate) |
| 3.11e | Mean contact pressure per nail | 100–200 kPa | 30–500 kPa | ESTIMATED | 0.2 N / 1.5 mm² |
| 3.11f | Nail-plate angle to scalp tangent plane | 45° | 25–65° | ESTIMATED | < 20°: pulp takes the load, becomes a rub; > 70°: edge digs/scrapes, hair catches |
| 3.12 | Finger compliance normal to scalp (effective stiffness at the nail) | 0.3 N/mm | 0.1–1 N/mm | ESTIMATED | Pulp stiffness 0.17–0.52 N/mm below 1 N (KNOWN) but the nail bypasses the pulp; the compliance seen by the scalp is DIP/PIP/MCP joint give plus wrist; a relaxed scratching finger yields ~1 mm per 0.3 N and the scalp 1–3 mm per N on top. Consequence: a 1 mm head/scalp irregularity changes force by only ~0.3 N, not by a stall. Any device must deliver comparable or lower stiffness (0.1–0.5 N/mm) at the tip |
| 3.13 | Finger centre-to-centre spacing | 20 mm | 16–28 mm | ESTIMATED | Index-finger breadth ~15–17 mm (KNOWN); fingers relaxed-splayed during scratching |
| 3.14 | Penetration / fraction of stroke in skin contact | short hair (< 3 cm): 70–90% of stroke; medium: 40–70%; long dense hair: 10–40% | 5–95% | UNKNOWN | No data. Nails ride up over bundles and re-descend; hair exit angle 10–60° means a nail moving against the lie lifts hair and reaches skin, moving with the lie slides under/along it |
| 3.15 | Hair deflection per hair | 1–3 mm lateral at 2–5 mm above skin; per-hair force 0.1–3 mN; follicle moment ~1–5 µN·m | | ESTIMATED | Section 2.3 |
| 3.16 | Scalp curvature radii | crown/vertex 85–100 mm (near-spherical); frontal/top 80–100 mm sagittal; parietal sides 100–150 mm vertical, 70–90 mm front-back; temporal 100–200 mm (nearly flat, slight concavity in the fossa); occipital bun 60–80 mm; nape/occipital-to-neck transition concave, R ≈ −50 to −100 mm | | ESTIMATED | Head length ~190–195 mm, breadth ~140–155 mm (KNOWN); ellipsoid curvature; no published regional radius table found |
| 3.17 | Scalp pressure discomfort threshold | 190 kPa (1 cm² probe) | 110–300 kPa; men 167 ± 73, women 214 ± 95 | KNOWN | Dense 3D PDT map of head (Antwerp). Note: thresholds for sub-mm edges are much higher in pressure terms (pinprick pain needs several MPa) but lower in force terms; use FORCE per nail ≤ 0.6 N and EDGE RADIUS ≥ 0.1 mm as the twin ceilings |
| 3.18 | Scalp skin thickness | epidermis+dermis 1.7–1.9 mm (ultrasound/histology) adult; total soft tissue to bone 3.5–5.5 mm | 1.4–2.1 mm skin | KNOWN | |
| 3.19 | Hair density | 200/cm² | 150–250/cm² by ancestry (Caucasian 214–230, Hispanic 169–178, African 148–160) | KNOWN | |
| 3.20 | Hair shaft diameter | 70 µm | 50–120 µm | KNOWN | |
| 3.21 | Hair exit angle from skin | 30° | 10–60° | KNOWN | |
| 3.22 | Hair extraction force | anagen 0.36 N, telogen 1.8 N (slow pull) | | KNOWN (pig skin, in vitro) | Human scalp anagen likely similar order (0.2–0.6 N); 10–15% of hairs are telogen and come out easily under tension |
| 3.23 | Single-hair breaking force | ~1 N (100 gf) at 80 µm | 0.5–1.5 N | KNOWN | |
| 3.24 | Abrasion/shear ceiling for repeated cycles | no number exists; blister/abrasion is a function of shear × cycles | | UNKNOWN | Working rule: tangential force per nail ≤ 0.3 N, pressure ≤ 300 kPa, no single spot receiving > 50 passes/min, skin inspection after each session |

Derived check on pressure vs. threshold: a nail at 0.2 N over 1.5 mm² is ~130 kPa, i.e. around the 1 cm²-probe discomfort threshold. This is consistent with scratching sitting at the itch/pain boundary: it is designed by biology to be just-sub-noxious locally while being tiny in total force. A pad 10 mm across at the same force gives ~2.5 kPa and reads as a touch, not a scratch.

---

## 4. Pattern model: what scratchers actually do

### 4.1 Primitives
No published ethogram exists for scratching another person's head; the following decomposition is from observation and is UNKNOWN in its proportions (candidate for a quick video study, section 9).

| Primitive | Geometry | Speed / rate | Force | Typical duration | Notes |
|---|---|---|---|---|---|
| P1 Short reciprocating rake | 4 nails, stroke 1.5–4 cm, mostly across or against hair lie | 1.5–4 Hz, 5–15 cm/s mean | 0.1–0.4 N per nail, modulated ±30% stroke to stroke | 2–8 s bouts (4–25 cycles) | the canonical "scratch"; the hand stays put, fingers/wrist reciprocate |
| P2 Long sweep | 4 nails, 6–15 cm single pass, nape→crown, temple→crown, hairline→back | 5–12 cm/s, one direction, then lift and return | 0.1–0.3 N | 1–2 s per sweep, 3–6 sweeps | engages the most follicles per pass; feels "luxurious"; often along the lie on the sides |
| P3 Circular rub | nail tips tracing 1–3 cm circles | 0.7–2 Hz | 0.2–0.5 N | 2–6 s | borderline massage; nails on skin keeps it a scratch, pulp makes it a rub |
| P4 Finger-wiggle "spider" | fingers move individually out of phase, 0.5–1.5 cm excursions, hand stationary | 3–6 Hz per finger | 0.05–0.2 N | 2–6 s | highest unpredictability; strong tingle driver; low force |
| P5 Pause/rest | nails resting or just lifted | 0 | 0–0.1 N | 0.3–3 s | lets FA units reset; anticipation |
| P6 Region change | lift 1–3 cm, translate 3–10 cm, soft landing | landing ramp 0.2–0.5 s | ramps 0→target | 0.3–1 s | landing is a soft touch-down, not a tap |
| P7 Edge events | hairline tracing, behind-ear, nape scratch | slow 2–5 cm/s | low | 2–5 s | high-sensitivity regions, used as "treats" |

### 4.2 Sequencing and dwell
- Dwell per region before moving: 5–20 s typical; rarely > 30 s in one spot (ESTIMATED).
- A typical 60 s episode: 3–6 region changes, 60–70% of time in P1/P2, 10–20% P4, 5–10% P3, 10% pauses.
- Transitions follow adjacency (crown→back→nape, or temple→side→crown) more than random jumps; occasional long jumps (left temple → right occipital) add surprise.
- Stroke-to-stroke variability (ESTIMATED from hand motor variability): stroke length ±25–35%, speed ±20%, force ±30–50%, inter-stroke interval ±20%, direction wander ±15–30°.
- Fingers are not phase-locked: in P1 the four nails hit the skin within a spread of 20–80 ms and at different depths because of joint compliance and scalp curvature. This asynchrony is probably perceptually important (it is what P4 maximises).

### 4.3 Why variability matters (adaptation)
- Hair units, field units and Pacinians fire only on movement/change; SA1 slows within seconds; CT fibres show fatigue to repeated identical strokes.
- Centrally, predictable self-generated or periodic touch is attenuated (the reason self-tickling fails). A machine running a fixed trajectory becomes "a machine" within ~10–30 s even if the first strokes feel right.
- Itch-relief studies show pleasure tracks ongoing relief, and in the no-itch case pleasure is modest and decays; the ASMR literature identifies "unpredictability", "personal attention" and "slow movements" as triggers.

### 4.4 Recommended pattern specification (control-system level; mechanism-agnostic)

```
PATTERN SPEC v1
Session = sequence of EPISODES (5–20 s each) separated by TRANSITIONS.
EPISODE: choose primitive from {P1 60%, P2 20%, P4 15%, P3 5%} (weights adjustable).
  P1: N_cycles ~ U(4, 20); L_stroke ~ N(30 mm, 25%); f ~ U(1.5, 3.5 Hz);
      F_nail ~ N(0.2 N, 30%) resampled every cycle; direction drift ~ U(-20°, +20°) per 3 cycles;
      per-finger phase offset ~ U(0, 60 ms); per-finger force scale ~ U(0.7, 1.3).
  P2: N_sweeps ~ U(2, 6); L ~ U(60, 140 mm); v ~ U(50, 120 mm/s); lift between sweeps;
      alternate direction with p = 0.6, same direction with p = 0.4.
  P4: duration ~ U(2, 6 s); per-finger independent sinusoid + noise, amplitude 5–15 mm,
      f_i ~ U(3, 6 Hz) independently per finger, F ≤ 0.15 N.
  P3: optional; disable by default (massage risk).
TRANSITION: lift to clearance ≥ 15 mm above canopy; move to next region (adjacent with p = 0.8,
  random with p = 0.2); descend with force ramp 0→target over 0.3 s; optional PAUSE ~ U(0.3, 2 s) with p = 0.5.
GLOBAL: speed envelope 20–200 mm/s; force envelope per contact 0.05–0.5 N (hard limit 0.6 N);
  never hold a contact stationary under load > 0.1 N for > 1 s; never repeat an identical
  (L, f, F, direction) tuple more than 3 cycles; keep a slow-mode (v 20–50 mm/s, F ≤ 0.15 N)
  episode at least once per minute for the CT channel.
INTENSITY KNOB: scales F_nail (0.5×–1.5×) and f (0.7×–1.3×) together; does not change edge geometry.
```

---

## 5. Regional differences

| Region | Hair lie | Curvature | Sensitivity / notes | What human scratchers do |
|---|---|---|---|---|
| Crown / vertex | whorl, radiating outward (clockwise in most people) | R ≈ 85–100 mm, near-spherical, convex in all directions | high follicle density, often the most-requested spot; hair stands most upright here (exit angle highest) | short rakes in several directions around the whorl; circular P3 is tolerated here; hair tangles least because the lie is radial and strokes naturally run outward |
| Top / mid-scalp | forward with lateral fanning toward the part | R ≈ 80–100 mm sagittal, ~90 mm coronal | moderate; large flat-ish field good for P2 sweeps | front-to-back sweeps against the lie (lifts hair, reaches skin) and back-to-front with the lie (smoother); alternate |
| Sides / parietal-temporal | downward toward the ear; temple hair sweeps backward in a semicircle | vertical R 100–150 mm, nearly flat; front-back R 70–90 mm; temporal fossa slightly concave; temporalis muscle under the skin (softer substrate) | temple and above-ear are high-sensitivity (facial-nerve/trigeminal border); PDT lower than vertex | slower, lighter (0.1–0.2 N), upward strokes against the downward lie (toward the crown) feel strongest; must avoid the ear and the arm of glasses |
| Occipital / back | downward toward the nape | R ≈ 60–80 mm on the bun, convex; tightly bone-backed | tolerates the most force; highest hairy-skin innervation band (neck+scalp ~17 units/cm²) | vigorous P1 rakes, up-strokes against the lie; the "sweet spot" for many people |
| Nape / hairline-to-neck | downward, then wispy; hair shortens | concave transition R ≈ −50 to −100 mm; muscle/tendon substrate | very high sensitivity (shiver trigger), thin hair means nails are fully on skin | light, slow (2–5 cm/s), short strokes or P7 tracing; force ≤ 0.15 N; this is CT territory |
| Frontal hairline / temples | forward and down; vellus-to-terminal transition | R ≈ 80–100 mm | skin thin, nails on skin; forehead ~48 units/cm² adjacent | slow tracing P7 along the hairline; minimal force |

Adaptation rules human scratchers apply (observed; UNKNOWN in proportion): force drops ~50% going from occiput to temple/nape; speed drops at hairline/nape; stroke direction is chosen against the lie for intensity and with the lie for smoothness; the hand re-orients so the four nails sit tangent to the local surface (the hand "cups" the crown, "flattens" on the side, "hooks" under the occiput).

Design-relevant conclusions: (1) a device that only covers the occiput and crown covers the two highest-value regions and the two simplest curvatures (convex, R 60–100 mm); (2) the nape/temples are high-value but low-tolerance, demanding ≤ 0.15 N and slow speeds, and should be a separate, later experiment; (3) the hair lie is region-specific, so stroke direction must be settable per region rather than fixed.

---

## 6. Why human scratching does not tangle or pull hair

Hair is damaged when a shaft is loaded in tension (pull-out at ~0.4 N anagen, break at ~1 N) or when shafts are wound/knotted. Bending, even to 90° at the root, is harmless. Human scratching converts almost all the interaction into bending and sliding and almost none into tension or wrapping, for the following reasons; each yields a design rule.

| Mechanism in the human hand | Why it protects hair | Design rule |
|---|---|---|
| The nail is a smooth, convex, continuous edge with no re-entrant features; the plate slopes up and away from the edge at ~45° | hair that climbs onto the nail slides along the plate and off the far side; there is nothing for a loop to hook on | DR1: the scratching element must be a smooth convex profile with no concavities, holes, slots, steps or edges < 0.1 mm radius anywhere within 15 mm of the contact |
| Approach angle ~45° and the edge is the lowest point | hairs are pushed down-and-aside (bent), not scooped under | DR2: contact element enters hair canopy with the leading face at 30–60° to the scalp; nothing on the element lies closer to the scalp than the contact edge itself |
| Fingers are soft-mounted (joint compliance 0.1–1 N/mm); if a bundle resists, the nail rides up over it instead of pushing through | the maximum tension any trapped hair can see is bounded by the compliance: the nail yields before the hair does | DR3: tip compliance normal to the scalp ≤ 0.5 N/mm and a hard force ceiling ≤ 0.6 N per contact; a trapped hair must be able to lift the tip |
| Strokes are predominantly across or against the lie with lift-off and a short return, or with the lie; direction reversals happen with a momentary force dip | at reversal the edge pivots in place; hairs bent ahead of it straighten and pass over as load drops; a hair never gets dragged a full stroke in both directions under load | DR4: reciprocating motion must unload (≥ 50% force reduction, or full lift) at each reversal; never reverse under full load |
| Nails are 16–28 mm apart with open-ended gaps between fingers | a hair that enters the gap between two fingers can leave by the same open path; no closed aperture | DR5: no closed apertures, gaps or pinch lines anywhere hair can reach; any gap between moving parts must be either < 0.3 mm (hair cannot enter) or > 10 mm and open-ended |
| No rotating parts; every motion is a bounded reciprocation or translation of a finite stroke | rotation is what winds hair; a shaft can only wrap around something that turns a full revolution relative to it | DR6: no continuously rotating surface within reach of the hair canopy (reach = hair length + 20 mm); rotary drives must be fully enclosed with hair exclusion |
| Fingers lift between bouts and regions | any hair draped over a nail is released every few seconds | DR7: full lift-off (clearance above the canopy) at least every 10–20 s and at every region change |
| Scratching edge is dry and hard; hair slides on keratin at μ ≈ 0.2–0.3 | low friction means hair slides along the edge instead of being carried with it | DR8: tip material hard (E > 1 GPa) with a polished finish (Ra < 1 µm); no elastomer at the edge, which grabs hair (μ > 1) |
| The hand feels the pull and stops | closed-loop; a snag is felt in < 100 ms | DR9: a snag must be detectable (force/current) and must produce an immediate unload/retract; mechanical breakaway preferred |
| Speed is modest (< 20 cm/s) | hairs have time to bend and slide; no whipping | DR10: cap velocity at ~20 cm/s in-hair |

Failure modes to carry into safety review: (a) an edge that is too sharp (< 0.05 mm) cuts hair at the bend point rather than deflecting it; (b) an edge that is too blunt/soft (> 1 mm, elastomer) grabs bundles and drags; (c) parallel tines at pitch < 5 mm act as a comb and load long hair in tension when the comb reverses with hair threaded through it; (d) a contact that moves while stationary in its own frame (e.g. a spinning ball) winds hair.

---

## 7. Sensation-critical variables, ranked

Scores: importance = expected effect on "feels like a person scratching" (5 = decisive); uncertainty = how little we know about the right value (5 = no data). Priority for prototype adjustability = importance × uncertainty.

| Rank | Variable | Importance | Uncertainty | Priority | Must be adjustable in SP1? |
|---|---|---|---|---|---|
| 1 | Pattern irregularity (phase, force, length, direction jitter; region changes; pauses) | 5 | 5 | 25 | yes, in software; include "fully periodic" as a control condition |
| 2 | Tip reaches skin through hair (penetration depth / canopy engagement) | 5 | 4 | 20 | yes: tip height/force preload adjustable; interchangeable tips of different reach |
| 3 | Normal force per contact (0.05–0.6 N) | 5 | 3 | 15 | yes, continuously, with readout |
| 4 | Stroke velocity (2–20 cm/s) | 4 | 3 | 12 | yes |
| 5 | Edge geometry: radius (0.05–0.5 mm), contact length (2–8 mm), angle (25–65°) | 4 | 3 | 12 | yes, via tip swap and angle adjustment |
| 6 | Number of simultaneous contacts (1–5) and their asynchrony | 4 | 3 | 12 | yes, at least 1 vs 4 and locked vs independent phase |
| 7 | Tip compliance (0.1–1 N/mm) | 4 | 3 | 12 | yes, via spring swap |
| 8 | Stroke direction relative to hair lie (with / across / against) | 3 | 4 | 12 | yes, by orientation of module on head |
| 9 | Stroke length (1–15 cm) | 3 | 3 | 9 | yes |
| 10 | Reciprocation frequency (1–4 Hz) | 3 | 2 | 6 | yes (coupled to length/velocity) |
| 11 | Contact spacing (16–28 mm) | 2 | 3 | 6 | nice-to-have (two spacings) |
| 12 | Tip material/finish (keratin-like hardness, μ) | 3 | 2 | 6 | yes, via tip swap |
| 13 | Region covered (crown/occiput vs sides/nape) | 3 | 2 | 6 | yes, by repositioning the module |
| 14 | Dwell per region / time-in-region | 2 | 3 | 6 | software |
| 15 | Sound (presence/level of scratch hiss, motor noise masking) | 2 | 3 | 6 | test with ear plugs/white noise, not a build variable |
| 16 | Thermal (tip temperature) | 1 | 2 | 2 | no (note: cold metal tips will feel alien; pre-warm or use low-conductivity polymer) |

---

## 8. Massager-vs-scratcher test criteria

Apply to any proposed mechanism before it enters the tournament. Score each item PASS / FAIL / UNSURE. Any FAIL on items 1–6 means the design will not produce scratching regardless of the rest.

1. Edge, not pad. Contact element is a stiff (E > 1 GPa) edge with radius 0.05–0.5 mm and contact length 2–8 mm. FAIL if the contact is a dome/pad ≥ 2 mm radius or any elastomer with hardness < Shore D 60 at the contact.
2. Reaches the skin. In medium-length hair (5–10 cm) the edge contacts the scalp surface for ≥ 40% of stroke length at ≤ 0.3 N. FAIL if the element rides on the canopy (brush) or cannot get below 2 mm above the skin.
3. Light. Normal force per contact 0.05–0.5 N (hard ceiling 0.6 N); total scratch load ≤ 2.5 N. FAIL if the design needs > 1 N per contact to function or is force-controlled only by the user's head weight/strap tension.
4. Slides. Each contact translates ≥ 10 mm across the skin per cycle with slip at the interface (scalp displacement over skull < 1 mm). FAIL if the skin moves with the contact (massage) or if the motion is predominantly normal to the skin (tapping/vibration).
5. Right speed band. Tangential velocity 2–20 cm/s; dominant motion frequency 1–4 Hz. FAIL if there is a sustained component > 20 Hz at the contact (vibration) or if sliding speed exceeds 30 cm/s (flicking/brushing).
6. Deflects hair near the root. Hair engagement happens within ~5 mm of the skin; the element parts the canopy. FAIL if hair is only displaced at its free length (comb/brush) or compressed as a mat.
7. Multiple independent contacts. 3–5 contacts at 16–28 mm pitch that are not rigidly phase-locked (compliance or independent drive gives ≥ 20 ms spread and ≥ 20% force spread). UNSURE is acceptable for SP1 if a single contact is used as a deliberate experiment.
8. Irregular. The control can vary stroke length, speed, force, direction and location with the jitter in section 4.4 and includes pauses and lift-offs. FAIL if the mechanism is kinematically fixed (cam/crank with no adjustable stroke, no lift) unless the fixedness is explicitly the control-condition experiment.
9. Compliant at the tip. Tip stiffness normal to the scalp ≤ 0.5 N/mm with a travel of ≥ 5 mm so the contact follows curvature (R 60–150 mm) and head motion without force spikes. FAIL if force rises > 0.3 N per mm of surface error.
10. Unloads at reversal and lifts between bouts (DR4, DR7). FAIL if the contact reverses under full load or never leaves the hair.
11. Hair-safe geometry (DR1, DR5, DR6, DR8). FAIL if any rotating surface or closed aperture is within reach of the hair.
12. Sounds like a scratch, not a motor. Scratch hiss audible; motor/gear noise < the scratch noise at the ear. UNSURE acceptable for SP1.

Quick sanity test for engineers: draw the contact footprint, force and velocity of your mechanism on the table in section 1.2. If the row it lands in is not the first column, it is not a scratcher.

---

## 9. Open questions only physical testing can answer

1. Skin contact necessity. Does the pleasure require the edge to touch the skin, or is near-root hair deflection alone (edge held 1–2 mm above the skin) sufficient? Test: same stroke with tip height stepped 0, 1, 2, 5 mm above skin.
2. Preferred velocity on the scalp. Does the CT optimum (~3 cm/s) or the self-scratch speed (~12 cm/s) win on the scalp, and does the answer differ by region? Test: 2, 5, 10, 15, 20 cm/s at fixed force.
3. Force–pleasure curve and ceiling. Where between 0.05 and 0.6 N per contact does pleasure peak, and where does it turn into discomfort over a 10-minute session? Instrument the tip.
4. Contact count and asynchrony. Does one perfect contact feel like a scratch at all, or is the 4-contact asynchrony essential? Test: 1, 2, 4 contacts; locked vs. jittered phase.
5. Predictability penalty. How quickly does a perfectly periodic pattern lose its effect (seconds? minutes?), and which jitter dimension (force, phase, direction, location) restores it most cheaply?
6. Edge geometry. Which radius (0.05/0.15/0.3/0.5 mm), contact length (2/4/8 mm) and angle (30/45/60°) feel most "nail-like"? Which materials (acetal, nylon, PLA, PETG, polished aluminium, real-nail-like keratin substitutes) are indistinguishable from a nail?
7. Direction vs. hair lie. Across, against or with the lie: pleasure and snag rate for the tester's actual hair.
8. Penetration vs. hair length and density. Quantify fraction of stroke in skin contact for the tester's hair; define what "reaching the skin" requires in force and tip reach.
9. Sound contribution. Same stimulus with and without ear plugs/white-noise masking.
10. Habituation over 20 minutes. Does pleasure fade, and does region rotation (section 4.2 dwell) prevent it?
11. Scalp tolerance to repeated passes. Any erythema, tenderness or abrasion after 10 / 20 / 30 min at 0.3 N; defines the real abrasion ceiling (section 3.24 is UNKNOWN).
12. Hair damage audit. Count shed hairs on a dark cloth after each session versus a baseline hair-pull test; defines the practical pull/snag rate of the mechanism.
13. Human reference measurement. Before trusting any of section 3, have a person scratch an instrumented head (thin-film force sensors under a wig, or FSRs on a headband) to get actual per-nail force, speed and rhythm. This single afternoon of measurement would convert most ESTIMATED rows to KNOWN and is the highest-value experiment in the program.

---

## 10. Sources used

Scratch force/velocity/power (self-scratch, forearm, instrumented tablet): Multimodal sensing ring for scratch intensity, Communications Medicine 2023 — https://www.nature.com/articles/s43856-023-00345-2 ; preprint https://arxiv.org/pdf/2302.03813 (forces 0.36 ± 0.23 / 0.66 ± 0.29 / 1.56 ± 0.58 N; velocities 112 / 136 / 178 mm/s; power mostly 0–200 mW).
Scratch pleasantness stimuli (0.1–0.3 N, 1–5 Hz brush scratching): Yosipovitch group reviews — https://journals.physiology.org/doi/full/10.1152/jn.00374.2013 ; https://www.sciencedirect.com/science/article/pii/S0022202X1533949X ; https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0082389
Topography of scratching pleasure: bin Saif et al. 2012 — https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1365-2133.2012.10826.x ; https://www.sciencedaily.com/releases/2012/01/120127135712.htm
Scratch inhibits spinal itch neurons: https://www.nature.com/articles/nn.2292 ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3144926/
Scratch vs tickle review (2026): https://www.jidonline.org/article/S0022-202X(25)03615-2/abstract
C-tactile velocity tuning (1–10 cm/s, peak ~3): https://iasat.org/about/affective-touch/ ; https://www.sciencedirect.com/science/article/abs/pii/S0166432815302114 ; https://www.sciencedirect.com/science/article/abs/pii/S0166432816311585
CT afferent–hair follicle coupling in humans (2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12369303 ; https://physoc.onlinelibrary.wiley.com/doi/full/10.1113/JP287706
Lanceolate endings in human scalp follicles: https://pmc.ncbi.nlm.nih.gov/articles/PMC10184541/ ; mechanical stimulation of scalp follicle cells activates sensory neurons: https://www.science.org/doi/full/10.1126/sciadv.adh3273
Hairy-skin unit types, hair units innervate ~25 follicles: Vallbo et al. 1995 — https://physoc.onlinelibrary.wiley.com/doi/10.1113/jphysiol.1995.sp020622 ; review "Hairy Sensation" — https://journals.physiology.org/doi/full/10.1152/physiol.00059.2012
Innervation densities (neck+scalp ~17 units/cm², forehead 48): Corniani & Saal 2020 — https://journals.physiology.org/doi/full/10.1152/jn.00313.2020 (open PDF https://eprints.whiterose.ac.uk/id/eprint/166148/8/jn.00313.2020.pdf)
Mechanoreceptor classes/adaptation: https://www.ncbi.nlm.nih.gov/sites/books/NBK541068/
Fingernail modulus/thickness: https://onlinelibrary.wiley.com/doi/full/10.1111/srt.13456 ; https://www.researchgate.net/publication/24311004_Tensile_and_shear_properties_of_fingernails_as_a_function_of_a_changing_humidity_environment
Fingernail transverse curvature radii: https://files01.core.ac.uk/download/pdf/8778792.pdf ; nail configuration https://pmc.ncbi.nlm.nih.gov/articles/PMC4659990/
Fingertip pulp stiffness: https://pmc.ncbi.nlm.nih.gov/articles/PMC13038334/ ; https://pubmed.ncbi.nlm.nih.gov/9796686/
Hair density by ancestry: https://pmc.ncbi.nlm.nih.gov/articles/PMC6219221/ ; hair diameter https://hairstylecamp.com/which-ethnicity-has-thickest-and-thinnest-hair/
Hair mechanical properties: https://www.sciencedirect.com/science/article/pii/S0928493116319208 ; https://www.triprinceton.org/single-fiber-tensile-experiments
Hair extraction force (anagen 0.36 N, telogen 1.8 N): https://pubmed.ncbi.nlm.nih.gov/11182122
Hair direction by region and exit angle 10–60°: https://ilht.com/hair-directions/ ; https://en.wikipedia.org/wiki/Hair_whorl ; https://hairdoctornyc.com/hair-transplant-for-vertex-coverage/
Scalp pressure discomfort threshold (190.7 kPa): https://www.sciencedirect.com/science/article/pii/S0003687022002423
Scalp skin thickness: https://pmc.ncbi.nlm.nih.gov/articles/PMC12445948/ ; https://xyonhealth.com/blogs/library/scalp-anatomy
Skin friction coefficients: https://link.springer.com/article/10.1007/s11249-011-9854-y ; head/hair-on-helmet friction https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11402834/
Head dimensions: https://www.ijcap.org/html-article/22334 ; https://www.researchgate.net/publication/264024487_Analysis_of_Human_Head_Shapes_in_the_United_States
ASMR triggers (scratching, personal attention, unpredictability): https://www.sciencedirect.com/science/article/pii/S1053810023001216 ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4380153/
Mouse scratch kinematics (6 Hz; NOT a human reference): https://www.sciencedirect.com/science/article/pii/S0896627321005419
