n = int(input())
sa = []
al = []
for i in range(n):
    s, a = input().split()
    a = int(a)
    sa.append([a, s])
    al.append(a)
minA = al.index(min(al))
slicedSa = sa[minA:] + sa[:minA]
for i in range(n):
    print(slicedSa[i][1])
