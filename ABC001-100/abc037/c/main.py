n, k = map(int, input().split())
a = list(map(int, input().split()))
wa = [a[0]]
for i in range(1, n):
    wa.append(wa[i - 1] + a[i])
ans = 0
for i in range(1, n - k + 1):
    ans += wa[i + k - 1] - wa[i - 1]
ans += wa[k - 1]
print(ans)
