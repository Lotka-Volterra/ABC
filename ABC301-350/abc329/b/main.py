import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

n = int(input())
a = list(map(int, input().split()))
a = list(set(a))
a.sort(reverse=True)
print(a[1])
