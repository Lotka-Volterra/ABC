import math

ans = 0
k = int(input())
for a in range(1, k + 1):
    for b in range(1, k + 1):
        for c in range(1, k + 1):
            ans += math.gcd(a, b, c)
print(ans)
