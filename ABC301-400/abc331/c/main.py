import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

n = int(input())
a = list(map(int, input().split()))
sumA = sum(a)
indA = []
waList = [0] * n
for i in range(n):
    indA.append([a[i], i])
indA.sort()
count = 0
sameNumber = []
for i in range(n):
    count += 1
    sameNumber.append(indA[i][1])
    if i < n - 1 and indA[i][0] != indA[i + 1][0]:
        sumA -= count * indA[i][0]
        for j in sameNumber:
            waList[j] = sumA
        count = 0
        sameNumber.clear()
print(*waList)
