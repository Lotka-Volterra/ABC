n,m= map(int,input().split())
ab=[[]for i in range(n)]
for i in range(m):
    a,b= map(int,input().split())
    ab[a-1].append(b)
    ab[b-1].append(a)
for i in range(n):
    if len(ab[i])!=0:
        print(len(ab[i]),end=" ")
        print(*sorted(ab[i]))
    else:
        print(0)