from collections import deque

que = deque()

n, x, y = map(int, input().split())
# 隣接行列。頂点0から頂点nまで合計n+1のリストに、各頂点iと隣接する頂点のリストを作成
adjacencyList = [[] for i in range(n + 1)]
adjacencyList[x].append(y)
adjacencyList[y].append(x)

for i in range(1, n):
    adjacencyList[i].append(i + 1)
    adjacencyList[i + 1].append(i)
ans = [0] * (n + 1)
for h in range(1, n + 1):
    # 最短距離を格納する配列。今回、最短距離がない場合の-1で初期化
    shortestPath = [-1] * (n + 1)
    # 出発地点から出発地点の距離は0
    shortestPath[h] = 0
    # 出発地点をキューに追加
    que.append(h)
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
                if i > h:
                    ans[shortestPath[i]] += 1

for i in range(1, n):
    print(ans[i])
