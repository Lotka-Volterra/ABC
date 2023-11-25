w, h, n = map(int, input().split())
hw = [[0] * w for i in range(h)]
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        for j in range(h):
            for k in range(x):
                hw[j][k] = 1
    elif a == 2:
        for j in range(h):
            for k in range(x, w):
                hw[j][k] = 1
    elif a == 3:
        for j in range(y):
            for k in range(w):
                hw[j][k] = 1
    else:
        for j in range(y, h):
            for k in range(w):
                hw[j][k] = 1
ans = 0
for i in range(h):
    for j in range(w):
        if hw[i][j] == 0:
            ans += 1
print(ans)
