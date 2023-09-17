def searchList(a,index):
    return a[index]

a= list(map(int,input().split()))
b1=searchList(a,0)
b2=searchList(a,b1)
print(searchList(a,b2))

#簡潔に
a= list(map(int,input().split()))
print(a[a[a[0]]])