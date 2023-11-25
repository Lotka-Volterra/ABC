a, b, c, x = map(int, input().split())
if x <= a:
    print(1)
else:
    if x <= b:
        print(c/(b-a))
    else:
        print(0)
