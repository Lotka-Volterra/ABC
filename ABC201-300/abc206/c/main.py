from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
num = defaultdict(int)
for key in a:
    num[key] += 1
ans = 0
rest = n
for i in num:
    rest -= num[i]
    ans += num[i] * rest
print(ans)
