import sys,copy

file = "day16.in"

ans=0
ans2=0

with open(file, "r") as f:
    string = f.read()
    lines = string.split("\n")
    #nums = [[int(x) for x in line.split()] for line in lines]

scores = {}

lx = len(lines)
ly = len(lines[0])

dirs = {">":(0,1), "<":(0,-1), "^":(-1,0), "v":(1,0)}

for x in range(lx):
    for y in range(ly):
        if lines[x][y] == "S":
            scores[(x, y, ">")] = (0, set([(x, y)]))
            scores[(x, y, "<")] = (0, set([(x, y)]))
            scores[(x, y, "^")] = (0, set([(x, y)]))
            scores[(x, y, "v")] = (0, set([(x, y)]))
            
new = set([s for s in scores])
while len(new) > 0:
    renew = set()
    for x, y, m in new:
        #print(x, y, m, scores[(x, y, m)])
        for d in dirs:
            dx, dy = dirs[d]
            if lines[x+dx][y+dy] in ".E":
                score = 1+scores[(x, y, m)][0]+1000*(m!=d)
                if not (x+dx, y+dy, d) in scores or score <= scores[(x+dx, y+dy, d)][0]:
                    renew.add((x+dx, y+dy, d))
                    spaces = copy.deepcopy(scores[(x, y, m)][1])
                    spaces.add((x+dx, y+dy))
                    if (x+dx, y+dy, d) in scores and score == scores[(x+dx, y+dy, d)][0]:
                        spaces.update(scores[(x+dx, y+dy, d)][1])
                    scores[(x+dx, y+dy, d)] = (score, spaces)
    new = renew
    #input()

for x in range(lx):
    for y in range(ly):
        if lines[x][y] == "E":
            for i in "><^v":
                if (x, y, i) in scores:
                    print(scores[(x, y, i)][0], len(scores[(x, y, i)][1]))
