a, b, c, d, e, f = map(int, input().split())
div = 998244353
a %= div
b %= div
c %= div
d %= div
e %= div
f %= div
ABC = (a * b) % div * c % div
DEF = (d * e) % div * f % div
print((ABC - DEF) % div)
