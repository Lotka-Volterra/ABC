n = int(input())
a = list(map(int, input().split()))
bunshi = 0
bunbo = 0
for i in range(n):
    if a[i] > 0:
        bunshi += a[i]
        bunbo += 1
print((bunshi + bunbo - 1) // bunbo)
