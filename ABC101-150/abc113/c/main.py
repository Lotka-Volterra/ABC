n, m = map(int, input().split())
PYI = []
for i in range(m):
    p, y = map(int, input().split())
    PYI.append([p, y, i])
PYI.sort()
idList = []
preP = PYI[0][0]
count = 1
for i in range(m):
    if PYI[i][0] != preP:
        count = 1
        preP = PYI[i][0]
    id = str(preP).zfill(6) + str(count).zfill(6)
    idList.append([PYI[i][2], id])
    count += 1
idList.sort()
for i in range(m):
    print(idList[i][1])
