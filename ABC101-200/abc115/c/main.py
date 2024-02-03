n, k = map(int, input().split())
h = [int(input()) for i in range(n)]
h.sort()
ans = 10**10
# ソートした中をk本ずつ選んでいき、hmax-hminが最小となる値を見つける
for i in range(n - k + 1):
    ans = min(h[i + k - 1] - h[i], ans)
print(ans)
