n, k = map(int, input().split())
p = list(map(int, input().split()))
expect = [0]
for i in range(n):
    expect.append((p[i] * (p[i] + 1) // 2) / p[i] + expect[i])
ans = 0
for i in range(k, n + 1):
    ans = max(ans, expect[i] - expect[i - k])
print(ans)
