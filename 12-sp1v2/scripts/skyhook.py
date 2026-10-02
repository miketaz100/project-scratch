# Leap-4 C1 SKYHOOK: residual moment about O when a room-fixed constant-force line lifts the carriage.
# Frame H (spec §3): X fwd, Y left, Z up; u(a,b) = (-sin a cos b, sin b, cos a cos b), +a toward occiput.
import math, itertools
import numpy as np
A,Bx,C = 98.,77.,88.
def rskin(u):
    return 1/math.sqrt((u[0]/A)**2+(u[1]/Bx)**2+(u[2]/C)**2)
def u_of(a,b):
    a,b=math.radians(a),math.radians(b)
    return np.array([-math.sin(a)*math.cos(b), math.sin(b), math.cos(a)*math.cos(b)])
def Rot(pitch,yaw):   # head pose: pitch + = nose down (rotation about Y), then yaw about Z
    p,y=math.radians(pitch),math.radians(yaw)
    Ry=np.array([[math.cos(p),0,math.sin(p)],[0,1,0],[-math.sin(p),0,math.cos(p)]])
    Rz=np.array([[math.cos(y),-math.sin(y),0],[math.sin(y),math.cos(y),0],[0,0,1]])
    return Rz@Ry
NECK=np.array([-10.,0,-80.])
g=9.81e-3   # N per g
m_pad, m_fc, R_CAR = 70., 29., 210.
def bail_com(a, m_bail):
    # arc beta ±62 at R210 (454 mm) + legs to hubs (236 mm): CoM 129 mm along the bail's 'up' in its plane
    a=math.radians(a); return m_bail, np.array([-math.sin(a)*129,0,math.cos(a)*129])
def moments(a,b,pitch,yaw,W,F,m_bail,reel=True):
    Rt=Rot(pitch,yaw); O=NECK+Rt@(-NECK)            # O in world
    u=u_of(a,b); rs=rskin(u)
    pts=[(m_pad, u*(rs+40)), (m_fc, u*(rs+105))]
    mb,cb=bail_com(a,m_bail); pts.append((mb,cb))
    M=np.zeros(3)
    for m,p in pts:
        pw=O+Rt@p; M+=np.cross(pw-O, np.array([0,0,-m*g]))
    car=O+Rt@(u*R_CAR)
    clear=1e9
    if reel:
        d=W-car; L=np.linalg.norm(d); f=F*d/L
        M+=np.cross(car-O,f)
        for t in np.linspace(0.05,1,40):   # line clearance from O (must stay outside bail shell R 215)
            clear=min(clear,np.linalg.norm(car+t*d-O))
        hz=math.degrees(math.acos(d[2]/L))
    else: hz=0
    return np.linalg.norm(M[:2]), abs(M[2]), clear, (np.linalg.norm(W-car) if reel else 0)
poses=[(a,b) for a in range(-25,101,5) for b in range(-40,41,5)]   # RT2 β stops ±40
for W in (np.array([-80.,0,420.]), np.array([-150.,0,380.]), np.array([-60.,0,500.])):
  for Fg in (99., 99+36*129/210):
    F=Fg*g
    print(f"\nhanger {W}, reel force {Fg:.0f} gf")
    for pitch,yaw,label in ((0,0,'upright'),(20,0,'20° nod fwd'),(-20,0,'20° recline'),(0,45,'45° turn'),(15,30,'15° nod+30° turn')):
        worst=max(poses,key=lambda p:moments(p[0],p[1],pitch,yaw,W,F,36)[0])
        mh,mz,cl,L=moments(*worst,pitch,yaw,W,F,36)
        base=max(moments(a,b,pitch,yaw,W,F,58,reel=False)[0] for a,b in poses)
        clmin=min(moments(a,b,pitch,yaw,W,F,36)[2] for a,b in poses)
        Ls=[moments(a,b,pitch,yaw,W,F,36)[3] for a,b in poses]
        print(f"  {label:18s} worst pitch/roll {mh:.3f} N·m at {worst} (baseline no reel {base:.3f}); yaw {mz:.3f}; min line clearance {clmin:.0f} mm; line length {min(Ls):.0f}-{max(Ls):.0f}")

# --- scan hanger position and reel force for the best worst-case (all poses x head moves) ---
print("\nSCAN (N·m, worst over poses and 5 head moves)")
moves=((0,0),(20,0),(-20,0),(0,45),(15,30),(0,-45))
best=[]
for x in (-60,-30,-10,20):
  for z in (420,500,600,700):
    for Fg in (50,70,85,99):
      W=np.array([float(x),0,float(z)]); F=Fg*g
      w=max(moments(a,b,p,y,W,F,36)[0] for a,b in poses[::3] for p,y in moves)
      best.append((w,x,z,Fg))
best.sort()
for r in best[:8]: print("  worst %.3f N·m  hanger x=%d z=%d  F=%d gf"%(r[0]/1000,r[1],r[2],r[3]))
w0=max(moments(a,b,p,y,np.zeros(3),0,58,reel=False)[0] for a,b in poses[::3] for p,y in moves)
print("  baseline (no reel, Al bail) worst %.3f"%(w0/1000))
w1=max(moments(a,b,p,y,np.zeros(3),0,36,reel=False)[0] for a,b in poses[::3] for p,y in moves)
print("  feather bail, no reel worst %.3f"%(w1/1000))
# tug from a stand-up / lean of 150 mm forward: line angle change and horizontal pull

print("\nATTACH POST on the carriage (line anchor at R_attach), hanger (-10,0,600), F=85 gf")
for Ra in (210,240,260):
    R_CAR=Ra
    W=np.array([-10.,0,600.]); F=85*g
    w=max(moments(a,b,p,y,W,F,36)[0] for a,b in poses for p,y in moves)
    cl=min(moments(a,b,p,y,W,F,36)[2] for a,b in poses for p,y in moves)
    yz=max(moments(a,b,p,y,W,F,36)[1] for a,b in poses for p,y in moves)
    Ls=[moments(a,b,p,y,W,F,36)[3] for a,b in poses for p,y in moves]
    print(f"  R_attach {Ra}: worst pitch/roll {w/1000:.3f} N·m, worst yaw {yz/1000:.3f}, min line radius from O {cl:.0f} mm (bail shell 215), line length {min(Ls):.0f}-{max(Ls):.0f} mm")

print("\nLINE vs BAIL contact check (min distance line<->bail tube centreline, excluding 40 mm round the carriage)")
def bail_pts(a):
    pts=[]
    for b in np.linspace(-62,62,125): pts.append(u_of(a,b)*210)
    e=u_of(a,62)*210; h=np.array([0,120.,0])
    for t in np.linspace(0,1,30): pts.append(e+(h-e)*t); pts.append(np.array([1,-1,1])*(e+(h-e)*t))
    return pts
def line_bail(a,b,p,y,W,Ra):
    Rt=Rot(p,y); O=NECK+Rt@(-NECK); car=O+Rt@(u_of(a,b)*Ra); d=W-car
    best=1e9
    for q in bail_pts(a):
        qw=O+Rt@q
        if np.linalg.norm(qw-(O+Rt@(u_of(a,b)*210)))<40: continue
        t=max(0,min(1,np.dot(qw-car,d)/np.dot(d,d)))
        best=min(best,np.linalg.norm(car+t*d-qw))
    return best
W=np.array([-10.,0,600.])
for Ra in (210,240):
    bad=[(a,b,p,y) for a,b in poses[::2] for p,y in moves if line_bail(a,b,p,y,W,Ra)<8]
    print(f"  R_attach {Ra}: poses with line within 8 mm of bail: {len(bad)} of {len(poses[::2])*len(moves)}; e.g. {bad[:4]}")
