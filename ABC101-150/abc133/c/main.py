l, r = map(int, input().split())
mod = 2019
if r - l >= 2018:
    print(0)
else:
    ans = 2018 * 2018
    for i in range(l, r):
        for j in range(l + 1, r + 1):
            ans = min(ans, ((i % mod) * (j % mod) % mod))
    print(ans)
