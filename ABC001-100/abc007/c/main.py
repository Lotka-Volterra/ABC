from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
s = [input() for i in range(r)]
que = deque()

# 上下左右
DX = [0, 0, -1, 1]
DY = [1, -1, 0, 0]
# 最短距離を格納する配列。今回、最短距離がない場合の-1で初期化
shortestPath = [[-1] * c for i in range(r)]

# 出発地点から出発地点の距離は0
shortestPath[sy - 1][sx - 1] = 0
# 出発地点をキューに追加
que.append([sy - 1, sx - 1])
# キューが空になるまで実行
while len(que) > 0:
    # 最も近い位置=queの最古要素を取得
    nearestPosition = que.popleft()
    # 最古要素に隣接する位置の最短距離を確定
    for dx, dy in zip(DX, DY):
        x = nearestPosition[0] + dx
        y = nearestPosition[1] + dy
        # 移動先のマスが範囲外ならスキップ
        if x < 0 or x > r - 1:
            continue
        if y < 0 or y > c - 1:
            continue
        # 隣接する位置で、空きマスかつ最短距離が確定していないものであれば、最短距離を確定し、キューに追加
        if s[x][y] == "." and shortestPath[x][y] == -1:
            shortestPath[x][y] = (
                shortestPath[nearestPosition[0]][nearestPosition[1]] + 1
            )
            que.append([x, y])
        if x == gy - 1 and y == gx - 1:
            break
print(shortestPath[gy - 1][gx - 1])
