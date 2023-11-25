n,m= map(int,input().split())
a=[]
c=[]
for i in range(m):
    c.append( int(input()))
    a.append( list(map(int,input().split())))
count=0
# iから(1<<n)-1まで全探索。
for i in range(1 << m):
    shutsugen=[]
    for j in range(m):
        wari = 1 << j
        
        if (i//wari) % 2 == 1:
            for k in range(len(a[j])):
                shutsugen.append(a[j][k])
            shutsugen=list(set(shutsugen))
    #print(shutsugen)
    if len(shutsugen)==n:
        count+=1
print(count)
    