n, m, p = map(int, input().split())
count = 0
for i in range(1, n + 1):
    if (i - m) % p == 0:
        count += 1
print(count)
