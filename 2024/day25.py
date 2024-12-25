file = "day25.in"

ans=0
ans2=0

with open(file, "r") as f:
    string = f.read()
    lines = string.split("\n\n")
    #nums = [[int(x) for x in line.split()] for line in lines]

locks = []
keys = []

for thing in lines:
    lock = thing[0] == "#"
    rows = thing.split("\n")
    counts = [0]*7
    for r in rows:
        for i in range(len(r)):
            counts[i] += r[i] == "#"
    if lock:
        locks.append(counts)
    else:
        keys.append(counts)

for l in locks:
    for k in keys:
        bad = False
        for i in range(len(l)):
            if l[i]+k[i] > 7:
                bad = True
        if not bad:
            ans += 1

print(ans, ans2)
