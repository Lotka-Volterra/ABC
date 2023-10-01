n = int(input())
check = [0] * n
a = list(map(int, input().split()))
for i in range(n):
    check[a[i] - 1] += 1
for i in range(n):
    if check[i] != 1:
        print("No")
        quit()
print("Yes")
