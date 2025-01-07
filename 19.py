G = open(0).read().splitlines()
R,C = len(G),len(G[0])
r,c = 0,0
for cc in range(C):
    if G[0][cc] == '|':
        c = cc
        break
D = ((1,0),(0,1),(-1,0),(0,-1))
d = 0
path = ''
step = 0
while -1<r<R and -1<c<C and G[r][c] != ' ':
    step += 1
    char = G[r][c]
    dr,dc = D[d]
    if char.isalpha():
        path += char
        r,c = r + dr, c + dc
    elif char in '-|':
        r,c = r + dr, c + dc
    else:
        assert char == '+'
        for i in [d-1,d+1]:
            dr,dc = D[i % 4]
            rr,cc = r + dr, c + dc
            if -1<rr<R and -1<cc<C and G[rr][cc] != ' ':
                d = i
                dr,dc = D[d]
                r,c = r + dr, c + dc
                break
        if G[rr][cc] == ' ':
            break
print('part 1:',path)
print('part 2:',step)
