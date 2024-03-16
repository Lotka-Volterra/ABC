n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    temp_min = a[i]
    temp_count = 1
    ans = max(ans, temp_min * temp_count)
    for j in range(i + 1, n):
        temp_min = min(a[j], temp_min)
        temp_count += 1
        ans = max(ans, temp_min * temp_count)
print(ans)
