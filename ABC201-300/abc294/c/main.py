from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_dict = defaultdict(int)
b_dict = defaultdict(int)
for i in range(n):
    a_dict[a[i]] = i + 1
for i in range(m):
    b_dict[b[i]] = i + 1
c = a + b
c.sort()
ans_a = []
ans_b = []
for i in range(n + m):
    # Aにある場合
    if a_dict[c[i]] != 0:
        ans_a.append(i + 1)
    # Bにある場合
    else:
        ans_b.append(i + 1)
print(*ans_a)
print(*ans_b)
# 模範解答は、Cについて、値とインデックスの連想配列を作って、それに対してAとBをそれぞれfor文回している
