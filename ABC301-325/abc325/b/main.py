n = int(input())
wx = []
for i in range(n):
    w, x = map(int, input().split())
    wx.append([w, x])
work = [0] * 24
for i in range(9):
    for j in range(n):
        work[(wx[j][1] + i) % 24] += wx[j][0]
print(max(work))
