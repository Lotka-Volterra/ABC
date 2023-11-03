n, m, t = map(int, input().split())
a = [0] + list(map(int, input().split()))
xy = [0] * n

for i in range(m):
    tempx, tempy = map(int, input().split())
    xy[tempx - 1] = tempy
# print(xy)
for i in range(1, n):
    if a[i] >= t:
        print("No")
        quit()
    t -= a[i]
    t += xy[i]
print("Yes")
