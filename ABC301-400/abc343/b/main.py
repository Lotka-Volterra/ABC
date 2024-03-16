import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n = int(input())
A = []
for i in range(n):
    a = list(map(int, input().split()))
    A.append(a)
for i in range(n):
    ans = []
    for j in range(n):
        if A[i][j] == 1:
            ans.append(j + 1)
    print(*ans)
