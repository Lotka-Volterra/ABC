n = int(input())
h = list(map(int, input().split()))
ans = 1
maxh = h[0]
for i in range(1, n):
    if maxh <= h[i]:
        ans += 1
        maxh = h[i]
print(ans)
