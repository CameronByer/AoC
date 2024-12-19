from math import lcm

ans = 0
ans2 = 0

fname = "2018.in"
#fname = "day13test.in"
with open(fname, "r") as f:
    raw = f.read()
    lines = raw.split("\n")
    #nums = [[int(x) for x in line.split()] for line in lines][0]

nums = [int(x) for x in raw]

a = 0
b = 1

scoreboard="37"

while not "556061" in scoreboard[-10:]:
    newr = nums[a]+nums[b]
    scoreboard = scoreboard + str(newr)
    while newr >= 10:
        nums.append(newr//10)
        newr-=10*(newr//10)
    nums.append(newr)
    recis = len(nums)
    a = (a+nums[a]+1)%recis
    b = (b+nums[b]+1)%recis

print(len(scoreboard), scoreboard[-10:])

while len(nums) < 556071:
    newr = nums[a]+nums[b]
    while newr >= 10:
        nums.append(newr//10)
        newr-=10*(newr//10)
    nums.append(newr)
    recis = len(nums)
    a = (a+nums[a]+1)%recis
    b = (b+nums[b]+1)%recis

print(ans, ans2)