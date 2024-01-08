import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n = int(input())
h = list(map(int, input().split()))
dp = [[10**10] * n for i in range(n)]
dp[0][0] = 0
for i in range(n - 1):
    for j in range(n):
        if dp[i][j] != 10**10:
            if j + 1 < n:
                dp[i + 1][j + 1] = min(
                    dp[i][j] + abs(h[j] - h[j + 1]), dp[i + 1][j + 1]
                )
            if j + 2 < n:
                dp[i + 1][j + 2] = min(
                    dp[i][j] + abs(h[j] - h[j + 2]), dp[i + 1][j + 2]
                )
            if j == n - 1:
                dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])
print(dp[n - 1][n - 1])
