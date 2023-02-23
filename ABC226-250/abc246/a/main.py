x = []
y = []
for i in range(3):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
xans = 0
yans = 0
for i in range(3):
    if x.count(x[i]) == 1:
        xans = x[i]
    if y.count(y[i]) == 1:
        yans = y[i]
print(xans, yans)
