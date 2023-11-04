n, m, q = map(int, input().split())
g = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
c = [0] + list(map(int, input().split()))
for i in range(q):
    s = list(map(int, input().split()))
    print(c[s[1]])
    if s[0] == 1:
        for j in g[s[1]]:
            c[j] = c[s[1]]
    else:
        c[s[1]] = s[2]
