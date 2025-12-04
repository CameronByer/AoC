import sys, copy

file_in = "Day4.in"

ans = 0
ans2 = 0

with open(file_in, "r") as f:
    string = f.read()
    lines = string.split("\n")

for line in range(len(lines)):
    lines[line] = "."+lines[line]+"."
lines = ["."*len(lines[0])] + lines + ["."*len(lines[0])]

c = [line for line in lines]

ans = -1

while ans != 0:
    ans = 0
    lines = copy.deepcopy(c)
    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[0])-1):
            if lines[i][j] == "@":
                rolls = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if lines[i+x][j+y] == "@":
                            rolls += 1
                if rolls <= 4:
                    ans += 1
                    ans2 += 1
                    c[i] = c[i][:j] + "." + c[i][j+1:]
    print(ans)
print(ans2)