n, a, b = map(int, input().split())
distance = 0
for i in range(n):
    s, d = input().split()
    d = int(d)
    if d < a:
        d = a
    elif d > b:
        d = b
    if s == "West":
        d = -d
    distance += d
if distance < 0:
    print("West", abs(distance))
elif distance > 0:
    print("East", distance)
else:
    print(0)
