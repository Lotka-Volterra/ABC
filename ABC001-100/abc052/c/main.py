from collections import defaultdict


def prime_factorize(n):
    temp = n
    for i in range(2, n + 1):
        if i**2 > n:
            break
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            num[i] += cnt
    if temp != 1:
        num[temp] += 1


num = defaultdict(int)
mod = 10**9 + 7
n = int(input())
ans = 1

for i in range(2, n + 1):
    prime_factorize(i)
for i in num.values():
    ans *= i + 1
    ans %= mod
print(ans)
