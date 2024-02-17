import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

n = int(input())
a = list(map(int, input().split()))
jokyaku = 0
for i in range(n):
    jokyaku += a[i]
    if jokyaku < 0:
        jokyaku = 0
print(jokyaku)
