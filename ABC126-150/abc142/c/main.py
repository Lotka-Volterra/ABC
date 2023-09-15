n = int(input())
a = list(map(int, input().split()))
toko = []
for i in range(n):
    toko.append([a[i], i + 1])
toko.sort()
ans = []
for i in range(n):
    ans.append(toko[i][1])
print(*ans)
