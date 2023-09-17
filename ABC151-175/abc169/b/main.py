n= int(input())
a=list(map(int,input().split()))
ai=1
if min(a)==0:
    print(0)
    quit()
else:
    for i in range(n):
        ai*=a[i]
        if ai>10**18:
            print(-1)
            quit()
print(ai)