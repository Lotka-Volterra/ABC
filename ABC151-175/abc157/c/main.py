n, m = map(int, input().split())
sc = []
for i in range(m):
    s, c = map(int, input().split())
    sc.append([s, c])
for i in range(1000):
    if len(str(i)) != n:
        continue
    ok = True
    for j in range(m):
        if str(i)[sc[j][0] - 1] != str(sc[j][1]):
            ok = False
    if ok:
        print(i)
        quit()
print(-1)
