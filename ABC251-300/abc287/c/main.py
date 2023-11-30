import itertools

n, m = map(int, input().split())
path = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    path[u - 1].append(v - 1)
    path[v - 1].append(u - 1)
seq = list(range(n))
for i in list(itertools.permutations(seq)):
    isPath = False
    for j in range(n - 1):
        for k in range(n):
            if k == j + 1 and (path[i[j]][i[k]] == 1 and path[i[k]][i[j]] == 1):
                print(i, j, k)
                isPath = True
            elif k != j + 1 and (path[i[j]][i[k]] != 0 or path[i[k]][i[j]] != 0):
                isPath = False
                print(i, j, k)
    if isPath:
        print("Yes")
        quit()
print("No")
