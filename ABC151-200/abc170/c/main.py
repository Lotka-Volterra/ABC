x, n = map(int, input().split())
p = list(set(list(map(int, input().split()))))
ans = -1
dist = 101
for i in range(102):
    if i not in p and abs(x - i) < dist:
        ans = i
        dist = abs(x - i)
print(ans)
