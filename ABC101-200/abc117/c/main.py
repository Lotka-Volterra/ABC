# 方針
# コマの進む方向は一方向に統一しても構わない
# コマを置くのは、左端の座標と、直前に訪れる座標からの距離が離れている座標
n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
X = [[0, x[0]]]
for i in range(1, m):
    X.append([x[i] - x[i - 1], x[i]])
piece = set()
X.sort(reverse=True)
piece.add(x[0])
for i in range(min(n, m) - 1):
    piece.add(X[i][1])
ans = 0
for i in range(1, m):
    if x[i] not in piece:
        ans += x[i] - x[i - 1]
print(ans)
