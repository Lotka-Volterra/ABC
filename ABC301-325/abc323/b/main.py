n = int(input())
s = [input() for i in range(n)]
ans = []
for i in range(n):
    win = 0
    for j in range(n):
        if s[i][j] == "o":
            win += 1
    ans.append([n - win, i + 1])
ans.sort()
finalans = []
for i in range(n):
    finalans.append(ans[i][1])
print(*finalans)
