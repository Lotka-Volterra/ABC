n= int(input())
a=[]
for i in range(n):
    a.append(input())

mas=[]
for i in range(n):
    for j in range(n):
        tatesum=a[i][j]
        yokosum=a[i][j]
        hidarisum=a[i][j]
        migisum=a[i][j]
        s1=i
        s2=j
        tate=i
        yoko=j
        hidarii=i
        hidarij=j
        migii=i
        migij=j
        for k in range(n-1):
            tate+=1
            yoko+=1
            hidarii+=1
            hidarij+=1
            migii-=1
            migij+=1
            if tate>=n:
                tate=0
            if yoko>=n:
                yoko=0
            if hidarii>=n:
                hidarii=0
            if hidarij>=n:
                hidarij=0
            if migii<0:
                migii=n-1
            if migij>=n:
                migij=0
            tatesum+=a[tate][j]
            yokosum+=a[i][yoko]
            hidarisum+=a[hidarii][hidarij]
            migisum+=a[migii][migij]
        tatesumre = tatesum[::-1]
        yokosumre = yokosum[::-1]
        hidarisumre = hidarisum[::-1]
        migisumre = migisum[::-1]
        mas.append(tatesum)
        mas.append(yokosum)
        mas.append(hidarisum)
        mas.append(migisum)
        mas.append(tatesumre)
        mas.append(yokosumre)
        mas.append(hidarisumre)
        mas.append(migisumre)
print(max(mas))

