import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

n, l = map(int, input().split())
a = list(map(int, input().split()))
count = 0
for i in range(n):
    if a[i] >= l:
        count += 1
print(count)
