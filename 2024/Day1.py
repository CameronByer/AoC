import sys

file_in = "Day1.in"

with open(file_in, "r") as f:
    string = f.read()
    lines = string.split("\n")

numsa = []
numsb = []
for line in lines:
    x = line.split()
    a,b = x[0], x[1]
    numsa.append(int(a))
    numsb.append(int(b))

numsa = sorted(numsa)
numsb = sorted(numsb)

total = 0
total2 = 0
for i in range(len(numsa)):
    total += abs(numsa[i]-numsb[i])
    total2 += numsa[i]*numsb.count(numsa[i])

print(total)
print(total2)
