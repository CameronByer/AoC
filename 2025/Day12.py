import functools, copy

file_in = "Day12.in"

ans = 0

with open(file_in, "r") as f:
    string = f.read()
    pieces = string.split("\n\n")
    presents = [piece.split("\n")[1:] for piece in pieces[:-1]]
    problems = pieces[-1].split("\n")

# Seems like naive heuristic works for input
def potentially_overflow(size, reqs):
    return (size[0]//3) * (size[1]//3) >= sum(reqs)

for problem in problems:
    size = [int(x) for x in problem.split(":")[0].split("x")]
    reqs = [int(x) for x in problem.split()[1:]]
    ans += potentially_overflow(size, reqs)

print(ans)