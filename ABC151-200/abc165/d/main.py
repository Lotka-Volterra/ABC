import math

a, b, n = map(int, input().split())
ansX = min(b - 1, n)
print(math.floor(a * ansX / b) - a * math.floor(ansX / b))
