h, w = map(int, input().split())
G = []
for i in range(h):
    G.append(input())
count = 0
i, j = 0, 0
while count < h * w:
    count += 1
    if G[i][j] == "U":
        if i != 0:
            i -= 1
        else:
            print(i + 1, j + 1)
            quit()
    elif G[i][j] == "D":
        if i != h - 1:
            i += 1
        else:
            print(i + 1, j + 1)
            quit()
    elif G[i][j] == "L":
        if j != 0:
            j -= 1
        else:
            print(i + 1, j + 1)
            quit()
    else:
        if j != w - 1:
            j += 1
        else:
            print(i + 1, j + 1)
            quit()
print(-1)
