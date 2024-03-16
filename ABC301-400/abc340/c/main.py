import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n = int(input())
que = set()
que.add(n)
dict = defaultdict(int)
dict[n] = 1
ans = 0
while que:
    q = que.pop()
    ans += q * dict[q]
    floor = math.floor(q / 2)
    ceil = math.ceil(q / 2)
    if floor != 1:
        que.add(floor)
        dict[floor] += dict[q]
    if ceil != 1:
        que.add(ceil)
        dict[ceil] += dict[q]
    dict[q] = 0
print(ans)
