n = int(input())
w = list(map(int, input().split()))
minw = 10**4
for i in range(1, n):
    s1 = w[:i]
    s2 = w[i:]
    minw = min(minw, abs(sum(s1) - sum(s2)))
print(minw)
