l,m,n = list(map(int,input().split()))
if l == m and l == n:
    print(n)
    
elif l == m and l != n:
    print(n)
elif l!= m and m == n:
    print(l)
elif l==n and l!= m:
    print(m)
else:
    print(0)

#B
n,k= list(map(int,input().split()))
total = 0
for i in n:
    total += 1/2*k*(k+1) + 100*k*i
print(int(total))

#C
n,k = list(map(int,input().split()))

ab = []

for i in range(n):
    a,b = list(map(int,input().split()))
    ab.append([a, b])


