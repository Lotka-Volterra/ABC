n, m = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_flight, b_flight = 0, 0
ans, time = 0, 0
while True:
    if a_flight == n:
        break
    if time > a[-1]:
        break
    for i in range(a_flight, n):
        if a[i] >= time:
            time = a[i]
            a_flight = i + 1
            break
    time += x
    if b_flight == m:
        break
    if time > b[-1]:
        break
    for i in range(b_flight, m):
        if b[i] >= time:
            time = b[i]
            b_flight = i + 1
            ans += 1
            break
    time += y
print(ans)
