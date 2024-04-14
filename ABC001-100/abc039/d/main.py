h, w = map(int, input().split())
s = [input() for i in range(h)]
DX = [-1, -1, -1, 0, 0, 1, 1, 1]
DY = [-1, 0, 1, -1, 1, -1, 0, 1]
ans = [["#"] * w for i in range(h)]
# 周囲8マスに白がなければそのマスは黒
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            ans[i][j] = "."
            continue
        for dx, dy in zip(DX, DY):
            x = dx + i
            y = dy + j
            if 0 <= x <= h - 1 and 0 <= y <= w - 1 and s[x][y] == ".":
                ans[i][j] = "."
                break
for i in range(h):
    for j in range(w):
        # 期待結果。もともと白でも、周りに黒があると黒になる。もともと黒なら変わらない
        expected = ans[i][j]
        for dx, dy in zip(DX, DY):
            x = dx + i
            y = dy + j
            if 0 <= x <= h - 1 and 0 <= y <= w - 1 and ans[x][y] == "#":
                expected = "#"
                break
        if s[i][j] != expected:
            print("impossible")
            exit()
print("possible")
for i in range(h):
    print(*ans[i], sep="")
