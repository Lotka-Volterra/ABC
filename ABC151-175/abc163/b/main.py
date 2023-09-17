N,M= map(int,input().split())
A = list(map(int,input().split()))

sumA = sum(A)
subA = N - sumA
if subA < 0:
    print(-1)
else:
    print(subA)

#別解
print(max(N - sum(A), -1))