point = 0
for i in range(3):
    j, k = map(int, input().split())
    point += int(j*k*0.1)
print(point)
