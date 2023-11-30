n, x, y = map(int, input().split())
jewels = [[0, 0] for i in range(n)]
jewels[0][0] = 1
for i in range(n - 1):
    # 赤の宝石の変換
    jewels[i + 1][0] += jewels[i][0]
    jewels[i][1] += jewels[i][0] * x
    # 青の宝石の変換
    jewels[i + 1][0] += jewels[i][1]
    jewels[i + 1][1] += jewels[i][1] * y
print(jewels[n - 1][1])
