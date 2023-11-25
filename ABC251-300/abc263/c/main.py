import copy


def monotonically(i, n, m):
    if len(i) == n:
        print(*i)
        return
    else:
        for j in range(i[-1] + 1, m + 1):
            tempI = copy.deepcopy(i)
            tempI.append(j)
            monotonically(tempI, n, m)


n, m = map(int, input().split())
for i in range(1, m + 1):
    monotonically([i], n, m)
