from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
q = int(input())
num = defaultdict(int)
for i in range(n):
    num[a[i]] += 1
ans = sum(a)
for i in range(q):
    b, c = map(int, input().split())
    num_b = num[b]
    ans -= num_b * b
    num[b] = 0
    ans += num_b * c
    num[c] += num_b
    print(ans)
