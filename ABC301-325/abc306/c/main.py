n = int(input())
a = list(map(int, input().split()))
count = [0] * n
ans = []
for i in range(3 * n):
    if count[a[i] - 1] == 0:
        count[a[i] - 1] += 1
    elif count[a[i] - 1] == 1:
        count[a[i] - 1] += 1
        ans.append(a[i])
print(*ans)
