n = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(n - 2):
    plist = [p[i], p[i + 1], p[i + 2]]
    if min(plist) < p[i + 1] < max(plist):
        ans += 1
print(ans)
