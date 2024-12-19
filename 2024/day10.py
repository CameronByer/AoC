ans = 0
ans2 = 0

fname = "day10.in"
#fname = "day10test.in"
with open(fname, "r") as f:
    raw = f.read()
    lines = raw.split("\n")
    #nums = [[int(x) for x in line.split()] for line in lines]

def paths(grid, x, y):
    mvs = [(0,1), (1,0), (0,-1), (-1,0)]
    locs = set()
    locs.add((x, y))
    for i in range(1,10):
        newlocs = set()
        for l in locs:
            for m in mvs:
                nx, ny = l[0]+m[0],l[1]+m[1]
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == str(i):
                    newlocs.add((nx, ny))
        locs = newlocs
    return len(locs)

def paths2(grid, x, y):
    mvs = [(0,1), (1,0), (0,-1), (-1,0)]
    locs = []
    locs.append((x, y))
    for i in range(1,10):
        newlocs = []
        for l in locs:
            for m in mvs:
                nx, ny = l[0]+m[0],l[1]+m[1]
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == str(i):
                    newlocs.append((nx, ny))
        locs = newlocs
    return len(locs)

grid = lines

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == "0":
            ans += paths(grid, x, y)
            ans2 += paths2(grid, x, y)

print(ans, ans2)