import sys

file_in = "Day1.in"

with open(file_in, "r") as f:
    string = f.read()
    lines = string.split("\n")

ans = 0
ans2 = 0

dial = 50

for line in lines:
    val = int(line[1:])
    ans2 += val // 100
    val %= 100
    if line[0] == "R":
        dial += val
    if line[0] == "L":
        if dial == 0:
            ans2 -= 1
        dial -= val
    if dial == 0 or dial == 100:
        ans += 1
    if dial <= 0 or dial >= 100:
        ans2 += 1
    dial %= 100

print(ans)
print(ans2)
