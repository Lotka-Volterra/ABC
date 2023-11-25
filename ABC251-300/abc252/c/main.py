n = int(input())
time = [[] for i in range(10)]
for i in range(n):
    s = input()
    for j in range(10):
        time[int(s[j]) - 1].append(j % 10)
ans = 1000
for i in range(10):
    time[i].sort()
    chohuku = 0
    for j in range(1, n):
        if time[i][j] == time[i][j - 1]:
            chohuku += 10
        else:
            if chohuku != 0:
                time[i].append(chohuku + time[i][j - 1])
                chohuku = 0
    if chohuku != 0:
        time[i].append(chohuku + time[i][n - 1])
        chohuku = 0
    ans = min(ans, max(time[i]))
print(ans)
