import functools

file = "day21.in"

ans = 0
ans2 = 0

with open(file, "r") as f:
    string = f.read()
    lines = string.split("\n")

grid = tuple('''789
456
123
#0A'''.split("\n"))

grid2 = tuple('''#^A
<v>'''.split("\n"))

@functools.cache
def shortest_path(g, start, end, human, robots = None):
    # g - the current grid
    # start - starting cell
    # end - ending cell
    # human - keeps track of how many more directional robots stand between the humans input and the current robots input
    # robot - how many robots in total (only used for determining when we can't go to the far corner cause we'd fall off the pad)
    if robots == None:
        robots = human
    for x in range(len(g)):
        if start in g[x]:
            sx = x
            sy = g[x].index(start)
        if end in g[x]:
            ex = x
            ey = g[x].index(end)
    if sx > ex:
        vert = "^"*(sx-ex)
    else:
        vert = "v"*(ex-sx)
    if sy > ey:
        hor = "<"*(sy-ey)
    else:
        hor = ">"*(ey-sy)
    if human==0:
        return abs(sx-ex)+abs(sy-ey)+1

    # Other than the numpad robot which will press numbers,
    # the directional robots always finish their cycle by pressing button A,
    # so we can assume that they start there

    # Doesn't make sense to do some combo of horizontal/vertical movement
    # other than all horizontal first then all vertical or vice-verse
    a = "A"+vert+hor+"A"
    b = "A"+hor+vert+"A"

    acost = sum(shortest_path(grid2, a[x], a[x+1], human-1, robots) for x in range(len(a)-1))
    bcost = sum(shortest_path(grid2, b[x], b[x+1], human-1, robots) for x in range(len(b)-1))

    # Avoid falling off directional pad
    if hor == "<<" and human != robots:
        return acost
    
    # Avoid falling off numpad
    if hor == "<<" and human == robots and sx == len(g)-1:
        return acost

    return min(acost, bcost)

for line in lines:
    # Add A to beginning of line to simulate starting there
    line = "A"+line
    shortest2 = 0
    shortest25 = 0
    for i in range(len(line)-1):
        shortest2 += shortest_path(grid, line[i], line[i+1], 2)
        shortest25 += shortest_path(grid, line[i], line[i+1], 25)
    ans += int(line[1:-1])*shortest2
    ans2 += int(line[1:-1])*shortest25

print(ans, ans2)
