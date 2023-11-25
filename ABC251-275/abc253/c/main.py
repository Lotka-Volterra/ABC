from collections import defaultdict

q = int(input())
s = set()
num = defaultdict(int)
for i in range(q):
    n, *xc = map(int, input().split())
    if n == 1:
        s.add(xc[0])
        num[xc[0]] += 1
    elif n == 2:
        num[xc[0]] = max(0, num[xc[0]] - xc[1])
        if num[xc[0]] == 0:
            s.discard(xc[0])
    else:
        s = sorted(s)
        print(s[-1] - s[0])
        s = set(s)
