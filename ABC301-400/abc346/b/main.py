import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
w, b = map(int, input().split())
s = "wbwbwwbwbwbw" * 100
for i in range(200):
    wcount = 0
    bcount = 0
    for j in range(w + b):
        if s[i + j] == "w":
            wcount += 1
        else:
            bcount += 1
    if wcount == w and bcount == b:
        print("Yes")
        quit()
print("No")
