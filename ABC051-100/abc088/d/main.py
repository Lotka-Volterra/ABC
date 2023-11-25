from collections import deque

h, w = map(int, input().split())
s = [input() for i in range(h)]
que = deque()

# 上下左右
DX = [0, 0, -1, 1]
DY = [1, -1, 0, 0]
# 最短距離を格納する配列。今回、最短距離がない場合の-1で初期化
shortestPath = [[-1] * w for i in range(h)]

# 出発地点から出発地点の距離は0
shortestPath[0][0] = 0
# 出発地点をキューに追加
que.append([0, 0])
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
        # 隣接する位置で、色が白かつ最短距離が確定していないものであれば、最短距離を確定し、キューに追加
        if s[x][y] == "." and shortestPath[x][y] == -1:
            shortestPath[x][y] = (
                shortestPath[nearestPosition[0]][nearestPosition[1]] + 1
            )
            que.append([x, y])
if shortestPath[h - 1][w - 1] == -1:
    print(-1)
else:
    white = sum(i.count(".") for i in s)
    # 残す必要がある白色のマス = 最短距離（＝通る白色の地点）+ 出発地点（最初の白色の地点）
    # スコア = 全ての白色のマス(white) - 残す必要がある白色のマス
    print(white - (shortestPath[h - 1][w - 1] + 1))
