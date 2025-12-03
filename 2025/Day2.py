import sys

file_in = "Day2.in"

with open(file_in, "r") as f:
    string = f.read()
    ranges = string.split(",")

ans = 0
ans2 = 0

def invalid(num):
    if len(num) == 1:
        return False
    for r in range(2, len(num)+1):
        i = len(num)//r
        if r > 0:
            if num[:i]*r == num:
                return True
    return False

for r in ranges:
    a, b = r.split("-")
    print(a, b)
    for i in range(int(a), int(b)+1):
        if invalid(str(i)):
            ans += i
            print(i)
    print()

print(ans, ans2)
