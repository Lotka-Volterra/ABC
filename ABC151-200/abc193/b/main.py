n = int(input())
minmoney = float("inf")
for i in range(n):
    a, p, x = map(int, input().split())
    if x - a > 0:
        minmoney = min(p, minmoney)
print(minmoney) if minmoney < float("inf") else print(-1)
