import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

b, g = map(int, input().split())
if b > g:
    print("Bat")
else:
    print("Glove")
