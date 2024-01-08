import itertools

n, m = map(int, input().split())
path = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    path[u - 1].append(v - 1)
    path[v - 1].append(u - 1)


def isPath(position, count, former):
    if count == n and len(path[position]) == 1:
        return True
    if count != 1 and len(path[position]) != 2:
        return False
    else:
        for j in path[position]:
            if j != former:
                return isPath(j, count + 1, position)


for i in range(n):
    if len(path[i]) == 1:
        if isPath(i, 1, -1):
            print("Yes")
            quit()
print("No")
