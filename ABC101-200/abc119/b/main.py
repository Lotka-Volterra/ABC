n = int(input())
ans = 0
for i in range(n):
    x, u = input().split()
    if u == "BTC":
        ans += float(x) * 380000
    else:
        ans += float(x)
print(ans)
