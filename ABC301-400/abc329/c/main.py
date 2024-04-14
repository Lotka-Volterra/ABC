import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n = int(input())
s = input()
s = s + "Z"
ans = 0
str_dict = defaultdict(int)
count = 0
for i in range(n):
    count += 1
    if s[i] != s[i + 1]:
        str_dict[s[i]] = max(str_dict[s[i]], count)
        count = 0

for i in str_dict.values():
    ans += i
print(ans)
