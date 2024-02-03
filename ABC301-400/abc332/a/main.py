import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

n, s, k = map(int, input().split())
price = 0
for i in range(n):
    p, q = map(int, input().split())
    price += p * q
if price >= s:
    print(price)
else:
    print(price + k)
