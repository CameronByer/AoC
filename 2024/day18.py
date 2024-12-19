fname = "day18.in"
#fname = "day18test.in"
with open(fname, "r") as f:
    raw = f.read()
    lines = raw.split("\n")
    walls = [tuple(int(x) for x in line.split(",")) for line in lines]

print(len(walls))

end = (70, 70)
distances = {end: 0}
new = set([end])

corrupted = 1024
maxcorruption = len(walls)
mincorruption = 0

for i in range(15):
    corrupted = int((mincorruption+maxcorruption)/2)
    print(corrupted, walls[corrupted])
    end = (70, 70)
    distances = {end: 0}
    new = set([end])
    while new:
        renew = set()
        for x, y in new:
            for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                nx, ny = x+dx, y+dy
                if 0<=nx<=end[0] and 0<=ny<=end[1]:
                    if not (nx, ny) in distances and not (nx, ny) in walls[:corrupted]:
                        distances[(nx, ny)] = end[0]*end[1]
                    if (nx, ny) in distances and 1 + distances[(x, y)] < distances[(nx, ny)]:
                        distances[(nx, ny)] = 1 + distances[(x, y)]
                        renew.add((nx, ny))
        new = renew
    if not (0,0) in distances:
        maxcorruption = corrupted
    else:
        mincorruption = corrupted