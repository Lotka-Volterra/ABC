import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n = int(input())
oishisa = defaultdict(int)
for i in range(n):
    a, c = map(int, input().split())
    if oishisa[c] == 0:
        oishisa[c] = a
    else:
        oishisa[c] = min(oishisa[c], a)
print(max(oishisa.values()))
