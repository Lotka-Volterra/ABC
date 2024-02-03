n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(n - 1):
    if a[i + 1] - a[i] > 1:
        for j in range(a[i], a[i + 1]):
            ans.append(j)
    elif a[i] - a[i + 1] > 1:
        for j in range(a[i], a[i + 1], -1):
            ans.append(j)
    else:
        ans.append(a[i])
ans.append(a[-1])
print(*ans)
