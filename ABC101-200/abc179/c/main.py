n = int(input())
count = 0
for i in range(1, n):
    for j in range(1, n // i + 1):
        c = n - i * j
        if c >= 1:
            count += 1
print(count)
