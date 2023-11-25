n = int(input())
a = list(map(int, input().split()))
b = [0] * n
half = n // 2
b[half] = a[0]
for i in range(1, n):
    if i % 2 == 1:
        b[half - (i + 1) // 2] = a[i]
    else:
        b[half + i // 2] = a[i]
if n % 2 == 1:
    b.reverse()
print(*b)
