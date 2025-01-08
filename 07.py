import collections, re, networkx as nx

TEST=1
lines = open(0).read().splitlines()
D = collections.defaultdict(int)
g = nx.DiGraph() # p2
for line in lines:
    words = re.findall(r'[a-z]+', line)
    W = int(re.findall(r'\((\d+)\)', line)[0])
    for w in words: D[w] += 1
    # p2
    g.add_node(words[0], W=W)
    if '->' in line:
        for i in range(1, len(words)):
            g.add_edge(words[0], words[i])

p1 = None
for k,v in D.items():
    if v == 1:
        p1 = k
        break

p2 = None
# info of the graph
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
trackingwei = {}
# traverse upwards in a reversed tree, one level at a time
for node in rev:
    if TEST:
        print('node -',node,g.nodes[node]['W'],'in/out',ID[node],OD[node])
    curr = g.nodes[node]['W']
    levelwei = collections.defaultdict(int)
    children = g[node]
    for child in children:
        levelwei[trackingwei[child]] += 1
    special = None
    found = False
    assert -1 < len(levelwei) < 3
    most_common = max(levelwei, key=levelwei.get) if levelwei else None
    less_common = min(levelwei, key=levelwei.get) if levelwei else None
    for child in children:
        wc = trackingwei[child]
        curr += wc
        if most_common and wc != most_common:
            assert len(levelwei) == 2
            special = child
            found = True
            break
    if found:
        p2 = g.nodes[special]['W'] - abs(most_common - less_common)
        break
    trackingwei[node] = curr

print('part 1:', p1)
print('part 2:', p2)
assert p1 == list( nx.topological_sort(g) )[0]
assert p1 in ['gynfwly','tknk']
assert p2 in [60,1526]
