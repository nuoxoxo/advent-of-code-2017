lines = open(0).read().split('\n\n')
begin = lines.pop(0).splitlines()
start = begin[0].split()[-1][:-1]
steps = int(begin[1].split()[-2])

print('begin/',start,steps)

class St:
    def __init__(self,w,m,c,w1,m1,c1):
        self.w = (w,w1)
        self.m = (m,m1)
        self.c = (c,c1)
    def __repr__(self):
        return f'w:{self.w} m:{self.m} c:{self.c}'

from collections import defaultdict
tape = defaultdict(int) # idx
states = {}

for bl in lines:
    instr = bl.splitlines()
    name = instr[0].split()[-1][:-1]

    w = int(instr[2].split()[-1][:-1])
    m = -1 if instr[3].split()[-1][:-1] == 'left' else 1
    c = instr[4].split()[-1][:-1]

    w1 = int(instr[6].split()[-1][:-1])
    m1 = -1 if instr[7].split()[-1][:-1] == 'left' else 1
    c1 = instr[8].split()[-1][:-1]
    states[name] = St(w,m,c,w1,m1,c1)

for k,v in states.items(): print(k,'->',v)

name = start
idx = 0
for _ in range(steps):
    st = states[name]
    curr = tape[idx]
    #print('name/',name,'curr/',curr)
    tape[idx] = st.w[curr]
    name = st.c[curr]
    idx += st.m[curr]

p1 = len([_ for _,v in tape.items() if v == 1])
print('part x:',p1)
