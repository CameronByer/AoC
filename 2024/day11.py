ans = 0
ans2 = 0

fname = "day11.in"
#fname = "day11test.in"
with open(fname, "r") as f:
    raw = f.read()
    lines = raw.split("\n")
    nums = [[int(x) for x in line.split()] for line in lines][0]

dp = {}
def get_stones(n, i):
    if i == 0:
        return 1
    if (n, i) in dp:
        return dp[(n, i)]
    if n == 0:
        dp[(1, i-1)] = get_stones(1, i-1)
        return dp[(1, i-1)]
    elif len(str(n))%2==0:
            a = len(str(n))//2
            x = n % (10 ** a)
            y = (n - x) // (10**a)
            dp[(x, i-1)] = get_stones(x, i-1)
            dp[(y, i-1)] = get_stones(y, i-1)
            return dp[(x, i-1)] + dp[(y, i-1)]
    else:
        x = n*2024
        dp[(x, i-1)] = get_stones(x, i-1)
        return dp[(x, i-1)]

for s in nums:
    ans += get_stones(s, 75)

print(ans, ans2)