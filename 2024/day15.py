import sys, copy

file = "day15.in"

ans=0
ans2=0

with open(file, "r") as f:
    string = f.read()
    lines = string.split("\n")
    #nums = [[int(x) for x in line.split()] for line in lines]

def supersize(grid):
    return grid.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")

string = supersize(string)

gri, moves = string.split("\n\n")
gri = gri.split("\n")


'''
class grid:

    def __init__(self, s):
        self.sx = len(s)
        self.sy = len(s[0])
        self.c = []
         
        for x in range(self.sx):
            self.c.append([])
            for y in range(self.sy):
                if s[x][y] == "@":
                    self.rx = x
                    self.ry = y
                self.c[-1].append(s[x][y])

    def move(self, di):
        dirs = {">":(0,1), "<":(0,-1), "^":(-1,0), "v":(1,0)}
        d = dirs[di]
        cx = self.rx
        cy = self.ry
        while self.c[cx][cy] != ".":
            cx += d[0]
            cy += d[1]
            if self.c[cx][cy] == "#":
                return
        while cx!=self.rx or cy!=self.ry:
            self.c[cx][cy] = "O"
            cx -= d[0]
            cy -= d[1]
        self.c[self.rx][self.ry] = "."
        self.rx += d[0]
        self.ry += d[1]        
        self.c[self.rx][self.ry] = "@"

    def dis(self):
        for row in self.c:
            print("".join(row))

    def score(self):
        t = 0
        for x in range(self.sx):
            for y in range(self.sy):
                if self.c[x][y] == "O":
                    print(x, y)
                    t += 100*x + y
        return t
'''

class grid:

    def __init__(self, s):
        self.sx = len(s)
        self.sy = len(s[0])
        self.c = []
         
        for x in range(self.sx):
            self.c.append([])
            for y in range(self.sy):
                if s[x][y] == "@":
                    self.rx = x
                    self.ry = y
                self.c[-1].append(s[x][y])

    def push(self, x, y, di, r = False):
        dirs = {">":(0,1), "<":(0,-1), "^":(-1,0), "v":(1,0)}
        d = dirs[di]
        dx, dy = d
        if self.c[x+dx][y+dy] == ".":
            self.c[x][y], self.c[x+dx][y+dy] = self.c[x+dx][y+dy], self.c[x][y]
            if r:
                self.rx += dx
                self.ry += dy
            return True
        elif self.c[x+dx][y+dy] == "#":
            return False
        elif dx == 0:
            if self.push(x+dx, y+dy, di):
                self.c[x][y], self.c[x+dx][y+dy] = self.c[x+dx][y+dy], self.c[x][y]
                if r:
                    self.rx += dx
                    self.ry += dy
                return True
        else:
            if self.c[x+dx][y+dy] == "[":
                if self.push(x+dx, y+dy, di) and self.push(x+dx, y+dy+1, di):
                    self.c[x][y], self.c[x+dx][y+dy] = self.c[x+dx][y+dy], self.c[x][y]
                    if r:
                        self.rx += dx
                        self.ry += dy
                    return True
                return False
            elif self.c[x+dx][y+dy] == "]":
                if self.push(x+dx, y+dy, di) and self.push(x+dx, y+dy-1, di):
                    self.c[x][y], self.c[x+dx][y+dy] = self.c[x+dx][y+dy], self.c[x][y]
                    if r:
                        self.rx += dx
                        self.ry += dy
                    return True
                return False

    def dis(self):
        for row in self.c:
            print("".join(row))

    def score(self):
        t = 0
        for x in range(self.sx):
            for y in range(self.sy):
                if self.c[x][y] == "[":
                    t += 100*x + y
        return t

g = grid(gri)
for m in moves.split("\n"):
    for n in m:
        old = copy.deepcopy(g)
        if not g.push(g.rx, g.ry, n, True):
            g = old

print(g.score())
            
