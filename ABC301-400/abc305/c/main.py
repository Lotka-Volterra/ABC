h, w = map(int, input().split())
S = [input() for i in range(h)]
# 上下左右
DX = [0, 0, -1, 1]
DY = [1, -1, 0, 0]
for i in range(h):
    for j in range(w):
        if S[i][j] == ".":
            cookie = 0
            for dx, dy in zip(DX, DY):
                x = dx + i
                y = dy + j
                if 0 <= x <= h - 1 and 0 <= y <= w - 1:
                    if S[x][y] == "#":
                        cookie += 1
            if cookie >= 2:
                print(i + 1, j + 1)
                quit()
