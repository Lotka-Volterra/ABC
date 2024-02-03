n, k = list(map(int, input().split()))
total = 0
for i in range(1, n + 1):
    total += 1 / 2 * k * (k + 1) + 100 * k * i
print(int(total))
