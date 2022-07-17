l = list(map(int, input().split()))
l.sort()
if l[0] != l[1]:
    print(l[0])
else:
    print(l[2])

#別解　要素数が１なら1とのANDでTrueになり、print()
a=list(map(int,input().split()))
for x in a:
    if a.count(x)&1:print(x);break
#bool(2&2)==True
#bool(1&2)==True
#bool(0&0)==False
#print(2&1) #0
#print(1&1) #1
#print(2&2) #2

#総当り
a,b,c= map(int,input().split())
if a==b:
    print(c)
elif b==c:
    print(a)
else:
    print(b)