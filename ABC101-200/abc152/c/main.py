n = int(input())
p = list(map(int, input().split()))
minP = [p[0]]
for i in range(1, n):
    minP.append(min(minP[i - 1], p[i]))
ans = 0
for i in range(n):
    if minP[i] == p[i]:
        ans += 1
print(ans)
