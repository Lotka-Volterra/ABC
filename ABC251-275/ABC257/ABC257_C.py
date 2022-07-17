n= int(input())
s= input()
w=list(map(int,input().split()))
strs=list(s)
child=strs.count('0')
adult=strs.count('1')
ws=[]
for i in range(n):
    ws.append([w[i],s[i]])
ws.sort()
setw=list(set(w))
wsc=[]
for i in range(len(setw)):
    wsc.append(setw[i],0,ws.count([setw[i],'0']))
    wsc.append(setw[i],1,ws.count([setw[i],'1']))
correctnum=[]
for i in range(len(setw)):
    childcount=0
    adultcount=0
