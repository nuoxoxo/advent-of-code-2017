"""Spin, written sX, makes P programs move from the end to the front, 
but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
Exchange, written xA/B, makes the programs at positions A and B swap places.
Partner, written pA/B, makes the programs named A and B swap places."""

line = open(0).read().strip()
#N = 5;line = 's1,x3/4,pe/b'; # TEST
N = 16

def dance(line,N,IT):
    def P(l,r):
        nonlocal dancers,idx
        #L,R = dancers[l],dancers[r] # dancers
        #dancers[l],dancers[r] = R,L
        idx[L],idx[R] = r,l
        L,R = dancers.index(l),dancers.index(r)
        dancers[L],dancers[R] = dancers[R],dancers[L]
        #print('x/',''.join(dancers))
    dancers = [chr(ord('a') + i)for i in range(N)]
    D = line.split(',')
    assert all(len(d) > 1 for d in D)
    idx = {k:v for v,k in enumerate(dancers)} # to be obsolete
    found = False
    it = 0
    SEEN = {}#set()
    SEEN[''.join(dancers)] = 0
    while it < IT:
    #for it in range(IT):
        if it % 1000 == 0: print('i/',it)
        for d in D:
            m,r = d[0],d[1:]
            if '/' in d:
                l,r = r.split('/')
                if 'x' in d: # XCH/pos
                    l,r = int(l),int(r)
                    dancers[l],dancers[r] = dancers[r],dancers[l]
                else: # PARTN
                    L,R = dancers.index(l),dancers.index(r)
                    dancers[L],dancers[R] = dancers[R],dancers[L]
                    """
                    L,R = idx[l],idx[r] # index
                    dancers[L],dancers[R] = dancers[R],dancers[L]
                    idx[l],idx[r] = R,L
                    """
                    #print('p/',''.join(dancers))
            else: # SPIN
                offset = -int(r)
                dancers = dancers[offset:] + dancers[:offset]
                """
                for _ in range(int(r)):
                    #for end in range(N-1,0,-1):
                        #P(end - 1,end)
                    todo = dancers.pop()
                    idx[todo] = -1
                    for k in idx.keys():
                        idx[k] += 1
                    dancers.insert(0,todo)
                """
                #print('s/',''.join(dancers))
        if not found:
            pattern = ''.join(dancers)
            if pattern in SEEN:
                IT = (IT - it) % (it - SEEN[pattern]) + 1
                found = True
                print(pattern, 'seen/at',it,'IT/updated',IT)
                SEEN = {}
                continue
            SEEN[pattern] = it#.add(pattern)
        it += 1
        print(it,''.join(dancers))
    return ''.join(dancers)
p1 = ''.join(dance(line,N,1))
print('part 1:', p1)
assert p1 in ['baedc','ceadb','ionlbkfeajgdmphc']
print('part 2:',''.join(dance(line,N,1000000000)))
