a, b, c, x, y = map(int, input().split())
z = max(x, y)
ans = 2 * 10**9
# ABピザの枚数を全探索する
# ABピザは偶数枚ずつ買うとする
for i in range(z + 1):
    restX = max(x - i, 0)
    restY = max(y - i, 0)
    ans = min(ans, 2 * c * i + a * restX + b * restY)
print(ans)
