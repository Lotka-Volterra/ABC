n, m = map(int, input().split())
nlist = [[] * n]
for i in range(m):
    k = list(map(int, input().split()))
    for i in range(k[i]):
        nlist[k[i - 1] - 1].append(i)
for i in range(n - 1):
    for j in range(i, n):
        if len(nlist[i] + nlist[j]) == len(list(set(nlist[i] + nlist[j]))):
            print("No")
            quit()
print("Yes")
