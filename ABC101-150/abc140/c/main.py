n = int(input())
b = list(map(int, input().split()))
b = [b[0]] + b + [b[-1]]
ans = 0
for i in range(n):
    ans += min(b[i], b[i + 1])
print(ans)
