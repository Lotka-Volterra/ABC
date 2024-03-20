n = int(input())
X = []
Y = []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if (X[i] - X[k]) * (Y[i] - Y[j]) != (X[i] - X[j]) * (Y[i] - Y[k]):
                ans += 1
print(ans)
