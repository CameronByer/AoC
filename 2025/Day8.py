import functools, copy

file_in = "Day8.in"

with open(file_in, "r") as f:
    string = f.read()
    lines = string.split("\n")

def dist(a, b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)**0.5

paired = set()

results = []

for box in range(len(lines)):
    x, y, z = [int(i) for i in lines[box].split(",")]
    for box2 in range(box+1, len(lines)):
        x2, y2, z2 = [int(i) for i in lines[box2].split(",")]
        d = dist((x, y, z), (x2, y2, z2))
        results.append((d, box, box2))

sorted_results = sorted(results, key=lambda x: x[0])

groups = []
rounds = 1000
round=0
for s in sorted_results:
    round += 1
    a, b = s[1], s[2]
    new = []
    merged = set((a, b))
    for g in groups:
        if a in g or b in g:
            merged = merged.union(g)
        else:
            new.append(g)
    new.append(merged)
    groups = new

    # Part 1
    if round == 1000:
        groups = sorted(groups, key=lambda x: len(x))
        ans = 1
        for g in groups[-3:]:
            ans *= len(g)

    # Part 2
    if len(groups[0])==len(lines):
        ans2 = int(lines[a].split(",")[0]) * int(lines[b].split(",")[0])
        break

print(ans)
print(ans2)