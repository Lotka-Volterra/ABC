n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    ans += b[a[i] - 1]
    if a[i] + 1 == a[i + 1]:
        ans += c[a[i] - 1]
ans += b[a[n - 1] - 1]
print(ans)
