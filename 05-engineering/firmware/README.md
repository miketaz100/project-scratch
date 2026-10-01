# SP1 firmware — `sp1_scratch/sp1_scratch.ino`

Elbow-servo firmware for PROJECT SCRATCH SP1: OpenRB-150 + DYNAMIXEL XL330-M288-T (ID 1), current-based position mode, HUMAN/PERIODIC pattern engine, serial experiment interface. Specification and safety rationale: `../electronics-firmware.md`. **The hardware rail (fuse → NC e-stop → hold-to-run → servo VIN + magnet) is the safety barrier; this firmware is the secondary layer.**

## Versions
| Item | Version | Source |
|---|---|---|
| Arduino IDE | 2.x | <https://www.arduino.cc/en/software> |
| OpenRB-150 board package | latest (1.0.x) via Boards Manager URL `https://raw.githubusercontent.com/ROBOTIS-GIT/OpenRB-150/master/package_openrb_index.json` | <https://github.com/ROBOTIS-GIT/OpenRB-150> |
| Dynamixel2Arduino library | 0.7.x (Library Manager → "Dynamixel2Arduino" by ROBOTIS) | <https://github.com/ROBOTIS-GIT/Dynamixel2Arduino> |
| XL330-M288-T firmware | any V42+ (velocity-based profile; protocol 2.0) | <https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/> |
| sketch | `SP1-fw-0.2` (boot banner) | this folder |

Compile target: board **"OpenRB-150"** (defines `ARDUINO_OpenRB`, `__SAMD21G18A__`). The sketch was syntax-checked with clang++ against stubs of the Arduino core and Dynamixel2Arduino API (see "Assumptions to confirm" below); it has **not** yet been compiled by the real toolchain on this machine (no arduino-cli installed) — the first upload is bring-up step B0.

## Board setup (Arduino IDE)
1. File → Preferences → *Additional boards manager URLs*: add the OpenRB-150 URL above.
2. Tools → Board → Boards Manager → search "OpenRB" → install **OpenRB-150**.
3. Tools → Manage Libraries → search "Dynamixel2Arduino" → install.
4. Put the OpenRB-150 **power jumper on `VIN(DXL)`** (never `USB(5V)` — that would feed the servo from the laptop, bypassing the safety loop).
5. Tools → Board → OpenRB-150; Tools → Port → the OpenRB-150 USB port.

## Upload
1. Rail **off** (button released or e-stop in). USB-C to the laptop.
2. Open `sp1_scratch/sp1_scratch.ino`, Sketch → Upload. If the port disappears, double-press the board's reset button (bootloader mode) and upload again.
3. Serial Monitor at **115200**, line ending **Newline**. Expect the banner, the limits table, a `C,` settings line and `H,` telemetry at 1 Hz, then `INIT: waiting for actuator rail`.
4. Hold the button: the servo is found (a factory servo at 57600 is migrated to 1 Mbps automatically), configured, and parks at +25°; after 1 s it starts stroking (the hold-to-run press is the start action). `stop` ends a run at +25° with torque off; `run` re-arms.

First-time only: with the hand hanging freely, `stop`, then `zero` (writes the servo's Homing Offset). Then the bench tests B1–B13 in `../electronics-firmware.md` §6 before any human use.

## Serial commands (newline-terminated)
```
help | status | limits
run | stop | reset              run latch on / finish lifted + torque off / leave FAULT
zero                           zero calibration, hand hanging, rail on, not running
goto <deg> | gotoraw <deg>     LIFTED_IDLE only; limit tests (gotoraw beyond ±28 must be REFUSED)
hang                           stop the loop → MCU watchdog reset ≈ 1 s → servo limp
mode human|periodic|auto       override the toggle
spd <0-100>|auto               override the SPEED pot      (0/50/100 = S1/S2/S3)
var <0-100>|auto               override the VARIATION pot  (0/50/100 = V0/V50/V100)
amp <min> <max>                HUMAN amplitude band, deg (5..25)
speed <min> <max>              HUMAN peak tip speed band, mm/s (20..360), × SPEED
jitter <%> | asym <%> | dwell <ms> | slow <p>
pause <p> | pausen <min> <max> | pausems <min> <max> | episode <min> <max>
periodic <deg> <mm/s>          PERIODIC amplitude and speed (× SPEED)
cur <mA>                       goal current 100..450 (servo Current Limit ceiling)
seed <n>                       RNG seed (same seed + same settings code = same strokes)
log on|off                     per-stroke lines
bset <1-8> per|hum|auto <spd%|-1> <var%|-1>    define a BLIND slot
blind <n> | next | reveal | unblind            shuffled hidden trials over slots 1..n
```

## Log format
- `H,t,state,mode,spd%,var%,strokes,pos_deg,mA,fault,code` — 1 Hz, always.
- `S,t,n,amp_deg,vel_lsb,tip_mm_s,dwell_ms,cur_peak_mA,cur_mean_mA,pos_end_deg,code` — per stroke.
- `C,t,code,…full settings…,seed` — at boot and whenever the settings code changes.
- `E,` episode · `Z,` pause · `T,` stroke timeout · `STATE …` · `R,` reveal.
- Settings code: `MODE-S<spd%>-V<var%>-C<mA>#<hash>`; `BLD` while blind.

Save a session with the IDE's serial monitor (or `screen -L /dev/cu.usbmodem* 115200`); the `C,` lines make the file self-describing.

## Changing the pattern
- **Live, per session:** the serial commands above (they are what the experiment matrix uses; record the code from the `C,` line on the session log).
- **Defaults:** edit `Pattern P = { … }` in the CONFIG BLOCK (order: amp min/max, speed min/max, jitter amp, jitter speed, asym, dwell max, pause every min/max, pause prob, pause ms min/max, episode s min/max, slow-stroke prob, periodic amp, periodic speed).
- **Shape:** `newEpisode()` (how bands are re-drawn), `beginStroke()` (how one stroke is sampled), `endStroke()` (pauses). Every goal goes through `setGoal()`, which clamps position to ±25°, velocity to 180 LSB and acceleration to 20–60 LSB — keep it that way; it is the single clamp point the safety document relies on.
- **Limits** (`LIMIT_*`, `CURRENT_LIMIT_MA`, `goalCurrentMa`, `PROFILE_*`, `STALL_*`, `BUS_WATCHDOG_LSB`) are in the CONFIG BLOCK and printed at boot; change them only with a matching edit to `../electronics-firmware.md` §4 and a re-run of bench tests B6–B10.
- Stage 3 yaw: `DXL_ID_YAW` is reserved; add a second `setGoal`-style clamp for ID 2 before driving it.

## Assumptions to confirm at first compile / bring-up
1. `Dynamixel2Arduino::readControlTableItem()` sets `getLastLibErrCode()` to 0 on success (used by `rd()`); if reads never flag errors, the comm-loss test B10(b) will show it — then switch `rd()` to check the returned value against a sentinel.
2. `getModelNumber(id)` returns 1200 for the XL330-M288-T.
3. The SAMD21 WDT block is the Adafruit SleepyDog sequence; if the core already configures GCLK2, remove the two `GCLK->` lines.
4. Sign convention: `goto 25` must lift the nails toward the park side; if the horn is mirrored, negate `TICKS_PER_DEG` use in `degToTicks()`/`presentDeg()`.
