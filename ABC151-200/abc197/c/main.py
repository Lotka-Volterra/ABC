# 数字が書かれたカードがn枚あるとして、そのうちいくつかを選んで、和を求め、それが1000になる組み合わせを求める。
# 要素数n
n = int(input())

# 要素数nのリストa
a = list(map(int, input().split()))

# 組み合わせの総数
ans = 1 << 30

# ０から(1<<n)-1まで全探索。
for i in range(1 << n - 1):
    partation = [0]
    for j in range(n - 1):
        wari = 1 << j
        if (i // wari) % 2 == 1:
            partation.append(j)
    partation.append(n - 1)
    or_list = []
    for j in range(1, len(partation)):
        part = a[partation[j - 1] : partation[j] + 1]
        or_ans = part[0]
        for k in range(1, len(part)):
            or_ans = or_ans | part[k]
        or_list.append(or_ans)
    xor_ans = or_list[0]
    for j in range(1, len(or_list)):
        xor_ans = xor_ans ^ or_list[j]
    ans = min(ans, xor_ans)
print(ans)
