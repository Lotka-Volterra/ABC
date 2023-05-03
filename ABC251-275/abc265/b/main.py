n, m, t = map(int, input().split())
a = list(map(int, input().split()))
xy = []
for i in range(m):
    x, y = map(int, input().split())
    xy.append([x, y])
flag = True
j = 0
for i in range(n):
    t -= a[i]
    if t <= 0:
        flag = False
        break
    if xy[j][0] == i + 1:
        t += xy[j][1]
        j += 1
print(["No", "Yes"][flag])
