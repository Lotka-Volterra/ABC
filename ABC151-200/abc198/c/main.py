import math

r, x, y = map(int, input().split())
distance = math.sqrt(x**2 + y**2)
if distance < r:
    print(2)
else:
    print(math.ceil(distance / r))
