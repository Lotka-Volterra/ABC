n = int(input())
s = list(map(int, input().split()))
candidate = []
ans = 0
for a in range(1, 1001):
    for b in range(a, 1001):
        candidate.append(4 * a * b + 3 * a + 3 * b)
candidate = list(set(candidate))
ans = 0
for i in range(n):
    if s[i] not in candidate:
        ans += 1
print(ans)
