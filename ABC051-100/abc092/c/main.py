n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [0]
p = [0]
for i in range(1, n + 2):
    p.append(abs(a[i - 1] - a[i]))
sum_p = sum(p)
# sum_pで総和を出しておいて、各iについて個別に再計算する
for i in range(1, n + 1):
    print(sum_p - (p[i] + p[i + 1]) + abs(a[i + 1] - a[i - 1]))
