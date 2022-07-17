a,b= map(int,input().split())
count=0
for i in range(a,b+1):
    si=str(i)
    if si[:2]==si[4]+si[3]:
        count+=1
print(count)