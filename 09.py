line = open(0).read().strip()
noxcl = ''
N = len(line)
i = 0
while i < N:
    if line[i] == '!':
        i += 2
        continue
    else:
        noxcl += line[i]
        i += 1
print(noxcl,'no/!')

final = ''
i = 0
N = len(noxcl)
p2 = 0
while i < N:
    if noxcl[i] == '<':
        shift = -1
        while i < N and noxcl[i] != '>':
            i += 1
            shift += 1
        p2 += shift
    elif i < N:
        if noxcl[i] != '>':
            final += noxcl[i]
        i += 1
print(final,'no/<')

p1 = 0
sc = 0
for c in final:
    if c == '{':
        sc += 1
        p1 += sc
    elif c == '}':
        sc -= 1
print('part 1:',p1)
print('part 2:',p2)
