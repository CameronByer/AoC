from math import lcm

ans = 0
ans2 = 0

fname = "day13.in"
#fname = "day13test.in"
with open(fname, "r") as f:
    raw = f.read()
    lines = raw.split("\n")
    #nums = [[int(x) for x in line.split()] for line in lines][0]

def cost(ax, ay, bx, by, cx, cy):
    if cx/cy > ax/ay and cx/cy > bx/by:
        return 0
    if cx/cy < ax/ay and cx/cy < bx/by:
        return 0
    difa = abs(ax-ay)
    difb = abs(bx-by)
    if difb != 0:
        mindif = abs(lcm(difa, difb))
        apress = mindif//difa
        bpress = mindif//difb
    else:
        mindif = bx
        apress = 0
        bpress = max(ax, ay)
    shave = ax*apress+bx*bpress
    presses = (min(cx, cy)//shave)
    costper = 3*apress + bpress
    bonus = presses*costper
    cx -= ax*apress*presses + bx*bpress*presses
    cy -= ay*apress*presses + by*bpress*presses

    b = cy//by + (apress+1000)*(bpress+1000)
    a = 0
    while (a*ax+b*bx)!=cx or (b*by + a*ay)!=cy:
        #print(a, b, ax, ay, bx, by, a*ax+b*bx, a*ay+b*by, cx, cy, apress, bpress)
        while (b*by + a*ay) < cy:
            a += 1
        if (a*ax+b*bx)==cx and (b*by + a*ay)==cy:
            break
        b -= 1
        if b < -(apress+1000)*(bpress+1000):
            return 0
    #print(a, b, apress, bpress, presses, ax, ay, bx, by)
    totala = a+apress*presses
    totalb = b+bpress*presses
    #print(totala, totalb, totala*ax+totalb*bx, totala*ay+totalb*by)
    return 3*a+b+bonus

def cost2(ax, ay, bx, by, cx, cy):
    # a*ax+b*bx=cx -> a = (cx-b*bx)/ax
    # a*ay+b*by=cy -> (cx-b*bx)/ax*ay+b*by=cy -> cx*ay-b*bx*ay+b*by*ax=cy*ax -> b*(by*ax-bx*ay)=cy*ax-cx*ay -> b=(cy*ax-cx*ay)/(by*ax-bx*ay)
    a = (cy*bx-cx*by)//(ay*bx-ax*by)
    b = (cy*ax-cx*ay)//(by*ax-bx*ay)
    if a*ax+b*bx == cx and a*ay+b*by == cy:
        return 3*a+b
    return 0

for i in range(0, len(lines), 4):
    a = lines[i]
    ax = int(a.split("X+")[1].split(",")[0])
    ay = int(a.split("Y+")[1])
    b = lines[i+1]
    bx = int(b.split("X+")[1].split(",")[0])
    by = int(b.split("Y+")[1])
    c = lines[i+2]
    cx = int(c.split("X=")[1].split(",")[0]) + 10000000000000
    cy = int(c.split("Y=")[1]) + 10000000000000
    ans += cost2(ax, ay, bx, by, cx, cy)

print(ans, ans2)