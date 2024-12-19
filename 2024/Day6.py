import sys

file = "Day6.in"

ans=0
ans2=0

with open(file, "r") as f:
    string = f.read()
    lines = string.split("\n")
    #nums = [[int(x) for x in line.split()] for line in lines]

x = 0
for line in lines:
    if any(c in line for c in "<>^v"):
        break
    x += 1

y=0
for ch in line:
    if any(c == ch for c in "<>^v"):
        break
    y += 1

sx, sy = x, y

def rot(dx, dy):
    if dx == 0:
        return dy, 0
    return 0, -dx

def isbad(grid, c, d):
    visits = set()
    x, y = c
    dx, dy = d
    while 0<=x<len(grid) and 0<=y<len(grid[0]):
        if (x, y, dx, dy) in visits:
            return True
        visits.add((x, y, dx, dy))
        if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and grid[x+dx][y+dy] == "#":
            dx, dy = rot(dx, dy)
            visits.add((x, y, dx, dy))
            while grid[x+dx][y+dy] == "#":
                dx, dy = rot(dx, dy)
                visits.add((x, y, dx, dy))
        x+=dx
        y+=dy
    return False

pos = set()
bads = set()
pos.add((x, y))

dx = -1
dy = 0
while 0<=x<len(lines) and 0<=y<len(lines[0]):
    pos.add((x, y))
    if 0<=x+dx<len(lines) and 0<=y+dy<len(lines[0]):
        if lines[x+dx][y+dy] == "#":
            while lines[x+dx][y+dy] == "#":
                dx, dy = rot(dx, dy)
    x+=dx
    y+=dy

for i, j in pos:
    if (i, j) != (sx, sy):
        newgrid=lines[:i]+[lines[i][:j]+"#"+lines[i][j+1:]]+lines[i+1:]
        if isbad(newgrid, (sx, sy), (-1, 0)):
            bads.add((i, j))
    
print(len(pos), len(bads))
