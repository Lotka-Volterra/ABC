import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
s = input()
n = len(s)
str_dict = defaultdict(int)
for i in range(n):
    str_dict[s[i]] += 1
ans = n * (n - 1) // 2
same = False
for i in str_dict.values():
    if i > 1:
        ans -= i * (i - 1) // 2
        same = True
if same:
    ans += 1
print(ans)
