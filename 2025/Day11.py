import functools, copy

file_in = "Day11.in"

ans = 0
ans2 = 0

with open(file_in, "r") as f:
    string = f.read()
    lines = string.split("\n")

conns = {}

for line in lines:
    start = line.split(":")[0]
    conns[start] = line.split()[1:]

paths = [["you"]]

old_paths = None

while paths != old_paths:
    old_paths = copy.deepcopy(paths)
    paths = [path + [next] for path in paths if path[-1] != "out" for next in conns[path[-1]] if conns[path[-1]] not in paths]
    for path in paths:
        if path[-1] == "out":
            ans += 1

@functools.cache
def solve(pos, dac, fft):
    if pos == "out":
        return dac and fft
    return sum(solve(conn, dac or conn == "dac", fft or conn == "fft") for conn in conns[pos])

ans2 = solve("svr", False, False)

print(ans)
print(ans2)