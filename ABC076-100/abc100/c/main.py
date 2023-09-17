n= int(input())
a=list(map(int,input().split()))
a2=[]
for i in range(n):
    count=0
    ai=a[i]
    while ai%2==0:
        count+=1
        ai/=2
    a2.append(count)
print(sum(a2))

#2で割れる回数を知りたいので、各要素の素因数の数をわざわざリストに保存するのではなく、一つにまとめればいい
n= int(input())
a=list(map(int,input().split()))
count=0
for i in range(n):
    while a[i]%2==0:
        count+=1
        a[i]/=2
print(count)