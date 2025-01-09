test=0#1
import re
LINE = open(0).read().strip()

def p2(line: str):
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

def p1(line: str) -> int:
    n = go(1,line,256)
    return n[0]*n[1]

def go(n,line,RANGE):
    lens = getlens( line )
    nums = list(range(RANGE))
    if test==1:
        nums = list(range(5))
        lens = getlens('3, 4, 1, 5')
    skip = 0
    curr = 0
    assert not any([_ > RANGE for _ in lens])
    for _ in range(n):
        for ln in lens:
            indices,rev = [],[]
            for i in range(ln):
                idx = (curr + i) % RANGE
                indices.append(idx)
                rev.append(nums[idx])
            rev = rev[::-1]
            """
            print('curr/pos',curr,'/val',nums[curr],'\nskip/',skip)
            print('nums/',nums)
            print('idxs/',indices)
            print('rev/',rev)
            """
            for idx,i, in enumerate(indices):
                nums[i] = rev[idx]
            curr = (curr + ln + skip) % RANGE
            skip = (skip + 1) % RANGE
            """"
            print('inp/',ln, '\nnew/',nums)
            print('curr/pos',curr,'/val',nums[curr],'\nskip/',skip)
            print()
            """
    return nums

def getlens(s): return list(map(int,(re.findall(r'\d+', s))))

if __name__ == '__main__':
    print('part 1:', p1( LINE ))
    print('part 2:', p2( LINE ))

