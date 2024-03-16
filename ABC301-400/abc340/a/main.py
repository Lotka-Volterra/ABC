import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
a, b, d = map(int, input().split())

ans = [a]
while a < b:
    a += d
    ans.append(a)
print(*ans)
# 模範解答　for文を適切に使う
print(*range(a, b + 1, d))
