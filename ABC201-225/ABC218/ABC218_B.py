p=list(map(int,input().split()))
ord_a=ord('a')
s=''
for i in range(26):
    s+=chr(ord_a+p[i]-1)
print(s)
