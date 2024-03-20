n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
num = 0
for i in range(n):
    if a[i] == num:
        num += 1
print(min(num, k))
