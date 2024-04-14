import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n = int(input())
X = []
Y = []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
for i in range(n):
    dist = 0
    ans = n
    for j in range(n):
        if (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2 > dist:
            ans = j + 1
            dist = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
    print(ans)
