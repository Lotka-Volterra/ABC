# PAST 202005 E Sprinkler
# 14行目の*yの*がExtended Iterable Unpacking Operatorという演算子。
# 「残りすべて」の入力をリストとして受け取る。
# つまり、入力のうち、最初の1つ目をt、2つ目をx、3つ目以降をリストyとして受け取る。
# もし入力が2つだけでも、空のリスト[]として受け取り、y==[]となる。
n, m, q = map(int, input().split())
g = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
c = [0] + list(map(int, input().split()))
for i in range(q):
    t, x, *y = map(int, input().split())
    print(c[x])
    if t == 1:
        for j in g[x]:
            c[j] = c[x]
    else:
        c[x] = y
