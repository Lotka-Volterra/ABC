h, w = map(int, input().split())
mine = [[0] * w for i in range(h)]
for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == "#":
            mine[i][j] = "#"
            for k in range(max(0, j - 1), min(j + 2, w), 1):
                if i - 1 >= 0 and mine[i - 1][k] != "#":
                    mine[i - 1][k] += 1
                if mine[i][k] != "#":
                    mine[i][k] += 1
                if i + 1 <= h - 1:
                    mine[i + 1][k] += 1
for i in range(h):
    ans = ""
    for j in range(w):
        ans += str(mine[i][j])
    print(ans)
