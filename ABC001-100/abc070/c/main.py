import math

n = int(input())
t = int(input())
for i in range(n - 1):
    t = math.lcm(t, int(input()))
print(t)
