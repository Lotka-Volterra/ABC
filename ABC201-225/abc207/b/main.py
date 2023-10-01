a, b, c, d = map(int, input().split())
if c*d-b<=0:
    print(-1)
else:
    print(int((a + (c * d - b - 1)) / (c * d - b)))
