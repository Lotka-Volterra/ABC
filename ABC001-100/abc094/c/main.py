# n = int(input())
# x = list(map(int, input().split()))
# sortedX = sorted(x)
# lowMedian = sortedX[n // 2 - 1]
# highMedian = sortedX[n // 2]
# for i in x:
#     if i <= lowMedian:
#         print(highMedian)
#     else:
#         print(lowMedian)
# 模範解答。インデックスの比較で実装している
N = int(input())
X = list(map(int, input().split()))
A = X.copy()
A.sort()
# sort関数を使用してリストをソートし、ソート前とソート後の対応関係を idx 辞書で保存
idx = {A[i]: i for i in range(N)}

for i in range(N):
    j = idx[X[i]]
    if j < N // 2:
        print(A[N // 2])
    else:
        print(A[N // 2 - 1])
