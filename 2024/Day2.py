import sys

file_in = "Day2.in"

with open(file_in, "r") as f:
    string = f.read()
    lines = string.split("\n")

total = 0
for line in lines:
    x = [int(a) for a in line.split()]
    if x == sorted(x) or x[::-1] == sorted(x):
        y = sorted(x)
        bad = False
        for i in range(len(x)-1):
            if abs(y[i] - y[i+1]) >= 4 or y[i] == y[i+1]:
                bad = True
        if not bad:
            total += 1

print(total)

total = 0
for line in lines:
    xx = [int(a) for a in line.split()]
    for j in range(len(xx)):
        x = xx[:j] + xx[j+1:]
        if x == sorted(x) or x[::-1] == sorted(x):
            y = sorted(x)
            bad = False
            for i in range(len(x)-1):
                if abs(y[i] - y[i+1]) >= 4 or y[i] == y[i+1]:
                    bad = True
            if not bad:
                total += 1
                break

print(total)
