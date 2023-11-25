n, m = map(int, input().split())
pce = []
for i in range(n):
    pce.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if pce[i][0] >= pce[j][0]:
            jHasAll = True
            for k in range(2, len(pce[i])):
                if pce[i][k] not in pce[j][2:]:
                    jHasAll = False
            if jHasAll:
                if pce[i][0] > pce[j][0] or len(pce[i]) < len(pce[j]):
                    print("Yes")
                    quit()
print("No")
