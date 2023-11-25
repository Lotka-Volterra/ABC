n = int(input())
a = list(map(int, input().split()))
buka = [0] * n
for i in range(n - 1):
    buka[a[i] - 1] += 1
for i in range(n):
    print(buka[i])
