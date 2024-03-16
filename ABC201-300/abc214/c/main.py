n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
tind = []
for i in range(n):
    tind.append([t[i], i])
tind.sort()
ans = [10**10] * n
ans[tind[0][1]] = tind[0][0]
pre = tind[0][1]
next = (tind[0][1] + 1) % n
for i in range(n - 1):
    ans[next] = min(ans[pre] + s[pre], t[next])
    pre = next
    next = (pre + 1) % n
for i in ans:
    print(i)
