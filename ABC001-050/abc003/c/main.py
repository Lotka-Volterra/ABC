n, k = map(int, input().split())
r = list(map(int, input().split()))
r.sort()
rate = 0
for i in range(-k, 0):
    rate = (rate + r[i]) / 2
print(rate)
