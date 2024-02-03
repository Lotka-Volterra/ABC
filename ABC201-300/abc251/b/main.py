n,w= map(int,input().split())
a=list(map(int,input().split()))
la=len(a)
ol = []
if la==1:
    if a[0]<=w:
        print(1)
elif la ==2:
    count=0
    if a[0]<=w:
        count+=1
    if a[1]<=w:
        count+=1
    if a[1]+a[0]<=w:
        count+=1
    print(count)
else:
    for i in range(la-2):
        for j in range(i,la-1):
            for k in range(j,la):
                a3=a[i]+a[j]+a[k]
                a12 = a[i]+a[j]
                a23 = a[j]+a[k]
                a31= a[k]+a[i]
                omori = [a[i],a[j],a[k],a12,a23,a31,a3]
                for z in omori:
                    if z<=w:
                        ol.append(z)
    print(len(set(ol)))
            
n,w= map(int,input().split())
a=list(map(int,input().split()))
la=len(a)
ol = []
count = 0

if la==1:
    if a[0]<=w:
        count+=1
elif la ==2:
    if a[0]<=w:
        count+=1
    if a[1]<=w:
        count+=1
    if a[1]+a[0]<=w:
        count+=1
else:
    a.sort()
    for i in a:
        if i <=w:
            ol.append(i)
    lol=len(ol)
    cl=[]
    for i in range(lol-1):
        for j in range(i,lol):
            a12 = ol[i]+ol[j]
            if a12<=w:
                ol.append(a12)
                cl.append(ol[i])
                cl.append(ol[j])
    lcl=len(cl)
    for i in range(lcl-2):
        for j in range(i,lcl-1):
            for k in range(j,lcl):
                a123=cl[i]+cl[j]+cl[k]
                if a123<=w:
                    ol.append(a123)
    count+=len(set(ol))
print(count)

