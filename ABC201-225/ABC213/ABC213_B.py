import copy
n = int(input())
a = list(map(int, input().split()))
b = copy.deepcopy(a)
a.sort(reverse=True)
idx = b.index(a[1])
print(idx+1)
