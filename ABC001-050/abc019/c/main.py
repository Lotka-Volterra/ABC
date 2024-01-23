def special_factorization(N):
    if N % 2 == 1:
        return N
    else:
        while N % 2 == 0:
            N //= 2
        return N


n = int(input())
a = list(map(int, input().split()))
ans = set()
for i in range(n):
    ans.add(special_factorization(a[i]))
print(len(ans))
