n, m = map(int, input().split())
matrix = [[4 * 10**5] * n for i in range(n)]
for i in range(n):
    matrix[i][i] = 0
for i in range(m):
    a, b, t = map(int, input().split())
    matrix[a - 1][b - 1] = t
    matrix[b - 1][a - 1] = t
for k in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
ans = float("inf")
for i in range(n):
    ans = min(ans, max(matrix[i]))
print(ans)
