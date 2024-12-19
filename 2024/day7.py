ans = 0
ans2 = 0

fname = "day7.in"
#fname = "day7test.in"
with open(fname, "r") as f:
    raw = f.read()
    lines = raw.split("\n")
    nums = [[int(x.replace(":", "")) for x in line.split()] for line in lines]

def getall(x):
    if len(x) == 1:
        return [x[0]]
    return [x[-1] + y for y in getall(x[:-1])] + [x[-1] * y for y in getall(x[:-1])]

def getall2(x):
    if len(x) == 1:
        return [x[0]]
    return [x[-1] + y for y in getall2(x[:-1])] + [x[-1] * y for y in getall2(x[:-1])] + [int(str(y)+str(x[-1])) for y in getall2(x[:-1])]

for test in nums:
    if test[0] in getall(test[1:]):
        ans += test[0]
    if test[0] in getall2(test[1:]):
        ans2 += test[0]

print(ans, ans2)