n, m = map(int, input().split())
AB = []
for i in range(m):
    AB.append(list(map(int, input().split())))
k = int(input())
CD = []
for i in range(k):
    CD.append(list(map(int, input().split())))

# 組み合わせの総数
ans = 0

# ０から(1<<n)-1まで全探索。
for i in range(1 << k):
    bowl = [0] * (n + 1)
    # sum = 0
    choice = set()
    for j in range(k):
        wari = 1 << j
        if (i // wari) % 2 == 1:
            choice.add(CD[j][1])
        else:
            choice.add(CD[j][0])
    for l in choice:
        bowl[l] = 1
    count = 0
    for l in range(m):
        if bowl[AB[l][0]] == 1 and bowl[AB[l][1]] == 1:
            count += 1
    ans = max(count, ans)
print(ans)
