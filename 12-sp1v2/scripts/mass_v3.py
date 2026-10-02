# SP1 freeze v3 mass + CoM ledger (single pad), rerunnable. [EST] values, grams and mm in frame H.
import math
a,b,c=98.,77.,88.  # head ellipsoid semi-axes (X fwd, Y left, Z up), about O
def rskin(u):
    x,y,z=u
    zz = c if z>=0 else 70.
    return 1/math.sqrt((x/a)**2+(y/b)**2+(z/zz)**2)
def u_ab(al,be):
    al,be=math.radians(al),math.radians(be)
    v=(0,math.sin(be),math.cos(be))
    # R_Y(alpha): +alpha swings toward occiput (-X)
    return (-math.sin(al)*v[2], v[1], math.cos(al)*v[2])
static=[ # name, g, (X,Y,Z)
 ("carbon front band",8,(85,0,20)),("forehead pad",6,(92,0,15)),("dial cradle",30,(-85,0,-30)),
 ("temple pads",6,(40,0,0)),("doff lip/handle node",3,(90,0,30)),
 ("hub bosses+2 E6 hinges+detent",30,(0,0,0)),
 ("lanyard breakaway+head switch+clips",7,(-20,-80,0)),("fasteners/misc",10,(0,0,20)),
 ("pad-2 provisions",2,(0,-90,0)),("umbilical head share",11,(-20,-95,-10))]
pad,float_car,bail,harness=81.5,34.0,36.2,21.0
def com(al,be):
    m=0;s=[0,0,0]
    for n,g,p in static:
        m+=g; s=[s[i]+g*p[i] for i in range(3)]
    u=u_ab(al,be); r=rskin(u)
    for g,dr in ((pad,40),(float_car,105)):
        p=[u[i]*(r+dr) for i in range(3)]; m+=g; s=[s[i]+g*p[i] for i in range(3)]
    # bail: centroid ~ 0.62*210 along pad direction at beta=0 plane (approx)
    ub=u_ab(al,0); p=[ub[i]*130 for i in range(3)]; m+=bail; s=[s[i]+bail*p[i] for i in range(3)]
    p=[u[i]*150 for i in range(3)]; m+=harness; s=[s[i]+harness*p[i] for i in range(3)]
    cm=[s[i]/m for i in range(3)]
    mom=9.81*m/1000*math.hypot(cm[0],cm[1])/1000  # about O, upright head
    return m,cm,mom
for pose in [(-25,0),(0,0),(45,0),(90,0),(0,40),(0,-40)]:
    m,cm,mom=com(*pose)
    print(pose, round(m,1),"g CoM",[round(x) for x in cm],"moment %.3f N.m"%mom)
