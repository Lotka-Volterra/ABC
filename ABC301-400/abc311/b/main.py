n, d = map(int, input().split())
days = [0] * d
for i in range(n):
    s = input()
    for i in range(d):
        if s[i] == "o":
            days[i] += 1
ans = 0
count = 0
for i in range(d):
    if days[i] == n:
        count += 1
    else:
        count = 0
    ans = max(ans, count)
print(ans)
