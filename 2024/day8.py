ans = 0
ans2 = 0

fname = "day8.in"
#fname = "day8test.in"
with open(fname, "r") as f:
    raw = f.read()
    lines = raw.split("\n")
    #nums = [[int(x) for x in line.split()] for line in lines]

def ingrid(grid, x, y):
    return x>=0 and y>=0 and x<len(grid) and y<len(grid[0])

sigs = {}

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j]!=".":
            c = lines[i][j]
            if not c in sigs:
                sigs[c] = set()
            sigs[c].add((i, j))

total=set()

for _, sig in sigs.items():
    anti = set()
    for a in sig:
        for b in sig:
            if a!=b:
                ax, ay = a
                bx, by = b
                difx = ax-bx
                dify = ay-by
                for i in range(len(lines)):
                    c = (ax+i*difx, ay+i*dify)
                    if ingrid(lines, c[0], c[1]):
                        anti.add(c)
    total.update(anti)

ans = len(total)
                

print(ans, ans2)