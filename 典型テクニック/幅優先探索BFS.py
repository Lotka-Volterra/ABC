from collections import deque

# 地点1を出発地点として各地点への最短距離を出力する幅優先探索
n, m = map(int, input().split())
que = deque()
# 隣接行列
adjacency_list = [[] for i in range(n + 1)]
# 最短距離を格納する配列。今回、最短距離がない場合の-1で初期化
shortest_path = [-1] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    adjacency_list[a].append(b)
    adjacency_list[b].append(a)
# 出発地点から出発地点の距離は0
shortest_path[1] = 0
# 出発地点をキューに追加
que.append(1)
# キューが空になるまで実行
while len(que) > 0:
    # 最も近い位置=queの最古要素を取得
    nearest_position = que.popleft()
    # 最古要素に隣接する位置の最短距離を確定
    for i in adjacency_list[nearest_position]:
        # 隣接する位置で、最短距離が確定していないものであれば、最短距離を確定し、キューに追加
        if shortest_path[i] == -1:
            shortest_path[i] = shortest_path[nearest_position] + 1
            que.append(i)
# 1からnまでの位置の最短距離を表示
for i in range(1, n + 1):
    print(shortest_path[i])
