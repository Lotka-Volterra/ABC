n, k = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

# 組み合わせの総数
ans = 0
# ０から(1<<n)-1まで全探索。
for i in range(1 << n):
    chosen = []
    alph = [0] * 26
    for j in range(n):
        wari = 1 << j
        if (i // wari) % 2 == 1:
            chosen.append(s[j])
    for j in chosen:
        for l in list(set(j)):
            alph[ord(l) - ord("a")] += 1
    count = 0
    for j in alph:
        if j == k:
            count += 1
    ans = max(count, ans)
print(ans)
