n = int(input())
a = list(map(int, input().split()))
baisu4 = 0
kisu = 0
for i in range(n):
    if a[i] % 4 == 0:
        baisu4 += 1
    elif a[i] % 2 == 1:
        kisu += 1
# 4の倍数が奇数以上あればOK
if baisu4 >= kisu:
    print("Yes")
# 4の倍数が奇数より1個少なくても、他に4の倍数でない偶数がなければOK
elif baisu4 + 1 == kisu and baisu4 + kisu == n:
    print("Yes")
else:
    print("No")
