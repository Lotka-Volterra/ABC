# aの最大の要素をk,2番目に大きい要素をk'とする。
# ai==kのとき、kが複数あるならk、kが一つならk'を出力（いずれにしてもaの降順ソートした後の2番目）
# ai!=kのとき、kを出力
n = int(input())
a = [int(input()) for i in range(n)]
sortedA = sorted(a, reverse=True)
maxA = sortedA[0]
secondA = sortedA[1]
for i in range(n):
    if a[i] == maxA:
        print(secondA)
    else:
        print(maxA)
