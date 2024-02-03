n, w = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
ab.sort(reverse=True)
ans = 0
total = 0
for i in range(n):
    if total == w:
        break
    for j in range(ab[i][1]):
        if total == w:
            break
        ans += ab[i][0]
        total += 1
print(ans)
