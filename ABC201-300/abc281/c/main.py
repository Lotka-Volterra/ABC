n, t = map(int, input().split())
a = list(map(int, input().split()))
sumA = sum(a)
t %= sumA
total = 0
for i in range(n):
    if total < t <= total + a[i]:
        print(i + 1, t - total)
        quit()
    total += a[i]
