n = int(input())
A_B = []
for i in range(n):
    a, b = map(int, input().split())
    A_B.append([b, a])
A_B.sort()
time = 0
for i in range(n):
    time += A_B[i][1]
    if time > A_B[i][0]:
        print("No")
        exit()
print("Yes")
