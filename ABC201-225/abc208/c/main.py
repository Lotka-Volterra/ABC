h, w = list(map(int, input().split()))
s = []
for i in range(h):
    si = list(map(int, input().split()))
    s.append(si)
dp = [[0] * w for i in range(h)]
for i in range(w):
    dp[0][i] = s[0][i]
for i in range(1, h):
    for j in range(w):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + s[i][j]
            dp[i][j + 1] = dp[i - 1][j] + s[i][j + 1]
        elif j == w - 1:
            dp[i][j - 1] = max(dp[i - 1][j] + s[i][j - 1], dp[i][j - 1])
            dp[i][j] = max(dp[i - 1][j] + s[i][j], dp[i][j])
        else:
            dp[i][j - 1] = max(dp[i - 1][j] + s[i][j - 1], dp[i][j - 1])
            dp[i][j] = max(dp[i - 1][j] + s[i][j], dp[i][j])
            dp[i][j + 1] = max(dp[i - 1][j] + s[i][j + 1], dp[i][j + 1])
print(max(dp[h - 1]))
