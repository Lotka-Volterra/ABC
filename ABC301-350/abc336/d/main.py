import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

n = int(input())
a = list(map(int, input().split()))
left = [0] * n
right = [0] * n
count_left = 0
count_right = 0
for i in range(n):
    if a[i] > count_left:
        count_left += 1
        left[i] = count_left
    else:
        left[i] = min(left[i - 1], a[i])
        count_left = min(left[i - 1], a[i])
a.reverse()
for i in range(n):
    if a[i] > count_right:
        count_right += 1
        right[i] = count_right
    else:
        right[i] = min(right[i - 1], a[i])
        count_right = min(right[i - 1], a[i])
ans = 0
right.reverse()
for i in range(n):
    ans = max(ans, min(left[i], right[i]))
print(ans)
# 初めてコンテスト中にD問題解いた
