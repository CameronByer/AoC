file = "day22.in"

ans=0
ans2=0

with open(file, "r") as f:
    string = f.read()
    lines = string.split("\n")
    nums = [int(line) for line in lines]

def next_secret(secret):
    n = secret*64
    secret = n^secret
    secret %= 16777216
    n = secret // 32
    secret = n ^ secret
    n = secret * 2048
    secret = n ^ secret
    secret %= 16777216
    return secret

poss = set()
saved = {}
for n in nums:
    orig = n
    saved[orig] = {}
    c = tuple()
    for i in range(2000):
        prev = n%10
        n = next_secret(n)
        new = n%10
        c = c + (new-prev,)
        poss.add(c[-4:])
        if not c[-4:] in saved[orig]:
            saved[orig][c[-4:]] = new
    ans += n

def bananas(p):
    total = 0
    for k, v in saved.items():
        if p in v:
            total += v[p]
    return total

best = max(poss, key=bananas)

print(best)

for s in saved:
    if best in saved[s]:
        ans2 += saved[s][best]

print(ans, ans2)