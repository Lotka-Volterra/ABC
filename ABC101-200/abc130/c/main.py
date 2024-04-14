w, h, x, y = map(int, input().split())
exist = 1 if h % 2 == 0 and w % 2 == 0 and x == w // 2 and y == h // 2 else 0
print(h * w / 2, exist)
