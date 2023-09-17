a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
a = []
a.append(a1)
a.append(a2)
a.append(a3)
bingo = [[0] * 3 for i in range(3)]
n = int(input())
for i in range(n):
    b = int(input())
    for j in range(3):
        for h in range(3):
            if a[j][h] == b:
                bingo[j][h] = 1
for i in range(3):
    if bingo[i][0] + bingo[i][1] + bingo[i][2] == 3:
        print("Yes")
        quit()
    elif bingo[0][i] + bingo[1][i] + bingo[2][i] == 3:
        print("Yes")
        quit()
if (
    bingo[0][0] + bingo[1][1] + bingo[2][2] == 3
    or bingo[0][2] + bingo[1][1] + bingo[2][0] == 3
):
    print("Yes")
    quit()
print("No")
