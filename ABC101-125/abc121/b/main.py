n, m, c = map(int, input().split())
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    a = list(map(int, input().split()))
    abc = c
    for j in range(m):
        abc += a[j] * b[j]
    if abc > 0:
        ans += 1
print(ans)
