n = int(input())
k = int(input())
x = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += min(abs(x[i]), abs(k - x[i])) * 2
print(ans)
