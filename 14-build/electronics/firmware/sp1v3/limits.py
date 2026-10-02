"""SP1 v3 limits table: the ONE clamp point for every user/score-settable number.

Every value the host may command (speed, force, palm pressure, amplitude ...) passes
through `clamp()` before it is used.  The table is printed at boot (`limits` command)
and every log line carries the settings code (`settings_code()`).

Sources: 12-sp1v2/SYSTEM-SPEC-v3.md (§4.1-4.5, §7.2, §8.3-8.4).  Tags as in the spec:
KNOWN / EST / JUDG.  Firmware limits are the THIRD barrier; the mechanical caps
(reliefs, breakaways, coupling) and the hardware safety loop come first (red line 13).
"""
from __future__ import annotations

import hashlib
import json
import logging
from dataclasses import dataclass

log = logging.getLogger("sp1v3.limits")

# --------------------------------------------------------------------------------------
# Geometry of the dish gate (frame S, mm).  SPEC §4.2.
# --------------------------------------------------------------------------------------
D_MAX = 16.5            # no segment may command |d| beyond this (rim top 17.0)
R_NO_REVERSAL = 13.7    # C5: no reversal / cusp / sharp heading change inside this radius
R_LAND_INNER = 8.5      # landing band, inner edge (nails touch at |d| ~ 8.5-12.2)
R_LAND_OUTER = 12.2     # landing band, outer edge = "contact zone" boundary for checks
R_PARK = 16.5           # REST / PARK radius

# --------------------------------------------------------------------------------------
# Kinematic limits (SPEC §4.5, §8.3; hair rule H-5.4)
# --------------------------------------------------------------------------------------
V_MAX = 200.0                 # mm/s, any segment
A_CONTACT_MAX = 2000.0        # mm/s^2 while |d| < R_LAND_OUTER
HEADING_MAX_DEG = 30.0        # max heading change ...
HEADING_WINDOW_S = 0.050      # ... per 50 ms, inside R_NO_REVERSAL
V_REST_JOIN = 30.0            # mm/s: max first/last-interval speed of a token (tokens join at rest)
V_CUSP = 10.0                 # mm/s: slower than this inside R_NO_REVERSAL = a cusp/dwell
LAND_SPEED_FRAC = 0.30        # landing/lift at >= 0.3 v_peak
CIRCLE_RPE_MIN = 14.5         # R + e >= 14.5
CIRCLE_RME_MAX = 8.5          # R - e <= 8.5
CIRCLE_PREC_MIN_DEG = 15.0    # offset heading rotates >= 15 deg per revolution
CIRCLE_PREC_MAX_DEG = 40.0
CIRCLE_F_MAX = 1.5            # Hz: (1 + prec/360) * 360 * f * 0.05 s <= 30 deg at prec 40  ->  f <= 1.5 (EST, heading rule)
SAMPLE_DT = 0.005             # s, host path sampling (<= 1 mm at 200 mm/s)

# --------------------------------------------------------------------------------------
# Force model (SPEC §4.1, §4.3)
# --------------------------------------------------------------------------------------
N_PER_KPA_PIN = 0.0385        # Ø7.0 bore: 38.5 mm^2
PIN_SPRING_N = 0.03           # return spring at contact
RAIL_MAX_KPA = 15.6           # firmware ceiling = 0.60 N per nail
F_NAIL_MAX = 0.60
FLOAT_N_PER_KPA = 0.20        # Airpel E16: 2.0 cm^2
FLOAT_SPRING_N = 1.45         # EST mid of 1.2-1.7 N; measured at B2 -> `cal` overwrite
SKID_FLOOR_N = 0.45           # constant support margin
PALM_MAX_KPA = 20.0
PINS_PER_GROUP = {"A": 3, "B": 3}


@dataclass(frozen=True)
class Limit:
    default: float
    lo: float
    hi: float
    unit: str
    source: str


# The settable values.  Anything not in here cannot be set from a score or a console.
LIMITS: dict[str, Limit] = {
    "f":         Limit(1.4, 0.6, 2.0, "Hz", "§4.5 PLINE f 0.6-2.0"),
    "f_circle":  Limit(1.2, 0.6, CIRCLE_F_MAX, "Hz", "§8.3 heading rule (EST)"),
    "amp":       Limit(16.0, 14.0, 16.5, "mm", "§4.5 A 14-16.5"),
    "dpsi":      Limit(4.5, 0.0, 15.0, "deg/cycle", "§4.5 PLINE precession"),
    "dpsi_jit":  Limit(1.5, 0.0, 3.0, "deg", "§4.5 jitter"),
    "psi":       Limit(0.0, -180.0, 180.0, "deg", "LINE heading"),
    "R":         Limit(11.5, 9.0, 12.5, "mm", "§4.5 CIRCLE R (13 infeasible: CONFLICTS E-C9)"),
    "e":         Limit(3.5, 3.0, 6.0, "mm", "§4.5 CIRCLE offset (R+e>=14.5, R-e<=8.5)"),
    "prec":      Limit(25.0, CIRCLE_PREC_MIN_DEG, CIRCLE_PREC_MAX_DEG, "deg/rev", "§4.5"),
    "chord_e":   Limit(7.0, 0.0, 9.0, "mm", "§8.4 chord offset"),
    "force":     Limit(0.30, 0.10, F_NAIL_MAX, "N/nail", "§8.4 INTENSITY"),
    "force_lo_B": Limit(0.20, 0.20, 0.45, "N/nail", "Stage B INTENSITY band"),
    "sF":        Limit(0.15, 0.0, 0.30, "rel", "§8.4 force sigma"),
    "bratio":    Limit(1.0, 0.5, 1.0, "rel", "§4.3 line B ratio"),
    "palm":      Limit(18.0, 8.0, PALM_MAX_KPA, "kPa", "§4.3 PALM 8-20"),
    "rail":      Limit(8.0, 2.0, RAIL_MAX_KPA, "kPa", "§4.1 rail 2-13, ceiling 15.6"),
    "dwell":     Limit(90.0, 20.0, 300.0, "s", "H-5.5 placeholder, set at B5"),
    "session":   Limit(1200.0, 60.0, 1200.0, "s", "20-min cap"),
    "pause_p":   Limit(0.08, 0.0, 0.3, "p/stroke", "§8.4"),
    "rest_s":    Limit(0.5, 0.2, 3.0, "s", "§8.1 REST"),
    "approach_F": Limit(0.10, 0.05, 0.20, "N/nail", "§7.1 restart rule"),
}


def clamp(name: str, value: float) -> float:
    """The single clamp point.  Unknown names raise; out-of-range values are clamped and logged."""
    lim = LIMITS[name]
    v = float(value)
    if v != v:  # NaN
        log.warning("clamp %s: NaN -> default %s", name, lim.default)
        return lim.default
    c = min(max(v, lim.lo), lim.hi)
    if c != v:
        log.warning("clamp %s: %.4g -> %.4g [%s..%s]", name, v, c, lim.lo, lim.hi)
    return c


def table() -> str:
    rows = [f"{'name':<11}{'default':>9}{'lo':>9}{'hi':>9}  unit        source"]
    for k, l in LIMITS.items():
        rows.append(f"{k:<11}{l.default:>9.3g}{l.lo:>9.3g}{l.hi:>9.3g}  {l.unit:<11} {l.source}")
    rows.append(f"geometry: |d|<= {D_MAX}  no-reversal r {R_NO_REVERSAL}  landing {R_LAND_INNER}-{R_LAND_OUTER}"
                f"  v<= {V_MAX} mm/s  a_contact<= {A_CONTACT_MAX} mm/s2  heading<= {HEADING_MAX_DEG} deg/"
                f"{int(HEADING_WINDOW_S*1000)} ms")
    rows.append(f"force: {N_PER_KPA_PIN} N/kPa per pin; rail<= {RAIL_MAX_KPA} kPa; float {FLOAT_N_PER_KPA} N/kPa"
                f" - spring {FLOAT_SPRING_N} N; support margin {SKID_FLOOR_N} N")
    return "\n".join(rows)


def settings_code(settings: dict) -> str:
    """6-hex code of a settings dict; logged on every line so a blind A/B can be revealed later."""
    blob = json.dumps(settings, sort_keys=True, default=str).encode()
    return hashlib.sha1(blob).hexdigest()[:6]


# ------------------------------- force helpers ----------------------------------------
def nail_force(rail_kpa: float, ratio: float = 1.0) -> float:
    """Net normal force per nail at a given gallery pressure (N)."""
    return max(0.0, N_PER_KPA_PIN * rail_kpa * ratio - PIN_SPRING_N)


def rail_for_force(force_n: float) -> float:
    return (force_n + PIN_SPRING_N) / N_PER_KPA_PIN


def float_net(palm_kpa: float, spring_n: float = FLOAT_SPRING_N) -> float:
    return FLOAT_N_PER_KPA * palm_kpa - spring_n


def pins_total(rail_kpa: float, groups: str, bratio: float = 1.0) -> float:
    total = 0.0
    if "A" in groups:
        total += PINS_PER_GROUP["A"] * nail_force(rail_kpa)
    if "B" in groups:
        total += PINS_PER_GROUP["B"] * nail_force(rail_kpa, bratio)
    return total


def palm_for_support(rail_kpa: float, groups: str, bratio: float = 1.0,
                     spring_n: float = FLOAT_SPRING_N) -> float:
    """Minimum palm pressure for constant support: sum(F_pins) + 0.45 <= F_float."""
    return (pins_total(rail_kpa, groups, bratio) + SKID_FLOOR_N + spring_n) / FLOAT_N_PER_KPA
