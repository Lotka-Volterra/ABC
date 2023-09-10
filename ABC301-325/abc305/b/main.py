dist = [0, 3, 1, 4, 1, 5, 9]
sumDist = [0] * len(dist)
for i in range(1, len(dist)):
    sumDist[i] = sumDist[i - 1] + dist[i]
ABC = ["A", "B", "C", "D", "E", "F", "G"]
p, q = input().split()
pind = ABC.index(p)
qind = ABC.index(q)
print(abs(sumDist[pind] - sumDist[qind]))
