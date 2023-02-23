n, x = map(int, input().split())
x = x * 100
alc = 0
for i in range(n):
    v, p = map(int, input().split())
    alc += v * p
    if alc > x:
        print(i + 1)
        quit()
print(-1)
