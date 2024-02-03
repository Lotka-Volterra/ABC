from collections import defaultdict, deque

n = int(input())
stair = defaultdict(set)
for i in range(n):
    a, b = map(int, input().split())
    stair[a].add(b)
    stair[b].add(a)
que = deque()
ans = {1}
# 出発地点をキューに追加
que.append(1)
# キューが空になるまで実行
while len(que) > 0:
    # 最も近い位置=queの最古要素を取得
    nearestPosition = que.popleft()
    for i in stair[nearestPosition]:
        # はしごで到達する階で、その階からの到達階の精査が完了していないものであれば、キューに追加
        if i not in ans:
            que.append(i)
            ans.add(i)
print(max(ans))
