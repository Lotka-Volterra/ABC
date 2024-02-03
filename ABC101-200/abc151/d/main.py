from collections import deque

h, w = map(int, input().split())
s = [input() for i in range(h)]
# 地点1を出発地点として各地点への最短距離を出力する幅優先探索
que = deque()

ans = 0
# 上下左右
DX = [0, 0, -1, 1]
DY = [1, -1, 0, 0]
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            continue
        shortestPath = [[-1] * w for i in range(h)]
        # 出発地点から出発地点の距離は0
        shortestPath[i][j] = 0
        # 出発地点をキューに追加
        que.append([i, j])
        # キューが空になるまで実行
        while len(que) > 0:
            # 最も近い位置=queの最古要素を取得
            nearestPosition = que.popleft()
            # 最古要素に隣接する位置の最短距離を確定
            for dx, dy in zip(DX, DY):
                x = nearestPosition[0] + dx
                y = nearestPosition[1] + dy
                # 移動先のマスが範囲外ならスキップ
                if x < 0 or x > h - 1:
                    continue
                if y < 0 or y > w - 1:
                    continue
                # 隣接する位置で、壁ではく、かつ最短距離が確定していないものであれば、最短距離を確定し、キューに追加
                if s[x][y] == "." and shortestPath[x][y] == -1:
                    shortestPath[x][y] = (
                        shortestPath[nearestPosition[0]][nearestPosition[1]] + 1
                    )
                    que.append([x, y])
        for k in range(h):
            for l in range(w):
                ans = max(ans, shortestPath[k][l])
print(ans)
