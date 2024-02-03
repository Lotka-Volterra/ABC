import math

n = int(input())
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
maxlen = 0
for i in range(n - 1):
    for j in range(1, n):
        maxlen = max(maxlen, (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
print(math.sqrt(maxlen))
