n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(4 * n - 1):
    if i % 4 == 2 and i != 4 * n - 2 and a[i] != a[i + 1]:
        print(a[i])
        quit()
print(n)
