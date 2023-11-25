a, b = map(int, input().split())
ans = []
for i in range(1, 1010):
    if int(i * 0.08) == a and int(i * 0.1) == b:
        ans.append(i)
print(-1) if len(ans) == 0 else print(ans[0])
