"""Unit tests for the host-side inverse kinematics (SPEC §8.2)."""
import math

import pytest

from sp1v3.ik import CableComp, DishModel, Geometry, TendonIK, path_ik
from sp1v3 import paths

IK = TendonIK()


def grid(rmax=16.5, n_r=12, n_a=24):
    yield (0.0, 0.0)
    for i in range(1, n_r + 1):
        r = rmax * i / n_r
        for k in range(n_a):
            a = 2 * math.pi * k / n_a
            yield (r * math.cos(a), r * math.sin(a))


# ------------------------------------------------------------------------- dish model
def test_dish_rise_matches_spec_profile():
    d = DishModel()
    assert d.rise(0.0) == 0.0
    # R160 sphere to 7 mm: 7^2 / (2*160) = 0.153 (+ half the 1 mm blend)
    assert d.rise(7.0) == pytest.approx(0.153, abs=0.12)
    # +4.5 mm over the 34 deg band to 13.7
    assert d.rise(13.7) - d.rise(7.0) == pytest.approx(4.5, abs=0.2)
    # +8.5 mm total at the rim top (17.0)
    assert d.rise(17.0) == pytest.approx(8.6, abs=0.25)


def test_dish_rise_monotonic_and_c1():
    d = DishModel()
    prev_z, prev_s = 0.0, 0.0
    r = 0.0
    while r < 17.0:
        r2 = r + 0.05
        z = d.rise(r2)
        s = (z - d.rise(r)) / 0.05
        assert z >= prev_z - 1e-12
        assert abs(s - prev_s) < 0.1, f"slope jump at r={r:.2f}: {prev_s:.3f} -> {s:.3f}"
        prev_z, prev_s, r = z, s, r2


def test_dish_tilt_limits():
    d = DishModel()
    assert d.tilt(0.0) == 0.0
    assert d.tilt(7.0) == pytest.approx(0.0, abs=1e-9)
    assert math.degrees(d.tilt(17.0)) == pytest.approx(5.5, abs=1e-6)
    assert all(d.tilt(r / 10) <= math.radians(5.5) + 1e-12 for r in range(0, 171))


def test_dish_from_table():
    t = DishModel.from_table([(0, 0, 0), (10, 2, 1), (17, 8.5, 5.5)])
    assert t.rise(5) == pytest.approx(1.0)
    assert math.degrees(t.tilt(13.5)) == pytest.approx(3.25)


# ------------------------------------------------------------------------- IK basics
def test_centred_block_is_zero():
    assert IK.ik((0.0, 0.0)) == pytest.approx([0.0, 0.0, 0.0], abs=1e-12)


def test_small_motion_toward_stop_shortens_that_cable_one_to_one():
    # stop A at 90 deg: moving +y by a small amount shortens cable A by the same amount
    J = IK.jacobian((0.0, 0.0))
    assert J[0][1] == pytest.approx(-1.0, abs=1e-3)
    assert J[0][0] == pytest.approx(0.0, abs=1e-6)
    # B (210 deg) and C (330 deg) lengthen by sin(30 deg) = 0.5
    assert J[1][1] == pytest.approx(0.5, abs=1e-3)
    assert J[2][1] == pytest.approx(0.5, abs=1e-3)


def test_three_fold_symmetry():
    rot = 2 * math.pi / 3
    for d in grid(n_r=5, n_a=7):
        x, y = d
        d2 = (x * math.cos(rot) - y * math.sin(rot), x * math.sin(rot) + y * math.cos(rot))
        l1, l2 = IK.ik(d), IK.ik(d2)
        # rotating the block by +120 deg moves cable i's role to cable i+1
        assert l2 == pytest.approx([l1[2], l1[0], l1[1]], abs=1e-9)


def test_mirror_symmetry_about_stop_a_axis():
    for d in grid(n_r=5, n_a=7):
        l1 = IK.ik(d)
        l2 = IK.ik((-d[0], d[1]))
        assert l2 == pytest.approx([l1[0], l1[2], l1[1]], abs=1e-9)


def test_rise_hand_calculation_without_tilt():
    g = Geometry(dish=DishModel(tilt_max_deg=0.0))
    ik = TendonIK(g)
    r = 16.5
    z = g.dish.rise(r)
    # move straight toward stop A (+y): horizontal gap 48 - 30 - 16.5 = 1.5 mm, vertical z
    expect = math.sqrt(1.5 ** 2 + z ** 2) - 18.0
    assert ik.ik((0.0, r))[0] == pytest.approx(expect, abs=1e-9)
    # cable B: post at (30cos210, 30sin210 + 16.5, z)
    a = (48 * math.cos(math.radians(210)), 48 * math.sin(math.radians(210)), 0.0)
    p = (30 * math.cos(math.radians(210)), 30 * math.sin(math.radians(210)) + r, z)
    lb = math.dist(a, p) - 18.0
    assert ik.ik((0.0, r))[1] == pytest.approx(lb, abs=1e-9)


def test_tilt_raises_the_leading_post():
    ik = TendonIK()
    c, axis, ang = ik.block_pose((0.0, 16.5))
    posts = ik.posts((0.0, 16.5))
    # post A (leading, +y side) sits higher than the block centre by ~30 sin(t)
    assert posts[0][2] - c[2] == pytest.approx(30 * math.sin(ang), abs=1e-9)
    assert posts[1][2] < c[2] and posts[2][2] < c[2]


def test_round_trip_fk_ik_whole_workspace():
    worst = 0.0
    for d in grid():
        l = IK.ik(d)
        d2 = IK.fk(l, guess=(0.0, 0.0))
        worst = max(worst, math.hypot(d2[0] - d[0], d2[1] - d[1]))
    assert worst < 1e-6


def test_workspace_conditioning_reported():
    # default (spec) geometry: the Jacobian stays usable (singular-value ratio < 4) everywhere
    worst = max(IK.condition(d) for d in grid())
    assert worst < 4.0
    # a wider stop circle (CONFLICTS E-C10 proposal) is better conditioned at the rim
    wide = TendonIK(Geometry(stop_radius=70.0))
    assert max(wide.condition(d) for d in grid()) < worst


def test_ik_is_continuous_along_a_fine_radial_sweep():
    prev = IK.ik((0.0, 0.0))
    for k in range(1, 1651):
        cur = IK.ik((0.0, k * 0.01))
        assert max(abs(cur[i] - prev[i]) for i in range(3)) < 0.02   # < 2 x the path step
        prev = cur


def test_microstep_resolution():
    rot_dist = math.pi * 12.0
    assert rot_dist / (200 * 16) == pytest.approx(0.0118, abs=1e-4)   # SPEC: 12 um of cable


# ------------------------------------------------------------------------- statics
def test_tension_change_balances_external_force():
    for d in grid(n_r=4, n_a=6):
        F = (0.3, -0.4)
        dT = IK.tension_change(d, F)
        u = IK.unit_vectors(d)
        sx = sum(dT[i] * u[i][0] for i in range(3)) + F[0]
        sy = sum(dT[i] * u[i][1] for i in range(3)) + F[1]
        assert abs(sx) < 1e-9 and abs(sy) < 1e-9


def test_tension_change_zero_force_is_zero():
    assert IK.tension_change((3.0, 4.0), (0.0, 0.0)) == pytest.approx([0, 0, 0], abs=1e-12)


# ------------------------------------------------------------------------- compensation
def test_deadband_compensation_on_reversal():
    comp = CableComp(b=(0.8, 0.8, 0.8), spread_mm=3.0)
    comp.reset(last_direction=+1)
    # cable 0 increases for a while, then decreases
    s = 0.0
    out = []
    seq = [i * 0.1 for i in range(50)] + [4.9 - i * 0.1 for i in range(1, 50)]
    for v in seq:
        s += 0.1
        out.append(comp.apply([v, 0.0, 0.0], s)[0] - v)
    assert out[10] == pytest.approx(+0.4)                  # paying out: +b/2
    assert out[-1] == pytest.approx(-0.4)                  # reeling in: -b/2
    # the switch is spread over 3 mm of path: no step bigger than b/(3 mm / 0.1 mm) + eps
    steps = [abs(out[i + 1] - out[i]) for i in range(len(out) - 1)]
    assert max(steps) <= 0.8 / 30 + 1e-9


def test_zero_deadband_is_identity():
    comp = CableComp()
    comp.reset()
    for k in range(20):
        l = [math.sin(k / 3), math.cos(k / 3), 0.1 * k]
        assert comp.apply(l, k * 0.5) == pytest.approx(l)


def test_spring_feedforward_sign():
    comp = CableComp(k=(1.2, 1.2, 1.2))
    comp.reset()
    out = comp.apply([1.0, 1.0, 1.0], 0.0, dT=(0.6, 0.0, -0.6))
    assert out == pytest.approx([1.0 - 0.5, 1.0, 1.0 + 0.5])   # more tension -> reel in


# ------------------------------------------------------------------------- streamed paths
def test_cable_speed_bounded_on_fastest_pline():
    tok = paths.line(37.0, amp=16.5, f=2.0)
    l = path_ik(IK, [(x, y) for _, x, y in tok.samples])
    dt = tok.samples[1][0]
    vmax = max(max(abs(l[k + 1][i] - l[k][i]) for i in range(3)) / dt for k in range(len(l) - 1))
    # block <= 200 mm/s; cable speed <= block speed x max |dl/dd| (~1) plus rim geometry
    assert vmax < 230.0
    # and stays far below the drum's stepping limit at 1/16 (2 kHz/0.0118 mm = 23 mm/s per kHz)
    assert vmax / 0.01178 < 25000          # step rate < 25 kHz, Klipper on an H723 manages > 100 kHz


# ------------------------------------------------------------------------- tendon statics audit
@pytest.mark.parametrize("geom,total,ok", [
    (Geometry(), 4.5, False),                                     # SPEC M13/M14: stops R48, posts R30, 1.5 N
    (Geometry(stop_radius=70.0, post_radius=15.0), 6.0, True),    # CONFLICTS E-C1 proposal, 2.0 N each
    (Geometry(stop_radius=65.0, post_radius=10.0), 6.0, True),    # alternative: small yoke hub, 2.0 N each
])
def test_tendons_hold_the_block_with_positive_tension_everywhere(geom, total, ok):
    """Predicted tensions over |d| <= 16.5 incl. the modelled rim reaction must stay inside the
    comparator window (0.2 N slack limit ... 3.6 N) with margin: 0.3 ... 3.3 N."""
    from sp1v3.forcemodel import ForceModel
    a = TendonIK(geom).audit(ForceModel(), total=total)
    if ok:
        assert a["reach_min"] >= 16.5 and a["min_T"] >= 0.3 and a["max_T"] <= 3.3, a
    else:
        # documents the conflict: positive-tension reach is only ~9 mm in the worst direction
        assert a["reach_min"] < 10.0 and a["min_T"] < 0.0, a


def test_predicted_tensions_sum_and_balance():
    ik = TendonIK(Geometry(stop_radius=70.0))
    d, F = (5.0, -3.0), (0.4, 0.2)
    T = ik.tensions(d, F)
    assert sum(T) == pytest.approx(4.5)
    u = ik.unit_vectors(d)
    assert sum(T[i] * u[i][0] for i in range(3)) == pytest.approx(-F[0], abs=1e-9)
    assert sum(T[i] * u[i][1] for i in range(3)) == pytest.approx(-F[1], abs=1e-9)
