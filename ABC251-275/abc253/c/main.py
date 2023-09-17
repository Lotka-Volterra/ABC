q= int(input())
s=[]
querry=[]
for i in range(q):
    querry.append(input())

for i in querry:
    qu=i[0]
    if qu=="1":
        qlist=i.split()
        s.append(int(qlist[1]))
    elif qu=="2":
        qlist=i.split()
        x=int(qlist[1])
        c=int(qlist[2])
        xcnt=s.count(x)
        minxc=min(xcnt,c)
        for j in range(minxc):
            s.remove(x)
    else:
        print(max(s)-min(s))

