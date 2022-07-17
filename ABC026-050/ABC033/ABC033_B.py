N = int(input())
data = []
soujinko = 0
for i in range(N):
    S, T = map(str, input().split())
    T = int(T)
    soujinko += T
    data.append([T, S])
data.sort(reverse=True)
if data[0][0] > soujinko/2:
    print(data[0][1])
else:
    print("atcoder")

#ABC201と同じような解き方で解いた。以下別解。
#SとPというリストを別々に作り、インデックスで結びつける
n=int(input())
S=[]
P=[]
for _ in range(n):
    s,p=input().split()
    S.append(s)
    P.append(int(p))
if max(P)>sum(P)//2:
    print(S[P.index(max(P))])
else:
    print("atcoder")