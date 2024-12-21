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

bdistances = {(ex, ey): 0}
new = {(ex, ey)}
while new:
   renew = set()
   for x, y in new:
       for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
           nx, ny = x+dx, y+dy
           if not (nx, ny) in bdistances and not lines[nx][ny]=="#":
               bdistances[(nx, ny)] = 99999
           if (nx, ny) in bdistances and 1 + bdistances[(x, y)] < bdistances[(nx, ny)]:
               bdistances[(nx, ny)] = 1 + bdistances[(x, y)]
               renew.add((nx, ny))
   new = renew

def mh(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

for d in distances:
   for bd in bdistances:
      if distances[d] + bdistances[bd] + mh(d, bd) <= orig - 100:
         if mh(d, bd) <= 2:
            ans += 1
         if mh(d, bd) <= 20:
            ans2 += 1

print(ans, ans2)

