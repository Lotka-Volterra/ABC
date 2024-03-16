import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

n = int(input())
ans = "1"
for i in range(n):
    ans += "01"
print(ans)
