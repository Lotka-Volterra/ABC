n = int(input())
mod = 998244353
dp = [[0] * 9 for i in range(n)]
for i in range(9):
    dp[0][i] = 1
for i in range(n - 1):
    for j in range(9):
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= mod
        if j != 0:
            dp[i + 1][j - 1] += dp[i][j]
            dp[i + 1][j - 1] %= mod
        if j != 8:
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= mod
sum = 0
for i in range(9):
    sum += dp[n - 1][i]
    sum %= mod
print(sum)
