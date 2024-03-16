import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

n, t = map(int, input().split())
dict = defaultdict(int)
for i in range(n):
    dict[i + 1] = 0
point_dict = defaultdict(int)
point_dict[0] = n
ans = 1
for i in range(t):
    a, b = map(int, input().split())
    point_dict[dict[a]] = max(0, point_dict[dict[a]] - 1)
    if point_dict[dict[a]] == 0:
        ans -= 1
    dict[a] += b
    point_dict[dict[a]] += 1
    if point_dict[dict[a]] == 1:
        ans += 1
    print(ans)
