k, n = map(int, input().split())
house = []
a = list(map(int, input().split()))
for i in range(n):
    house.append(a[i])
    house.append(-(k - a[i]))
house.sort()
ans = k
for i in range(n):
    ans = min(ans, house[n + i - 1] - house[i])
print(ans)
