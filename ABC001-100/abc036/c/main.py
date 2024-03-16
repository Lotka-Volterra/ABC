from collections import defaultdict

n = int(input())
a = []
# 行だけ（圧縮のため集合を使う）
A = set()
# 列だけ
B = set()

# 連想配列で、圧縮前の座標と圧縮後の座標を関連付ける
a_order = defaultdict(int)
for i in range(n):
    ai = int(input())
    A.add(ai)
    a.append(ai)
# 行だけ、列だけでソートする。
A = sorted(list(A))
# 圧縮すると、行1=1番目、行3=1番目、行5=3番目の行になる。この対応付けに連想配列を用いる
for i in range(len(A)):
    a_order[A[i]] = i
for i in range(n):
    print(a_order[a[i]])
