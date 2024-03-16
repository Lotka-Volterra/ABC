import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
h, w, n = map(int, input().split())
t = input()
S = []
for i in range(h):
    hi = input()
    S.append(hi)
ans = 0
for i in range(h):
    for j in range(w):
        if S[i][j] == "#":
            continue
        position_h = i
        position_w = j
        ok = True
        for k in range(n):
            if t[k] == "L" and position_w != 0:
                position_w -= 1
            elif t[k] == "R" and position_w != w - 1:
                position_w += 1
            elif t[k] == "U" and position_h != 0:
                position_h -= 1
            elif t[k] == "D" and position_h != h - 1:
                position_h += 1
            if S[position_h][position_w] == "#":
                ok = False
                break
        if ok:
            ans += 1
print(ans)
