D = {k:v for k,v in[list(map(int,_.split(': ')))\
    for _ in open(0).read().splitlines()]}
#for l,r in D.items(): print(l,r)

L = list(D.keys())
N = max(D.keys()) + 1
scanners = [-1] * N
for i in L: scanners [i] = 0

def iscaught(t,size,delay):
    ending_pos = t + delay
    cyclic_len = 2 * (size - 1)
    if ending_pos % cyclic_len == 0:
        return True
    return False

def caughtat(delay):
    for k,v in D.items():
        if iscaught(k,v,delay):
            return True
    return False

def go2_using_cyclic_size():
    delay = 0
    while caughtat(delay):
        delay += 1
    return delay

def go1_using_cyclic_size():
    res = 0
    for k,v in D.items():
        if iscaught(k,v,0):
            res += k * v
    return res

# p2 bruteforced impossibly slow
def go2(SCANNERS): # deprecated
    delay = 0
    SEEN = set()
    while 42:
        if delay % 100 == 0: print('delay/',delay)
        pac = 0
        direc = [1] * N
        elaps = 0
        caught = False
        scanners = SCANNERS[:]
        tried = tuple(scanners)
        if tried in SEEN:
            delay += 1
            continue
        while 42:
            scanners,direc = patrol(scanners,direc) # scan
            if elaps == delay:
                curr = tuple(scanners+direc) # check beginning set
                if curr in SEEN:
                    caught = True
                    break
                SEEN.add(curr)
            if elaps >= delay:
                pac += 1 # move pac
            elaps += 1
            if pac == N:
                break
            if elaps >= delay and scanners[pac] == 0:
                caught = True
                break
        if not caught:
            break
        delay += 1
    return delay

def patrol(sc,direc):    
    for i,pos in enumerate(sc):
        if i not in D:
            continue
        pos = (pos + direc[i])
        if pos == D[i] - 1:
            direc[i] = -1
        elif pos == 0:
            direc[i] = 1
        sc[i] = pos
    return sc,direc

def go1(scanners):
    print(scanners,'/initial')
    res = 0
    pac = 0
    direc = [1] * N
    while 42:
        scanners,direc = patrol(scanners,direc) # scan
        pac += 1 # move pac 
        if pac == N:
            break
        if scanners[pac] == 0:
            res += pac * D[pac]
        print(scanners,pac)
    return scanners,pac,res

if __name__ == '__main__':
    _,_,p1bf = go1(scanners[:])
    print('part 1:', p1bf,'/bruteforce')

    p1 = go1_using_cyclic_size()
    print('part 1:', p1)

    p2 = go2_using_cyclic_size()#go2(scanners[:])
    print('part 2:', p2)

    assert p1 in [1728,24]
    assert p2 in [3946838,10]

    p2bf = go2(scanners[:])
    print('part 2:', p2bf, '/bruteforce') # takes years
