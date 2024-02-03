n,q= map(int,input().split())
s=input()
query=[]
""" sumquery=[]
sumquery.append(0)
for i in range(q):
    t,x= map(int,input().split())
    query.append([t,x]) """

""" xsum=0
for i in range(q):
    if query[i][0]==1:
        xsum+=query[i][1]
    else:
        xmod=xsum%n
        s=s[n-xmod:]+s[:n-xmod]
        print(s[query[i][1]-1])
        xsum=0 """
xsum=0
for i in range(q):
    t,x= map(int,input().split())
    if t==1:
        xsum+=x
    else:
        xmod=xsum%n
        s=s[n-xmod:]+s[:n-xmod]
        print(s[x-1])
        xsum=0 
