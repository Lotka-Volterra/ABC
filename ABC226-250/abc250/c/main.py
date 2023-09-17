n,q= map(int,input().split())
qlist=[]
x=[]
for i in range(1,n+1):
    x.append(i)

for i in range(q):
    qlist.append( int(input()))

for i in range(q):
    y=x.index(qlist[i])+1
    if y>n-1:
        y = x.index(qlist[i])-1
        z = x[y]
        x[y]=x[y+1]
        x[y+1]=z
    else:
        z=x[y]
        x[y-1]=z
print(*x)
