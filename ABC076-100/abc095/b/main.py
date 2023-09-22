n, x = map(int, input().split())
m = []
for i in range(n):
    mi = int(input())
    m.append(mi)
    x -= mi
m.sort()
print(n + x // m[0])
