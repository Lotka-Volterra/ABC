import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

# 解説AC
a, m, l, r = map(int, input().split())
l -= a
r -= a

print(r // m - (l - 1) // m)
