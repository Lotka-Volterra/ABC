r, c = map(int, input().split())
if r % 2 != 0 and min(r, 16 - r) <= c <= max(r, 16 - r):
    print("black")
elif c % 2 != 0 and min(c, 16 - c) <= r <= max(c, 16 - c):
    print("black")
else:
    print("white")
