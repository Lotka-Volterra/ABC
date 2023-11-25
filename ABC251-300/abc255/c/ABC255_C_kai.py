x,a,d,n= map(int,input().split())
makko=a+d*(n-1)
if d==0:
    print(abs(x-a))
elif d>0:
    if x<a:
        print(a-x)
    elif x>makko:
        print(x-makko)
    else:
        i=(x-a)//d
        sa1=x-(a+d*i)
        sa2=a+d*(i+1)-x
        print(min(sa1,sa2))
else:
    if x<makko:
        print(makko-x)
    elif x>a:
        print(x-a)
    else:
        i=(x-a)//d
        sa1=(a+d*i)-x
        sa2=x-(a+d*(i+1))
        print(min(sa1,sa2))
#教訓　交差で場合分けするとわかりやすい。
# x-(a+d*(i+1))のように、時間がかかってもかっこをつける。x-a+d*(i+1)という間違いを防ぐ