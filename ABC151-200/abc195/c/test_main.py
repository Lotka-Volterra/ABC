def Ans(n):
    ans = 0
    if n >= 1000:
        ans += n - 999
    if n >= 1000000:
        ans += n - 999999
    if n >= 1000000000:
        ans += n - 999999999
    if n >= 1000000000000:
        ans += n - 999999999999
    if n >= 1000000000000000:
        ans += n - 999999999999999
    return ans


def myAns(n):
    lenN = len(str(n))
    lenNDiv = (lenN - 1) // 3
    ans = 0
    for i in range(1, lenNDiv + 1):
        # 10**3倍ごとに考える。つまり、10**3.10**6,10**9...
        # 10**3倍ごとの区切りで、コンマが書かれる数は、(min(10 ** (3 * (i + 1)) - 1, n) - (10 ** (3 * i) - 1))
        # その区切りの一つ一つの数で書かれるコンマの数はi
        ans += (min(10 ** (3 * (i + 1)) - 1, n) - (10 ** (3 * i) - 1)) * i
    return ans


for i in range(10**3, 10**6):
    if myAns(i) != Ans(i):
        print(i, myAns(i), Ans(i))
