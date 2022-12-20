path = '1701.0'
# path = '1701.1'
pfix = '_inputs_/'

def main():
    file = open(pfix + path).read().strip()
    a = [s for s in file.split('\n')]
    print(a)
    res, res2 = 0, 0
    for s in a:
        res, res2 = solver1(s), solver2(s)
    print('Star 1:', res)
    print('Star 2:', res2)

def solver2(s: str) -> int:
    res = 0
    S = len(s)
    mid = S // 2
    for i in range(S):
        if i + mid < S and s[i] == s[i + mid]: res += 2 * int(s[i])
    return res

def solver1(s: str) -> int:
    # Z = ord('0')
    S = len(s)
    res = 0
    for i in range(S):
        if (i != S-1 and s[i] == s[i + 1]) or (i == S-1 and s[i] == s[0]):
            res += int(s[i])
    return res

if __name__ == '__main__':
    main()
