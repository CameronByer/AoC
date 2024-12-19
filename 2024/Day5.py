import sys

file = "Day5.in"

ans=0
ans2=0

with open(file, "r") as f:
    string = f.read()
    lines = string.split("\n")

orders = [[int(x) for x in line.split("|")] for line in lines if "|" in line]
nums = [[int(x) for x in line.split(",")] for line in lines if "," in line]

for rule in nums:
    bad = False
    for o in orders:
        try:
            if rule.index(o[0])>=rule.index(o[1]):
                bad = True
        except:
            pass
    if not bad:
        ans += rule[(len(rule))//2]

for rule in nums:
    bad = True
    while bad:
        bad = False
        for o in orders:
            try:
                if rule.index(o[0])>=rule.index(o[1]):
                    bad = True
                    rule[rule.index(o[0])], rule[rule.index(o[1])] = rule[rule.index(o[1])], rule[rule.index(o[0])]
            except:
                pass
    ans2 += rule[(len(rule))//2]

print(ans, ans2)
