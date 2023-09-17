s = int(input())
k = int(input())

strS = str(s)
slist = []
for i in range(len(strS)):
    if strS[i] == '1':
        slist.append([strS[i], 1])
    else:
        slist.append([strS[i], int(strS[i])*5000*(10**12)])

count = 0

for i in range(len(strS)):
    count += slist[i][1]
    if count >= k:
        print(slist[i][0])
        quit()
