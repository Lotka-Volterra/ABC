n = int(input())
L = []
R = []
for i in range(n):
    t, l, r = map(float, input().split())
    if t == 2:
        r -= 0.5
    elif t == 3:
        l += 0.5
    elif t == 4:
        r -= 0.5
        l += 0.5
    L.append(l)
    R.append(r)
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if not (R[i] < L[j] or R[j] < L[i]):
            ans += 1
print(ans)
