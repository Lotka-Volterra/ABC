from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
sonomama = []
for i in range(n):
    if a[i] == i + 1:
        sonomama.append(i)
ans = 0
for i in range(n):
    if a[i] != i + 1 and a[a[i] - 1] == i + 1:
        ans += 1
ans //= 2
len_sonomama = len(sonomama)
ans += len_sonomama * (len_sonomama - 1) // 2
print(ans)
