n= int(input())
a0=list(map(int,input().split()))
a1=list(map(int,input().split()))
sums=[]
for i in range(n):
    a0sum=sum(a0[:i+1])
    a1sum=sum(a1[i:])
    sums.append(a0sum+a1sum)
print(max(sums))
