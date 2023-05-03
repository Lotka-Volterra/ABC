n= int(input())
x= list(map(int,input().split()))
x.sort()
xslice=x[n:4*n]
print(sum(xslice)/(3*n))