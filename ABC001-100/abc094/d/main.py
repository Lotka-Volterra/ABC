n = int(input())
a = list(map(int, input().split()))
ai = max(a)
aj_ind = -1
k = ai // 2
min_abs = k
for i in range(n):
    if a[i] == ai:
        continue
    if abs(a[i] - k) < min_abs:
        aj_ind = i
        min_abs = abs(a[i] - k)
print(ai, a[aj_ind])
