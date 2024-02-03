n,w= map(int,input().split())
a=list(map(int,input().split()))
total=[]
#1個選ぶ
for i in range(n):
    if a[i]<=w:
        total.append(a[i])
#2個選ぶ
if len(a)>=2:
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]+a[j]<=w:
                total.append(a[i]+a[j])

#3個選ぶ
if len(a)>=3:
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if a[i]+a[j]+a[k]<=w:
                    total.append(a[i]+a[j]+a[k])
count=list(set(total))
print(len(count))
