n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
adp = [False] * n
bdp = [False] * n
adp[0] = True
bdp[0] = True
for i in range(n - 1):
    adp[i + 1] = (adp[i] and abs(a[i + 1] - a[i]) <= k) or (
        bdp[i] and abs(a[i + 1] - b[i]) <= k
    )
    bdp[i + 1] = (adp[i] and abs(b[i + 1] - a[i]) <= k) or (
        bdp[i] and abs(b[i + 1] - b[i]) <= k
    )
if adp[n - 1] or bdp[n - 1]:
    print("Yes")
else:
    print("No")
