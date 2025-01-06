A,B = [int(_.split()[-1]) for _ in open(0).read().splitlines()]
# A,B = 65,8921 # test
mod = 2147483647
fa,fb = 16807,48271

ML = 10**6
mask = (1 << 16) - 1 # 0xFFFF

def p1(A,B,ITER):
    res = 0
    N = 40 * (10**6)
    for _ in range(N):
        if _ % ML == 0: print('i/',_)
        A = A * fa % mod
        B = B * fb % mod
        #print(A,B)
        """ # bruteforce impossible
        a = bin(A)[2:].zfill(32);b = bin(B)[2:].zfill(32)
        print(a);print(b);print()
        """
        res += (A & mask) == (B & mask)
    return res

# p2
def p2(A,B,ITER):
    LA,LB = [],[]
    N = 5 * (10**6)
    mask = (1 << 16) - 1 # 0xFFFF
    while len(LA) < N:
        A = A * fa % mod
        if A % 4 == 0:
            LA.append(A)
            if len(LA) % ML == 0: print('a/i',len(LA))
    while len(LB) < N:
        B = B * fb % mod
        if B % 8 == 0:
            LB.append(B)
            if len(LB) % ML == 0: print('b/i',len(LB))
    return sum((a & mask) == (b & mask) for a,b in zip(LA,LB))

res1 = p1(A,B,40 * ML)
res2 = p2(A,B, 5 * ML)
print('part 1:',res1)
print('part 2:',res2)
assert res1 in [588,619]
assert res2 in [309,290]
