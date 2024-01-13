n, m = map(int, input().split())
# ccをSに変換するためにまずm//2をする。Sccは、S1個とc2個、つまりS2個出できているのでさらに2で割る。
# ちなみにc6個でSccが1個できる。
if n >= m / 2:
    print(m // 2)
else:
    print((n + m // 2) // 2)
