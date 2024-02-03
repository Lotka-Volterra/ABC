s = input()
mod = 10**9 + 7
chokudai = "chokudai"
dp = [[0] * len(s) for i in range(9)]
for i in range(len(s)):
    dp[0][i] = 1
for i in range(1, 9):
    for j in range(len(s)):
        if s[j] == chokudai[i - 1]:
            dp[i][j] += dp[i - 1][j]
        if j != 0:
            dp[i][j] += dp[i][j - 1]
        dp[i][j] %= mod
print(dp[8][-1])
