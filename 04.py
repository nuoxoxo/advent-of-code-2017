lines = [_.split() for _ in open(0).read().splitlines()]
p1,p2 = 0,0
for a in lines:
    if len(set(a)) == len(a):
        p1 += 1
    aa = [''.join(sorted([_ for _ in wd])) for wd in a]
    if len(set(aa)) == len(a):
        p2 += 1
print('part 1:',p1)
print('part 2:',p2)
assert p1 == 455
assert p2 == 186
