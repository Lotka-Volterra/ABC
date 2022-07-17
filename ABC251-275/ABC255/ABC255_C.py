x,a,d,n= map(int,input().split())
makko=a+d*(n-1)
if x<a:
    if d>=0:
        print(x-a)
    else:
        #ここおかしい、必ずしも末項との差ではないはず
        print(min(abs(x-makko),abs(a-x)))
elif x>makko:
    if d>=0:
        print(x-makko)
    else:
        #ここおかしい、必ずしも初項との差ではないはず
        print(min(abs(x-makko),abs(a-x)))
else:
    if d>0:
        i=(x-a)//d
        sa1=x-(a+d*i)
        sa2=a+d*(i+1)-x
        print(min(sa1,sa2))
    elif d==0:
        print(x-a)
    else:
        i=(x-a)//d
        sa1=abs(x-(a+d*i))
        sa2=abs(a+d*(i+1)-x)
        print(min(sa1,sa2))
"""     for i in range(1,n+1):
        if a+d*(i-2)<x<=a+d*(i-1):
            dist.append(a+d*(i-1)-x)
        elif a+d(i-1)<x<a+d*i:
            dist.append(x-a+d(i-1)) """
    
