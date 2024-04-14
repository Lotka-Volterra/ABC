# 要素数n
n, m = map(int, input().split())
s = []
for i in range(m):
    k = list(map(int, input().split()))
    s.append(k[1:])
p = list(map(int, input().split()))
# 組み合わせの総数
ans = 0

# ０から(1<<n)-1まで全探索。
for i in range(1 << n):
    lit = []
    for j in range(n):
        wari = 1 << j
        if (i // wari) % 2 == 1:
            lit.append(j + 1)
    all_lit = True
    for j in range(m):
        count = 0
        for k in s[j]:
            if k in lit:
                count += 1
        if count % 2 != p[j]:
            all_lit = False
            break
    if all_lit:
        ans += 1
print(ans)
