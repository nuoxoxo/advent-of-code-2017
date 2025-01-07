import re
lines = open(0).read().splitlines()
P = [list(map(int,re.findall(r'-?\d+',_))) for _ in lines]
pcl,PCL = [],[]
for line in P:
    p,v,a = line[:3],line[3:6],line[6:]
    #if sum([_ == 0 for _ in a]) == 2: print(i,'/',p,v,a)
    pcl.append([p,v,a])
    PCL.append([p[:],v[:],a[:]])
import collections
D = collections.defaultdict(int)
it = 0

while 42:
    close = 10**20
    which = None
    for i, pc in enumerate(pcl):
        p,v,a = pc
        for j in range(3):
            v[j] += a[j]
            p[j] += v[j]
        pcl[i] = [p,v,a]
        d = sum([abs(_) for _ in p])
        if close > d:
            close = d
            which = i
    if it % 200 == 0: print(f'p1 - i/{it}\tp({which}) has d({close})')
    D[which] += 1
    if D[which] > 2**10:
        break
    it += 1
print('p1/ends\n')
p1 = max(D,key=D.get)

D.clear()
gone = set()
np = len(lines)
it = 0
while 42:
    coors = collections.defaultdict(list)
    ng = len(gone)
    diff = np - ng
    if it % 200 == 0: print(f'p2 - i/{it}\t{np} - {ng} = {diff}')
    D[diff] += 1
    if D[diff] > 2**10:
        p2 = diff
        break
    for i, pc in enumerate(PCL):
        if i in gone:
            continue
        p,v,a = pc
        coors[tuple(p)].append(i)
        for j in range(3):
            v[j] += a[j]
            p[j] += v[j]
        PCL[i] = [p,v,a]
    for _,l in coors.items():
        if len(l) > 1:
            for idx in l:
                gone.add(idx)
    it += 1
print('\npart 1:',p1)
print('part 2:',p2)
