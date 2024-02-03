import itertools
from collections import defaultdict

n, m = map(int, input().split())
takahashi = [[0] * n for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    takahashi[a - 1][b - 1] = 1
    takahashi[b - 1][a - 1] = 1
aokiHimo = [list(map(int, input().split())) for i in range(m)]
seq = list(range(n))
for i in list(itertools.permutations(seq)):
    dict = defaultdict(int)
    for j in range(n):
        dict[j] = i[j]
    aoki = [[0] * n for i in range(n)]
    for j in aokiHimo:
        aoki[dict[j[0] - 1]][dict[j[1] - 1]] = 1
        aoki[dict[j[1] - 1]][dict[j[0] - 1]] = 1
    isSame = True
    for j in range(n):
        if aoki[j] != takahashi[j]:
            isSame = False
            break
    if isSame:
        print("Yes")
        quit()
print("No")
