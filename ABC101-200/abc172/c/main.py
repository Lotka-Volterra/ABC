# 解説AC
# 貪欲法で考えていた（読む時間が短い本からドンドン読んでいく）が、
# 机の一番上に読む時間が大きい本があるが、2番目以降に読む時間が短い本が連なっている時にACできない
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ruiseki_a, ruiseki_b = [0], [0]
for i in range(n):
    ruiseki_a.append(ruiseki_a[i] + a[i])
for i in range(m):
    ruiseki_b.append(ruiseki_b[i] + b[i])
ans = 0
j = m
for i in range(n + 1):
    if ruiseki_a[i] > k:
        break
    while ruiseki_b[j] > k - ruiseki_a[i]:
        j -= 1
    ans = max(ans, i + j)
print(ans)
