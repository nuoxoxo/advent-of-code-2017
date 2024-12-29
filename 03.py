END = int(open(0).read())
print('inp/', END)
sq,step,curr = None,0,1
while curr ** 2 < END:
    sq = curr ** 2
    curr += 2
    step += 1
print('sq/nearest',sq,'- step/',step)
dist = (sq - END) % (step * 2)
p1 = step + abs((curr // 2) - dist)

p2 = None
lines = open('_inputs_/b141481.txt').read().splitlines()[3:-7]
for n in [int(_.split()[1]) for _ in lines]:
    if n > END:
        p2 = n
        break

print('part 1:',p1)
print('part 2:',p2)
assert p1 == 419
assert p2 == 295229
