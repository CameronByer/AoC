file = "day23.in"

ans=0
ans2=0

with open(file, "r") as f:
    string = f.read()
    lines = string.split("\n")

conns = set()
network = {}

def add(a, b):
    if not a in network:
        network[a] = set()
    if not b in network:
        network[b] = set()
    network[a].add(b)
    network[b].add(a)
    conns.add(a)
    conns.add(b)

for line in lines:
    a,b = line.split("-")
    add(a, b)

def part1():
    total = 0
    for a in conns:
        for b in conns:
            for c in conns:
                if a.startswith("t") or b.startswith("t") or c.startswith("t"):
                    if a in network[b] and a in network[c] and b in network[c]:
                        total += 1
    return total//6

def part2():
    groups = []
    for conn in conns:
        for group in groups:
            if all(conn in network[c] for c in group):
                group.append(conn)
        groups.append([conn])
    return ",".join(sorted(max(groups, key=len)))

ans = part1()
ans2 = part2()

print(ans, ans2)
