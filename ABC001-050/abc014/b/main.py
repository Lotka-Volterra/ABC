n, x = map(int, input().split())
a = list(map(int, input().split()))
binx = bin(x)[2:]
ans = 0
for i in range(len(binx)):
    if binx[-1 - i] == "1":
        ans += a[i]
print(ans)
