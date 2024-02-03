pizza = [0] * 360
pizza[0] = 1
position = 0
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    position = (a[i] + position) % 360
    pizza[position] = 1
pre = 0
maxangle = 0
for i in range(360):
    if pizza[i] == 1:
        maxangle = max(maxangle, i - pre)
        pre = i
for i in range(359, 0, -1):
    if pizza[i] == 1:
        maxangle = max(maxangle, 360 - i)
        break
print(maxangle)
