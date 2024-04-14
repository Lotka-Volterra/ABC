import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
s = input()
ans = set()
for i in range(len(s)):
    for j in range(1, len(s) + 1):
        ans.add(s[i : i + j])
print(len(ans))
