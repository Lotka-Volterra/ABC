# 自身＋隣接するマスの数だけ反転する→裏になるのはこのマスの数が奇数の場合。
# 1行1列の場合は、裏になる。
def myAns(n, m):
    if n == 1 and m == 1:
        return 1
    # 1列かつ奇数行の場合は両端のマス以外が裏になる。
    elif n == 1 and m % 2 == 1:
        return m - 2
    # 1行かつ奇数列の場合は両端のマス以外が裏になる。
    elif m == 1 and n % 2 == 1:
        return n - 2
    # 2行あるいは2列の場合は裏になるマスはない（下のelseに統合できる）
    elif m == 2 or n == 2:
        return 0
    # 上記以外の場合、外側に位置しないマスが裏になる
    else:
        return (m - 2) * (n - 2)


def Mohan(n, m):
    #!/usr/bin/env python
    if n > 1:
        n = n - 2
    if m > 1:
        m = m - 2
    return n * m


for i in range(1, 1000):
    for j in range(1, 1000):
        if myAns(i, j) != Mohan(i, j):
            print(i, j)
# n=1,m=4など、nとmのどちらかが1かつもう一方が偶数の場合、myAnsはうまく判定ができていなかった
