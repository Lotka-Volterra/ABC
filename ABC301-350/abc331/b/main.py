import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n, s, m, l = map(int, input().split())
ans = float("INF")
for i in range(20):
    for j in range(20):
        for k in range(20):
            count = 12 * i + 8 * j + 6 * k
            if count >= n:
                ans = min(ans, l * i + m * j + s * k)
print(ans)
