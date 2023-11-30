n = int(input())
a = list(map(int, input().split()))
sumA = sum(a)
kirisute = int(sumA / n)
kiriage = int((sumA + n - 1) / n)
suteCost = 0
ageCost = 0
for i in range(n):
    suteCost += (a[i] - kirisute) ** 2
    ageCost += (a[i] - kiriage) ** 2
print(min(suteCost, ageCost))
