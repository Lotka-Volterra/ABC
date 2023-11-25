import math

n, x = map(int, input().split())
xlist = list(map(int, input().split()))
xlist.append(x)
xlist.sort()
distance = []
for i in range(len(xlist)-1):
    distance.append(xlist[i + 1] - xlist[i])
print(math.gcd(*distance))
