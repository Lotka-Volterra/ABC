n = int(input())
color = [0] * (10**6 + 2)
for i in range(n):
    a, b = map(int, input().split())
    color[a] += 1
    color[b + 1] -= 1
ans = color[0]
for i in range(1, 10**6 + 1):
    color[i] = color[i - 1] + color[i]
    ans = max(ans, color[i])
print(ans)
