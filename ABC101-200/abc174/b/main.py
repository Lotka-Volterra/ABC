n, d = map(int, input().split())
ans = 0
d2 = d**2
for i in range(n):
    x, y = map(int, input().split())
    if x**2 + y**2 <= d2:
        ans += 1
print(ans)
