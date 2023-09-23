n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    if a[i] % 6 == 0:
        ans += 3
    elif a[i] % 6 == 2 or a[i] % 6 == 4:
        ans += 1
    elif a[i] % 6 == 5:
        ans += 2
print(ans)
