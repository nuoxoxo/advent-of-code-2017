from collections import defaultdict
lines = open(0).read().splitlines()
conn = defaultdict(list)
for line in lines:
    L,R = line.split(' <-> ')
    L,R = int(L),list(map(int,R.split(', ')))
    for r in R:
        conn[L].append(r)

def p1():
    SEEN = set()
    res = 0
    def BFS(prog): # floodfill
        Q = [prog]
        while Q:
            node = Q.pop(0)
            for nei in conn[node]:
                if nei not in SEEN:
                    SEEN.add(nei)
                    Q.append(nei)
    for node in conn:
        if node not in SEEN:
            SEEN.add(node)
            BFS(node)
            res += 1
    return res

def p0():
    res = set()
    def backtrack(node, path): # DFS
        nonlocal res
        path.append(node)
        if 0 in path:
            res.add(tuple(path))
        for nei in conn[node]:
            if nei not in path:
                backtrack (nei,path)
        path.pop()
    for node in conn:
        backtrack(node, [])
    return list(res)

paths = p0()
res1 = set()
res2 = p1()
for p in paths:
    res1.add(p[0])
    res1.add(p[-1])
print('part 1:', len(res1))
print('part 2:', res2)
