# SP1 v3 "PUPPET HALO, LEAN" — TEST PROTOCOLS (Stages A, B, C, D)

**Project SCRATCH · 14-build/tests · Test Protocols work package · 2026-10-02**
**Binds to:** 12-sp1v2/SYSTEM-SPEC-v3.md (freeze v3: §7 safety, §10 gates, §8.6 commands), 12-sp1v2/safety-ruling-dish-gate.md §4 (conditions C1–C8), 01-foundations/safety-requirements.md (§2 limits, §6 template, §7 red lines), 01-foundations/hair-interaction.md (§6.8 checklist, §7 bench method), DECISION-2 north-star amendment, DECISION-3.
**Reuses:** 05-engineering/test-protocols.md (Float-Arm): checklist layout, stop rules, wig-head test, tape test, ABBA pairs, session log, packing list. Rewritten for v3 hardware.
**Not in this file:** Stage S0 (tape fit, hinge evening, dish bench, Klipper test, tendon ink rig). It lives in **14-build/S0/**. This file only lists what S0 hands forward (§4).
**Spec items that cannot be tested as written:** collected in §15 and in 14-build/tests/CONFLICTS.md, each with the operational definition used here.

**Print and keep at the bench:** §1 kit list, §5–§10 data sheets for the stage you are in, §11 checklist (one per session), §12 feedback form (one per bout), §13 session log (one per session), §14 blind guide (give it to the helper).

---

## Contents

0. How to use this document
1. Test kit (equipment), with prices
2. Measurement recipes (force with a kitchen scale, 240 fps timing, sound, pressure, the fast force logger)
3. Stopping rules (bench and human)
4. What S0 hands forward
5. Stage A gates A0–A5 and the Stage A sensation point
6. Hair bench HB-0…HB-11, including the RC1 rim-snag tether rig
7. Stage B gates B1–B6 and the first sessions
8. Stage C gates C1–C8 and the wearability session
9. Stage D sessions D1–D4
10. Stage D5 blind experiment matrix
11. Pre-human safety checklist v3 (PHC-A once per build state, PHC-B every session)
12. Feedback form (amended goal) + CSV header
13. Session log template + CSV header
14. How to have a helper run a blind test
15. Spec items not testable as written (summary)
16. One-page gate summary

---

## 0. How to use this document

### 0.1 Order of work

```
S0 (14-build/S0/) ─GO─► buy Cart 2 ─► A0 → A1 → A2 → A3 → A4 → A5 ─► HB-mini + PHC-A(bench pad) ─► A-S (Michael's head)
   ─GO A─► buy Cart 3 ─► B1 → B2 → B3 → B4 → B5 (full hair bench) → B6 (PHC-A + PHC-B) ─► B-S sessions 2 → 5 → 10 → 20 min
   ─GO B─► buy Cart 4 ─► C1 … C8 ─► C-S (20 min MIX) ─► D1–D4 evenings ─► D5 blind matrix ─► GO D (SP1 hypothesis)
```

Never skip ahead. **The next cart is bought only after the previous GO** (spec §10). A gate is "passed" only when its results sheet is filled, dated and initialled. Keep every sheet in a ring binder and type the rows into the CSV files named on each sheet (folder `14-build/tests/results/`, create it on first use).

### 0.2 Names used in this file

- **RC1–RC8** = the eight conditions of the safety ruling (spec §7.3 calls them C1–C8). Written "RC" here so they are never confused with **Stage C gates C1–C8**.
- **Gate** = a numbered test with a pass line from the spec (A0…C8). **Sensation point** = a rated run on Michael's head that the stage's GO also needs (A-S, B-S, C-S).
- **Bout** = one continuous run of the pad on the head at one setting and one station, ended by a nails-up rest. **Trial** = one bout plus its feedback form. **Session** = one evening, ≤ 20 min of contact (spec §8.1 cap), ≤ 5 min for any first exposure (red line 12).
- **Station** = an α detent (15° steps) × β detent (10° steps). Written `α45β-10`.
- **Settings code** = the short code the firmware prints on every log line (`C` record, spec §8.6). Copy it onto every form; never describe a setting in words only.
- **Michael** = the person on whose head the device runs. **Helper** = anyone else present. The helper never holds the hold-to-run lever.

### 0.3 Units and conversions you will use constantly

A kitchen scale reads grams. Force in newtons = grams × 0.00981. The spec's force numbers, in grams:

| Spec force | grams | Spec force | grams | Spec force | grams |
|---|---|---|---|---|---|
| 0.05 N | 5.1 g | 0.385 N | 39.3 g | 2.0 N | 204 g |
| 0.10 N | 10.2 g | 0.50 N | 51.0 g | 2.5 N | 255 g |
| 0.12 N | 12.2 g | 0.80 N | 81.6 g | 3.0 N | 306 g |
| 0.15 N | 15.3 g | 0.92 N | 93.8 g | 3.1 N | 316 g |
| 0.20 N | 20.4 g | 1.04 N | 106 g | 4.6 N | 469 g |
| 0.25 N | 25.5 g | 1.5 N | 153 g | 6 N | 612 g |
| 0.30 N | 30.6 g | 1.93 N | 197 g | 12 N | 1,224 g |
| 0.35 N | 35.7 g | | | 20 N | 2,040 g |

Pressure: 1 psi = 6.895 kPa. 1 kPa = 10.2 cm of water column. 20.7 kPa = 3.0 psi; 24 kPa = 3.5 psi; 30 kPa = 4.35 psi; 50 kPa = 7.25 psi.
Video: at 240 fps one frame = 4.17 ms. 20 ms ≈ 5 frames; 50 ms = 12 frames; 100 ms = 24 frames; 150 ms = 36 frames; 200 ms = 48 frames.
**Weights you already own:** a US nickel is 5.00 g; a US penny (1983 or later) is 2.50 g. Five nickels = 25.0 g = 0.245 N, the per-session nail hang test (RC1 e).

### 0.4 Price tags

Prices were checked on 2026-10-02: **[cited]** = URL given in §1; **[est]** = estimate; **[verify]** = check before buying. Items already in the spec's tools list (≈ $185: soldering, calipers, scales, logic analyser, tube cutter) or in an earlier cart are marked **(owned)** and not counted again.

---

## 1. Test kit (equipment)

Buy the **S0/A test kit** with Cart 2 and the **B test kit** with Cart 3. Everything is cheap on purpose.

### 1.1 Test kit list

| # | Item | Used in | Price | Tag / source |
|---|---|---|---|---|
| K1 | Kitchen scale, 1 g, ≥ 3 kg, tare | B1, B2, C2, C6, many | $12 | (owned, tools list) [est] |
| K2 | Pocket scale 100 g × 0.01 g, tare (e.g. American Weigh AWS-100) | A2, HB, PHC-B | ≈ $15–17 | [cited] amazon.com/clp/B002SVLB8E |
| K3 | Digital luggage scale 50 kg (hook) | B3 mount, C6 clip, C7 lip force | ≈ $5–10 | [cited] amazon.com (Amazon Basics 110 lb) [verify current price] |
| K4 | Digital calipers 150 mm | A2, A3, B3 | — | (owned, tools list) |
| K5 | Feeler gauge set 0.04–1.00 mm, 32 blades | A3 (lift ≥ 5 mm with a stack), C8 gaps | $4.99 | [cited] Harbor Freight Pittsburgh 32-pc, harborfreight.com/32-piece-sae-metric-feeler-gauge-32214.html |
| K6 | Phone with **240 fps** slow motion, sound-meter app (A-weighted; iOS: NIOSH SLM), inclinometer, stopwatch, voice memo | everywhere | $0 | (owned) |
| K7 | Clip-on macro lens + small LED desk lamp | A3, HB, B4 | $10 + $0 | [est] |
| K8 | USB logic analyser 24 MHz 8 ch (Saleae-clone, PulseView/sigrok) | A0, A4 | $10–14 | (owned, tools list) [cited] amazon.com HiLetgo 24 MHz 8 ch |
| K9 | **Fast force logger:** Raspberry Pi Pico | RC1(c)(d), A4, HB-6/7/11 | $4.00 | [cited] adafruit.com/product/4864 |
| K10 | **ADS1115** 16-bit ADC breakout (a second one; the box's ADS1115 stays in the box) | fast logger | $14.95 (Adafruit) or ≈ $6 (clone) | [cited] adafruit.com/product/1085 |
| K11 | **Load cell 100 g**, straight bar TAL221 (SparkFun SEN-14727) | RC1(a)(c)(d), HB-11 slip loop | $14.50 | [cited] sparkfun.com/mini-load-cell-100g-straight-bar-tal221.html |
| K12 | **Load cell 500 g**, straight bar TAL221 (SEN-14728), 0.7 ± 0.15 mV/V | A4 reflex trip, B2 coupling pull | $15.50 | [cited] sparkfun.com/mini-load-cell-500g-straight-bar-tal221.html |
| K13 | Spare XGZP6847A 0–40 kPa sensor + tee (for the gallery tee) | A2 RC3 vent trace | $5 | (same part as the box BOM) [est] |
| K14 | **0–15 psi (0–103 kPa) dial gauge, 1/8 NPT** + 1/8 NPT to 4 mm push-fit | A1 deadheads | $5–16 | [cited] compressor-source.com 1/8 NPT 0–15 psi ($4.95); buyfittingsonline.com ($15.98) |
| K15 | Water U-tube manometer: 2.5 m clear vinyl tube 6 mm ID, tape measure, food colouring, tape to a door frame | A1 sensor calibration 0–12 kPa | $6 | [est] |
| K16 | **Real-hair mannequin head** (cosmetology, 100 % human hair, with table clamp) ×2: trim one to 3–5 cm; keep one long | HB, B5, C8 | $30–40 each | [cited] amazon.com (Opini / TopDirect / Hairingrid, $29.69–39.99) |
| K17 | Kanekalon braiding hair, 1 pack (conservative wrap screen, pinned to a foam head) | HB-4, HB-8 | $5–15 | [cited] mybeautymart.com Superline 3-pack $4.99 |
| K18 | Paper-covered Ø 170 ball (R 85), R 65 mock, 70 × 150 side mock | A3, HB-6 | — | from the S0 dish bench (owned) |
| K19 | 0.25 mm nylon monofilament (fishing line, ≈ 10 lb) and 0.1 mm (≈ 2 lb) | A2, A4, HB | $5 | [est] |
| K20 | Wide-tooth comb, lint roller, black cotton cloth 1 × 1 m, hair clips | HB, sessions | $8 | [est] |
| K21 | Hygrometer/thermometer | HB-10, every session | $10 | [est] |
| K22 | IR thermometer | A5 thermal, B | $15 | [est] |
| K23 | 10 mm wooden dowel + 50 µm PTFE or polyester tape (3 layers) | B3 tape test | $5 | [est] |
| K24 | Two binder clips, a hemostat or small spring clamp (kinks a tube), 2 mm drill, small smooth pulley (or a polished rod edge) | A2, HB-6 | $6 | [est] |
| K25 | Lazy-susan bearing turntable 150 mm + dowel lever arm | C6 yaw torque | $10 | [est] |
| K26 | Safety glasses (clear) | every human run | $8 | (owned) [est] |
| K27 | Foam earplugs; small fan or white-noise speaker for masking | A-S, D5 | $5 | [est] |
| K28 | Divider resistors (22 k, 6.8 k, 100 k, 22 k), breadboard, jumpers | logger rail-sense, A0 | $5 | [est] |

**Test-only adds, total:** ≈ **$230** (≈ $160 at Cart 2: K2, K5, K7, K9–K15, K19, K21, K22, K24, K28 plus one wig head; ≈ $70 at Cart 3: second wig head, Kanekalon, K20, K23, K25, K27). Not in spec §13. BOM WP: please add.

**Why not an HX711?** The ruling's RC1(c) asks for "an HX711 at 1 kHz". The HX711 runs at **10 or 80 samples/s only** (datasheet, RATE pin) [cited: cdn.sparkfun.com/datasheets/Sensors/ForceFlex/hx711_english.pdf]. 80 samples/s is one sample every 12.5 ms, so it cannot show "≤ 20 ms above 0.15 N". The ADS1115 reads a load-cell bridge differentially at **860 samples/s** (1.16 ms) [cited: adafruit.com/product/1085]. That is the K9–K11 logger. An HX711 kit is fine for slow, static forces (B2, B3) if you already have one; the kitchen scale does those too.

### 1.2 Sources checked 2026-10-02

- HX711 data rate 10/80 SPS: https://cdn.sparkfun.com/datasheets/Sensors/ForceFlex/hx711_english.pdf
- TAL221 100 g, $14.50: https://www.sparkfun.com/mini-load-cell-100g-straight-bar-tal221.html
- TAL221 500 g, $15.50, 0.7 ± 0.15 mV/V: https://www.sparkfun.com/mini-load-cell-500g-straight-bar-tal221.html
- ADS1115, 860 SPS, $14.95: https://www.adafruit.com/product/1085
- Raspberry Pi Pico, $4.00: https://www.adafruit.com/product/4864
- Real-hair mannequin heads $29.69–48.99: https://www.amazon.com/100-real-human-hair-mannequin-head/s?k=100%25+real+human+hair+mannequin+head
- 0–15 psi 1/8 NPT gauges $4.95–15.98: https://compressor-source.com/products/1-8-npt-0-15-psi-air-pressure-gauge-lower-side-mount-with-1-5-face , https://www.buyfittingsonline.com/pressure-gauges-standard-dry-air-1-1-2-in-face-1-8-in-lower-mount-0-15-psi/
- 24 MHz 8 ch logic analysers $9.99–14: https://www.amazon.com/HiLetgo-Analyzer-Device-Ferrite-Channel/dp/B0FRFF6GLP
- Pocket scale 100 g × 0.01 g: https://www.amazon.com/clp/B002SVLB8E
- Feeler gauge 32-pc $4.99: https://www.harborfreight.com/32-piece-sae-metric-feeler-gauge-32214.html
- Kanekalon 3-pack $4.99: https://mybeautymart.com/3-pack-kanekalon-braid/
- Luggage scale 50 kg: https://www.amazon.com/Wifehelper-Luggage-Portable-Electronic-Digital/dp/B07Q2BT612

---

## 2. Measurement recipes

Each gate below says "use recipe R-x". Learn these once.

### R-1 Small forces with the pocket scale ("reverse-reading pull")

Use this for any pull of 0.05–0.5 N (nail breakaway, slip loop, friction).
1. Put a **50 g** mass (ten nickels in a small bag) on the pocket scale. Tare is OFF; the scale reads ≈ 50.00 g.
2. Tie a 0.1 mm monofilament line from the bag to the thing you are pulling (for example a loop round a nail cone). Leave 5 mm of slack.
3. Raise the part slowly (screw a lab jack, or lift the bench block on a stack of cards one card at a time). As the line tightens, the scale reading **falls**.
4. Watch for the moment the part lets go (the reading jumps back to ≈ 50 g). The pull at release = 50.00 g − **lowest reading seen**. Film the display at 240 fps if it moves too fast to read; step through the frames.
5. Convert with §0.3. Example: lowest reading 31.2 g → pull 18.8 g → 0.184 N.

### R-2 Bigger forces with the kitchen or luggage scale

- **Push** (normal force): the part presses down onto the kitchen scale (tare first). Read directly.
- **Pull** (≥ 1 N): hook the luggage scale on and pull slowly along the line of action; read the peak (most luggage scales have a hold function; otherwise film the display).
- **Sideways pull** with a kitchen scale: run the line over a smooth pulley (or polished rod) so it pulls straight down onto a weight sitting on the scale; same reverse-reading method as R-1.

### R-3 Timing with 240 fps video

1. Check your phone really records 240 fps: film a running stopwatch app on a second screen for 2 s and count frames per 1 s of displayed time (should be 240 ± 2). iPhone: Photos ▸ ⓘ shows "240 fps".
2. Put **a 5 mm LED on a 1 k resistor across the 12 V actuator rail (ACT-12)** in the frame. LED off = rail dead. This gives you the electrical event in the same video as the mechanical one.
3. Put a **mm ruler** (steel rule) in the frame, in the same plane as the motion, and light the scene from the side with the desk lamp.
4. Count frames from the event (LED goes dark, or the nail starts moving) to the end condition. Time = frames × 4.17 ms. Count twice; use the larger.

### R-4 Sound with a phone

Phones cannot measure below about 30–35 dBA, and a Naples apartment with AC running is often 35–45 dBA. So:
1. Use an A-weighted app (iOS: NIOSH SLM, free). Read **LAeq over 30 s**.
2. Measure **room only** (device off) and **room + device**, same spot, same time of day, AC off if you can.
3. Background correction: difference 10 dB or more → no correction; 6–9 dB → subtract 1 dB; 4–5 dB → subtract 2 dB; 3 dB → subtract 3 dB; under 3 dB → "device below room noise", record "≤ room".
4. To check a "≤ 30 dBA at 1 m" line you cannot read at 1 m, measure at **0.25 m** and subtract **12 dB** (free-field distance law, 20 log 4). Record both numbers. See §15 item 5.

### R-5 Pressure

- **0–12 kPa, accurate:** water U-tube manometer (K15). Tape a 2.5 m clear tube in a U on a door frame, half fill with coloured water, connect one end to the line under test. Pressure (kPa) = height difference between the two water surfaces (cm) ÷ 10.2. Use it to check the box sensors at 2, 5, 10 kPa (sensor reading within ±0.5 kPa).
- **12–100 kPa:** 0–15 psi dial gauge (K14) on a tee. Read at eye level, tap the glass once before reading.
- **Fast (≥ 100 samples/s):** a spare XGZP6847A on the Pico ADC (R-6, second mode).

### R-6 The fast force logger (Pico + ADS1115 + TAL221)

**Build (≈ 45 min).**
1. Load cell: bolt one end of the TAL221 bar (two M3 screws) to a rigid block glued to the bench; the other end is free. Its arrow points in the direction of the force. Glue a small hook (bent paper clip) on the free end. **Fit an overload stop:** an M3 screw under the free end with 0.3 mm clearance (one feeler blade), so a big pull cannot overload the bar.
2. Wiring (3.3 V excitation):
   - TAL221 red (E+) → Pico 3V3 (pin 36); black (E−) → GND (pin 38); green (A+) → ADS1115 A0; white (A−) → ADS1115 A1.
   - ADS1115 VDD → 3V3, GND → GND, SDA → Pico GP0 (pin 1), SCL → GP1 (pin 2), ADDR → GND (address 0x48).
   - **Rail sense:** ACT-12 → 22 kΩ → Pico GP15 (pin 20) → 6.8 kΩ → GND (12 V gives ≈ 2.8 V). Join the box GND to the Pico GND with one wire.
3. Install MicroPython on the Pico (hold BOOTSEL, plug in, drag the .uf2 from raspberrypi.com), install **Thonny** on the PC, save this as `tether_logger.py` on the Pico:

```python
# tether_logger.py  (Raspberry Pi Pico, MicroPython)
# ADS1115 differential A0-A1, +/-0.256 V, continuous, 860 SPS; logs rail sense on GP15.
from machine import I2C, Pin
import time, array
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
ADDR = 0x48
i2c.writeto_mem(ADDR, 0x01, bytes([0x8A, 0xE3]))   # config: MUX=A0-A1, PGA=0.256 V, continuous, 860 SPS
rail = Pin(15, Pin.IN, Pin.PULL_DOWN)
N = 8000                                          # 8000 samples = about 9.3 s
t = array.array('l', [0] * N)
v = array.array('h', [0] * N)
r = bytearray(N)
buf = bytearray(2)
input("Press Enter to start a 9 s capture")
t0 = time.ticks_us()
nxt = t0
for i in range(N):
    while time.ticks_diff(time.ticks_us(), nxt) < 0:
        pass
    nxt = time.ticks_add(nxt, 1163)               # one ADS1115 conversion period
    i2c.readfrom_mem_into(ADDR, 0x00, buf)
    x = (buf[0] << 8) | buf[1]
    v[i] = x - 65536 if x > 32767 else x
    t[i] = time.ticks_diff(time.ticks_us(), t0)
    r[i] = rail.value()
print("t_us,raw,rail")
for i in range(N):
    print("%d,%d,%d" % (t[i], v[i], r[i]))
```

4. **Calibrate** every time you move the cell: run with nothing on the hook (zero, average the raw values = Z), then hang **2, 4 and 10 nickels** (10, 20, 50 g) on the hook (100 g cell) or 10, 20, 40 nickels on the 500 g cell. Fit grams per count, S = mass ÷ (raw − Z). Expect ≈ 0.4 g per count for the 100 g cell at 3.3 V, ≈ 1.7 g per count for the 500 g cell [est from 0.6–0.7 mV/V]. If the zero drifts > 3 counts in 10 s, let the cell warm up 10 min.
5. **Use:** start the capture, then start the event within 9 s. Copy the printed lines from Thonny's shell into `tether_YYYYMMDD_run.csv`. Force (N) = (raw − Z) × S × 0.00981.
6. **Read the results** with this PC script (Python 3, no extra packages):

```python
# analyse_tether.py  usage: python3 analyse_tether.py file.csv Z S
import sys, csv
f, Z, S = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
rows = [(int(a), int(b), int(c)) for a, b, c in list(csv.reader(open(f)))[1:]]
F = [((b - Z) * S * 0.00981, a, c) for a, b, c in rows]
peak = max(F)
above = [a for n, a, c in F if n > 0.15]
t_above = (above[-1] - above[0]) / 1000 if above else 0.0
print("peak %.3f N at %.1f ms" % (peak[0], peak[1] / 1000))
print("time between first and last sample above 0.15 N: %.1f ms" % t_above)
for thr in (0.15, 0.8):
    t_thr = next((a for n, a, c in F if n > thr), None)
    t_dead = next((a for n, a, c in F if t_thr is not None and a > t_thr and c == 0), None)
    if t_thr is not None and t_dead is not None:
        print("force > %.2f N -> rail dead: %.1f ms" % (thr, (t_dead - t_thr) / 1000))
```

**Second mode (fast pressure, RC3 vent trace):** wire the spare XGZP6847A (5 V supply from Pico VBUS pin 40, output through 10 kΩ / 20 kΩ divider → 0.33–3.0 V) to Pico **GP26/ADC0**, and the PIN-valve coil's low side through the 22 k / 6.8 k divider to GP15. In the script replace the ADS1115 read with `v[i] = adc.read_u16() >> 4` (with `from machine import ADC; adc = ADC(26)`) and the period with `1000` µs (1 kHz). Calibrate against the manometer at 0, 2 and 10 kPa.

---

## 3. Stopping rules

These apply in every stage. They override any procedure step. Print this page and tape it above the bench.

### 3.1 Bench (no human)

Stop, release the lever, press the e-stop, and do not restart until the cause is found and logged, if:
- the actuator rail does not die when the lever is released, or the weld check fails (FAULT at ARMING);
- anything moves that you did not command, or the block moves with the lever released;
- a nail is missing or a nail released when it should not (nuisance release) — **find the nail first**;
- you smell hot plastic or electronics, or any part reads > 48 °C by touch or IR;
- a hair, fibre or monofilament is found inside a gap, wiper, guide or the yoke cage;
- a pressure reads above its relief (pin rail > 22.2 kPa with R1a fitted; palm > 25.5 kPa with R2 and R2b) — a relief has failed;
- a printed part cracks, a fastener loosens, or a tendon frays.

### 3.2 Human (Michael's head) — release first, think second

**Release the lever (or lift the forearm off the armrest switch) at once on:** any pull you feel; any pain, sharp prick or burning; a catch or "snag"; the pad pressing rather than resting; an unexpected sound; the hat moving suddenly; dizziness, neck pain or headache; the helper saying "stop". Releasing costs nothing: the pins vent and the pad lifts.

Then press the e-stop, take the helmet off (§7.7 of the spec: release, grab the doff lip, tilt up and back), and look at the scalp and the pad **before** deciding anything.

| Event | Rule |
|---|---|
| **Tuft pull** (more than a few hairs at once, or a patch that hurts after) | **End the session. No further human sessions** until a redesign item is logged and the hair bench HB-3…HB-8 is passed again. |
| A single felt pull | End the bout. Count nails. If it happens twice in a session, end the session. In Stage B any felt pull fails GO B for that session. |
| Pain or discomfort ≥ 4/10 | End the session. Next session at the previous (lower) setting. |
| Any skin break, bleeding, or a mark still there next morning | **Stop all human testing** until a written review (what caused it, what changed). |
| Nail count after a session ≠ 6 | Find the missing nail (pad, hair, towel, floor) before the next session. Log it. A nail found in the hair is a reflex/RC1 event: check the log for a trip. |
| Two reflex trips in one session, or any FAULT | End the session; diagnose on the bench (`tensions`, `sensors`, log). |
| Redness lasting > 60 min | Skip the next day. |
| PHC-B has an unticked box or an out-of-limit value | No session that day. |
| Michael tired, unwell, drowsy, or has had alcohol | No session. (The lever and the 20-min cap protect against sleep; do not test that.) |

### 3.3 Stage-level stops (spec §10 NO-GO actions)

- **Stage A:** sensation < 6/10 → tip, force and variation A/B before any halo work (spec §10).
- **Stage B:** < 5/10 → fix the pad (cone, force, variation) before Stage C; 5–6/10 → run the Stage D experiment matrix first.
- **Stage D:** on evidence, powered drift if "having to move it" > 3/10; pad 2 if lean is felt.

---

## 4. What S0 hands forward (do not repeat S0 here)

S0 procedures and data sheets are in **14-build/S0/**. Before starting Stage A, copy these numbers onto the first page of the Stage A binder (each comes from an S0 sheet):

| From S0 | Needed by |
|---|---|
| Michael's tape fit (V1): head lengths, hairline α, ear positions | C1 stops, C4 fences |
| Michael's hair: length (cm) and pile (mm) at crown, occiput, both parietals; grain direction per region; whorl position | B-S stations, D-paths, LINE grain table, HB wig choice |
| Dish bench: chord, lift, landing angle, spread; the helper-held rating ("scratch not brush", "crisp on both flanks", ≥ 6/10) | A3 comparison, A-S anchor |
| Klipper test V-K1/V-K2 result and the kinematics route chosen (§8.2: GCODE_AXIS, or fallback 1, or fallback 2) | A3 |
| Tendon ink rig: bow, circle flats, shrink, drift, dead band per cable, earplug A/B result | A3, C5 |
| Hinge evening: "having to move it" score, cradle lean | C-S comparison |

If S0 did not record Michael's hair numbers, do it now (10 min): part the hair at each region, hold a steel rule against the scalp, read length; press a ruler lightly on the hair and read pile height; comb gently in four directions and note which way the hair lies flat (grain). Photograph.

---

## 5. Stage A — bench puppet (gates A0–A5, then the sensation point A-S)

**Entry:** GO S0 recorded; Cart 2 delivered; firmware WP has delivered `printer.cfg`, `scorer.py`, `reflexd`, `scratchctl` with the §8.6 commands; ELECTRONICS WP has delivered the bring-up procedure. Nothing in Stage A touches a head except A-S, and A-S has its own entry rules (§5.7).
**Bench layout:** drive box parts on a table; bench pad on the R 85 ball (K18); the e-stop puck under your left thumb and the hand controller in your right hand **for every powered test**, even on the bench.

### 5.1 A0 — Safety loop on a board

**Pass line (spec §10):** each element opens ACT-24 within 5 ms (logic analyser), logic stays up; weld check fires on a jumpered K1; 10 cycles each. Plus V-K3 (watchdog on host loss), V-E1…V-E4 bring-up items.
**Kit:** logic analyser (K8) with PulseView, divider 100 k / 22 k (24 V → 4.3 V), multimeter, the safety loop board, the M8P + CB1 powered from the adapter.
**How the 5 ms is measured (see §15 item 3):** the 470 µF and TVS on ACT-24 hold the bus up after K1 opens, so the bus voltage itself may take longer than 5 ms to fall with light loads. Measure two things: **(a)** K1's **auxiliary NC contact** closing (it is force-guided, so NC closed = NO contacts open) on analyser channel 1, and **(b)** ACT-24 through the divider on channel 2. Pass = (a) ≤ 5 ms after the element opens; (b) below 2 V within 50 ms (the weld-check window). If (b) is slow, ask ELECTRONICS for a bleeder resistor on ACT-24 (e.g. 2.2 kΩ 1 W).

**Steps.**
1. Wire analyser: CH0 = the element under test (its contact, via a divider if > 5 V), CH1 = K1 aux NC (pulled up to 3.3 V), CH2 = ACT-24 divider, CH3 = M8P 3.3 V rail (logic stays up). GND to box GND. Sample 1 MHz, trigger on CH0 edge.
2. Hold the lever; confirm ACT-24 = 24 V ± 1 V on the meter.
3. For each element below, 10 cycles: open it, capture, note t(aux) and t(bus < 2 V), re-close, re-arm (release lever, re-hold).
   - E-stop puck pressed.
   - Lever released.
   - REFLEX latch: (i) press a cable flexure by hand until the comparator trips; (ii) from the host: `inject snag` (bench).
   - Helmet loop: unplug the lanyard pogo; separately, open the head-present switch.
   - Watchdog: (i) stop the PWM (`FIRMWARE_RESTART` in the Klipper console); (ii) kill the host (unplug the CB1 network and stop `scorer.py`/Klipper host with `sudo systemctl stop klipper`) and time until the rail opens (spec: ≤ 50 ms after PWM stops; host hang ≤ 1 s per §7.8).
4. **Logic stays up:** after every cycle, CH3 still 3.3 V and `status` answers on the console.
5. **Weld check:** power off, jumper K1's NO contacts with a clip lead (simulated weld), power on, hold and release the lever. Pass = host refuses ARMING with a weld-check FAULT, 10/10. **Remove the jumper; tick it off on the sheet.**
6. **Restart rule:** after each element, hold the lever again: the host must go through ARMING (drums home, pad side retracted), never resume a path.
7. **V-E1/V-E2 checks:** meter the M8P driver-supply jumper position (motor input = ACT-24); with ACT-24 dead, the drivers have no motor voltage while the CB1 is up; each low-side output switches a 12 V test lamp only when ACT-12 is live.

**A0 results sheet** — CSV `results/A0.csv`: `date,element,cycle,t_aux_ms,t_bus2V_ms,logic_up,restart_ok,notes`

| Element | Cycles passed /10 | max t(aux) ms (≤ 5) | max t(bus < 2 V) ms (≤ 50) | Logic up 10/10 | Restart via ARMING 10/10 | ✓ |
|---|---|---|---|---|---|---|
| E-stop | | | | | | ☐ |
| Lever release | | | | | | ☐ |
| Latch – comparator | | | | | | ☐ |
| Latch – host GPIO (`inject snag`) | | | | | | ☐ |
| Lanyard pogo | | | | | | ☐ |
| Head-present switch | | | | | | ☐ |
| Watchdog – Klipper restart | | | | | | ☐ |
| Watchdog – host killed (≤ 1 s) | | | | | | ☐ |
| Weld check (jumpered K1) | /10 FAULT | — | — | — | jumper removed ☐ | ☐ |
| V-E1 motor input jumper, V-E2 low-side, V-E3 ADC count, V-E4 CB1 GPIO/I²C | | | | | | ☐ |

Date ______ Build state ______ Initials ____ **A0 PASS ☐**

### 5.2 A1 — Pneumatics: reliefs, deadheads, rail control

**Pass line (spec §10):** R1a 20.7 ± 1.5 kPa, R1b ≈ 24 ± 1.5, R2 20.7 ± 1.5, R2b ≈ 24 ± 1.5 (5 trials each); deadheads measured: **P1 ≤ 50 kPa, P3 ≤ 30 kPa**; rail PID ± 0.5 kPa. (V9, V12.)
**Kit:** manometer (K15), 0–15 psi gauge (K14) on a tee, push-fit plugs, the box sensors read with `sensors`.
**Why the gauge:** the box sensors are 0–40 kPa (XGZP6847A). The P1 deadhead pass line is 50 kPa, which they cannot read. Use the dial gauge (§15 item 2).

**Steps.**
1. **Sensor check (once):** connect the rail tee to the manometer. Pump by `pump 1 <duty>` (diagnostic, pad retracted) to 2, 5 and 10 kPa on the manometer; record `sensors`. Each sensor within ±0.5 kPa, else fix its kPa table in `printer.cfg`. Repeat for line A, line B and palm sensors.
2. **R1a:** plug PIN A and PIN B outlets. Cap R1b's port (so only R1a can relieve). Run P1 at 100 % (`pump 1 1.0`) for 20 s. Read the steady rail on the sensor and the dial gauge. Vent (pump off, dump open). 5 trials. Pass: each 19.2–22.2 kPa.
3. **R1b:** cap R1a's port, uncap R1b. Same 5 trials. Pass: within ±1.5 kPa of its own nominal (≈ 24) and **higher than R1a** (R1a must be the working relief).
4. **R2, R2b:** same on the palm side with P3 (`pump 3 1.0`), PALM outlet plugged.
5. **Deadheads:** cap **both** reliefs on one side; run the pump at 100 % for 30 s with the dial gauge on the tee (the 0–40 kPa sensor may read full scale — that is expected). Read the gauge. **Uncap the reliefs immediately after.** Pass: P1 ≤ 50 kPa (7.25 psi), P3 ≤ 30 kPa (4.35 psi). If a pump exceeds its line, that pump is not allowed (red line 2 depends on it): change pump or fit an inlet restrictor and repeat.
6. **Rail control:** reliefs uncapped, outlets plugged. Set the rail to 4, 8, 12 kPa (`force` equivalent on the rail, or the firmware's rail setpoint); log `sensors` at 1 Hz for 60 s each. Pass: every reading within ±0.5 kPa of the setpoint after a 5 s settle.
7. **Dumps:** with the rail at 12 kPa, release the lever. Rail < 1.3 kPa within 50 ms (240 fps on the dial gauge, or the fast logger second mode).
8. **Seal (spec §5.2):** pin lines with the gallery bleed plugged: ≤ 1 kPa/min decay from 10 kPa; palm ≤ 2 kPa/min (excluding the Airpel, which is fitted in B).

**A1 results sheet** — CSV `results/A1.csv`: `date,item,trial,kPa_sensor,kPa_gauge,pass,notes`

| Item | T1 | T2 | T3 | T4 | T5 | Limit | ✓ |
|---|---|---|---|---|---|---|---|
| R1a kPa | | | | | | 19.2–22.2 | ☐ |
| R1b kPa | | | | | | nominal ± 1.5, > R1a | ☐ |
| R2 kPa | | | | | | 19.2–22.2 | ☐ |
| R2b kPa | | | | | | nominal ± 1.5, > R2 | ☐ |
| P1 deadhead kPa (gauge) | | | | | | ≤ 50 | ☐ |
| P3 deadhead kPa (gauge) | | | | | | ≤ 30 | ☐ |
| Rail PID error at 4 / 8 / 12 kPa | ___ / ___ / ___ | | | | | ≤ ±0.5 | ☐ |
| Rail dump to < 1.3 kPa (ms) | | | | | | ≤ 50 | ☐ |
| Seal decay pin A / pin B / palm (kPa/min) | ___ / ___ / ___ | | | | | ≤ 1 / 1 / 2 | ☐ |
| Sensor check vs manometer (rail, A, B, palm) | | | | | | ±0.5 kPa | ☐ |

Reliefs uncapped after the test ☐ Date ______ Initials ____ **A1 PASS ☐**

### 5.3 A2 — Six pins in the bench block (RC1 a/b, RC2, RC3, RC6, RC7, force)

**Pass line (spec §10):** RC1 (a)(b); RC2 shadowgraph + slip loop; RC3 scope trace ≤ 100 ms, bleed < 1 s, relief with B at 100 % ≤ 1.04 N; RC6 calipers; RC7 retract ≥ 8 mm in 200 ms; force at 10 kPa = 0.385 ± 0.04 N net of spring. Also V4 (sleeve life), V-N1, V-N2, V-P1.
**Kit:** pocket scale (K2), 0.1 mm monofilament, 50 g side-load mass, fast logger in pressure mode (R-6), spare sensor and tee (K13), hemostat (K24), calipers, 240 fps phone, nail shadowgraph template (PAD WP), a hair from the wig.
**Setup:** SLA bench block clamped nails **down** above the bench, real galleries A/B, 1.6 m lines, both S070s. Number every nail with a dot of paint on its shaft top: N1…N6 plus spares S1…Sn. Every nail made gets tested, spares included.

**A2.1 RC1(a) — breakaway force, 10× per nail (V-N2).**
1. Pins vented. Tie a 0.1 mm monofilament slip loop round the nail's cone, just below the Ø 4.5 shoulder.
2. Recipe R-1 with the 50 g bag on the pocket scale, line straight down along the nail axis.
3. Raise the block slowly (stack of cards) until the nail drops off the magnet. Record the pull at release. Re-seat the nail (push the shaft up through the guides onto the magnet until it clicks).
4. 10 pulls per nail. Pass: **every** pull 12.2–25.5 g (0.12–0.25 N).
5. **With side load:** hang a 51 g mass (0.5 N) on a second line from the tip over the pulley, horizontal. Repeat 10 pulls. Pass: every pull ≤ 35.7 g (0.35 N).
6. If a nail is out of range: adjust its magnet gap shim (PAD WP procedure) and repeat all 10.

**A2.2 Friction and B_min ≥ 3× aged friction (RC1, RC7).**
1. Remove the magnet's nail; push a bare shaft up through the wiper and both guides with the pocket scale under its tip (scale reading = friction while moving at ≈ 5 mm/s). Read the steady value. 3 reads per pin.
2. Repeat after A2.6 (1,000 cycles) and after the A4 20-min run ("aged").
3. Pass: smallest breakaway of that pin (A2.1) ≥ 3 × the aged friction. Return spring ≥ 2 × aged friction (spring force at contact from the PAD WP spring data, or measured on the pocket scale with the piston at 15 mm extension).

**A2.3 RC2 — profile (shadowgraph) and slip loop.**
1. Tape the printed template to a window (backlight). Hold each nail on it with the tip at the template's tip line; photograph straight on with the macro lens.
2. Pass: the outline lies on the template within the PAD WP tolerance, and **no section is narrower than any section nearer the tip** (run a fingernail down the silhouette on the photo: it must never step inward going up). No shoulder within 3 mm of the nose at full retract (calipers).
3. **Slip loop:** tie a slip loop of real hair (from the wig) round the nail mid-stem, other end to the 100 g load cell hook (R-6). Pressurise to 10 kPa, nail extended. Lift the block 10 mm by hand (≈ 1 s). Pass: the loop slides off over the tip **10/10**, logger peak ≤ 0.10 N before any breakaway (if the nail breaks away instead, that trial fails).

**A2.4 RC3 — vent time, kinked-line bleed, relief with B at 100 %.**
1. Fit the spare sensor on a tee **at gallery A** (at the block end of the 1.6 m line). Fast logger in pressure mode; valve coil sense on GP15.
2. Rail at 13 kPa, PIN A energised. Release the lever (de-energise). Capture.
3. Pass: gallery pressure < 1.3 kPa (force < 0.05 N) **≤ 100 ms** after the coil sense falls. 10 trials; repeat for gallery B. If not, fit a gallery QEV (spec C3) and repeat.
4. **Kinked line:** pressurise line A to 13 kPa, clamp the tube with the hemostat **between the valve and the gallery**, then de-energise. Pass: gallery < 2 kPa in < 1 s (bleed working). Repeat for B.
5. **Relief with B at 100 %:** rail held at R1a by running P1 at 100 % with the PIN outlets connected to the block; command line B servo to 100 % duty (`bratio 1.0`, groups b). Put one B nail on the pocket scale at contact extension. Pass: ≤ 106 g (1.04 N). Repeat for each B nail.

**A2.5 Force at 10 kPa (and RC6 stroke).**
1. Rail 10.0 kPa (checked on the manometer). One nail at a time on the pocket scale with the scale surface at the 15.0 mm contact extension (spacer under the scale).
2. Pass: **35.2–43.3 g** (0.385 ± 0.04 N) net of the spring (record also the vented reading = spring force; subtract).
3. **RC6 calipers (bench):** each pin's full stroke from the retract stop: 18.5 mm (PAD WP tolerance). The margin on curved mocks is measured in A3.

**A2.6 RC1(b), part 1 — 1,000 vent/re-pressurise cycles (and V4 start).**
1. Firmware macro (ask FIRMWARE for `cal lines` in loop form, or `valve a 300` repeated by a script): 1,000 cycles of pressurise 0.5 s / vent 0.5 s on both lines, nails free in air, a towel under the block.
2. Pass: **zero nuisance releases** (nail count 6 at the end) and no sleeve failure. (Part 2, the 20-min wig PLINE, is in A4/HB.) V4 (10⁵ cycles) runs on the separate sleeve rig overnight; log the count.

**A2.7 RC7 — retract ≥ 8 mm in 200 ms.**
1. Ruler behind the block, 240 fps, LED on the coil (R-3). All six nails down at 10 kPa on a soft foam block.
2. Vent group B only. Count frames until every B nail has risen 8 mm. Pass: ≤ 48 frames (200 ms).
3. Do it with the block axis **vertical** (vertex) and **horizontal** (sides). Repeat after the A4 20-min run.

**A2 results sheet** — CSV `results/A2.csv`: `date,test,nail,trial,value,unit,pass,notes`

| Nail | RC1(a) min–max g (12.2–25.5) | RC1(a)+0.5 N side max g (≤ 35.7) | Friction new / aged g | B_min ≥ 3× aged ✓ | Shadowgraph ✓ | Slip loop /10 | Force @10 kPa g (35.2–43.3) | Stroke mm (18.5) | B@100 % g (≤ 106) |
|---|---|---|---|---|---|---|---|---|---|
| N1 | | | / | ☐ | ☐ | | | | — |
| N2 | | | / | ☐ | ☐ | | | | |
| N3 | | | / | ☐ | ☐ | | | | |
| N4 | | | / | ☐ | ☐ | | | | |
| N5 | | | / | ☐ | ☐ | | | | |
| N6 | | | / | ☐ | ☐ | | | | |
| S1 | | | / | ☐ | ☐ | | | | |
| S2 | | | / | ☐ | ☐ | | | | |

(Group B = C, P1, P4: fill the last column only for those.)

| Item | Value | Limit | ✓ |
|---|---|---|---|
| Vent A: worst of 10 (ms) | | ≤ 100 | ☐ |
| Vent B: worst of 10 (ms) | | ≤ 100 | ☐ |
| Kinked line A / B to < 2 kPa (s) | / | < 1 | ☐ |
| 1,000 cycles: nuisance releases | | 0 | ☐ |
| RC7 retract vertex / sides, new (ms) | / | ≤ 200 | ☐ |
| RC7 retract vertex / sides, aged (ms) | / | ≤ 200 | ☐ |

Date ______ Initials ____ **A2 PASS ☐**

### 5.4 A3 — Drum module, tendons, real deck on the R 85 ball

**Pass line (spec §10):** ink rosette: PLINE never retraces within 2 mm in 60 s (**see §15 item 4 for the operational definition used**); LINE bow ≤ 0.5 mm; offset circle flats ≤ 0.3 mm; rim reaction measured (V-D1: ≤ 1.3 N inner, ≤ 0.8 N outer, total < coupling with margin ≥ 1.25); coupling: zero nuisance releases in 20 min each mode at 2.0 N; RC5 240 fps on R 85 / R 65 / side mock; checker unit tests. Also V-T1, V-T2, V-T5, V-T6, V-D2, V-D3, RC6 margin on mocks.
**Kit:** R 85 ball, R 65 mock, 70 × 150 side mock (K18), plain paper, washable marker, feeler gauges, calipers, 240 fps phone, ruler, pocket scale, protractor (printed), phone accelerometer app.

**Steps.**
1. **Calibrate first:** `cal drums` (index, trim: each tension 1.5 ± 0.1 N = 153 ± 10 g on the Hall flexures; check one flexure against the pocket scale by hanging 153 g from a cable via a pulley), `cal deadband`, `cal rim`. Record per-cable dead band b₁, b₂, b₃ and repeat `cal deadband` at three bail pose classes if available (V-T2: variation ≤ ±30 %).
2. **Index repeatability (V-T6):** 20 × ARMING; after each, `tensions` and the rosette centre dot. Pass: ≤ 0.1 mm of cable (firmware reports the index error; > 0.3 mm is a FAULT).
3. **Ink rosette (PLINE):** paper on the ball, marker on all six tips, F = 0.25 N, 1.4 Hz, `vary on`, 60 s. Photograph flat with a ruler. Then the same 60 s from the `B` log. Pass (operational, §15 item 4): (a) the rosette covers all headings with no gap > 15°; (b) no single trace is visibly darker (traced ≥ 3 times) than its neighbours; (c) the B log passes the §8.4 no-repeat rule (no (length, period, heading, group) tuple repeated for > 3 strokes; tolerances ±1 mm, ±5 %, ±2°).
4. **LINE bow:** `mode line`, `vary off`, fixed ψ, 20 strokes on fresh paper. Lay a steel rule along the trace end-to-end; the largest gap between rule and trace centre (feeler gauge or the macro photo with a mm scale) = bow. Pass ≤ 0.5 mm. Do it at ψ = 0°, 60°, 120°.
5. **Circle flats:** `mode circle`, R 11.5, e 3.5, 10 revolutions. Photograph with a mm grid under it; on the PC, overlay a true circle (any drawing app) and measure the largest flat (straight segment deviating from the circle). Pass ≤ 0.3 mm after dead-band compensation. If > 0.5 mm, the spec's fallback is circles R ≤ 10 (§8.2).
6. **Tendon stiffness and shrink (V-T1):** block centred, pins down at 0.5 N, push the block sideways with the pocket scale (R-2 sideways): 1.0 N should move it ≤ 0.6 mm (≥ 1.7 N/mm); shrink of the LINE at 0.5 N vs 0.1 N ≤ 0.3 mm.
7. **Rim reaction (V-D1):** tie monofilament to the block yoke post, run over a pulley to the pocket scale (R-1). Pins pressurised at F = 0.25 and 0.50 N on the ball. Drive the block slowly (`amp` sweep or `cal rim`) from centre up the inner rim and on up the outer rim. Read the horizontal pull. Pass: ≤ 133 g (1.3 N) on the inner rim, ≤ 82 g (0.8 N) on the outer rim, and the largest total (incl. PTFE drag) ≤ 2.0 N ÷ 1.25 = 1.6 N (163 g). Compare with the `cal rim` model; differences > 20 % go to FIRMWARE.
8. **Coupling nuisance (20 min each):** coupling at 2.0 N (`B2` tangential test confirms the value later); run 20 min each of PLINE, LINE, CIRCLE, MIX and D-paths on the ball. Pass: zero coupling releases (tension pattern collapse logged as a trip) and zero false reflex trips. If a mode releases: spec allows raising to **2.5 N only** after this test fails, never above.
9. **RC5 lift geometry, 240 fps:** on each mock (R 85 ball, R 65 mock, 70 × 150 side mock), film the block from the side with a ruler in the plane, PLINE at 1.4 Hz and 2.0 Hz.
   - Lift: at |d| ≥ 13.7 every nail's tip is ≥ 5 mm above the surface (frame where the block is at 13.7 mm; measure with the ruler; check with a 5 mm feeler stack slid under the lifted nail with the block parked on the rim, `park`).
   - Landing ≤ 35°: measure the printed inner rim with a printed 34° template (protractor): 33–35°.
   - Lift and landing at ≥ 0.3 v_peak: from the video, the block's speed at the landing/lift frame (mm moved per 4 frames) vs mid-stroke speed. Pass ≥ 0.3.
   - Landing spread ≥ 20 ms (≥ 5 frames between first and last nail touching).
10. **RC6 margin on mocks:** with the pad seated on each mock and pins pressurised, measure with calipers each pin's remaining travel to its retract stop (top of piston to stop). Pass ≥ 15 mm for every pin on every mock.
11. **Checker unit tests:** on the CB1 or PC, in the firmware repo: `python3 -m pytest firmware/sp1v3 -k "checker or ik"`. Pass: all tests pass, including the deliberately bad tokens (reversal inside |d| < 13.7, landing below 0.3 v_peak, |d| > 16.5, v > 200 mm/s, a > 2 m/s², centred circle, group switch inside 13.7, ΣF + 0.45 N > F_float). Paste the summary line onto the sheet.
12. **Stick-slip (V-D3):** phone flat on the deck, accelerometer app, PLINE 1.4 Hz: no buzz or periodic spikes at 140 mm/s; listen with a stethoscope or a straw to the deck.
13. **Cable-life rig (V-T4):** start the 10⁵-stroke run (≈ 20 h at 1.4 Hz) on the spare cable set; inspect at 10⁴ and 10⁵ for broken strands or crimp slip.

**A3 results sheet** — CSV `results/A3.csv`: `date,test,mock,setting,value,unit,limit,pass,notes`

| Item | Value | Limit | ✓ |
|---|---|---|---|
| Dead band b₁ / b₂ / b₃ (mm); variation with pose (%) | / / ; | ≤ ±30 % | ☐ |
| Index repeatability, worst of 20 (mm cable) | | ≤ 0.1 | ☐ |
| Rosette: largest heading gap (°); darker trace? ; no-repeat check | ; y/n ; | ≤ 15; n; pass | ☐ |
| LINE bow at 0 / 60 / 120° (mm) | / / | ≤ 0.5 | ☐ |
| Circle largest flat (mm) | | ≤ 0.3 | ☐ |
| Stiffness at the block (N/mm); shrink 0.1→0.5 N (mm) | ; | ≥ 1.7; ≤ 0.3 | ☐ |
| Rim reaction inner / outer / max total (N) at F 0.25 | / / | ≤ 1.3 / 0.8 / 1.6 | ☐ |
| Rim reaction inner / outer / max total (N) at F 0.50 | / / | ≤ 1.3 / 0.8 / 1.6 | ☐ |
| Coupling releases, 20 min each: PLINE / LINE / CIRCLE / MIX / D | / / / / | 0 each | ☐ |
| False reflex trips in those runs | | 0 | ☐ |
| RC5 lift at \|d\| 13.7, worst nail: R85 / R65 / side (mm) | / / | ≥ 5 | ☐ |
| Inner rim angle (°) | | 33–35 | ☐ |
| v at landing ÷ v_peak (worst) | | ≥ 0.3 | ☐ |
| Landing spread (ms) | | ≥ 20 | ☐ |
| RC6 margin, worst pin: R85 / R65 / side (mm) | / / | ≥ 15 | ☐ |
| Checker + IK unit tests (summary line) | | all pass | ☐ |
| Stick-slip at 140 mm/s | | silent | ☐ |
| Cable-life rig started (date) / result at 10⁵ | | no broken strand | ☐ |

Date ______ Initials ____ **A3 PASS ☐**

### 5.5 A4 — Snag reflex on the wig tether (RC4) and RC1(b) part 2

**Pass line (spec §10, RC4):** trip ≤ 50 ms at centre and rim; 20 min PLINE, D-paths, CIRCLE without tether: zero false trips. Plus RC1(b): 20-min wig PLINE with zero nuisance releases.
**What "trip ≤ 50 ms" means here (§15 item 8):** time from the tether force crossing the firmware threshold (0.8 N residual drag) to rail-sense low. Also recorded: time from 0.15 N to rail-sense low.
**Why a monofilament tether:** a single real hair breaks near 1 N and is plucked from a real scalp at ≈ 0.7 N. To measure the reflex itself we need a tether that does not break first: **0.25 mm monofilament** (≈ 10 lb). Real hair is used in HB-6/HB-7 (RC1 c/d), where the breakaway, not the reflex, is under test.
**Kit:** fast logger with the **500 g** cell (R-6), pad deck on the trimmed wig head (or the R 85 ball with a wig cap pulled over it), 240 fps phone with the ACT-12 LED.

**Setup (tether rig, also used in HB-6):**
1. Drill a Ø 2 mm hole through the ball/foam head at the station under the pad axis (centre, |d| = 0) and a second hole at **|d| = 10 mm** along the stroke heading (the lift zone; the landing band is |d| ≈ 8.5–12.2). Mark both on the pad with tape.
2. Mount the load cell inside/under the head directly below the hole, arrow pointing up, so the tether runs straight down the scalp normal.
3. Tether: 0.25 mm monofilament tied to the load-cell hook, up through the hole, a small slip loop round the chosen nail (centre nail C for the centre test; the nail whose path crosses the |d| = 10 hole for the rim test). Length from hole to loop ≈ 15 mm, slack 2 mm.

**Steps.**
1. Calibrate the cell (R-6 step 4).
2. Start a capture; hold the lever; `play` PLINE F = 0.25 N, 1.4 Hz, ψ fixed so the stroke crosses the hole (`mode line` and `psi` for the rim test).
3. The snag happens within a stroke or two. The rail should drop (LED dark), pins vent, drums stop.
4. Run `analyse_tether.py`. Record peak force, time > 0.8 N → rail dead, time > 0.15 N → rail dead.
5. 5 trials at the centre, 5 at the rim, at F = 0.25 N; then 5 + 5 at F = 0.50 N.
6. After each trip: release the lever (resets the latch), count nails, re-seat, re-arm.
7. **False-trip runs:** no tether, wig head, 20 min each of PLINE, D-paths (`dpath 8` bursts in MIX or PLINE with D-paths on), CIRCLE, F = 0.30 N. Pass: zero trips.
8. **RC1(b) part 2:** count the nails after the 20-min PLINE run: 6, zero nuisance releases. Then redo A2.2 friction ("aged") and A2.7 ("after 20 min").

**A4 results sheet** — CSV `results/A4.csv`: `date,location,F_N,trial,peak_N,t_08_to_dead_ms,t_015_to_dead_ms,nails_ok,notes`

| Location / F | Trials | Worst t(0.8 N → rail dead) ms (≤ 50) | Worst t(0.15 N → dead) ms (record) | Peak N (record) | ✓ |
|---|---|---|---|---|---|
| Centre, 0.25 N | /5 | | | | ☐ |
| Rim \|d\| 10, 0.25 N | /5 | | | | ☐ |
| Centre, 0.50 N | /5 | | | | ☐ |
| Rim \|d\| 10, 0.50 N | /5 | | | | ☐ |
| False trips, 20 min PLINE / D / CIRCLE | | 0 / 0 / 0 | | | ☐ |
| Nuisance releases after 20-min PLINE (RC1 b) | | 0 | | | ☐ |

Date ______ Initials ____ **A4 PASS ☐**

### 5.6 A5 — Everything into the Apache case

**Pass line (spec §10):** ≤ 30 dBA at 1 m; ≤ 2.8 kg; runs on its back, side and face. Also V-B1 (≤ +20 K after 1 h).
**Steps.**
1. **Mass:** close the case with everything inside (not the umbilical beyond the box-end block, not the adapter). Kitchen scale (if > 3 kg range, luggage scale by the handle). Pass ≤ 2.80 kg.
2. **Noise (R-4):** box on the desk, MIX at 1.4 Hz, pad on the R 85 ball (pins down; nail hiss is wanted, so put the ball 2 m away on a towel and run the umbilical to it) — or use a dry run if the firmware provides one (§15 item 12). Measure room-only and room + box at **1 m** and at **0.25 m**. Pass: corrected value at 1 m ≤ 30 dBA **or** (if the room is above 30 dBA) 0.25 m corrected value − 12 dB ≤ 30 dBA. Record both.
3. **Orientation:** 5 min MIX with the case on its back, on each side, and on its face. Pass: no fault, no rail-PID error > 0.5 kPa, no rattle.
4. **Thermal (V-B1):** 1 h MIX on a sofa cushion (worst case), IR thermometer at 0/30/60 min on the case top, the stepper bodies, the buck and the M8P heatsink (lid open briefly at 60 min). Pass: case rise ≤ 20 K; no part > 48 °C to the touch (stepper bodies may run hotter; record).

**A5 results sheet** — CSV `results/A5.csv`

| Item | Value | Limit | ✓ |
|---|---|---|---|
| Box mass (kg) | | ≤ 2.80 | ☐ |
| Room / room + box at 1 m (dBA); corrected | / ; | ≤ 30 | ☐ |
| Room / room + box at 0.25 m (dBA); corrected − 12 | / ; | ≤ 30 | ☐ |
| Back / side / side / face, 5 min each | ☐ ☐ ☐ ☐ | no fault | ☐ |
| Case rise after 1 h on a cushion (K) | | ≤ 20 | ☐ |
| Hottest touchable part (°C, which) | | ≤ 48 | ☐ |

Date ______ Initials ____ **A5 PASS ☐**

### 5.7 A-S — Stage A sensation point (first powered pad on Michael's head)

**Pass line (spec §10):** bench pad hand-held by a helper on Michael's crown and occiput (float bypassed, skids on the scalp), PLINE vs LINE vs CIRCLE vs MIX, blind: **≥ 6/10 "as satisfying as a good scratch"** and **"scratch not brush" in ≥ 6/8 headings.**
**This is the first time powered nails touch a head.** Red line 12 applies: checklist, wig test, glasses, ≤ 5 min. The spec's wig gate (B5) and checklist (B6) come later, so this file adds an entry gate (§15 item 6):

**A-S entry (all ticked):**
- ☐ A0–A5 passed.
- ☐ **HB-mini** passed with the bench pad (§6.4): HB-3 reversal/loop, HB-4 wrap, HB-5 gap probe, HB-6 RC1(c) tether at F = 0.25 N — all zero events.
- ☐ **PHC-A (bench-pad variant)** and PHC-B filled (§11), with the items marked "B and later" set to N/A.
- ☐ **Hold force fixed by weight, not by the helper's hand:** the bench pad rests on the scalp by its own weight plus a slug so the total is **≤ 4 N (≤ 400 g)** measured on the kitchen scale with the pad sitting on a foam dome. The helper only steadies it with fingertips on the deck edge and keeps it from sliding; they **never push down**. Practise on the kitchen scale until the reading stays within ±30 g of the pad's own weight while steadying. (Red line 3 needs a constant; a pressing hand is not one. §15 item 6.)
- ☐ F = 0.25 N (INTENSITY fixed; Stage B range is 0.20–0.45 N); f = 1.4 Hz.
- ☐ Glasses on; e-stop puck under Michael's free thumb; lever in Michael's other hand (not the helper's).

**Day 1 — crown (≤ 5 min contact).** Day 2 — occiput (same, Michael seated and leaning forward onto forearms on the desk). ≥ 20 h apart.
1. Helper sets up the blind order with §14 (four modes as slots A–D; 8 LINE headings in a random order).
2. **Modes:** four bouts of 45 s (PLINE, LINE, CIRCLE, MIX in the random order), 30 s nails-up between. After each, Michael fills the short form (§12, Q1–Q3, Q5–Q6).
3. **Headings:** LINE at 0, 22.5, 45, … 157.5° in random order, 15 s each, nails-up 10 s between. After each Michael says one word: **"scratch"** or **"brush"** (or "massage", "buzz"). Helper writes it.
4. Total contact = 4 × 45 + 8 × 15 = 300 s = 5 min. Stop there.
5. Helper reveals the order only after all forms are filled.

**A-S results sheet** — CSV uses §12 header, stage = A-S.

| Day / region | PLINE Q1 | LINE Q1 | CIRCLE Q1 | MIX Q1 | Best Q1 (≥ 6) | "scratch" headings /8 (≥ 6) | Pulls | Discomfort max | ✓ |
|---|---|---|---|---|---|---|---|---|---|
| 1 crown | | | | | | | | | ☐ |
| 2 occiput | | | | | | | | | ☐ |

**GO A:** A0–A5 all passed **and** best Q1 ≥ 6 **and** ≥ 6/8 "scratch" (at both regions; if only one region passes, record it and decide with the Director). **NO-GO:** < 6/10 → tip, force and variation A/B on the bench pad before any halo work (spec §10). ☐ GO ☐ NO-GO Date ______

---

## 6. Hair bench (HB-0 … HB-11), including the RC1 rim-snag tether rig

This is the hair gate (red line 12; hair-interaction §7; spec B5 and C8; ruling RC1 c/d, RC2). The **full** bench runs at **B5** on the finished pad and again at **C8** on the whole system. A **mini** subset (HB-mini, §6.4) runs on the bench pad before A-S.
**Heads (K16, K17):** **W-S** = real-hair wig trimmed to 3–5 cm; **W-L** = real-hair wig, long; **KAN** = Kanekalon pinned in a 10 × 10 cm patch on a foam head (higher friction and static: the conservative wrap/loop screen). If Michael's hair (S0 numbers) is outside 3–8 cm, trim W-S to match his length instead.
**Instruments:** black cloth under the head, lint roller, hygrometer, 240 fps phone + macro lens + side lamp, fast logger (100 g cell), pocket scale, wide-tooth comb, tweezers.
**Mounting:** the helmet (B5, C8) or the bench pad (HB-mini) on the wig head clamped to the table. Wig head clamped so the station under test faces up.
**Count every hair:** after each test, lint-roll the cloth and the pad underside, count hairs on the roller under the lamp, split into **with bulb** (white root bulb, pulled) and **broken** (no bulb).

### 6.1 Tests

**HB-0 Baseline (once per wig, then weekly).** Comb W-S 20 strokes with the wide-tooth comb over the black cloth; count shed hairs = **B₂₀** (per 20 comb strokes). Measure comb-through force: luggage or pocket scale on the comb, pull slowly through the test patch, read the peak (3 reads, average) = **K₀**. Record RH %.

**HB-1 Static reach.** Pad on its float at R2 palm, pins at 0.20, 0.30 and 0.45 N, block centred (`park` is rim; use `cal` centre or a firmware hold at d = 0 [ask FIRMWARE]). Side photo through the hair with the macro lens. Pass: the cone tips visibly reach the wig scalp at ≤ 0.30 N on W-S. (Record only for W-L; Stage D will tell whether long hair is in scope.)

**HB-2 Single-stroke drag (record).** `mode line`, `vary off`, F = 0.30 N, 1.0 Hz, ψ with-grain, cross-grain, against-grain, 10 strokes each; read the peak residual drag from the `B` log. Flag (and tell the Director) if against-grain drag > 3 × with-grain or rises along the stroke.

**HB-3 Reversal / loop (RC2 hair §7.3.3).** On W-S and on KAN: 50 LINE strokes (ψ with-grain), 50 LINE cross-grain, 50 D-path strokes, F = 0.30 N, 1.4 Hz. Film 20 reversals at 240 fps. Pass: **zero loops, zero knots**; on video every strand is released before the block turns (no strand tensioned across the turnaround frame); every nail visibly up at both ends.

**HB-4 Wrap.** W-L draped over the running helmet in every orientation the head could take: hair falling over the pad cover, over the carriage, over the bail track, over the hub bosses and the umbilical exit. 5 min MIX, F = 0.30 N. Also 5 min with KAN fibres laid across the pad skirt and yoke area. Pass: **zero wraps**, zero strands in any gap (inspect every node, roller, hinge, the yoke cage, tendon stops, the umbilical bore).

**HB-5 Gap probe (running).** At 1.0 Hz, offer single hairs and 5-hair tufts with tweezers to: every wiper, the nail guides' exits, the block–deck gap, the yoke ring and magnets, the tendon stops and springs, the skid stems, the kinematic mount, the float rod, the carriage rollers, the β/α detents. Also offer 100 µm monofilament. Pass: **zero captures**.

**HB-6 RC1(c) — rim-snag tether (the key RC1 test).**
- **Rig:** the A4 tether rig (§5.5) with the **100 g** cell, but the tether is **one real hair** from W-S (≈ 60–80 mm long), tied to the load-cell hook, up through the |d| = 10 mm hole, with a slip loop round the nail whose path crosses the hole. Free length hole-to-loop ≈ 15 mm.
- **Run:** PLINE on the R 85 ball (or W-S at a crown-like station) at **F = 0.25 N** and **F = 0.50 N**, 1.4 Hz, ψ set so the nail's lift crosses the hole. Capture with the logger. 5 trials per force (new hair each trial).
- **Pass (every trial):** peak **≤ 0.30 N**; time above 0.15 N **≤ 20 ms**; the nail released (dropped off its magnet) or the loop slid off; **no hair broken by the test** is expected but record it.
- After each trial: count nails, re-seat the released nail, check the wiper closed (look up the bore with the lamp: no open hole).

**HB-7 RC1(d) — snag during a stop.** Same rig, hair looped, block parked at |d| ≈ 10 with pins down at 0.50 N. Then (a) press the **e-stop**; (b) trip the **latch** (`inject snag`) — v3's reflex is a full fail-to-free, not the ruling's 10 mm retract (§15 item 7); (c) **pull the lanyard**. 3 trials each. Pass: peak ≤ 0.30 N, ≤ 20 ms above 0.15 N, nail released, pad retracted.

**HB-8 Endurance and shed (B5 / C8 main run).** On W-S over the black cloth, one station, F = 0.30 N, 1.4 Hz, `vary on`: **20 min PLINE + 5 min CIRCLE + 5 min LINE + 5 min D-paths** (spec B5). Station dwell timer **off** for this test (it is a worst case). Photos before/after. Count shed (bulb/broken), stroke count from the `B` log. Then comb-through force K₁.
- Shed per 100 machine strokes **≤ 2 ×** combing shed per 100 comb strokes. Combing shed per 100 strokes = 5 × B₂₀, so **allowed shed for the run = 2 × 5 × B₂₀ × (machine strokes) ÷ 100** (worked example under the sheet, §6.3).
- Zero wraps, captures, knots; nail count 6; zero nuisance releases.
- Repeat the 20 min PLINE part on W-L and on KAN (record shed; wraps/knots must still be zero).

**HB-9 Matting run → sets T_dwell (spec B5, §7.4 H-5.5).** The spec gives no matting criterion; this file defines it (§15 item 11).
1. Fresh W-S patch, comb it, measure K₀ at that patch.
2. Run PLINE + variation (MIX) at the session default (F 0.30 N, 1.4 Hz) on that patch for cumulative contact times **30, 60, 90, 120, 180 s** (the `E` log shows contact-seconds). After each step: photo, comb-through force K, look for clumps.
3. **Matting onset** = the first step where any of: K > 1.5 × K₀; a visible clump/rope of hairs that does not fall apart when you blow on it; shed in that step > 2 × the combing rate.
4. **T_dwell = the last clean step** (e.g. onset at 120 s → T_dwell = 90 s). Cap 180 s. Set it with `dwell <s>` and write it on the PHC. If T_dwell < 60 s, log risk R4 for the Director (spec §12.1).
5. Repeat on a second patch with the with-grain D-path comb-out every 20 strokes active (spec §7.4): record whether T_dwell rises.

**HB-10 Static (V19).** Repeat 5 min of HB-8 PLINE at **< 40 % RH** (run the AC/dehumidifier, or a dry winter day; record RH) and at > 50 % RH. Record fly-away and hair following the nails up > 10 mm. Pass for V19: no hair follows the nails > 10 mm at < 40 % RH; if it does, add an antistatic wipe to the PHC-B cleaning step and tell PAD.

**HB-11 Slip-loop shed (RC2, repeat on the finished pad).** As A2.3 step 3 but on the finished pad: 10/10 sheds, ≤ 0.10 N before any breakaway.

### 6.2 Hair checklist H-6.8 (self-score at B5, re-score at C8)

Score 2 = fully met, 1 = partly, 0 = not met. **Any 0 on items 1–7, or a total < 28, blocks human testing.** The ruling expects ≈ 30/36 with items 4 and 7 at 1 by design.

| # | Item (hair-interaction §6.8) | Gating | Evidence (test / doc) | Score |
|---|---|---|---|---|
| 1 | No exposed rotating surface in the zone | Y | HB-4, HB-5; nothing rotates on the pad | |
| 2 | Every joint in the zone has an exclusion method | Y | HB-5; PAD drawings | |
| 3 | No changing gap or 40 µm–3 mm gap within 25 mm of scalp | Y | C8 CAD sweep report; HB-5 | |
| 4 | Lift before every reversal | Y | A3 RC5; HB-3 video | (1 expected) |
| 5 | Rigid group | Y | one block | |
| 6 | Drafted nail, no re-entrant feature | Y | A2.3 shadowgraph | |
| 7 | Yield ≤ 0.15 N tangential on a snag | Y | HB-6 (pull-off ≤ 0.25 N) | (1 expected) |
| 8 | Protrusion ≥ 25 mm | | block underside ≥ 32 mm | |
| 9 | Tip spacing ≥ 8 mm | | 18 mm layout | |
| 10 | Low-friction polished tips | | POM; Ra check | |
| 11 | Breakaway 3–5 N with no tether | | RC1 0.25 N (stricter) | |
| 12 | Hair-shedding guard, drafted pass-throughs | | wiper skirt | |
| 13 | With-grain bias + grain map in logic | | LINE/D-path grain table | |
| 14 | Dwell / repetition limits | | HB-9 T_dwell set | |
| 15 | Snag reflex lifts, never reverses | | A4, HB-7 | |
| 16 | Antistatic | | HB-10 | |
| 17 | Tool-free removal for cleaning | | pad lifts off, nails drop out | |
| 18 | States which hair variants it tolerates | | HB-8 on W-S/W-L/KAN | |
| | **Total /36 (≥ 28, no gating 0)** | | | |

### 6.3 Hair bench results sheet

CSV `results/HB.csv`: `date,stage,test,head,setting,trial,value,unit,limit,pass,RH,notes`

| Test | Head | Key values | Limit | ✓ |
|---|---|---|---|---|
| HB-0 baseline | W-S | B₂₀ = ___ hairs; K₀ = ___ g; RH ___ % | — | — |
| HB-1 reach | W-S / W-L | reaches at 0.20 ☐ 0.30 ☐ 0.45 ☐ N | ≤ 0.30 N on W-S | ☐ |
| HB-2 drag | W-S | with ___ cross ___ against ___ N | against ≤ 3× with (flag) | — |
| HB-3 reversal | W-S / KAN | loops ___ knots ___ ; video ok ☐ | 0 / 0 | ☐ |
| HB-4 wrap | W-L / KAN | wraps ___ strands in gaps ___ | 0 / 0 | ☐ |
| HB-5 gap probe | — | captures ___ (list locations) | 0 | ☐ |
| HB-6 RC1(c) F 0.25 | real hair | peaks ___ ___ ___ ___ ___ N; t>0.15 N ___ ___ ___ ___ ___ ms; released 5/5 ☐ | ≤ 0.30 N; ≤ 20 ms | ☐ |
| HB-6 RC1(c) F 0.50 | real hair | peaks ___ ___ ___ ___ ___ N; t>0.15 N ___ ___ ___ ___ ___ ms; released 5/5 ☐ | ≤ 0.30 N; ≤ 20 ms | ☐ |
| HB-7 RC1(d) e-stop / latch / lanyard | real hair | worst peak ___ / ___ / ___ N; worst t ___ / ___ / ___ ms | ≤ 0.30; ≤ 20 | ☐ |
| HB-8 endurance | W-S | strokes ___; shed bulb ___ broken ___; allowed ___; K₁/K₀ ___; wraps/caps/knots ___; nails 6 ☐ | shed ≤ allowed; 0 | ☐ |
| HB-8 on W-L / KAN (20 min PLINE) | | shed ___ / ___; wraps/knots ___ / ___ | 0 wraps/knots | ☐ |
| HB-9 matting | W-S | onset at ___ s (sign: ___); **T_dwell = ___ s** (with comb-out: ___ s) | set; flag if < 60 | ☐ |
| HB-10 static | W-S | RH ___ %: follow ___ mm; RH ___ %: follow ___ mm | ≤ 10 mm | ☐ |
| HB-11 slip loop | real hair | sheds ___/10; max ___ N | 10/10; ≤ 0.10 | ☐ |
| H-6.8 score | — | total ___ /36; gating zeros ___ | ≥ 28; 0 | ☐ |

**Allowed shed worked example:** B₂₀ = 4 hairs per 20 comb strokes = 20 per 100 strokes. HB-8 ran 2,940 strokes. Allowed = 2 × 20 × 2,940 / 100 = 1,176 → in practice the run passes unless shedding is wildly high; **bulb hairs > 5 in any 5-min block are a stop-and-look item** regardless (a bulb means a pull, not a broken hair).

### 6.4 HB-mini (before A-S, bench pad)

Run HB-3 (W-S only, 50 LINE + 50 D-path), HB-4 (5 min, W-L), HB-5 and HB-6 at F = 0.25 N (3 trials) with the bench pad held on the wig by its weight (same ≤ 4 N setup as A-S). Pass: zero loops, knots, wraps, captures; HB-6 peaks ≤ 0.30 N, ≤ 20 ms above 0.15 N. Record on the §6.3 sheet with stage = A.

---

## 7. Stage B — pad on a fixed-pose halo, first sessions (gates B1–B6, then B-S)

**Entry:** GO A; Cart 3 built: complete pad, Airpel float + QEV + float relief, carriage, halo (band, dial cradle, hub bosses with hinges, carbon bail), umbilical with ear-axis exit, lanyard and clip; JLC3DP production parts fitted. Firmware has the station dwell timer and MOVED.
**Bench setup for B1–B5:** helmet on the trimmed real-hair wig head (W-S) clamped to the table; box 1 m away; e-stop and lever in your hands for every powered step.

### 7.1 B1 — Mass (V17)

**Pass line:** pad ≤ 90 g; moving group ≤ 125 g; helmet ≤ 320 g.
**Definitions used (§15 item 9):** *pad* = everything that lifts off the kinematic mount (deck, dish, skids, RCC, cover, block, six pins and nails, yoke, coupling, springs, stops, PP link, lift spring, on-pad jumpers to the barbs). *Moving group* = what the hand moves between stations and what the float carries: **carriage + float + pad** (spec ledger: 10 + 24 + 81.5 = 115.5 g). *Helmet* = everything head-borne, including the head-side harness on the bail and the umbilical's head share measured as in C6 step 1.
**Steps.** Kitchen scale (1 g). Pad alone. Carriage + float + pad (unclip the carriage from the track with the pad on it). Whole helmet with the harness cut free at the 3 N clip (support the loop beyond the clip off the scale) — weigh 3 times, average.

| Item | Reading 1 | 2 | 3 | Mean (g) | Limit | ✓ |
|---|---|---|---|---|---|---|
| Pad | | | | | ≤ 90 | ☐ |
| Moving group (carriage + float + pad) | | | | | ≤ 125 | ☐ |
| Helmet (head-borne) | | | | | ≤ 320 | ☐ |

**B1 PASS ☐** Date ______ Initials ____

### 7.2 B2 — Force audit

**Pass line:** all six nails at R1a + palm at R2 on a load cell under a foam dome: total ≤ 12 N (expect ≤ 4.6); one nail ≤ 0.92 N; tangential pull at the coupling 2.0 ± 0.3 N. **Plus RC6 bottoming test** (spec §7.3: 15 mm block under each nail, float at R2b, ≤ 1.04 N) and red line 7 (power-pull: nothing self-locking).
**Kit:** kitchen scale, pocket scale, a **foam dome** (half of a Ø 170 craft-foam ball, flat side down, ≈ R 85), luggage scale, the 500 g logger cell or pocket scale with a pulley, a 15 mm spacer block (printed or wood) with a 5 mm flat top.

**Steps.**
1. **Total normal (worst case):** helmet on a stand so the pad sits over the foam dome on the kitchen scale (tare with the dome on). Palm at R2: cap R2b, run P3 at 100 % (palm rises to R2 ≈ 20.7). Pin rail at R1a: P1 at 100 %, `groups ab`, block centred over the dome. Read total. Then cap R2 and uncap R2b (palm at R2b) and read again. Pass: ≤ 1,224 g (12 N) in both; expected ≤ 469 g (4.6 N). If > 469 g, find out why before going on.
2. **One nail:** pad on the stand, one nail pressing the pocket scale through a hole in a card (other nails held off the scale by the card). Rail at R1a: record it (expect 0.80 ± 0.06 N, i.e. ≈ 76–88 g, minus the small return-spring force); with R1a capped (rail at R1b): pass **≤ 93.8 g (0.92 N)**. Every nail.
3. **RC6 bottoming:** put the 15 mm spacer under one nail on the kitchen scale, the other nails off the edge; float at R2b (R2 capped), rail at R1b. Read. Pass **≤ 106 g (1.04 N)** for every nail. (This is the "finger or 10° tilt" case.)
4. **Coupling (tangential cap):** pins vented, block centred, pull the **block** (not the yoke) sideways with monofilament through the pocket scale reverse-reading (R-1, with a 300 g bag on the kitchen scale instead of 50 g) or with the 500 g logger cell, in 6 directions (every 60°). Read the force at which the yoke parts from the block. Pass: **173–235 g (2.0 ± 0.3 N)** in every direction. Re-seat by recentring (ARMING).
5. **Red line 7 power-pull:** rail dead. Push the block by hand across its range and swing the bail by hand: everything back-drives, nothing locks. Pass/fail by feel, noted.

| Item | Value | Limit | ✓ |
|---|---|---|---|
| Total at R1a + R2 (g) | | ≤ 1,224 (expect ≤ 469) | ☐ |
| Total at R1a + R2b (g) | | ≤ 1,224 | ☐ |
| One nail at R1b, N1…N6 (g) | / / / / / | ≤ 93.8 | ☐ |
| RC6 bottomed, N1…N6 (g) | / / / / / | ≤ 106 | ☐ |
| Coupling release 0°…300° (g) | / / / / / | 173–235 | ☐ |
| Back-drivable with rail dead | | yes | ☐ |

Reliefs uncapped after ☐ **B2 PASS ☐** Date ______ Initials ____

### 7.3 B3 — Proof loads and tape test (red lines 9 and 11, V-N1)

**Pass line:** each nail: cone-to-shaft 3.1 N tension; 3.1 N compression; 3.0 N lateral in guides; kinematic mount 6 ± 2 N; tape test.
**Steps.**
1. **Tension (cone-to-shaft):** nail out of the pad. Hold the shaft in a pin vice (or pliers wrapped in tape) above the bench, tie a monofilament loop under the cone shoulder, hang a 316 g mass (a filled water bottle weighed on the kitchen scale) slowly for 10 s. Pass: no movement of the cone on the shaft (mark it with a pen line across the joint; the line must stay aligned under the loupe).
2. **Compression on the magnet face:** nail installed, pin vented. Press the nail tip straight down onto the kitchen scale (pad held by hand above it) to 316 g for 5 s. Pass: nothing cracks, the nail does not push the magnet out of the piston face (check under the loupe), and the nail slides back freely.
3. **Lateral in the guides:** nail installed, extended to contact height, pull the tip sideways with a loop through the pulley onto a 306 g reverse-reading (R-2) or with the luggage scale: to 306 g (3.0 N). Pass: no bend (roll the shaft on glass after: it must roll freely), no guide crack.
4. **Kinematic mount:** luggage scale hooked to the pad's lift point, pull straight off the float. Peak at release, 3 pulls. Pass: 408–816 g (6 ± 2 N).
5. **Tape test (red line 11):** wrap a 10 mm dowel with three layers of 50 µm tape. Press each nail tip at 1.0 N (102 g on the kitchen scale under the dowel) then at 2.5 N (255 g), slide 50 mm along the dowel at ≈ 50 mm/s, three passes. Do the same with the shaft's top end (dropped-nail case) and by hand at 5 N on the pad skirt, skids, cover, yoke edge, carriage, band, hub bosses. Pass: no cut through the first layer under the loupe.
6. Do steps 1–3 on every nail and every spare. A nail that fails anything is scrapped, not repaired.

| Nail | Tension 316 g ✓ | Compression 316 g ✓ | Lateral 306 g ✓ | Tape 1.0 / 2.5 N ✓ | Shaft top tape ✓ |
|---|---|---|---|---|---|
| N1 | ☐ | ☐ | ☐ | ☐ ☐ | ☐ |
| N2 | ☐ | ☐ | ☐ | ☐ ☐ | ☐ |
| N3 | ☐ | ☐ | ☐ | ☐ ☐ | ☐ |
| N4 | ☐ | ☐ | ☐ | ☐ ☐ | ☐ |
| N5 | ☐ | ☐ | ☐ | ☐ ☐ | ☐ |
| N6 | ☐ | ☐ | ☐ | ☐ ☐ | ☐ |
| Spares | ☐ | ☐ | ☐ | ☐ ☐ | ☐ |

Kinematic mount pulls: ___ / ___ / ___ g (408–816) ☐ Structure edges at 5 N, no cut ☐ **B3 PASS ☐** Date ______

### 7.4 B4 — Fail-to-free (red line 8, V-P2)

**Pass line:** power pull ×10, lanyard pull ×10, latch trip ×10, `hang` ×5: pad ≥ 25 mm retracted in ≤ 150 ms (240 fps), no nail in contact.
**Setup:** helmet on W-S at the vertex station; MIX at F = 0.30 N; ruler taped vertically beside the pad in the camera plane; ACT-12 LED in frame (R-3); camera side-on.
**Steps.** For each event: start filming, `play`, wait ≥ 10 s, trigger the event at a random moment, film 2 s more.
- **Power pull:** pull the adapter's DC plug at the box. (Logic dies too: the de-energised state must still be free.)
- **Lanyard pull:** pull the magnetic pogo lanyard apart by hand.
- **Latch trip:** `inject snag` (host GPIO) on 5, press a cable flexure (comparator) on 5.
- **Hang:** `inject hang` (wig head only; spec §8.6): the watchdog must open the rail.
Count frames from the event (LED dark, or for `hang` the moment the command is sent — use the console timestamp and film the screen too) to the pad being ≥ 25 mm above the wig scalp. Check every frame after: no nail touches the hair. Also measure the Airpel/QEV retract with the palm at R2b once (V-P2).

| Event | n | Worst frames to ≥ 25 mm | Worst ms (≤ 150) | Any nail in contact after? | ✓ |
|---|---|---|---|---|---|
| Power pull | /10 | | | | ☐ |
| Lanyard pull | /10 | | | | ☐ |
| Latch trip (5 host + 5 comparator) | /10 | | | | ☐ |
| `hang` (watchdog) | /5 | | (spec ≤ 1 s to rail open, then ≤ 150 ms) | | ☐ |

**B4 PASS ☐** Date ______ Initials ____

### 7.5 B5 — Hair gate

**Pass line (spec §10):** real-hair wig 3–5 cm and long + Kanekalon: 20 min PLINE + 5 min CIRCLE + 5 min LINE + 5 min D-paths: zero wraps, captures, knots; shed ≤ 2× combing; RC1 (c)(d) rim-snag tether ≤ 0.30 N peak, ≤ 20 ms above 0.15 N; matting run sets T_dwell.
**Procedure:** run the **full hair bench** §6 (HB-0 … HB-11) on the finished helmet, fill §6.3 and the H-6.8 score §6.2. **B5 PASS** = every §6.3 row ticked, H-6.8 ≥ 28 with no gating 0, and T_dwell entered in the firmware (`dwell <s>`) and on PHC-A. **B5 PASS ☐** Date ______

### 7.6 B6 — Session entry

**Pass line:** safety checklist signed, glasses, e-stop under the free thumb, ≤ 5 min (red line 12).
**Procedure:** PHC-A complete for this build state (§11.1), PHC-B complete today (§11.2), the first B session is ≤ 5 min. **B6 PASS ☐** Date ______

### 7.7 B-S — First sessions on Michael's head (the hypothesis at fixed poses)

**Spec:** 2 → 5 → 10 → 20 min sessions at 3–6 stations (vertex, upper occiput, both parietals), the halo moved by hand between bouts. **GO B:** ≥ 7/10 "as satisfying as being scratched well", "machine on my head" ≤ 3/10, zero pulls, nail count intact every session.
**Posture (spec §7.7):** a chair whose headrest is ≥ 120 mm behind the bun, or no headrest; no reclining at bun stations (α > 75°).
**Every session:** PHC-B first; a black towel over the shoulders; voice memo running; the helper (if any) sits where Michael can't see the laptop; the session timer is the firmware's (it stops at 20 min) plus a phone timer set to the session's limit.
**Moving the halo:** release the lever (pins vent, pad retracts) → move α/β by hand to the next detent click → press MOVED → hold the lever (APPROACH, 3 ramp strokes) → bout.

| Session | Contact limit | Stations (bouts) | Settings | Forms | Extra |
|---|---|---|---|---|---|
| **B-S1** | **2 min** | vertex: 2 × 60 s | PLINE 1.4 Hz, F 0.20 N (net-force floor, spec §4.1), `vary on` | §12 short form after each bout; full form at end | first thing: lever held with the pad on the head, then released: feel the pad lift (fail-to-free felt on the head). Scalp photo 0/10/60 min. |
| **B-S2** | **5 min** | vertex 2.5 min, upper occiput 2.5 min | PLINE then MIX; F 0.20–0.30 N (Michael may turn INTENSITY) | short form per bout; full at end; voice ratings every 60 s | ≥ 20 h after B-S1 and scalp clear |
| **B-S3** | **10 min** | vertex, upper occiput, left parietal, right parietal: 2.5 min each | MIX; F knob 0.20–0.45 N; SPEED knob free | as above | — |
| **B-S4** | **20 min** | 4–6 stations; the dwell timer (T_dwell from HB-9) chimes, Michael moves the halo and presses MOVED | MIX, knobs free | short form per station; full at 10 and 20 min; voice ratings every 2 min | scalp photo next morning |

**GO B decision (operational definition, §15 item 10):** all four sessions completed in order, **and** at B-S4: end-of-session Q1 (satisfying) **≥ 7** and Q3 (machine on my head) **≤ 3**; **and** Q1 ≥ 7 at the end of at least one other B session or at B-S4's 10-min form; **and** zero felt pulls in every B session; **and** nail count = 6 after every session; **and** no stop rule (§3.2) triggered. **NO-GO:** < 5/10 → fix the pad (cone, force, variation) before Stage C; 5–6/10 → Stage D experiment matrix (§10) first.

**B-S results sheet** — CSV §13 session header + §12 rows.

| Session | Date | Contact min | Stations | End Q1 (≥ 7 at B-S4) | End Q3 machine (≤ 3) | Pulls felt (0) | Discomfort max | Nails after (6) | Wants again Y/N | Stop rules hit | ✓ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-S1 | | / 2 | | | | | | | | | ☐ |
| B-S2 | | / 5 | | | | | | | | | ☐ |
| B-S3 | | / 10 | | | | | | | | | ☐ |
| B-S4 | | / 20 | | 10-min ___ / end ___ | | | | | | | ☐ |

☐ GO B ☐ NO-GO (< 5) ☐ to D-matrix first (5–6) Date ______

---

## 8. Stage C — finish and wearability (gates C1–C8, then C-S)

**Entry:** GO B; Cart 4 fitted (finishing parts, armrest switch parts). Stage C gates are mostly on Michael's head **unpowered** or with the pad retracted; the powered ones (C5, C8, C-S) need PHC-B first.

### 8.1 C1 — Fit (V15)

**Pass line:** cradle seats under the shelf; bun free ≥ 60 mm above the cradle edge; 20 min no mark beyond 10 min; mechanical α/β stops set from Michael's hairline and ears.
**Steps.**
1. Set the dial once; mark the band position on the forehead pad with a pen line at the brow midline.
2. Seat the helmet; helper runs a finger along the cradle: it hooks under the occipital shelf on both sides (no gap you can push a finger into above it). Photo from behind with a ruler.
3. Measure with a ruler from the cradle's top edge up to the most prominent point of the occipital bun: ≥ 60 mm (so bun stations are free).
4. Wear it 20 min (TV), unpowered. Doff; photograph forehead, temples, occiput at 0 and 10 min. Pass: any red mark gone by 10 min.
5. **Stops:** follow the HALO WP stop-setting procedure (α front stop = α_hairline + 20° from the S0 tape fit; β stops ±40°). Record the angles read on the printed zero gauge. (C4 verifies them.)
6. **V15:** with the helmet on the foam head, luggage scale on the doff lip, pull up-and-back: cradle override ≈ 10 N (record); pitch hold: hang 100 g at 100 mm in front of the band (0.1 N·m steps) until the helmet tips; record the torque (≥ 1 N·m expected).

| Item | Value | Limit | ✓ |
|---|---|---|---|
| Cradle under shelf both sides | | yes | ☐ |
| Cradle edge to bun (mm) | | ≥ 60 | ☐ |
| Marks at 10 min after 20 min wear | | none | ☐ |
| α front stop / rear stop (°); β stops (°) | / ; / | set per HALO | ☐ |
| Cradle override (N); pitch hold (N·m) | ; | ≈ 10; ≥ 1 | ☐ |

**C1 PASS ☐** Date ______

### 8.2 C2 — Mass

**Pass line:** helmet ≤ 320 g measured. **Procedure:** as B1 "helmet" row, on the finished helmet. ___ / ___ / ___ g, mean ___ g ≤ 320 ☐ **C2 PASS ☐**

### 8.3 C3 — Lean (coin bag)

**Pass line:** coin bag at the pad pose, moved every 2 min for 20 min of TV: lean ≤ 2/10, slip ≤ 3°.
**Steps.**
1. Use the real pad on the float (unpowered, pad retracted). If the pad is off for service, use a coin bag of the **moving-group mass (≈ 116 g, B1)** on the carriage instead.
2. Before starting: put a small pen dot on the skin of the forehead right at the band's lower edge on the midline, and a second dot at the right temple pad's front edge.
3. Every 2 min move the halo to the next station in this loop: front stop, vertex, upper occiput, bun (α ≈ 90°), β +40° (left side; spec §3.1: +β is toward the left ear), β −40° (right side), then repeat. At each move Michael says a lean score 0–10 (0 = can't feel the pad's weight pulling; 10 = constantly aware of it pulling).
4. At 20 min measure how far each dot is from its band edge: slip angle ≈ displacement (mm) ÷ 100 mm × 57.3°. **3° ≈ 5 mm** at the forehead (radius ≈ 100 mm).

| Minute | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | Max (≤ 2) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Station | | | | | | | | | | | |
| Lean 0–10 | | | | | | | | | | | |

Forehead dot slip ___ mm = ___° ; temple dot slip ___ mm = ___° (≤ 3°) ☐ **C3 PASS ☐**

### 8.4 C4 — Fences (red line 6, V18)

**Pass line:** ear ≥ 25 mm (expect ≥ 30) and hairline guard verified with the halo displaced ±15 mm.
**Kit:** steel rule, helper, mirror, washable eyeliner, the **nail-reach line** painted on the pad skirt by PAD (the outermost point any nail can reach including ±17 mm amplitude and the 5.5° tilt, from the CAD C8 sweep).
**Steps.**
1. Helmet seated, unpowered. Mark Michael's hairline (midline and above each eyebrow) and each ear canal entrance (tragus notch) with eyeliner dots.
2. **Hairline:** halo at the α front stop, β = 0, −40°, +40°. Measure from the nail-reach line to the hairline dot along the scalp. Pass: the reach line is **behind** the hairline at every β (record the margin in mm, + = behind), and the front band lies between the pad and the eyes.
3. **Ear:** at β = +40° and −40°, each α detent from front stop to bun. Measure from the nearest point of the reach line (or any moving part of the pad) to the tragus notch dot. Pass: ≥ 25 mm everywhere (expect ≥ 30).
4. **Displaced ±15 mm:** push the whole helmet 15 mm forward, back, left, right (ruler against the brow midline/temple; helper holds it there). Repeat steps 2–3 at the worst pose from steps 2–3. Pass: same lines still hold.
5. **Coverage (V18, record):** on a printed head map, shade every station the pad reaches; estimate % of the scalp area reached (spec expects ≈ 85 %).

| Pose | Hairline margin (mm, + behind) | Ear distance L / R (mm, ≥ 25) | Displaced ±15 worst (mm) | ✓ |
|---|---|---|---|---|
| α front stop, β 0 | | — | | ☐ |
| α front stop, β ±40 | | / | | ☐ |
| α 45, β ±40 | — | / | | ☐ |
| α 90 (bun), β ±40 | — | / | | ☐ |

Coverage estimate ___ % **C4 PASS ☐**

### 8.5 C5 — Noise at the ear

**Pass line:** at the tragus within 3 dB of room level with pins up; earplug A/B indistinguishable.
**"Pins up" needs a dry run** (drums and valves cycling with the pad retracted). §8.6 of the spec has no such command; FIRMWARE is asked for `dryrun` (§15 item 12). Until it exists, run on the wig head 1 m away with the umbilical to Michael's helmet unattached — this measures the air path only; note it on the sheet.
**Steps.**
1. Helmet on Michael, box in its session place (desk/chair back). Room quiet, AC off for the minute.
2. Phone mic held next to the right tragus (and then the left). LAeq 30 s: box off; box on (`dryrun` MIX). Background-correct (R-4). Pass: (on − off) ≤ 3 dB at both ears.
3. **Earplug A/B (bone path):** Michael in foam earplugs, eyes closed. Helper runs 10 trials of 10 s each, on or off at random (coin flip, written down first), using `dryrun` start/stop. Michael says "on" or "off". **Pass: ≤ 7 correct out of 10** (8+ correct is unlikely by guessing, p ≈ 0.055; §15 item 16).

| Item | Room (dBA) | On (dBA) | Diff (≤ 3) | ✓ |
|---|---|---|---|---|
| Right tragus | | | | ☐ |
| Left tragus | | | | ☐ |
| Earplug A/B correct /10 (≤ 7) | | | | ☐ |

Dry run used: `dryrun` ☐ / air-path fallback ☐ **C5 PASS ☐**

### 8.6 C6 — Umbilical

**Pass line:** head share ≤ 15 g; yaw torque at ±60° ≤ 0.02 N·m; clip pops at 3 ± 1 N; lanyard parts before any tube is taut; stand-up ×5.
**Steps.**
1. **Head share:** helmet on the foam head standing on the kitchen scale. Lift the umbilical's free loop so none of it rests on the head; tare. Let the loop hang from the 3 N clip as in use (clip on its stand beside the "ear", 100–200 mm out). Read the increase. Pass ≤ 15 g.
2. **Yaw torque:** foam head on the lazy-susan turntable (K25), a 100 mm dowel arm glued to the head's crown pointing sideways. First, umbilical unclipped: pull the arm's end tangentially with monofilament to the pocket scale (R-1) and read the force to start rotating = turntable friction f₀. Then umbilical clipped as in use, rotate the head to +60° and −60° and read the force needed to hold it there (the umbilical's restoring pull) = f. Torque = (f − f₀) in N × 0.100 m. Pass ≤ 0.02 N·m (≤ 20.4 g net at 100 mm). If f₀ > 10 g, the turntable is too stiff: use a better bearing or a plate on three marbles.
3. **Clip:** luggage scale on the riser just above the clip; pull straight away from the clip 5 times. Pass: every pop 204–408 g (3 ± 1 N).
4. **Lanyard first:** clip popped, pull the umbilical slowly away from the head (hand on the bundle 300 mm out). Watch the lanyard pogo and the tubes/housings: the pogo must separate while every tube and housing between the right hub and your hand is still slack. 5 trials. Pass 5/5.
5. **Stand-up ×5:** (a) on the foam head: system in READY (rail live, lever held by you, pad retracted), carry the head 1 m away quickly: clip pops, lanyard parts, rail dies (LED), 5/5. (b) on Michael, same state, he stands up and steps away: rail dies, no tube pulled tight, tug rating 0–10 recorded (≤ 2 expected). 5/5.

| Item | Values | Limit | ✓ |
|---|---|---|---|
| Head share (g) | | ≤ 15 | ☐ |
| Turntable friction f₀ (g); f at +60 / −60 (g); torque (N·m) | ; / ; | ≤ 0.02 | ☐ |
| Clip pops (g) ×5 | / / / / | 204–408 | ☐ |
| Lanyard before any tube taut | /5 | 5/5 | ☐ |
| Stand-up foam head; on Michael (tug 0–10) | /5 ; /5 (tug ___) | 5/5 | ☐ |

**C6 PASS ☐**

### 8.7 C7 — Doff (red line 10)

**Pass line:** 10 eyes-closed trials ≤ 3 s (max ≤ 2.5 s); spec §7.7 also: lift force at the lip ≤ 20 N. This file reads it as **every one of the 10 trials ≤ 2.5 s** (§15 item 17).
**Steps.**
1. Helmet on Michael, system in PLAY on the head at F 0.20 N (PHC-B done), lever in one hand, eyes closed.
2. Helper films at 240 fps (or normal video) and says "go" at a random moment.
3. Michael: release the lever → grab the doff lip → tilt up and back until the helmet is off the head.
4. Time from "go" (audio onset in the video) to the cradle clear of the occiput.
5. **Lift force:** helmet on the foam head; luggage scale hooked to the doff lip, pull up and back as Michael does; read the peak, 3 pulls. Pass ≤ 2.04 kg (20 N).

| Trial | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Max (≤ 2.5 s) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| s | | | | | | | | | | | |

Lip force ___ / ___ / ___ kg (≤ 2.04) ☐ **C7 PASS ☐**

### 8.8 C8 — Whole-system wig

**Pass line:** 20 min MIX with station moves: B5 pass lines again.
**Procedure:** helmet on W-S, 20 min MIX at F 0.30 N with a station move every T_dwell (as Michael will use it), then HB-3, HB-4, HB-5, HB-6 (3 trials per force) and HB-8 shed counting over the 20 min; re-score H-6.8 (§6.2). Fill a fresh §6.3 sheet with stage = C. **C8 PASS ☐**

### 8.9 C-S — Wearability session

**Spec:** a 20-minute MIX session with ≥ 4 station moves: "does the hat move?" ≤ 2/10; "having to move it" ≤ 3/10.
PHC-B, then 20 min MIX, Michael's knobs, ≥ 4 moves by Michael (dwell chime). Full §12 form at 10 and 20 min.

| Date | Moves | Q11 hat moves (≤ 2) | Q10 having to move it (≤ 3) | Q1 satisfying | Q3 machine | Pulls | ✓ |
|---|---|---|---|---|---|---|---|
| | | | | | | | ☐ |

**GO C:** C1–C8 passed and both C-S lines met. If "having to move it" > 3/10 or the hat moves > 2/10, note it: it feeds the Stage D decision (powered drift, pad 2). ☐ GO C Date ______

---

## 9. Stage D — sessions D1–D4 (20-minute evenings)

**Spec:** D1–D4 are 20-minute evenings with the **armrest switch** (forearm-weight hold-to-run, RT1 #10). Then D5 (§10).
**Armrest switch acceptance (once, before D1):** A0 timing method on the new switch (10 lifts: K1 aux opens ≤ 5 ms), and PHC-B item B-12 done 10 times (10/10 forearm lifts kill the rail). The lever stays wired as the alternative; the e-stop stays under the free thumb.

| Session | What | Forms |
|---|---|---|
| D1 | 20 min MIX, Michael's knobs, INTENSITY range now 0.10–0.50 N (spec §8.4, after D1) | §12 at 10 and 20 min; voice ratings every 2 min |
| D2 | same; ask explicitly: "did the hat move with the strokes?" (RT1) | same |
| D3 | same; Michael picks the stations | same |
| D4 | same; one evening in the other seat/couch placement (spec §6) | same |

Log every session on §13. These four evenings and the first D5 evenings count toward GO D.

**GO D (SP1 hypothesis, amended north star), operational definition (§15 item 13):** over **5 consecutive** Stage D sessions at Michael's own preferred settings (D1–D4 plus the next one, or any later run of 5): **median end-of-session Q1 ≥ 7**; **median Q3 ≤ 3**; **Q9 "want it again tomorrow" = YES in ≥ 4 of 5**; **zero tuft pulls in all 5**. Then, on evidence (spec §10): powered drift (leap4-C C2) if median Q10 "having to move it" > 3; pad 2 if median Q12 lean > 3 or the free text says lean.

| Session | Date | Q1 | Q3 | Q9 again | Tuft pulls | Q10 move | Q12 lean | Counted ✓ |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | ☐ |
| | | | | | | | | ☐ |
| | | | | | | | | ☐ |
| | | | | | | | | ☐ |
| | | | | | | | | ☐ |
| **Median / count** | | | | /5 | | | | |

☐ GO D ☐ NO-GO Date ______

---

## 10. Stage D5 — blind experiment matrix

**Spec (§10):** blind matrix, ≤ 1 variable per block: PLINE vs MIX; F 0.2 / 0.3 / 0.45 N; variation on/off; B-contrast on/off; chords on/off; D-paths on/off; stations moved by Michael vs by a helper.

### 10.1 Design rules

- **Reference condition D\*** = Michael's preferred settings at the end of D1–D4 (write its settings code here: ______________). Every block holds everything at D\* except its one variable.
- **One variable per block.** Never change two things between arms. The station sequence is the same for both arms of a block (see 10.3).
- **Blind wherever the variable allows** (all but D5-S). The helper runs it with §14; without a helper, use the firmware's `bset` / `blind` / `next` / `reveal` (spec §8.6).
- **Contact budget:** ≤ 20 min per evening (firmware cap). ≥ 20 h between evenings. Stop rules §3 apply; a stopped bout is re-run another evening, never "made up" in the same one.
- **Forms:** the §12 short form after every bout (within 60 s, nails up); the full form at the end of the evening; Q-BLIND ("which arm do you think that was?") after each block.
- **Masking:** nail hiss is part of the scratch, so do not mask by default. Before each new block the helper listens from Michael's position to both arms for 20 s with the pad on the wig head: if the arms sound different, run the block with the fan/white-noise speaker on at a fixed level for **both** arms and note "masked".
- **Order:** randomise the order of blocks across evenings (draw block cards from a cup). Within a block, the arm order is drawn as in 10.3.

### 10.2 The matrix

| Block | Variable | Arm A | Arm B (C) | Held at D\* | Bouts per run (order) | Bout length | Runs (evenings) | Blind | Primary outcome | Decision rule |
|---|---|---|---|---|---|---|---|---|---|---|
| **D5-M** | Mode | PLINE (`mode pline`) | MIX (`mode mix`) | F, f, variation, groups, chords, D-paths | 4 (ABBA or BAAB) | 2 × T_dwell, max 3 min | 2 (+1 if split) | yes | forced choice per pair; Q1 | W-2 |
| **D5-F** | Force | 0.20 N | 0.30 N (C = 0.45 N) | mode, f, variation; **groups alternate A/B single (never A+B), `bratio 1`** so 0.45 N is deliverable within the float budget (§15 item 14) | 6 (Williams order: ABC CBA, BCA ACB or CAB BAC) | 2 min | 2 | yes | Q1, Q5 discomfort, Q7 intensity fit, pulls | W-3 |
| **D5-V** | Variation | `vary on` | `vary off` | all else | 2 (AB or BA), voice Q1 every 2 min | 8 min | 2 (reverse order) | yes | Q1 at minute 8 and the **slope** of Q1 from minute 2 to 8 (habituation, RT1 #12) | W-V |
| **D5-B** | B-contrast | on (B at 0.5–1.0 × rail in contrast phrases) | off (`bratio 1`) | all else | 4 (ABBA / BAAB) | 2 × T_dwell, max 3 min | 2 (+1) | yes | forced choice; Q1 | W-2 |
| **D5-C** | Chords | `chord on` | `chord off` | all else | 4 | as D5-B | 2 (+1) | yes | forced choice; Q1 | W-2 |
| **D5-P** | D-paths | on (bursts) | off (`dpath 0`) | all else | 4 | as D5-B | 2 (+1) | yes | forced choice; Q1 | W-2 |
| **D5-S** | Who moves the halo | Michael moves (lever release, move, MOVED) | helper moves on the chime (Michael keeps eyes closed, releases the lever, helper moves and presses MOVED) | all else | 1 full 20-min session per run, ≥ 4 moves | 20 min | 4 (M H H M) | **no** (open label: Michael always knows) | Q10 "having to move it", Q1, Q3 | W-S |

Firmware notes: the spec's commands are in §8.6 (`mode`, `force`, `groups`, `bratio`, `vary`, `chord`, `dpath`, `bset`, `blind`, `next`, `reveal`, `rate`). If a command is missing or behaves differently, write the actual command used on the sheet.

### 10.3 Stations inside a block

The station dwell timer forces moves (T_dwell from HB-9). So a bout is **two stations × min(T_dwell, 90 s)** of contact. For each block run, the helper writes a station list before starting, e.g. *vertex → upper occiput → left parietal → right parietal → vertex → …*, and **both arms walk the same list in the same order**. Bout k always starts at station k of the list.

### 10.4 Decision rules

- **W-2 (two arms, ABBA):** after bouts 1–2 and after 3–4, Michael answers the forced choice "which of the last two felt more like being scratched well: first or second?" (2 choices per run). After 2 runs (4 choices): **4/4 for the same arm → decided.** **3/4 and mean Q1 difference ≥ 1.0 → decided.** Otherwise run a third evening: **≥ 5/6 and mean Q1 difference ≥ 1.0 → decided**; else **"no difference"** (a result: that knob does not matter at this precision; keep the cheaper or simpler setting).
- **W-3 (force):** exclude any level with a felt pull or Q5 discomfort > 3 in any bout. Among the rest, the level with the highest mean Q1 wins if it beats the next by ≥ 1.0; otherwise "flat" → keep the lower force. Note Q7 "intensity fit" (5 = just right).
- **W-V (variation):** variation wins if Q1 at minute 8 is higher by ≥ 1.0 **or** the minute 2→8 slope is less negative by ≥ 1 point per 6 min, in both runs; "no difference" otherwise (then keep it on: it is a spec requirement, DECISION-3 #9).
- **W-S (mover):** report means of Q10 and Q1 for each mover over 2 runs each. If Michael-moved Q10 > 3 and helper-moved Q10 ≤ 2, the "having to move it" cost is real → the spec's powered-drift branch (leap4-C C2). Open-label: treat as indicative.
- **Blinding check:** if Q-BLIND guesses are right in ≥ 3 of 4 arms in a block, record "blind broken" next to the result and repeat that block masked.

### 10.5 Session count

2-level blocks (M, B, C, P): 4 × 2 runs × 10–12 min = two block-runs per evening → **4 evenings** (+ up to 2 for third runs). D5-F: **2 evenings** (12 min each; the remaining minutes are free D\* play, not rated). D5-V: **2 evenings** (16 min). D5-S: **4 evenings** (these also count as normal D sessions for GO D). **Total ≈ 12 evenings (≤ 14).**

### 10.6 D5 results sheet (one per block)

CSV `results/D5.csv`: one row per bout, using the §12 header (block_id, run, bout, arm_code filled; arm_true filled at reveal).

Block ______ Run ___ Date ______ Helper ______ Masked y/n Station list: ______________________

| Bout | Arm code (blind) | Station(s) | Q1 | Q2 type | Q3 | Q5 | Pulls | Forced choice (pair) | Arm (after reveal) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | 1 vs 2: ___ | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | 3 vs 4: ___ | |
| 4 | | | | | | | | | |
| 5 (F only) | | | | | | | | — | |
| 6 (F only) | | | | | | | | — | |

Q-BLIND guesses: ______ Correct ___/4 Result for this run: A / B / C / none

**Block summary after all runs:** choices for A ___ / B ___; mean Q1 A ___ B ___ (C ___); rule ___ → **decision:** ______________

---

## 11. Pre-human safety checklist v3

Two parts. **PHC-A** is filled **once per build state** (redo it after any mechanical, nail, pneumatic, electrical or firmware change) and copies measured values from the gate sheets. **PHC-B** is filled **before every session**, takes ≈ 10 minutes and costs nothing. **Any unticked box, or any value outside its limit, means no session.** (Red line 12; safety-requirements §6; spec §7.)

### 11.1 PHC-A — build state

Build state ID ______ Firmware version (boot banner) ______ Date ______ Initials ____
Variant: ☐ bench pad (A-S: items marked "B+" are N/A) ☐ full helmet (B, C, D)

**A1 Visual and build**

| # | Check | Limit / source | Value / date | OK |
|---|---|---|---|---|
| A1.1 | Printed and bonded parts: no cracks, delamination, glue line gaps (bail nodes, hubs, carriage, deck, cartridges) — loupe | none | | ☐ |
| A1.2 | Load-bearing parts unchanged since their proof test (B3; bail node 10 N, cradle 20 N per H9) | yes | B3 date ____ | ☐ |
| A1.3 | Skin-side edges R ≥ 1 mm, nail tips R ≥ 0.4, shaft tops domed R 0.5; tape test passed | B3 | B3 date ____ | ☐ |
| A1.4 | No fastener tip, wire, zip-tie tail or burr toward the scalp | none | | ☐ |
| A1.5 | Nothing rotates within 30 mm of hair; no open sliding slot (red line 1) | — | | ☐ |
| A1.6 | No 0.04–3 mm gap within 25 mm of the scalp; block–deck gap ≥ 32 mm from skin (HB-5; CAD C8 sweep report on file) | 0 captures | HB-5 date ____ | ☐ |
| A1.7 | Nails red/orange, one piece, count of spares ≥ 2 | — | spares ___ | ☐ |

**A2 Force and mechanics** (copy from the sheets)

| # | Check | Limit | Measured | OK |
|---|---|---|---|---|
| A2.1 | R1a / R1b (kPa) [A1] | 19.2–22.2 / nominal ± 1.5 | / | ☐ |
| A2.2 | R2 / R2b (kPa) [A1] | 19.2–22.2 / nominal ± 1.5 | / | ☐ |
| A2.3 | P1 / P3 deadhead (kPa) [A1] | ≤ 50 / ≤ 30 | / | ☐ |
| A2.4 | Nail breakaway, lowest – highest of all nails (g) [A2.1] | 12.2–25.5 | – | ☐ |
| A2.5 | One nail at R1b, worst (g) [B2] B+ | ≤ 93.8 | | ☐ |
| A2.6 | Total normal at R2b, worst (g) [B2] B+ | ≤ 1,224 | | ☐ |
| A2.7 | Bottomed nail, worst (g) [B2, RC6] B+ | ≤ 106 | | ☐ |
| A2.8 | Coupling release range (g) [B2] B+ (bench pad: A3 coupling test) | 173–235 | – | ☐ |
| A2.9 | Retract margin on mocks, worst (mm) [A3, RC6] | ≥ 15 | | ☐ |
| A2.10 | Vented nails retract ≥ 8 mm, worst (ms) [A2.7, RC7] | ≤ 200 | | ☐ |
| A2.11 | Gallery vent, worst (ms) [A2.4, RC3] | ≤ 100 | | ☐ |
| A2.12 | Fail-to-free: pad ≥ 25 mm, worst (ms) [B4] B+ | ≤ 150 | | ☐ |
| A2.13 | Kinematic mount breakaway (g) [B3] B+ | 408–816 | | ☐ |
| A2.14 | Helmet mass (g) [B1/C2] B+ | ≤ 320 | | ☐ |
| A2.15 | Doff, one hand, eyes closed, 3 trials before the first B session (C7 later does 10) B+ | ≤ 3 s each | / / | ☐ |
| A2.16 | Bench pad only (A-S): pad + slug resting weight on a foam dome (g) | ≤ 400 | | ☐ |

**A3 Electrical**

| # | Check | Limit | Measured | OK |
|---|---|---|---|---|
| A3.1 | Adapter certification mark visible; output metered (V) | 23–25 V | | ☐ |
| A3.2 | No mains inside the box; no lithium cell anywhere (red line 5) | yes | | ☐ |
| A3.3 | Inlet fuse 3.15 A slow fitted; spare in the kit | yes | | ☐ |
| A3.4 | A0 loop: every element opens K1 ≤ 5 ms; weld check fires; logic stays up | A0 sheet | A0 date ____ | ☐ |
| A3.5 | Stepper VREF measured on each driver (V) vs ELECTRONICS target (≤ 0.35 A) | ≤ target | / / | ☐ |
| A3.6 | Harness: every wire across the hinge and through the right hub sleeved, strain-relieved, no exposed conductor | yes | | ☐ |
| A3.7 | Thermal: 1 h run, hottest touchable part (°C) [A5]; nothing on the head is powered | ≤ 48 | | ☐ |

**A4 Functional and firmware**

| # | Check | Limit | Value / date | OK |
|---|---|---|---|---|
| A4.1 | Reflex trip, worst (ms) and false trips [A4, RC4] | ≤ 50; 0 | ; | ☐ |
| A4.2 | Path checker + IK unit tests pass on this firmware [A3] | all pass | version ____ | ☐ |
| A4.3 | Boot limits table matches the spec: rail clamp 15.6 kPa; F 0.20–0.45 N (Stage B) / 0.10–0.50 N (after D1); f ≤ 2.0 Hz; \|d\| ≤ 16.5 mm; v ≤ 200 mm/s; a ≤ 2 m/s²; session cap 20 min; dwell = T_dwell | match | | ☐ |
| A4.4 | Hair gate (HB full, or HB-mini for A-S) passed; H-6.8 total and gating zeros [§6] | ≥ 28, 0 | ___ /36 | ☐ |
| A4.5 | RC1(c)(d) tether: worst peak (N), worst time above 0.15 N (ms) [HB-6/7] | ≤ 0.30; ≤ 20 | ; | ☐ |
| A4.6 | T_dwell (s) entered in the firmware [HB-9] B+ | set | | ☐ |
| A4.7 | Noise at the ear (C5) or box at 1 m (A5) (dBA) | per gate | | ☐ |

**A5 The 13 red lines (spec §7.5) — evidence present**

| RL | Short | Evidence | OK |
|---|---|---|---|
| 1 | no rotation within 30 mm | A1.5, HB-4/5 | ☐ |
| 2 | ≤ 2.5 N per element, mechanical | A2.1–A2.3, A2.5, A2.7 | ☐ |
| 3 | ≤ 12 N total, ≤ 2 N tangential | A2.6, A2.8 (A-S: A2.16) | ☐ |
| 4 | NC e-stop in series + hold-to-run | A3.4 | ☐ |
| 5 | no mains, ≤ 24 V, no lithium | A3.1, A3.2 | ☐ |
| 6 | nothing moving near hairline, ear, eyes | C4 (before C: stops set conservatively at α_hairline + 20° and β ±40°, checked by ruler) | ☐ |
| 7 | no self-locking drive | B2 step 5 | ☐ |
| 8 | free on power loss, e-stop, watchdog, stall | A2.11, A2.12, A0 | ☐ |
| 9 | retention, proof 3× | B3 | ☐ |
| 10 | doff ≤ 3 s, no strap, ≤ 500 g | A2.14, A2.15 | ☐ |
| 11 | edges, tape test | A1.3 | ☐ |
| 12 | checklist + wig test + glasses + ≤ 5 min first session | this sheet, A4.4, PHC-B | ☐ |
| 13 | firmware never the only barrier | A4.1 is backed by RC1 (A4.5) and the comparator; A4.3 is backed by reliefs | ☐ |

Signed ______________ Date ______ **PHC-A valid for build state ______**

### 11.2 PHC-B — every session (≈ 10 min)

Session # ____ Date ______ Time ______ PHC-A build state ______ (must match the hardware today)

| # | Check | Value | OK |
|---|---|---|---|
| B-1 | Safety glasses on before the rail is powered | — | ☐ |
| B-2 | Hair: no gel/spray; nothing tied, clipped or hanging near the bail, hubs or umbilical exit; no jewellery, hood strings, earbud cables | — | ☐ |
| B-3 | Scalp checked in the mirror (photo): no broken skin, rash, sunburn; no haircut or chemical treatment in the last 24 h | photo # ___ | ☐ |
| B-4 | Seat: headrest ≥ 120 mm behind the bun, or none; 0.5 m clear around; box placed (desk / chair back / couch back) | headrest gap ___ mm | ☐ |
| B-5 | Umbilical: clip beside the right ear, free loop to the hub (≥ 450 mm), nothing tied | loop ___ mm | ☐ |
| B-6 | Walk-round: no crack, loose screw, frayed tendon, kinked tube, torn Penrose; wiper skirt clean | — | ☐ |
| B-7 | **Nail count = 6** | ___ | ☐ |
| B-8 | **RC1(e) hang test**, pad off its magnets, nails down, pins vented: a **10 g** loop-and-bag must **hold**, a **25 g** bag (5 nickels) must **release**, every nail; re-seat each nail after | N1 ☐ N2 ☐ N3 ☐ N4 ☐ N5 ☐ N6 ☐ | ☐ |
| B-9 | Wipers closed after re-seating (look up each bore with the lamp: no open hole) | — | ☐ |
| B-10 | Power up: boot limits table read; firmware version = PHC-A; SELFTEST passed; `status` shows no FAULT | version ___ | ☐ |
| B-11 | **E-stop:** hold the lever → ARMING; press e-stop → ACT-12 LED off; twist release → nothing moves until the lever is held again → ARMING again | — | ☐ |
| B-12 | **Lever (or armrest switch in Stage D) released 3×** → LED off each time; no weld-check FAULT at re-arming | 3/3 | ☐ |
| B-13 | **Head-present:** helmet on, READY, lever held; lift the forehead pad 10 mm with a finger → LED off | — | ☐ |
| B-14 | Pressures at READY (`sensors`): rail ≤ 15.6 kPa; palm per setting | rail ___ palm ___ kPa | ☐ |
| B-15 | Session settings written on the §13 log before starting; INTENSITY ceiling for the stage (B: 0.20–0.45 N; D after D1: 0.10–0.50 N) | code ___ | ☐ |
| B-16 | Timer: phone alarm at the session limit (2 / 5 / 10 / 20 min); firmware cap 20 min | limit ___ min | ☐ |
| B-17 | E-stop puck under the free thumb; lever / armrest under the other arm; both found with eyes closed | — | ☐ |
| B-18 | Doff rehearsed once with the pad retracted: release, lip, tilt off | ___ s (≤ 3) | ☐ |
| B-19 | Nails and skids wiped with 70 % IPA ≥ 1 min ago | — | ☐ |
| B-20 | Black towel over the shoulders; lint roller, forms, pen; voice memo and 240 fps ready; someone told where you are if alone | — | ☐ |
| B-21 | Room: RH ___ %, temp ___ °C, room noise ___ dBA | | ☐ |
| B-22 | Michael: rested, not unwell, no alcohol; not within 20 h of the last session; no redness left from the last one | hours since last ___ | ☐ |

Signed ______________ Time ______

**After the session (≈ 5 min):** lever released, e-stop pressed, adapter unplugged **first** · nail count ___ (6?) · lint-roll towel and pad underside, count hairs bulb ___ broken ___ · pad off its magnets, nails out, IPA wipe of nails, skids, cover · look into every bore and gap with the lamp for trapped hair (a found hair is a **design item**: log it) · scalp photo now ___ and phone reminders at 10 and 60 min · CSV rows typed.

**Weekly, or every 10 sessions (spec §4.4, H9, H10):** inspect each tendon at the drum and the spring ferrule (replace at the first broken strand or 50 sessions); lanyard pull test (rail dies); clip pop once with the luggage scale (204–408 g); one B4 power-pull on the wig head; RC1(a) on two nails with the pocket scale (12.2–25.5 g); wash the wiper skirt plate; tape test one nail; torque-mark check on all fasteners.

---

## 12. Feedback form (amended goal)

**The goal (DECISION-2 north-star amendment):** a scratch **as satisfying as being scratched well by a person** — crisp edge reaching the scalp, right force and speed, coverage, no habituation. It does **not** have to feel like a real hand. It must be a **scratch, not a brush, massage or vibration.**
**How to fill it:** nails up (bout over), within 60 s. Say the numbers into the voice memo first, write them after. Don't look at earlier forms. 0 and 10 are the ends of each scale as written; 5 is the middle.
**Anchor for Q1:** 10 = the best scratch a person has given you; 5 = "fine, but I'd rather have a person do it"; 0 = nothing worth having. If a helper can, give Michael 30 s of a real fingernail scratch at the crown once before Stage B to re-anchor "10".

### 12.1 Short form — after every bout

Session ___ Bout ___ Stage ___ Block/arm code ___ Station α___β___ Settings code ______ Contact s ___

| # | Question | Answer |
|---|---|---|
| Q1 | **How satisfying was that, compared with being scratched well by a person?** 0 = worthless … 10 = as good as the best person scratch | ___ |
| Q2 | **What was it?** circle one: **SCRATCH** · BRUSH · RUB/MASSAGE · BUZZ/VIBRATION · TAP/POKE · NOTHING | |
| Q2b | Crisp edge on the skin, on both directions of the stroke? Y / N / only one way | |
| Q3 | **"Machine on my head"** — how much were you aware of wearing a machine (weight, lean, noise, movement, the umbilical)? 0 = forgot it · 10 = all I could think about | ___ |
| Q4 | **Pulls:** number of hair pulls you felt ___ · small tugs ___ · tuft pull (several hairs, hurt after) Y / N | |
| Q5 | **Discomfort or pain** 0 = none · 10 = stop now | ___ |
| Q6 | **Noise** — how annoying was the sound? 0 = didn't notice · 10 = intolerable. Did you hear the machine (not the nail hiss)? Y / N | ___ |
| Q7 | **Intensity fit** 0 = far too light · 5 = just right · 10 = far too hard | ___ |
| Q8 | **Want more of exactly this?** 0 = turn it off · 10 = don't stop | ___ |
| Q-BLIND | (blind blocks only) Which setting do you think that was? A / B / C / no idea | |
| Pair | (pairs only) The last two bouts: which felt more like being scratched well? first / second / same | |

### 12.2 End-of-session form (add to the last bout's form; also at 10 min in 20-min sessions)

| # | Question | Answer |
|---|---|---|
| Q9 | **Do you want this again tomorrow?** YES / maybe / NO | |
| Q10 | **"Having to move it"** — how much did moving the halo between stations break the experience? 0 = not at all · 10 = ruined it | ___ |
| Q11 | **Does the hat move?** with the strokes or as you moved your head. 0 = never · 10 = constantly | ___ |
| Q12 | **Lean** — did you feel the pad's weight pulling the helmet to one side? 0 = no · 10 = constantly | ___ |
| Q13 | **Did it fade?** minute when it got less satisfying ___ (or "never"); did a station move bring it back? Y / N | |
| Q14 | **Speed fit** 0 = far too slow · 5 = right · 10 = far too fast | ___ |
| Q15 | **Coverage** — it scratched where I wanted it. 0 = never · 10 = always | ___ |
| Q16 | Best station today ___ ; best mode/setting (if you know) ___ | |
| Q17 | Anything sharp, any tap or poke, any pattern you could predict, anything that felt like a machine: ______________________ | |
| Q18 | One sentence: what would make it as good as a person scratching? ______________________ | |

### 12.3 CSV header (one row per bout; append to `results/sp1v3_bouts.csv`)

```
session_id,date,time,stage,block_id,run,bout,arm_code,arm_true,blind,masked,station_alpha,station_beta,region,settings_code,mode,f_hz,force_n,groups,bratio,vary,chord,dpath,seed,contact_s,q1_satisfying,q2_type,q2b_crisp,q3_machine_on_head,q4_pulls_felt,q4_tugs,q4_tuft_pull,q5_discomfort,q6_noise,q6_heard_machine,q7_intensity_fit,q8_want_more,q_blind_guess,pair_choice,q9_again_tomorrow,q10_having_to_move,q11_hat_moves,q12_lean,q13_faded_min,q13_move_restored,q14_speed_fit,q15_coverage,q16_best_station,reflex_trips,nails_after,free_text
```

Rules: one row per bout; the end-of-session columns (q9…q16) are filled only on the last bout's row (and the 10-min row in 20-min sessions), blank elsewhere; `arm_true` is filled only after `reveal`; text fields in double quotes.

---

## 13. Session log template

One per session; staple the bout forms behind it. Type it into `results/sp1v3_sessions.csv`.

```
SP1 v3 SESSION LOG
Session # ____  Date ________  Start ______  End ______  Stage: A-S / B-S_ / C-S / D_ / D5-___ run ___
Build state ______  Firmware ______  PHC-A date ______  PHC-B signed ☐  Helper: y / n  Name ______
Seat / placement: desk / chair back / couch back   Headrest gap ___ mm   Box distance ___ m
Hair today: washed y/n, products none ☐   RH ___ %   Room ___ °C   Room noise ___ dBA
T_dwell ___ s   INTENSITY range ___–___ N   SPEED ___ Hz   MODE start ______
Planned bouts (stations, settings codes, blind order sealed y/n): __________________________________
Contact limit today ___ min   Actual contact (firmware E log) ___ min   Station moves ___
Nail count before 6 ☐  hang test ☐   after ___   (≠ 6 → find it before the next session)
Lever releases ___   e-stop presses ___   reflex trips ___   FAULTs ___   reason(s): __________________
Pulls felt ___   tugs ___   TUFT PULL y/n (y → STOP, redesign item # ____, HB re-run)
Shed hairs on towel + pad: bulb ___ broken ___
Scalp photo: 0 min ☐ 10 min ☐ 60 min ☐ next morning ☐   Findings: none / redness gone by ___ min / other ______
Device findings after (hair in a gap, wiper open, loose part, tendon wear): __________________________
End-of-session: Q1 ___  Q3 ___  Q9 again tomorrow ___  Q10 ___  Q11 ___  Q12 ___
Stop rules triggered (§3.2): none / ______________
Next session plan / changes to build state (→ new PHC-A if hardware or firmware changed): ____________
```

**CSV header (`results/sp1v3_sessions.csv`):**

```
session_id,date,start,end,stage,block_id,run,build_state,firmware,phc_a_date,phc_b_ok,helper,placement,headrest_gap_mm,rh_pct,room_c,room_dba,t_dwell_s,force_min_n,force_max_n,contact_limit_min,contact_min,station_moves,nails_before,hang_test_ok,nails_after,lever_releases,estop_presses,reflex_trips,faults,pulls_felt,tugs,tuft_pull,shed_bulb,shed_broken,scalp_findings,device_findings,q1_end,q3_end,q9_end,q10_end,q11_end,q12_end,stop_rules,notes
```

**Gate results CSV header** (all gate sheets, `results/gates.csv`, one row per measured value):

```
date,stage,gate,item,unit_under_test,trial,value,unit,limit_low,limit_high,pass,instrument,build_state,initials,notes
```

---

## 14. How to have a helper run a blind test

Give this page to the helper. It takes 10 minutes to read; the first blind block takes ≈ 40 minutes including setup.

### 14.1 What "blind" means here

Michael must not know which setting he is feeling until he has rated it. Anything that tells him — what you say, the laptop screen, the sound of a keyboard at a telling moment, how long a bout lasts, the order always being the same — breaks the test, and the result is then worth much less. Your job is to make every bout look, sound and last the same, except for the one setting under test.

### 14.2 Your safety role comes first

- You may press the **e-stop** at any time if anything looks wrong (a hair caught, the helmet slipping, Michael saying "stop", a smell, a noise). You never hold, tape or press the hold-to-run lever or armrest switch for him.
- You never touch the pad or the helmet while the rail is live (LED on). To move the halo (D5-S only), wait for Michael to release the lever and the pad to lift.
- If a stop rule (§3) happens, the block ends. Write down what happened; do not continue "to finish the block".

### 14.3 Before Michael sits down

1. Read the block's row in §10.2. Write the two (or three) settings as **arm A, arm B (arm C)** on your private sheet with the exact commands.
2. **Draw the order:** for a 2-arm block, flip a coin: heads = **ABBA**, tails = **BAAB**. For the 3-arm force block, roll a die: 1–2 = ABC CBA, 3–4 = BCA ACB, 5–6 = CAB BAC. Or on the laptop: `python3 -c "import random; print(random.choice(['ABBA','BAAB']))"`. Write the order on your sheet and **fold it over**.
3. Write the station list (§10.3) on your sheet. Both arms use the same list.
4. Load the arms. **Preferred (firmware does the blinding):** `bset A {...}`, `bset B {...}` (and C), then `blind <n>`; the firmware picks and hides the order, `next` starts each bout, `reveal` shows the order at the end (spec §8.6; check the exact syntax in the firmware README). **Manual:** you type the arm's commands before each bout from your folded sheet.
5. Turn the laptop so Michael cannot see it, even in a reflection (windows, glasses, a TV screen). Mute keyboard sounds if you can; type something before **every** bout, even when nothing changes, so typing is not a clue.
6. Masking check (§10.1): run both arms for 20 s on the wig head; listen from Michael's chair. If you can hear a difference, put the fan / white-noise speaker on at the same level for the whole block.

### 14.4 During the block — say only these things

| When | You say | You do |
|---|---|---|
| Before each bout | "Bout ___, ready when you are." | Settings loaded (or `next`); start your stopwatch when the pad lands. |
| At the bout's end | "Time." | Michael releases the lever (nails up). |
| After each bout | "Please rate." | Hand him the short form; wait; don't watch him fill it in, don't comment. |
| After bouts 2 and 4 (2-arm blocks) | "Which of the last two was better: first or second?" | Write his answer. |
| Station change | nothing extra | Michael moves the halo himself (except D5-S helper arm). |
| If he asks "which one was that?" | "I'll tell you at the end." | Nothing. |

Do not say "this one", "the other one", "same as before", "now the strong one". Do not react to his answers. Keep bout lengths equal (use the stopwatch, not "it feels done"). Keep rests the same length (30 s nails up).

### 14.5 After the block

1. Michael fills Q-BLIND ("which arm do you think each was?") for every bout **before** you reveal.
2. `reveal` (or unfold your sheet). Fill the arm column on the results sheet (§10.6).
3. Note anything that might have leaked (a dropped command, a longer bout, a comment).

### 14.6 Without a helper

Use the firmware's `blind <n>` with `bset` slots; Michael starts each bout with `next` from a single key on the hand controller or the laptop without looking at the screen (screen off or turned away), rates on paper, and runs `reveal` only after the block. If the firmware's blind mode is not ready, the block is run **unblinded** and marked so; D5-M and D5-V results from unblinded runs count as indicative only.

### 14.7 The one block that cannot be blind

**D5-S (who moves the halo):** Michael always knows who moved it. Run it open-label: on Michael-moved evenings he moves it himself at every chime; on helper-moved evenings he keeps his eyes closed, releases the lever at the chime, the helper moves the halo to the next station on the list and presses MOVED, then says "ready". Same station list both ways.

---

## 15. Spec items not testable as written (summary)

Full text with proposed spec wording: **14-build/tests/CONFLICTS.md**. The operational definition in the right-hand column is what this file uses until the Director rules.

| # | Spec text (where) | Problem | Used here |
|---|---|---|---|
| 1 | RC1(c): "HX711 at 1 kHz" (ruling §4; spec §10 B5) | HX711 runs at 10 or 80 samples/s only; 80 SPS = 12.5 ms per sample, so "≤ 20 ms above 0.15 N" cannot be resolved | 100 g TAL221 + **ADS1115 at 860 SPS** on a $4 Pico (R-6) |
| 2 | A1: "deadheads measured (P1 ≤ 50 kPa)" | box sensors are 0–40 kPa (XGZP6847A); 50 kPa is off scale | external 0–15 psi dial gauge on a tee ($5–16) |
| 3 | A0: "each element opens ACT-24 within 5 ms" | ACT-24 carries 470 µF + TVS (H16), so the bus may take > 5 ms to fall with light load even when K1 opens in 1 ms | K1 aux NC contact ≤ 5 ms **and** bus < 2 V ≤ 50 ms (the weld-check window); bleeder resistor if needed |
| 4 | A3: "PLINE never retraces within 2 mm in 60 s" | every PLINE stroke passes through the centre; successive strokes are 4.5° apart (≈ 0.8–1.3 mm at the chord ends) and the heading repeats every ≈ 28.6 s, so a literal reading always fails | rosette with no heading gap > 15° and no trace visibly darker, **plus** the §8.4 no-repeat rule checked on the `B` log |
| 5 | A5 / §4.9: "≤ 30 dBA at 1 m" | below a phone's measuring floor and below a typical room | background-corrected; at 0.25 m minus 12 dB when the room is above 30 dBA |
| 6 | A-S (Stage A sensation) runs on Michael's head before the B5 wig gate and the B6 checklist; the helper's hand force on the hand-held bench pad is not a mechanical constant | red line 12 (wig test + checklist before any first session) and red line 3 (total force by a constant) | added A-S entry: HB-mini + PHC-A (bench variant) + **pad resting by its own weight ≤ 4 N**, helper only steadies |
| 7 | RC1(d): "with a 10 mm reflex retract mid-snag" | v3 has no partial retract (§1 C22: full fail-to-free) | HB-7 with e-stop, latch trip (`inject snag`) and lanyard pull |
| 8 | RC4 / A4: "trip ≤ 50 ms" | start point not defined; a real single hair plucks (≈ 0.7 N) or breaks (≈ 1 N) near the 0.8 N firmware threshold | monofilament tether; time from tether force > 0.8 N to rail-sense low (also record from 0.15 N) |
| 9 | B1: "moving group ≤ 125 g" | "moving group" not defined | carriage + float + pad (ledger 115.5 g) |
| 10 | GO B: "≥ 7/10 … machine ≤ 3/10" | which session(s) not stated | B-S4 end ≥ 7 and ≤ 3, plus ≥ 7 once more (another session or B-S4 at 10 min); zero felt pulls in all |
| 11 | B5: "matting run sets T_dwell" | no matting criterion | onset = comb-through > 1.5× K₀, a clump, or shed > 2× combing; T_dwell = last clean step of 30/60/90/120/180 s |
| 12 | C5 "with pins up"; A5 noise | no firmware command plays paths with the pad retracted | request `dryrun` from FIRMWARE; fallback = air path only, marked |
| 13 | GO D: "≥ 7/10 … wants it again tomorrow; zero tuft pulls over 5 sessions" | aggregation over sessions not stated | 5 consecutive D sessions: median Q1 ≥ 7, median Q3 ≤ 3, "again" YES in ≥ 4/5, zero tuft pulls |
| 14 | D5: "F 0.2 / 0.3 / 0.45 N" | §4.3 force budget limits all-six-down to ≈ 0.37 N per nail; at 0.45 N the firmware must clamp or change groups, so the level is not what it says | D5-F runs single groups alternating A/B, `bratio 1`, so 0.45 N is delivered (≤ 0.50 N per nail with one group down) |
| 15 | D5: "stations moved by Michael vs by a helper" in a "blind matrix" | cannot be blinded | open-label block D5-S, indicative only |
| 16 | S0/C5: "earplug A/B indistinguishable" | no trial count or criterion | 10 random trials; ≤ 7 correct = indistinguishable (8+ has p ≈ 0.055 by guessing) |
| 17 | C7: "10 eyes-closed trials ≤ 3 s (max ≤ 2.5 s)" | two limits; the second makes the first redundant | every trial ≤ 2.5 s |
| 18 | B5: "shed ≤ 2× combing" | per stroke or per run not stated | per 100 strokes (as 05-engineering L8.7) |

---

## 16. One-page gate summary (tick as you go)

| Gate | Pass line (spec) | Section | Date | ✓ |
|---|---|---|---|---|
| **S0** | four rigs pass (14-build/S0/) | §4 | | ☐ |
| A0 | loop element → K1 open ≤ 5 ms ×10 each; logic up; weld check fires | 5.1 | | ☐ |
| A1 | R1a 20.7 ± 1.5, R1b ≈ 24 ± 1.5, R2, R2b; P1 ≤ 50, P3 ≤ 30 kPa; PID ± 0.5 | 5.2 | | ☐ |
| A2 | RC1 a/b 0.12–0.25 N (≤ 0.35 N with side load), B_min ≥ 3× friction; RC2 profile + slip loop 10/10; RC3 vent ≤ 100 ms, bleed < 1 s, ≤ 1.04 N at B 100 %; RC6 stroke; RC7 ≥ 8 mm in 200 ms; 0.385 ± 0.04 N at 10 kPa | 5.3 | | ☐ |
| A3 | rosette (§15-4); bow ≤ 0.5; flats ≤ 0.3; rim ≤ 1.3 / 0.8 N; coupling 0 releases 20 min/mode; RC5 lift ≥ 5 mm, ≤ 35°, ≥ 0.3 v_peak; RC6 ≥ 15 mm; tests pass | 5.4 | | ☐ |
| A4 | RC4 trip ≤ 50 ms centre and rim; 0 false trips in 20 min ×3; RC1(b) 0 nuisance | 5.5 | | ☐ |
| A5 | ≤ 30 dBA at 1 m; ≤ 2.8 kg; any orientation; ≤ +20 K | 5.6 | | ☐ |
| HB-mini | 0 loops/knots/wraps/captures; RC1(c) ≤ 0.30 N, ≤ 20 ms | 6.4 | | ☐ |
| **A-S / GO A** | ≥ 6/10 satisfying; "scratch" ≥ 6/8 headings | 5.7 | | ☐ |
| B1 | pad ≤ 90; moving group ≤ 125; helmet ≤ 320 g | 7.1 | | ☐ |
| B2 | total ≤ 12 N; one nail ≤ 0.92 N; bottomed ≤ 1.04 N; coupling 2.0 ± 0.3 N | 7.2 | | ☐ |
| B3 | 3.1 N tension, 3.1 N compression, 3.0 N lateral; mount 6 ± 2 N; tape test | 7.3 | | ☐ |
| B4 | ×10 / ×10 / ×10 / ×5: ≥ 25 mm in ≤ 150 ms; no nail in contact | 7.4 | | ☐ |
| B5 | full hair bench §6: 0 wraps/captures/knots; shed ≤ 2×; RC1 c/d; T_dwell set; H-6.8 ≥ 28 | 7.5 | | ☐ |
| B6 | PHC-A + PHC-B signed; glasses; e-stop; first session ≤ 5 min | 7.6 | | ☐ |
| **B-S / GO B** | ≥ 7/10; machine ≤ 3/10; zero pulls; nails intact every session | 7.7 | | ☐ |
| C1 | cradle under shelf; bun ≥ 60 mm; marks gone ≤ 10 min; stops set | 8.1 | | ☐ |
| C2 | helmet ≤ 320 g | 8.2 | | ☐ |
| C3 | lean ≤ 2/10; slip ≤ 3° | 8.3 | | ☐ |
| C4 | ear ≥ 25 mm; hairline guard; with ±15 mm displacement | 8.4 | | ☐ |
| C5 | tragus within 3 dB of room (pins up); earplug A/B ≤ 7/10 | 8.5 | | ☐ |
| C6 | head share ≤ 15 g; yaw ≤ 0.02 N·m; clip 3 ± 1 N; lanyard first; stand-up ×5 | 8.6 | | ☐ |
| C7 | 10 eyes-closed doffs ≤ 2.5 s; lip ≤ 20 N | 8.7 | | ☐ |
| C8 | whole-system wig: B5 lines again | 8.8 | | ☐ |
| **C-S / GO C** | hat moves ≤ 2/10; having to move it ≤ 3/10 | 8.9 | | ☐ |
| D1–D4 | four 20-min evenings with the armrest switch | 9 | | ☐ |
| D5 | blind matrix decided block by block | 10 | | ☐ |
| **GO D** | ≥ 7/10; machine ≤ 3/10; again tomorrow; 0 tuft pulls over 5 sessions | 9 | | ☐ |

**Count:** 20 build gates (A0–A5, B1–B6, C1–C8) + 3 sensation points (A-S, B-S, C-S) + GO D = **24 decision gates**, plus HB-mini (added) and the D5 blocks; S0's 4 are in 14-build/S0/.
