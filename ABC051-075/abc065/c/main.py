n, m = map(int, input().split())
ans = 1
if abs(n - m) > 1:
    ans = 0
elif n == m:
    for i in range(1, n + 1):
        ans *= i
        ans %= 10**9 + 7
    ans *= ans
    ans %= 10**9 + 7
    ans *= 2
    ans %= 10**9 + 7
else:
    for i in range(1, n + 1):
        ans *= i
        ans %= 10**9 + 7
    for i in range(1, m + 1):
        ans *= i
        ans %= 10**9 + 7
print(ans)
