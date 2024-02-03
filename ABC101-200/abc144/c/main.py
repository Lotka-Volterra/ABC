n = int(input())
ans = n - 1
for i in range(2, n):
    if i**2 > n:
        break
    if n % i == 0:
        sho = n // i
        ans = min(ans, (sho - 1 + i - 1))
print(ans)
