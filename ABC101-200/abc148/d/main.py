n = int(input())
a = list(map(int, input().split()))
num = 1
ans = 0
for i in range(n):
    if a[i] == num:
        num += 1
    else:
        ans += 1
if num == 1:
    print(-1)
else:
    print(ans)
