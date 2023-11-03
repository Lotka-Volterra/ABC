n = int(input())
c = []
a = []
for i in range(n):
    c.append(int(input()))
    a.append(list(map(int, input().split())))
x = int(input())
candidate = []
for i in range(n):
    if x in a[i]:
        candidate.append([len(a[i]), i + 1])
ans = []
candidate.sort()
if len(candidate) > 0:
    ans.append(candidate[0][1])
for i in range(1, len(candidate)):
    if candidate[i - 1][0] != candidate[i][0]:
        break
    ans.append(candidate[i][1])
print(len(ans))
print(*ans)
