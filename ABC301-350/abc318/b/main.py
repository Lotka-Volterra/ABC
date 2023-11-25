masu = [[0] * 101 for i in range(101)]
n = int(input())
for i in range(n):
    a, b, c, d = map(int, input().split())
    for j in range(a + 1, b + 1):
        for k in range(c + 1, d + 1):
            masu[j][k] = 1
print(sum(sum(row) for row in masu))
# メモ：面積=正方形のマスの数と考える。そのマスが1なら面積としてカウント
# a,b,c,dで囲われる領域を1にする。すでに1ならそのまま
# 境界値に対応するため、マスは101*101にしている