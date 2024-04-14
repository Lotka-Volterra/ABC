import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n, m = map(int, input().split())
s = input()
plain_t = m
log_t = 0
worn_logo_t = 0
for i in range(n):
    if s[i] == "0":
        plain_t = m
        worn_logo_t = 0
    elif s[i] == "1":
        if plain_t > 0:
            plain_t -= 1
        else:
            if log_t == worn_logo_t:
                log_t += 1
            worn_logo_t += 1
    else:
        if log_t == worn_logo_t:
            log_t += 1
        worn_logo_t += 1
print(log_t)
