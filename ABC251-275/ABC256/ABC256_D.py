n = int(input())
l = []
r = []
lr = []
kukan = []
for i in range(n):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)
    lr.append([li, ri])
for i in range(n):
    li = lr[i][0]
    ri = lr[i][1]
    for j in range(n):
        if l[j] < li <= r[j]:
            li == l[j]
        if l[j] <= ri < r[j]:
            ri = r[j]
    kukan.append([li, ri])
kukan = list(set(kukan))
for i in range(len(kukan)):
    print(kukan[i])
