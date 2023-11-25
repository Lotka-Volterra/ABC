h, w = map(int, input().split())
s = [input() for i in range(h)]
# 縦、横、斜めで合計8通りを見る
tate1 = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]
tate2 = [[0, 0], [-1, 0], [-2, 0], [-3, 0], [-4, 0]]
yoko1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
yoko2 = [[0, 0], [0, -1], [0, -2], [0, -3], [0, -4]]
naname1 = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
naname2 = [[0, 0], [-1, -1], [-2, -2], [-3, -3], [-4, -4]]
naname3 = [[0, 0], [-1, 1], [-2, 2], [-3, 3], [-4, 4]]
naname4 = [[0, 0], [1, -1], [2, -2], [3, -3], [4, -4]]
direction = [tate1, tate2, yoko1, yoko2, naname1, naname2, naname3, naname4]
snuke = ["s", "n", "u", "k", "e"]
for i in range(h):
    for j in range(w):
        for k in range(8):
            isSnuke = True
            for l in range(5):
                x = i + direction[k][l][0]
                y = j + direction[k][l][1]
                # 見る対象が領域を越えないことを確認
                if x < 0 or x >= h or y < 0 or y >= w:
                    isSnuke = False
                    break
                # snukeの順に並んでいるかどうかを確認
                if s[x][y] != snuke[l]:
                    isSnuke = False
                    break
            if isSnuke:
                for l in range(5):
                    print(i + direction[k][l][0] + 1, j + direction[k][l][1] + 1)
                quit()
