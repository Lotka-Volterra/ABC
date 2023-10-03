r, c = map(int, input().split())
b = []
bomb = []
for i in range(r):
    bi = input()
    b.append(list(bi))
    for j in range(c):
        if bi[j] != "." and bi[j] != "#":
            bomb.append([i, j, int(bi[j])])
for i in range(len(bomb)):
    bombR = bomb[i][0]
    bombC = bomb[i][1]
    explosion = bomb[i][2]
    for j in range(explosion + 1):
        for k in range(
            max(0, bombC - (explosion - j)), min(c, bombC + (explosion - j) + 1), 1
        ):
            b[max(0, bombR - j)][k] = "."
            b[min(r - 1, bombR + j)][k] = "."
for i in range(r):
    print("".join(map(str, b[i])))
