n = int(input())
mod = 10**9 + 7
a = 1
b = 1
c = 1
for i in range(n):
    a *= 10
    a %= mod
    b *= 8
    b %= mod
    c *= 9
    c %= mod
c = c * 2 % mod
# print(10**n + 8**n - (9**n) * 2)
print((a + b - c) % mod)
