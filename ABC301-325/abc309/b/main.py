n = int(input())
a = []
for i in range(n):
    a.append(input())
ans = []
ans.append(a[1][0] + a[0][:-1])
for i in range(1, n - 1):
    ans.append(a[i + 1][0] + a[i][1:-1] + a[i - 1][-1])
ans.append(a[n - 1][1:] + a[n - 2][-1])
for i in range(n):
    print(ans[i])
