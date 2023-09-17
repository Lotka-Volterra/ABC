h1,h2,h3,w1,w2,w3= map(int,input().split())
count=0
hw=[h1,h2,h3,w1,w2,w3]
maxhw=max(hw)
for i in range(1,maxhw-1):
    for j in range(1,maxhw-1):
        for k in range(1,maxhw-1):
            for l in range(1,maxhw-1):
                a=i
                b=j
                c=k
                d=l
                e=h1-a-b
                f=h2-c-d
                g=w1-a-c
                h=w2-b-d
                hi=h3-g-h
                wi=w3-e-f
                if min(e,f,g,h,hi,wi)<1:
                    continue
                if hi!=wi:
                    continue
                count+=1
print(count)
