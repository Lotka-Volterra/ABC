from collections import defaultdict

h, w, n = map(int, input().split())
AB = []
A = set()
B = set()
a_order = defaultdict(int)
b_order = defaultdict(int)
for i in range(n):
    a, b = map(int, input().split())
    A.add(a)
    B.add(b)
    AB.append([a, b])
A = sorted(list(A))
B = sorted(list(B))
for i in range(len(A)):
    a_order[A[i]] = i + 1
for i in range(len(B)):
    b_order[B[i]] = i + 1
for i in range(n):
    print(a_order[AB[i][0]], b_order[AB[i][1]])
