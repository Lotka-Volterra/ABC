n, k = map(int, input().split())
ans = (n // k) ** 3
if k % 2 == 0:
    count = 0
    for i in range(1, n + 1):
        if i % k == k // 2:
            count += 1
    ans += count**3
print(ans)
