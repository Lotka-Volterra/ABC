n, m, x = map(int, input().split())
a = list(map(int, input().split()))
tozero = 0
for i in range(m):
    if a[i] < x:
        tozero += 1
print(min(tozero, m - tozero))
