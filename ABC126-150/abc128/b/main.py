n= int(input())
s=[]
p=[]
for i in range(n):
    si,pi= input().split()
    s.append(si)
    p.append(int(pi))
sets=list(set(s))
sets.sort()
for i in sets:
    data=[]
    for j in range(n):
        if s[j]==i:
            data.append([p[j],j])
    data.sort(reverse=True)
    for j in range(len(data)):
        print(data[j][1]+1)

#点数は、自然数だから、高い方から→降順。しかし、負に変換すると、市名と一緒に昇順ソートができる。
#インデックスも一緒に格納しているのもミソ
N = int(input())
a = []
for i in range(N):
    N, K = input().split()
    K = int(K)
    a.append([N, -K, i+1])
a.sort()
for a_ in a:
    print(a_[2])


