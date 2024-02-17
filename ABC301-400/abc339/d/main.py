import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
from collections import deque

# 地点1を出発地点として各地点への最短距離を出力する幅優先探索
n = int(input())
que = deque()
S = []
player1_x = 0
player1_y = 0
player2_x = 0
player2_y = 0
player1_found = False
visited = defaultdict(bool)

for i in range(n):
    s = input()
    S.append(s)
    for j in range(n):
        if not player1_found and s[j] == "P":
            player1_x = i
            player1_y = j
            player1_found = True
        if player1_found and s[j] == "P":
            player2_x = i
            player2_y = j
visited[(player1_x, player1_y, player2_x, player2_y)] = True
count = [[[-1, -1] for i in range(n)] for j in range(n)]
# 出発地点をキューに追加
que.append([player1_x, player1_y, player2_x, player2_y])
count[player1_x][player1_y][0] = 0
count[player2_x][player2_y][0] = 0

# キューが空になるまで実行

while len(que) > 0:
    # 最も近い位置=queの最古要素を取得
    position = que.popleft()
    # 最古要素に隣接する位置の最短距離を確定
    # 上
    player1_x = position[0]
    player1_y = position[1]
    player2_x = position[2]
    player2_y = position[3]
    if player1_y - 1 >= 0 and S[player1_x][player1_y - 1] != "#":
        player1_y -= 1
    if player2_y - 1 >= 0 and S[player2_x][player2_y - 1] != "#":
        player2_y -= 1
    count[player1_x][player1_y][0] = count[position[0]][position[1]][0] + 1
    count[player2_x][player2_y][1] = count[position[2]][position[3]][1] + 1

    if player1_x == player2_x and player1_y == player2_y:
        print(count[position[0]][position[1]][0] + 1)
        quit()
    if not visited[(player1_x, player1_y, player2_x, player2_y)]:
        visited[(player1_x, player1_y, player2_x, player2_y)] = True
        que.append((player1_x, player1_y, player2_x, player2_y))
    # 下
    player1_x = position[0]
    player1_y = position[1]
    player2_x = position[2]
    player2_y = position[3]
    if player1_y + 1 < n and S[player1_x][player1_y + 1] != "#":
        player1_y += 1
    if player2_y + 1 < n and S[player2_x][player2_y + 1] != "#":
        player2_y += 1
    count[player1_x][player1_y][0] = count[position[0]][position[1]][0] + 1
    count[player2_x][player2_y][1] = count[position[2]][position[3]][1] + 1

    if player1_x == player2_x and player1_y == player2_y:
        print(count[position[0]][position[1]][0] + 1)
        quit()
    if not visited[(player1_x, player1_y, player2_x, player2_y)]:
        visited[(player1_x, player1_y, player2_x, player2_y)] = True
        que.append((player1_x, player1_y, player2_x, player2_y))

    # 右
    player1_x = position[0]
    player1_y = position[1]
    player2_x = position[2]
    player2_y = position[3]
    if player1_x + 1 < n and S[player1_x + 1][player1_y] != "#":
        player1_x += 1
    if player2_x + 1 < n and S[player2_x + 1][player2_y] != "#":
        player2_x += 1
    count[player1_x][player1_y][0] = count[position[0]][position[1]][0] + 1
    count[player2_x][player2_y][1] = count[position[2]][position[3]][1] + 1

    if player1_x == player2_x and player1_y == player2_y:
        print(count[position[0]][position[1]][0] + 1)
        quit()
    if not visited[(player1_x, player1_y, player2_x, player2_y)]:
        visited[(player1_x, player1_y, player2_x, player2_y)] = True
        que.append((player1_x, player1_y, player2_x, player2_y))
    # 左
    player1_x = position[0]
    player1_y = position[1]
    player2_x = position[2]
    player2_y = position[3]
    if player1_x - 1 >= 0 and S[player1_x - 1][player1_y] != "#":
        player1_x -= 1
    if player2_x - 1 >= 0 and S[player2_x - 1][player2_y] != "#":
        player2_x -= 1
    count[player1_x][player1_y][0] = count[position[0]][position[1]][0] + 1
    count[player2_x][player2_y][1] = count[position[2]][position[3]][1] + 1

    if player1_x == player2_x and player1_y == player2_y:
        print(count[position[0]][position[1]][0] + 1)
        quit()
    if not visited[(player1_x, player1_y, player2_x, player2_y)]:
        visited[(player1_x, player1_y, player2_x, player2_y)] = True
        que.append((player1_x, player1_y, player2_x, player2_y))
    print(count)
