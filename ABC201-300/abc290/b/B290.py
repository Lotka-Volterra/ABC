n,k= map(int,input().split())
s=input()
ans=''
count=0
for i in range(n):
    if s[i]=='o':
        if count<k:
            ans+='o'
            count+=1
        else:
            ans+='x'
    else:
        ans+='x'
print(ans)
