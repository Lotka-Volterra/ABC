a, b, k = map(int, input().split())
ans = []
for i in range(a, min(a + k, b + 1)):
    ans.append(i)
for i in range(b, max(a - 1, b - k), -1):
    ans.append(i)
ans = list(set(ans))
ans.sort()
for i in ans:
    print(i)
