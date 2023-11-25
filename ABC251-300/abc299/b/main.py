def new_func(n, t, c, r, tvalue, tind):
    for i in range(n):
        if c[i] == t:
            if r[i] > tvalue:
                tind = i
                tvalue = r[i]
    return tind, tvalue


n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))
tind = 0
tvalue = 0
tind, tvalue = new_func(n, t, c, r, tvalue, tind)
if tvalue > 0:
    print(tind + 1)
else:
    t = c[0]
    tvalue = r[0]
    tind = 0
    tind, tvalue = new_func(n, t, c, r, tvalue, tind)
    print(tind + 1)
