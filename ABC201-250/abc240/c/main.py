n, x = map(int, input().split())
A, B = [], []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
dp = [[0] * (10001) for i in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(10001):
        if dp[i][j] == 1:
            if j + A[i] <= 10001:
                dp[i + 1][j + A[i]] = 1
            if j + B[i] <= 10001:
                dp[i + 1][j + B[i]] = 1
if dp[n][x] == 1:
    print("Yes")
else:
    print("No")
