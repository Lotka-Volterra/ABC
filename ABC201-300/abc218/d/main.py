from collections import defaultdict

dict_x = defaultdict(list)
dict_y = defaultdict(list)
n = int(input())
XY = []
for i in range(n):
    x, y = map(int, input().split())
    XY.append([x, y])
    dict_x[x].append(y)
    dict_y[y].append(x)
count = 0
for i in range(n):
    x, y = XY[i]
    for j in dict_x[x]:
        for k in dict_y[y]:
            if k != x and j != y:
                if j in dict_x[k]:
                    count += 1
print(count // 4)
