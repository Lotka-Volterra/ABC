import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
# H行W列の行列に二次元配列を格納。
# H回の配列の入力をXに格納。

# 入力（前半）
N, Q = map(int, input().split())

X = [input() for i in range(N)]
# 配列 Z は二次元累積和計算用の、H+1行 W+1列の二次元配列。行、列を1つ多くとることで、境界を気にせず二次元累積和を計算できる。
Z = [[0] * (N) for i in range(N)]

# Q回の入力で、（A,B）から（C,D）に囲まれる長方形の面積を求めてくる。
# 入力（後半）
A = [None] * Q
B = [None] * Q
C = [None] * Q
D = [None] * Q
for i in range(Q):
    A[i], B[i], C[i], D[i] = map(int, input().split())

# 配列 Z は既に初期化済み
# 1からH列まで、横方向に累積和をとる。
for i in range(N):
    # 配列のインデックス=0は0が入っているので、累積和計算後の1行目も「0行目と計算前の1行目の和」として表せる。
    for j in range(N):
        if j != 0:
            Z[i][j] = Z[i][j - 1]
        if X[i][j] == "B":
            Z[i][j] += 1
# 縦方向に累積和をとる
for j in range(N):
    for i in range(N):
        if i != 0:
            Z[i][j] = Z[i - 1][j] + Z[i][j]
# 答えを求める
for i in range(Q):
    rightDown = (
        Z[(C[i]) % N][(D[i]) % N]
        + Z[(C[i]) % N][N - 1] * ((C[i] // N) - (A[i] // N))
        + Z[N - 1][(D[i]) % N] * ((D[i] // N) - (B[i] // N))
    )
    rightUp = Z[(A[i] - 1) % N][(D[i]) % N] + Z[(A[i]) % N][N - 1] * (
        (D[i] // N) - ((B[i] - 1) // N)
    )
    leftUp = Z[(A[i] - 1) % N][(B[i] - 1) % N]
    leftDown = Z[(C[i]) % N][(B[i] - 1) % N] + Z[(C[i]) % N][N - 1] * (
        ((C[i] - 1) // N) - ((A[i] - 1) // N)
    )
    print(rightUp)
#     print(Z[C[i]][D[i]] + Z[A[i] - 1][B[i] - 1] - Z[A[i] - 1][D[i]] - Z[C[i]][B[i] - 1])
