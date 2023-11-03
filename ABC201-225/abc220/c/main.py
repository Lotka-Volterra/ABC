n = int(input())
a = list(map(int, input().split()))
x = int(input())
suma = sum(a)
sho = x // suma
ans = sho * n
currentsum = sho * suma
for i in range(n):
    ans += 1
    currentsum += a[i]
    if currentsum > x:
        print(ans)
        quit()
