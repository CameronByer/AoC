n = [2,4,1,1,7,5,4,6,0,3,1,4,5,5,3,0]
A = 28066687
B = 0
C = 0
i = 0
out = []

def get_combo(op):
    if op <= 3:
        return op
    return [A, B, C][op-4]

def run_command(code, op):
    global A, B, C, i
    combo = get_combo(op)
    match code:
        case 0:
            A //= 2**combo
        case 1:
            B ^= op
        case 2:
            B = combo % 8
        case 3:
            i = -2 if A else i
        case 4:
            B ^= C
        case 5:
            out.append(combo%8)
        case 6:
            B = A // 2**combo
        case 7:
            C = A // 2**combo
    i += 2

def part1():
    global A, B, C, i, out
    while i+2 <= len(n):
        code, op = n[i], n[i+1]
        run_command(code, op)
    return(out)


'''
(2, 4) B = A % 8
(1, 1) B ^= 1
(7, 5) C = A // (2^B) # Remove Last B digits of binary A and store the rest in C... B is at most 7, so only the final 3 digits of octal A are changed
(4, 6) B ^= C # We only ever care about the last digit of octal C, which means at most only the final 4 digits of octal A play a role in the calculation of B
(0, 3) A //= # 8 Remove last digit of octal A
(1, 4) B ^= 4
(5, 5) out B % 8
(3, 0) Jump to start if A != 0

The corollary to this is that the first four digits of A completely determine the final number in the output.
Thus, If we can generate the final 5 numbers of the output, then we know that the first digit of octal A must be fixed.
'''

def part2():
    global A, B, C, i, out
    Astart = 0
    immutable_dist = 5
    out_to_match = immutable_dist
    while out != n:
        Astart += 1
        A = Astart
        B = 0
        C = 0
        i = 0
        out = []
        while i+2 <= len(n):
            code, op = n[i], n[i+1]
            run_command(code, op)
        if out[-out_to_match:] == n[-out_to_match:]:
            print(oct(Astart), Astart, out)
            if out == n:
                break
            Astart *= 8
            Astart -= Astart % (8**immutable_dist)
            out_to_match += 1
    return Astart

ans = part1()
ans2 = part2()

print(ans)
print(ans2)