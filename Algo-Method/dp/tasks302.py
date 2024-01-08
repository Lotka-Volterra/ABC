n, x, y = map(int, input().split())
a = [0] * n
a[0], a[1] = x, y
for i in range(2, n):
    a[i] = (a[i - 1] + a[i - 2]) % 100
print(a[n - 1])
