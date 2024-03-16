n = int(input())
a = list(map(int, input().split()))
ans = -50 * n
for i in range(n):
    aoki_max_point = -50 * n
    aoki_max_point_index = 0
    for j in range(i):
        t = a[j : i + 1]
        aoki = 0
        for k in range(len(t)):
            if k % 2 == 1:
                aoki += t[k]
        if aoki > aoki_max_point:
            aoki_max_point = aoki
            aoki_max_point_index = j
    for j in range(i + 1, n):
        t = a[i : j + 1]
        aoki = 0
        for k in range(len(t)):
            if k % 2 == 1:
                aoki += t[k]
        if aoki > aoki_max_point:
            aoki_max_point = aoki
            aoki_max_point_index = j
    start, end = min(i, aoki_max_point_index), max(i, aoki_max_point_index)
    ans_t = a[start : end + 1]
    takahashi = 0
    for j in range(len(ans_t)):
        if j % 2 == 0:
            takahashi += ans_t[j]
    ans = max(ans, takahashi)
print(ans)
