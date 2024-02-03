n= int(input())
a= list(map(int,input().split()))
m= int(input())
b= list(map(int,input().split()))
x= int(input())
dp=[0]*(x+1)
dp[0]=1
b = set(b)
for i in range(1,x+1):
    if i in b:
        continue
    else:
        for j in range(n):
            if i-a[j]>=0 and dp[i-a[j]]:
                dp[i]=1
                break
if dp[x]:
    print("Yes")
else:
    print("No")