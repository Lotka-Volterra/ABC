import math

n = int(input())
a = list(map(int, input().split()))
print(math.gcd(*a))
