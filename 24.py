cmps = []
for line in open(0).read().splitlines():
    a,b = list(map(int,line.split('/')))
    cmps.append((int(a),int(b)))

def go1(cmps):
    res = 0
    bridge = []
    def backtracking(seen,port,score):
        nonlocal bridge, res
        if res < score:
            res = score
            bridge = seen[:]
        for cmp in cmps:
            l,r = cmp
            if cmp not in seen and port in cmp:
                otherport = l if l != port else r
                seen.append(cmp)
                backtracking(seen, otherport, score + sum(cmp))
                seen.pop()
    backtracking([],0,0)
    return res, bridge

def go2(cmps):
    maxsize = 0
    maxscore = 0
    bridge = []
    def backtracking(seen,port,size,score):
        nonlocal bridge, maxsize, maxscore
        if maxsize <= size:
            maxsize = size
            maxscore = max(maxscore,score)
            bridge = seen[:]
        for cmp in cmps:
            l,r = cmp
            if cmp not in seen and port in cmp:
                otherport = l if l != port else r
                seen.append(cmp)
                backtracking(seen, otherport, size + 1, score + sum(cmp))
                seen.pop()
    backtracking([],0,0,0)
    return maxscore, bridge

p1,path = go1(cmps)
print('part 1:',p1)

p2,path = go2(cmps)
print('part 2:',p2)

print('path 1:','-'.join(['/'.join(list(map(str,_)))for _ in path]))
print('path 2:','-'.join(['/'.join(list(map(str,_)))for _ in path]))

