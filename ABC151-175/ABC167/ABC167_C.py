n, m, x = map(int, input().split())
a = []
c = []
minmoney = 10**8
for i in range(n):
    l = list(map(int, input().split()))
    c.append(l[0])
    a.append(l[1:])

# iから(1<<n)-1まで全探索。
for i in range(1 << n):
    alg = [0]*m
    summoney = 0
    for j in range(n):
        wari = 1 << j
        if (i//wari) % 2 == 1:
            summoney += c[j]
            for k in range(m):
                alg[k] += a[j][k]

    allokflag = True
    for each in range(m):
        if alg[each] < x:
            allokflag = False
            break
    if allokflag:
        if 0 < summoney < minmoney:
            minmoney = summoney

if minmoney < 10**8:
    print(minmoney)
else:
    print(-1)
