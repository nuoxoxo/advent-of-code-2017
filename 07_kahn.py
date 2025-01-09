import collections, re

lines = open(0).read().splitlines()
g = collections.defaultdict(lambda: { 'w': 0, 'pg': [] })
for line in lines:
    names = re.findall(r'[a-z]+', line)
    w = int(re.findall(r'\((\d+)\)', line)[0])
    g[names[0]]['w'] = w
    if '->' in line:
        for i in range(1,len(names)):
            g[names[0]]['pg'].append(names[i])
for k,v in g.items(): print('tree/',k,v)

# do kahn?
#   get all non-0 in-degree nodes
indg = collections.defaultdict(int)
for node in g:
    for child in g[node]['pg']:
        indg[child] += 1
for k,v in indg.items(): print('in-degree/',k,v)

#   expect only one node is not incl. above -> root node
todos = collections.deque()
for node in g:
    if node not in indg:
        todos.append(node)
        #break
print('degree-0/',todos); assert len(todos) == 1
p1 = todos[0]

#   bfs
topo = []
while todos:
    node = todos.popleft()
    topo.append(node)
    for child in g[node]['pg']:
        indg[child] -= 1 # decr. child's dg if its dg-0 parent is processed
        if indg[child] == 0:
            todos.append(child)
print('sorted/42',','.join(topo[:42])); assert len(topo) == len(g)

# going up|backwards one level at a time
topo = topo[::-1]
SUMS = {}
for node in topo:
    children = g[node]['pg']
    print(node,'-',','.join(children))
    FREQ = collections.defaultdict(int)
    for child in children:
        FREQ[SUMS[child]] += 1
    N = len(FREQ)
    special = None
    assert N in range(3)
    if N == 2:
        only,many = [k for k,_ in sorted(FREQ.items(),key=lambda _:_[1])]
    update = 0
    for child in children:
        update += SUMS[child]
        accwei = SUMS[child]
        if N == 2 and accwei != many:
            special = child
            break
    if special:
        correction = abs(many - only)
        p2 = g[special]['w'] - correction
        print(f'disc/ {list(FREQ.items())}')
        print(f'found/ {special}\ncorrection/ {correction}')
        break
    SUMS[node] = update + g[node]['w']

print('part 1:', p1)
print('part 2:', p2)
assert p1 in ['gynfwly','tknk']
assert p2 in [60,1526]
