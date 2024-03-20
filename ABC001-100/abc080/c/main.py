# 要素数n
n = int(input())

f = [list(map(int, input().split())) for i in range(n)]
p = [list(map(int, input().split())) for i in range(n)]

ans = -float("inf")
# 1から(1<<n)-1まで全探索。
for i in range(1, 1 << 10):
    open_day = []
    for j in range(10):
        wari = 1 << j
        if (i // wari) % 2 == 1:
            open_day.append(j)
    count = []
    for j in range(n):
        same_day_count = 0
        for k in range(10):
            if f[j][k] == 1 and k in open_day:
                same_day_count += 1
        count.append(same_day_count)
    profit = 0
    for i in range(n):
        profit += p[i][count[i]]
    ans = max(ans, profit)
print(ans)
