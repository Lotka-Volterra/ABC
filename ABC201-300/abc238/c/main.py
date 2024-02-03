n = int(input())
ans = 0
mod = 998244353
for i in range(18):
    if n >= 10 ** (i + 1):
        total = 9 * (10**i) * (1 + (9 * (10**i))) // 2
        ans += total % mod
        ans %= mod
    elif n >= 10**i:
        kousuu = n - (10**i - 1)
        total = kousuu * (1 + (n - (10**i - 1))) // 2
        ans += total % mod
        ans %= mod
        break
print(ans)
