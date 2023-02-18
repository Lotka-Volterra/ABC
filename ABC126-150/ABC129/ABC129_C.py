n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(int(input()))
a = set(a)

dp = [0]*(n+1)
dp[0] = 1
for i in range(n):
    if i in a:
        continue
    if i != n-1:
        dp[i+2] += dp[i]
    dp[i+1] += dp[i]
print(dp[n] % 1000000007)
