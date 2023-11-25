n= int(input())
blue=[]
for i in range(n):
    blue.append(input())
m= int(input())
red=[]
for i in range(m):
    red.append(input())
point=[]

blueset=list(set(blue))

for i in range(len(blueset)):
    bluecnt=blue.count(blueset[i])
    redcnt=red.count(blueset[i])
    point.append(bluecnt-redcnt)
print(max(max(point),0))

