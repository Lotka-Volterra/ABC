import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
a, b = map(int, input().split())
for i in range(10):
    if i != a + b:
        print(i)
        quit()
