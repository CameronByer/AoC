import sys, copy

file_in = "Day5.in"

ans = 0
ans2 = 0

with open(file_in, "r") as f:
    string = f.read().split("\n\n")
    fresh = string[0].split("\n")
    ings = string[1].split("\n")

print(fresh)
print(ings)

for i in ings:
    for f in fresh:
        f = f.split("-")
        if int(i) >= int(f[0]) and int(i) <= int(f[1]):
            ans += 1
            print(i, f)
            break

counted = []

for f in fresh:
    low, high = f.split("-")
    low = int(low)
    for other_low, other_high in counted:
        other_low = int(other_low)
        other_high = int(other_high)
        if low >= other_low and low <= other_high:
            low = other_high + 1
    high = int(high)
    for other_low, other_high in counted:
        other_low = int(other_low)
        other_high = int(other_high)
        if high >= other_low and high <= other_high:
            high = other_low - 1
    if low > high:
        continue
    counted = [(other_low, other_high) for other_low, other_high in counted if not (other_low >= low and other_high <= high)]
    counted.append((low, high))
    print(counted)

for l, h in counted:
    ans2 += h - l + 1

print(ans)
print(ans2)