n = int(input())
a = list(map(int, input().split()))
bunbo = 1
for i in range(n):
    bunbo *= a[i]
bunshi = 0
for i in range(n):
    bunshi += bunbo // a[i]
print(bunbo / bunshi)
