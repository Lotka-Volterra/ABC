import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
q = int(input())
stack = []
for i in range(q):
    a, b = map(int, input().split())
    if a == 1:
        stack.append(b)
    else:
        print(stack[-b])
