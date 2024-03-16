import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n = int(input())
ans = 1
for i in range(1, n + 1):
    if i**3 > n:
        break
    str_k = str(i**3)
    is_kaibun = True
    for i in range(len(str_k)):
        if str_k[i] != str_k[len(str_k) - i - 1]:
            is_kaibun = False
            break
    if is_kaibun:
        ans = int(str_k)
print(ans)
