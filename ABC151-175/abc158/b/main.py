n, a, b = map(int, input().split())
sho = n // (a + b)
amari = n % (a + b)
print(sho * a + min(amari, a))
