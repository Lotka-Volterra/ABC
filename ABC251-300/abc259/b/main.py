import math
a, b, d = map(int, input().split())
radd = math.radians(d)
x = a*math.cos(radd)-b*math.sin(radd)
y = a*math.sin(radd)+b*math.cos(radd)
print(x, y)
