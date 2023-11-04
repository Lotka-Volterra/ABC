n, m = map(int, input().split())
h = list(map(int, input().split()))
tenbodai = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    tenbodai[a - 1].append(h[b - 1])
    tenbodai[b - 1].append(h[a - 1])
ans = 0
for i in range(n):
    if len(tenbodai[i]) == 0:
        ans += 1
    elif h[i] > max(tenbodai[i]):
        ans += 1
print(ans)
# 模範解答
# 入力を受け取るときに比較する
n, m = map(int, input().split())
h = list(map(int, input().split()))
tenbodai = [True for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if h[a - 1] <= h[b - 1]:
        tenbodai[a] = False
    if h[b - 1] <= h[a - 1]:
        tenbodai[b] = False
ans = 0
for i in range(n):
    if tenbodai[i]:
        ans += 1
print(ans)
