import collections, re, networkx as nx

TEST=0#1
lines = open(0).read().splitlines()
D = collections.defaultdict(int)
g = nx.DiGraph() # p2
for line in lines:
    names = re.findall(r'[a-z]+', line)
    w = int(re.findall(r'\((\d+)\)', line)[0])
    for name in names: D[name] += 1
    # p2
    g.add_node(names[0], w=w)
    if '->' in line:
        for i in range(1, len(names)):
            g.add_edge(names[0], names[i])

p1 = None
for k,v in D.items():
    if v == 1:
        p1 = k
        break

p2 = None
if TEST:
    for node in g:
        print('node/',node)
        if g[node]: print('\t↳',','.join(g[node]))
    for it in g.nodes.items(): print('item/',it)
    for ig in g.in_degree(): print('in-degree/',ig)
    for og in g.out_degree(): print('out-degree/',og)
    for dg in g.degree: print('degree/',dg)
ID = dict(g.in_degree())
OD = dict(g.out_degree())

rev = list(nx.topological_sort(g))[::-1]
SUMS = {}
# traverse upwards in a reversed tree, one level at a time
for node in rev:
    if TEST:
        print('node -',node,g.nodes[node]['w'],'in/out',ID[node],OD[node])
    children = g[node]
    FREQ = collections.defaultdict(int)
    for child in children:
        FREQ[SUMS[child]] += 1
    N = len(FREQ)
    special = None
    assert N in range(3)
    if N == 2:
        many = max(FREQ, key=FREQ.get)
        only = min(FREQ, key=FREQ.get)
    update = 0
    for child in children:
        update += SUMS[child]
        accwei = SUMS[child]
        if N == 2 and accwei != many:
            special = child
            break
    if special:
        correction = abs(many - only)
        p2 = g.nodes[special]['w'] - correction
        print(f'disc/ {list(FREQ.items())}')
        print(f'found/ {special}\ncorrection/ {correction}')
        break
    SUMS[node] = update + g.nodes[node]['w']

print('part 1:', p1)
print('part 2:', p2)
assert p1 == list( nx.topological_sort(g) )[0]
assert p1 in ['gynfwly','tknk']
assert p2 in [60,1526]
