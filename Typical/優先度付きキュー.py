import heapq
q = int(input())
priority_que = []
# リストを優先度付きキューに変換（要素が入っている既存リストの場合は必要、今回は空のリストなので実は不要）
heapq.heapify(priority_que)

for i in range(q):
    query = list(input().split())
    # 優先度付きキューに追加
    if query[0] == '1':
        heapq.heappush(priority_que, int(query[1]))
    # キューの最小要素を表示
    elif query[0] == '2':
        print(priority_que[0])
    # キューの最小要素を削除
    else:
        heapq.heappop(priority_que)
