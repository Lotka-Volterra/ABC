n= int(input())
x= list(map(int,input().split()))
ans=100*100*100
for i in range(1,101):
    sum=0
    for j in x:
        sum+=(j-i)**2
    if sum<ans:
        ans=sum
print(ans)

# 別解
# 数学的に最小値を取る値を導き出す
# https://atcoder.jp/contests/abc156/editorial/7020