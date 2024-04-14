import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    if a[i] % k == 0:
        ans.append(a[i] // k)
print(*ans)
