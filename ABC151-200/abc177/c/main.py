n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        aij = ((a[i] % mod) * (a[j] % mod)) % mod
        ans = (ans + aij) % mod
        ans %= mod
print(ans)
