n = int(input())
stringlist = [[] for i in range(2 * (10**5))]

for i in range(n):
    a = list(map(int, input().split()))
    slicedAl = a[1:]
    ai = a[0]
    s = ",".join(map(str, slicedAl))
    stringlist[ai - 1].append(s)
ans = 0
for i in range(len(stringlist)):
    ans += len(list(set(stringlist[i])))
print(ans)
