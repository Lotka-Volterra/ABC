a, b = map(int, input().split())
c, d = map(int, input().split())
if a == c and b == d:
    print(0)
elif a + b == c + d:
    print(1)
elif a - b == c - d:
    print(1)
elif abs(a - c) + abs(b - d) <= 3:
    print(1)
elif (a + b) % 2 == (c + d) % 2:
    print(2)
elif abs(a - c) + abs(b - d) <= 6:
    print(2)
elif abs((a + b) - (c + d)) <= 3:
    print(2)
elif abs((a - b) - (c - d)) <= 3:
    print(2)
else:
    print(3)
