n = int(input())
h = list(map(int, input().split()))
ans = []
count = 0
for i in range(1, n):
    if h[i] <= h[i - 1]:
        count += 1
    else:
        ans.append(count)
        count = 0
ans.append(count)
print(max(ans))
