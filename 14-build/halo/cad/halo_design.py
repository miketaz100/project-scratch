#!/usr/bin/env python
"""
halo_design.py - HALO numbers from Michael's tape fit (PROJECT SCRATCH / 14-build/halo/cad / 2026-10-02)

  <cadenv>/bin/python halo_design.py [--set HL=201 ...] [--light-float]

Prints: derived dimensions, cut list (carbon), beta notch positions, alpha stop guide, mass ledger by
part, centre of mass and lean at the spec poses, hinge torque check.  Writes bail_template.svg
(1:1 bonding template; print at 100 %, check the 100 mm bar).
Reads stl/_part_table.csv (run gen_halo_stl.py first) for printed-part masses.
"""
import os, sys, math, csv
from gen_halo_stl import get_params

HERE = os.path.dirname(os.path.abspath(__file__))
G = 9.81e-6   # N per (g * mm) -> N*m


def main():
    over = {}
    args = sys.argv[1:]
    light = "--light-float" in args
    while "--set" in args:
        i = args.index("--set")
        k, val = args[i + 1].split("=")
        over[k] = float(val)
        del args[i:i + 2]
    p, v = get_params(over)
    d = math.radians
    # ------------------------------------------------------------ derived
    print("=== DERIVED FROM THE TAPE FIT ===")
    for k in ("HA", "HBB", "HCZ", "TRAG_X", "BROW_Z", "EAR_TOP_Z", "Y_SIDE_IN", "Y_F1", "Y_HINGE0", "Y_HINGE1", "Y_HUB",
              "R_BAIL", "R_SI", "DELTA", "LEG_L", "SH_Y", "SH_Z", "RHO_SPIDER_TOP", "RHO_PLATE1", "RHO_BODY1", "R_NB", "X_NB"):
        print("  %-16s %8.2f" % (k, v[k]))
    print("  helmet width at the shoulder nodes: %.0f mm; at the hub feet: %.0f mm" % (2 * v["SH_Y"] + 2 * 5.7, 2 * (v["Y_HUB"] + 15)))
    print("  Airpel top above the vertex scalp: %.0f mm" % (v["RHO_BODY1"] - v["HCZ"]))
    # hairline angle from G2H (arc length along the midline ellipse from the brow)
    a, c = v["HA"], v["HCZ"]
    zb = v["BROW_Z"]
    t0 = math.asin(max(-1, min(1, zb / c)))           # parametric angle of the brow (x = a cos t, z = c sin t)
    s, t = 0.0, t0
    while s < v["G2H"] and t < math.pi / 2:
        dt = 0.0005
        s += math.hypot(a * math.sin(t), c * math.cos(t)) * dt
        t += dt
    xh, zh = a * math.cos(t), c * math.sin(t)
    th = math.degrees(math.atan2(xh, zh))              # angle from vertical, forward
    print("  front hairline point: X %.0f Z %.0f -> %.1f deg in front of the vertex (alpha_hairline = %.1f)" % (xh, zh, th, -th))
    a_front = -th + 20
    print("  spec rule alpha_hairline + 20 gives alpha_pad %.0f deg, which puts the 35 mm nail reach IN FRONT of the hairline (CONFLICTS #7)" % a_front)
    # nail reach: block +-17 mm plus pentagon R 18 = 35 mm from the pad axis, measured on the scalp
    reach, margin = 35.0, 15.0
    def scalp_pt(al, be):
        al, be = d(al), d(be)
        u = (-math.sin(al) * math.cos(be), math.sin(be), math.cos(al) * math.cos(be))
        x, y, z = u
        zz = v["HCZ"] if z >= 0 else 70.0
        r = 1 / math.sqrt((x / v["HA"]) ** 2 + (y / v["HBB"]) ** 2 + (z / zz) ** 2)
        return (x * r, y * r, z * r)
    hp_ = (xh, 0.0, zh)
    al = -60.0
    while al < 60:
        pc = scalp_pt(al, 0)
        if math.dist(pc, hp_) >= reach + margin:
            break
        al += 0.5
    print("  front stop for nail reach %.0f mm + %.0f mm margin behind the hairline: alpha_pad >= %.1f deg (set on the head, halo.md 9)" % (reach, margin, al))
    canal = (v["TRAG_X"], v["HBB"] * 0.94, -45.0)
    for be in (30, 35, 40, 45):
        dmin = min(math.dist(scalp_pt(a_, be), canal) for a_ in range(-30, 101, 5)) - reach
        print("  beta %d: nail reach to ear canal %.0f mm (red line 6 >= 25, C4 asks >= 25 with the halo moved 15 mm, so aim >= 40)" % (be, dmin))
    # ------------------------------------------------------------ cut list
    print("\n=== CARBON CUT LIST (cut 0.5 mm long, dress to fit) ===")
    print("  chords 8x6 tube: 6 x %.1f mm" % v["CHORD_CUT"])
    print("  legs   8x6 tube: 2 x %.1f mm" % v["LEG_CUT"])
    print("  exit stub 8x6 tube: 1 x 30 mm (right foot)")
    tube_total = 6 * v["CHORD_CUT"] + 2 * v["LEG_CUT"] + 30
    print("  tube total %.0f mm of 1000" % tube_total)
    # band length: elastica estimate = quarter-ellipse plus rise, plus pocket depth both ends
    ax_, by_ = v["X_NB"] + 0.7 - 56.0, v["Y_SIDE_IN"] - 2.25
    h = ((by_ - ax_) / (by_ + ax_)) ** 2
    q = math.pi * (by_ + ax_) * (1 + 3 * h / (10 + math.sqrt(4 - 3 * h))) / 4
    q = math.hypot(q, v["BAND_Z_FRONT"] - v["BAND_Z_SIDE"])
    band = 2 * (q + 28)
    print("  front band: 2 strips 10x1 x %.0f mm (cut %d, trim at the pockets)" % (band, int(band + 10)))
    print("  band bend strain at the forehead node: %.2f %% (pultruded carbon fails near 1.5 %%)" % (100 * 0.5 / v["R_NB"]))
    print("  track strip 10x1: 1 x %.0f mm (beta -%.1f..+%.1f)" % (v["STRIP_LEN"], v["STRIP_END"], v["STRIP_END"]))
    print("  guide rod 3 mm carbon: 1 x 100 mm")
    # ------------------------------------------------------------ notches
    Re = v["R_SI"] + v["STRIP_T"] / 2
    print("\n=== BETA NOTCHES on strip edge A (front edge), measured along the strip from the vertex-post centre, + toward the LEFT ear ===")
    print("  (carriage +x points to the RIGHT ear, plunger 16 mm right of the carriage centre)")
    for k in range(-4, 5):
        sk = Re * d(10 * k) - v["DET_X"] * Re / v["R_SI"]
        print("  beta %+3d deg: %+8.2f mm" % (10 * k, sk))
    print("  pitch %.2f mm" % (Re * d(10)))
    print("\n=== ALPHA DETENT NOTCHES (left hub plate) ===  notch k at theta = 15k + DELTA - 40 = alpha_pad 15k, k -3..7")
    # ------------------------------------------------------------ mass ledger
    rows = {}
    pt = os.path.join(HERE, "stl", "_part_table.csv")
    for r in csv.DictReader(open(pt)):
        rows[r["part"]] = float(r["mass_g_PA12"]) * int(r["qty"])
    small = v["HINGE_SIZE"] < 1.5
    if small:      # hub parts of the small-hinge variant
        for r in csv.DictReader(open(os.path.join(HERE, "stl", "variant_small_hinge", "_part_table.csv"))):
            rows[r["part"]] = float(r["mass_g_PA12"]) * int(r["qty"])
    hinge_g = 18.0 if small else 32.0
    tube_g = tube_total * 22.0 * 1.55e-3
    strip_g = v["STRIP_LEN"] * 10 * 1.55e-3
    band_g = 2 * band * 10 * 1.55e-3
    float_g = 15.0 if light else 96.0
    L = [  # (group, item, g, basis, (where for CoM): ('fix', (X,Y,Z)) or ('bail', r) or ('pad', dr) or ('float', rho))
        ("retention", "front band 2 strips 10x1 carbon, each %.0f mm" % band, band_g, "calc 1.55 g/cm3", ("fix", (75, 0, 25))),
        ("retention", "H13 forehead node + H14 trigger + foam", rows["H13_forehead_node"] + rows["H14_trigger_plate"] + 0.4, "CAD", ("fix", (v["X_NB"], 0, v["BAND_Z_FRONT"]))),
        ("retention", "head-present switch D2F-01FL + wire to the right hub", 1.5, "est", ("fix", (60, -40, 20))),
        ("retention", "dial cradle (UltAlt retention, bought)", 30.0, "est [VERIFY scale]", ("fix", (-85, 0, -30))),
        ("retention", "H15 cradle arms x2 + jaws x2", rows["H15L_cradle_arm"] + rows["H15R_cradle_arm"] + rows["H15b_cradle_jaw"], "CAD", ("fix", (-45, 0, -2))),
        ("retention", "temple pads 2 x 12 mm closed-cell foam", 1.8, "calc", ("fix", (0, 0, 0))),
        ("hub", "H01 hub plates L+R", rows["H01L_hub_plate"] + rows["H01R_hub_plate"], "CAD", ("fix", (0, 0, 0))),
        ("hub", ("E6-10-101-20 hinges x2 with push-on nuts" if small else "E6-10-301-20 hinges x2 + 8 x M4x10 + inserts"), hinge_g,
         ("Zygology 9 g each" if small else "est 14 g each + 4 g screws [VERIFY scale]"), ("fix", (0, 0, 0))),
        ("hub", "H04/H05 feet", rows["H04L_foot_left"] + rows["H05R_foot_right"], "CAD", ("bail", 12)),
        ("hub", "H06 alpha stops x2 + pins + M3", rows["H06_alpha_stop"] + 2.4, "CAD + est", ("fix", (0, 0, 20))),
        ("hub", "M4 ball plunger (alpha), brake cords + set screws x2", 1.0 + 1.2, "McMaster 85015A46 est", ("bail", 20)),
        ("bail", "carbon 8x6 tube, %.0f mm" % tube_total, tube_g, "calc 34 g/m", ("bail", 150)),
        ("bail", "H07 x4, H08a/b, H09 x2 nodes", rows["H07_chord_node"] + rows["H08a_vertex_half"] + rows["H08b_vertex_half"] + rows["H09L_shoulder_node"] + rows["H09R_shoulder_node"], "CAD", ("bail", 185)),
        ("bail", "track strip 10x1, %.0f mm" % v["STRIP_LEN"], strip_g, "calc", ("bail", v["R_SI"])),
        ("bail", "H11 beta stops x2 + M3", rows["H11_beta_stop"] + 1.6, "CAD", ("bail", 190)),
        ("bail", "H16 harness clips x6, H17 exit clamp + stub", rows["H16_harness_clip"] + rows["H17_exit_clamp"] + 0.8, "CAD", ("bail", 120)),
        ("bail", "epoxy (nodes, feet, strip, band)", 4.0, "est", ("bail", 150)),
        ("bail", "vertex splice M3 x2, misc M3 screws/nuts/inserts", 8.0, "est (use aluminium M3 to save 5 g)", ("bail", 100)),
        ("carriage", "H10 carriage + H10b spool", rows["H10_carriage"] + rows["H10b_spool"], "CAD", ("float", v["R_SI"] + 3)),
        ("carriage", "MR63ZZ x4, 3 mm pins x5, M4 plunger, O-ring cord, M3 set screw", 1.3 + 2.6 + 1.0 + 0.3 + 0.4, "est", ("float", v["R_SI"] + 3)),
        ("float", "Airpot Airpel E16D2.0N" if not light else "light float (Penrose sleeve in a PA12 bore) PROPOSED", float_g,
         "catalogue 64.6 + 15.8 x stroke" if not light else "est, CONFLICTS #1", ("float", (v["RHO_PLATE1"] + v["RHO_BODY1"]) / 2)),
        ("float", "QEV + float relief poppet on the float port", 8.0, "est [VERIFY parts]", ("float", v["RHO_BODY1"])),
        ("float", "H12 spider + 3 balls + 3 magnets + 10-32 nut", rows["H12_spider"] + 1.5 + 1.9 + 0.6, "CAD + est", ("float", v["RHO_SPIDER_TOP"] - 15)),
        ("float", "CF spring 9293K123 + 3 mm carbon guide rod", 2.3 + 1.1, "est", ("float", v["RHO_SPIDER_TOP"])),
        ("pad", "PAD work package (spec 4.8)", 81.5, "spec", ("pad", 40)),
        ("harness", "head-side harness on the bail (about 0.72 m at 43 g/m)", 31.0, "calc (spec 21; CONFLICTS #6)", ("bail", 170)),
        ("harness", "umbilical head share", 11.0, "spec", ("fix", (-20, -150, -10))),
        ("harness", "pogo lanyard half", 1.0, "est", ("fix", (0, -165, 0))),
    ]
    tot = sum(x[2] for x in L)
    print("\n=== MASS LEDGER BY PART (single pad%s) ===" % (", LIGHT FLOAT" if light else ""))
    grp = {}
    for g_, item, m, basis, _ in L:
        grp[g_] = grp.get(g_, 0) + m
        print("  %-9s %-62s %6.1f  %s" % (g_, item, m, basis))
    for g_, m in grp.items():
        print("  subtotal %-10s %6.1f" % (g_, m))
    print("  TOTAL HEAD-BORNE %.0f g   (spec 286 / gate B1-C2 <= 320 / red line 10 <= 500)" % tot)
    # ------------------------------------------------------------ CoM and lean
    def rskin(u):
        x, y, z = u
        zz = v["HCZ"] if z >= 0 else 70.0
        return 1 / math.sqrt((x / v["HA"]) ** 2 + (y / v["HBB"]) ** 2 + (z / zz) ** 2)

    def u_ab(al, be):
        al, be = d(al), d(be)
        return (-math.sin(al) * math.cos(be), math.sin(be), math.cos(al) * math.cos(be))

    def com(al, be):
        ab = al + v["DELTA"]
        m = 0.0
        sx = [0.0, 0.0, 0.0]
        rot = 0.0      # moment of the bail-borne group about the hub axis, upright head (g*mm, signed X arm)
        bail_m, bail_mx = 0.0, 0.0
        for g_, item, mm, basis, (kind, w) in L:
            if kind == "fix":
                pos = w
            elif kind == "bail":
                ub = u_ab(ab, 0)
                pos = tuple(ub[i] * w for i in range(3))
            elif kind == "float":
                uf = u_ab(al, be)
                pos = tuple(uf[i] * w for i in range(3))
            else:
                uf = u_ab(al, be)
                rs = rskin(uf)
                pos = tuple(uf[i] * (rs + w) for i in range(3))
            m += mm
            for i in range(3):
                sx[i] += mm * pos[i]
            if kind in ("bail", "float", "pad"):
                bail_m += mm
                bail_mx += mm * math.hypot(pos[0], pos[2])
        cm = [s_ / m for s_ in sx]
        mom = 9.81 * m / 1000 * math.hypot(cm[0], cm[1]) / 1000
        return m, cm, mom, bail_m, bail_mx

    print("\n=== CENTRE OF MASS AND LEAN (frame H, head upright) ===")
    worst = 0
    for pose in [(-25, 0), (0, 0), (45, 0), (90, 0), (100, 0), (0, 40), (0, -40)]:
        m, cm, mom, bm, bmx = com(*pose)
        worst = max(worst, mom)
        print("  pose alpha %+4d beta %+3d: CoM (%+5.0f, %+5.0f, %+5.0f) mm, gravity moment about O %.3f N.m" % (pose + tuple(cm) + (mom,)))
    print("  worst lean %.2f N.m against a cradle form lock of 1-1.5 N.m (margin %.1f-%.1f)" % (worst, 1 / worst, 1.5 / worst))
    # ------------------------------------------------------------ hinge torque
    m, cm, mom, bm, bmx = com(90, 0)
    t_grav = 9.81 * bmx / 1e6          # worst case: the bail-borne group's CoM horizontal from the hub axis
    t_scrub = 0.11
    need = t_grav + t_scrub
    e6_new = 0.248 if v["HINGE_SIZE"] < 1.5 else 0.79
    e6_worn = e6_new * 0.53     # Southco TD-E6-3-J: a 35 in-oz setting decays to ~19 in-oz by 5,000 cycles (re-tighten restores it)
    det = 4.0 * v["R_DET"] / 1000
    brake = 2 * 0.5 * 10.0 * (v["R_BRAKE0"] + v["R_BRAKE1"]) / 2 / 1000
    print("\n=== HINGE TORQUE CHECK (alpha) ===")
    print("  bail-borne mass %.0f g, sum m*r %.0f g.mm -> worst gravity torque %.3f N.m (+ scrub %.2f) = %.3f N.m" % (bm, bmx, t_grav, t_scrub, need))
    for lab, e6 in (("new", e6_new), ("after ~5k cycles", e6_worn)):
        for blab, br in (("brakes off", 0.0), ("brakes at 10 N", brake)):
            have = 2 * e6 + br + det
            print("  E6 %-17s %-15s: 2 x %.3f + brake %.3f + detent click %.3f = %.3f N.m -> margin %.2f %s" % (
                lab, blab, e6, br, det, have, have / need, "OK" if have / need >= 1.5 else ("LOW" if have / need >= 1.0 else "SLIPS")))
    # ------------------------------------------------------------ template
    svg(v)
    print("\nwrote bail_template.svg")


def svg(v):
    """1:1 bonding template in the bail plane: node centres, tube outlines, legs, hub points,
    strip post positions, notch ticks, 100 mm scale bar."""
    R = v["R_BAIL"]
    ch = v["CH_DEG"]
    W, H = 460, 300
    ox, oy = W / 2, 260          # O on the page
    P = lambda y, z: (ox + y, oy - z)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" width="%dmm" height="%dmm" viewBox="0 0 %d %d">' % (W, H, W, H),
           '<rect x="0" y="0" width="%d" height="%d" fill="white"/>' % (W, H),
           '<g fill="none" stroke="black" stroke-width="0.3">']
    nodes = [(R * math.sin(math.radians(k * ch)), R * math.cos(math.radians(k * ch))) for k in range(-3, 4)]
    for i in range(6):
        (y0, z0), (y1, z1) = nodes[i], nodes[i + 1]
        dx, dz = y1 - y0, z1 - z0
        L = math.hypot(dx, dz)
        nx, nz = -dz / L * 4, dx / L * 4
        for s in (-1, 1):
            a, b = P(y0 + s * nx, z0 + s * nz), P(y1 + s * nx, z1 + s * nz)
            out.append('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>' % (a + b))
    for s in (-1, 1):
        sh = (s * v["SH_Y"], v["SH_Z"])
        hub = (s * v["Y_HUB"], 0)
        a, b = P(*sh), P(*hub)
        out.append('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke-dasharray="3,2"/>' % (a + b))
        c = P(*hub)
        out.append('<circle cx="%.2f" cy="%.2f" r="3"/>' % c)
    for k, (y, z) in enumerate(nodes):
        c = P(y, z)
        out.append('<circle cx="%.2f" cy="%.2f" r="5.7"/><circle cx="%.2f" cy="%.2f" r="0.6" fill="black"/>' % (c + c))
        out.append('<text x="%.2f" y="%.2f" font-size="4" fill="black" stroke="none">N%+d (beta %+.1f)</text>' % (c[0] - 12, c[1] - 8, k - 3, (k - 3) * ch))
    # strip arc
    rs = v["R_SI"]
    a0, a1 = -v["STRIP_END"], v["STRIP_END"]
    pts = []
    for i in range(61):
        b = math.radians(a0 + (a1 - a0) * i / 60)
        pts.append("%.2f,%.2f" % P(rs * math.sin(b), rs * math.cos(b)))
    out.append('<polyline points="%s" stroke="blue"/>' % " ".join(pts))
    # notch ticks (beta) on the strip arc
    for k in range(-4, 5):
        b = math.radians(10 * k)
        a, bb = P(rs * math.sin(b), rs * math.cos(b)), P((rs + 6) * math.sin(b), (rs + 6) * math.cos(b))
        out.append('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="blue"/>' % (a + bb))
        t = P((rs + 8) * math.sin(b), (rs + 8) * math.cos(b))
        out.append('<text x="%.2f" y="%.2f" font-size="3.5" fill="blue" stroke="none">%+d</text>' % (t[0] - 3, t[1], 10 * k))
    c = P(0, 0)
    out.append('<circle cx="%.2f" cy="%.2f" r="1.5" fill="black"/><text x="%.2f" y="%.2f" font-size="4" fill="black" stroke="none">O (skull centre)</text>' % (c + (c[0] + 3, c[1])))
    out.append('<line x1="20" y1="290" x2="120" y2="290" stroke-width="0.8"/><text x="20" y="286" font-size="4" fill="black" stroke="none">100 mm: measure this before you trust the print</text>')
    out.append('<text x="10" y="12" font-size="5" fill="black" stroke="none">SP1 v3 HALO bail bonding template 1:1 (R_BAIL %.0f, chord %.2f c-c, tube cut %.2f, leg cut %.2f, hub Y %.1f). Lay nodes on the circles, tubes on the double lines.</text>' % (R, v["CHORD_C"], v["CHORD_CUT"], v["LEG_CUT"], v["Y_HUB"]))
    out.append("</g></svg>")
    open(os.path.join(HERE, "bail_template.svg"), "w").write("\n".join(out))


if __name__ == "__main__":
    main()
