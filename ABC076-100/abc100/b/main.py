d, n = map(int, input().split())
if d == 0:
    if n == 100:
        print(101)
    else:
        print(n)
elif d == 1:
    if n == 100:
        print(10100)
    else:
        print(100*n)
else:
    if n == 100:
        print(1010000)
    else:
        print(10000*n)

#短く
d,n= map(int,input().split())
if n==100:
    n=101
print(str(n)+'00'*d)
