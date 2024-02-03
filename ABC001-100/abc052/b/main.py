n= int(input())
s=input()
maxx=0
x=0
for i in range(n):
    if s[i]=="I":
        x+=1
    else:
        x-=1
    maxx=max(maxx,x)
print(maxx)