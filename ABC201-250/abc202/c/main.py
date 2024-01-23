from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
dictA = defaultdict(int)
dictC = defaultdict(int)

for i in range(n):
    dictA[a[i]] += 1
for i in range(n):
    dictC[c[i]] += 1
ans = 0
for i in range(n):
    if dictA[b[i]] > 0:
        ans += dictA[b[i]] * dictC[i + 1]
print(ans)
