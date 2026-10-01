/*
 * sp1_scratch.ino — PROJECT SCRATCH SP1, elbow-servo firmware
 * Board: ROBOTIS OpenRB-150 (SAMD21G18A). Library: Dynamixel2Arduino (>= 0.7).
 * Servo: DYNAMIXEL XL330-M288-T, ID 1 (elbow), protocol 2.0, current-based position mode (mode 5).
 *
 * SAFETY STANCE (DESIGN-FREEZE §1.10, safety-requirements §4): the HARDWARE loop
 * (5 V adapter -> fuse -> NC e-stop -> NO hold-to-run -> servo VIN + holding magnet) is the primary
 * barrier. This file is the SECONDARY layer: it may READ the rail; it never implements the stop.
 * Nothing here is credited alone for any S>=3 hazard (red line 13).
 *
 * States: INIT -> LIFTED_IDLE -> RUNNING ; rail loss -> PAUSED -> INIT ; any -> FAULT (serial 'reset').
 * Secondary barriers: servo EEPROM position limits +/-28 deg, firmware clamp +/-25 deg, profile-velocity
 * cap, goal-current cap (~1.2 N at the tip), servo Bus Watchdog 100 ms, MCU watchdog 1 s (reset ->
 * DXL power FET defaults OFF), stall trip 250 ms, comm-loss trip, hardware-error trip, 20-min session
 * limit, torque-off + bus FET off on every fault.
 * Test-protocol hooks (test-protocols.md §Q.3): 1 Hz 'H,' telemetry, 'goto', 'gotoraw', 'hang', BLIND.
 */
#include <Dynamixel2Arduino.h>

// ============================== CONFIG BLOCK (all tunables) ==============================
#define FW_VERSION        "SP1-fw-0.2"
#define DXL_SERIAL        Serial1          // OpenRB-150 DYNAMIXEL TTL port (auto direction)
#define DEBUG_SERIAL      Serial           // USB-C CDC
const int      DXL_DIR_PIN         = -1;
const uint8_t  DXL_ID_ELBOW        = 1;
const uint8_t  DXL_ID_YAW          = 2;         // reserved, Stage 3 (not driven here)
const uint32_t DXL_BAUD            = 1000000;   // bus speed in service
const uint32_t DXL_FACTORY_BAUD    = 57600;     // XL330 default; a fresh servo is migrated automatically
const float    DXL_PROTOCOL        = 2.0;
const uint16_t XL330_M288_MODEL    = 1200;

// --- pins (OpenRB-150 variant.h: A0=15..A6=21, LED_BUILTIN=32, BDPIN_DXL_PWR_EN=31) ---
const int PIN_POT_SPEED     = A0;   // 10 k pot: ends 3V3/GND, wiper A0
const int PIN_POT_VARIATION = A1;   // 10 k pot
const int PIN_RAIL_SENSE    = A2;   // actuator rail through 10k/10k divider (5 V -> 2.5 V). READ ONLY.
const int PIN_MODE_TOGGLE   = 4;    // SPST toggle to GND, INPUT_PULLUP: open = HUMAN, closed = PERIODIC
const int PIN_STATUS_LED    = 5;    // external LED + 330 R (LED_BUILTIN mirrors it)
const int PIN_HX711_DT      = 2;    // reserved header, Stage 3 load cell
const int PIN_HX711_SCK     = 3;    // reserved header, Stage 3 load cell

// --- geometry & position limits (DESIGN-FREEZE §1.5, §1.10) ---
const float    ARM_LEN_MM        = 84.0f;   // elbow axis to nail tip at the down-stop
const float    LIMIT_ABS_DEG     = 28.0f;   // servo Min/Max Position Limit (EEPROM) — the servo refuses goals beyond
const float    LIMIT_NOM_DEG     = 25.0f;   // firmware clamp on every pattern goal
const float    PARK_DEG          = +25.0f;  // lifted position: start, stop, pause happen here
const int32_t  ZERO_TICKS        = 2048;    // calibrated zero = hand hanging vertical
const float    TICKS_PER_DEG     = 4096.0f / 360.0f;
const float    ZERO_SANITY_DEG   = 40.0f;   // free-hanging hand must be within this of zero at INIT

// --- current (torque) limits — derivation in electronics-firmware.md §4 ---
const uint16_t CURRENT_LIMIT_MA  = 450;     // EEPROM(38) ceiling: 450 mA x 0.354 Nm/A / 0.084 m = 1.9 N tangential
uint16_t       goalCurrentMa     = 300;     // RAM(102) working cap: 300 mA -> 0.106 Nm -> 1.26 N at 84 mm (bench-calibrated)
const uint16_t GOAL_CURRENT_MIN  = 100;
const float    STALL_FRACTION    = 0.90f;   // |present current| >= 0.9 x goal, no motion ...
const uint32_t STALL_MS          = 250;     // ... for 250 ms -> FAULT (safety §4.6: < 300 ms)

// --- velocity / acceleration (Profile Velocity 0.229 rpm/LSB; Profile Accel 214.577 rev/min^2/LSB) ---
const float    TIP_SPEED_CAP_MM_S  = 360.0f;  // < 0.4 m/s cap (safety §2.4)
const uint16_t PROFILE_VEL_MAX_LSB = 180;     // 41.2 rpm -> 0.36 m/s at 84 mm; absolute cap on reg 112
const uint16_t PROFILE_ACC_MIN_LSB = 20;      // 429 deg/s^2  (0.63 m/s^2 at the tip)
const uint16_t PROFILE_ACC_MAX_LSB = 60;      // 1287 deg/s^2 (1.9 m/s^2 at the tip)

// --- servo housekeeping registers ---
const uint8_t  BUS_WATCHDOG_LSB   = 5;    // x 20 ms = 100 ms without a packet -> servo stops
const uint8_t  RETURN_DELAY_LSB   = 0;    // 0 us
const uint8_t  STATUS_RETURN_LVL  = 2;    // every write acknowledged, so every write is verified
const uint8_t  SHUTDOWN_MASK      = 0x34; // overload | electrical shock | overheating (factory default)

// --- loop / timing ---
const uint32_t TICK_MS            = 20;       // 50 Hz loop; each tick reads the servo (feeds Bus Watchdog)
const uint32_t LIFTED_HOLD_MS     = 1000;     // hold at PARK before the first stroke (freeze §2)
const uint8_t  RAMP_STROKES       = 3;        // first strokes at 50/70/90 % speed
const uint32_t SESSION_MAX_MS     = 20UL * 60UL * 1000UL;
const uint8_t  COMM_FAIL_LIMIT    = 5;        // consecutive failed reads -> FAULT (100 ms)
const uint8_t  TIMEOUT_LIMIT      = 3;        // consecutive strokes that never arrive -> FAULT
const bool     AUTO_RUN_ON_RAIL   = true;     // the hold-to-run press is the start action
const bool     MCU_WATCHDOG       = true;     // SAMD21 WDT, 1 s
const uint32_t SERIAL_BAUD        = 115200;
const uint32_t TELEMETRY_MS       = 1000;     // §Q.3: 1 Hz echo

// --- PATTERN SPEC v1 (DESIGN-FREEZE §2); all fields settable over serial ---
struct Pattern {
  float amp_min_deg, amp_max_deg;     // HUMAN half-amplitude band (12..25 deg)
  float spd_min_mm_s, spd_max_mm_s;   // HUMAN peak tip speed band (50..150 mm/s), x SPEED pot
  float jitter_amp, jitter_spd, asym; // per-stroke jitter (+/-25 %), direction asymmetry; all x VARIATION
  uint16_t dwell_max_ms;              // random end-dwell 0..300 ms, x VARIATION
  uint8_t  pause_every_min, pause_every_max;  // pause every 4..10 strokes
  float    pause_prob;                // probability a due pause happens
  uint16_t pause_min_ms, pause_max_ms;        // 500..3000 ms lifted
  uint16_t episode_min_s, episode_max_s;      // 5..20 s between band re-draws
  float    slow_stroke_prob;          // episode may start with one slow long stroke
  float    periodic_amp_deg, periodic_spd_mm_s; // PERIODIC: fixed 18 deg, 100 mm/s x SPEED pot
};
Pattern P = { 12.0f, 25.0f, 50.0f, 150.0f, 0.25f, 0.25f, 0.15f, 300, 4, 10, 1.0f, 500, 3000, 5, 20, 0.20f, 18.0f, 100.0f };
// ============================ END CONFIG BLOCK ============================================

Dynamixel2Arduino dxl(DXL_SERIAL, DXL_DIR_PIN);
using namespace ControlTableItem;

enum State { ST_INIT, ST_LIFTED_IDLE, ST_RUNNING, ST_PAUSED, ST_FAULT };
enum Phase { PH_MOVING, PH_DWELL, PH_PAUSE };
enum Fault { F_NONE, F_COMM, F_OVERCURRENT, F_HW_ERROR, F_TIMEOUT, F_ZERO, F_CONFIG };
const char* STATE_NAMES[] = { "INIT", "LIFTED_IDLE", "RUNNING", "PAUSED", "FAULT" };
const char* FAULT_NAMES[] = { "none", "comm_loss", "over_current", "hw_error", "motion_timeout", "zero_out_of_range", "config" };

State    state = ST_INIT;  Fault fault = F_NONE;  Phase phase = PH_MOVING;
bool     runLatch = AUTO_RUN_ON_RAIL, logOn = true, idleTorque = true;
uint32_t stateEnteredMs = 0, sessionStartMs = 0, lastTickMs = 0, lastTelemetryMs = 0;

// live inputs and overrides
float    potSpeed = 0.5f, potVar = 0.5f;          // 0..1 (EMA filtered)
int      spdOverridePct = -1, varOverridePct = -1, modeOverride = -1;   // -1 = use pot / toggle
bool     railOn = false, modeHuman = true;

// BLIND presets (§Q.3): slot = {mode 0/1, spd %, var %}; -1 = leave to pot/toggle
struct Slot { int8_t mode; int16_t spd, var; };
Slot     blindSlot[8]; uint8_t blindN = 0, blindOrder[8], blindIdx = 0; bool blindActive = false;

// servo telemetry
int32_t  presentTicks = ZERO_TICKS; int16_t presentMa = 0; uint8_t commFails = 0, hwError = 0;
float    presentDeg() { return (presentTicks - ZERO_TICKS) / TICKS_PER_DEG; }

// stroke bookkeeping
uint32_t strokeN = 0, strokeStartMs = 0, strokeTimeoutMs = 0, phaseEndMs = 0, stallStartMs = 0, episodeEndMs = 0;
uint8_t  strokesToPause = 6, timeoutsInRow = 0;  int8_t dir = -1;
float    goalDeg = PARK_DEG, epAmpMin, epAmpMax, epSpdMin, epSpdMax;  bool slowStrokePending = false;
int16_t  curPeakMa = 0; int32_t curSumMa = 0; uint16_t curSamples = 0;
float    lastAmp = 0, lastTip = 0; uint16_t lastVelLsb = 0, lastDwell = 0;
uint32_t rngSeed = 0x5EEDC0DEu, rngState = 0x5EEDC0DEu; uint16_t lastCode = 0;

// ------------------------------- deterministic RNG (xorshift32) -------------------------
uint32_t rngNext() { uint32_t x = rngState; x ^= x << 13; x ^= x >> 17; x ^= x << 5; return rngState = x; }
float    rndf() { return (rngNext() >> 8) * (1.0f / 16777216.0f); }
float    rndRange(float a, float b) { return a + (b - a) * rndf(); }
uint32_t rndInt(uint32_t a, uint32_t b) { return a + (rngNext() % (b - a + 1)); }
float    clampf(float v, float lo, float hi) { return v < lo ? lo : (v > hi ? hi : v); }

// ------------------------------- MCU hardware watchdog ----------------------------------
#if defined(__SAMD21G18A__) || defined(__SAMD21__)
void wdtInit() {   // per Adafruit_SleepyDog WatchdogSAMD (SAMD21): GCLK2 = OSCULP32K / 32 = 1024 Hz
  GCLK->GENDIV.reg = GCLK_GENDIV_ID(2) | GCLK_GENDIV_DIV(4);
  GCLK->GENCTRL.reg = GCLK_GENCTRL_ID(2) | GCLK_GENCTRL_GENEN | GCLK_GENCTRL_SRC_OSCULP32K | GCLK_GENCTRL_DIVSEL;
  while (GCLK->STATUS.bit.SYNCBUSY);
  GCLK->CLKCTRL.reg = GCLK_CLKCTRL_ID_WDT | GCLK_CLKCTRL_CLKEN | GCLK_CLKCTRL_GEN_GCLK2;
  WDT->CTRL.reg = 0; while (WDT->STATUS.bit.SYNCBUSY);
  WDT->INTENCLR.bit.EW = 1;
  WDT->CONFIG.bit.PER = 0x7;          // 1024 cycles @ 1024 Hz = 1 s
  WDT->CTRL.bit.WEN = 0;
  WDT->CTRL.bit.ENABLE = 1; while (WDT->STATUS.bit.SYNCBUSY);
}
void wdtKick() { WDT->CLEAR.reg = WDT_CLEAR_CLEAR_KEY; while (WDT->STATUS.bit.SYNCBUSY); }
#else
#warning "No SAMD21 watchdog on this target: MCU watchdog disabled"
void wdtInit() {}  void wdtKick() {}
#endif

// ------------------------------- servo helpers ------------------------------------------
bool     dxlOk() { return dxl.getLastLibErrCode() == 0; }     // 0 == DXL_LIB_OK
bool     wr(uint8_t item, int32_t v) { return dxl.writeControlTableItem(item, DXL_ID_ELBOW, v) && dxl.getLastStatusPacketError() == 0; }  // false on timeout OR a servo-side error (range, access)
int32_t  rd(uint8_t item, bool* ok) { int32_t v = dxl.readControlTableItem(item, DXL_ID_ELBOW); *ok = dxlOk() && dxl.getLastStatusPacketError() == 0; return v; }
int32_t  degToTicks(float d) { return ZERO_TICKS + (int32_t)lroundf(d * TICKS_PER_DEG); }
uint16_t tipSpeedToVelLsb(float mm_s) {          // v = w L ; LSB = 0.229 rpm
  float rpm = (clampf(mm_s, 10.0f, TIP_SPEED_CAP_MM_S) / ARM_LEN_MM) * 60.0f / (2.0f * 3.14159265f);
  uint16_t lsb = (uint16_t)lroundf(rpm / 0.229f);
  return lsb > PROFILE_VEL_MAX_LSB ? PROFILE_VEL_MAX_LSB : (lsb < 5 ? 5 : lsb);
}
void dxlPowerOff() { pinMode(BDPIN_DXL_PWR_EN, OUTPUT); digitalWrite(BDPIN_DXL_PWR_EN, LOW); }  // firmware-side bus cut

bool setGoal(float deg, uint16_t velLsb, uint16_t accLsb, float clampDeg = LIMIT_NOM_DEG) {
  goalDeg = clampf(deg, -clampDeg, clampDeg);
  if (velLsb > PROFILE_VEL_MAX_LSB) velLsb = PROFILE_VEL_MAX_LSB;
  accLsb = (uint16_t)clampf(accLsb, PROFILE_ACC_MIN_LSB, PROFILE_ACC_MAX_LSB);
  bool ok = wr(PROFILE_ACCELERATION, accLsb); ok &= wr(PROFILE_VELOCITY, velLsb); ok &= wr(GOAL_POSITION, degToTicks(goalDeg));
  lastVelLsb = velLsb; return ok;
}

// Open the bus (migrating a factory-57600 servo to DXL_BAUD), write the EEPROM limits table if it
// differs, then the RAM working registers, torque on at PARK, arm the Bus Watchdog last.
bool servoConfigure() {
  dxl.begin(DXL_BAUD); dxl.setPortProtocolVersion(DXL_PROTOCOL);   // begin() also raises BDPIN_DXL_PWR_EN on OpenRB-150
  if (!dxl.ping(DXL_ID_ELBOW)) {
    dxl.begin(DXL_FACTORY_BAUD); dxl.setPortProtocolVersion(DXL_PROTOCOL);
    if (!dxl.ping(DXL_ID_ELBOW)) { DEBUG_SERIAL.println("ERR servo ID 1 not found at 1M or 57600"); return false; }
    DEBUG_SERIAL.println("servo found at 57600, migrating to 1 Mbps");
    dxl.torqueOff(DXL_ID_ELBOW);
    if (!dxl.setBaudrate(DXL_ID_ELBOW, DXL_BAUD)) return false;
    delay(100); dxl.begin(DXL_BAUD); dxl.setPortProtocolVersion(DXL_PROTOCOL);
    if (!dxl.ping(DXL_ID_ELBOW)) return false;
  }
  bool ok; uint16_t model = dxl.getModelNumber(DXL_ID_ELBOW);
  if (model != XL330_M288_MODEL) { DEBUG_SERIAL.print("ERR model "); DEBUG_SERIAL.println(model); return false; }
  dxl.torqueOff(DXL_ID_ELBOW);                   // EEPROM writable only with torque off
  struct { uint8_t item; int32_t val; } eeprom[] = {
    { OPERATING_MODE,      OP_CURRENT_BASED_POSITION },
    { CURRENT_LIMIT,       CURRENT_LIMIT_MA },
    { MIN_POSITION_LIMIT,  degToTicks(-LIMIT_ABS_DEG) },
    { MAX_POSITION_LIMIT,  degToTicks(+LIMIT_ABS_DEG) },
    { RETURN_DELAY_TIME,   RETURN_DELAY_LSB },
    { STATUS_RETURN_LEVEL, STATUS_RETURN_LVL },
    { SHUTDOWN,            SHUTDOWN_MASK },
  };
  for (auto& e : eeprom) {                       // write only when different (EEPROM endurance)
    int32_t cur = rd(e.item, &ok); if (!ok) return false;
    if (cur != e.val) { if (!wr(e.item, e.val)) return false; delay(20); }
  }
  if (!wr(BUS_WATCHDOG, 0)) return false;        // clear a watchdog error left from the last session
  if (!wr(GOAL_CURRENT, goalCurrentMa)) return false;
  presentTicks = rd(PRESENT_POSITION, &ok); if (!ok) return false;
  if (fabsf(presentDeg()) > ZERO_SANITY_DEG) {   // the hand hangs free here: it must be near zero
    DEBUG_SERIAL.print("ERR present "); DEBUG_SERIAL.print(presentDeg()); DEBUG_SERIAL.println(" deg: run 'zero' with the hand hanging");
    fault = F_ZERO; return false;
  }
  if (!setGoal(PARK_DEG, tipSpeedToVelLsb(60.0f), PROFILE_ACC_MIN_LSB)) return false;
  if (!dxl.torqueOn(DXL_ID_ELBOW)) return false;
  return wr(BUS_WATCHDOG, BUS_WATCHDOG_LSB);     // from here on we must talk every < 100 ms
}

// Zero calibration: hand hanging vertical, torque off. XL330: Present = Actual + Homing Offset (reg 20).
bool calibrateZero() {
  bool ok; dxl.torqueOff(DXL_ID_ELBOW);
  if (!wr(HOMING_OFFSET, 0)) return false; delay(20);
  int32_t raw = rd(PRESENT_POSITION, &ok); if (!ok) return false;
  int32_t offset = ZERO_TICKS - raw;
  if (!wr(HOMING_OFFSET, offset)) return false; delay(20);
  presentTicks = rd(PRESENT_POSITION, &ok);
  DEBUG_SERIAL.print("zero: raw "); DEBUG_SERIAL.print(raw); DEBUG_SERIAL.print(" offset "); DEBUG_SERIAL.print(offset);
  DEBUG_SERIAL.print(" now "); DEBUG_SERIAL.print(presentDeg()); DEBUG_SERIAL.println(" deg (expect 0.0)");
  return ok && fabsf(presentDeg()) < 0.5f;
}

// ------------------------------- state helpers ------------------------------------------
void enterState(State s) {
  state = s; stateEnteredMs = millis();
  DEBUG_SERIAL.print("STATE "); DEBUG_SERIAL.print(STATE_NAMES[s]);
  if (s == ST_FAULT) { DEBUG_SERIAL.print(" fault="); DEBUG_SERIAL.print(FAULT_NAMES[fault]); }
  DEBUG_SERIAL.println();
}
void goFault(Fault f) { fault = f; dxl.torqueOff(DXL_ID_ELBOW); dxlPowerOff(); enterState(ST_FAULT); }  // torque off (best effort), bus FET off; the rail does the lift
void stopToPark() { setGoal(PARK_DEG, tipSpeedToVelLsb(80.0f), PROFILE_ACC_MIN_LSB); idleTorque = false; enterState(ST_LIFTED_IDLE); }  // finish lifted, then torque off

// ------------------------------- settings code (reproducibility) ------------------------
int   speedPct()  { return spdOverridePct >= 0 ? spdOverridePct : (int)lroundf(potSpeed * 100); }
int   varPct()    { return varOverridePct >= 0 ? varOverridePct : (int)lroundf(potVar * 100); }
float variation() { return varPct() / 100.0f; }                 // 0..1
float speedScale(){ return 0.5f + speedPct() / 100.0f; }         // pot 0/50/100 % -> 0.5/1.0/1.5 x (S1/S2/S3); active in PERIODIC too
bool  humanMode() { return modeOverride >= 0 ? modeOverride == 1 : modeHuman; }
const char* modeName() { return blindActive ? "BLD" : (humanMode() ? "HUM" : "PER"); }

uint16_t settingsHash() {   // FNV-1a over the pattern struct + current + seed + visible levels
  uint32_t h = 2166136261u; const uint8_t* p = (const uint8_t*)&P;
  for (size_t i = 0; i < sizeof(P); i++) { h ^= p[i]; h *= 16777619u; }
  uint32_t extra[4] = { goalCurrentMa, rngSeed, (uint32_t)speedPct(), (uint32_t)varPct() };
  p = (const uint8_t*)extra; for (size_t i = 0; i < sizeof(extra); i++) { h ^= p[i]; h *= 16777619u; }
  h ^= blindActive ? 0xB11D : (humanMode() ? 1 : 0);
  return (uint16_t)(h ^ (h >> 16));
}
void printCode() {  // "HUM-S50-V100-C300#1a2b"; in BLIND the mode and hidden levels are masked
  DEBUG_SERIAL.print(modeName()); DEBUG_SERIAL.print("-S"); DEBUG_SERIAL.print(blindActive ? 0 : speedPct());
  DEBUG_SERIAL.print("-V"); DEBUG_SERIAL.print(blindActive ? 0 : varPct()); DEBUG_SERIAL.print("-C"); DEBUG_SERIAL.print(goalCurrentMa);
  DEBUG_SERIAL.print('#'); DEBUG_SERIAL.print(settingsHash(), HEX);
}
void printSettingsLine() {   // C,t,code,amp,speed,jitter,asym,dwell,pause,episode,slow,periodic,cur,seed  (emitted whenever the code changes)
  DEBUG_SERIAL.print("C,"); DEBUG_SERIAL.print(millis()); DEBUG_SERIAL.print(','); printCode();
  DEBUG_SERIAL.print(",amp "); DEBUG_SERIAL.print(P.amp_min_deg, 0); DEBUG_SERIAL.print('-'); DEBUG_SERIAL.print(P.amp_max_deg, 0);
  DEBUG_SERIAL.print(",spd "); DEBUG_SERIAL.print(P.spd_min_mm_s, 0); DEBUG_SERIAL.print('-'); DEBUG_SERIAL.print(P.spd_max_mm_s, 0);
  DEBUG_SERIAL.print(",jit "); DEBUG_SERIAL.print(P.jitter_amp * 100, 0); DEBUG_SERIAL.print(",asym "); DEBUG_SERIAL.print(P.asym * 100, 0);
  DEBUG_SERIAL.print(",dwell "); DEBUG_SERIAL.print(P.dwell_max_ms); DEBUG_SERIAL.print(",pause "); DEBUG_SERIAL.print(P.pause_prob, 2);
  DEBUG_SERIAL.print('/'); DEBUG_SERIAL.print(P.pause_every_min); DEBUG_SERIAL.print('-'); DEBUG_SERIAL.print(P.pause_every_max);
  DEBUG_SERIAL.print('/'); DEBUG_SERIAL.print(P.pause_min_ms); DEBUG_SERIAL.print('-'); DEBUG_SERIAL.print(P.pause_max_ms);
  DEBUG_SERIAL.print(",ep "); DEBUG_SERIAL.print(P.episode_min_s); DEBUG_SERIAL.print('-'); DEBUG_SERIAL.print(P.episode_max_s);
  DEBUG_SERIAL.print(",slow "); DEBUG_SERIAL.print(P.slow_stroke_prob, 2); DEBUG_SERIAL.print(",per "); DEBUG_SERIAL.print(P.periodic_amp_deg, 0);
  DEBUG_SERIAL.print('/'); DEBUG_SERIAL.print(P.periodic_spd_mm_s, 0); DEBUG_SERIAL.print(",seed "); DEBUG_SERIAL.println(rngSeed);
}

// ------------------------------- pattern engine (freeze §2) -----------------------------
void newEpisode() {   // every 5-20 s: new amplitude/speed sub-bands; sometimes one slow long stroke first
  float v = variation();
  float aw = rndRange(0.3f, 1.0f) * (P.amp_max_deg - P.amp_min_deg);
  epAmpMin = P.amp_min_deg + rndf() * (P.amp_max_deg - P.amp_min_deg - aw); epAmpMax = epAmpMin + aw;
  float sw = rndRange(0.3f, 1.0f) * (P.spd_max_mm_s - P.spd_min_mm_s);
  epSpdMin = P.spd_min_mm_s + rndf() * (P.spd_max_mm_s - P.spd_min_mm_s - sw); epSpdMax = epSpdMin + sw;
  if (v < 0.05f) { epAmpMin = epAmpMax = 0.5f * (P.amp_min_deg + P.amp_max_deg); epSpdMin = epSpdMax = 0.5f * (P.spd_min_mm_s + P.spd_max_mm_s); }
  slowStrokePending = rndf() < P.slow_stroke_prob * v;
  episodeEndMs = millis() + 1000UL * rndInt(P.episode_min_s, P.episode_max_s);
  if (logOn) { DEBUG_SERIAL.print("E,"); DEBUG_SERIAL.print(millis()); DEBUG_SERIAL.print(','); DEBUG_SERIAL.print(epAmpMin, 1); DEBUG_SERIAL.print(',');
    DEBUG_SERIAL.print(epAmpMax, 1); DEBUG_SERIAL.print(','); DEBUG_SERIAL.print(epSpdMin, 0); DEBUG_SERIAL.print(','); DEBUG_SERIAL.print(epSpdMax, 0); DEBUG_SERIAL.println(slowStrokePending ? ",slow" : ""); }
}

void beginStroke() {
  float amp, tip; uint16_t acc, dwell = 0;
  if (!humanMode()) { amp = P.periodic_amp_deg; tip = P.periodic_spd_mm_s * speedScale(); acc = 40; }   // PERIODIC: fixed, no pauses
  else {
    float v = variation();
    if (millis() > episodeEndMs) newEpisode();
    if (slowStrokePending) { amp = P.amp_max_deg; tip = 40.0f * speedScale(); acc = PROFILE_ACC_MIN_LSB; slowStrokePending = false; }
    else {
      amp = rndRange(epAmpMin, epAmpMax) * (1.0f + rndRange(-P.jitter_amp, P.jitter_amp) * v);
      tip = rndRange(epSpdMin, epSpdMax) * (1.0f + rndRange(-P.jitter_spd, P.jitter_spd) * v) * speedScale();
      tip *= 1.0f + (dir > 0 ? 1.0f : -1.0f) * P.asym * v * rndf();          // randomized direction asymmetry
      acc = (uint16_t)rndInt(PROFILE_ACC_MIN_LSB, PROFILE_ACC_MAX_LSB);
    }
    dwell = (uint16_t)(rndf() * P.dwell_max_ms * v);
  }
  if (strokeN < RAMP_STROKES) tip *= 0.5f + 0.2f * strokeN;                   // startup ramp 50/70/90 %
  amp = clampf(amp, 5.0f, LIMIT_NOM_DEG); tip = clampf(tip, 20.0f, TIP_SPEED_CAP_MM_S);
  uint16_t vel = tipSpeedToVelLsb(tip);
  float target = dir * amp, dist = fabsf(target - presentDeg()), degPerS = vel * 0.229f * 6.0f;
  strokeStartMs = millis(); strokeTimeoutMs = strokeStartMs + (uint32_t)(2000.0f * dist / degPerS) + 600;
  curPeakMa = 0; curSumMa = 0; curSamples = 0; lastAmp = amp; lastTip = tip; lastDwell = dwell;
  if (!setGoal(target, vel, acc)) { goFault(F_COMM); return; }
  phase = PH_MOVING; dir = -dir;
}

void endStroke() {
  strokeN++;
  uint16_t code = settingsHash(); if (code != lastCode) { lastCode = code; printSettingsLine(); }
  if (logOn) {   // S,t_ms,n,amp_deg,vel_lsb,tip_mm_s,dwell_ms,cur_peak_mA,cur_mean_mA,pos_end_deg,code
    DEBUG_SERIAL.print("S,"); DEBUG_SERIAL.print(millis()); DEBUG_SERIAL.print(','); DEBUG_SERIAL.print(strokeN); DEBUG_SERIAL.print(',');
    DEBUG_SERIAL.print(lastAmp, 1); DEBUG_SERIAL.print(','); DEBUG_SERIAL.print(lastVelLsb); DEBUG_SERIAL.print(','); DEBUG_SERIAL.print(lastTip, 0); DEBUG_SERIAL.print(',');
    DEBUG_SERIAL.print(lastDwell); DEBUG_SERIAL.print(','); DEBUG_SERIAL.print(curPeakMa); DEBUG_SERIAL.print(',');
    DEBUG_SERIAL.print(curSamples ? curSumMa / curSamples : 0); DEBUG_SERIAL.print(','); DEBUG_SERIAL.print(presentDeg(), 1); DEBUG_SERIAL.print(',');
    printCode(); DEBUG_SERIAL.println();
  }
  if (humanMode() && --strokesToPause == 0) {
    strokesToPause = (uint8_t)rndInt(P.pause_every_min, P.pause_every_max);
    if (rndf() < P.pause_prob) {
      setGoal(PARK_DEG, tipSpeedToVelLsb(80.0f), PROFILE_ACC_MIN_LSB);
      phaseEndMs = millis() + rndInt(P.pause_min_ms, P.pause_max_ms) + 400; phase = PH_PAUSE; dir = -1;
      if (logOn) { DEBUG_SERIAL.print("Z,"); DEBUG_SERIAL.print(millis()); DEBUG_SERIAL.print(','); DEBUG_SERIAL.println(phaseEndMs - millis()); }
      return;
    }
  }
  phaseEndMs = millis() + lastDwell; phase = PH_DWELL;
}

void runningTick() {
  if (millis() - sessionStartMs > SESSION_MAX_MS) { DEBUG_SERIAL.println("session limit 20 min: stopping"); runLatch = false; stopToPark(); return; }
  if (phase == PH_MOVING) {
    if (fabsf(presentDeg() - goalDeg) < 1.5f) { timeoutsInRow = 0; endStroke(); }
    else if (millis() > strokeTimeoutMs) {
      if (++timeoutsInRow >= TIMEOUT_LIMIT) { goFault(F_TIMEOUT); return; }
      if (logOn) DEBUG_SERIAL.println("T,stroke timeout"); endStroke();
    }
  } else if (millis() >= phaseEndMs) beginStroke();      // PH_DWELL / PH_PAUSE
}

// ------------------------------- inputs, telemetry, trips -------------------------------
void readInputs() {
  potSpeed += 0.2f * (analogRead(PIN_POT_SPEED) / 1023.0f - potSpeed);
  potVar   += 0.2f * (analogRead(PIN_POT_VARIATION) / 1023.0f - potVar);
  railOn    = analogRead(PIN_RAIL_SENSE) > 400;         // ~1.3 V threshold on a 3.3 V ADC; rail gives ~2.5 V
  modeHuman = digitalRead(PIN_MODE_TOGGLE) == HIGH;
}
bool pollServo() {   // one position + current read per tick keeps the Bus Watchdog fed
  bool ok; int32_t p = rd(PRESENT_POSITION, &ok); if (!ok) { commFails++; return commFails < COMM_FAIL_LIMIT; }
  presentTicks = p;
  int32_t c = rd(PRESENT_CURRENT, &ok); if (!ok) { commFails++; return commFails < COMM_FAIL_LIMIT; }
  if (c > 32767) c -= 65536; presentMa = (int16_t)c; commFails = 0;
  int16_t a = presentMa < 0 ? -presentMa : presentMa;
  if (a > curPeakMa) curPeakMa = a; curSumMa += a; curSamples++;
  static uint8_t slow = 0; if (++slow >= 10) { slow = 0; int32_t h = rd(HARDWARE_ERROR_STATUS, &ok); if (ok) hwError = (uint8_t)h; }
  return true;
}
void checkTrips() {
  if (hwError) { goFault(F_HW_ERROR); return; }
  int16_t a = presentMa < 0 ? -presentMa : presentMa;
  static float lastDeg = 0; float d = presentDeg();
  bool stalled = a >= STALL_FRACTION * goalCurrentMa && fabsf(d - lastDeg) < 0.3f; lastDeg = d;
  if (!stalled) stallStartMs = 0;
  else if (!stallStartMs) stallStartMs = millis();
  else if (millis() - stallStartMs >= STALL_MS) goFault(F_OVERCURRENT);
}
void telemetry() {   // H,t,state,mode,spd%,var%,strokes,pos_deg,mA,fault,code   (1 Hz, §Q.3)
  if (millis() - lastTelemetryMs < TELEMETRY_MS) return; lastTelemetryMs = millis();
  DEBUG_SERIAL.print("H,"); DEBUG_SERIAL.print(millis()); DEBUG_SERIAL.print(','); DEBUG_SERIAL.print(STATE_NAMES[state]); DEBUG_SERIAL.print(',');
  DEBUG_SERIAL.print(modeName()); DEBUG_SERIAL.print(','); DEBUG_SERIAL.print(blindActive ? -1 : speedPct()); DEBUG_SERIAL.print(',');
  DEBUG_SERIAL.print(blindActive ? -1 : varPct()); DEBUG_SERIAL.print(','); DEBUG_SERIAL.print(strokeN); DEBUG_SERIAL.print(',');
  DEBUG_SERIAL.print(presentDeg(), 1); DEBUG_SERIAL.print(','); DEBUG_SERIAL.print(presentMa); DEBUG_SERIAL.print(',');
  DEBUG_SERIAL.print(FAULT_NAMES[fault]); DEBUG_SERIAL.print(','); printCode(); DEBUG_SERIAL.println();
}
void ledTick() {
  uint32_t t = millis(); bool on = false;
  switch (state) {
    case ST_INIT:        on = (t / 100) % 2; break;     // fast blink
    case ST_LIFTED_IDLE: on = (t / 500) % 2; break;     // slow blink
    case ST_RUNNING:     on = true; break;              // solid
    case ST_PAUSED:      on = (t % 1000) < 100 || ((t % 1000) > 200 && (t % 1000) < 300); break;   // double blink
    case ST_FAULT:       on = (t / 50) % 2; break;      // rapid flash
  }
  digitalWrite(PIN_STATUS_LED, on); digitalWrite(LED_BUILTIN, on);
}

// ------------------------------- serial command interface -------------------------------
void printLimits() {
  DEBUG_SERIAL.println("--- limits table (firmware = secondary layer; hardware rail is primary) ---");
  DEBUG_SERIAL.print("position: servo EEPROM +/-"); DEBUG_SERIAL.print(LIMIT_ABS_DEG, 0); DEBUG_SERIAL.print(" deg, firmware clamp +/-"); DEBUG_SERIAL.print(LIMIT_NOM_DEG, 0); DEBUG_SERIAL.println(" deg, park +25");
  DEBUG_SERIAL.print("current: limit "); DEBUG_SERIAL.print(CURRENT_LIMIT_MA); DEBUG_SERIAL.print(" mA (EEPROM), goal "); DEBUG_SERIAL.print(goalCurrentMa); DEBUG_SERIAL.print(" mA = ");
  DEBUG_SERIAL.print(goalCurrentMa * 0.354f / 84.0f, 2); DEBUG_SERIAL.println(" N tangential at 84 mm (0.354 Nm/A linear)");
  DEBUG_SERIAL.print("velocity: profile cap "); DEBUG_SERIAL.print(PROFILE_VEL_MAX_LSB); DEBUG_SERIAL.print(" LSB = "); DEBUG_SERIAL.print(PROFILE_VEL_MAX_LSB * 0.229f * 2.0f * 3.14159f / 60.0f * ARM_LEN_MM, 0); DEBUG_SERIAL.println(" mm/s tip; accel 20-60 LSB");
  DEBUG_SERIAL.print("trips: stall "); DEBUG_SERIAL.print(STALL_FRACTION * goalCurrentMa, 0); DEBUG_SERIAL.print(" mA/"); DEBUG_SERIAL.print(STALL_MS); DEBUG_SERIAL.print(" ms; comm "); DEBUG_SERIAL.print(COMM_FAIL_LIMIT * TICK_MS);
  DEBUG_SERIAL.print(" ms; bus watchdog "); DEBUG_SERIAL.print(BUS_WATCHDOG_LSB * 20); DEBUG_SERIAL.print(" ms; mcu watchdog 1000 ms; session "); DEBUG_SERIAL.print(SESSION_MAX_MS / 60000); DEBUG_SERIAL.println(" min");
}
void printStatus() {
  DEBUG_SERIAL.print("state="); DEBUG_SERIAL.print(STATE_NAMES[state]); DEBUG_SERIAL.print(" fault="); DEBUG_SERIAL.print(FAULT_NAMES[fault]);
  DEBUG_SERIAL.print(" rail="); DEBUG_SERIAL.print(railOn); DEBUG_SERIAL.print(" pos="); DEBUG_SERIAL.print(presentDeg(), 1); DEBUG_SERIAL.print(" mA="); DEBUG_SERIAL.print(presentMa);
  DEBUG_SERIAL.print(" strokes="); DEBUG_SERIAL.print(strokeN); DEBUG_SERIAL.print(" blind="); DEBUG_SERIAL.print(blindActive); DEBUG_SERIAL.print(" code="); printCode(); DEBUG_SERIAL.println();
  printSettingsLine();
}
void printHelp() {
  DEBUG_SERIAL.println("help status limits | run stop reset zero | goto <deg> (idle, +/-28) gotoraw <deg> (unclamped, expect servo refusal) hang (watchdog test)");
  DEBUG_SERIAL.println("mode human|periodic|auto | spd <0-100>|auto | var <0-100>|auto | cur <mA> | seed <n> | log on|off");
  DEBUG_SERIAL.println("amp <min> <max> | speed <min> <max> | jitter <%> | asym <%> | dwell <ms> | pause <p> | pausen <min> <max> | pausems <min> <max> | episode <min> <max> | slow <p> | periodic <deg> <mm/s>");
  DEBUG_SERIAL.println("bset <slot1-8> per|hum|auto <spd%|-1> <var%|-1> | blind <n> | next | reveal | unblind");
}
void applySlot(uint8_t k) { modeOverride = blindSlot[k].mode; spdOverridePct = blindSlot[k].spd; varOverridePct = blindSlot[k].var; episodeEndMs = 0; }

void handleCommand(char* line) {
  char* cmd = strtok(line, " \r\n"); if (!cmd) return;
  char* a1 = strtok(NULL, " \r\n"); char* a2 = strtok(NULL, " \r\n"); char* a3 = strtok(NULL, " \r\n");
  float f1 = a1 ? atof(a1) : 0, f2 = a2 ? atof(a2) : 0;
  bool idle = state == ST_LIFTED_IDLE && idleTorque;
  if (!strcmp(cmd, "help") || !strcmp(cmd, "?")) { printHelp(); return; }
  else if (!strcmp(cmd, "status")) { printStatus(); return; }
  else if (!strcmp(cmd, "limits")) { printLimits(); return; }
  else if (!strcmp(cmd, "run"))   runLatch = true;
  else if (!strcmp(cmd, "stop"))  { runLatch = false; if (state == ST_RUNNING) stopToPark(); }
  else if (!strcmp(cmd, "reset")) { if (state == ST_FAULT) { fault = F_NONE; commFails = 0; hwError = 0; enterState(ST_INIT); } }
  else if (!strcmp(cmd, "zero"))  {
    if (state == ST_RUNNING || !railOn) { DEBUG_SERIAL.println("needs: not running, rail on"); return; }
    dxl.begin(DXL_BAUD); dxl.setPortProtocolVersion(DXL_PROTOCOL);
    if (!dxl.ping(DXL_ID_ELBOW)) { DEBUG_SERIAL.println("no servo"); return; }
    wr(BUS_WATCHDOG, 0);
    DEBUG_SERIAL.println(calibrateZero() ? "zero OK (stored in servo Homing Offset)" : "zero FAILED"); enterState(ST_INIT);
  }
  else if (!strcmp(cmd, "goto") && a1)    { if (!idle) { DEBUG_SERIAL.println("goto: only in LIFTED_IDLE"); return; } runLatch = false; setGoal(f1, tipSpeedToVelLsb(60.0f), PROFILE_ACC_MIN_LSB, LIMIT_ABS_DEG); DEBUG_SERIAL.print("goal "); DEBUG_SERIAL.println(goalDeg, 1); }
  else if (!strcmp(cmd, "gotoraw") && a1) { if (!idle) { DEBUG_SERIAL.println("gotoraw: only in LIFTED_IDLE"); return; } runLatch = false;
    bool ok = wr(GOAL_POSITION, degToTicks(f1)); DEBUG_SERIAL.print("servo "); DEBUG_SERIAL.println(ok ? "ACCEPTED (inside EEPROM limits)" : "REFUSED (data range error) - expected beyond +/-28"); }
  else if (!strcmp(cmd, "hang"))   { DEBUG_SERIAL.println("hang: loop stopped, MCU watchdog should reset in ~1 s"); DEBUG_SERIAL.flush(); while (true) {} }
  else if (!strcmp(cmd, "mode"))   modeOverride = a1 && !strcmp(a1, "human") ? 1 : (a1 && !strcmp(a1, "periodic") ? 0 : -1);
  else if (!strcmp(cmd, "spd") && a1)    spdOverridePct = !strcmp(a1, "auto") ? -1 : (int)clampf(f1, 0, 100);
  else if (!strcmp(cmd, "var") && a1)    varOverridePct = !strcmp(a1, "auto") ? -1 : (int)clampf(f1, 0, 100);
  else if (!strcmp(cmd, "amp") && a2)    { P.amp_min_deg = clampf(f1, 5, LIMIT_NOM_DEG); P.amp_max_deg = clampf(f2, P.amp_min_deg, LIMIT_NOM_DEG); episodeEndMs = 0; }
  else if (!strcmp(cmd, "speed") && a2)  { P.spd_min_mm_s = clampf(f1, 20, TIP_SPEED_CAP_MM_S); P.spd_max_mm_s = clampf(f2, P.spd_min_mm_s, TIP_SPEED_CAP_MM_S); episodeEndMs = 0; }
  else if (!strcmp(cmd, "jitter") && a1) P.jitter_amp = P.jitter_spd = clampf(f1 / 100.0f, 0, 1);
  else if (!strcmp(cmd, "asym") && a1)   P.asym = clampf(f1 / 100.0f, 0, 0.5f);
  else if (!strcmp(cmd, "dwell") && a1)  P.dwell_max_ms = (uint16_t)clampf(f1, 0, 1000);
  else if (!strcmp(cmd, "pause") && a1)  P.pause_prob = clampf(f1, 0, 1);
  else if (!strcmp(cmd, "pausen") && a2) { P.pause_every_min = (uint8_t)clampf(f1, 1, 50); P.pause_every_max = (uint8_t)clampf(f2, P.pause_every_min, 50); }
  else if (!strcmp(cmd, "pausems") && a2){ P.pause_min_ms = (uint16_t)clampf(f1, 100, 10000); P.pause_max_ms = (uint16_t)clampf(f2, P.pause_min_ms, 10000); }
  else if (!strcmp(cmd, "episode") && a2){ P.episode_min_s = (uint16_t)clampf(f1, 1, 120); P.episode_max_s = (uint16_t)clampf(f2, P.episode_min_s, 120); }
  else if (!strcmp(cmd, "slow") && a1)   P.slow_stroke_prob = clampf(f1, 0, 1);
  else if (!strcmp(cmd, "periodic") && a2){ P.periodic_amp_deg = clampf(f1, 5, LIMIT_NOM_DEG); P.periodic_spd_mm_s = clampf(f2, 20, TIP_SPEED_CAP_MM_S); }
  else if (!strcmp(cmd, "cur") && a1)    { goalCurrentMa = (uint16_t)clampf(f1, GOAL_CURRENT_MIN, CURRENT_LIMIT_MA); if (state == ST_LIFTED_IDLE || state == ST_RUNNING) wr(GOAL_CURRENT, goalCurrentMa); }
  else if (!strcmp(cmd, "seed") && a1)   { rngSeed = (uint32_t)strtoul(a1, NULL, 10); if (!rngSeed) rngSeed = 1; rngState = rngSeed; episodeEndMs = 0; }
  else if (!strcmp(cmd, "log") && a1)    logOn = !strcmp(a1, "on");
  // ---- BLIND (§Q.3): define slots, shuffle, step through hidden, reveal at the end ----
  else if (!strcmp(cmd, "bset") && a3)   { uint8_t k = (uint8_t)clampf(f1, 1, 8) - 1;
    blindSlot[k].mode = !strcmp(a2, "per") ? 0 : (!strcmp(a2, "hum") ? 1 : -1);
    blindSlot[k].spd = (int16_t)clampf(atof(a3), -1, 100); char* a4 = strtok(NULL, " \r\n"); blindSlot[k].var = a4 ? (int16_t)clampf(atof(a4), -1, 100) : -1; }
  else if (!strcmp(cmd, "blind") && a1)  { blindN = (uint8_t)clampf(f1, 1, 8);
    for (uint8_t i = 0; i < blindN; i++) blindOrder[i] = i;
    for (uint8_t i = blindN - 1; i > 0; i--) { uint8_t j = (uint8_t)rndInt(0, i); uint8_t t = blindOrder[i]; blindOrder[i] = blindOrder[j]; blindOrder[j] = t; }
    blindIdx = 0; blindActive = true; applySlot(blindOrder[0]);
    DEBUG_SERIAL.print("BLIND: trial 1 of "); DEBUG_SERIAL.print(blindN); DEBUG_SERIAL.println(" armed (mode/levels hidden; 'next', 'reveal')"); }
  else if (!strcmp(cmd, "next"))         { if (!blindActive) { DEBUG_SERIAL.println("not blind"); return; }
    if (blindIdx + 1 >= blindN) { DEBUG_SERIAL.println("BLIND: last trial done; 'reveal'"); return; }
    applySlot(blindOrder[++blindIdx]); DEBUG_SERIAL.print("BLIND: trial "); DEBUG_SERIAL.print(blindIdx + 1); DEBUG_SERIAL.print(" of "); DEBUG_SERIAL.println(blindN); }
  else if (!strcmp(cmd, "reveal"))       { for (uint8_t i = 0; i < blindN; i++) { Slot& s = blindSlot[blindOrder[i]];
      DEBUG_SERIAL.print("R,trial "); DEBUG_SERIAL.print(i + 1); DEBUG_SERIAL.print(" = slot "); DEBUG_SERIAL.print(blindOrder[i] + 1); DEBUG_SERIAL.print(' ');
      DEBUG_SERIAL.print(s.mode == 1 ? "HUM" : (s.mode == 0 ? "PER" : "toggle")); DEBUG_SERIAL.print(" S"); DEBUG_SERIAL.print(s.spd); DEBUG_SERIAL.print(" V"); DEBUG_SERIAL.println(s.var); } }
  else if (!strcmp(cmd, "unblind"))      { blindActive = false; modeOverride = -1; spdOverridePct = -1; varOverridePct = -1; }
  else { DEBUG_SERIAL.println("? (type help)"); return; }
  DEBUG_SERIAL.print("ok "); DEBUG_SERIAL.println(cmd);
}
void serviceSerial() {
  static char buf[64]; static uint8_t n = 0;
  while (DEBUG_SERIAL.available()) {
    char c = (char)DEBUG_SERIAL.read();
    if (c == '\n' || c == '\r') { if (n) { buf[n] = 0; handleCommand(buf); n = 0; } }
    else if (n < sizeof(buf) - 1) buf[n++] = c;
  }
}

// ------------------------------- setup / loop -------------------------------------------
void setup() {
  pinMode(PIN_MODE_TOGGLE, INPUT_PULLUP); pinMode(PIN_STATUS_LED, OUTPUT); pinMode(LED_BUILTIN, OUTPUT);
  dxlPowerOff();                                        // bus stays dead until INIT decides otherwise
  for (auto& s : blindSlot) s = { -1, -1, -1 };
  DEBUG_SERIAL.begin(SERIAL_BAUD);
  uint32_t t0 = millis(); while (!DEBUG_SERIAL && millis() - t0 < 1500) {}   // never block on the host
  DEBUG_SERIAL.print("PROJECT SCRATCH SP1 "); DEBUG_SERIAL.println(FW_VERSION);
  printLimits(); printSettingsLine();
  if (MCU_WATCHDOG) wdtInit();
  enterState(ST_INIT);
}

void loop() {
  uint32_t now = millis();
  if (now - lastTickMs < TICK_MS) { serviceSerial(); return; }
  lastTickMs = now; wdtKick(); readInputs(); serviceSerial();

  switch (state) {
    case ST_INIT:
      if (!railOn) { static uint32_t last = 0; if (now - last > 2000) { last = now; DEBUG_SERIAL.println("INIT: waiting for actuator rail (e-stop out, button held)"); } break; }
      if (fault == F_NONE && servoConfigure()) { idleTorque = true; enterState(ST_LIFTED_IDLE); }
      else goFault(fault == F_NONE ? F_CONFIG : fault);
      break;
    case ST_LIFTED_IDLE:
      if (!railOn) { enterState(ST_PAUSED); break; }
      if (!pollServo()) { goFault(F_COMM); break; }
      checkTrips(); if (state == ST_FAULT) break;
      if (runLatch && idleTorque && now - stateEnteredMs >= LIFTED_HOLD_MS) {
        strokeN = 0; timeoutsInRow = 0; dir = -1; episodeEndMs = 0; stallStartMs = 0;
        strokesToPause = (uint8_t)rndInt(P.pause_every_min, P.pause_every_max);
        sessionStartMs = now; enterState(ST_RUNNING); beginStroke();
      } else if (!idleTorque && now - stateEnteredMs > 1500 && dxl.getTorqueEnableStat(DXL_ID_ELBOW)) {
        dxl.torqueOff(DXL_ID_ELBOW); DEBUG_SERIAL.println("torque off at park");       // shutdown complete
      }
      if (!idleTorque && runLatch) { idleTorque = true; enterState(ST_INIT); }          // 'run' after a stop: re-init
      break;
    case ST_RUNNING:
      if (!railOn) { enterState(ST_PAUSED); break; }   // hardware already cut the servo; mirror it
      if (!pollServo()) { goFault(F_COMM); break; }
      checkTrips(); if (state == ST_FAULT) break;
      runningTick();
      break;
    case ST_PAUSED:                                    // rail off: servo and magnet unpowered by hardware
      if (railOn) { DEBUG_SERIAL.println("rail restored: re-initialising servo"); enterState(ST_INIT); }
      break;
    case ST_FAULT: break;                              // until 'reset'
  }
  telemetry(); ledTick();
}
