n, m = map(int, input().split())
blackX = [0, 0, 0, 1, 1, 1, 2, 2, 2, 6, 6, 6, 7, 7, 7, 8, 8, 8]
blackY = [0, 1, 2, 0, 1, 2, 0, 1, 2, 6, 7, 8, 6, 7, 8, 6, 7, 8]
whiteX = [0, 1, 2, 3, 3, 3, 3, 5, 5, 5, 5, 6, 7, 8]
whiteY = [3, 3, 3, 3, 0, 1, 2, 5, 6, 7, 8, 5, 5, 5]

s = [input() for i in range(n)]
for i in range(n - 8):
    for j in range(m - 8):
        blackOK = True
        whiteOK = True
        for b in range(18):
            if s[i + blackX[b]][j + blackY[b]] != "#":
                blackOK = False
                break
        for w in range(14):
            if s[i + whiteX[w]][j + whiteY[w]] != ".":
                whiteOK = False
                break
        if blackOK and whiteOK:
            print(i + 1, j + 1)
