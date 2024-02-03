s = input()
t = input()
slist = []
tlist = []
scount = 0
slen = len(s)
for i in range(slen):
    if i < slen-1 and s[i] == s[i+1]:
        scount += 1
    else:
        slist.append([s[i], scount+1])
        scount = 0
tcount = 0
tlen = len(t)
for i in range(tlen):
    if i < tlen-1 and t[i] == t[i+1]:
        tcount += 1
    else:
        tlist.append([t[i], tcount+1])
        tcount = 0
if len(slist) != len(tlist):
    print('No')
    quit()
for i in range(len(slist)):
    if slist[i][0] != tlist[i][0]:
        print('No')
        quit()
    if slist[i][1] != tlist[i][1]:
        if slist[i][1] > tlist[i][1]:
            print('No')
            quit()
        elif slist[i][1] < tlist[i][1] and slist[i][1] == 1:
            print('No')
            quit()
print('Yes')
