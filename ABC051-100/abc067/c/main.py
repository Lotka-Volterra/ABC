n = int(input())
a = list(map(int, input().split()))
arai = sum(a)
snuke = 0
ans = float("inf")
for i in range(n - 1):
    arai -= a[i]
    snuke += a[i]
    ans = min(ans, abs(arai - snuke))
print(ans)
