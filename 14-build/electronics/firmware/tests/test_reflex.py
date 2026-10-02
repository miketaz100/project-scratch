"""Tests for the reflexd snag criterion (SPEC §8.5 layer F)."""
import math

from sp1v3.forcemodel import ForceModel
from sp1v3.ik import Geometry, TendonIK
from sp1v3.reflexd import SnagDetector

# The spec tendon geometry (stops R48 / posts R30) cannot hold the block with positive tension
# beyond ~9 mm in three sextants (CONFLICTS E-C1); the criterion itself is geometry-independent,
# so it is tested on the proposed geometry (stops R70).
IK = TendonIK(Geometry(stop_radius=70.0, post_radius=15.0))
FM = ForceModel()


def tensions_for(d, F_ext):
    """Tensions a perfect sensor would read (common mode set by the floating stop plate, 3 x 2.0 N)."""
    return IK.tensions(d, F_ext, total=6.0)


def run(det, extra=(0.0, 0.0), extra_from=None, T_total=0.6, v=(140.0, 0.0), pins=2.0):
    """Block moving along +x through the centre; optional extra force from time extra_from."""
    t, dt = 0.0, 0.002
    while t < T_total:
        d = (-12.0 + v[0] * t, 0.0)
        if abs(d[0]) > 12.0:
            d = (math.copysign(12.0, d[0]), 0.0)
        F = FM.external(d, v, pins, True)
        if extra_from is not None and t >= extra_from:
            F = (F[0] + extra[0], F[1] + extra[1])
        trip, why, res = det.update(t, tensions_for(d, F), d, v, pins, True, armed=True)
        if trip:
            return t, why
        t += dt
    return None, ""


def test_no_snag_no_trip():
    det = SnagDetector(IK, FM)
    t, why = run(det)
    assert t is None, why


def test_large_snag_trips_within_4_ms():
    det = SnagDetector(IK, FM)
    t, why = run(det, extra=(-1.2, 0.0), extra_from=0.08)
    assert t is not None and t - 0.08 <= 0.0041, (t, why)


def test_moderate_opposing_drag_trips_after_60_ms():
    det = SnagDetector(IK, FM)
    t, why = run(det, extra=(-0.6, 0.0), extra_from=0.05)
    assert t is not None and 0.058 <= t - 0.05 <= 0.07, (t, why)


def test_lateral_0_6N_does_not_trip():
    det = SnagDetector(IK, FM)
    t, why = run(det, extra=(0.0, 0.6), extra_from=0.05)
    assert t is None, why


def test_cable_break_pattern_trips():
    det = SnagDetector(IK, FM)
    trip = False
    for k in range(3):
        trip, why, _ = det.update(k * 0.002, [2.0, 0.05, 2.0], (0.0, 0.0), (0.0, 0.0), 0.0, False, armed=True)
    assert trip and "pattern" in why


def test_disarmed_never_trips_on_residual():
    det = SnagDetector(IK, FM)
    for k in range(100):
        trip, _, _ = det.update(k * 0.002, [1.5, 1.5, 1.5], (5.0, 0.0), (100.0, 0.0), 2.0, True, armed=False)
        assert not trip
