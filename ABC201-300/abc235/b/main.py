n = int(input())
h = list(map(int, input().split()))
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        print(h[i])
        quit()
print(h[n - 1])
