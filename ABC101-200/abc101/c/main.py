import math

n, k = map(int, input().split())
a = list(map(int, input().split()))
order = a.index(1)
order += 1
ans = 100000
# 1の場所を中心として、左右に置き換える場所を広げていく。
# k個の範囲の中で、1の位置はk通り。
# それぞれについて、左側、右側に
for i in range(1, k + 1):
    # 1が含まれるk個の領域から左側の領域
    left = max(order - i, 0)
    # 1が含まれるk個の領域から右側の領域
    right = max(n - (order + (k - i)), 0)
    # k-1個ずつ1が増えていく。k-1で割る（切り上げ）回数+1が含まれるk個で1回
    ans = min(ans, 1 + math.ceil(left / (k - 1)) + math.ceil(right / (k - 1)))
print(ans)
