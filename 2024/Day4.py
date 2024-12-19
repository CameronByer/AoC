import sys

file = "Day4.in"

ans=0
ans2=0

with open(file, "r") as f:
    string = f.read()
    lines = string.split("\n")
    #nums = [[int(x) for x in line.split()] for line in lines]

grid = lines

def check(x, y, dx, dy):
    a = ""
    try:
        for i in range(4):
            if x+dx*i <0 or y+dy*i < 0:
                return False
            a += grid[x+dx*i][y+dy*i]
        return a == "XMAS"
    except:
        return False

def check2(ngrid, x, y):
    combos = ("MMSS", "MSSM", "SSMM", "SMMS")
    for c in combos:
        if ngrid[x][y] == c[0] and ngrid[x+2][y] == c[1] and ngrid[x+1][y+1] == "A" and ngrid[x][y+2] == c[3] and ngrid[x+2][y+2] == c[2]:
            return True
    return False

for i in range(len(grid)):
    for j in range(len(grid[i])):
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                ans += check(i, j, di, dj)

for i in range(len(grid)-2):
    for j in range(len(grid[i])-2):
        ans2 += check2(grid, i, j)

print(ans, ans2)
