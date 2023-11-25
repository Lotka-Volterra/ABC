h, w = map(int, input().split())
a = []
mina = 101
for i in range(h):
    ai = list(map(int, input().split()))
    a.append(ai)
    mina = min(mina, min(ai))
ans = 0
for i in range(h):
    for j in range(w):
        ans += a[i][j] - mina
print(ans)
