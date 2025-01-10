lines = open(0).read().splitlines()

begin=[list(_) for _ in """.#.
..#
###
""".split()]
for i,s in enumerate(begin):print('|',''.join(s),'\n'if i==len(begin)-1 else'')

def go(T,s):
    print('go/')
    RULES = {}
    for line in lines:
        p,rule = line.split(' => ')
        RULES[p] = rule
        """
        for f in f(p): print('  f/',f)
        for r in r(p): print('  r/',r)
        for fr in fr(p): print('  +/',fr)
        """
        for pattern in flip(p) + rot(p) + frot(p):
            RULES[pattern] = rule
    for k,v in RULES.items(): print(k,'=>',v)

    for i,_ in enumerate(s):print('|',''.join(_),'\n'if i==len(_)-1 else'')
    mult = 1
    res = None
    for _ in range(T):
        N = len(s)
        count = 0
        if N % 2 == 0 and N != 2:
            #print('here/2',N)
            s = s[:N//2]
            for i in range(len(s)):
                s[i] = s[i][:N//2]
            mult = (N//2) ** 2
        elif N != 3:
            print('here/3',N)
            assert N % 3 == 0
            s = s[:N//3]
            for i in range(len(s)):
                s[i] = s[i][:N//3]
            #mult *= N//3
            mult = (N//3) ** 2
        N = len(s) # redo
        for r in range(N):
            for c in range(N):
                if s[r][c] == '#':
                    print('curr/u',count,mult)
                    count += 1 * mult#(1 if not mult else mult)
                    print('curr/d',count,mult)
        res = count
        for i,_ in enumerate(s):print('|',''.join(_))#,'\n'if i==len(_)-1 else'')
        print('\ncount/',count)
        k = '/'.join([''.join(_) for _ in s])
        #print(k,k in RULES)
        v = RULES[k]
        tmp = []
        for r in v.split('/'):
            tmp.append(list(r))
        s = [_[:] for _ in tmp]

    print('res/',res)

# flip/ U->D - L->R
# rotate/ L-90,R-90 - further be same as flip
# flip+rotate/ U->D->L|R.90 - L->R->L|R.90

def flip(line):
    res = []
    g = line.split('/')
    N = len(g)
    LR = ''
    for r in range(N):
        t = list(g[r])
        for c in range(N//2): t[c],t[N-c-1] = t[N-c-1],t[c]
        LR += ''.join(t) + ('/' if r != N - 1 else '')
    res.append(LR)
    for r in range(N//2): g[r],g[N-r-1] = g[N-r-1],g[r]
    res.append('/'.join(_ for _ in g))
    return res

def rot(line):
    g = line.split('/')
    return ['/'.join([''.join(_) for _ in list(zip(*g))][::-1]),\
            '/'.join([''.join(_[::-1]) for _ in list(zip(*g))])]

def frot(line):
    return [_ for flipped in flip(line) for _ in rot(flipped)]

if __name__ == '__main__':
    #go( 2, [_[:] for _ in begin] )
    go( 5, [_[:] for _ in begin] )
