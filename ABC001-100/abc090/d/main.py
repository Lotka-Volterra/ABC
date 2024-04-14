n, k = map(int, input().split())
ans = 0
for i in range(max(k, 1), n + 1):
    ans += n - i
    for j in range(k + 1, i + 1):
        if i % j >= k:
            ans += 1
print(ans)
