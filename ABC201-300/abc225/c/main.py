n, m = map(int, input().split())
B = []
for i in range(n):
    B.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if j != 0 and B[i][j] != B[i][j - 1] + 1:
            print("No")
            quit()
        if i != 0 and B[i][j] != B[i - 1][j] + 7:
            print("No")
            quit()
        if j != m - 1 and B[i][j] % 7 == 0:
            print("No")
            quit()
print("Yes")
