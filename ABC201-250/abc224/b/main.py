h, w = map(int, input().split())
a = []
for i in range(h):
    a.append(list(map(int, input().split())))
for i1 in range(h - 1):
    for i2 in range(i1 + 1, h):
        for j1 in range(w - 1):
            for j2 in range(j1 + 1, w):
                if a[i1][j1] + a[i2][j2] > a[i1][j2] + a[i2][j1]:
                    print("No")
                    quit()
print("Yes")
