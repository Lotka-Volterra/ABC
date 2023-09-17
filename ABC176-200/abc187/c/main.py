n= int(input())
inashi=[]
iari=[]
for i in range(n):
    s=input()
    if s[0]=='!':
        iari.append(s)
    else:
        inashi.append(s)
inashi=set(inashi)
iari=set(iari)
for i in inashi:
    if '!'+i in iari:
        print(i)
        quit()
print('satisfiable')

#教訓：set使えば早くなる