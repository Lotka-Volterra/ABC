from collections import defaultdict, deque

n, k = map(int, input().split())
c = list(map(int, input().split()))
dict = defaultdict(int)
for i in range(k):
    dict[c[i]] += 1
ans = len(dict)
for i in range(k, n):
    dict[c[i - k]] -= 1
    if dict[c[i - k]] == 0:
        dict.pop(c[i - k])
    dict[c[i]] += 1
    ans = max(ans, len(dict))
print(ans)
