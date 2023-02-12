# 数字が書かれたカードがn枚あるとして、そのうちいくつかを選んで、和を求め、それが1000になる組み合わせを求める。
# 要素数n
n = int(input())

# 要素数nのリストa
a = list(map(int, input().split()))

# 組み合わせの総数
count = 0

# iから(1<<n)-1まで全探索。
for i in range(1 << n):
    sum = 0
    for j in range(n):
        wari = 1 << j
        if (i//wari) % 2 == 1:
            sum += a[j]
    if sum == 1000:
        count += 1
