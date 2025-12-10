import functools, copy

file_in = "Day10.in"

ans = 0
ans2 = 0

with open(file_in, "r") as f:
    string = f.read()
    lines = string.split("\n")

for line in lines:
    pieces = line.split()
    on = tuple(int(x) for x in pieces[0][1:-1].replace(".", "0").replace("#", "1"))
    buttons = [tuple(int(x) for x in button[1:-1].split(",")) for button in pieces[1:-1]]
    costs = tuple(int(x) for x in pieces[-1][1:-1].split(","))
    print(on)

    best = {on: 0}
    old = {}
    while old != best:
        old = copy.deepcopy(best)
        for o in old:
            for b in buttons:
                new = tuple((o[s]+(s in b))%2  for s in range(len(o)))
                if new in old:
                    best[new] = min(old[o] + 1, old[new])
                elif new in best:
                    best[new] = min(old[o] + 1, best[new])
                else:
                    best[new] = old[o] + 1
    print(best[tuple(0 for i in on)])
    print()
    ans += best[tuple(0 for i in on)]

print("--------")

for line in lines:
    pieces = line.split()
    on = tuple(int(x) for x in pieces[0][1:-1].replace(".", "0").replace("#", "1"))
    buttons = [tuple(int(x) for x in button[1:-1].split(",")) for button in pieces[1:-1]]
    costs = tuple(int(x) for x in pieces[-1][1:-1].split(","))
    print(on)

    best = {tuple(0 for i in on): 0}
    old = {}
    while True:
        old = {b:best[b] for b in best if all(b[i] <= costs[i] for i in range(len(b)))}
        best = {}
        for o in old:
            for b in buttons:
                new = tuple((o[s]+(s in b)) for s in range(len(o)))
                best[new] = old[o] + 1
        if costs in best:
            ans2 += best[costs]
            break
        print(len(best))
    print(best[costs])
    print()

print(ans)
print(ans2)