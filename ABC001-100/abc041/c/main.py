n = int(input())
a = list(map(int, input().split()))
height = []
for i in range(n):
    height.append([a[i], i + 1])
height.sort(reverse=True)
for i in range(n):
    print(height[i][1])
