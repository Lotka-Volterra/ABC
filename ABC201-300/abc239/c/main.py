x1, y1, x2, y2 = map(int, input().split())
chuten_x = (x1 + x2) // 2
chuten_y = (y1 + y2) // 2
for i in range(-3, 4, 1):
    for j in range(-3, 4, 1):
        if (x1 - chuten_x + i) ** 2 + (y1 - chuten_y + j) ** 2 == 5 and (
            x2 - chuten_x + i
        ) ** 2 + (y2 - chuten_y + j) ** 2 == 5:
            print("Yes")
            quit()
print("No")
