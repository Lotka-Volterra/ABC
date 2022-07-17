N = int(input())
D = list(map(int,input().split()))
sum = 0
for i in range(N):
    for j in range(i+1,N):
        sum += D[i]*D[j]
print(sum)

#別解　リストDを２乗し、平方数を引くことで、異なる数の積だけが残る
n=int(input())
da=list(map(int,input().split()))
ans=0
for i in range(n):
    ans+=da[i]
ans*=ans
for i in range(n):
    ans-=da[i]**2
print(ans//2)