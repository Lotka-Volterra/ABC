n = int(input())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
ans = float("inf")
for i in range(n - 1):
    for j in range(i + 1, n):
        aibj = max(a[i], b[j])
        ajbi = max(a[j], b[i])
        aibi = a[i] + b[i]
        ajbj = a[j] + b[j]
        ans = min([aibj, ajbi, aibi, ajbj, ans])
print(ans)
