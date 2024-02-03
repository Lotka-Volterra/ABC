n,m=  map(int,input().split())
if m!=0:
    a= list(map(int,input().split()))
else:
    a=[0]
midoku=1
keizokuflag=False
aindex=0
anslist=[]
for i in range(1,n+1):
    if a[aindex]==i:
        keizokuflag=True
        if aindex<m-1:
            aindex+=1
    else:
        if keizokuflag:
            keizokuflag=False
        for j in range(i,midoku-1,-1):
            anslist.append(j)
            midoku+=1
print(*anslist)