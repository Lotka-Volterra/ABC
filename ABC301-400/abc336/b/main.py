import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

n = int(input())
ans = 0
for i in range(1, 31):
    if n % (2**i) == 0:
        ans += 1
print(ans)
