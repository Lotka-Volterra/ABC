n, t = map(int, input().split())

ans = 1001
for i in range(n):
    ci, ti = map(int, input().split())
    if ti <= t:
        ans = min(ans, ci)
if ans > 1000:
    print("TLE")
else:
    print(ans)
