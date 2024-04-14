import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n, k = map(int, input().split())
a = list(map(int, input().split()))
num = set()
for i in range(n):
    if 1 <= a[i] <= k:
        num.add(a[i])
ans = 0
for i in num:
    ans += i
print(k * (k + 1) // 2 - ans)
