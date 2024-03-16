n = int(input())
a = list(map(int, input().split()))
ans = n
start, end = 0, 0
for i in range(n - 1):
    if a[i + 1] > a[i]:
        end += 1
    else:
        ans += (end - start + 2) * (end - start + 1) // 2 - (end - start + 1)
        start = i + 1
        end = i + 1
    if i == n - 2:
        ans += (end - start + 2) * (end - start + 1) // 2 - (end - start + 1)
print(ans)
