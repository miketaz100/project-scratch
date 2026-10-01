# Servo alternatives for the stroke axis (XL330-M288-T back-ordered)

Checked 2026-10-01 against live vendor pages (robotis.us, en.robotis.com, Amazon product pages opened in a browser pane, Seeed, Waveshare, Pololu, Adafruit, iFlight, Hiwonder, Babsco, roboticscenter.ai, eBay, Generation Robots, RoboSavvy, Mouser, ROBOTIS e-manual). Pages that could not be loaded are named in §7. Prices exclude shipping unless stated. Companion to bom-verified.md §6.17, §9, §11 and component-landscape.md §1.

## 0. What the axis needs (numbers used for every verdict)

| Quantity | Value | Basis |
|---|---|---|
| Stroke torque, peak | 0.10 N·m | brief |
| Gravity moment, arm horizontal (worst case) | 0.147 N·m | 0.15 kg × 9.81 m/s² × 0.10 m |
| Gravity moment at ±25° from hanging | 0.062 N·m | 0.147 × sin 25° |
| **Required, pendulum geometry** | **0.16 N·m** | 0.10 + 0.062 |
| **Required, arm horizontal** | **0.25 N·m** | 0.10 + 0.147 |
| Peak joint speed for ±25° sinusoid | 26 rpm at 1 Hz, 52 rpm at 2 Hz, **78 rpm at 3 Hz** | ω = 0.436 rad × 2πf |
| Inertial torque of 0.15 kg at 0.10 m, ±25° | 0.026 N·m at 1 Hz, 0.10 N·m at 2 Hz, **0.23 N·m at 3 Hz** | J = 1.5 × 10⁻³ kg·m², α = θ₀ω² |

Two flags for the design lead, not re-derived here: (1) the 0.10 N·m "peak" matches a 2 Hz stroke with this inertia; at 3 Hz the inertial term alone is 0.23 N·m, so either the effective inertia is lower than the 0.15 kg-at-0.10 m lump or the 3 Hz corner needs a smaller amplitude. (2) A servo's no-load speed must exceed the 78 rpm figure with margin, because speed falls roughly linearly with load fraction; anything under ~60 rpm no-load is a 2 Hz axis, not 3 Hz.

Baseline XL330-M288-T: 0.52 N·m stall, K_t 0.354 N·m/A, 103 rpm. The design's 450 mA Goal Current cap gives 0.16 N·m (mechanical.md §4, EF §4.2); 0.25 N·m would need 0.71 A, 48 % of stall. Margin 3.3× (pendulum) / 2.1× (horizontal).

## 1. The same part, other sellers (none inside one week)

| Seller | Price | Status shown today | Verdict |
|---|---|---|---|
| robotis.us https://robotis.us/products/dynamixel-xl330-m288-t | $27.49 | "Sold out", "estimated lead time of 2 months" | keep the back-order |
| ROBOTIS Korea https://en.robotis.com/shop_en/item.php?it_id=902-0163-000 | $23.90 | item page shows price and no lead-time line; the XL category list https://en.robotis.com/shop_en/list.php?ca_id=202030 shows **"Lead Time: 40 days"** for XL330-M288-T, XL330-M077-T, XL430-W250-T and 2XL430. "Normally ships out within 3 working days when in stock", DHL from Korea, duty not included | contradictory; email ROBOTIS Korea before relying on it (bom-verified §6.17 assumed in stock) |
| Amazon | — | both FPBIGCHA listings (B0DS7T94BS, B0DS7SFYPD) return "Page Not Found"; a search for "dynamixel xl330-m288-t" returns no XL330 | no Amazon source |
| Trossen Robotics https://www.trossenrobotics.com/search?q=xl330 | — | "No results found for xl330"; a "dynamixel" search returns only arm bundles | Trossen no longer retails single Dynamixels |
| RobotShop | — | every product URL returned 403 / Cloudflare bot check in both tools; search snippets show no XL330 page, only XC330 at $103.39 | unverifiable |
| Mouser 902-0163-000 | — | "Obsolete", "does not presently sell this product in your region" (search snippet; page timed out) | no |
| DigiKey | — | 403; no XL330 listing found by search | no |
| Pololu https://www.pololu.com/search?query=dynamixel | — | "your search returned no results" | no |
| eBay 198387610713 (tpower2025, Shenzhen) | $58.90 | "This item is out of stock"; delivery quoted Oct 27–30 | no |
| eBay 375789085580 | $57.00 | quantity and location not readable; China-origin listing | 3–4 weeks, 2× price |
| Generation Robots (FR) https://www.generationrobots.com/en/403817-dynamixel-xl330-m288-t-servo-motor.html | €40.20 | "Delivery within 4 weeks" (the "2 units available" snippet is stale) | no |
| RoboSavvy (UK) https://robosavvy.co.uk/robotis-dynamixel-xl330-m288-t.html | £22.67 sale | no stock wording on the page; courier UK→US is typically 3–5 days | the only unverified maybe; phone them |
| robotis.us LEAP Hand Bundle Lite (16× XL330-M288-T) | $582.47 | "estimated lead time of 2 months" | no back door |

**XL330-M077-T** (same body, 77.5:1): robotis.us https://robotis.us/products/dynamixel-xl330-m077-t now shows **"Sold out"** with no lead time (bom-verified §9 listed it as in stock earlier today; it changed). Korea $23.90, 40 days. Spec (e-manual): 0.215 N·m stall at 1.47 A, K_t 0.146 N·m/A, 383 rpm, Goal Current / Current Limit in 1 mA units. Margin **1.3× pendulum, 0.86× horizontal**: 0.16 N·m needs 1.1 A (75 % of stall) and 0.25 N·m exceeds stall. It is the only candidate with speed to spare (383 rpm), but it is a bridge servo only with the arm hanging and a counterweighted or lighter hand, and it is not in US stock either.

## 2. Comparison table, all candidates

Mass, torque and speed are manufacturer figures from the pages cited. "Current limit" means a closed current loop (Dynamixel) unless marked; Feetech's limit is a PWM/torque cap plus an over-current trip (see §4). Delivery is to a US address from today.

| # | Part | Price / vendor | Stock and lead today | Mass | Stall torque, V | Speed (no load) | Control | Margin vs 0.16 / 0.25 N·m | What changes in the design | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **XL330-M288-T** | $27.49 robotis.us; $23.90 Korea | 2 months / 40 days (§1) | 18 g | 0.52 N·m, 5 V | 103 rpm | current-based position, 12-bit absolute, Goal Current 1 mA units | 3.3× / 2.1× | none | baseline; keep the order |
| 2 | XL330-M077-T | $27.49 robotis.us; $23.90 Korea | sold out / 40 days | 18 g | 0.215 N·m, 5 V | 383 rpm | same table | 1.3× / 0.86× | Goal Current re-derived (K_t 0.146), bom.md §9.1 | bridge only, and not available |
| 3 | **XC330-M288-T** | $103.39 robotis.us https://robotis.us/products/dynamixel-xc330-m288-t; $89.90 Korea https://en.robotis.com/shop_en/item.php?it_id=902-0173-000; $103.39 RobotShop (unverifiable) | "Sold out", "lead time of 1 month" / "Lead Time: 40 days" | 23 g | 0.93 N·m, 5 V, 1.80 A (K_t ≈ 0.517) | 81 rpm | identical control table (Operating Mode 11, Current Limit 38, Goal Current 102; e-manual), current-based position | 5.8× / 3.7×; **2.5 Hz ceiling** at ±25° (81 rpm) | **drop-in**: same 20 × 34 × 26 body, same X330 drawing (4 × Ø1.6 on 16 × 30, horn Ø16 / PCD 12), same cable, same firmware; set Goal Current ≈ 310 mA for 0.16 N·m; metal gears are louder than the XL330's plastic train; +5 g | the only true drop-in, but 3.8× the price and not faster to get |
| 4 | XC330-T288-T | $103.39 robotis.us | "Sold out", 2 months | 23 g | 0.92 N·m, 11.1 V | — | same | — | 12 V rail | no |
| 5 | XL430-W250-T | $27.50 robotis.us; $23.90 Korea | "Sold out" / 40 days | 57.2 g | 1.4 N·m, 11.1 V (6.5–12 V) | 57 rpm | **no current sensor**; Present Load is inferred; no current-based position mode (e-manual) | 8.8× but no torque ceiling | 12 V supply, new P13 (28.5 × 46.5 × 34), new P16, +39 g | **no**: fails the safety requirement and the speed check |
| 6 | **Feetech STS3215 7.4 V (C001, 1:345)** | **$20.00 Seeed, US warehouse** https://www.seeedstudio.com/STS3215-19kg-cm-7-4V-Serial-Servo-p-6338.html; $25.99 Amazon (sold by waveshare, B0G2576KKN, delivery Oct 8–14); $135.99 Amazon RCmall 6-pack (B0FQHCV9GP, "Only 5 left", Prime next-day) | **in stock, 1–5 days** | 55 g | 1.9 N·m stall, 0.5 N·m rated, 4–7.4 V | 52 rpm (0.192 s/60°) | 12-bit magnetic absolute, Torque Limit reg 48 (0–1000 ‰), Protection Current reg 28 (×6.5 mA), Present Current reg 69, overload trip | 12× / 7.6×; **2 Hz ceiling** | Feetech bus driver (§4), 6–7.4 V rail (new buck or 2S), new P13 for a 45.2 × 24.7 × 35 standard-servo body, P16 for a 25T spline, firmware port, +37 g head mass | ships tomorrow; heavy and slow; the fallback if nothing lighter lands |
| 7 | Waveshare/Feetech ST3215 12 V | $23.99 Seeed (US/CN/DE), Amazon B0CFY52HVV "Currently unavailable" | Seeed in stock | 55 g | 3.0 N·m, 6–12.6 V | 45 rpm | as 6 | 1.7 Hz ceiling | as 6 plus 12 V | no |
| 8 | **Feetech STS3032** | roboticscenter.ai https://www.roboticscenter.ai/store/product/feetech-feetech-sts3032 "In stock", "ships from San Francisco in ~48 hours", price on request; Babsco (Elkhart, IN) https://shop.babsco.com/feetech-sts3032-4-5kg-compact-smart-servo-c001 **$32.99, "IN STOCK", 1 available**; $29–49 elsewhere (vecrobot DNS failed; evelta India; aifitlab back-ordered); no Amazon listing | **thin US stock, 2–4 days** | 20.6 g | 0.44 N·m stall (4.5 kg·cm), 0.15 N·m rated, 4.8–6 V, 1.2 A stall; ≈ 0.37 N·m on the existing 5 V rail | 111 rpm (0.09 s/60°) | 12-bit magnetic absolute, coreless motor, metal gears, aluminium case, same STS registers as 6 | 2.7× / 1.7× at 6 V (2.3× / 1.5× at 5 V); **3 Hz capable** | Feetech bus driver, new P13 for a 23.2 × 12.1 × 28.5 body (half the XL330 width), P16 for its spline, firmware port; **5 V rail stays**; +2.6 g | **best substitute on mass × torque × speed**; order from both US sellers at once because each shows 1–few units |
| 9 | Feetech SCS0009 | Amazon RCmall 2-pack B0FWBZ6DNF **$25.88, "Only 3 left", delivery Thu Oct 8**; Seeed $9.00 "In stock", China warehouse (DHL 2–5 days, 10–20 % of US parcels get a 7–15 day customs hold per Seeed's Feb-2026 notice); Waveshare SC09 clone Amazon B0C3QGLGB8 "Currently unavailable" | 1 week via Amazon | 13.2 g | 0.226 N·m stall, 0.07 N·m rated, 4–7.4 V, 1.0 A stall | 100 rpm (0.1 s/60°) | 10-bit (0.29°) sensor, position/load/speed/V/temp readback, max-torque register, overload cut at > 80 % stall for 2 s | 1.4× / 0.9×; rated torque is below the stroke load | as 8 (tiny cradle), plastic case, cored motor | smallest real bus servo; torque too marginal for continuous 1–3 Hz unless the arm is counterbalanced or shortened (§3) |
| 10 | Hiwonder LX-16A | $16.99 Amazon (delivery tomorrow Oct 2); $16.99 hiwonder.com "In stock" (320), DHL 3–5 days | next day | 54 g | 1.7 N·m at 6 V / 2.0 at 7.4 V, 6–8.4 V | 53 rpm | pot, 0.3°; readback position/temp/voltage; **no torque or current limit** (motor-off only); private protocol, needs Hiwonder debug/BusLinker board | — | everything (board, rail, cradle, firmware) | no |
| 11 | Hiwonder LX-224 | $16.99 Amazon B081CTX6DM "In Stock", Prime Oct 3 | next day | 63 g | 2.0 N·m, 6–8.4 V | 0.2 s/60° | as 10 | — | as 10 | no |
| 12 | Hiwonder HTS-35H / HTD-45H | $21.99 / $24.99 hiwonder.com | China | 64 g | 3.4 / 4.4 N·m | — | pos/V/temp, no current | — | as 10 | no |

Items 13–18 (sub-15 g and non-servo options) are in §3; humanoid-hand actuators in §5.

## 3. Smaller than the XL330 (director addition)

The XL330 (18 g, 20 × 34 × 23 mm) **is already the smallest and lightest Dynamixel**; the older XL-320 (16.7 g, 7.4 V, no current control) is "Out of Stock" at ROBOTIS Korea and has no current mode anyway, and every other X/P model is 57 g or more. Going smaller means leaving Dynamixel. Honest costs are stated per row.

| # | Part | Mass, size | Torque | Feedback | Current limit | Price, stock today | Design change | Where it loses |
|---|---|---|---|---|---|---|---|---|
| 13 | **Feetech STS3032** (row 8) | 20.6 g, 23.2 × 12.1 × 28.5 | 0.44 N·m stall, 0.15 rated | 12-bit magnetic | torque-limit + over-current trip registers | $32.99 Babsco (1); SF stock, price on request | Feetech bus board, tiny cradle, 5 V unchanged | not sub-15 g, but half the XL330 volume; limit is a PWM cap, not a current loop |
| 14 | **Feetech SCS0009** (row 9) | 13.2 g, 23.2 × 12.1 × 25.25 | 0.226 stall, 0.07 rated | 10-bit, 0.29° | max-torque register, overload cut | $25.88/2 Amazon (Oct 8); $9 Seeed CN | as 13 | 1.4× pendulum margin only, 0.9× horizontal; rated duty is below the stroke load; plastic case; cored motor |
| 15 | Micro digital hobby servos: Hitec HS-5055MG; KST X08 V6; MKS DS65K | 11.9 g, 22.8 × 11.6 × 24; 8 g, 23.5 × 8 × 16.8; 6.5 g, 22 × 23 × 8.5 | 0.157 N·m at 6 V; 0.216; 0.216 | **none exposed** (internal pot; tap the wiper for a crude analogue readback) | **none**: a current-sense driver (INA219 / ACS712 in the servo supply with a firmware cut) or a mechanical cap (slip clutch, magnet breakaway, series spring) is mandatory | HS-5055MG $29.99 Innov8tive (MI) "In stock" https://innov8tivedesigns.com/hitec-hs-5055mg-metal-gear-digital-micro-servo.html, Amazon $29.99 Oct 7; KST X08 $41.99 AMain "Back Order"; DS65K $60 Esprit "Coming Soon" | PWM from any OpenRB pin, 5–6 V rail OK, tiny cradle, current-sense board added | HS-5055MG margin 1.0× / 0.6×; KST 1.35× / 0.86×; position accuracy ±1°, 50 Hz update, deadband hunting; the safety layer moves from the servo into your own circuit |
| 16 | **N20-class gearmotor with encoder** (Pololu 298:1 HP 6 V + 12 CPR encoder https://www.pololu.com/product/5173; 150:1 https://www.pololu.com/product/5161 class) | ≈ 11–12 g, 10 × 12 mm gearbox, 3 mm D-shaft | 298:1: 0.39 N·m stall at 1.6 A, 100 rpm; 150:1: ≈ 0.20 N·m, 210 rpm | 12 CPR × ratio quadrature (3576 counts/rev at 298:1 ≈ 0.1°), **relative**: needs homing against the zero pin or a hard stop | via the driver: Adafruit DRV8871 $7.50 "In stock" https://www.adafruit.com/product/3190 (chopping current set by one resistor; output ≈ 0.24 N·m per amp at 298:1, so 0.7 A ≈ 0.17 N·m) | $29.95 Pololu "Active and Preferred" (ships same/next day) | direct joint drive on the D-shaft (new cradle, collar), own PID loop and current cut in firmware on the OpenRB (SAMD21 is ample), or a crank + spring follower for a fixed ±25° | 298:1 is a 2 Hz axis; 150:1 is 3 Hz-capable at 1.25× / 0.8× margin; gear whine; 1–3° backlash; not back-drivable at 298:1; no absolute position; no temperature readback |
| 17 | Tiny gimbal BLDC + FOC: GM2804 + AS5600 (Amazon B0FSZ7XWG2 $24.99 "In Stock", Prime next-day; DFRobot $18.90, shipping paused to Oct 8); GM3506 + AS5048A (iFlight $41.90 "In Stock") | 2804: ≈ 40 g, Ø34.5 × 19.5; 3506: 72 g, Ø40 × 26 | 0.03 N·m; 0.06–0.10 N·m | 12-bit magnetic absolute | true torque = current (SimpleFOC Mini $12.95 Amazon "In Stock", Oct 16; voltage-mode only) | in stock | SimpleFOC on the OpenRB, 12 V rail, new cradle, lever ≤ 25 mm or 4:1 belt | **fails both constraints** at 80 mm: 0.03 N·m is 1/5 of the need and the motor is 2–4× the XL330's mass; only viable as a frame-mounted or very-short-lever axis |
| 18 | Smaller BLDC (2204/2208 gimbal, ≈ 20–40 g) | 20–40 g | ≤ 0.07 N·m | needs encoder | as 17 | $25–40 | as 17 | same torque failure |

Net: below 15 g the only part with a real bus, readback and a torque register is the SCS0009, and it is torque-marginal. The STS3032 at 20.6 g is the honest "smaller than XL330" answer (half the volume, 85 % of the torque, same speed class, same 5 V rail). Everything lighter trades away either the torque margin (SCS0009, HS-5055MG), the absolute position and quietness (N20), or the safety features (hobby servos, which then need an external current sensor or a mechanical clutch).

## 4. Driving Feetech servos from this design

- **Bus boards in US stock:** Seeed Bus Servo Driver Board for XIAO **$5.99, "In stock", US warehouse** https://www.seeedstudio.com/Bus-Servo-Driver-Board-for-XIAO-p-6413.html (UART/USB; XIAO MCU sold separately, not needed if driven from the OpenRB's UART); Waveshare Bus Servo Adapter (A) $4.99 (Waveshare warehouse paused Oct 1–4) or Amazon 2-pack B0DK79JNNK **$19.99, "Only 11 left", Prime next-day**; Waveshare Servo Driver with ESP32 $15.99 / Amazon B0D83QMQ4N $26.59 ("Only 8 left", Oct 6). The adapter's input voltage must equal the servo voltage (9–12.6 V on the Waveshare (A); 5–6 V works on the Seeed XIAO board for STS3032/SCS0009; verify the Seeed board's input range on the schematic before powering).
- **Direct from the OpenRB-150?** Feetech's protocol is Dynamixel Protocol 1.0 packet framing with a different register map, on a 5 V half-duplex single-wire TTL bus, and the OpenRB DXL port carries VIN (3.7–12.6 V) on VDD. Electrically plausible with Dynamixel2Arduino's raw read/write-by-address calls, but the e-manual does not list Protocol 1.0 for the OpenRB, the connectors differ, and STS registers are little-endian while SCS are big-endian. Treat it as an experiment; the $5.99 board on a spare UART is the safe path.
- **Torque limiting semantics:** Torque Limit (reg 48, ‰ of max PWM) and Protection Current (reg 28, ×6.5 mA, with an over-current trip and a protection-time) cap output; Present Current (reg 69) and Present Load (reg 60) read back. It is a duty-cycle ceiling plus a trip, not the XL330's closed current loop, so the force ceiling is less linear and the firmware "software clutch" (EF §4.2) needs a bench re-calibration against the kitchen scale.
- **Mass and power accounting for the crown concept:** STS3032 +2.6 g, SCS0009 −4.8 g, STS3215 +37 g, plus 16–21 g for a bus board if it rides on the head (it need not; it can sit with the OpenRB).

## 5. Where humanoid and dexterous-hand builders buy small actuators (director addition)

Summarised from a parallel sourcing pass today (vendor pages cited; RobotShop and some Amazon pages could not be rendered and are marked as snippets).

| Project / company | Actuator | Mass, torque | Control | Price, US lead | Fit for one 0.1 N·m axis |
|---|---|---|---|---|---|
| **LEAP Hand (CMU)** https://v1.leaphand.com/parts | Full: 16× **XC330-M288-T** ($89.99 ea listed); Lite: 16× **XL330-M288-T** ($23.90 ea, "weaker motors… for education"). Bought at robotis.us / en.robotis.com. Their own note: "These often go out of stock, check in with Dynamixel Support if you need it quickly." | 23 g / 18 g | current-based position | both "Sold out" at robotis.us (1 month / 2 months); Koch v1.1 bundles "Expected ship date: Q1 2026" | the same part we want; confirms there is no US back door this week |
| **LeRobot SO-100/SO-101** https://github.com/TheRobotStudio/SO-ARM100 | Feetech **STS3215 7.4 V** (C001 1:345 ×7, C044 1:191 ×2, C046 1:147 ×3), Waveshare bus board | 55 g, 1.9 N·m | STS registers | Seeed US $20 in stock; Waveshare; Amazon; WowRobo; two-arm BOM ≈ $230 | over-torqued, over-weight; the ship-tomorrow fallback (row 6) |
| Koch v1.1 / low-cost ALOHA | XL330-M288-T ×4 + XL430 ×2 (follower), XL330-M077-T ×6 (leader); ALOHA uses XL430/XM430 | 18–57 g | Dynamixel | sold out as above | as LEAP |
| **Pollen Amazing Hand** / HOPEJr hand | 8× / 16× **Feetech SCS0009** (tendon); Seeed kit $99–104 "in stock" | 13.2 g, 0.23 N·m stall | SCS registers | Seeed $9 in stock (CN); Amazon 2-pack Oct 8 | the hand community's "tiny" answer; torque-marginal here (row 9) |
| DexHand / TheRobotStudio V1.0 | forearm BLDC tendon motors + small in-hand servos (~$300 parts) | — | — | — | architecture, not a part we can buy |
| Yale OpenHand T42 | Dynamixel RX/MX-28 or Power HD hobby servo | 72 g+ | — | — | too big |
| ORCA Hand (ETH) | 17× Dynamixel XC330-T288 | 23 g | current-based position | 2-month lead | drop-in class, 12 V variant |
| BiDexHand (NU) | 15× Kondo KRS-788HV; Kondo KRS-3301 is 26.4 g, 0.59 N·m, ICS serial, ¥2,035–3,800 | 26 g | position only | Japan import | no current limit |
| Hiwonder hands | LX-16A / LX-224 / HTS-35H / HTD-45H | 54–64 g | pos/V/temp, no current | Amazon next-day | no (rows 10–12) |
| Tesla Optimus V3 | tendon-driven, forearm actuators (gearbox + lead screw + wire, per patents/reporting) | — | — | — | class: micro gearmotor + lead screw |
| Figure 02/03 | 16 DoF, self-contained motor+sensor tendon units in the forearm | — | — | — | not purchasable |
| Sanctuary Phoenix | miniature hydraulic valves/actuators | — | — | — | not applicable |
| Inspire RH56 | 6 micro linear servo actuators (coreless + planetary + lead screw + position and force sensor; newer: BLDC + planetary roller screw), RS485/CAN; sold standalone https://inspire-robots.store/collections/micro-linear-servo-actuator | — | position + force | enquiry pricing | nearest commercial analogue of an OEM finger drive; linear, not rotary; price class far above $30 |
| Sharpa Wave | 22 proprietary tendon modules | — | — | — | not purchasable |
| Shadow Hand | 20× Maxon 118608 + 352367 (131:1) in the forearm, tendons | 50 g class | Hall, external driver | Maxon ECX SPEED 16 M + GPX16: €228.94 + €136.52 | right physics, 10× the budget, no integrated control |
| Wonik Allegro V4 | joint-mounted DC gearmotor 1:369, 0.70 N·m/joint, CAN | — | — | — | Dynamixel X330 is the hobby-scale analogue |
| Unitree Dex5; Seed Robotics RH8D | hollow-cup motors + encoders + low-damping reducers; 8 smart actuators with current feedback | — | — | not sold separately | — |
| Faulhaber 1028M006B + IEM3-1024 + 10/1 64:1 | 23 g, 54 mN·m cont / 200 mN·m | 1024-line encoder, external driver | $408.90 shop.faulhaber.com | right size, wrong price, no controller |
| MyActuator RMD-L-4005 | 65 g, 0.07 nom / 0.25 N·m peak, direct drive | 18-bit, CAN, FOC current limit | $65 snippet; Dings Motion USA $109 "sold out" | over 60 g, no gearing |
| CubeMars (smallest AK40-10, 185 g); Robstride RS00 (310 g, $125 Seeed US in stock); SteadyWin GIM3505-8 (97 g, $56–126) | — | CAN FOC | — | all far too heavy |
| T-Motor GB2208 gimbal | 39.5 g, 0.07 N·m, no gear, no encoder | — | $25.90 | needs encoder + driver + gear; no |
| Feetech HLS3915M ("humanoid", torque-control mode) | ≈ 60 g, 1.4 N·m at 12 V | TTL, torque mode | Amazon (unrendered) | too strong and heavy |

What this says: at finger scale the field converges on exactly two part families, Dynamixel X330 (LEAP, ORCA, Koch) and Feetech STS/SCS (SO-101, Amazing Hand, HOPEJr); the OEM hands use coreless-plus-planetary or lead-screw units that are either unpurchasable or $200–400 each. There is no hidden supplier of an 18 g current-controlled servo; the practical substitutes are the ones in §2 and §3.

## 6. Recommendation, ranked by least design change × fastest delivery

1. **Feetech STS3032 + Seeed XIAO bus board** ($32.99 Babsco, 1 unit; roboticscenter.ai SF stock, ships ~48 h, price on request; board $5.99 US). 20.6 g, 0.44 N·m, 111 rpm, 12-bit magnetic, coreless, runs on the existing 5 V rail. Changes: new P13 pocket (23.2 × 12.1 × 28.5, half the XL330 width) and P16 spline adapter, Feetech bus board on a spare OpenRB UART, firmware port of the position/current-limit layer to STS registers, re-calibrated force ceiling. Order from both US sellers today; cancel the duplicate.
2. **Feetech STS3215 7.4 V** ($20 Seeed US warehouse; $25.99 Amazon Oct 8–14; RCmall 6-pack Prime next-day). Same firmware and board changes as (1) plus a 6–7.4 V rail, a standard-servo cradle, and +37 g on the head; 2 Hz ceiling. Ships tomorrow; the "something on the bench this week" option, not the one to fly on the crown.
3. **Stay Dynamixel**: keep the robotis.us back-order (2 months), email ROBOTIS Korea to resolve the 40-day-vs-in-stock contradiction ($23.90 + DHL $30–40 + duty), ring RoboSavvy UK (£22.67, stock not shown), and if money matters less than time buy the **XC330-M288-T** when the 1-month lead clears: it is the only true drop-in (same control table, mounting, horn, cable; +5 g; 2.5 Hz ceiling; louder metal gears). Nothing in this family lands inside a week.

Do not use: XL430 (no current sensing), Hiwonder LX (no torque limit), gimbal BLDC on the head (torque), hobby micro servos without an added current sensor or clutch.

## 7. Pages not loaded

RobotShop (Cloudflare bot check in WebFetch and the browser pane; prices quoted from search snippets only); Amazon FPBIGCHA XL330 listings ("Page Not Found"); Mouser (timed out; "Obsolete" from the search snippet); DigiKey (403); Hiwonder product pages render without a price in the fetcher (Amazon prices used); vecrobot.com (DNS failure); Pololu DRV8871 page 404 (Adafruit's used); Waveshare and DFRobot warehouses paused for China's National Day until Oct 5 / Oct 8.
