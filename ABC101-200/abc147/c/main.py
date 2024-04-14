# 要素数n
n = int(input())
testimony = [[] for i in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        testimony[i].append([x, y])

# 組み合わせの総数
ans = 0

# ０から(1<<n)-1まで全探索。
for i in range(1 << n):
    honest = []
    for j in range(n):
        wari = 1 << j
        if (i // wari) % 2 == 1:
            honest.append(j + 1)
    contradiction = False
    for j in honest:
        for k in testimony[j - 1]:
            if k[1] == 1 and k[0] not in honest:
                contradiction = True
                break
            if k[1] == 0 and k[0] in honest:
                contradiction = True
                break
        if contradiction:
            break
    if not contradiction:
        ans = max(len(honest), ans)
print(ans)
