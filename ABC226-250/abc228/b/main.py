import sys

sys.setrecursionlimit(10**6)
n, x = map(int, input().split())
friends = [0] * (n + 1)
a = list(map(int, input().split()))
dict = {}
for i in range(n):
    dict[i + 1] = a[i]


def bakuro(person):
    if friends[dict[person]] == 0:
        friends[dict[person]] = 1
        bakuro(dict[person])
    else:
        return


friends[x] = 1
bakuro(x)
print(sum(friends))
