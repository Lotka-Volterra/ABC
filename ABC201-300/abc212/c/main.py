n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_b = []
for i in range(n):
    a_b.append([a[i], 0])
for i in range(m):
    a_b.append([b[i], 1])
a_b.sort()
ans = float("inf")
for i in range(n + m - 1):
    if a_b[i][1] != a_b[i + 1][1]:
        ans = min(ans, abs(a_b[i][0] - a_b[i + 1][0]))
print(ans)
