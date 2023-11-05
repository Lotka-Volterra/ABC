n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    diff = max(a[i - 1] - a[i], 0)
    if diff > 0:
        ans += diff
        a[i] += diff
print(ans)
