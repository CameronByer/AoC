import sys, copy

file = "day20.in"

ans = 0
ans2 = 0

with open(file, "r") as f:
    string = f.read()
    lines = string.split("\n")
    lines = [list(line) for line in lines]

for x in range(len(lines)):
    if 'S' in lines[x]:
        sx = x
        sy = lines[x].index('S')
    if 'E' in lines[x]:
        ex = x
        ey = lines[x].index('E')

print(sx, sy, ex, ey)

distances = {(sx, sy): 0}
new = {(sx, sy)}
while new:
    renew = set()
    for x, y in new:
        for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
            nx, ny = x+dx, y+dy
            if not (nx, ny) in distances and not lines[nx][ny]=="#":
                distances[(nx, ny)] = 99999
            if (nx, ny) in distances and 1 + distances[(x, y)] < distances[(nx, ny)]:
                distances[(nx, ny)] = 1 + distances[(x, y)]
                renew.add((nx, ny))
    new = renew

orig = distances[(ex, ey)]

for i in range(1, len(lines)-1):
    print(i)
    for j in range(1, len(lines[0])-1):
        grid = copy.deepcopy(lines)
        grid[i][j] = "."
        distances = {(sx, sy): 0}
        new = {(sx, sy)}
        while new:
            renew = set()
            for x, y in new:
                for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                    nx, ny = x+dx, y+dy
                    if not (nx, ny) in distances and not grid[nx][ny]=="#":
                        distances[(nx, ny)] = 99999
                    if (nx, ny) in distances and 1 + distances[(x, y)] < distances[(nx, ny)]:
                        distances[(nx, ny)] = 1 + distances[(x, y)]
                        renew.add((nx, ny))
            new = renew
    if orig-distances[(ex, ey)] <= 100:
        ans += 1

print(distances[(ex, ey)])

print(ans, ans2)
