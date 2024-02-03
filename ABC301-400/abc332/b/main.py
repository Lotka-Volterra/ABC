import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

k, g, m = map(int, input().split())
glass_water = 0
mug_water = 0
for i in range(k):
    if glass_water == g:
        glass_water = 0
    elif mug_water == 0:
        mug_water = m
    else:
        water = min(mug_water, g - glass_water)
        glass_water += water
        mug_water -= water
print(glass_water, mug_water)
