import sys

file_in = "Day3.in"

with open(file_in, "r") as f:
    string = f.read()
    lines = string.split("\n")

def best(vals, flips):
    if flips == 1:
        return int(max(vals, key=int))
    first = max(vals[:-flips+1], key=int)
    index = vals.index(first)
    return 10 ** (flips-1) * int(first) + best(vals[index+1:], flips-1)

ans = 0
ans2 = 0
for line in lines:
    ans += best(line, 2)
    ans2 += best(line, 12)





print(ans, ans2)
