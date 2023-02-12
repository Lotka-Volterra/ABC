#H行W列の行列に二次元配列を格納。
#H回の配列の入力をXに格納。

# 入力（前半）
H, W = map(int, input().split())
X = [ None ] * (H)
#配列 Z は二次元累積和計算用の、H+1行 W+1列の二次元配列。行、列を1つ多くとることで、境界を気にせず二次元累積和を計算できる。
Z = [ [ 0 ] * (W + 1) for i in range(H + 1) ]
for i in range(H):
	X[i] = list(map(int, input().split()))

#Q回の入力で、（A,B）から（C,D）に囲まれる長方形の面積を求めてくる。
# 入力（後半）
Q = int(input())
A = [ None ] * Q
B = [ None ] * Q
C = [ None ] * Q
D = [ None ] * Q
for i in range(Q):
	A[i], B[i], C[i], D[i] = map(int, input().split())

# 配列 Z は既に初期化済み
# 1からH列まで、横方向に累積和をとる。
for i in range(1, H+1):
    #配列のインデックス=0は0が入っているので、累積和計算後の1行目も「0行目と計算前の1行目の和」として表せる。
	for j in range(1, W+1):
		Z[i][j] = Z[i][j-1] + X[i-1][j-1]


# 縦方向に累積和をとる
for j in range(1, W+1):
	for i in range(1, H+1):
		Z[i][j] = Z[i-1][j] + Z[i][j]


# 答えを求める
for i in range(Q):
	print(Z[C[i]][D[i]] + Z[A[i]-1][B[i]-1] - Z[A[i]-1][D[i]] - Z[C[i]][B[i]-1])

# 配列 Z の[i][j]要素は、H行W列の配列の[i-i][j-1]要素に相当。
TwoDimensionalSum=[Z[i][1:] for i in range(1,H+1)]

