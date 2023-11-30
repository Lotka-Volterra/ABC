n = int(input())
prevX = 0
prevY = 0
prevT = 0
for i in range(n):
    t, x, y = map(int, input().split())
    if abs(x - prevX) + abs(y - prevY) > t - prevT:
        print("No")
        quit()
    if t % 2 != (x + y) % 2:
        print("No")
        quit()
    prevX = x
    prevY = y
    prevT = t
print("Yes")
