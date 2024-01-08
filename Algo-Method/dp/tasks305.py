n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    else:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
print(dp[-1])
