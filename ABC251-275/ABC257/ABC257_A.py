
n,x= map(int,input().split())

r='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s=''
for i in range(26):
    s+=r[i]*n
print(s[x-1])
