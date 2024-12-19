import sys, functools

file = "day19.in"

ans=0
ans2=0

with open(file, "r") as f:
    string = f.read()

towels, patterns = string.split("\n\n")

towels = tuple(towels.split(", "))
patterns = tuple(patterns.strip().split("\n"))

@functools.cache
def count_patterns(towels, pattern):
    num = 0
    if pattern == "":
        return 1
    for towel in towels:
        if pattern.startswith(towel):
            num += count_patterns(towels, pattern[len(towel):])
    return num

for pattern in patterns:
    combos = count_patterns(towels, pattern)
    ans += combos > 0
    ans2 += combos
    
print(ans, ans2)
