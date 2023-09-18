n = int(input())
pow = 1
for i in range(1, n + 1):
    pow = (pow * i) % (10**9 + 7)
print(pow)
