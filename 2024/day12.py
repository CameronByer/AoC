ans = 0
ans2 = 0

fname = "day12.in"
#fname = "day12test.in"
with open(fname, "r") as f:
    raw = f.read()
    lines = raw.split("\n")
    #nums = [[int(x) for x in line.split()] for line in lines][0]

zones = {}

def get_zone(grid, x, y):
    plant = grid[x][y]
    cells = [(x, y)]
    more = True
    while more:
        more = False
        new_cells = []
        for cx, cy in cells:
            for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                x = cx + dx
                y = cy + dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    if grid[x][y] == plant and not (x, y) in cells and not (x, y) in new_cells:
                        new_cells.append((x, y))
                        more = True
        for cell in new_cells:
            cells.append(cell)
    return set(cells)

def super_zone(zone):
    fences = 0
    for z in zone:
        for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
            x = z[0]+dx
            y = z[1]+dy
            if not (x, y) in zone:
                fences += 1
    return fences

def cheap_fences(zone):
    fences = 0
    for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
        squares = set()
        for z in zone:
            x = z[0]+dx
            y = z[1]+dy
            if not (x, y) in zone:
                squares.add((x, y))
        fences += len(squares)
        dxr, dyr = dy, -dx
        for fx, fy in squares:       
            if (fx+dxr, fy+dyr) in squares:
                fences -= 1
    return fences

counted = set()

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if not (i, j) in counted:
            nz = get_zone(lines, i, j)
            zones[(i, j)] = nz
            counted.update(nz)

for z in zones:
    ans += len(zones[z]) * super_zone(zones[z])
    ans2 += len(zones[z]) * cheap_fences(zones[z])

print(ans, ans2)