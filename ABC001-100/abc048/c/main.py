n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
if a[0] > x:
    diff = a[0] - x
    ans += diff
    a[0] -= diff
for i in range(1, n):
    diff = a[i] + a[i - 1] - x
    if diff > 0:
        ans += diff
        a[i] -= diff
print(ans)
