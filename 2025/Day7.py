import functools

file_in = "Day7.in"

ans = 0
ans2 = 0

with open(file_in, "r") as f:
    string = f.read()
    lines = string.split("\n")

initial = lines[0].index("S")

rays = {initial}

for line in lines:
    print(rays)
    newrays = set()
    for r in rays:
        if line[r] == "^":
            newrays.add(r-1)
            newrays.add(r+1)
            ans += 1
        else:
            newrays.add(r)
    rays = newrays

@functools.cache
def count(line, pos):
    if line >= len(lines):
        return 1
    if lines[line][pos] == "^":
        return count(line+1, pos-1) + count(line+1, pos+1)
    else:
        return count(line+1, pos)

ans2 = count(0, initial)

print(ans)
print(ans2)