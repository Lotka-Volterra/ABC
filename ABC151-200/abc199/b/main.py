n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
amax = max(a)
bmin = min(b)
if bmin-amax+1 < 0:
    print(0)
else:
    print(bmin-amax+1)

# さらに短く
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
amax = max(a)
bmin = min(b)
print(max(0, bmin-amax+1))

# 全探索
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0
for i in range(1, 1001):
    ok = True
    for j in range(n):
        if i < a[j] or i > b[j]:
            ok = False
    if ok:
        res += 1

print(res)
