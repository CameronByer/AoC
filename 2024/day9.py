ans = 0
ans2 = 0

fname = "day9.in"
#fname = "day9test.in"
with open(fname, "r") as f:
    raw = f.read()
    lines = raw.split("\n")
    #nums = [[int(x) for x in line.split()] for line in lines]

s = []
ss = []
index = 0
index2 = 0

for i in lines[0]:
    if index%2 == 0:
        for j in range(int(i)):
            s.append(index2)
        ss.append((index2, int(i)))
        index2 += 1
    else:
        for j in range(int(i)):
            s.append(None)
        ss.append((None, int(i)))
    index += 1

def gn(x):
    return x.index(None)

def gn2(x, le):
    for i in range(len(x)):
        if x[i][0]==None and x[i][1] >= le:
            return i
    return -1

'''for e in range(len(s)):
    ee = -e-1
    x = s[ee]
    if s[ee] != None:
        s[ee] = None
        s[gn(s)]=x
'''

for e in range(len(ss)):
    ee = len(ss)-e-1
    x = ss[ee]
    if ss[ee][0]!=None:
        sp = gn2(ss, ss[ee][1])
        toc = ss[sp]
        w = ss[ee]
        if sp != -1 and sp<ee:
            nn=(None, toc[1]-w[1])
            ss[ee]=(None, w[1])
            ss= ss[:sp] + [w, nn] + ss[sp+1:]
            for i in range(len(ss)-2,-1,-1):
                if ss[i][0] == None and ss[i+1][0] == None:
                    ss[i] = (None, ss[i][1]+ss[i+1][1])
                    ss[i+1] = (None, 0)

'''
for i in range(len(s)):
    if s[i]:
        ans += i*s[i]
'''

ind = 0

for a, b in ss:
    for i in range(b):
        if a:
            ans2 += ind*a
        ind += 1

print(ans, ans2)