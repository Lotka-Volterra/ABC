import math

a, b, c, d = map(int, input().split())
c_min = (a - 1) // c
d_min = (a - 1) // d
lcm_min = (a - 1) // math.lcm(c, d)

c_max = b // c
d_max = b // d
lcm_max = b // math.lcm(c, d)
print(b - (a - 1) - (c_max - c_min) - (d_max - d_min) + (lcm_max - lcm_min))
