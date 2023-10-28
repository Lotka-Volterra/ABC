n = int(input())

a = []
modlist = []
for i in range(n):
    ai = int(input())
    a.append(ai)
    if ai % 10 != 0:
        modlist.append(ai)
modlist.sort()
ans = sum(a)
if ans % 10 == 0:
    if len(modlist) > 0:
        ans -= modlist[0]
    else:
        ans = 0

print(ans)
