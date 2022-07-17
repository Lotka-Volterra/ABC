n = int(input())

a = [0,0,1]
if n == 1 or n == 2:
    print(0)
elif n == 3:
    print(1)
if n >= 4:
    for i in range(n-3):
        a = [a[1],a[2],a[0]+a[1]+a[2]]
    print(a[2]%10007)

n = int(input())

a = [0,0,1]
if n == 1 or n == 2:
    print(0)
elif n == 3:
    print(1)
if n >= 4:
    for i in range(n-3):
        a = [a[1]%10007,a[2]%10007,(a[0]+a[1]+a[2])%10007]
        #print(a)
    print(a[2]%10007)