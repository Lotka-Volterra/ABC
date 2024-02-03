k, x = map(int, input().split())
ans = []
for i in range(max(-1000000, x - (k - 1)), min(x + k, 1000000)):
    ans.append(i)
print(*ans)
