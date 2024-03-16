h, w, K = map(int, input().split())
C = [input() for i in range(h)]

# 組み合わせの総数
ans = 0

# ０から(1<<n)-1まで全探索。
for i in range(1 << h):
    h_list = []
    for j in range(h):
        wari = 1 << j
        if (i // wari) % 2 == 1:
            h_list.append(j)
    for k in range(1 << w):
        w_list = []
        count = 0
        for l in range(w):
            div = 1 << l
            if (k // div) % 2 == 1:
                w_list.append(l)
        for m in range(h):
            if m in h_list:
                continue
            for n in range(w):
                if n in w_list:
                    continue
                if C[m][n] == "#":
                    count += 1
        if count == K:
            ans += 1
print(ans)
