c = []
for i in range(4):
    ci = list(input().split())
    c.append(ci)
for i in range(4):
    ans = []
    for j in range(4):
        ans.append(c[3 - i][3 - j])
    print(*ans)
