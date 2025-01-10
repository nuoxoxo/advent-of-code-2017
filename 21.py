lines = open(0).read().splitlines()

BEGIN=[list(_) for _ in """.#.
..#
###
""".split()]

for i,s in enumerate(BEGIN):print('|',''.join(s),'\n'if i==len(BEGIN)-1 else'')

def go(state, checks, T):
    res = None
    for t in range(T):
        if t in checks:
            res = sum([line.count('#') for line in state])
            yield res
            print(f'res/{t} {res}')
            if t == checks[-1]: print(); return
        N = len(state)
        if N % 2 != 0 and N % 3 != 0:
            assert False
        _next = []
        sizeof = 2 if N % 2 == 0 else 3
        for r in range(0, N, sizeof):
            subs = ['' for _ in range(sizeof + 1)]
            for c in range(0, N, sizeof):
                i = tuple([''.join(state[r + i][c:c + sizeof]) for i in range(sizeof)])
                o = RULES[i]
                for i, line in enumerate(o):
                    subs[i] += line
            _next += subs
        state = _next

# flip/ U->D - L->R
# rotate/ L-90,R-90 - further be same as flip
# flip+rotate/ U->D->L|R.90 - L->R->L|R.90

def flip(G):
    return [tuple(''.join(_[::-1]) for _ in G),
            tuple(''.join(_) for _ in G[::-1])]

def rot(g):
    return [tuple(''.join(_) for _ in zip(*g[::-1])),
            tuple(''.join(_) for _ in zip(*g))[::-1],
            tuple(''.join(_[::-1]) for _ in g[::-1])]

def frot(G):
    r = [tuple(_) for _ in rot(G)]
    fr = [tuple(_) for f in flip(G) for _ in rot(f)]
    return r + fr

if __name__ == '__main__':

    RULES = {}
    for line in lines:
        L,R = [_.split('/') for _ in line.split(' => ')]
        RULES[tuple(L)] = tuple(R)
        for f in flip(L): print('f/',f)
        for r in rot(L): print('r/',r)
        for fr in frot(L): print('+/',fr)
        for pattern in flip(L) + rot(L) + frot(L):
            RULES[tuple(pattern)] = tuple(R)
    for k,v in RULES.items(): print(k,'=>',v,'/dict')
    _, p1, p2 = go([_[:] for _ in BEGIN], [2,5,18], 18+1)

    print('part 1:',p1)
    print('part 2:',p2)
    assert p1 == 167
    assert p2 == 2425195
