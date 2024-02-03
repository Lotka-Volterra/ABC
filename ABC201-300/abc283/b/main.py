n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
    query = list(map(int, input().split()))
    if len(query) == 2:
        print(a[query[1] - 1])
    else:
        a[query[1] - 1] = query[2]
