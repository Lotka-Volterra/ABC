import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n = int(input())
p = list(map(int, input().split()))
dict = defaultdict(int)
for i in range(n):
    dict[p[i]] = i
q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    if dict[a] < dict[b]:
        print(a)
    else:
        print(b)
