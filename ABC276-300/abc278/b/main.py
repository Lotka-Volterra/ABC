h, m = map(int, input().split())
a = h // 10
b = h % 10
c = m // 10
d = m % 10
if 6 <= h <= 9:
    print(10, 0)
elif 16 <= h <= 19:
    print(20, 0)
elif 20 <= h <= 23 and 4 <= c <= 5:
    if h == 23:
        print(0, 0)
    else:
        print(h + 1, 0)
else:
    print(h, m)
