n, q = map(int, input().split())
ll = []
for i in range(n):
    l = list(map(int, input().split()))
    ll.append(l)
for i in range(q):
    s, t = map(int, input().split())
    print(ll[s - 1][t])
