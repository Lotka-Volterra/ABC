n, k, x = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    used_coupon = min(k, a[i] // x)
    a[i] -= used_coupon * x
    k -= used_coupon
if k > 0:
    a.sort(reverse=True)
    for i in range(n):
        if k == 0:
            break
        a[i] = 0
        k -= 1
print(sum(a))
