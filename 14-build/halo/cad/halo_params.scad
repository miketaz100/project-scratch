// =====================================================================
//  halo_params.scad  -  SP1 v3 HALO: the ONE place where numbers live
//  PROJECT SCRATCH / 14-build/halo/cad / HALO engineer / 2026-10-02 / mm, degrees
// ---------------------------------------------------------------------
//  1. Put Michael's tape-fit numbers in the TAPE FIT block (halo.md section 3
//     says how to take each one).  Everything below it is derived.
//  2. Every part file does  include <halo_params.scad>  and uses these names.
//  3. gen_halo_stl.py reads THIS file (every line "NAME = expression;") so the
//     STLs and the SCAD always agree.  Keep each assignment on one line and use
//     only + - * / ( ) [ ] , numbers, names and the functions
//     sin cos tan asin acos atan2 sqrt ceil floor max min abs (degrees, as SCAD).
//  [VERIFY] = a bought-part dimension to check with calipers on arrival.
// =====================================================================

// ---------------- TAPE FIT (defaults = SYSTEM-SPEC-v3 section 3.2 design head) ----------------
HC  = 575;     // head circumference, brow + widest back (dial cradle range is 500-620)
HL  = 196;     // head length: brow (glabella) to the furthest point at the back
HB  = 154;     // head breadth: widest, just above the ears
TV  = 133;     // ear canal (tragion) to the top of the head, vertical
OT  = 88;      // back of the head to the ear canal, horizontal
GH  = 35;      // brow (glabella) height above the ear canal
G2H = 60;      // brow to the front hairline, tape laid on the skin up the midline
EW  = 190;     // width across the OUTSIDES of both ears at the top of the ears
ET  = 30;      // top of the ear above the ear canal
IH  = 0;       // occipital bump (inion) height above (+) or below (-) the ear canal

// ---------------- head model in frame H (origin O, X fwd, Y left, Z up) ----------------
HA = HL / 2;                 // ellipsoid semi-axis X (front and back radius)
HBB = HB / 2;                // semi-axis Y
HCZ = TV - 45;               // semi-axis Z+ (O is 45 above the ear canal)
TRAG_X = -HA + OT;           // ear canal X (spec table: -10)
BROW_Z = GH - 45;            // glabella Z
EAR_TOP_Z = ET - 45;         // top of ear Z
EAR_OUT_Y = EW / 2;          // outer rim of the ear, |Y|
INION_Z = IH - 45;           // inion Z

// ---------------- hub stack along |Y| (halo.md section 4.2) ----------------
TEMPLE_PAD_T = 12;           // two layers of 6 mm closed-cell foam
SIDE_T = 4;                  // hub plate thickness (side plate and boss are ONE part; CONFLICTS #5)
Y_F1 = HBB + TEMPLE_PAD_T + 1 + SIDE_T;      // hub plate OUTBOARD face = detent/brake face (spec F1 was 95 inboard)
Y_SIDE_IN = Y_F1 - SIDE_T;                   // hub plate inboard face (temple pad glued here)
BOSS_T = 0;
Y_BOSS_OUT = Y_F1 + BOSS_T;                  // detent / brake face
HINGE_SIZE = 2;              // 1 = Southco E6-10-101-20 small (0.25 N.m, studs + push-on nuts; needs the light float)
                             // 2 = Southco E6-10-301-20 medium (0.8 N.m, 4 x M4 screws; needed with the 96 g Airpel)
HS = HINGE_SIZE - 1;         // 0 small, 1 medium (arithmetic switch so OpenSCAD and Python read the same file)
HINGE_L = 25.4 + HS * (42.9 - 25.4);         // leaf height along the pin [KNOWN catalogue e6-at p.400-401]
HINGE_OPEN_W = 30.5 + HS * (36.5 - 30.5);    // both leaves flat [KNOWN]
HINGE_KNUCKLE_D = 10.2 + HS * (12.7 - 10.2); // [small KNOWN drawing; medium VERIFY]
HINGE_LEAF_T = 3.0 + HS * 0.2;               // [VERIFY]
HINGE_H = 5.1 + HS * (6.35 - 5.1);           // pin axis to the leaf mounting face [small KNOWN; medium VERIFY with calipers]
HINGE_STUD_X = 10.15 + HS * (12.7 - 10.15);  // fastener distance from the pin axis [KNOWN: 20.3/2; 25.4/2]
HINGE_STUD_Y = 7.55 + HS * (15.9 - 7.55);    // fastener distance from the hinge centre along the pin [KNOWN: 15.1/2; 31.8/2]
HINGE_STUD_HOLE = 5.4;       // small: Southco panel hole for the moulded stud [KNOWN]
HINGE_NUT_CB = 12.0;         // small: counterbore for the supplied push-on nut (10 AF x 3) [KNOWN]
HINGE_PANEL = 4.0;           // small: seat thickness at the studs (Southco max 7.9)
HINGE_SEAT_T = 6.5 + HS * 1.5;               // leaf-seat block thickness (medium: M4 heat-set inserts)
R_LEAF = HINGE_OPEN_W / 2;   // leaf reach from the pin axis
R_LEAFC = sqrt(HINGE_H * HINGE_H + R_LEAF * R_LEAF) + 0.75;   // swept radius of a leaf corner + clearance
Y_HINGE0 = Y_BOSS_OUT;       // hinge starts on the boss face
Y_HINGE1 = Y_HINGE0 + HINGE_L;
Y_HUB = Y_HINGE1 + 4.6;      // bail plane = where the legs meet the ear axis (spec 120; see CONFLICTS #2)

// ---------------- hinge leaf clocking (theta from straight up, + toward the back) ----------------
TH_B = -70;                  // boss leaf direction (front, 20 deg above horizontal)
FOOT_LEAF_OFF = 0;           // foot leaf lies along the leg direction
DET_ARM_OFF = -40;           // detent ball / stop tab arm, 40 deg ahead of the leg
R_BRAKE0 = R_LEAFC + 0.75; R_BRAKE1 = R_LEAFC + 5.25;    // smooth friction-brake track on the hub plate face
BRAKE_TH = 25;               // brake pad station on the foot bridge (theta at alpha_bail 0)
R_DET = R_LEAFC + 8.75;      // detent ball track radius
R_HUBDISC = R_DET + 2.5;     // hub-plate disc radius
R_STOP0 = R_HUBDISC - 1;  R_STOP1 = R_STOP0 + 17;   // stop ring (left); the arm hits blocks at r >= R_STOP0 + 1.5
STOP_RING_T = 3;             // stop ring thickness (from the inboard face)
R_STOP_SLOT = R_STOP0 + 5;   // stop-block clamp screw arc
R_STOP_PIN = R_STOP0 + 12;   // stop-block pin-hole row (every 10 deg)
STOP_FRONT0 = -104; STOP_FRONT1 = -44;   // ring sectors (theta)
STOP_REAR0 = 44;   STOP_REAR1 = 96;
EAR_CUT_Z = EAR_TOP_Z + 5;   // no boss or side plate below this Z behind X = +5
M1_R = 24 / sqrt(3);         // M1: 3 x M3 on a 24 mm equilateral triangle (circumradius 13.86)
ARM_W = 10;                  // detent / stop / brake arm width
DET_PITCH = 15;              // alpha detent spacing

// ---------------- bail (carbon polygon, frame B) ----------------
CH_DEG = 20.7;               // chord angle (spec C24)
N_HALF = 3;                  // chords per side (6 total)
TUBE_OD = 8;  TUBE_ID = 6;   // pultruded carbon tube
SOCK_D = 8.25;               // node socket bore (epoxy gap 0.12)
SOCK_WALL = 1.4;
SOCK_DEPTH = 14;             // tube engagement (1.75 x OD)
SOCK_BOT = 4;                // socket bottom distance from node centre
PAD_STACK = 86;              // skin to float-spider top (PAD RCC ring 80 + balls + spider)
RETRACT = 25;                // pad retract the spec asks for at every pose
CLEAR = 3;                   // spider-to-tube clearance at full retract
R_BAIL_SPEC = 210;
R_BAIL = max(R_BAIL_SPEC, ceil((HA + PAD_STACK + RETRACT + CLEAR + TUBE_OD / 2) / cos(CH_DEG / 2)));
CHORD_C = 2 * R_BAIL * sin(CH_DEG / 2);      // node-centre to node-centre
CHORD_CUT = CHORD_C - 2 * SOCK_BOT;          // tube cut length (chords)
B_SHOULDER = N_HALF * CH_DEG;                // shoulder node angle (62.1)
SH_Y = R_BAIL * sin(B_SHOULDER);             // shoulder node, bail-plane coords
SH_Z = R_BAIL * cos(B_SHOULDER);
LEG_L = sqrt((SH_Y - Y_HUB) * (SH_Y - Y_HUB) + SH_Z * SH_Z);
LEG_DY = (SH_Y - Y_HUB) / LEG_L;             // leg unit vector (hub -> shoulder)
LEG_DZ = SH_Z / LEG_L;
LEG_T0 = 11;                 // leg socket bottom, distance from the hub point along the leg
LEG_CUT = LEG_L - LEG_T0 - SOCK_BOT;         // leg tube cut length

// ---------------- track strip and posts ----------------
POST_H = 9;                  // tube top to strip underside at a node
STRIP_W = 10;  STRIP_T = 1;  // pultruded carbon flat (spec 3 x 1; see CONFLICTS #3)
R_SI = R_BAIL + TUBE_OD / 2 + POST_H;        // strip inner face radius
POST_N0 = -4.5;  POST_N1 = -1.5;             // post lateral span (side B)
POST_L = 8;                                   // post length along the track
B_TRAVEL = 40;               // beta stops +-40
B_DET = 10;                  // beta detent spacing
STRIP_END = 45.5;            // strip runs -45.5 .. +45.5 deg
STRIP_LEN = 2 * (R_SI + STRIP_T / 2) * STRIP_END * 3.14159265 / 180;
NOTCH_D = 0.75;  NOTCH_W = 1.5;              // 90 deg V notch filed in strip edge A

// ---------------- carriage (local frame: x along track, y = n lateral, +n = side A = float side) ----------------
CAR_L = 48;                  // carriage length along the track
ROLL_D = 6;  ROLL_W = 2.5;   // MR63ZZ 3 x 6 x 2.5
ROLL_S = 20;                 // roller stations at +-20 along the strip
PIN_D = 3.0;                 // dowel pin
GUIDE_GAP = 0.3;             // strip edge to lateral guide face, before PTFE tape
CHEEK_T = 3.2;
LIP_T = 2.0;
BRIDGE_T = 3.0;
DET_X = 16;                  // beta plunger station along the carriage
FLOAT_N = 24;                // float axis lateral offset at r = R_SI
DELTA = atan2(FLOAT_N, R_SI);                // pad axis leads the bail plane by DELTA (CONFLICTS #4)
SHL_X = ((Y_HUB - SH_Y) * cos(B_SHOULDER) + SH_Z * sin(B_SHOULDER)) / LEG_L;   // leg direction in the shoulder node frame
SHL_Z = ((Y_HUB - SH_Y) * sin(B_SHOULDER) - SH_Z * cos(B_SHOULDER)) / LEG_L;

// ---------------- float (Airpot Airpel E16D2.0N, catalogue ACC-02M pp. 4, 8, 9) ----------------
AIR_OD = 20.6;               // body OD 0.812 in [KNOWN]
AIR_L = 107.4;               // nose end to rear end, 2.230 in + stroke [KNOWN; VERIFY whether it includes the nose]
AIR_NOSE_D = 11.11;          // nose thread 7/16-20 [KNOWN]
AIR_NOSE_L = 9.5;            // 0.375 in [KNOWN]
AIR_NUT_AF = 17.5;  AIR_NUT_T = 5.0;          // supplied 7/16-20 mounting nut [VERIFY]
AIR_ROD_D = 5.0;             // 0.197 in [KNOWN]
AIR_ROD_OUT = 17.8;          // rod beyond the nose end at full retract, 0.700 in [KNOWN]
AIR_ROD_THR_L = 11.4;        // 10-32 x 0.450 in male [KNOWN]
ROD_HOLE = 5.0;              // spider hole for the 10-32 rod thread
ROD_NUT_AF = 9.8;  ROD_NUT_T = 3.3;           // 10-32 hex nut pocket
STROKE = 50.8;
AIR_PLATE_T = 3;
RHO_SPIDER_TOP = R_BAIL * cos(CH_DEG / 2) - TUBE_OD / 2 - CLEAR;   // spider top at full retract, from O
RHO_NOSE = RHO_SPIDER_TOP + AIR_ROD_OUT - AIR_ROD_THR_L;          // nose end
RHO_PLATE1 = RHO_NOSE + AIR_NOSE_L;                                // body shoulder = top of the mount plate
RHO_PLATE0 = RHO_PLATE1 - AIR_PLATE_T;
RHO_BODY1 = RHO_NOSE + AIR_L;                                      // rear end of the Airpel
CF_SPOOL_D = 8.8;  CF_W = 6.35;              // McMaster 9293K123 (1.60 N) coil bore and width [VERIFY]

// ---------------- float spider (M8 ball side) ----------------
SPIDER_R = 55;               // ball circle radius (spec: Ø110)
BALL_D = 5;                  // chrome steel balls
MAG_D = 6;  MAG_T = 3;  MAG_R = 42;          // N52 discs, attract PAD steel discs
SPIDER_ARM_W = 6;  SPIDER_ARM_T = 3.2;
SPIDER_HUB_D = 16;  SPIDER_HUB_T = 7;
SPIDER_ANG0 = 30;            // arms at 30, 150, 270 deg in pad frame P (clear of tendon stops)
GUIDE_R = 15;                // anti-rotation rod offset along -x_P
CF_X = 20;                   // constant-force spring line offset along +x_P
GUIDE_D = 3.0;

// ---------------- front band, forehead node ----------------
BAND_W = 20;  BAND_T = 1;
BAND_Z_FRONT = BROW_Z + 45;  // band centre 45 above the brows (spec)
FOREHEAD_FOAM = 8;
BAND_FA = HA * sqrt(1 - (BAND_Z_FRONT / HCZ) * (BAND_Z_FRONT / HCZ));    // head section at band height
BAND_FB = HBB * sqrt(1 - (BAND_Z_FRONT / HCZ) * (BAND_Z_FRONT / HCZ));
R_NB = BAND_FB * BAND_FB / BAND_FA + FOREHEAD_FOAM + 2.5;   // band radius at the forehead node
X_NB = BAND_FA + FOREHEAD_FOAM + 2.5;                       // band inner face on the midline
X_NC = X_NB - R_NB;                                          // node arc centre
BAND_Z_SIDE = 4;             // band centre height at the side plates
NODE_HALF = 21;              // forehead node half-length along the band
SW_L = 12.8;  SW_W = 5.8;  SW_H = 6.5;       // Omron D2F-01FL body (0.25 N lever) [VERIFY]
SW_HOLE_P = 6.5;  SW_HOLE_D = 1.6;           // D2F mounting holes [VERIFY]

// ---------------- general ----------------
M3_CLEAR = 3.4;  M3_INS_D = 4.0;  M3_INS_L = 4.0;  M3_NUT_AF = 5.5;  M3_HEAD_D = 6.0;
M4_INS_D = 5.6;  M4_INS_L = 6.5;
FN = 48;
