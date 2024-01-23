import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n = int(input())
takahashi = 0
aoki = 0
for i in range(n):
    x, y = map(int, input().split())
    takahashi += x
    aoki += y
if takahashi > aoki:
    print("Takahashi")
elif takahashi < aoki:
    print("Aoki")
else:
    print("Draw")
