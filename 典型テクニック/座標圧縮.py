# ABC213 C

from collections import defaultdict

h, w, n = map(int, input().split())
# 行と列の情報を格納するリスト
AB = []
# 行だけ（圧縮のため集合を使う）
A = set()
# 列だけ
B = set()
# 連想配列で、圧縮前の座標と圧縮後の座標を関連付ける
a_order = defaultdict(int)
b_order = defaultdict(int)
for i in range(n):
    a, b = map(int, input().split())
    A.add(a)
    B.add(b)
    AB.append([a, b])
# 行だけ、列だけでソートする。
A = sorted(list(A))
B = sorted(list(B))
# たとえば、行が[3,1,5]なら[1,3,5]になっている状態。
# 圧縮すると、行1=1番目、行3=1番目、行5=3番目の行になる。この対応付けに連想配列を用いる
for i in range(len(A)):
    a_order[A[i]] = i + 1
for i in range(len(B)):
    b_order[B[i]] = i + 1
for i in range(n):
    print(a_order[AB[i][0]], b_order[AB[i][1]])
