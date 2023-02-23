n, k = map(int, input().split())
a = list(map(int, input().split()))

# 組み合わせの総数
mex = []
# iから(1<<n)-1まで全探索。
for i in range(1, 1 << n):
    kumi = []
    for j in range(n):
        wari = 1 << j

        if (i // wari) % 2 == 1:
            kumi.append(a[j])
    if len(kumi)!=k:
        continue
    for l in range(min(kumi), 3 * 10**5 + 1):
        if l not in kumi:
            print(l, kumi)
            mex.append(l)
            break
print(max(mex))
