n, m = map(int, input().split())
L = []
R = []
for i in range(m):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
print(max(min(R) - max(L) + 1, 0))
