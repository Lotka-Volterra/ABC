n, m, k = map(int, input().split())
# i,j要素は、i項目までで和をjにする方法の総数
dp = [[0] * (k + 1) for i in range(n)]
mod = 998244353
for i in range(min(m, k)):
    dp[0][i + 1] = 1
for i in range(n - 1):
    for j in range(0, k + 1):
        for l in range(1, m + 1):
            if dp[i][j] != 0 and j + l <= k:
                dp[i + 1][j + l] += dp[i][j]
                dp[i + 1][j + 1] %= mod
    # print(dp)
ans = 0
for i in range(k + 1):
    ans += dp[n - 1][i]
    ans %= mod
print(ans)
