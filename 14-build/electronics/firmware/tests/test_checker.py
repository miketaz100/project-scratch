"""Unit tests for the path checker (dish-gate C5, SPEC §8.3) with deliberately bad tokens."""
import math

import pytest

from sp1v3 import checker, paths
from sp1v3 import limits as L
from sp1v3.paths import Token
from sp1v3.planner import Planner, Settings

DT = L.SAMPLE_DT


def rules(tok):
    return {v.rule for v in checker.check_token(tok)}


def tok_from_fn(fn, T, kind="line", **kw):
    n = int(math.ceil(T / DT))
    s = [(T * k / n, *fn(T * k / n)) for k in range(n + 1)]
    return Token(kind, s, **kw)


GOOD_FORCE = {"rail": L.rail_for_force(0.30), "groups": "AB", "bratio": 1.0, "palm": 20.0}


# ------------------------------------------------------------------------- good tokens
@pytest.mark.parametrize("f", [0.6, 1.0, 1.4, 2.0])
@pytest.mark.parametrize("amp", [14.0, 16.0, 16.5])
@pytest.mark.parametrize("e", [0.0, 4.0, 9.0])
def test_lines_pass(f, amp, e):
    assert checker.check_token(paths.line(23.0, amp=amp, e=e, f=f)) == []


@pytest.mark.parametrize("R,e", [(11.5, 3.5), (9.0, 5.5), (12.0, 3.5), (12.5, 4.0)])
@pytest.mark.parametrize("prec", [15.0, 25.0, 40.0])
def test_circles_pass(R, e, prec):
    for f in (0.6, 1.2, 1.5):
        for direction in (1, -1):
            t = paths.circle(R=R, e=e, prec_deg=prec, f=f, revs=2, direction=direction, phi0_deg=40)
            assert checker.check_token(t) == [], (R, e, prec, f, direction)


def test_dpath_passes():
    for tok in paths.dpath(60.0, amp=16.0, f=1.4, side=-1):
        assert checker.check_token(tok) == []


def test_rim_connector_and_park_pass():
    a, b = (16.0, 0.0), (-11.0, 11.0)
    assert checker.check_token(paths.rim_arc(a, b)) == []
    assert checker.check_token(paths.park((0.0, -16.5), 0.4)) == []


def test_force_within_support_passes():
    t = paths.line(0.0)
    t.force = dict(GOOD_FORCE)
    assert checker.check_token(t) == []


# ------------------------------------------------------------------------- bad tokens
def test_P1_outside_rim_top():
    t = tok_from_fn(lambda t: (17.2 * math.cos(t), 17.2 * math.sin(t)), 0.3)
    assert "P1" in rules(t)


def test_P2_too_fast():
    t = paths.line(0.0, amp=16.5, f=3.0)          # bypasses the clamp: v_c ~ 238 mm/s
    assert "P2" in rules(t)


def test_P4_reversal_inside_no_reversal_radius():
    # in from the rim at constant speed, reverse at |d| = 5 (centre side), back out
    def fn(t):
        s = -16.0 + 150.0 * t if t < 0.14 else 5.0 - 150.0 * (t - 0.14)
        return (s, 0.0)
    t = tok_from_fn(fn, 0.28)
    r = rules(t)
    assert "P4rev" in r or "P5" in r


def test_P4_sharp_turn_without_stopping_inside():
    # straight in along x, 90 deg turn at the centre at full speed, straight out along y
    def fn(t):
        if t < 0.1:
            return (-15.0 + 150.0 * t, 0.0)
        return (0.0, 150.0 * (t - 0.1))
    t = tok_from_fn(fn, 0.2)
    assert "P4" in rules(t)


def test_P5_stop_on_the_scalp():
    # a smooth line that stops for 200 ms at |d| = 4 (a dwell in contact)
    def fn(t):
        if t < 0.1:
            return (-15.0 + 190.0 * t, 0.0)
        if t < 0.3:
            return (4.0, 0.0)
        return (4.0 + 110.0 * (t - 0.3), 0.0)
    t = tok_from_fn(fn, 0.4)
    assert "P5" in rules(t)


def test_P6_slow_landing():
    # fast in the centre, but crawling (10 % of v_peak) through the landing band 8.5-12.2
    def s_of(t):
        # piecewise: 0-0.25 s crawl from -16 to -8 (32 mm/s), then 160 mm/s to +16
        if t < 0.25:
            return -16.0 + 32.0 * t
        return -8.0 + 160.0 * (t - 0.25)
    t = tok_from_fn(lambda t: (s_of(t), 0.0), 0.4)
    assert "P6" in rules(t)


def test_P3_acceleration_in_contact():
    # 5 Hz, 3 mm lateral wiggle while crossing the centre: a ~ 3 m/s^2
    def fn(t):
        return (-15.0 + 120.0 * t, 3.0 * math.sin(2 * math.pi * 5 * t))
    t = tok_from_fn(fn, 0.25)
    assert "P3" in rules(t)


def test_P1_circle_too_big_for_the_rim():
    # R 13 needs e >= 4.5 to land (R - e <= 8.5) but then R + e = 17.5 > 16.5: infeasible (CONFLICTS)
    t = paths.circle(R=13.0, e=4.5, prec_deg=25.0, f=1.0, revs=1)
    assert "P1" in rules(t)


def test_P7_centred_circle_rejected():
    t = paths.circle(R=11.5, e=3.5, prec_deg=25.0, f=1.0, revs=1)
    t.params["e"] = 0.0                            # claim it is centred
    assert "P7" in rules(t)
    t2 = paths.circle(R=13.0, e=3.0, prec_deg=25.0, f=1.0, revs=1)   # R - e = 10 > 8.5: never lands
    assert "P7" in rules(t2)


def test_P7_circle_without_precession_rejected():
    t = paths.circle(R=11.5, e=3.5, prec_deg=0.0, f=1.0, revs=1)
    assert "P7" in rules(t)


def test_P7_circle_too_fast_for_heading_rule():
    t = paths.circle(R=11.5, e=3.5, prec_deg=40.0, f=1.9, revs=1)
    assert "P4" in rules(t)


def test_P8_valve_switch_inside_rejected():
    t = paths.line(0.0, f=1.4)
    t_mid = t.duration / 2                          # block at the centre
    t.events = [(t_mid, "groups", "A")]
    assert "P8" in rules(t)
    t.events = [(0.0, "groups", "A")]               # on the rim: fine
    assert "P8" not in rules(t)


def test_P9_force_ceiling_and_support():
    t = paths.line(0.0)
    t.force = dict(GOOD_FORCE, rail=20.0)
    assert "P9" in rules(t)
    t.force = dict(GOOD_FORCE, rail=L.rail_for_force(0.45), palm=12.0)   # 6 x 0.45 N on a weak float
    assert "P9" in rules(t)
    t.force = dict(GOOD_FORCE, palm=25.0)
    assert "P9" in rules(t)


def test_P10_token_must_start_and_end_on_the_rim_at_rest():
    t = tok_from_fn(lambda t: (-5.0 + 50.0 * t, 0.0), 0.2)      # starts at |d| = 5
    assert "P10" in rules(t)
    t2 = tok_from_fn(lambda t: (-16.0 + 150.0 * t, 0.0), 0.05)   # starts on the rim, but moving
    assert "P10" in rules(t2)


def test_P11_sampling_too_coarse():
    t = paths.line(0.0)
    t.samples = t.samples[::3]
    assert "P11" in rules(t)


def test_P12_gap_between_tokens():
    a = paths.line(0.0)
    b = paths.line(10.0)
    v = checker.check_sequence([a, b])
    assert any(x.rule == "P12" for x in v)


def test_assert_ok_raises():
    with pytest.raises(checker.PathRejected):
        checker.assert_ok(paths.line(0.0, amp=16.5, f=3.0))


# ------------------------------------------------------------------------- planner integration
@pytest.mark.parametrize("mode", ["pline", "line", "circle", "mix", "dpath"])
@pytest.mark.parametrize("seed", [1, 7, 42])
def test_planner_output_always_passes(mode, seed):
    for f in (0.6, 1.4, 2.0):
        p = Planner(Settings(mode=mode, seed=seed, f=f, f_circle=min(f, 1.5), force=0.45))
        p.st.ramp_left = 3
        toks = []
        while p.st.t_session < 60:
            toks += p.next_tokens()
        assert checker.check_sequence(toks) == []
        assert p.st.log == []                     # no rejected candidates either
        # every token carries a force setting that satisfies constant support
        for t in toks:
            if t.force:
                need = L.pins_total(t.force["rail"], t.force["groups"], t.force["bratio"]) + L.SKID_FLOOR_N
                assert need <= L.float_net(t.force["palm"]) + 1e-9
