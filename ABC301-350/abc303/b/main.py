n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        isFunaka = True
        for k in range(m):
            for l in range(n - 1):
                if a[k][l] in [i + 1, j + 1] and a[k][l + 1] in [i + 1, j + 1]:
                    isFunaka = False
        if isFunaka:
            ans += 1
print(ans)
