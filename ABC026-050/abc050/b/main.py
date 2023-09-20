n = int(input())
t = list(map(int, input().split()))
m = int(input())
pm = []
for i in range(m):
    pi, mi = map(int, input().split())
    pm.append([pi, mi])
totalt = sum(t)
for i in range(m):
    print(totalt - t[pm[i][0] - 1] + pm[i][1])
