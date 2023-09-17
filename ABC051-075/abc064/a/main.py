r, g, b = map(int, input().split())
gb = g*10+b
if gb % 4 == 0:
    print("YES")
else:
    print("NO")
