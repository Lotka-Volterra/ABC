n = int(input())
a = [0]
for i in range(n):
    a.append(int(input()))
litButton = 1
pushCount = 0
while pushCount < n:
    litButton = a[litButton]
    pushCount += 1
    if litButton == 2:
        break
if pushCount == n:
    print(-1)
else:
    print(pushCount)
