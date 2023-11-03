num = {}
n = int(input())
a = []
for i in range(n):
    ai = int(input())
    if ai not in num:
        num[ai] = 1
    elif num[ai] == 0:
        num[ai] = 1
    else:
        num[ai] = 0
    a.append(ai)

a = list(set(a))
ans = 0
for i in range(len(a)):
    if num[a[i]] == 1:
        ans += 1
print(ans)
