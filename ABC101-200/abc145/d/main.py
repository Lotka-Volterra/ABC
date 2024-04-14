from collections import defaultdict

X, Y = map(int, input().split())
board = [[0] * (X + 1) for i in range(Y + 1)]
board[0][0] = 1
knight = [[0, 0]]
for i in range(Y):
    temp_knight = []
    for j, k in knight:
        for l, m in [[2, 1], [1, 2]]:
            x = j + l
            y = k + m
            if x > X or y > Y:
                continue
            board[y][x] = (board[y][x] + board[k][j]) % (10**9 + 7)
            temp_knight.append([y, x])
    knight = temp_knight
    print(board)
print(board[Y][X])
