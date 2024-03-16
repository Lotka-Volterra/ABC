from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
num = defaultdict(int)
for i in range(n):
    num[a[i]] += 1
k = n // 2
ok = True
if n % 2 == 1:
    # n=2k+1の場合は、0が1個、他が2個ずつ。並び方は2**k通り
    for i in range(1, k + 1):
        if num[2 * i] != 2:
            ok = False
            break
    if num[0] != 1:
        ok = False
else:
    # n=2kの場合は、1,3,5,...,2k-1が2個ずつ。
    for i in range(1, k + 1):
        if num[2 * i - 1] != 2:
            ok = False
            break
if ok:
    ans = 1
    for i in range(k):
        ans *= 2
        ans %= 10**9 + 7
    print(ans)
else:
    print(0)
