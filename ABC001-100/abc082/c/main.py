from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
setA = set(a)
dict = defaultdict(int)
for i in range(n):
    dict[a[i]] += 1
ans = 0
for i in setA:
    if dict[i] > i:
        ans += dict[i] - i
    elif dict[i] < i:
        ans += dict[i]
print(ans)
