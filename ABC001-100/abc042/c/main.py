n, k = map(int, input().split())
d = list(input().split())
for i in range(n, 10**5):
    ok = True
    for j in d:
        if j in str(i):
            ok = False
            break
    if ok:
        print(i)
        quit()
