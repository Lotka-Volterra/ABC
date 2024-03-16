# 数字が書かれたカードがn枚あるとして、そのうちいくつかを選んで、和を求め、それが1000になる組み合わせを求める。
# 要素数n
s = input()
n = len(s)

# 要素数nのリストa
a = list(map(int, list(s)))
# 組み合わせの総数
count = 0

# ０から(1<<n)-1まで全探索。
for i in range(1 << (n - 1)):
    sum = 0
    kakeru = []
    kakeru.append(n - 1)
    for j in range(n):
        wari = 1 << j
        if (i // wari) % 2 == 1:
            kakeru.append(j)
    sum_list = []
    kakeru_kazu = ""
    for j in range(n):
        kakeru_kazu += str(a[j])
        if j in kakeru:
            sum_list.append(int(kakeru_kazu))
            kakeru_kazu = ""
    temp_ans = 0
    for i in sum_list:
        temp_ans += i
    count += temp_ans
print(count)
