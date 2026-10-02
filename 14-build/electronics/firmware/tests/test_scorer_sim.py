"""Smoke test of the scorer state machine against the Klipper simulator (no hardware)."""
import re
import threading
import time

import pytest

from sp1v3 import limits as L
from sp1v3.klipper import SimKlipper
from sp1v3.scorer import Scorer, load_config


def wait_for(pred, timeout=10.0):
    t0 = time.monotonic()
    while time.monotonic() - t0 < timeout:
        if pred():
            return True
        time.sleep(0.02)
    return False


@pytest.fixture
def sim(tmp_path):
    kl = SimKlipper()
    kl.buttons.update({"gcode_button k1_nc": True, "gcode_button estop_ok": True,
                       "gcode_button loop_ok": True})
    sc = Scorer(kl, load_config(path=str(tmp_path / "none.json")), str(tmp_path), sim=True)
    th = threading.Thread(target=sc.run, daemon=True)
    th.start()
    assert wait_for(lambda: sc.state == "SAFE")
    yield kl, sc
    sc._stop.set()
    sc.streamer.abort.set()


def test_lever_arms_plays_and_release_pauses(sim):
    kl, sc = sim
    assert kl.pins.get("m8p_ok") == 1.0 and kl.pins.get("watchdog") == 0.5
    sc.command("sim lever 1")
    assert wait_for(lambda: sc.state == "READY")
    assert any(l.startswith("MANUAL_STEPPER STEPPER=cable_a GCODE_AXIS=A") for l in kl.lines)
    assert wait_for(lambda: sc.state == "PLAY", 3.0)              # lever held 1 s -> APPROACH -> PLAY
    time.sleep(2.0)
    g1 = [l for l in kl.lines if l.startswith("G1 A")]
    assert len(g1) > 100
    # every streamed cable coordinate inside the configured stepper range
    for l in g1:
        for v in re.findall(r"[ABC](-?[0-9.]+)", l):
            assert abs(float(v)) < 25.0
    assert kl.pins.get("palm") == 1.0                             # float extended
    sc.command("sim lever 0")                                      # release: hardware vents, host pauses
    assert wait_for(lambda: sc.state == "PAUSED", 2.0)
    n = len([l for l in kl.lines if l.startswith("G1 A")])
    time.sleep(0.5)
    assert len([l for l in kl.lines if l.startswith("G1 A")]) == n  # streaming stopped


def test_latch_trip_faults_and_needs_reset(sim):
    kl, sc = sim
    sc.command("sim lever 1")
    assert wait_for(lambda: sc.state in ("READY", "PLAY"), 5.0)
    sc.command("sim latch 1")                                      # comparator / reflexd trip
    assert wait_for(lambda: sc.state in ("FAULT", "PAUSED"), 2.0)
    sc.command("sim lever 0")
    sc.command("sim latch 0")
    if sc.state == "FAULT":
        assert kl.pins.get("m8p_ok") == 0.0
        assert "ok" in sc.command("reset")
        assert sc.state == "SAFE"


def test_console_limits_and_clamp(sim):
    kl, sc = sim
    assert "no-reversal" in sc.command("limits")
    sc.command("force 5")
    assert sc.settings.force == pytest.approx(L.F_NAIL_MAX)
    sc.command("f 9")
    assert sc.settings.f == pytest.approx(2.0)
    assert "refused" in sc.command("inject hang")


def test_streamed_gcode_timing_matches_the_plan():
    """Each G1 lasts max|dl|/(F/60) in Klipper (extra-axis-only move, see printer.cfg notes):
    the streamed durations must add up to the planned token time."""
    from sp1v3 import paths
    from sp1v3.forcemodel import ForceModel
    from sp1v3.ik import CableComp, TendonIK
    from sp1v3.scorer import Streamer
    ik = TendonIK()
    for tok in (paths.line(30.0, f=1.4), paths.circle(phi0_deg=10.0, f=1.2, revs=1),
                paths.park((0.0, -16.5), 0.4)):
        st = Streamer(SimKlipper(realtime=False), ik, CableComp(), ForceModel())
        st.ff = False
        st.reset(ik.ik(tok.start), tok.start)
        last = dict(zip("ABC", ik.ik(tok.start)))
        total = 0.0
        for dur, lines, _ in st.gcode_for(tok):
            for l in lines:
                if l.startswith("G4"):
                    total += float(l.split("P")[1]) / 1000.0
                else:
                    args = dict((w[0], float(w[1:])) for w in l.split()[1:])
                    dmax = max(abs(args[a] - last[a]) for a in "ABC")
                    total += dmax / (args["F"] / 60.0)
                    last.update({a: args[a] for a in "ABC"})
        assert total == pytest.approx(tok.duration, rel=0.01, abs=0.002), tok.kind


def test_stream_discontinuity_is_refused():
    from sp1v3 import checker, paths
    from sp1v3.forcemodel import ForceModel
    from sp1v3.ik import CableComp, TendonIK
    from sp1v3.scorer import Streamer
    st = Streamer(SimKlipper(realtime=False), TendonIK(), CableComp(), ForceModel())
    st.reset()                                       # block believed at the centre
    with pytest.raises(checker.PathRejected):
        st.gcode_for(paths.line(0.0))                # token starts on the rim: refused
