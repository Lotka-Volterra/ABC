from math import sqrt

n, k = map(int, input().split())
a = list(map(int, input().split()))
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
akari = []
nashi = []
for i in range(n):
    if i+1 in a:
        akari.append(i)
    else:
        nashi.append(i)
dist = []

for i in range(len(nashi)):
    mind=4*(10**20)
    for j in range(len(akari)):
        kyori = (x[nashi[i]]-x[akari[j]])**2+(y[nashi[i]]-y[akari[j]])**2
        if kyori < mind:
            mind = kyori
    dist.append(mind)
mindist = max(dist)
print(sqrt(mindist))
