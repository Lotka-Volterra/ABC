n = int(input())
transport = [int(input()) for i in range(5)]

time = [[0, 0]]
for i in range(1, 6):
    min_time = i
    sho = (n + transport[i - 1] - 1) // transport[i - 1]
    max_time = max(time[i - 1][0] + sho, time[i - 1][1] + 1)
    time.append([min_time, max_time])
print(time[5][1])
