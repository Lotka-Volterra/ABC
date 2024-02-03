h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(input())
HW = [[[0, 0] for j in range(w)] for i in range(h)]
for i in range(h - 1, -1, -1):
    for j in range(w - 1, -1, -1):
        if s[i][j] == "#":
            continue
        HW[i][j][0] += 1
        HW[i][j][1] += 1
        if j != w - 1:
            HW[i][j][1] += HW[i][j + 1][1]
        if i != h - 1:
            HW[i][j][0] += HW[i + 1][j][0]
ans = 0
for i in range(h):
    for j in range(w):
        minW = float("INF")
        tempAns = 0
        for k in range(HW[i][j][0]):
            for l in range(k + 1):
                minW = min(minW, HW[i + l][j][1])
            tempAns = max(tempAns, (k + 1) * minW)
        ans = max(ans, tempAns)
print(ans)
