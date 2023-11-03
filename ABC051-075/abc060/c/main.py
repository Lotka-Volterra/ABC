n, t = map(int, input().split())
tl = list(map(int, input().split()))
time = 0
start = 0
last = t
for i in range(1, n):
    if tl[i] > last:
        time += last - start
        start = tl[i]
    last = tl[i] + t
print(time + last - start)
