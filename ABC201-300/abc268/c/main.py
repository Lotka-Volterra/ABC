n = int(input())
p = list(map(int, input().split()))
newP = [p[-1]] + p + [p[0]]
ans = 0
for i in range(n):
    count = 0
    a = list(range(i, n)) + list(range(i))
    for j in range(n):
        if a[j] == newP[j] or a[j] == newP[j + 1] or a[j] == newP[j + 2]:
            count += 1
    ans = max(ans, count)
print(ans)
