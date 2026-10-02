import math, itertools, random
P=18.0
def grid(nx,ny,drop=()):
    pts=[]
    for i in range(nx):
        for j in range(ny):
            if (i,j) in drop: continue
            pts.append(((i-(nx-1)/2)*P,(j-(ny-1)/2)*P))
    return pts
L={}
L['4: 2x2 @18']=grid(2,2)
L['4: rhombus 18/31']=[(0,-15.6),(0,15.6),(-9,0),(9,0)]  # diamond 60deg
L['4: diamond (Y+centre) R20']=[(0,0)]+[(20*math.cos(a),20*math.sin(a)) for a in (math.pi/2,math.pi/2+2*math.pi/3,math.pi/2+4*math.pi/3)]
L['6: 2x3 @18']=grid(3,2)
L['6: brick 3+3 (offset 9)']=[(-18,-7.8),(0,-7.8),(18,-7.8),(-9,7.8),(9,7.8),(27,7.8)]
L['6: hex ring side 18']=[(18*math.cos(k*math.pi/3),18*math.sin(k*math.pi/3)) for k in range(6)]
L['6: triangle 1-2-3 @18']=[(0,15.6),(-9,0),(9,0),(-18,-15.6),(0,-15.6),(18,-15.6)]
L['6: centre+pentagon R18']=[(0,0)]+[(18*math.cos(k*2*math.pi/5),18*math.sin(k*2*math.pi/5)) for k in range(5)]
L['8: ring 3x3-centre @18']=grid(3,3,drop=((1,1),))
L['8: 4x2 @18']=grid(4,2)
L['12: 4x4-corners @18']=grid(4,4,drop=((0,0),(0,3),(3,0),(3,3)))
def rows(pts,psi):
    # heading psi; u perpendicular, v along heading
    c,s=math.cos(psi),math.sin(psi)
    proj=[(-x*s+y*c, x*c+y*s) for x,y in pts]
    best=1; nbest=0
    n=len(pts)
    for k in range(n,1,-1):
        cnt=0
        for comb in itertools.combinations(range(n),k):
            us=sorted(proj[i] for i in comb)
            gaps=[us[i+1][0]-us[i][0] for i in range(k-1)]
            vs=[q[1] for q in us]
            if all(14<=g<=28 for g in gaps) and max(vs)-min(vs)<=12:
                cnt+=1
        if cnt and best==1:
            best=k; nbest=cnt
    return best,nbest
def tracks(pts,psi,merge=3.0):
    c,s=math.cos(psi),math.sin(psi)
    us=sorted(-x*s+y*c for x,y in pts)
    t=1
    for i in range(1,len(us)):
        if us[i]-us[i-1]>merge: t+=1
    return t
def union_area(pts,r=15,n=60000):
    xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
    x0,x1=min(xs)-r,max(xs)+r; y0,y1=min(ys)-r,max(ys)+r
    random.seed(1); hit=0
    for _ in range(n):
        x=random.uniform(x0,x1); y=random.uniform(y0,y1)
        if any((x-a)**2+(y-b)**2<=r*r for a,b in pts): hit+=1
    return hit/n*(x1-x0)*(y1-y0)
def minspace(pts):
    return min(math.dist(a,b) for a,b in itertools.combinations(pts,2))
for name,pts in L.items():
    hs=[math.radians(d) for d in range(0,180,2)]
    rr=[rows(pts,h) for h in hs]
    r3=sum(1 for b,_ in rr if b>=3)/len(hs)
    r4=sum(1 for b,_ in rr if b>=4)/len(hs)
    r2=sum(1 for b,_ in rr if b>=2)/len(hs)
    tr=[tracks(pts,h) for h in hs]
    xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
    print(f"{name:28s} n={len(pts):2d} min={minspace(pts):5.1f} field={max(xs)-min(xs):.0f}x{max(ys)-min(ys):.0f} row>=2 {r2:4.0%} row>=3 {r3:4.0%} row>=4 {r4:4.0%} tracks(all down) mean {sum(tr)/len(tr):4.1f} min {min(tr)} reach(R15 disks) {union_area(pts)/100:5.0f} cm2")
