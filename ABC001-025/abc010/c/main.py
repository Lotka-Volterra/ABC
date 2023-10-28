import math

txa, tya, txb, tyb, t, v = map(int, input().split())
n = int(input())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    distA = pow(txa - x, 2) + pow(tya - y, 2)
    distB = pow(txb - x, 2) + pow(tyb - y, 2)
    if math.sqrt(distA) + math.sqrt(distB) <= v * t:
        print("YES")
        quit()
print("NO")
