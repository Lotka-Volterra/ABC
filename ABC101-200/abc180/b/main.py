import math

n= int(input())
x= list(map(int,input().split()))
man=0
eu=0
cheby=[]
for i in range(n):
    xi=abs(x[i])
    man+=xi
    eu+=xi**2
    cheby.append(xi)
print(man)
print(math.sqrt(eu))
print(max(cheby))