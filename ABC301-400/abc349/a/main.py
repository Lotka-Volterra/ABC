import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    ans += i
print(-ans)
