n, m = map(int, input().split())
ab = []
island = [[0, 0] for i in range(n + 1)]
# ある島iについて、1->iが可能なら、island[i][0]=1
# ある島iについて、i->nが可能なら、island[i][1]=1
for i in range(m):
    a, b = map(int, input().split())
    ab.append([a, b])
    if a == 1:
        island[b][0] = 1
    if b == n:
        island[a][1] = 1
for i in range(n):
    if island[i][0] == 1 and island[i][1] == 1:
        print("POSSIBLE")
        quit()
print("IMPOSSIBLE")
