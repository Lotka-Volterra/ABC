n= int(input())
a= list(map(int,input().split()))
p=0
rui=[0 for i in range(4)]
for i in range(n):
    rui[0]=1
    sinrui=[0 for i in range(4)]
    for j in range(4):
        if rui[j]>0:
            if j+a[i]<4:
                rui[j]=0
                sinrui[j+a[i]]=1
            else:
                p+=1
                rui[j]=0
    for i in range(4):
        if sinrui[i]==1:
            rui[i]=1
print(p)
            

