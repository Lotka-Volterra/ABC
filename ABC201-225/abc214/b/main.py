s,t= map(int,input().split())
count=0
for a in range(100):
    for b in range(100):
        for c in range(s-(a+b)+1):
            if a*b*c<=t:
                count+=1
print(count)