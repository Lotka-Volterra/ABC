h, w = map(int, input().split())
HW = []
for i in range(h):
    HW.append(input())
# 上下左右
DX = [0, 0, -1, 1]
DY = [1, -1, 0, 0]
for i in range(h):
    for j in range(w):
        if HW[i][j] == "#":
            is_lonely = True
            for dx, dy in zip(DX, DY):
                x = dx + i
                y = dy + j
                if 0 <= x <= h - 1 and 0 <= y <= w - 1:
                    if HW[x][y] == "#":
                        is_lonely = False
            if is_lonely:
                print("No")
                quit()
print("Yes")
