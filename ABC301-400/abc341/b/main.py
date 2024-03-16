import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n = int(input())
a = list(map(int, input().split()))
S = []
T = []
for i in range(n - 1):
    s, t = map(int, input().split())
    S.append(s)
    T.append(t)
for i in range(n - 1):
    shou = a[i] // S[i]
    a[i + 1] += T[i] * shou
print(a[n - 1])
