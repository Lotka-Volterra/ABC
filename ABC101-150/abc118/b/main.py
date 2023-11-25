n, m = map(int, input().split())
foods = [0] * m
for i in range(n):
    a = list(map(int, input().split()))
    k = a[0]
    a = a[1:]
    for j in range(k):
        foods[a[j] - 1] += 1
ans = 0
for i in range(m):
    if foods[i] == n:
        ans += 1
print(ans)
