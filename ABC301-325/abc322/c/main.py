n, m = map(int, input().split())
a = list(map(int, input().split()))
ai = 0
lena = len(a)
for i in range(1, n + 1):
    if ai == lena:
        print(0)
        continue
    print(a[ai] - i)
    if a[ai] == i:
        ai += 1
