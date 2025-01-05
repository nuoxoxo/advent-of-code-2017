import re

LINE = 'ljoxqyyw'
#LINE = 'flqrgnkx'
keys = [LINE + '-' + str(_) for _ in range(128)]

# day10/p2 - makeknot, getlens, go

def makeknot(line: str):
    sequence = '17, 31, 73, 47, 23'.replace(' ','')
    line = ','.join([str(ord(c)) for c in line]) + ',' + sequence
    n = go(64,line,256)
    dh = []
    for i in range(0,len(n),16):
        x = n[i]
        for j in range(i+1,i+16):
            x ^= n[j]
        dh.append(hex(x)[2:].zfill(2))
    knot = ''.join(dh)
    assert len(knot) == 32
    return knot

def getlens(s): return list(map(int,(re.findall(r'\d+', s))))

def go(n,line,RANGE):
    lens = getlens( line )
    nums = list(range(RANGE))
    skp = 0
    cur = nums[0]
    N = len(nums)
    assert not any([_ > N for _ in lens])
    for _ in range(n):
        for ln in lens:
            indices,rev = [],[]
            count = 0
            while count < ln:
                indices.append((cur + count) % N)
                rev.append(nums[(cur+count)%N])
                count += 1
            rev = rev[::-1]
            for idx,i, in enumerate(indices):
                nums[i] = rev[idx]
            cur = (cur + ln + skp) % N
            skp = (skp + 1) % N
    return nums

p1 = 0
g2 = []
for i,line in enumerate(keys):
    knot = makeknot(line)
    tmp = sum([ bin(int(c,16))[2:].count('1') for c in knot ])
    #print(i,knot,'curr/',tmp)
    p1 += tmp
    # p2
    row = ''.join([ bin(int(c,16))[2:].zfill(4) for c in knot ])
    g2.append(row) # row or col does not matter now
    
# p2
regions = 0
SEEN = set()
DR = (-1,0,1,0)
DC = (0,1,0,-1)
def BFS(sr,sc):
    Q = [(sr,sc)]
    SEEN.add((sr,sc))
    while Q:
        r,c = Q.pop(0)
        for dr,dc in zip(DR,DC):
            rr,cc = r + dr,c + dc
            if -1<rr<128 and -1<cc<128 and g2[rr][cc]=='1' and (rr,cc)not in SEEN:
                Q.append((rr,cc))
                SEEN.add((rr,cc))
p2 = 0
for r in range(128):
    for c in range(128):
        if g2[r][c] == '1' and (r,c) not in SEEN:
            BFS(r,c)
            p2 += 1

print('part 1:',p1)
print('part 2:',p2)
assert p1 in [8108,8316]
assert p2 in [1242,1074]

