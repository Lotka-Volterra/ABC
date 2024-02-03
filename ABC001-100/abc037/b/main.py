n, q = map(int, input().split())
seq = [0] * n
for i in range(q):
    l, r, t = map(int, input().split())
    for i in range(l - 1, r):
        seq[i] = t
for i in range(n):
    print(seq[i])
