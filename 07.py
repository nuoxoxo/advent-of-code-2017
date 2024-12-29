import collections, re
lines = open(0).read().splitlines()
D = collections.defaultdict(int)
for line in lines:
    wds = re.findall(r'[a-z]+', line)
    for w in wds: D[w] += 1
p1 = None
for k,v in D.items():
    if v == 1:
        p1 = k
        break

print('part 1:', p1)
assert p1 in ['gynfwly','tknk']
