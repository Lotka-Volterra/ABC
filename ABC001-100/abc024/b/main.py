n, t = map(int, input().split())
closeTime = 0
ans = 0
for i in range(n):
    a = int(input())
    if a <= closeTime:
        ans += (a + t) - closeTime
    else:
        ans += t
    closeTime = a + t
print(ans)
