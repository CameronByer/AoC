import sys

file = "blank.in"

ans=0
ans2=0

with open(file, "r") as f:
    string = f.read()
    lines = string.split("\n")
    #nums = [[int(x) for x in line.split()] for line in lines]

