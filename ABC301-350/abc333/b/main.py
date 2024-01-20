import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

s = "".join(sorted(input()))
t = "".join(sorted(input()))
length1 = ["AB", "BC", "CD", "DE", "AE"]
if (s in length1 and t in length1) or (s not in length1 and t not in length1):
    print("Yes")
else:
    print("No")

# 模範解答：長さが短い方→文字同士が隣接している→文字の引き算をすると、1か4（AとE）で判定
