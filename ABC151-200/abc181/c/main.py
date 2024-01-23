n = int(input())
x_y = []
for i in range(n):
    x, y = map(int, input().split())
    x_y.append([x, y])
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if (x_y[i][1] - x_y[j][1]) * (x_y[k][0] - x_y[i][0]) == (
                x_y[k][1] - x_y[i][1]
            ) * (x_y[i][0] - x_y[j][0]):
                print("Yes")
                quit()
print("No")
