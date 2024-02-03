n = int(input())
a = list(map(int, input().split()))
id = [0] * n
for i in range(n):
    if id[i] == 0:
        id[a[i] - 1] += 1
ans = []
for i in range(n):
    if id[i] == 0:
        ans.append(i + 1)
print(len(ans))
print(*ans)
