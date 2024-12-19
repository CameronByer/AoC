ans = 0
ans2 = 0

fname = "day14.in"
#fname = "day14test.in"
with open(fname, "r") as f:
    raw = f.read()
    lines = raw.split("\n")
    #nums = [[int(x) for x in line.split()] for line in lines][0]

class Robot():

    def __init__(self, s):
        self.pos = [int(x) for x in line.split("=")[1].split()[0].split(",")]
        self.vel = [int(x) for x in line.split("=")[2].split()[0].split(",")]
    
    def move(self):
        self.pos[0] = (self.pos[0]+self.vel[0])%101
        self.pos[1] = (self.pos[1]+self.vel[1])%103

def display(robots, x, y):
    locs = {}
    for r in robots:
        if not tuple(r.pos) in locs:
            locs[tuple(r.pos)] = 0
        locs[tuple(r.pos)]+=1
    for i in range(x):
        for j in range(y):
            if (i, j) in locs:
                print(locs[(i, j)], end='')
            else:
                print('.', end='')
        print()


rs = []

for line in lines:
    rs.append(Robot(line))
'''
for i in range(100):
    for r in rs:
        r.move()

tl = tr = bl = br = 0

for r in rs:
    if r.pos[0]<50 and r.pos[1]<51:
        tl += 1
    if r.pos[0]>50 and r.pos[1]<51:
        tr += 1
    if r.pos[0]<50 and r.pos[1]>51:
        bl += 1
    if r.pos[0]>50 and r.pos[1]>51:
        br += 1

print(tl, tr, bl, br)
ans = tl*tr*bl*br
'''
it = 0
while True:
    it += 1
    for r in rs:
        r.move()
    if it%103 == 25 or it%101 == 66:
        display(rs, 101, 103)
        print(it)
        input()

print(ans, ans2)