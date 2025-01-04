from collections import defaultdict
lines = open(0).read().splitlines()
n1 = set()
n2 = set()
D = defaultdict(int)
def REVAL(l,m,r):
    l = str(D[l])
    return eval(l+m+r)
def LEVAL(l,m,r):
    l = str(D[l])
    if m == 'inc': m = '+'
    elif m == 'dec': m = '-'
    return eval(l+m+r)
high = -1
for line in lines:
    l,r = line.split(' if ')
    k,o,v = l.split()
    kk,oo,vv = r.split()
    n1.add(k)
    n2.add(kk)
    if REVAL(kk,oo,vv):
        D[k] = LEVAL(k,o,v)
        high = max(high, D[k])
assert ''.join(sorted(list(n1))) == ''.join(sorted(list(n2)))
print('part 1:', max(list(D.values())))
print('part 2:', high)
    
