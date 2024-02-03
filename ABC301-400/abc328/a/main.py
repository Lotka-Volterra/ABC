import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

n, x = map(int, input().split())
s = list(map(int, input().split()))
ans = 0
for i in range(n):
    if s[i] <= x:
        ans += s[i]
print(ans)
