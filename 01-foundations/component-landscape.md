# PROJECT SCRATCH — Component Landscape (Actuators, Hardware, Electronics, Sourcing)

**Author:** Actuator & Component Sourcing Specialist
**Date:** 2026-10-01
**Status:** Foundations input for mechanism teams. Prices are US retail, checked by web search in Sept/Oct 2026 unless marked. Anything marked **(~unverified)** is my estimate from memory or a range seen in listings I could not confirm; treat those as ±30 %.

---

## 0. How to read this document

The mechanism teams need to pick parts that satisfy a narrow physical envelope:

| Requirement | Target | What it implies for part selection |
|---|---|---|
| Normal force at tip | 0.2–2 N (20–200 gf) | Torque needed is tiny: 2 N on a 50 mm lever = **0.1 N·m = ~1 kg·cm**. Almost any motor has enough torque; the problem is *controlling* and *limiting* a small force, not generating it. |
| Stroke | 1–5 cm | At a 50 mm lever that is 10–60° of swing; a rotary actuator with a lever or crank is adequate. Linear actuators must give ≥50 mm. |
| Cycle rate | 0.5–4 Hz | At 4 Hz × 5 cm reciprocating, peak tip speed ≈ 0.6 m/s. Hobby servos (0.1–0.15 s/60°) can just do it; micro linear actuators (6–28 mm/s) **cannot**. |
| Noise | "reasonable", near the ears | Gear whine and stepper hiss are the main offenders. FOC-driven gimbal motors and good smart servos are quietest; cheap metal-gear servos (MG996R-class) buzz. |
| Mounting | head-mounted or frame-mounted | Head-mounted: every actuator counts (XL330 = 18 g; NEMA 17 = 280 g). Frame-mounted: weight is irrelevant and a cable/Bowden drive can keep motors off the head. |
| Hair nearby | yes | No exposed rotating shafts/pinions/belts near the scalp; prefer enclosed gearboxes and shrouded linkages. |
| Safety | mechanical first | Favor back-drivable actuators, current-limited drivers, series springs, magnetic breakaways, and a hardware e-stop in the actuator power rail. |

**Bottom line up front.** For a one-off research rig: (1) **smart serial-bus servos with current/torque limiting** (Dynamixel XL330 or Feetech STS3215) are the best default actuator — position + current control, daisy-chain wiring, 4096-count feedback, and a software torque ceiling that acts as an electronic clutch; (2) **gimbal BLDC motors under SimpleFOC** are the best candidate when smoothness and genuine force control matter most — silent, back-drivable, direct-drive; (3) **cheap hobby servos** are fine for first "does the motion feel right?" mock-ups but must be paired with a series spring or magnetic breakaway because they have no force sense and are not back-drivable.

---

## 1. Rotary actuators

### 1.1 Hobby PWM servos

| Part | Key specs | Price (US) | Source | Pros / cons for this application |
|---|---|---|---|---|
| **SG90** (plastic micro) | 1.8 kg·cm @4.8 V, 0.1 s/60°, 9 g, 180°, analog, deadband ~10 µs | ~$2–3 ea in 5–10 packs **(~unverified)** | Amazon | + Dirt cheap, light, ok torque for 1 N at a 10 cm lever. − Plastic gears strip when you fight the scalp, jittery, audible whine, poor centering (~2–3° slop). Fine for a cardboard mock-up only. |
| **MG90S** (metal micro) | 2.0–2.2 kg·cm @4.8 V, 0.08–0.10 s/60°, 13.4 g, 5 µs deadband | $2.59 single, ~$12–15 per 4–5 pack ([Amazon](https://www.amazon.com/Helicopter-Arduino-Raspberry-Project-MakerDoIt/dp/B07FLXZ1VK)) | Amazon | + Best cheap head-mounted servo: light, metal gears, fast enough for 4 Hz. − Noisy gear whine, no force sense, not back-drivable (scalp contact = stall → heat). Pair with series spring. |
| **MG996R** (standard metal) | 9.4 kg·cm @4.8 V / 11 kg·cm @6 V, 0.17/0.14 s/60°, 55 g, 5 µs deadband ([spec](https://servodatabase.com/servo/towerpro/mg996r)) | ~$8–11 ea ([TowerPro MG996R ~$10.95](https://thinkrobotics.com/products/standard-metal-servo-mg996)) | Amazon, SparkFun | + Ubiquitous, torque overkill. − Famous for buzz/hunting at rest, ~1° jitter, heavy for the head, 55 g each; the torque is a liability (can push 10 N through a scalp before anything limits it). Not recommended near the head without a force limiter. |
| **DS3218 / DS3225** (20/25 kg digital) | 20 kg·cm @6.8 V, 0.14 s/60°, 60 g, 3 µs deadband, 180° or 270° ([spec](https://servodatabase.com/servo/miuzei/ds3218)) | ~$14.81 ea; Amazon 4-packs ~$30–40 **(~unverified)** ([Amazon](https://www.amazon.com/Waterproof-Digital-Arduino-Crawler-Control/dp/B07MH1QRK5)) | Amazon | + Precise, tight deadband, good for a frame-mounted carriage drive. − Far more torque than needed; needs 6–7.4 V UBEC; loud at speed; heavy. |
| **FS90R / FS5103R continuous rotation** | Speed-only control via PWM; ~1.5–3 kg·cm | ~$8–12 | Adafruit, Pololu | + Simplest crank drive (no driver board). − Crude open-loop speed, drift, same gear noise. An N20 gearmotor + DRV8871 is better. |

**Notes on hobby servo behaviour relevant to scratching.** Position resolution is set by pulse width: typical libraries give 1 µs = ~0.09°; analog servos actually resolve ~0.5–1°. Analog servos update at 50 Hz, so the fastest *smooth* commanded trajectory is ~10–20 waypoints per stroke at 2–4 Hz — adequate. Deadband is what makes a servo "hunt" or buzz under load; cheaper analog servos (SG90) are worst. **None of them is back-drivable** (worm-less spur trains with 200–300:1 ratio plus PID holding), so when the tip meets the scalp the servo keeps pushing until the error is zero — force rises to stall unless a spring, breakaway or current limit intervenes. That is the single most important reason to treat hobby servos as mock-up parts, not the SP1 default.

### 1.2 Smart serial-bus servos (position + current control) — recommended default

| Part | Key specs | Price | Source | Pros / cons |
|---|---|---|---|---|
| **Dynamixel XL330-M288-T** | 5 V (3.7–6 V), 0.52 N·m stall (5.3 kg·cm), 103 rpm no-load, 1.47 A stall, 18 g, 20×34×26 mm, 4096-count absolute, modes: current, velocity, position, **current-based position**, PWM; TTL half-duplex daisy chain ([Robotis](https://www.robotis.us/dynamixel-xl330-m288-t/)) | **$27.49** ([Robotis US](https://www.robotis.us/dynamixel-xl330-m288-t/)), $23.90 intl | robotis.us, Trossen | + Lightest actuator with true current (torque) limiting; quiet plastic gears; rich firmware (velocity/accel profiles, goal-current ceiling = electronic clutch); 2 wires for 6 servos. − Plastic gears strip if you crash them hard; 5 V bus is unusual (needs 5 V 4 A supply); needs a bus adapter. |
| **Dynamixel XL330-M077-T** | Same package, lower ratio: 0.22 N·m, 258 rpm | ~$27 **(~unverified)** | robotis.us | + Faster, smoother for low-force strokes at 4 Hz. − Less holding torque (still 2× what we need at a 5 cm lever). |
| **Dynamixel XL430-W250-T** | 12 V, 1.5 N·m, 57 rpm, 57 g, metal gear | **$49.90** ([Trossen](https://www.trossenrobotics.com/dynamixel-xl430-w250-t.aspx)) | Trossen, robotis.us | + 12 V bus (same PSU as everything else), tougher. − Heavier, slower, pricier; overkill torque. Good for a frame-mounted carriage. |
| **Feetech STS3215 (7.4 V, 19.5 kg·cm)** | 7.4 V, 1.9 N·m stall, 0.5 N·m rated, 12-bit magnetic encoder, 360° multi-turn, torque limit + current/position/temp feedback, TTL bus, 55 g | **$14–20 ea** ([Seeed $20](https://www.seeedstudio.com/STS3215-19kg-cm-7-4V-Serial-Servo-p-6338.html); Amazon 6-packs ~$90–110 **(~unverified)** ([Amazon](https://www.amazon.com/RCmall-High-Torque-Magnetic-Feedback-Function/dp/B0FQHCV9GP))) | Amazon, Seeed, Waveshare, RobotShop | + Half the price of XL330 with comparable features; huge community (LeRobot SO-100/SO-101 arms use it); configurable torque limit. − 55 g; metal gears are audibly whiny; torque is 4× what we need so the *software* limit is doing all the safety work. |
| **Feetech STS3215 (12 V, 30 kg·cm)** | as above, 12 V | $23.99 ([Seeed](https://www.seeedstudio.com/STS3215-30KG-Serial-Servo-p-6340.html)) | Seeed | Same comments; 12 V convenience. |

**Bus adapters:** Waveshare *Bus Servo Adapter (A)* **$4.99** ([Waveshare](https://www.waveshare.com/bus-servo-adapter-a.htm)) or Waveshare *Servo Driver with ESP32* **$14.97–15.99** (ESP32 + bus driver + power in one board, [Waveshare](https://www.waveshare.com/servo-driver-with-esp32.htm)) for Feetech; Robotis **OpenRB-150** **$24.90–28.64** (Arduino-compatible SAMD21 with Dynamixel bus + power pass-through, [Robotis](https://www.robotis.us/openrb-150/)) or **U2D2** **$32.10** ([Trossen](https://www.trossenrobotics.com/dynamixel-u2d2.aspx)) for Dynamixel.

**Why these matter for safety:** "current-based position control" lets you command a position but cap the current — the servo stops pushing at a set torque, and you can read back current to detect contact. That is a software clutch, which the brief explicitly prefers to be backed by a mechanical one, but it is a strong second layer and makes the force an *adjustable experimental variable* via a knob.

### 1.3 DC gearmotors

| Part | Key specs | Price | Source | Pros / cons |
|---|---|---|---|---|
| **N20 micro metal gearmotor (generic)** | 6 V or 12 V, 10–1000 rpm variants, 10–12 mm gearbox, ~10 g | ~$2–4 ea on Amazon 6-packs **(~unverified)**; AliExpress ~$1.50 | Amazon, AliExpress | + Cheapest crank/cam drive; 100–300 rpm versions give 1.5–5 Hz directly. − Gear whine, ±20 % rpm scatter, no feedback, D-shaft 3 mm. |
| **Pololu Micro Metal Gearmotor HP 6 V (100:1, 150:1, 210:1, 298:1)** | 100:1 HP = 320 rpm, 1.1 kg·cm stall; 298:1 = 100 rpm, ~2.5 kg·cm | $23.95 (100:1 HP, [Pololu](https://www.pololu.com/product/1101)); with 12 CPR magnetic encoder ~$30 **(~unverified)** ([Pololu](https://www.pololu.com/product/5173)) | Pololu | + Characterised, consistent, encoder option → closed-loop crank phase; same footprint as generic N20. − 5–10× generic price; same noise. For crank drives at 0.5–4 Hz pick 150:1–298:1 at 6 V and PWM down. |
| **Pololu 37D gearmotor w/ 64 CPR encoder** | 12 V, 10:1–150:1, up to 30 kg·cm, 200 g+ | $60.95 ([Pololu](https://www.pololu.com/product/4755)) | Pololu | Overkill, heavy, loud. Only for a frame-mounted large-stroke carriage. Not recommended. |
| **Coreless DC motors** (7–12 mm, Nfpshop etc.) | high rpm, ~1–10 mN·m | $1–8 ([NFP](https://nfpshop.com/product/12mm-coreless-dc-motor-12v-coreless-dc-motor)) | NFP, AliExpress | Only useful as a tiny vibrator (e.g., to add "texture" to a tip). Not a scratch drive. |

### 1.4 Steppers

| Part | Key specs | Price | Driver | Pros / cons |
|---|---|---|---|---|
| **28BYJ-48 + ULN2003** | 5 V, 64:1 gear, 300 gf·cm pull-in, max ~15 rpm, <35 dB spec ([spec](https://shop.controllerstech.com/products/28byj-48-stepper-motor-and-uln2003-stepper-motor-driver)) | $2–8 w/ driver | ULN2003 (included) | + Cheap, quiet, geared. − Too slow for >1 Hz strokes, unipolar (no microstepping without mods), lots of backlash. |
| **NEMA 17 (StepperOnline 40–45 N·cm)** | 1.5–2 A, 1.8°, 280–350 g | $10.99–15 ([Amazon/StepperOnline](https://www.amazon.com/Stepper-Motor-Bipolar-64oz-Printer/dp/B00PNEQI7W)) | TMC2209 | + Precise, open-loop position, proven with belts/lead screws. − Heavy (frame-mount only), stalls silently unless StallGuard; "singing" at some speeds. |
| **NEMA 11 / NEMA 8** | 6–12 N·cm / 1.5–3 N·cm, 100–150 g / ~40 g | $15–30 **(~unverified)** | TMC2209 | Smaller, still heavy relative to XL330, torque marginal for NEMA 8. |
| **TMC2209 stepstick** | 2 A rms, StealthChop (near-silent), **StallGuard4** sensorless stall detection via UART ([BTT](https://www.amazon.com/BIGTREETECH-TMC2209-Stepper-Stepstick-Motherboard/dp/B07ZPYKL46)) | ~$4–8 ea in 4–5 packs **(~unverified)** | — | StallGuard = collision detection = a credible software force limit for a stepper-driven carriage. A4988 ($2) is louder and has no stall detection; skip it. |

Steppers belong to the **frame-mounted carriage** family of designs (e.g., a MGN9 rail with GT2 belt). They are the worst fit for anything on the head.

### 1.5 Brushless gimbal motors + FOC — the smoothness candidate

Gimbal motors are high-pole-count, high-resistance outrunners made to hold a camera still; with Field-Oriented Control they give **silent, cog-free, back-drivable, direct-drive** motion, and torque is proportional to current, so you get force control for free. SimpleFOC (Arduino library) makes this a two-evening setup rather than a research project.

| Part | Key specs | Price | Source | Notes |
|---|---|---|---|---|
| **Makerbase / generic GM2804 + AS5600 encoder** | 12 V, ~300 g·cm (0.03 N·m) peak ([AliExpress](https://www.aliexpress.com/i/1005005065257355.html)), 28 mm, ~40 g, 7 pole-pair | $12.91 (AliExpress) / **$18.90** ([DFRobot](https://www.dfrobot.com/product-3005.html)); Amazon kit w/ driver ~$30–40 **(~unverified)** ([Amazon](https://www.amazon.com/Brushless-Outrunner-Magnetic-Encoder-SimpleFOCmini/dp/B0FXKN9YMJ)) | 0.03 N·m at a 20–30 mm lever = 1–1.5 N — exactly our force band, and it can't hurt you even at stall. |
| **iPower GM3506** (optionally with AS5048A encoder) | 600–1000 g·cm (0.06–0.1 N·m), 40 mm, ~60 g | $23.99 / $41.90 w/ encoder ([iFlight](https://shop.iflight.com/ipower-motor-gm3506-brushless-gimbal-motor-w-as5048a-encoder-pro1155)) | iFlight, Amazon | 2 N at a 50 mm lever with margin. Best size/torque match for a direct-drive finger. |
| **iPower GM4108H-120T** | ~0.1–0.15 N·m **(~unverified)**, 45 mm | $43.90 | iFlight | Bigger than needed; frame-mount. |
| **SimpleFOC Mini v1** (DRV8313, 3 A peak / <2 A continuous without heatsink) | 8–24 V, 26×21 mm | ~€12–20 / ~$15–20 ([SimpleFOC](https://simplefoc.com/simplefoc_mini_product_v1), [Amazon](https://www.amazon.com/SimpleFOC-Dual-Channel-Brushless-Controller-Automation/dp/B0GQPS4MG9)) | one per motor | No current sensing on the Mini: torque control is "voltage mode" (open-loop current estimate), which is adequate for a gimbal motor's high resistance. |
| **SimpleFOC Shield v3** (two motors, with current sense) | 5 A, inline current sensing | ~$35–45 **(~unverified)** | simplefoc.com, Mouser | Real current-mode torque control; Arduino Uno/ESP32 form factor. |

**Honest trade-offs.** + Silent (no gears at all), truly smooth at 0.5–4 Hz, force-controllable, back-drivable (you can push the finger away by hand), and a stall is harmless because peak torque is tiny. − You need an encoder per motor (AS5600 I²C is included on the kits; use SPI AS5048A if you run >2 motors), you must calibrate pole pairs and tune PID, continuous holding force heats the motor (keep < ~1 A), and the torque is low enough that the finger lever must be short (≤50 mm) or the motor must be geared (which gives back the noise). SimpleFOC community threads confirm closed-loop slow, smooth position control with these motors is routine ([community](https://community.simplefoc.com/t/experience-with-high-resistance-gimbal-motors-for-smooth-slow-closed-loop-motion/8306)). **Recommendation:** make one gimbal-motor "finger" module a parallel experiment to the smart-servo module; the sensory difference between geared-servo motion and direct-drive FOC motion may be exactly what distinguishes "machine" from "fingernails".

---

## 2. Linear actuators

| Option | Key specs | Price | Verdict |
|---|---|---|---|
| **Actuonix PQ12-R** | 20 mm stroke; 18 N @28 mm/s or 50 N @10 mm/s; 15 g; RC-PWM input ([Actuonix](https://www.actuonix.com/pq12-r)) | **$65–70** | Too short and too slow: 20 mm at 28 mm/s ≈ 0.7 Hz max. Lead-screw whine. No. |
| **Actuonix L12-R (50 or 100 mm, 50:1/100:1)** | 12–25 mm/s, 22–42 N; L16 up to 100 mm | **$70–90** ([Actuonix](https://www.actuonix.com/l12)) | 100 mm/s would be needed for 2 Hz × 50 mm; L12 tops out at 25 mm/s. No. |
| **Push/pull solenoids** | binary, 5–20 N snap, click | $5–15 | Binary and loud; the opposite of a nail stroke. No (except perhaps a "tap" experiment). |
| **Voice coil actuators** (BEI Kimco, Thorlabs VC063) | 1–10 N, 5–15 mm stroke, back-drivable, force ∝ current ([Thorlabs](https://www.thorlabs.com/voice-coil-actuators)) | **$150–200+** ea | Sensorially ideal (pure force control, silent) but no cheap hobby source. Cheap hacks: the arm actuator from a dead 3.5" hard drive (free; ~0.1–0.5 N·m over ~30°), or a 2–3" speaker driver with a pushrod (~$5, ~1–3 N, ~5 mm). Worth one afternoon as a "normal-force modulator" riding on a rotary stroke; not the primary stroke drive. |
| **Lead-screw + stepper (T8×8 or T8×2 w/ NEMA 17)** | 8 mm/rev × 300 rpm = 40 mm/s | $15–25 for screw+nut+coupler | OK for a frame-mounted slow-stroke carriage; audible; back-drivability depends on lead. |
| **Belt-driven carriage (GT2 + MGN9 rail + NEMA 17/TMC2209)** | fast (hundreds of mm/s), quiet with StealthChop | ~$45–60 | Best *linear* option if frame-mounted; see §4. |
| **Rack-and-pinion from a servo** | 3D-printed rack + pinion on MG90S/XL330 | print cost only | Cheap and compact; backlash and open gear teeth near hair are the concerns — enclose it. |
| **Cam / crank / Scotch-yoke from a rotary motor** | stroke = 2 × crank radius; sinusoidal velocity; adjustable by moving the crank pin | print cost + one N20 or servo | **The cheapest, quietest way to get reciprocation**; an N20 at 150–300 rpm gives 2.5–5 Hz directly, and a slotted crank gives adjustable stroke. Combine with a spring-loaded follower for compliance. Strongly recommended for a first "stroke feel" rig. |

---

## 3. Compliance and force-limiting hardware

The brief asks for mechanical force limiting ahead of software. Options, cheapest first:

| Element | Example part | Price | How to use it here |
|---|---|---|---|
| **Compression spring assortment** | Amazon 200–300 pc stainless assortment (wire 0.3–1.2 mm) **(~$10–15, unverified)**; McMaster [compression spring assortments](https://www.mcmaster.com/products/compression-spring-assortments/) ~$30–80 **(~unverified)** | $10–80 | Series element between actuator and tip: pick a rate so 2 N = 5–10 mm of travel (k ≈ 0.2–0.4 N/mm). A spring that soft also filters servo jitter — a feature. |
| **Extension spring assortment** | Amazon 200-pc **(~$10, unverified)** | $10 | Return springs for cam followers; preload for a magnetic breakaway. |
| **Torsion spring assortment** | 80–120 pc stainless, 60/90/120/180° ([Amazon](https://www.amazon.com/Assortment-Torsional-Stainless-Rust-Resistant-Mechanical/dp/B0F9PLNYYF)) | $11–17 | Compliant "knuckle" at the base of a printed finger; sets the normal-force ceiling. |
| **Constant-force spring** | Vulcan / McMaster small CF springs, 0.25–0.5 in wide, 0.5–5 lb | ~$5–15 ea **(~unverified)** | Gives a near-constant preload over a long travel — good for a hand-adjustable "pressure" setting of a floating module against the head. |
| **TPU / silicone elements** | TPU 95A printed flexures (any print service), silicone tubing 3–6 mm ID ($6–8), 1–3 mm silicone sheet ($8–12) | $6–12 | Living hinges, nail-tip cushions, flexible finger shafts. TPU prints are available from JLC3DP/Craftcloud. |
| **Magnetic breakaway** | K&J **D41** ¼"×1/16" N42: 1.19 lb (5.3 N) pull, **$0.28** ([K&J](https://www.kjmagnetics.com/d41-neodymium-disc-magnet)); **D61** 3/8"×1/16": 2.12 lb (9.4 N), **$0.49** ([K&J](https://www.kjmagnetics.com/d61-neodymium-disc-magnet)); D42, D52 for intermediate values | <$1 ea | Magnet pair holding the tip/finger to its carrier; separates at a set force. Remember the *shear* breakaway is ~1/3–1/5 of the axial pull figure; put a shallow printed cup around the magnet to make the direction deterministic. Steel washers (McMaster, or Amazon 10 pk ~$5) as the mating half halve the cost. |
| **Slip / friction clutch (small shaft)** | Industrial adjustable 6–8 mm bore units start at ~$98 ([Ondrives](https://www.ondrivesus.com/friction-clutches-adjustable-fixed-torque/component-mount-up-to-266-inlb/279.25.28)) — too much. DIY: 2 felt or PTFE washers + a wave washer + M6 nyloc nut on a printed hub, tune by nut torque; or a rubber O-ring friction drive on a servo horn | $3–8 DIY | Our torque band (0.05–0.1 N·m) is below what commercial limiters are made for, so DIY is actually the right answer. |
| **Magnetic coupling (DIY torque limiter)** | 2 printed discs each carrying 4–6 D41/D61 magnets, 1–2 mm air gap | ~$5 | Contactless torque limit, no wear, and the slip torque is tuned by gap. A good match for a gimbal-motor or N20 crank. |
| **Electronic clutch** | Dynamixel goal-current / Feetech torque-limit register; DRV8871 ILIM; TMC2209 StallGuard | $0 | Second layer, never the only layer. |

---

## 4. Motion hardware

| Item | Spec / part | Price | Source | Notes |
|---|---|---|---|---|
| Shafts | 3, 4, 6, 8 mm hardened ground rod, 100–300 mm (Amazon 2-packs) | ~$8–14 **(~unverified)**; McMaster precision 8 mm ~$10/300 mm **(~unverified)** | Amazon, McMaster | 3–4 mm for finger pivots; 8 mm only for a frame carriage. |
| Linear ball bearings | **LM8UU** 8×15×24 mm | $1.89 ([Prusa](https://www.prusa3d.com/product/linear-bearing-lm8uu/)) – $2.95 ea; LM6UU similar | Prusa, Amazon, Adafruit ($1.95 **(~unverified)**) | Rattly on cheap rod; igus RJ4JP-01-08 plastic drylin bushings (~$2–3) are *silent* — prefer those near the head. |
| Ball bearings | 608ZZ (8×22×7) 10 pk ~$8; 623ZZ (3×10×4) 10 pk ~$7; MR63/MR84/MR104 10 pk ~$8; F623ZZ flanged ~$8/10 **(all ~unverified)** | $7–9 per 10 | Amazon | 623/MR series for finger pivots; shield them from hair with a printed lip. |
| Mini linear rail | **MGN9H 150 mm + carriage** | **$11.99** ([Amazon](https://www.amazon.com/Miniature-Length-Linear-Sliding-Printer/dp/B08HK19M83)); MGN7 150 mm ~$12–15 | Amazon | Quiet, stiff, light (MGN9 150 mm ≈ 40 g). Use for a stroke carriage. |
| Drawer slides | 10–12" ball-bearing slides, pair | ~$10–15 **(~unverified)** | Amazon/Home Depot | Cheap frame-mounted X travel; noisy, sloppy — mock-ups only. |
| GT2 belts/pulleys | 20T 5 mm-bore pulleys, 6 mm belt; Adafruit pulley $5.95 ([Adafruit](https://www.adafruit.com/product/1251)); starter kits $7–40 ([LumenPnP kit $39.99](https://www.opulo.io/products/lumenpnp-gt2-belt-and-pulley-kit); goBILDA [GT2 starter pack](https://www.gobilda.com/2mm-pitch-gt2-timing-belt-pulley-starter-pack-8mm-rex-bore/)) | $7–40 | Amazon, Adafruit, goBILDA | Belt + idler is the quiet way to move a carriage; keep belts away from hair (fully enclosed). |
| Bowden / cable drive | Bicycle shift cable (1.2 mm) + 4 mm lined housing, ~$10 kit ([Performance Bike](https://www.performancebike.com/shift-cables-housing-parts/c16547)); 3D-printer PTFE tube 4×2 mm ($6–8/2 m) as liner; 1/4" push-pull conduit ([Amazon](https://www.amazon.com/Cable-Universal-Push-Pull-Lawnmowers-Snowblowers/dp/B00WL5N298)) | $8–15 | Amazon, bike shop | **Key enabler for keeping motors off the head**: a frame-mounted servo pulls a cable; a return spring at the finger closes the loop. Friction/hysteresis is the main cost (~10–20 % force loss; worse with bends). |
| Tendon line | Braided PE fishing line 30–80 lb (Dyneema/Spectra), 100 m | ~$8–12 | Amazon | Near-zero stretch, slick, tiny. Terminate with a figure-8 knot in a printed cleat. |
| Flexible shaft | Rotary-tool flex shaft (Dremel 225 ~$25; generic 3 mm ~$12) | $12–25 | Amazon | Frame-mounted motor, rotation delivered to a head-mounted cam. Transmits vibration and whine; test before committing. |

---

## 5. Structure, fabrication, head interface

### 5.1 Frames
| Item | Price | Notes |
|---|---|---|
| 2020 aluminium extrusion, 4 × 500 mm | ~$25–30 **(~unverified)** | Amazon; Misumi/8020 for cut-to-length. |
| 2020 corner bracket kits (20–40 sets w/ T-nuts & M5) | ~$10–18 **(~unverified)** ([Amazon](https://www.amazon.com/Aluminum-Extrusion-Connectors-Hardware-Accessories/dp/B0FF9ZBTZJ)) | Buy one 40-set kit; you will use all of it. |
| M3/M4/M5 screw + nut assortment (Amazon 1000-pc) | ~$15–25 | Plus M3 heat-set inserts, 100 pc ~$8–10. |

### 5.2 3D printing without a printer
| Service | Typical cost, 100 g PETG part | Lead time to a US apartment | Notes |
|---|---|---|---|
| **JLC3DP** (jlc3dp.com) | $8–25 part + $8–15 shipping ([JLC3DP](https://jlc3dp.com/blog/how-much-does-3d-printing-cost)) | 2–5 days print + 5–10 days ship (DHL ~4–6 days extra cost) | Cheapest per gram; also does SLA resin, MJF nylon (strong, thin walls) and TPU. Batch all parts into one order. |
| **Craftcloud** (craftcloud3d.com) | $8–30 incl. shipping for a palm-size FDM part ([Craftcloud](https://support.craftcloud3d.com/en/articles/24-understanding-prices-on-craftcloud)) | 5–12 days | Aggregator; pick a US vendor for speed. |
| **Shapeways** | higher; relaunched after 2024 bankruptcy — check availability | 7–14 days | Nylon SLS only worth it for thin compliant parts. |
| **Public-library makerspaces** | **$0.05–0.20 per gram** → $5–20 per 100 g ([Jeffersonville $0.20/g](https://jefflibrary.org/makerspace/fees/), [Jersey City $0.10/g](https://jclibrary.org/communipaw-makerspace-3d-printing-service/)) | same week, often same day | Usually PLA only, sometimes PETG; limited size (~200 mm). Best iteration speed if one is nearby. |
| **Buy a printer** | Bambu A1 mini ~$199–249 **(~unverified)** | 2 days (Amazon) | If the project will go through >5 print iterations, this pays for itself in lead time alone and is within budget. Flagging as a real option, not a recommendation. |

Filament guidance: **PETG** for structural/finger carriers (tougher than PLA, fine near skin), **PLA** for first fit-checks (cheapest, stiffest), **TPU 95A** for compliant tips/flexures, **nylon (MJF)** for thin snap-fit or cantilever springs.

### 5.3 Laser-cut
SendCutSend (sendcutsend.com): acrylic, Delrin, aluminium, from ~$29 minimum order, 2–5 day ship **(~unverified)**. Ponoko similar. Delrin 3 mm plates make excellent quiet cam followers and finger links.

### 5.4 Head interface
| Option | Price | Notes |
|---|---|---|
| **Hard-hat ratchet suspension (replacement, 4- or 6-point)** | **$12–23** ([Amazon 4-pt ratchet](https://www.amazon.com/A79RS2-4-Point-Ratchet-Suspension-Replacement/dp/B00209KOMI); [6-pt Mega Ratchet](https://www.amazon.com/Replacement-Mega-Ratchet-Suspension-Omega/dp/B005KA6MSE)) | **Best adjustable head interface**: sized by ratchet 52–64 cm, standoff from scalp ~25–30 mm, four/six clip tabs you can print a ring to. Stays put under modest lateral loads. Buy the matching $10–20 hard hat too (MSA V-Gard or Pyramex) if you want the full shell as a mounting dome you can cut windows into. |
| **Welding-helmet ratchet headgear** | $16 ([Tractor Supply JobSmart](https://www.tractorsupply.com/tsc/product/jobsmart-welding-helmet-replacement-ratchet-headband-wa032); [Amazon generic](https://www.amazon.com/Generic-Headgear-Replacement-Accessory-Headbands/dp/B0D3HX6LY9)) | Has side pivots designed to carry a load (the helmet) — handy for a hinged module over the crown or back. |
| **Headlamp strap / elastic head harness** | $5–10 | Lowest profile; only for the lightest modules (<150 g). |
| **Bicycle helmet (cheap)** | ~$25 **(~unverified)** | Rigid dome, pre-vented (vents = cable/finger ports). Harder to size-adjust than a ratchet suspension. |
| **Mic boom arm (desk clamp)** | $40–50 ([Neewer/Samson](https://www.bestbuy.com/site/searchpage.jsp?st=mic-boom-arm)) | Frame-mounted approach: positions a 0.5–1 kg module over a seated head, springs balance weight. |
| **Gas-spring monitor arm (VESA)** | $36 ([HUANUO/VIVO](https://www.cuttles.io/monitors/arms/clamp)) | Holds 2–9 kg, 3 DOF; bolt a 100×100 plate to the module. Stiffer than a mic arm. |
| **Camera tripod + ball head** | $25–40 | Floor-standing; fine for a "hold still under it" rig. |
| **Salon dryer-hood stand** | ~$60–150 **(~unverified)** | Purpose-made to hover over a seated head; heavy base, height-adjustable. Worth a look if the design converges on a hood. |

---

## 6. Electronics

### 6.1 Controllers
| Board | Price | Why / why not |
|---|---|---|
| Arduino Uno R4 Minima / Nano Every | ~$20 / $13.70 ([SparkFun](https://www.sparkfun.com/arduino-nano-every.html)) | Most tutorials; Nano Every lacks hardware float speed for SimpleFOC. |
| **ESP32 DevKitC (WROOM-32E)** | **$8–17** ([Amazon](https://www.amazon.com/ESP32-DevKitC-ESP32-DevKitC-32E-ESP32-DevKitC-32UE-ESP32-WROOM-32E-ESP32-WROOM-32UE/dp/B0F2J2S8YQ)) | 240 MHz dual-core, 16 PWM channels, 3 UARTs (one per servo bus), Wi-Fi for a phone web-UI, runs SimpleFOC well. Default pick. |
| Raspberry Pi Pico 2 / 2 W | **$5 / $7** ([Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-pico-2/)) | Cheapest; PIO is great for timing; less library coverage for Dynamixel/SimpleFOC. |
| OpenRB-150 | $24.90–28.64 ([Robotis](https://www.robotis.us/openrb-150/)) | SAMD21 + Dynamixel bus + power pass-through, Arduino IDE. The zero-fuss path for XL330. |
| Waveshare Servo Driver with ESP32 | $14.97–15.99 ([Waveshare](https://www.waveshare.com/servo-driver-with-esp32.htm)) | ESP32 + Feetech bus + barrel-jack power in one; also drives PWM servos. The zero-fuss path for STS3215. |

### 6.2 Drivers
| Driver | Current limit? | Price | Notes |
|---|---|---|---|
| **PCA9685 16-ch PWM** | n/a | $14.95 Adafruit ([Adafruit](https://www.adafruit.com/product/815)); clones $6–8 | Only needed if >6 hobby servos or you want a separate servo power rail with a terminal block. |
| **DRV8871** (Adafruit breakout) | **Yes — ILIM resistor sets the current limit** ([Adafruit](https://www.adafruit.com/product/3190)) | $7.50 | Best cheap DC-motor driver here: 3.6 A, 6.5–45 V, and the current limit gives an N20 crank a hard torque ceiling. |
| TB6612FNG | No | $5 | Efficient dual H-bridge; no limit → pair with INA219 + firmware. |
| L298N | No; 2+ V drop, hot | $5 | Avoid. |
| **TMC2209** | StallGuard4 stall detection + current setting via UART | $4–8 | For steppers. |
| **SimpleFOC Mini / Shield** | voltage-mode torque limit / true current limit | $15–20 / $35–45 | For gimbal motors. |

### 6.3 Sensing, UI, safety, power
| Item | Price | Notes |
|---|---|---|
| **INA219 current sensor breakout** | $9.95 ([Adafruit](https://www.adafruit.com/product/904)) | Put one on the actuator power rail: fault the system if total current exceeds a ceiling (e.g., stalled servo). 26 V, ±3.2 A; use INA226/ACS712 for >3 A. |
| Potentiometer 10 kΩ w/ knob | $1–2 | Intensity (maps to goal-current / spring preload / amplitude). Two more for speed and stroke. |
| KY-040 rotary encoder | $2 | Menu navigation if using a display. |
| SSD1306 0.96" OLED (I²C) | $5–8 | Shows mode, force ceiling, current draw, fault state. |
| **22 mm mushroom E-stop, NC, latching** | **$8–14** ([Amazon APIELE/TWTADE](https://www.amazon.com/TWTADE-Mushroom-Emergency-Warranty-YW1B-V4E02R-BOX/dp/B07NNZB41H)); boxed version ~$15 ([Amazon](https://www.amazon.com/Mushroom-Emergency-Enclosure-Protective-Control/dp/B0DYYGMMGC)) | Wire the **NC contact in series with the actuator power rail** (not just a GPIO), with a second NC contact or the same loop read by the MCU so firmware also knows. Add a cheap inline rocker switch ($3) on the DC input as a second cut-off. |
| **Mean Well GST60A12-P1J** 12 V 5 A, UL/Level VI | **$18.60–19.40** ([Mouser](https://www.mouser.com/ProductDetail/MEAN-WELL/GST60A12-P1J?qs=odmYgEirbwzBCeXKJrW1mg%3D%3D), [DigiKey](https://www.digikey.com/en/products/detail/mean-well-usa-inc/GST60A12-P1J/7703712)) | The one certified supply for the 12 V family (XL430, STS3215-12V, NEMA 17, gimbal motors). |
| Adafruit 5 V 4 A UL-listed supply (#1466) | ~$15–24 ([Jameco/PiShop](https://www.jameco.com/z/1466-Adafruit-Industries-5V-4A-4000Ma-Switching-Power-Supply-UL-Listed_2505471.html)) | For XL330 (5 V bus) and logic. |
| 6 V / 7.4 V UBEC (Hobbywing 3 A, Turnigy 6 A, generic 8 A) | $3–16 ([Turnigy 6 A $10.17](https://hobbyking.com/en_us/turnigy-6a-6v-25v-switch-mode-ubec-w-selectable-voltages.html)) | Derive servo voltage from the 12 V supply for MG90S/DS3218/STS3215-7.4 V. Avoid LiPo entirely; nothing here needs to be cordless. |
| Fuses | Blade-fuse holder + 3 A/5 A fuses ~$6; 2.5 A polyfuse ~$0.50 | Fuse the 12 V input and each servo bus branch. |
| Wiring | JST-XH 2.54 kit ~$10, Dupont kit ~$8, 22 AWG silicone wire 6-colour ~$12, heat-shrink ~$6, screw-terminal breakout ~$6 | Dynamixel uses JST-EH 3-pin (cables included); Feetech uses JST-PH-ish 3-pin (cables included with multi-packs). |

---

## 7. Test and measurement

| Item | Price | Use |
|---|---|---|
| Digital luggage scale (G-Force 110 lb) | $12 ([Walmart](https://www.walmart.com/ip/G-force-Digital-Hanging-Luggage-Scale-110-lbs-Max/40900467)) | Pull-force of tendons, magnet breakaway force (resolution 10 g = 0.1 N, fine for us). |
| Kitchen scale (0.1 g, 500 g–3 kg) | $10–15 | Static tip normal force: push the finger onto the scale pan. Cheapest "force gauge" with the right range. |
| 5–50 N spring force gauge (Shimpo/generic) | $15–25 **(~unverified)** | Optional; the kitchen scale covers it. |
| **FSR 402** (Interlink) | $7 ([Adafruit](https://www.adafruit.com/product/166)) | Thin sensor under a tip or on the wig head to log contact force vs time; ±10–20 % accuracy, fine for relative work. |
| **1 kg bar load cell + HX711** | $8–12 kit; HX711 alone $4.95 ([SparkFun](https://www.sparkfun.com/products/13879)) | Proper 0.01 N-resolution force log for bench testing; mount the tip on the load cell. |
| Sound-level app (NIOSH SLM on iPhone; Decibel X) | free | Compare actuators at 30 cm; phone mics are fine for A/B. |
| **Cosmetology mannequin head with real human hair** | **$28–36** ([Amazon, e.g. Opini 100 % human hair](https://www.amazon.com/wig-heads/s?k=wig+heads)) | Essential bench target: real hair density/direction on a head-shaped form. Clamp (~$8) usually sold separately. |
| Human-hair wig (for a second hair type/length) | $65–100 ([Luvme / Mslynn under $100](https://mslynnhair.com/collections/under-100)) | Optional; the mannequin covers most needs. |
| Foam/styrofoam wig head | $5–8 | For geometry fit-checks only. |

---

## 8. Tools Michael probably needs

| Tool | Price | Source |
|---|---|---|
| **Pinecil V2** USB-C soldering iron (+ 65 W PD charger if none) | $26–42 ([Pine64](https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/), [Ameridroid $41.95](https://ameridroid.com/products/pinecil-v2-soldering-iron)) | Pine64, Amazon |
| Heat-set insert tips (Pinecil/TS100 compatible) | $7–15 ([Amazon kits](https://www.amazon.com/heat-set-insert-tool/s?k=heat+set+insert+tool)) | Amazon |
| Solder (63/37, 0.6 mm) + flux pen | $10 | Amazon |
| Metric hex-key set (ball end, 1.5–10 mm) | $8–12 | Amazon |
| Digital calipers (150 mm) | $8–20 ([Amazon](https://www.amazon.com/digital-calipers/s?k=digital+calipers)) | Amazon |
| Deburring tool + needle-file set + 220/400 sandpaper | $8 + $10 + $6 | Amazon |
| Multimeter (AstroAI 2000/4000-count) | $15–23 ([AstroAI](https://www.astroai.com/digital-multimeter-6000-counts-dm6000ar/ap/100019)) | Amazon |
| Hot-glue gun, CA glue (thin + gel), Loctite 243 threadlocker | $10 + $6 + $6 | Amazon |
| Small screwdriver set, flush cutters, wire stripper | $8 + $6 + $8 | Amazon |
| Helping-hands / PCB vise, breadboard, jumper kit | $12 + $8 | Amazon |
| **Tool subtotal** | **~$150–190** if starting from nothing | |

---

## 9. Recommended default electronics stack

**Design goals:** 2–6 actuators, per-actuator current/force limiting, hardware e-stop in the power path, a manual intensity knob, reprogramming in seconds from a laptop, all from a single certified wall supply.

### Stack A (recommended): Dynamixel XL330 + OpenRB-150

| Qty | Item | Unit | Ext. |
|---|---|---|---|
| 4 | Dynamixel XL330-M288-T (mix in 1–2 M077 if speed > torque) | $27.49 | $110 |
| 1 | OpenRB-150 controller | $28.64 | $29 |
| 1 | 5 V 4 A UL-listed supply (Adafruit #1466) | ~$18 | $18 |
| 1 | 22 mm NC mushroom e-stop (+ small enclosure) | $12 | $12 |
| 1 | INA219 (actuator rail current watchdog) | $9.95 | $10 |
| 2 | 10 kΩ pots + knobs (intensity, speed) | $2 | $4 |
| 1 | SSD1306 OLED | $6 | $6 |
| 1 | Inline rocker switch, blade fuse holder + fuses, JST/Dupont/wire kit | — | $25 |
| | **Total** | | **≈ $214** |

*Justification.* XL330 is the lightest actuator with native current-based position control; the "goal current" register is an adjustable electronic clutch read by the intensity pot; velocity/acceleration profiles are in firmware so stroke shaping is parametric; six servos daisy-chain on one cable; the OpenRB-150 is Arduino-IDE programmable over USB-C and passes bus power straight through, so the e-stop simply breaks the 5 V actuator rail while the controller stays alive to log the fault. Adding actuators #5–6 is +$27.49 each with no new driver hardware. Noise is low (plastic gears, 5 V), and 18 g per actuator keeps a four-finger head module under 150 g of motors.

### Stack B (budget substitute, ~$150): Feetech STS3215 + Waveshare ESP32 servo driver
4 × STS3215-7.4 V ($80) + Waveshare Servo Driver with ESP32 ($16) + Mean Well GST60A12 ($19) + e-stop/INA219/pots/OLED/wiring ($55) ≈ **$170**. Same architecture; servos are 55 g and audibly whinier, but torque-limit and current readback work, the ESP32 gives Wi-Fi tuning from a phone, and the LeRobot community has mature Python drivers. Choose B if the design converges on a frame-mounted module where weight is free.

### Stack C (smoothness experiment, add-on ~$90 for 2 axes): GM2804/GM3506 + SimpleFOC Mini
2 × GM2804 w/ AS5600 ($38) + 2 × SimpleFOC Mini ($35) + shares the 12 V supply and ESP32 from Stack B. Direct-drive, silent, back-drivable force control. Worth building **one** finger this way in parallel with the smart-servo module so the sensation gate can A/B geared vs direct-drive motion.

All stacks share: NC e-stop in the actuator power rail (never just logic), INA219 rail watchdog with a firmware trip, fuse on the DC input, no batteries, one certified brick.

---

## 10. Lead times and a one-week sourcing strategy

| Vendor | Ship speed to a US apartment | Use for |
|---|---|---|
| **Amazon (Prime)** | 1–2 days | Servos (MG90S, DS3218, STS3215 multipacks), N20s, bearings/rails/belts, springs/magnet assortments, extrusion, e-stop, tools, mannequin head, OLED/pots/wire. |
| **McMaster-Carr** | same-day/next-day ground in most of the US, no minimum | Precision shafts, springs by spec, CF springs, fasteners, Delrin/acrylic stock, washers. Expensive per item but unbeatable lead time and the catalogue *is* the spec sheet. |
| **Adafruit / SparkFun / Pololu** | ship same or next business day; 2–5 days USPS/UPS | Breakouts (DRV8871, INA219, PCA9685), Pololu gearmotors/encoders, certified PSUs. |
| **DigiKey / Mouser** | next-day available; 2–3 days ground | Mean Well supplies, TMC2209/A4988 originals, connectors, fuses. |
| **Robotis US (robotis.us) / Trossen** | ships from California/Illinois, 2–5 days | Dynamixel, OpenRB-150, U2D2. Order day 1. |
| **ServoCity / goBILDA** | 2–5 days | Pulleys, hubs, shafts, clamping collars, pattern plates if the design wants a bolt-together frame. |
| **K&J Magnetics** | 1–3 days | Magnets by exact pull force. |
| **iFlight (US warehouse) / DFRobot / Amazon** | 2–7 days | Gimbal motors + SimpleFOC Mini. AliExpress is cheapest but 2–4 weeks: only for spares. |
| **JLC3DP / Craftcloud** | 7–14 days door-to-door | Batch all printed parts in one order on the day the geometry freezes; use a library makerspace or a bought printer for the week-one iteration loop. |
| **AliExpress** | 10–30 days | Never on the critical path; second-iteration spares (N20 10-packs, STS3215, GM2804 kits). |

**Strategy.** Day 0: place the Amazon, McMaster, Robotis and Adafruit orders in parallel (four carts, ~$250–350 total including tools). Day 1–2: Amazon hardware and McMaster arrive → bench mock-up with MG90S/N20 crank and the mannequin head starts. Day 3–5: Dynamixel/Adafruit arrive → wire Stack A, calibrate current limits against the kitchen scale. Printed parts: library/own printer in week 1; JLC3DP for the refined PETG set in week 2. Do not wait on AliExpress for anything the first human test depends on.

### Indicative budget for SP1

| Block | Low | High |
|---|---|---|
| Actuators (4–6 smart servos or mixed) | $80 | $170 |
| Controller + drivers + sensing + e-stop + PSU + wiring | $70 | $110 |
| Motion/compliance hardware (bearings, rail, springs, magnets, cable) | $40 | $80 |
| Structure (extrusion, head suspension, hard hat or arm, fasteners) | $40 | $90 |
| Printed parts (service or library) | $20 | $80 |
| Test gear (mannequin head, scale, FSR/load cell) | $45 | $70 |
| **Build subtotal** | **$295** | **$600** |
| Tools (if starting from zero) | $150 | $190 |

The $100–400 target holds for the build if actuators stay at four and printing goes through a library; the upper end adds a gimbal-motor module, more actuators and service-printed PETG. Tools are a one-time cost outside the build budget.

---

## Appendix: quick actuator decision guide for mechanism teams

- **Need a reciprocating stroke at 1–4 Hz, cheaply, now:** N20 (150–300:1) + DRV8871 with ILIM set + printed slotted crank + spring-loaded follower. ~$15 per module.
- **Need programmable strokes with an adjustable force ceiling, head-mounted:** XL330 in current-based position mode on a 30–60 mm printed finger with a torsion-spring knuckle and magnet breakaway tip. ~$30 per finger.
- **Need the smoothest, quietest, most "hand-like" force profile:** GM2804/GM3506 direct-drive under SimpleFOC, lever ≤50 mm, magnetic-coupling torque limit. ~$40–60 per finger; one evening of tuning.
- **Need a long linear traverse across the head (frame-mounted):** MGN9 rail + GT2 belt + NEMA 17 + TMC2209 StallGuard. ~$50.
- **Avoid:** micro linear actuators (too slow), solenoids (binary), 37D gearmotors (heavy/loud), L298N (no limiting), hobby servos without a series spring near the head, LiPo packs.
