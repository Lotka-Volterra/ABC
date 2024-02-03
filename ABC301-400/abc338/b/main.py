import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
s = input()
dict = defaultdict(int)
for i in s:
    dict[i] += 1
order = []
for i in dict:
    order.append([1000 - dict[i], i])
order.sort()
print(order[0][1])
