# from collections import deque

# 地点1を出発地点として各地点への最短距離を出力する幅優先探索
h, w = map(int, input().split())
# 隣接行列
adjacency_list = [list(map(int, input().split())) for i in range(10)]

h_w = [list(map(int, input().split())) for i in range(h)]
# 最短距離を格納する配列。今回、最短距離がない場合の-1で初期化
shortest_path = [-1] * (10)
# 出発地点から出発地点の距離は0
shortest_path[1] = 0
# 出発地点をキューに追加
for k in range(10):
    for i in range(10):
        for j in range(10):
            adjacency_list[i][j] = min(
                adjacency_list[i][j], adjacency_list[i][k] + adjacency_list[k][j]
            )
for i in range(10):
    shortest_path[i] = adjacency_list[i][1]
ans = 0
for i in range(h):
    for j in range(w):
        if h_w[i][j] == -1:
            continue
        ans += shortest_path[h_w[i][j]]
print(ans)
