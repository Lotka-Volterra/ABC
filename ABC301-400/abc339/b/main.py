import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
h, w, n = map(int, input().split())
HW = [["."] * w for i in range(h)]
position_h = 0
position_w = 0
direction = "U"
for i in range(n):
    if HW[position_h][position_w] == ".":
        HW[position_h][position_w] = "#"
        if direction == "U":
            direction = "R"
            position_w += 1
        elif direction == "R":
            direction = "D"
            position_h += 1
        elif direction == "D":
            direction = "L"
            position_w -= 1
        else:
            direction = "U"
            position_h -= 1
    else:
        HW[position_h][position_w] = "."
        if direction == "U":
            direction = "L"
            position_w -= 1
        elif direction == "R":
            direction = "U"
            position_h -= 1
        elif direction == "D":
            direction = "R"
            position_w += 1
        else:
            direction = "D"
            position_h += 1
    if position_w == w:
        position_w = 0
    if position_h == h:
        position_h = 0
    if position_w == -1:
        position_w = w - 1
    if position_h == -1:
        position_h = h - 1
    # print(direction, position_h, position_w)
    # print(HW)
for i in range(h):
    print("".join(HW[i]))
