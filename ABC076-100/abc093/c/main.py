a=list(map(int,input().split()))
odev=[]
a.sort()
for i in range(3):
    if a[i]%2==0:
        odev.append(0)
    else:
        odev.append(1)
sa1=a[1]-a[0]
sa2=a[2]-a[1]
if sum(odev)==0 or sum(odev)==3:
    print(sa1//2+sa2)
elif sum(odev)==1:
    kisu=odev.index(1)
    if kisu==2:
        print(sa1//2+sa2)
    elif kisu==1:
        sa3=a[2]+1-a[1]
        sa4=a[2]-a[0]
        print((sa3+sa4)//2+1)
    else:
        sa5=a[2]+1-a[0]
        print((sa5+sa2)//2+1)