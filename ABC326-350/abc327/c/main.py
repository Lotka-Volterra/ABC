a = []
for i in range(9):
    a.append(list(map(int, input().split())))
columnFlag = True
for i in range(9):
    if len(set(a[i])) != 9:
        columnFlag = False
lineFlag = True
for i in range(9):
    aline = []
    for j in range(9):
        aline.append(a[j][i])
    if len(set(aline)) != 9:
        lineFlag = False
corner = [0, 3, 6]
box = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
boxflag = True
for i in corner:
    for j in corner:
        boxCell = []
        for k in range(9):
            boxCell.append(a[i + box[k][0]][j + box[k][1]])
        if len(set(boxCell)) != 9:
            boxflag = False
if columnFlag and lineFlag and boxflag:
    print("Yes")
else:
    print("No")
