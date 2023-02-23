n,m= map(int,input().split())
a= list(map(int,input().split()))
b= list(map(int,input().split()))
count=0
for i in range(m):
    count+=a[b[i]-1]
print(count)