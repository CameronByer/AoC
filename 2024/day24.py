import random

file = "day24.in"

with open(file, "r") as f:
    string = f.read()
    a, b = string.split("\n\n")

allout = set()

for line in b.split("\n"):
    x, o, y, _, out = line.split()
    allout.add(out)

desc = [0]*46
for m in allout:
    #desc = [0]*46
    for ii in range(10):
        ans=0
        ans2=0

        vals = {}

        def randomize():
            for v in vals:
                if v[0] in "xy":
                    vals[v] = random.randint(0, 1)

        for line in a.split("\n"):
            c = line.split(":")[0]
            v = int(line.split(":")[1])
            vals[c] = v

        #"z13":m, m:"z13"
        swaps = {"z07":"swt", "swt":"z07", "z13":"pqc", "pqc":"z13", "rjm":"wsv", "wsv":"rjm", "z31":"bgs", "bgs":"z31"}
        randomize()

        lines = b.split("\n")
        broken = False
        while lines != []:
            newlines = []
            for line in lines:
                x, o, y, _, out = line.split()
                if out in swaps:
                    out = swaps[out]
                match o:
                    case "AND":
                        o = "*"
                    case "OR":
                        o = " or "
                    case "XOR":
                        o = "^"
                try:
                    z = eval(str(vals[x])+o+str(vals[y]))
                    vals[out] = z
                except:
                    newlines.append(line)
            if lines == newlines:
                broken = True
                break
            lines = newlines
        if broken:
            break

        out = {}
        out["x"] = ["0"]*46
        out["y"] = ["0"]*46
        out["z"] = ["0"]*46
        for v in vals:
            if v[0] in "xyz":
                n = int(v[1:])
                ans += 2**n*vals[v]
                out[v[0]][n] = str(vals[v])

        x="".join(out["x"][::-1])
        y="".join(out["y"][::-1])
        z="".join(out["z"][::-1])

        xy = int(x, 2) + int(y, 2)
        difs = xy^int(z,2)
        t = bin(difs)[2:]
        for i in range(len(t)):
            desc[i] += int(t[-i-1])
        #print(bin(difs)[2:])
    if desc[31] == 0 and not broken:
        print(m)

print(desc)
#print(ans, ans2)

print(",".join(sorted(i for i in swaps)))