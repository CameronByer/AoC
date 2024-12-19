import sys
file = "day17.in"

ans=0
ans2=0

A = 15055668866
B = 0
C = 0
n = [2,4,1,1,7,5,4,6,0,3,1,4,5,5,3,0]
i = 0
out = []

'''
A = 729
B = 0
C = 9
n = [2,6]'''

def get_val(operand):
    if operand <= 3:
        return operand
    return (A, B, C)[operand-4]

def get_op(nums, x):
    global A, B, C, n, i, out
    if x >= len(n)-1:
        return False
    code, operand = nums[x], nums[x+1]
    if code == 0:
        A //= 2**get_val(operand)
    elif code == 1:
        B ^= operand
    elif code == 2:
        B = get_val(operand)%8
    elif code == 3:
        if A:
            i = get_val(operand)-2
    elif code == 4:
        B ^= C
    elif code == 5:
        out.append(get_val(operand)%8)
    elif code == 6:
        B = A // (2**get_val(operand))
    elif code == 7:
        C = A // (2**get_val(operand))
    i += 2
    return True

while get_op(n, i):
    pass
print(out)

AA = 0
goal = 3
while True:
    out = []
    while out != [2,4,1,1]:
        AA += 1
        A = AA
        B = 0
        C = 0
        i = 0
        out = []
        while get_op(n, i):
            pass
    st = bin(AA)[2:]
    print(st[:len(st)%3], end = " ")
    for x in range(len(st)):
        if x%3 == len(st)%3:
            print(st[x:x+3], end = " ")
    print(out)
    input()

print(A, out)

'''
A=0
while out != n:
    out = []
    A+=1
    i=0
    if A % 1 == 0:
        print(A)
    while get_op(n, i):
        if len(out) > len(n):
            break'''
