import sys, re
file_in = "input.in"

with open(file_in, "r") as f:
    string = f.read()
    string = "do()" + string + "don't()"

muls = re.compile(r"mul\((\d+),(\d+)\)")
dos = re.compile(r"do\(\).*?don't\(\)", re.DOTALL)

part1 = 0
for mul in muls.finditer(string):
    part1 += int(mul.group(1)) * int(mul.group(2))

part2 = 0
for match in dos.finditer(string):
    for mul in muls.finditer(match.group(0)):
        part2 += int(mul.group(1)) * int(mul.group(2))

print(part1, part2)