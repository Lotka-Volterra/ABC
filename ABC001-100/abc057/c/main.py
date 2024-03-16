n = int(input())
ans = len(str(n))
for a in range(1, n + 1):
    if a**2 > n:
        break
    if n % a == 0:
        b = n // a
        ans = min(ans, max(len(str(a)), len(str(b))))
print(ans)
