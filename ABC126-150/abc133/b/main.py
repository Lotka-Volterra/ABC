n, d = map(int, input().split())
x = []
for i in range(n):
    xi = list(map(int, input().split()))
    x.append(xi)
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        dis = 0
        for k in range(d):
            dis += (x[i][k] - x[j][k]) ** 2
        # dは最大で130**2くらいになる
        for k in range(1, 130):
            if k**2 == dis:
                ans += 1
print(ans)
