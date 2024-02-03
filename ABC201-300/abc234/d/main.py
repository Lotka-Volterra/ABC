import heapq

n, k = map(int, input().split())
p = list(map(int, input().split()))
heap_p = p[:k]
heapq.heapify(heap_p)

for i in range(n - k + 1):
    # k個の要素の中で最小値を出力
    min_value = heapq.heappop(heap_p)
    print(min_value)
    # p[k+i]と先程出力した最小値を比較して、大きい方をheqp pueに追加。
    # 小さい場合はこれ以降k+1番目以降に大きい数にしかなり得ないため、大きい方を追加
    if i != n - k:
        heapq.heappush(heap_p, max(min_value, p[k + i]))
