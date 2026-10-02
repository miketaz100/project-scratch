"""
halo_parts.py - every printed SP1 v3 HALO part, written once (PROJECT SCRATCH / 14-build/halo/cad).

Each function takes the parameter namespace p (names of halo_params.scad, as E objects)
and returns a scadpy solid.  gen_halo_stl.py turns each into an STL and a .scad file.

Frames (README.md has pictures in words):
  HUB-LOCAL  x = X_H forward, y = Z_H up, z = |Y_H| outboard.  theta = angle from straight
             up, + toward the back:  direction(theta) = (-sin theta, cos theta).
             Right side installed = rotate([90,0,0]);  left side = mirror([0,1,0]) rotate([90,0,0]).
             Every hub part is drawn with the bail at alpha_bail = 0 (leg straight up).
  NODE       origin = node centre, x = along the bail toward +beta, y = n (lateral,
             + = side A = the float side = forward at alpha 0), z = radially out from O.
  CARRIAGE   x = along the track, y = n, z = radially out, z = 0 on the strip's inner face.
  SPIDER     pad frame P: x_P = track tangent, y_P = n, z_P = float axis (outward); z = 0 on top.
  FOREHEAD   head frame H (installed position).
"""
from scadpy import *


def th_dir(th, r=1.0):
    """hub-local point at radius r in direction theta"""
    return [-r * sin(th), r * cos(th)]


def sector(r0, r1, z0, z1, th0, th1, fn=96):
    """annular sector in hub-local, theta th0..th1 (th1 > th0), z0..z1"""
    return translate([0, 0, z0], rotate([0, 0, th0 + 90],
                     rotate_extrude([[r0, 0], [r1, 0], [r1, z1 - z0], [r0, z1 - z0]], angle=th1 - th0, fn=fn)))


def rr_profile(x0, x1, y0, y1, r, n=4):
    """2D rounded-rectangle point list (corner radius r, n segments per corner)"""
    import math as _m
    pts = []
    corners = [(x1 - r, y0 + r, -90), (x1 - r, y1 - r, 0), (x0 + r, y1 - r, 90), (x0 + r, y0 + r, 180)]
    for cx, cy, a0 in corners:
        for i in range(n + 1):
            a = _m.radians(a0 + 90.0 * i / n)
            pts.append([cx + r * _m.cos(a), cy + r * _m.sin(a)])
    return pts


def hexagon(af, h):
    """hex prism, across-flats af, height h, axis z, base at z=0"""
    return cylinder(h, r=af / sqrt(3) if isinstance(af, E) else af / 3 ** 0.5, fn=6)


# ===================================================================== HUB
def leaf_seat(p, th, side_sign, z0, z1):
    """Southco E6 leaf seat block on the side of the leaf away from the other leaf.
    side_sign = -1: block toward decreasing theta (boss); +1: toward increasing theta (foot).
    Returns (block, holes)."""
    # frame: x'' = toward the block side (normal), y'' = along the leaf (direction(theta))
    #   block side -1: x'' = (cos th, sin th) -> rotate(th);  y'' = direction(th)
    #   block side +1: x'' = (-cos th, -sin th) -> rotate(th + 180); y'' = -direction(th)
    yl0, yl1 = (2, p.R_LEAF + 1.75) if side_sign < 0 else (-(p.R_LEAF + 1.75), -2)
    ystud = p.HINGE_STUD_X if side_sign < 0 else -p.HINGE_STUD_X
    rot = th if side_sign < 0 else th + 180
    blk = rotate([0, 0, rot], box(p.HINGE_H, p.HINGE_H + p.HINGE_SEAT_T, yl0, yl1, z0, z1))
    zc = (p.Y_HINGE0 + p.Y_HINGE1) / 2
    holes = []
    for dz in (-1, 1):
        zz = zc + dz * p.HINGE_STUD_Y
        if V(p.HINGE_SIZE) < 1.5:      # small E6: moulded studs through, push-on nuts in counterbores
            holes.append(rotate([0, 0, rot], translate([p.HINGE_H - 1, ystud, zz], rotate([0, 90, 0],
                         cylinder(p.HINGE_SEAT_T + 2, r=p.HINGE_STUD_HOLE / 2, fn=24)))))
            holes.append(rotate([0, 0, rot], translate([p.HINGE_H + p.HINGE_PANEL, ystud, zz], rotate([0, 90, 0],
                         cylinder(p.HINGE_SEAT_T, r=p.HINGE_NUT_CB / 2, fn=32)))))
        else:                          # medium E6: M4 screws through the leaf into heat-set inserts
            holes.append(rotate([0, 0, rot], translate([p.HINGE_H - 0.01, ystud, zz], rotate([0, 90, 0],
                         cylinder(p.M4_INS_L + 0.01, r=p.M4_INS_D / 2, fn=24)))))
    return blk, holes


def ear_cut(p, z0, z1):
    return box(-60, 5, -70, p.EAR_CUT_Z, z0, z1)


def h02_hub_plate(p, side):
    """H01L (left) / H01R (right) HUB PLATE, hub-local: side plate and boss merged (CONFLICTS #5).
    Inboard face Y_SIDE_IN carries the temple pad; outboard face Y_F1 is the smooth brake track and
    (left) the alpha detent track; front-band pocket on an inboard boss; cradle-arm lug at the rear;
    boss leaf seat of the E6 hinge; (left) stop ring sectors with clamp slots and 10-deg pin holes."""
    z0 = p.Y_SIDE_IN
    zb = p.Y_F1
    zbs = p.BAND_Z_SIDE
    body = [translate([0, 0, z0], cylinder(p.SIDE_T, r=p.R_HUBDISC, fn=96)),
            box(26, 56, zbs - 12, zbs + 12, z0 - 5.5, z0 + 1),                    # band pocket boss (inboard)
            hull(translate([16, 3, z0], cylinder(p.STOP_RING_T, r=8)), box(30, 56, zbs - 12, zbs + 12, z0, z0 + 1)),
            box(-46, -22, -9.5, -2.5, z0, z0 + p.STOP_RING_T)]                    # cradle-arm lug
    if side == "L":
        body.append(sector(p.R_HUBDISC - 1, p.R_STOP1, z0, z0 + p.STOP_RING_T, p.STOP_FRONT0, p.STOP_FRONT1))
        body.append(sector(p.R_HUBDISC - 1, p.R_STOP1, z0, z0 + p.STOP_RING_T, p.STOP_REAR0, p.STOP_REAR1))
    blk, bholes = leaf_seat(p, p.TH_B, -1, z0, p.Y_HINGE1)
    body.append(blk)
    zm = z0 - 2.25
    cuts = [ear_cut(p, z0 - 7, zb + 0.5)] + bholes
    cuts.append(box(28, 56.1, zbs - 10.3, zbs + 10.3, zm - 0.7, zm + 0.7))         # band pocket, open at the front
    cuts.append(translate([51, zbs, z0 - 7], cylinder(10, r=p.M3_CLEAR / 2, fn=20)))  # one cross-bolt + epoxy (outside the stop ring)
    for xl in (-40, -29):
        cuts.append(translate([xl, -6, z0 - 0.01], cylinder(p.STOP_RING_T + 0.02, r=p.M3_INS_D / 2, fn=20)))
    if side == "L":
        a = p.NOTCH_D * sqrt(2)
        for k in range(-3, 8):
            th = 15 * k + p.DELTA + p.DET_ARM_OFF
            cuts.append(translate([0, 0, zb], rotate([0, 0, th + 90], translate([p.R_DET, 0, 0],
                        rotate([45, 0, 0], cube([4, a, a], center=True))))))
        for t0, t1 in ((p.STOP_FRONT0, p.STOP_FRONT1), (p.STOP_REAR0, p.STOP_REAR1)):
            cuts.append(sector(p.R_STOP_SLOT - 1.7, p.R_STOP_SLOT + 1.7, z0 - 1, z0 + p.STOP_RING_T + 1, t0 + 5, t1 - 5))
        for j in range(-10, 10):
            th = 10 * j
            if (V(p.STOP_FRONT0) + 4 <= th <= V(p.STOP_FRONT1) - 4) or (V(p.STOP_REAR0) + 4 <= th <= V(p.STOP_REAR1) - 4):
                q = th_dir(th, p.R_STOP_PIN)
                cuts.append(translate([q[0], q[1], z0 - 1], cylinder(p.STOP_RING_T + 2, r=1.55, fn=20)))
    return difference(union(body), cuts)


def h04_foot(p, side):
    """H04 (left) / H05 (right) leg foot, hub-local, drawn at alpha_bail = 0 (leg up).
    Rotates with the bail.  Foot leaf of the E6 hinge, the leg socket, the brake pad and
    (left) the detent plunger + stop tab arm; (right) the umbilical exit-stub socket."""
    zh0 = p.Y_HINGE0 + 0.5
    zc0 = p.Y_HINGE1 + 0.5
    zc1 = p.Y_HINGE1 + 4.5
    u = [0, p.LEG_DZ, p.LEG_DY]
    hub = [0, 0, p.Y_HUB]
    P = lambda t: [hub[0] + t * u[0], hub[1] + t * u[1], hub[2] + t * u[2]]
    ro = p.SOCK_D / 2 + p.SOCK_WALL
    blk, fholes = leaf_seat(p, p.FOOT_LEAF_OFF, +1, zh0, zc1)
    cap = hull(translate([0, 0, zc0], cylinder(zc1 - zc0, r=8)),
               rotate([0, 0, p.FOOT_LEAF_OFF + 180], box(p.HINGE_H, p.HINGE_H + p.HINGE_SEAT_T, -(p.R_LEAF + 1.75), -2, zc0, zc1)))
    sleeve = cyl_between(P(p.LEG_T0 - 2), P(p.LEG_T0 + p.SOCK_DEPTH), ro)
    neck = hull(translate([0, 0, zc0], cylinder(zc1 - zc0, r=8)), cyl_between(P(p.LEG_T0 - 2), P(p.LEG_T0 + 3), ro))
    # arm 40 deg ahead of the leg: brake pad (both), detent + stop tab (left)
    tha = p.DET_ARM_OFF
    za0 = p.Y_F1 + p.BOSS_T + 0.5
    za1 = za0 + 8
    r_out = p.R_STOP1
    arm = [rotate([0, 0, tha + 90], box(p.R_LEAFC + 0.5, r_out, -p.ARM_W / 2, p.ARM_W / 2, za0, za1))] if side == "L" else []
    if side == "L":
        arm.append(rotate([0, 0, tha + 90], box(p.R_STOP0 + 1.5, p.R_STOP1, -p.ARM_W / 2, p.ARM_W / 2,
                                                p.Y_SIDE_IN + p.STOP_RING_T + 0.5, za0 + 0.01)))
    bridge = sector(p.R_LEAFC, p.R_LEAFC + 6, za0, za1, tha - 5 if side == "L" else 5, 45)
    body = union(blk, cap, sleeve, neck, arm, bridge)
    cuts = list(fholes)
    cuts.append(cyl_between(P(p.LEG_T0), P(p.LEG_T0 + p.SOCK_DEPTH + 0.1), p.SOCK_D / 2))
    cuts.append(cyl_between(P(p.LEG_T0 + p.SOCK_DEPTH - 0.6), P(p.LEG_T0 + p.SOCK_DEPTH + 0.01), p.SOCK_D / 2,
                            r1=p.SOCK_D / 2 + 0.6))
    # knuckle clearance (hinge knuckle is on the axis up to Y_HINGE1)
    cuts.append(translate([0, 0, zh0 - 1], cylinder(p.Y_HINGE1 - zh0 + 1, r=p.HINGE_KNUCKLE_D / 2 + 0.4, fn=32)))
    # brake: NBR cord plug pressed by an M3 set screw onto the boss's smooth track
    qb = th_dir(p.BRAKE_TH, (p.R_BRAKE0 + p.R_BRAKE1) / 2)
    cuts.append(translate([qb[0], qb[1], za0 - 0.01], cylinder(5.01, r=1.75, fn=20)))
    cuts.append(translate([qb[0], qb[1], za1 - p.M3_INS_L], cylinder(p.M3_INS_L + 0.01, r=p.M3_INS_D / 2, fn=20)))
    cuts.append(translate([qb[0], qb[1], za0 + 4.9], cylinder(za1 - za0, r=1.7, fn=20)))
    if side == "L":
        qd = th_dir(tha, p.R_DET)
        cuts.append(translate([qd[0], qd[1], za1 - p.M4_INS_L], cylinder(p.M4_INS_L + 0.01, r=p.M4_INS_D / 2, fn=24)))
        cuts.append(translate([qd[0], qd[1], za0 - 0.01], cylinder(za1 - za0, r=2.1, fn=24)))
    else:
        # exit stub socket on the axis, outboard (8 x 6 carbon stub, bonded)
        zs0 = zc1 - 0.01
        body = union(body, translate([0, 0, zs0], cylinder(12, r=ro)))
        cuts.append(translate([0, 0, zs0 + 1], cylinder(11.1, r=p.SOCK_D / 2)))
    return difference(body, cuts)


def h06_alpha_stop(p):
    """H06 alpha stop block (x2, left boss).  Local: x radial (r), y tangential, z up from the
    ring face.  M3 insert from below on R_STOP_SLOT, pins on R_STOP_PIN at +-7.5 deg (5 deg steps)."""
    r0, r1 = p.R_STOP0 + 1, p.R_STOP1 - 1
    blk = linear_extrude(6, rr_profile(r0, r1, -7, 7, 1.2))
    cuts = [translate([p.R_STOP_SLOT, 0, -0.01], cylinder(p.M3_INS_L + 0.01, r=p.M3_INS_D / 2, fn=24))]
    for s in (-1, 1):
        cuts.append(translate([p.R_STOP_PIN * cos(7.5), s * p.R_STOP_PIN * sin(7.5), -0.01], cylinder(4.01, r=1.55, fn=20)))
    return difference(blk, cuts)


def h15_cradle_arm(p):
    """H15 cradle-arm adapter (L; R mirror), hub-local.  Bolts to the side-plate lug (2 x M3)
    and clamps the bike-retention side-arm tab behind and above the ear."""
    z0 = p.Y_SIDE_IN
    xc, yc = p.TRAG_X - 35, p.EAR_TOP_Z + 13
    zc = p.HBB * 0.89 + 6        # retention tab about 6 mm off the scalp behind the ear
    lugp = box(-46, -22, -9.5, -2.5, z0 - 3, z0)
    clamp = box(xc - 11, xc + 11, yc - 7, yc + 7, zc, zc + 3)
    arm = hull(box(-44, -24, -9, -3, z0 - 3, z0), box(xc - 6, xc + 6, yc - 6, yc + 6, zc, zc + 3))
    body = union(lugp, clamp, arm)
    cuts = []
    for xl in (-40, -29):
        cuts.append(translate([xl, -6, z0 - 4], cylinder(5, r=p.M3_CLEAR / 2, fn=20)))
    for dx in (-7, 7):
        cuts.append(translate([xc + dx, yc, zc - 1], cylinder(5, r=p.M3_CLEAR / 2, fn=20)))
    return difference(body, cuts)


def h15b_cradle_jaw(p):
    """H15b clamp jaw for the retention tab (x2).  22 x 14 x 3, two M3 holes 14 apart."""
    return difference(linear_extrude(3, rr_profile(-11, 11, -7, 7, 1.5)),
                      [translate([dx, 0, -1], cylinder(5, r=p.M3_CLEAR / 2, fn=20)) for dx in (-7, 7)])


# ===================================================================== BAIL NODES
def _socket(p, u, solid=True):
    ro = p.SOCK_D / 2 + p.SOCK_WALL
    L = p.SOCK_BOT + p.SOCK_DEPTH
    if solid:
        return cyl_between([0, 0, 0], [L * u[0], L * u[1], L * u[2]], ro)
    b0 = [p.SOCK_BOT * u[i] for i in range(3)]
    b1 = [(L + 0.1) * u[i] for i in range(3)]
    c0 = [(L - 0.6) * u[i] for i in range(3)]
    c1 = [(L + 0.01) * u[i] for i in range(3)]
    return [cyl_between(b0, b1, p.SOCK_D / 2), cyl_between(c0, c1, p.SOCK_D / 2, r1=p.SOCK_D / 2 + 0.6)]


def _post(p, x0, x1):
    """strip post on side B.  Node frame y = -n, so side B (back, +n negative) is +y here."""
    top = p.TUBE_OD / 2 + p.POST_H
    return hull(box(x0, x1, -p.POST_N1, -p.POST_N0, 2, top), box(x0 - 2, x1 + 2, -p.POST_N1, -p.POST_N0, 2, 4))


def h07_chord_node(p):
    """H07 chord node N1/N2 (x4, identical).  Two sockets at +-CH_DEG/2 and the strip post (side B)."""
    ch = p.CH_DEG / 2
    ua = [cos(ch), 0, -sin(ch)]
    ub = [-cos(ch), 0, -sin(ch)]
    ro = p.SOCK_D / 2 + p.SOCK_WALL
    body = union(_socket(p, ua), _socket(p, ub), sphere(ro, fn=32), _post(p, -p.POST_L / 2, p.POST_L / 2))
    return difference(body, _socket(p, ua, False), _socket(p, ub, False))


def h08_vertex_half(p, sgn):
    """H08a (sgn +1, toward +beta) / H08b (sgn -1) vertex node halves, bolted 2 x M3 (pad-2 splice, M18).
    H08b carries the harness anchor (zip-tie bar, side B)."""
    ch = p.CH_DEG / 2
    u = [sgn * cos(ch), 0, -sin(ch)]
    ro = p.SOCK_D / 2 + p.SOCK_WALL
    xs = (0, 3) if sgn > 0 else (-3, 0)
    half_ball = intersection(sphere(ro, fn=32), box(xs[0], xs[1], -10, 10, -10, 10) if sgn > 0 else box(-10, 0, -10, 10, -10, 10))
    if sgn > 0:
        half_ball = intersection(sphere(ro, fn=32), box(0, 10, -10, 10, -10, 10))
    flange = box(xs[0], xs[1], -12, 12, -6, 2)
    post = _post(p, 0, 4) if sgn > 0 else _post(p, -4, 0)
    post = intersection(post, box(0, 20, -20, 20, -5, 30) if sgn > 0 else box(-20, 0, -20, 20, -5, 30))
    parts = [_socket(p, u), half_ball, flange, post]
    if sgn < 0:
        parts.append(box(-8, -2, 9, 19, -6, -2))
    cuts = list(_socket(p, u, False))
    for yb in (-8.5, 8.5):
        cuts.append(translate([-4, yb, -2], rotate([0, 90, 0], cylinder(8, r=p.M3_CLEAR / 2, fn=20))))
        if sgn < 0:
            cuts.append(translate([-3.01, yb, -2], rotate([0, 90, 0], hexagon(p.M3_NUT_AF + 0.2, 2.5))))
    if sgn < 0:
        cuts.append(box(-6.5, -3.5, 12.5, 17.5, -6.1, -1.9))   # zip-tie window
    return difference(union(parts), cuts)


def h09_shoulder_node(p):
    """H09 shoulder node, LEFT (beta +62.1).  Right = mirror([1,0,0]).  Chord socket toward N2,
    leg socket toward the hub, zip-tie bar on side B for the harness."""
    ch = p.CH_DEG / 2
    u1 = [-cos(ch), 0, -sin(ch)]
    u2 = [p.SHL_X, 0, p.SHL_Z]
    ro = p.SOCK_D / 2 + p.SOCK_WALL
    tie = union(box(-3, 3, 5, 12, -6, -2), box(-3, 3, 11.9, 19, -6, -2))
    body = union(_socket(p, u1), _socket(p, u2), sphere(ro, fn=32), tie)
    return difference(body, _socket(p, u1, False), _socket(p, u2, False), box(-1.5, 1.5, 13, 18, -6.1, -1.9))


def h11_beta_stop(p):
    """H11 beta stop (x2): split collar on chord-3 tube + tower whose face (x = 0) meets the
    carriage cheek end.  Local: tube along x, z radially out, y = n."""
    ztop = p.R_SI + 12 - p.R_BAIL * cos(p.CH_DEG / 2)
    collar = rotate([0, 90, 0], cylinder(10, r=7, fn=40))
    ears = box(0, 10, -6, 6, 3, 9.5)
    tower = box(0, 4, 3, 10, 3, ztop)
    body = union(collar, ears, tower)
    cuts = [translate([-1, 0, 0], rotate([0, 90, 0], cylinder(12, r=4.05, fn=40))),
            box(-1, 11, -0.75, 0.75, 0, 9.6),
            translate([5, -7, 6.5], rotate([-90, 0, 0], cylinder(14, r=p.M3_CLEAR / 2, fn=20))),
            translate([5, -6.01, 6.5], rotate([-90, 0, 0], hexagon(p.M3_NUT_AF + 0.2, 2.5)))]
    return difference(body, cuts)


# ===================================================================== CARRIAGE + FLOAT
def float_pt(p, rho):
    return [0, rho * sin(p.DELTA), rho * cos(p.DELTA) - p.R_SI]


def h10_carriage(p):
    """H10 carriage.  Rides the 10 x 1 strip on 2 outer + 2 inner MR63 rollers, PTFE-taped lateral
    guide faces, M4 ball plunger into edge-A notches, O-ring friction pad + M3 set screw,
    Airpel nose plate, upper steady collar, anti-rotation guide lug, CF-spring spool fork,
    harness zip-tie anchor."""
    L2 = p.CAR_L / 2
    yc0 = p.STRIP_W / 2 + p.GUIDE_GAP
    yc1 = yc0 + p.CHEEK_T
    yl1 = -(p.STRIP_W / 2 + p.GUIDE_GAP)
    yl0 = yl1 - p.LIP_T
    cheek = box(-L2, L2, yc0, yc1, -9, 11)
    bridge = box(-L2, L2, yl0, yc1, 8, 11)
    lip = box(-L2, L2, yl0, yl1, -1.5, 11)
    # roller stations on the arc
    Ro = p.R_SI + p.STRIP_T + p.ROLL_D / 2
    Ri = p.R_SI - p.ROLL_D / 2
    ao = p.ROLL_S / (p.R_SI + p.STRIP_T) * 57.29578
    ai = p.ROLL_S / p.R_SI * 57.29578
    xo, zo = Ro * sin(ao), Ro * cos(ao) - p.R_SI
    xi, zi = Ri * sin(ai), Ri * cos(ai) - p.R_SI
    bos = []
    for s in (-1, 1):
        bos.append(translate([s * xo, yc0, zo], rotate([90, 0, 0], cylinder(yc0 - p.ROLL_W / 2 - 0.2, r=2.5, fn=24))))
        bos.append(translate([s * xo, yl1 + (yc0 - p.ROLL_W / 2 - 0.2), zo], rotate([90, 0, 0], cylinder(yc0 - p.ROLL_W / 2 - 0.2, r=2.5, fn=24))))
        bos.append(translate([s * xi, yc0, zi], rotate([90, 0, 0], cylinder(0.85, r=2.5, fn=24))))
    det = translate([p.DET_X, yc1 - 0.01, 0.5], rotate([-90, 0, 0], cylinder(5, r=4, fn=32)))
    oboss = translate([0, 0, 10.99], cylinder(6, r=4, fn=32))
    # Airpel nose plate, perpendicular to the float axis
    plate = translate([0, 0, -p.R_SI], rotate([-p.DELTA, 0, 0], translate([0, 0, p.RHO_PLATE0],
                      linear_extrude(p.AIR_PLATE_T, rr_profile(-13, 13, -16, 13, 3)))))
    plate = translate([0, -0.0, 0], plate)
    # steady collar (loose) and lugs, about 18-26 mm above the plate
    rc0, rc1 = p.RHO_PLATE1 + 18, p.RHO_PLATE1 + 26
    collar = translate([0, 0, -p.R_SI], rotate([-p.DELTA, 0, 0], translate([0, 0, rc0], cylinder(rc1 - rc0, r=13, fn=48))))
    guide = translate([0, 0, -p.R_SI], rotate([-p.DELTA, 0, 0], translate([-p.GUIDE_R, 0, rc0], cylinder(rc1 - rc0, r=3.5, fn=24))))
    fork = translate([0, 0, -p.R_SI], rotate([-p.DELTA, 0, 0], union(
        translate([0, 0, rc0], box(10.5, p.CF_X + 1, p.CF_W / 2 + 0.6, p.CF_W / 2 + 2.1, 0, rc1 - rc0 + 4)),
        translate([0, 0, rc0], box(10.5, p.CF_X + 1, -p.CF_W / 2 - 2.1, -p.CF_W / 2 - 0.6, 0, rc1 - rc0 + 4)))))
    web = box(-5, 5, 8, 13.5, 8, 17)
    anchor = box(-15, -4, yl0 - 6, yl0 + 0.01, 8, 11)
    body = union(cheek, bridge, lip, bos, det, oboss, plate, collar, guide, fork, web, anchor)
    cuts = []
    for s in (-1, 1):
        cuts.append(translate([s * xo, yc1 + 1, zo], rotate([90, 0, 0], cylinder(yc1 - yl0 + 2, r=1.45, fn=20))))
        cuts.append(translate([s * xi, yc1 + 1, zi], rotate([90, 0, 0], cylinder(yc1 - 3, r=1.45, fn=20))))
    cuts.append(translate([p.DET_X, yc1 + 5 - p.M4_INS_L, 0.5], rotate([-90, 0, 0], cylinder(p.M4_INS_L + 0.1, r=p.M4_INS_D / 2, fn=24))))
    cuts.append(translate([p.DET_X, yc0 - 0.1, 0.5], rotate([-90, 0, 0], cylinder(yc1 + 5, r=2.1, fn=24))))
    cuts.append(box(-5.2, 5.2, -1.7, 1.7, 1.2, 13))
    cuts.append(translate([0, 0, 17 - p.M3_INS_L], cylinder(p.M3_INS_L + 0.1, r=p.M3_INS_D / 2, fn=20)))
    cuts.append(translate([0, 0, 10], cylinder(8, r=1.7, fn=20)))
    # Airpel nose hole, collar bore, guide bore, spool pin
    cuts.append(translate([0, 0, -p.R_SI], rotate([-p.DELTA, 0, 0], translate([0, 0, p.RHO_PLATE0 - 1],
                cylinder(p.AIR_PLATE_T + 2, r=p.AIR_NOSE_D / 2 + 0.2, fn=40)))))
    cuts.append(translate([0, 0, -p.R_SI], rotate([-p.DELTA, 0, 0], translate([0, 0, rc0 - 1],
                cylinder(rc1 - rc0 + 2, r=p.AIR_OD / 2 + 0.4, fn=48)))))
    cuts.append(translate([0, 0, -p.R_SI], rotate([-p.DELTA, 0, 0], translate([-p.GUIDE_R, 0, rc0 - 1],
                cylinder(rc1 - rc0 + 2, r=p.GUIDE_D / 2 + 0.15, fn=20)))))
    cuts.append(translate([0, 0, -p.R_SI], rotate([-p.DELTA, 0, 0], translate([p.CF_X - p.CF_SPOOL_D / 2 - 0.3, 0, rc1 - 1],
                rotate([90, 0, 0], cylinder(20, r=1.5, center=True, fn=20))))))
    cuts.append(box(-12.5, -6.5, yl0 - 4.5, yl0 - 2.5, 7.9, 11.1))
    return difference(body, cuts)


def h10b_spool(p):
    """H10b spool sleeve for the constant-force spring coil, on a 3 mm pin."""
    return difference(cylinder(p.CF_W + 0.4, r=p.CF_SPOOL_D / 2 - 0.2, fn=40),
                      translate([0, 0, -1], cylinder(p.CF_W + 3, r=1.65, fn=20)))


def h12_spider(p):
    """H12 float spider (M8 ball side): hub on the Airpel 10-32 rod, 3 arms with 5 mm balls on
    R 55 and N52 6x3 magnets on R 42, guide-rod socket (-x) and CF-spring anchor (+x)."""
    t = p.SPIDER_ARM_T
    arms = []
    for a in (p.SPIDER_ANG0, p.SPIDER_ANG0 + 120, p.SPIDER_ANG0 + 240):
        c42 = [p.MAG_R * cos(a), p.MAG_R * sin(a), -t]
        c55 = [p.SPIDER_R * cos(a), p.SPIDER_R * sin(a), -t]
        arms.append(hull(translate([0, 0, -t], cylinder(t, r=3)), translate(c42, cylinder(t, r=4.3))))
        arms.append(hull(translate(c42, cylinder(t, r=4.3)), translate(c55, cylinder(t, r=3.6))))
    hub = translate([0, 0, -p.SPIDER_HUB_T], cylinder(p.SPIDER_HUB_T, r=p.SPIDER_HUB_D / 2))
    gsock = translate([-p.GUIDE_R, 0, -t], cylinder(t + 6, r=3.5, fn=32))
    garm = hull(translate([0, 0, -t], cylinder(t, r=3)), translate([-p.GUIDE_R, 0, -t], cylinder(t, r=3.5)))
    cfa = hull(translate([0, 0, -t], cylinder(t, r=3)), translate([p.CF_X, 0, -t], cylinder(t, r=4)))
    body = union(arms, hub, gsock, garm, cfa)
    cuts = [translate([0, 0, -p.SPIDER_HUB_T - 1], cylinder(p.SPIDER_HUB_T + 2, r=p.ROD_HOLE / 2, fn=24)),
            translate([0, 0, -p.SPIDER_HUB_T - 0.01], hexagon(p.ROD_NUT_AF, p.ROD_NUT_T + 0.01)),
            translate([-p.GUIDE_R, 0, -2], cylinder(8.1, r=p.GUIDE_D / 2 + 0.03, fn=20)),
            translate([p.CF_X, 0, -t - 1], cylinder(t + 2, r=1.1, fn=16))]
    for a in (p.SPIDER_ANG0, p.SPIDER_ANG0 + 120, p.SPIDER_ANG0 + 240):
        cuts.append(translate([p.SPIDER_R * cos(a), p.SPIDER_R * sin(a), -t - p.BALL_D / 2 + 2.05], sphere(p.BALL_D / 2 + 0.05, fn=24)))
        cuts.append(translate([p.MAG_R * cos(a), p.MAG_R * sin(a), -t - 0.01], cylinder(p.MAG_T + 0.11, r=p.MAG_D / 2 + 0.05, fn=24)))
    return difference(body, cuts)


# ===================================================================== FOREHEAD
def _arc_sector(p, r0, r1, z0, z1, half_len, rcen=None):
    rc = rcen if rcen is not None else p.R_NB
    a = half_len / rc * 57.29578
    return translate([p.X_NC, 0, 0], rotate([0, 0, -a], rotate_extrude(rr_profile(r0, r1, z0, z1, 0.9, 3), angle=2 * a, fn=72)))


def h13_forehead_node(p):
    """H13 forehead node, head frame H.  Holds the band (two 10 x 1 strips edge to edge) on the
    midline 45 mm above the brows; doff lip on top; pocket for the Omron D2F-01FL head-present
    switch below the band; guide holes for the trigger plate (H14)."""
    zf = p.BAND_Z_FRONT
    R = p.R_NB
    main = _arc_sector(p, R - 1.8, R + 2.6, zf - 12, zf + 12, p.NODE_HALF)
    low = _arc_sector(p, R - 1.8, R + 5.0, zf - 24, zf - 11, 14)
    lip = _arc_sector(p, R + 1.6, R + 13, zf + 9.5, zf + 12, 17)
    rim = _arc_sector(p, R + 10.5, R + 13, zf + 9.5, zf + 16, 17)
    body = union(main, low, lip, rim)
    a_slot = (p.NODE_HALF + 2) / R * 57.29578
    slot = translate([p.X_NC, 0, 0], rotate([0, 0, -a_slot], rotate_extrude(
        [[R, zf - 10.3], [R + 1.4, zf - 10.3], [R + 1.4, zf + 10.3], [R, zf + 10.3]], angle=2 * a_slot, fn=72)))
    sw = translate([p.X_NC + R - 1.81, -p.SW_L / 2, zf - 21.4], cube([p.SW_H + 0.01, p.SW_L, p.SW_W]))
    wire = translate([p.X_NC + R + 3, -1.5, zf - 21], cube([4, 3, 4]))
    cuts = [slot, sw, wire]
    for s in (-1, 1):
        cuts.append(translate([p.X_NC + R - 4, s * 10.5, zf - 18.5], rotate([0, 90, 0], cylinder(12, r=1.6, fn=20))))
    return difference(body, cuts)


def h14_trigger_plate(p):
    """H14 head-present trigger plate: rides on two 3 mm pins in front of the switch lever,
    1-2 mm of foam on its skin side stands proud of the forehead foam."""
    zf = p.BAND_Z_FRONT
    R = p.R_NB
    pl = _arc_sector(p, R - 5.3, R - 3.3, zf - 23, zf - 12, 13)
    cuts = [translate([p.X_NC + R - 7, s * 10.5, zf - 18.5], rotate([0, 90, 0], cylinder(4, r=1.45, fn=20))) for s in (-1, 1)]
    return difference(pl, cuts)


# ===================================================================== CLIPS, TOOLS
def h16_harness_clip(p):
    """H16 harness clip (x6): snaps on the 8 mm tube (opening toward the head), holds the
    11 mm umbilical bundle on side B at (n -12.5, +3.5).  Local: tube along x."""
    ring = rotate([0, 90, 0], difference(cylinder(8, r=5.5, fn=40), translate([0, 0, -1], cylinder(10, r=3.95, fn=40))))
    c = translate([0, -12.5, 3.5], rotate([0, 90, 0], difference(cylinder(8, r=7.3, fn=40), translate([0, 0, -1], cylinder(10, r=5.8, fn=40)))))
    web = box(0, 8, -7.0, -4.6, -1, 5)
    body = union(ring, c, web)
    cuts = [box(-1, 9, -3.1, 3.1, -7, -3.2),       # snap opening (toward the head)
            box(-1, 9, -24, -16, -0.5, 7.5)]       # bundle opening (outboard side B)
    return difference(body, cuts)


def h17_exit_clamp(p):
    """H17 umbilical exit clamp on the right foot's carbon stub (ear axis).  Local: stub along z.
    Bundle C-ring beside the stub; pocket for the 2-pin magnetic pogo (loop-wire lanyard)."""
    ro = p.SOCK_D / 2 + p.SOCK_WALL
    sl = cylinder(12, r=ro)
    c = translate([0, -12.5, 0], difference(cylinder(12, r=7.3, fn=40), translate([0, 0, -1], cylinder(14, r=5.8, fn=40))))
    web = box(-2.5, 2.5, -7, -4, 0, 12)
    pogo = box(-8, 8, 4.5, 11, 0, 12)
    body = union(sl, c, web, pogo)
    cuts = [translate([0, 0, -1], cylinder(11, r=p.SOCK_D / 2)),
            box(-4, 4, -24, -16, -1, 13),
            box(-6.7, 6.7, 5.3, 10.2, 6.5, 12.1)]          # pogo half, 13.4 x 4.9 x 5.5 [VERIFY part]
    return difference(body, cuts)


def h18a_umb_collar(p):
    """H18a bundle collar of the 3 N magnetic fuse: C-clamp on the 11 mm bundle (zip tie) with a
    pocket for a steel M5 x 15 fender washer."""
    return difference(union(cylinder(14, r=7.5, fn=40), translate([0, 6.5, 7], rotate([-90, 0, 0], cylinder(5, r=9, fn=48)))),
                      translate([0, 0, -1], cylinder(16, r=5.8, fn=40)),
                      box(-3.5, 3.5, -10, -4, -1, 15),
                      translate([0, 10.1, 7], rotate([-90, 0, 0], cylinder(1.5, r=7.7, fn=48))))


def h18b_umb_cup(p):
    """H18b hanger cup: 10 x 3 N52 magnet behind a 1.45 mm skin, shallow cone so it lets go in any
    direction at about 3 N; zip-tie lug to the drive-box hanger."""
    return difference(union(cylinder(6.2, r=9, fn=48), box(-4, 4, -13, -8, 0, 6.2)),
                      translate([0, 0, -0.01], cylinder(3.15, r=5.1, fn=40)),
                      translate([0, 0, 4.6], cylinder(2, r1=5, r2=9.5, fn=48)),
                      box(-2.5, 2.5, -12.5, -9.5, -1, 7))


def h19_zero_gauge(p):
    """H19 zero gauge: snaps on the Airpel body; its top platform is square to the float (pad)
    axis, so a phone inclinometer on it reads the pad axis tilt."""
    clip = difference(cylinder(14, r=p.AIR_OD / 2 + 2.2, fn=64),
                      translate([0, 0, -1], cylinder(16, r=p.AIR_OD / 2 + 0.15, fn=64)),
                      box(-9.6, 9.6, -20, -4, -1, 15))
    plat = translate([0, 0, 14], linear_extrude(3, rr_profile(-30, 30, -5, 45, 3)))
    plat = difference(plat, translate([0, 0, 13], cylinder(5, r=p.AIR_OD / 2 + 0.3, fn=64)), box(-9.6, 9.6, -20, 0, 13, 18))
    clip = difference(clip, box(-9.6, 9.6, -20, -4, -1, 15))
    return union(clip, plat)


def h20_notch_jig(p):
    """H20 notch jig: slides on the 10 x 1 strip (lying flat); pin hole indexes the previous notch,
    the file window 40.75 mm on sets the next one (pitch = (R_SI + 0.5) x 10 deg)."""
    pitch = (p.R_SI + p.STRIP_T / 2) * 10 / 57.29578
    blk = box(0, 70, -9, 9, 0, 8)
    cuts = [box(-1, 71, -(p.STRIP_W / 2 + 0.15), p.STRIP_W / 2 + 0.15, -1, p.STRIP_T + 0.2),
            box(60 - 1.5, 60 + 1.5, p.STRIP_W / 2 - 0.5, 10, -1, 9),
            translate([60 - pitch, 4, 0.5], rotate([-90, 0, 0], cylinder(8, r=1.3, fn=20)))]
    return difference(blk, cuts)


# ===================================================================== registry
def parts(p):
    """name -> (solid, frame, qty, print note)"""
    hubR = lambda s: rotate([90, 0, 0], s)
    hubL = lambda s: mirror([0, 1, 0], rotate([90, 0, 0], s))
    return {
        "H01L_hub_plate": (hubL(h02_hub_plate(p, "L")), "H", 1, "MJF PA12; print service OK (stops are adjustable)"),
        "H01R_hub_plate": (hubR(h02_hub_plate(p, "R")), "H", 1, "MJF PA12; print service OK"),
        "H04L_foot_left": (hubL(h04_foot(p, "L")), "H at alpha_bail 0", 1, "MJF PA12; print service OK"),
        "H05R_foot_right": (hubR(h04_foot(p, "R")), "H at alpha_bail 0", 1, "MJF PA12; print service OK"),
        "H06_alpha_stop": (h06_alpha_stop(p), "local", 2, "MJF PA12; print service OK"),
        "H07_chord_node": (h07_chord_node(p), "node", 4, "MJF PA12; print service OK"),
        "H08a_vertex_half": (h08_vertex_half(p, 1), "node", 1, "MJF PA12; print service OK"),
        "H08b_vertex_half": (h08_vertex_half(p, -1), "node", 1, "MJF PA12; print service OK"),
        "H09L_shoulder_node": (h09_shoulder_node(p), "node", 1, "MJF PA12; print service OK"),
        "H09R_shoulder_node": (mirror([1, 0, 0], h09_shoulder_node(p)), "node", 1, "MJF PA12; print service OK"),
        "H10_carriage": (h10_carriage(p), "carriage", 1, "MJF PA12; needs iteration (roller fit), home printer helps"),
        "H10b_spool": (h10b_spool(p), "local", 1, "MJF PA12 or PETG"),
        "H11_beta_stop": (h11_beta_stop(p), "local", 2, "MJF PA12; print service OK"),
        "H12_spider": (h12_spider(p), "spider", 1, "MJF PA12; print service OK"),
        "H13_forehead_node": (h13_forehead_node(p), "H", 1, "MJF PA12; needs one fit iteration (forehead curve)"),
        "H14_trigger_plate": (h14_trigger_plate(p), "H", 1, "MJF PA12 or PETG"),
        "H15L_cradle_arm": (hubL(h15_cradle_arm(p)), "H", 1, "PETG home print preferred (fit to the bought cradle)"),
        "H15R_cradle_arm": (hubR(h15_cradle_arm(p)), "H", 1, "PETG home print preferred (fit to the bought cradle)"),
        "H15b_cradle_jaw": (h15b_cradle_jaw(p), "local", 2, "any"),
        "H16_harness_clip": (h16_harness_clip(p), "local", 6, "MJF PA12 (snap needs nylon)"),
        "H17_exit_clamp": (h17_exit_clamp(p), "local", 1, "MJF PA12; print service OK"),
        "H18a_umb_collar": (h18a_umb_collar(p), "local", 1, "MJF PA12 or PETG"),
        "H18b_umb_cup": (h18b_umb_cup(p), "local", 1, "MJF PA12 or PETG"),
        "H19_zero_gauge": (h19_zero_gauge(p), "local", 1, "any (tool)"),
        "H20_notch_jig": (h20_notch_jig(p), "local", 1, "any (tool); PETG fine"),
    }
