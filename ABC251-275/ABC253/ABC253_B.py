h,w= map(int,input().split())
ban = []
komah=[]
komaw=[]
for i in range(h):
    ban.append(input())
for i in range(h):
    for j in range(w):
        if ban[i][j]=="o":
            komah.append(i)
            komaw.append(j)
hdist=abs(komah[0]-komah[1])
wdist=abs(komaw[0]-komaw[1])
print(hdist+wdist)
