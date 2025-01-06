line = open(0).read().strip()
#N = 5;line = 's1,x3/4,pe/b'; # TEST
N = 16

def dance(line,N,IT):
    dancers = [chr(ord('a') + i)for i in range(N)]
    D = line.split(',')
    assert all(len(d) > 1 for d in D)
    found = False
    it = 0
    SEEN = {}#set()
    SEEN[''.join(dancers)] = 0
    while it < IT:
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
                    #print('p/',''.join(dancers))
            else: # SPIN
                offset = -int(r)
                dancers = dancers[offset:] + dancers[:offset]
                #print('s/',''.join(dancers))
        it += 1
        if not found:
            pattern = ''.join(dancers)
            if pattern in SEEN:
                
                IT = (IT - it) % (it - SEEN[pattern])
                it = 0
                found = True
                print(pattern, 'seen/at',it,'IT/updated',IT)
                SEEN = {}
                continue
            SEEN[pattern] = it#.add(pattern)
        print(it,''.join(dancers))
    return ''.join(dancers)

p1 = ''.join(dance(line,N,1))
p2 = ''.join(dance(line,N,1000000000))
print('part 1:', p1)
print('part 2:', p2)
assert p1 in ['baedc','ceadb','ionlbkfeajgdmphc']
assert p2 == 'fdnphiegakolcmjb'
