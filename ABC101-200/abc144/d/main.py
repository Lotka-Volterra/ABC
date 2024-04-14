import math

a, b, x = map(int, input().split())
ans1 = math.degrees(math.atan(2 * x / (a**3)))
ans2 = math.degrees(math.atan(a * (b**2) / (2 * x)))
ans3 = math.degrees(math.atan(2 * (a**2) * b - 2 * x) / (a**3))
print(2 * (a**2) * b - 2 * x)
print(ans1, ans2, ans3)
print(max(ans1, ans2, ans3))
