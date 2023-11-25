m = int(input())
d = list(map(int, input().split()))
halfDay = (sum(d) + 1) // 2
count = 0
for i in range(m):
    for j in range(d[i]):
        count += 1
        if count == halfDay:
            print(i + 1, j + 1)
            quit()
