import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

h, w = map(int, input().split())
A = []
start = 0
goal = 0
for i in range(h):
    a = list(input())
    A.append(a)
    for j in range(w):
        if a[j] == "S":
            start = [i, j]
        elif a[j] == "T":
            goal = [i, j]
n = int(input())
# medicine = defaultdict(int)
# energy = []
# for i in range(n):
#     r, c, e = map(int, input().split())
#     medicine.append([r, c])
#     energy.append(e)
energy = 0
is_startable = False
for i in range(n):
    r, c, e = map(int, input().split())
    if r - 1 == start[0] and c - 1 == start[1]:
        is_startable = True
        energy = e
        continue
    A[r - 1][c - 1] = e
if not is_startable:
    print("No")
    quit()

que = deque()
# 上下左右
DX = [0, 0, -1, 1]
DY = [1, -1, 0, 0]
# 最短距離を格納する配列。今回、最短距離がない場合の-1で初期化
shortestPath = [[-1] * w for i in range(h)]
# 出発地点から出発地点の距離は0
shortestPath[start[0]][start[1]] = energy
# 出発地点をキューに追加
que.append([start[0], start[1], energy])
# キューが空になるまで実行
while len(que) > 0:
    # 最も近い位置=queの最古要素を取得
    nearestPosition = que.popleft()
    # 最古要素に隣接する位置の最短距離を確定
    current_x = nearestPosition[0]
    current_y = nearestPosition[1]
    current_energy = nearestPosition[2]
    if current_energy == 0:
        shortestPath[current_x][current_y] = 0
        continue
    for dx, dy in zip(DX, DY):
        x = current_x + dx
        y = current_y + dy
        # 移動先のマスが範囲外ならスキップ
        if x < 0 or x > h - 1:
            continue
        if y < 0 or y > w - 1:
            continue
        temp_energy = current_energy - 1
        # 隣接する位置で、最短距離が確定していないものであれば、最短距離を確定し、キューに追加
        if A[x][y] != "#" and (
            shortestPath[x][y] == -1 or temp_energy > shortestPath[x][y]
        ):
            if A[x][y] == "T":
                print("Yes")
                quit()
            # print(A[x][y])
            if A[x][y] != "." and A[x][y] != "S":
                temp_energy = max(temp_energy, A[x][y])
            shortestPath[x][y] = temp_energy
            que.append([x, y, temp_energy])
print("No")
