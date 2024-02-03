a, b = map(int, input().split())
if a > b:
    print(str(b) * a)
elif b > a:
    print(str(a) * b)
else:
    minAB = min(a, b)
    print(str(a) * minAB)
