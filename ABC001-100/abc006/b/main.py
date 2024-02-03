a = [0, 0, 1]
n = int(input())
sum = 0
if n <= 3:
    print(a[n-1])
else:
    for i in range(3, n):
        sum = (a[0]+a[1]+a[2]) % 10007
        a[0] = a[1]
        a[1] = a[2]
        a[2] = sum
    print(sum)
#はじめて解いた緑diff問題