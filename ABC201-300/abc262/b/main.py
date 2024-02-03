n, m = map(int, input().split())
graph = [[0] * n for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u - 1][v - 1] = 1
    graph[v - 1][u - 1] = 1
ans = 0
for i in range(n):
    for j in range(n - 1):
        for k in range(j, n):
            if graph[i][j] == 1 and graph[i][k] == 1 and graph[j][k] == 1:
                ans += 1
print(ans // 3)
