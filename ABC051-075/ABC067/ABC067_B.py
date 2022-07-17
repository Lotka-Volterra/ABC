N,K = map(int,input().split())
L = list(map(int,input().split()))
L.sort(reverse=True)
length = 0
for i in range(K):
    length +=L[i]
print(length)

#別解　sumとスライスを組み合わせる
N,K = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
print(sum(l[-K:]))