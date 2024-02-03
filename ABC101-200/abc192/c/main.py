n, k = map(int, input().split())
ans = n
for i in range(k):
    listAns = list(str(ans))
    listAns.sort(reverse=True)
    g1 = ""
    for i in listAns:
        g1 += i
    listAns.sort()
    g2 = ""
    for i in listAns:
        if i != 0:
            g2 += i
    ans = str(int(g1) - int(g2))
print(ans)


# 模範解答。0埋めの文字列でもintでうまく変換してくれる
def g1(n):
    return int("".join(sorted(str(n))[::-1]))


def g2(n):
    return int("".join(sorted(str(n))))


def f(n):
    return g1(n) - g2(n)


N, K = map(int, input().split())
for _ in range(K):
    N = f(N)
print(N)
