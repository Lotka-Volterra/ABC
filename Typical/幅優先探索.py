from collections import deque

n, m = map(int, input().split())
que = deque()
# 隣接行列
adjacencyList = [[] for i in range(n + 1)]
# 最短距離を格納する配列。今回、最短距離がない場合の-1で初期化
shortestPath = [-1] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    adjacencyList[a].append(b)
    adjacencyList[b].append(a)
# 出発地点から出発地点の距離は0
shortestPath[1] = 0
# 出発地点をキューに追加
que.append(1)
# キューが空になるまで実行
while len(que) > 0:
    # 最も近い位置=queの最古要素を取得
    nearestPosition = que.popleft()
    # 最古要素に隣接する位置の最短距離を確定
    for i in adjacencyList[nearestPosition]:
        # 隣接する位置で、最短距離が確定していないものであれば、最短距離を確定し、キューに追加
        if shortestPath[i] == -1:
            shortestPath[i] = shortestPath[nearestPosition] + 1
            que.append(i)
# 1からnまでの位置の最短距離を表示
for i in range(1, n + 1):
    print(shortestPath[i])
